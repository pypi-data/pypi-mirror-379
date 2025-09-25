import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
from pathlib import Path
import traceback
import pickle
import gzip
import io
from typing import Tuple, Dict, Any, List
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LAMMPSFileParser:
    """Parser especializado para archivos LAMMPS dump"""
    
    def __init__(self):
        self.supported_extensions = ['.dump', '.dump.gz', '.lammpstrj', '.lammpstrj.gz']
        self.ATM_TOTAL = 16384  # Configuración por defecto
    
    def _open_file(self, path: str):
        """Abrir archivo, detectando si está comprimido"""
        p = Path(path)
        if p.suffix == ".gz":
            return io.TextIOWrapper(gzip.open(p, "rb"), encoding="utf-8", newline="")
        return open(p, "r", encoding="utf-8", newline="")
    
    def parse_last_frame(self, path: str) -> Tuple[pd.DataFrame, int, Dict[str, Any]]:
        """Parser robusto del último frame de un archivo LAMMPS dump"""
        try:
            with self._open_file(path) as f:
                lines = f.read().splitlines()
        except Exception as e:
            raise RuntimeError(f"Error leyendo archivo {path}: {str(e)}")
        
        # Buscar la última sección ATOMS
        atoms_indices = [i for i, line in enumerate(lines) 
                        if line.startswith("ITEM: ATOMS")]
        
        if not atoms_indices:
            raise RuntimeError(f"No se encontró 'ITEM: ATOMS' en {path}")
        
        start_idx = atoms_indices[-1]
        
        # Extraer metadata del frame
        metadata = self._extract_metadata(lines, start_idx)
        
        # Parsear header de átomos
        header_line = lines[start_idx].replace("ITEM: ATOMS", "").strip()
        columns = header_line.split()
        
        if not columns:
            raise RuntimeError(f"Header de ATOMS vacío en {path}")
        
        # Determinar número de átomos
        n_atoms = self._find_num_atoms(lines, start_idx, metadata)
        
        if n_atoms <= 0:
            raise RuntimeError(f"Número inválido de átomos ({n_atoms}) en {path}")
        
        # Parsear datos de átomos
        df = self._parse_atomic_data(lines, start_idx + 1, n_atoms, columns)
        
        if df.empty:
            raise RuntimeError(f"No se pudieron extraer datos de átomos de {path}")
        
        logger.debug(f"Parseado {Path(path).name}: {len(df)} átomos, {len(df.columns)} columnas")
        
        return df, len(df), metadata
    
    def _extract_metadata(self, lines: List[str], atoms_start: int) -> Dict[str, Any]:
        """Extraer metadata del frame"""
        metadata = {}
        
        # Buscar timestep
        for i in range(max(0, atoms_start - 20), atoms_start):
            if i < len(lines) and "ITEM: TIMESTEP" in lines[i]:
                try:
                    if i + 1 < len(lines):
                        metadata['timestep'] = int(lines[i + 1])
                except (IndexError, ValueError):
                    pass
                break
        
        # Buscar box bounds
        for i in range(max(0, atoms_start - 20), atoms_start):
            if i < len(lines) and "ITEM: BOX BOUNDS" in lines[i]:
                try:
                    # Leer 3 líneas de bounds
                    bounds = []
                    for j in range(3):
                        line_idx = i + 1 + j
                        if line_idx < len(lines):
                            bounds.append(lines[line_idx].split())
                        else:
                            break
                    if len(bounds) == 3:  # Solo agregar si tenemos todas las bounds
                        metadata['box_bounds'] = bounds
                except (IndexError, ValueError):
                    pass
                break
        
        return metadata
    
    def _find_num_atoms(self, lines: List[str], atoms_start: int, metadata: Dict) -> int:
        """Determinar número de átomos en el frame"""
        # Buscar "ITEM: NUMBER OF ATOMS"
        for i in range(max(0, atoms_start - 20), atoms_start):
            if i < len(lines) and "ITEM: NUMBER OF ATOMS" in lines[i]:
                try:
                    if i + 1 < len(lines):
                        return int(lines[i + 1])
                except (IndexError, ValueError):
                    pass
        
        # Si no se encuentra, calcular hasta la siguiente sección
        data_start = atoms_start + 1
        count = 0
        for i in range(data_start, len(lines)):
            line = lines[i].strip()
            if not line or line.startswith("ITEM:"):
                break
            count += 1
        
        return count
    
    def _parse_atomic_data(self, lines: List[str], start_idx: int, n_atoms: int, columns: List[str]) -> pd.DataFrame:
        """Parsear datos atómicos"""
        data_rows = []
        
        for i in range(start_idx, min(start_idx + n_atoms, len(lines))):
            line = lines[i].strip()
            if not line:
                continue
            
            parts = line.split()
            if len(parts) >= len(columns):
                try:
                    row = []
                    for j, part in enumerate(parts[:len(columns)]):
                        try:
                            row.append(float(part))
                        except ValueError:
                            row.append(np.nan)
                    data_rows.append(row)
                except Exception as e:
                    logger.warning(f"Error parseando línea {i}: {line[:50]}...")
                    continue
        
        if not data_rows:
            return pd.DataFrame()
        
        df = pd.DataFrame(data_rows, columns=columns)
        df = df.replace([np.inf, -np.inf], np.nan)
        
        return df

class DumpFeatureExtractor:
    """Extractor de features desde archivos dump procesados"""
    
    def __init__(self):
        self.ATM_TOTAL = 16384
        self.ENERGY_BINS = 10
        self.ENERGY_MIN = -4.0
        self.ENERGY_MAX = -3.0
    
    def extract_features(self, atomic_df: pd.DataFrame, filename: str = "") -> pd.Series:
        """Extraer features para ML desde datos atómicos"""
        if atomic_df.empty:
            raise ValueError("DataFrame atómico vacío, no se pueden extraer features")
        
        features = {}
        
        # Basic atom statistics
        features['n_atoms'] = len(atomic_df)
        
        # Features basadas en energía (si existe columna 'c_pe')
        if 'c_pe' in atomic_df.columns:
            energies = atomic_df['c_pe'].dropna()
            if len(energies) > 0:
                features.update({
                    'energy_mean': energies.mean(),
                    'energy_std': energies.std() if len(energies) > 1 else 0.0,
                    'energy_min': energies.min(),
                    'energy_max': energies.max(),
                    'energy_q25': energies.quantile(0.25),
                    'energy_q75': energies.quantile(0.75),
                    'energy_range': energies.max() - energies.min()
                })
                
                # Distribución de energía en bins
                try:
                    energy_hist, _ = np.histogram(energies, bins=self.ENERGY_BINS, 
                                                range=(self.ENERGY_MIN, self.ENERGY_MAX))
                    for i, count in enumerate(energy_hist):
                        features[f'energy_bin_{i}'] = count
                except Exception as e:
                    logger.warning(f"Error calculando histograma de energía: {e}")
                    # Agregar bins vacíos como fallback
                    for i in range(self.ENERGY_BINS):
                        features[f'energy_bin_{i}'] = 0
        
        # Features espaciales (si existen coordenadas x, y, z)
        coord_cols = [col for col in ['x', 'y', 'z'] if col in atomic_df.columns]
        if coord_cols:
            for col in coord_cols:
                coords = atomic_df[col].dropna()
                if len(coords) > 0:
                    features.update({
                        f'{col}_mean': coords.mean(),
                        f'{col}_std': coords.std() if len(coords) > 1 else 0.0,
                        f'{col}_range': coords.max() - coords.min()
                    })
        
        # Features de tipo de átomo (si existe columna 'type')
        if 'type' in atomic_df.columns:
            type_counts = atomic_df['type'].value_counts()
            total_atoms = len(atomic_df)
            for atom_type, count in type_counts.items():
                features[f'type_{atom_type}_count'] = count
                features[f'type_{atom_type}_fraction'] = count / total_atoms if total_atoms > 0 else 0.0
        
        # Features de velocidad (si existen vx, vy, vz)
        vel_cols = [col for col in ['vx', 'vy', 'vz'] if col in atomic_df.columns]
        if vel_cols:
            for col in vel_cols:
                velocities = atomic_df[col].dropna()
                if len(velocities) > 0:
                    features.update({
                        f'{col}_mean': velocities.mean(),
                        f'{col}_std': velocities.std() if len(velocities) > 1 else 0.0,
                        f'speed_{col}': np.sqrt((velocities**2).mean())  # RMS velocity
                    })
        
        # Calcular vacancies estimadas (diferencia con ATM_TOTAL)
        estimated_vacancies = max(0, self.ATM_TOTAL - len(atomic_df))
        features['estimated_vacancies'] = estimated_vacancies
        
        # Metadata del archivo
        features['file'] = filename
        
        return pd.Series(features)

class PredictorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔮 Predictor de Vacancies - Extendido con Dump Processor")
        self.root.geometry("1200x800")
        
        # Variables para almacenar datos
        self.csv_path = None
        self.model_path = None
        self.df = None
        self.model = None
        self.feature_columns = None
        self.scaler = None
        self.predictions_df = None
        
        # Variables para dump processing
        self.dump_files = []
        self.processed_dump_df = None
        self.dump_model = None
        self.dump_model_path = None
        self.dump_predictions = None
        
        # Referencias a widgets
        self.predict_btn = None
        self.save_btn = None
        self.csv_label = None
        self.model_label = None
        
        # Herramientas de procesamiento
        self.parser = LAMMPSFileParser()
        self.feature_extractor = DumpFeatureExtractor()
        
        self.create_widgets()
        self.setup_style()
    
    def setup_style(self):
        """Configurar estilos visuales"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar colores para los labels de estado
        style.configure("Success.TLabel", foreground="green")
        style.configure("Error.TLabel", foreground="red")
        style.configure("Warning.TLabel", foreground="orange")
    
    def create_widgets(self):
        # Frame principal con scroll
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill="both", expand=True)
        
        # Título
        title_label = ttk.Label(main_frame, text="🔮 Predictor de Vacancies ML - Extendido", 
                               font=("Arial", 18, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Frame de controles principal (CSV/Model clásico)
        control_frame = ttk.LabelFrame(main_frame, text="📂 Controles Clásicos (CSV + Modelo)", padding="15")
        control_frame.pack(fill="x", pady=(0, 15))
        
        # Botones de carga clásicos
        btn_frame = ttk.Frame(control_frame)
        btn_frame.pack(fill="x", pady=5)
        
        ttk.Button(btn_frame, text="📄 Cargar CSV", 
                  command=self.load_csv, width=18).pack(side="left", padx=(0, 10))
        ttk.Button(btn_frame, text="🤖 Cargar Modelo", 
                  command=self.load_model, width=18).pack(side="left", padx=(0, 10))
        
        # Botón de predicción clásico
        self.predict_btn = ttk.Button(btn_frame, text="🔮 Predecir CSV", 
                                     command=self.predict, width=15, state="disabled")
        self.predict_btn.pack(side="left", padx=(0, 10))
        
        # Botón de guardar clásico
        self.save_btn = ttk.Button(btn_frame, text="💾 Guardar", 
                                  command=self.save_results, width=15, state="disabled")
        self.save_btn.pack(side="left")
        
        # Info de archivos cargados
        info_frame = ttk.Frame(control_frame)
        info_frame.pack(fill="x", pady=(10, 0))
        
        self.csv_label = ttk.Label(info_frame, text="📄 CSV: No cargado")
        self.csv_label.pack(anchor="w", pady=2)
        
        self.model_label = ttk.Label(info_frame, text="🤖 Modelo: No cargado")
        self.model_label.pack(anchor="w", pady=2)
        
        # Progress bar
        self.progress_frame = ttk.Frame(main_frame)
        self.progress_frame.pack(fill="x", pady=(0, 10))
        
        self.progress = ttk.Progressbar(self.progress_frame, mode='indeterminate')
        self.progress_label = ttk.Label(self.progress_frame, text="")
        
        # Pestañas para resultados
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill="both", expand=True)
        
        # Pestañas existentes
        self.create_info_tab()
        self.create_results_tab()
        self.create_viz_tab()
        self.create_stats_tab()
        
        # Nueva pestaña para dump processing
        self.create_dump_processor_tab()
    
    def create_dump_processor_tab(self):
        """Crear pestaña para procesamiento de archivos dump"""
        dump_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(dump_frame, text="🔥 Dump Processor")
        
        # Frame superior de controles
        control_frame = ttk.LabelFrame(dump_frame, text="🔥 Procesamiento de Archivos LAMMPS Dump", padding="10")
        control_frame.pack(fill="x", pady=(0, 10))
        
        # Primera fila de botones
        btn_row1 = ttk.Frame(control_frame)
        btn_row1.pack(fill="x", pady=5)
        
        ttk.Button(btn_row1, text="📁 Cargar Dumps", 
                  command=self.load_dump_files, width=15).pack(side="left", padx=(0, 10))
        ttk.Button(btn_row1, text="🔄 Procesar a CSV", 
                  command=self.process_dumps_to_csv, width=15).pack(side="left", padx=(0, 10))
        ttk.Button(btn_row1, text="🤖 Cargar Modelo ML", 
                  command=self.load_dump_model, width=15).pack(side="left", padx=(0, 10))
        
        # Segunda fila de botones
        btn_row2 = ttk.Frame(control_frame)
        btn_row2.pack(fill="x", pady=5)
        
        self.dump_predict_btn = ttk.Button(btn_row2, text="🔮 Predecir Dump", 
                                          command=self.predict_from_dumps, width=15, state="disabled")
        self.dump_predict_btn.pack(side="left", padx=(0, 10))
        
        self.dump_save_btn = ttk.Button(btn_row2, text="💾 Guardar Resultados", 
                                       command=self.save_dump_results, width=18, state="disabled")
        self.dump_save_btn.pack(side="left", padx=(0, 10))
        
        ttk.Button(btn_row2, text="📊 Exportar CSV Features", 
                  command=self.export_dump_csv, width=18).pack(side="left")
        
        # Labels de estado
        status_frame = ttk.Frame(control_frame)
        status_frame.pack(fill="x", pady=(10, 0))
        
        self.dump_files_label = ttk.Label(status_frame, text="📁 Archivos dump: Ninguno cargado")
        self.dump_files_label.pack(anchor="w", pady=2)
        
        self.dump_model_label = ttk.Label(status_frame, text="🤖 Modelo dump: No cargado")
        self.dump_model_label.pack(anchor="w", pady=2)
        
        self.dump_status_label = ttk.Label(status_frame, text="⏳ Estado: Listo para cargar archivos")
        self.dump_status_label.pack(anchor="w", pady=2)
        
        # Área de resultados
        results_frame = ttk.LabelFrame(dump_frame, text="📊 Resultados del Procesamiento", padding="10")
        results_frame.pack(fill="both", expand=True)
        
        self.dump_results_text = scrolledtext.ScrolledText(results_frame, height=15, wrap='word',
                                                          font=("Consolas", 10))
        self.dump_results_text.pack(fill="both", expand=True)
        
        # Mensaje inicial
        welcome_dump = """🔥 DUMP PROCESSOR - PREDICCIÓN DE VACANCIES
=====================================================

💡 FUNCIONALIDAD:
Este módulo procesa archivos LAMMPS dump (.dump, .dump.gz) para:

🔹 Extraer features automáticamente de archivos dump
🔹 Convertir datos atómicos a formato CSV con features ML
🔹 Predecir vacancies usando modelos entrenados
🔹 Exportar resultados y datasets generados

📋 PASOS PARA USAR:
1️⃣ Cargar archivos dump (puedes seleccionar múltiples)
2️⃣ Procesar dumps a CSV (extrae features automáticamente)
3️⃣ Cargar modelo ML entrenado (.joblib)
4️⃣ Predecir vacancies desde los dumps
5️⃣ Exportar resultados y datasets

🔧 FEATURES EXTRAÍDAS AUTOMÁTICAMENTE:
• Estadísticas de energía (media, std, quantiles, distribución)
• Estadísticas espaciales (x, y, z: media, std, rango)
• Conteos por tipo de átomo
• Features de velocidad (si disponibles)
• Estimación inicial de vacancies

⚡ FORMATOS SOPORTADOS:
• .dump, .dump.gz
• .lammpstrj, .lammpstrj.gz

🚀 ¡Comienza cargando tus archivos dump!
"""
        self.dump_results_text.insert(1.0, welcome_dump)
    
    def load_dump_files(self):
        """Cargar archivos dump"""
        file_paths = filedialog.askopenfilenames(
            title="Seleccionar archivos LAMMPS dump",
            filetypes=[
                ("LAMMPS dump files", "*.dump *.dump.gz *.lammpstrj *.lammpstrj.gz"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if file_paths:
            self.dump_files = list(file_paths)
            self.dump_files_label.config(
                text=f"📁 Archivos dump: {len(self.dump_files)} archivos cargados", 
                style="Success.TLabel"
            )
            
            self.dump_status_label.config(
                text="⏳ Estado: Archivos cargados, listo para procesar", 
                style="Success.TLabel"
            )
            
            # Mostrar lista de archivos en el área de resultados
            files_info = "🔥 ARCHIVOS DUMP CARGADOS\n" + "="*50 + "\n\n"
            files_info += f"📊 Total de archivos: {len(self.dump_files)}\n\n"
            files_info += "📁 ARCHIVOS:\n"
            
            for i, filepath in enumerate(self.dump_files, 1):
                filename = Path(filepath).name
                filesize = Path(filepath).stat().st_size / (1024*1024)  # MB
                files_info += f"   {i:2d}. {filename} ({filesize:.1f} MB)\n"
            
            files_info += f"\n✅ Archivos listos para procesar\n"
            files_info += "🔄 Haz clic en 'Procesar a CSV' para extraer features"
            
            self.dump_results_text.delete(1.0, tk.END)
            self.dump_results_text.insert(1.0, files_info)
    
    def process_dumps_to_csv(self):
        """Procesar archivos dump y convertir a CSV con features"""
        if not self.dump_files:
            messagebox.showwarning("Advertencia", "Primero carga archivos dump")
            return
        
        try:
            self.show_progress("Procesando archivos dump...")
            self.dump_status_label.config(text="⏳ Estado: Procesando archivos dump...", 
                                        style="Warning.TLabel")
            
            all_features = []
            failed_files = []
            
            for i, dump_file in enumerate(self.dump_files):
                try:
                    # Actualizar progreso
                    self.progress_label.config(text=f"Procesando archivo {i+1}/{len(self.dump_files)}: {Path(dump_file).name}")
                    self.root.update()
                    
                    # Parsear archivo dump
                    atomic_df, n_atoms, metadata = self.parser.parse_last_frame(dump_file)
                    
                    # Extraer features
                    features = self.feature_extractor.extract_features(atomic_df, Path(dump_file).name)
                    all_features.append(features)
                    
                    logger.info(f"Procesado exitosamente: {Path(dump_file).name} ({n_atoms} átomos)")
                    
                except Exception as e:
                    failed_files.append((dump_file, str(e)))
                    logger.error(f"Error procesando {dump_file}: {str(e)}")
                    continue
            
            if not all_features:
                raise RuntimeError("No se pudieron procesar archivos dump")
            
            # Crear DataFrame con todas las features
            self.processed_dump_df = pd.DataFrame(all_features)
            
            # Reordenar columnas (file primero, luego features)
            cols = ['file'] + [col for col in self.processed_dump_df.columns if col != 'file']
            self.processed_dump_df = self.processed_dump_df[cols]
            
            # Actualizar estado
            self.dump_status_label.config(
                text=f"✅ Estado: {len(all_features)} archivos procesados exitosamente", 
                style="Success.TLabel"
            )
            
            # Mostrar resultados
            self.show_dump_processing_results(failed_files)
            
            # Verificar si podemos predecir
            self.check_dump_prediction_ready()
            
        except Exception as e:
            self.dump_status_label.config(text="❌ Estado: Error en procesamiento", style="Error.TLabel")
            messagebox.showerror("Error", f"Error procesando dumps:\n{str(e)}\n\n{traceback.format_exc()}")
        finally:
            self.hide_progress()
    
    def show_dump_processing_results(self, failed_files):
        """Mostrar resultados del procesamiento"""
        if self.processed_dump_df is None:
            return
        
        results_text = "🔥 PROCESAMIENTO DE DUMPS COMPLETADO\n" + "="*50 + "\n\n"
        
        # Estadísticas generales
        results_text += f"📊 RESUMEN:\n"
        results_text += f"   • Archivos procesados exitosamente: {len(self.processed_dump_df)}\n"
        results_text += f"   • Features extraídas por archivo: {len(self.processed_dump_df.columns)-1}\n"  # -1 por 'file'
        results_text += f"   • Archivos fallidos: {len(failed_files)}\n\n"
        
        # Features disponibles
        feature_cols = [col for col in self.processed_dump_df.columns if col != 'file']
        results_text += f"🔧 FEATURES EXTRAÍDAS ({len(feature_cols)}):\n"
        
        # Agrupar features por categoría
        energy_features = [f for f in feature_cols if 'energy' in f]
        spatial_features = [f for f in feature_cols if any(coord in f for coord in ['x_', 'y_', 'z_'])]
        type_features = [f for f in feature_cols if 'type_' in f]
        velocity_features = [f for f in feature_cols if any(vel in f for vel in ['vx', 'vy', 'vz', 'speed'])]
        other_features = [f for f in feature_cols if f not in energy_features + spatial_features + type_features + velocity_features]
        
        if energy_features:
            results_text += f"   🔋 Energía ({len(energy_features)}): {', '.join(energy_features[:5])}"
            if len(energy_features) > 5:
                results_text += f" ... y {len(energy_features)-5} más"
            results_text += "\n"
        
        if spatial_features:
            results_text += f"   📐 Espaciales ({len(spatial_features)}): {', '.join(spatial_features[:5])}"
            if len(spatial_features) > 5:
                results_text += f" ... y {len(spatial_features)-5} más"
            results_text += "\n"
        
        if type_features:
            results_text += f"   🧬 Tipos de átomo ({len(type_features)}): {', '.join(type_features[:5])}"
            if len(type_features) > 5:
                results_text += f" ... y {len(type_features)-5} más"
            results_text += "\n"
        
        if velocity_features:
            results_text += f"   🚀 Velocidad ({len(velocity_features)}): {', '.join(velocity_features[:3])}"
            if len(velocity_features) > 3:
                results_text += f" ... y {len(velocity_features)-3} más"
            results_text += "\n"
        
        if other_features:
            results_text += f"   📊 Otros ({len(other_features)}): {', '.join(other_features[:3])}"
            if len(other_features) > 3:
                results_text += f" ... y {len(other_features)-3} más"
            results_text += "\n"
        
        # Estadísticas de vacancies estimadas
        if 'estimated_vacancies' in self.processed_dump_df.columns:
            vac_stats = self.processed_dump_df['estimated_vacancies'].describe()
            results_text += f"\n🔍 ESTADÍSTICAS DE VACANCIES ESTIMADAS:\n"
            results_text += f"   • Mínimo: {vac_stats['min']:.0f}\n"
            results_text += f"   • Máximo: {vac_stats['max']:.0f}\n"
            results_text += f"   • Media: {vac_stats['mean']:.1f}\n"
            results_text += f"   • Desviación: {vac_stats['std']:.1f}\n"
        
        # Primeras filas como ejemplo
        results_text += f"\n📋 PRIMERAS 3 FILAS DEL DATASET:\n"
        display_cols = ['file', 'n_atoms', 'estimated_vacancies']
        if 'energy_mean' in self.processed_dump_df.columns:
            display_cols.append('energy_mean')
        if 'energy_std' in self.processed_dump_df.columns:
            display_cols.append('energy_std')
        
        available_cols = [col for col in display_cols if col in self.processed_dump_df.columns]
        results_text += self.processed_dump_df[available_cols].head(3).to_string()
        
        # Archivos fallidos
        if failed_files:
            results_text += f"\n\n⚠️ ARCHIVOS FALLIDOS ({len(failed_files)}):\n"
            for failed_file, error in failed_files[:5]:  # Mostrar solo los primeros 5
                results_text += f"   • {Path(failed_file).name}: {error[:100]}...\n"
            if len(failed_files) > 5:
                results_text += f"   ... y {len(failed_files)-5} errores más\n"
        
        results_text += f"\n✅ Dataset listo para predicción ML"
        results_text += f"\n💾 Usa 'Exportar CSV Features' para guardar el dataset"
        
        self.dump_results_text.delete(1.0, tk.END)
        self.dump_results_text.insert(1.0, results_text)
    
    def load_dump_model(self):
        """Cargar modelo para predicciones desde dump"""
        file_path = filedialog.askopenfilename(
            title="Seleccionar modelo .joblib para dumps",
            filetypes=[("Joblib files", "*.joblib"), ("Todos los archivos", "*.*")]
        )
        
        if file_path:
            try:
                self.show_progress("Cargando modelo para dumps...")
                
                self.dump_model_path = file_path
                model_data = joblib.load(file_path)
                
                # Manejar diferentes formatos de modelo
                if isinstance(model_data, dict):
                    self.dump_model = model_data["model"]
                    self.dump_feature_columns = model_data.get("feature_columns", None)
                    self.dump_scaler = model_data.get("scaler", None)
                else:
                    self.dump_model = model_data
                    self.dump_feature_columns = None
                    self.dump_scaler = None
                
                self.dump_model_label.config(
                    text=f"🤖 Modelo dump: {Path(file_path).name}", 
                    style="Success.TLabel"
                )
                
                # Mostrar info del modelo cargado
                model_info = f"\n\n🤖 MODELO ML CARGADO PARA DUMPS\n" + "="*40 + "\n"
                model_info += f"📁 Archivo: {Path(file_path).name}\n"
                model_info += f"🧠 Tipo: {type(self.dump_model).__name__}\n"
                
                if self.dump_feature_columns:
                    model_info += f"🔧 Features requeridas: {len(self.dump_feature_columns)}\n"
                    model_info += f"📋 Features: {', '.join(self.dump_feature_columns[:10])}"
                    if len(self.dump_feature_columns) > 10:
                        model_info += f" ... y {len(self.dump_feature_columns)-10} más"
                    model_info += "\n"
                
                if self.dump_scaler:
                    model_info += f"📊 Escalador: {type(self.dump_scaler).__name__}\n"
                
                model_info += "✅ Modelo cargado exitosamente\n"
                
                # Agregar al área de resultados
                current_text = self.dump_results_text.get(1.0, tk.END)
                self.dump_results_text.insert(tk.END, model_info)
                
                self.check_dump_prediction_ready()
                
            except Exception as e:
                self.dump_model_label.config(text="🤖 Modelo dump: Error al cargar", style="Error.TLabel")
                messagebox.showerror("Error", f"Error cargando modelo:\n{str(e)}\n\n{traceback.format_exc()}")
            finally:
                self.hide_progress()
    
    def check_dump_prediction_ready(self):
        """Verificar si se puede predecir desde dumps"""
        if (hasattr(self, 'processed_dump_df') and self.processed_dump_df is not None and
            hasattr(self, 'dump_model') and self.dump_model is not None):
            
            if (hasattr(self, 'dump_feature_columns') and 
                self.dump_feature_columns is not None and 
                len(self.dump_feature_columns) > 0):
                # Verificar que las features requeridas estén disponibles
                available_features = set(self.processed_dump_df.columns)
                required_features = set(self.dump_feature_columns)
                missing_features = required_features - available_features
                
                if missing_features:
                    self.dump_predict_btn.config(state="disabled")
                    self.dump_status_label.config(
                        text=f"⚠️ Estado: Features faltantes: {', '.join(list(missing_features)[:3])}...", 
                        style="Warning.TLabel"
                    )
                    return
            
            # Todo listo para predecir
            self.dump_predict_btn.config(state="normal")
            self.dump_status_label.config(
                text="🔮 Estado: Listo para predecir vacancies", 
                style="Success.TLabel"
            )
        else:
            self.dump_predict_btn.config(state="disabled")
    
    def predict_from_dumps(self):
        """Realizar predicciones desde dumps procesados"""
        if self.processed_dump_df is None or self.dump_model is None:
            messagebox.showwarning("Advertencia", "Necesitas datos procesados y modelo cargado")
            return
        
        try:
            self.show_progress("Prediciendo vacancies desde dumps...")
            
            # Preparar datos
            if (hasattr(self, 'dump_feature_columns') and 
                self.dump_feature_columns is not None and 
                len(self.dump_feature_columns) > 0):
                # Usar features específicas del modelo
                feature_cols = [col for col in self.dump_feature_columns 
                              if col in self.processed_dump_df.columns]
                if not feature_cols:
                    raise RuntimeError("No se encontraron features del modelo en los datos procesados")
                X_new = self.processed_dump_df[feature_cols].copy()
            else:
                # Usar todas las features numéricas excepto las prohibidas
                exclude_cols = ['file', 'estimated_vacancies']  # Excluir file y la estimación inicial
                feature_cols = [col for col in self.processed_dump_df.columns 
                              if col not in exclude_cols and self.processed_dump_df[col].dtype in ['int64', 'float64']]
                
                if not feature_cols:
                    raise RuntimeError("No se encontraron features numéricas para la predicción")
                X_new = self.processed_dump_df[feature_cols].copy()
            
            # Aplicar escalado si existe
            if hasattr(self, 'dump_scaler') and self.dump_scaler is not None:
                X_new = pd.DataFrame(
                    self.dump_scaler.transform(X_new),
                    columns=X_new.columns,
                    index=X_new.index
                )
            
            # Hacer predicciones
            predictions = self.dump_model.predict(X_new)
            predictions = np.round(predictions).astype(int)
            
            # Crear DataFrame de resultados
            self.dump_predictions = self.processed_dump_df.copy()
            self.dump_predictions["vacancies_predicted"] = predictions
            
            # Calcular estadísticas
            self.show_dump_prediction_results(predictions)
            
            # Habilitar botón de guardar
            self.dump_save_btn.config(state="normal")
            
            self.dump_status_label.config(
                text="✅ Estado: Predicciones completadas exitosamente", 
                style="Success.TLabel"
            )
            
        except Exception as e:
            self.dump_status_label.config(text="❌ Estado: Error en predicción", style="Error.TLabel")
            messagebox.showerror("Error", f"Error en predicción:\n{str(e)}\n\n{traceback.format_exc()}")
        finally:
            self.hide_progress()
    
    def show_dump_prediction_results(self, predictions):
        """Mostrar resultados de predicciones desde dump"""
        results_text = "\n\n🔮 PREDICCIONES DE VACANCIES COMPLETADAS\n" + "="*50 + "\n\n"
        
        # Estadísticas básicas de predicciones
        results_text += f"📊 ESTADÍSTICAS DE PREDICCIONES:\n"
        results_text += f"   • Total archivos procesados: {len(predictions)}\n"
        results_text += f"   • Rango predicciones: {int(predictions.min())} - {int(predictions.max())}\n"
        results_text += f"   • Media: {predictions.mean():.2f}\n"
        results_text += f"   • Mediana: {np.median(predictions):.0f}\n"
        results_text += f"   • Desviación estándar: {predictions.std():.2f}\n\n"
        
        # Distribución de predicciones
        value_counts = pd.Series(predictions).value_counts().sort_index()
        results_text += f"📈 DISTRIBUCIÓN DE PREDICCIONES:\n"
        for i, (value, count) in enumerate(value_counts.items()):
            if i >= 10:  # Mostrar solo los primeros 10
                results_text += f"   ... y {len(value_counts)-10} valores más\n"
                break
            results_text += f"   • {int(value)} vacancies: {count} archivos\n"
        
        # Comparación con estimación inicial (si existe)
        if 'estimated_vacancies' in self.dump_predictions.columns:
            initial_estimates = self.dump_predictions['estimated_vacancies'].values
            mae_vs_initial = np.mean(np.abs(predictions - initial_estimates))
            correlation = np.corrcoef(predictions, initial_estimates)[0,1] if len(set(predictions)) > 1 and len(set(initial_estimates)) > 1 else 0
            
            results_text += f"\n🔍 COMPARACIÓN CON ESTIMACIÓN INICIAL:\n"
            results_text += f"   • MAE vs estimación inicial: {mae_vs_initial:.2f}\n"
            results_text += f"   • Correlación: {correlation:.3f}\n"
        
        # Tabla de primeros resultados
        results_text += f"\n📋 PRIMERAS 10 PREDICCIONES:\n"
        display_cols = ['file', 'vacancies_predicted']
        if 'estimated_vacancies' in self.dump_predictions.columns:
            display_cols.append('estimated_vacancies')
        if 'n_atoms' in self.dump_predictions.columns:
            display_cols.append('n_atoms')
        
        results_text += self.dump_predictions[display_cols].head(10).to_string(index=False)
        
        # Archivos con mayor y menor número de vacancies
        sorted_preds = self.dump_predictions.sort_values('vacancies_predicted')
        results_text += f"\n\n🔻 ARCHIVOS CON MENOS VACANCIES:\n"
        results_text += sorted_preds[['file', 'vacancies_predicted']].head(3).to_string(index=False)
        
        results_text += f"\n\n🔺 ARCHIVOS CON MÁS VACANCIES:\n"
        results_text += sorted_preds[['file', 'vacancies_predicted']].tail(3).to_string(index=False)
        
        results_text += f"\n\n✅ Predicciones completadas exitosamente"
        results_text += f"\n💾 Usa 'Guardar Resultados' para exportar las predicciones"
        
        # Agregar al área de resultados
        self.dump_results_text.insert(tk.END, results_text)
    
    def export_dump_csv(self):
        """Exportar dataset de features procesadas a CSV"""
        if self.processed_dump_df is None:
            messagebox.showwarning("Advertencia", "No hay datos procesados para exportar")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Guardar dataset de features",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
        )
        
        if file_path:
            try:
                self.show_progress("Exportando dataset de features...")
                
                if file_path.endswith('.xlsx'):
                    self.processed_dump_df.to_excel(file_path, index=False)
                else:
                    self.processed_dump_df.to_csv(file_path, index=False)
                
                messagebox.showinfo("Éxito", 
                                   f"✅ Dataset exportado exitosamente:\n\n"
                                   f"📁 {file_path}\n"
                                   f"📊 {len(self.processed_dump_df)} filas\n"
                                   f"🔧 {len(self.processed_dump_df.columns)} columnas")
            except Exception as e:
                messagebox.showerror("Error", f"Error exportando dataset:\n{str(e)}")
            finally:
                self.hide_progress()
    
    def save_dump_results(self):
        """Guardar resultados de predicciones desde dump"""
        if self.dump_predictions is None:
            messagebox.showwarning("Advertencia", "No hay predicciones para guardar")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Guardar resultados de predicciones dump",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
        )
        
        if file_path:
            try:
                self.show_progress("Guardando resultados de predicciones...")
                
                if file_path.endswith('.xlsx'):
                    self.dump_predictions.to_excel(file_path, index=False)
                else:
                    self.dump_predictions.to_csv(file_path, index=False)
                
                messagebox.showinfo("Éxito", 
                                   f"✅ Predicciones guardadas exitosamente:\n\n"
                                   f"📁 {file_path}\n"
                                   f"📊 {len(self.dump_predictions)} archivos procesados\n"
                                   f"🔮 Columna 'vacancies_predicted' añadida")
            except Exception as e:
                messagebox.showerror("Error", f"Error guardando predicciones:\n{str(e)}")
            finally:
                self.hide_progress()
    
    # ===============================================================
    # MÉTODOS EXISTENTES (funcionalidad CSV/Modelo clásica)
    # ===============================================================
    
    def create_info_tab(self):
        """Crear pestaña de información"""
        info_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(info_frame, text="📋 Información")
        
        self.info_text = scrolledtext.ScrolledText(info_frame, height=20, wrap='word',
                                                  font=("Consolas", 10))
        self.info_text.pack(fill="both", expand=True)
        
        # Mensaje inicial
        welcome_msg = """🔮 PREDICTOR DE VACANCIES ML - VERSIÓN EXTENDIDA
=====================================================

👋 ¡Bienvenido! Esta aplicación te permite:

🔹 MODO CLÁSICO (CSV + Modelo):
   • Cargar archivos CSV con datos de materiales
   • Usar modelos entrenados (.joblib) para predecir vacancies
   • Visualizar resultados y estadísticas

🔹 MODO DUMP PROCESSOR (NUEVO):
   • Procesar archivos LAMMPS dump directamente
   • Extraer features automáticamente
   • Predecir vacancies sin necesidad de CSV previo

📋 PESTAÑAS DISPONIBLES:
🔮 Dump Processor - Procesa archivos .dump/.lammpstrj
📊 Resultados - Predicciones del modo clásico
📈 Gráficos - Visualizaciones del modo clásico
📈 Estadísticas - Análisis detallado del modo clásico

🚀 ¡Explora las diferentes pestañas para comenzar!
"""
        self.info_text.insert(1.0, welcome_msg)
    
    def create_results_tab(self):
        """Crear pestaña de resultados"""
        results_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(results_frame, text="📊 Resultados CSV")
        
        self.results_text = scrolledtext.ScrolledText(results_frame, height=20, wrap='word',
                                                     font=("Consolas", 10))
        self.results_text.pack(fill="both", expand=True)
    
    def create_viz_tab(self):
        """Crear pestaña de visualización"""
        viz_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(viz_frame, text="📈 Gráficos CSV")
        
        # Frame para controles de gráficos
        viz_control_frame = ttk.Frame(viz_frame)
        viz_control_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Button(viz_control_frame, text="📊 Distribución", 
                  command=self.plot_distribution).pack(side="left", padx=(0, 5))
        ttk.Button(viz_control_frame, text="🎯 Precisión", 
                  command=self.plot_accuracy).pack(side="left", padx=(0, 5))
        ttk.Button(viz_control_frame, text="🔄 Actualizar", 
                  command=self.update_visualization).pack(side="left")
        
        # Canvas para matplotlib
        self.fig, self.axes = plt.subplots(2, 2, figsize=(12, 8))
        self.fig.tight_layout(pad=3.0)
        
        self.canvas = FigureCanvasTkAgg(self.fig, viz_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def create_stats_tab(self):
        """Crear pestaña de estadísticas"""
        stats_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(stats_frame, text="📈 Estadísticas CSV")
        
        self.stats_text = scrolledtext.ScrolledText(stats_frame, height=20, wrap='word',
                                                   font=("Consolas", 10))
        self.stats_text.pack(fill="both", expand=True)
    
    def show_progress(self, message):
        """Mostrar barra de progreso"""
        self.progress_label.config(text=message)
        self.progress_label.pack(pady=5)
        self.progress.pack(fill="x", pady=5)
        self.progress.start()
        self.root.update()
    
    def hide_progress(self):
        """Ocultar barra de progreso"""
        self.progress.stop()
        self.progress.pack_forget()
        self.progress_label.pack_forget()
    
    def load_csv(self):
        """Cargar archivo CSV"""
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo CSV",
            filetypes=[("CSV files", "*.csv"), ("Todos los archivos", "*.*")]
        )
        
        if file_path:
            try:
                self.show_progress("Cargando CSV...")
                
                self.csv_path = file_path
                self.df = pd.read_csv(file_path)
                
                self.csv_label.config(text=f"📄 CSV: {Path(file_path).name} ({len(self.df):,} filas)", 
                                    style="Success.TLabel")
                
                # Mostrar información del CSV
                info = f"""📄 ARCHIVO CSV CARGADO
========================

📁 Archivo: {Path(file_path).name}
📁 Ubicación: {file_path}
📊 Dimensiones: {len(self.df):,} filas × {len(self.df.columns)} columnas

🔧 COLUMNAS DISPONIBLES ({len(self.df.columns)}):
{self._format_columns_list(self.df.columns.tolist())}

📋 INFORMACIÓN GENERAL:
• Memoria utilizada: {self.df.memory_usage(deep=True).sum() / 1024**2:.1f} MB
• Valores nulos: {self.df.isnull().sum().sum():,}
• Tipos de datos: {dict(self.df.dtypes.value_counts())}

📁 PRIMERAS 5 FILAS:
{self.df.head().to_string()}

✅ CSV cargado correctamente
"""
                self.info_text.delete(1.0, tk.END)
                self.info_text.insert(1.0, info)
                
                self.check_ready()
                
            except Exception as e:
                self.csv_label.config(text="📄 CSV: Error al cargar", style="Error.TLabel")
                messagebox.showerror("Error", f"Error cargando CSV:\n{str(e)}\n\n{traceback.format_exc()}")
            finally:
                self.hide_progress()
    
    def _format_columns_list(self, columns, max_per_line=4):
        """Formatear lista de columnas para mostrar"""
        formatted = []
        for i in range(0, len(columns), max_per_line):
            line_cols = columns[i:i+max_per_line]
            formatted.append("  • " + " | ".join(line_cols))
        return "\n".join(formatted)
    
    def load_model(self):
        """Cargar modelo .joblib"""
        file_path = filedialog.askopenfilename(
            title="Seleccionar modelo .joblib",
            filetypes=[("Joblib files", "*.joblib"), ("Todos los archivos", "*.*")]
        )
        
        if file_path:
            try:
                self.show_progress("Cargando modelo...")
                
                self.model_path = file_path
                model_data = joblib.load(file_path)
                
                # Manejar diferentes formatos de modelo
                if isinstance(model_data, dict):
                    # Formato con metadatos
                    self.model = model_data["model"]
                    self.feature_columns = model_data["feature_columns"]
                    self.scaler = model_data.get("scaler", None)
                    training_params = model_data.get("training_params", {})
                else:
                    # Formato simple (solo modelo)
                    self.model = model_data
                    self.feature_columns = None
                    self.scaler = None
                    training_params = {}
                
                self.model_label.config(text=f"🤖 Modelo: {Path(file_path).name}", 
                                      style="Success.TLabel")
                
                # Mostrar información del modelo
                model_info = f"""🤖 MODELO CARGADO
================

📁 Archivo: {Path(file_path).name}
📁 Ubicación: {file_path}
🧠 Tipo: {type(self.model).__name__}

"""
                
                if self.feature_columns:
                    model_info += f"""🔧 FEATURES REQUERIDAS ({len(self.feature_columns)}):
{self._format_columns_list(self.feature_columns)}

"""
                
                if self.scaler:
                    model_info += f"📊 Escalador: {type(self.scaler).__name__}\n"
                
                if training_params:
                    model_info += f"""⚙️ PARÁMETROS DE ENTRENAMIENTO:
{self._format_params(training_params)}

"""
                
                if hasattr(self.model, 'get_params'):
                    params = self.model.get_params()
                    model_info += f"""🔧 PARÁMETROS DEL MODELO:
{self._format_params(params, max_items=8)}

"""
                
                model_info += "✅ Modelo cargado correctamente"
                
                # Agregar a la información existente
                current_info = self.info_text.get(1.0, tk.END)
                self.info_text.insert(tk.END, "\n" + "="*50 + "\n" + model_info)
                
                self.check_ready()
                
            except Exception as e:
                self.model_label.config(text="🤖 Modelo: Error al cargar", style="Error.TLabel")
                messagebox.showerror("Error", f"Error cargando modelo:\n{str(e)}\n\n{traceback.format_exc()}")
            finally:
                self.hide_progress()
    
    def _format_params(self, params_dict, max_items=None):
        """Formatear diccionario de parámetros"""
        items = list(params_dict.items())
        if max_items:
            items = items[:max_items]
        
        formatted = []
        for key, value in items:
            if isinstance(value, float):
                formatted.append(f"  • {key}: {value:.4f}")
            else:
                formatted.append(f"  • {key}: {value}")
        
        if max_items and len(params_dict) > max_items:
            formatted.append(f"  • ... y {len(params_dict) - max_items} parámetros más")
        
        return "\n".join(formatted)
    
    def check_ready(self):
        """Verificar si se puede predecir"""
        if (self.csv_path and self.model_path and 
            hasattr(self, 'df') and self.df is not None and
            hasattr(self, 'model') and self.model is not None):
            
            if self.feature_columns:
                # Verificar que todas las features estén en el CSV
                missing_features = [feat for feat in self.feature_columns if feat not in self.df.columns]
                if missing_features:
                    self.predict_btn.config(state="disabled")
                    error_msg = f"⚠️ Features faltantes en CSV:\n{', '.join(missing_features)}"
                    messagebox.showwarning("Features Faltantes", error_msg)
                    return
            
            # Todo listo para predecir
            self.predict_btn.config(state="normal")
        else:
            self.predict_btn.config(state="disabled")
    
    def predict(self):
        """Realizar predicciones"""
        try:
            self.show_progress("Realizando predicciones...")
            
            # Preparar datos
            if self.feature_columns:
                X_new = self.df[self.feature_columns].copy()
            else:
                # Si no hay feature_columns, usar todas excepto 'vacancies' y columnas de texto
                exclude_cols = ['vacancies', 'file', 'filename', 'file_processed']
                feature_cols = [col for col in self.df.columns 
                              if col not in exclude_cols and self.df[col].dtype in ['int64', 'float64']]
                X_new = self.df[feature_cols].copy()
                self.feature_columns = feature_cols
            
            # Aplicar escalado si existe
            if self.scaler is not None:
                X_new = pd.DataFrame(
                    self.scaler.transform(X_new),
                    columns=self.feature_columns,
                    index=self.df.index
                )
            
            # Hacer predicciones
            predictions = self.model.predict(X_new)
            predictions = np.round(predictions).astype(int)
            
            # Agregar predicciones al DataFrame
            self.predictions_df = self.df.copy()
            self.predictions_df["vacancies_predicted"] = predictions
            
            # Calcular estadísticas
            self.calculate_and_show_stats(predictions)
            
            # Crear visualización
            self.update_visualization()
            
            # Habilitar botón de guardar
            self.save_btn.config(state="normal")
            
            # Cambiar a pestaña de resultados
            self.notebook.select(1)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en predicción:\n{str(e)}\n\n{traceback.format_exc()}")
        finally:
            self.hide_progress()
    
    def calculate_and_show_stats(self, predictions):
        """Calcular y mostrar estadísticas"""
        has_real_vacancies = "vacancies" in self.df.columns
        
        # Estadísticas básicas
        stats_text = f"""🔮 RESULTADOS DE PREDICCIÓN
==========================

📊 ESTADÍSTICAS GENERALES:
• Total de predicciones: {len(predictions):,}
• Rango de predicciones: {int(predictions.min())} - {int(predictions.max())}
• Media: {predictions.mean():.2f}
• Mediana: {np.median(predictions):.0f}
• Desviación estándar: {predictions.std():.2f}

📈 DISTRIBUCIÓN DE PREDICCIONES:
{self._format_value_counts(predictions)}

"""
        
        if has_real_vacancies:
            actual = self.df["vacancies"].values
            mae = np.mean(np.abs(predictions - actual))
            rmse = np.sqrt(np.mean((predictions - actual)**2))
            exact_accuracy = np.mean(predictions == actual)
            
            # Precisión por rangos
            tolerance_1 = np.mean(np.abs(predictions - actual) <= 1)
            tolerance_2 = np.mean(np.abs(predictions - actual) <= 2)
            
            stats_text += f"""🎯 MÉTRICAS DE EVALUACIÓN:
• MAE (Error Absoluto Medio): {mae:.2f}
• RMSE (Raíz Error Cuadrático Medio): {rmse:.2f}
• Precisión exacta: {exact_accuracy:.1%}
• Precisión ±1: {tolerance_1:.1%}
• Precisión ±2: {tolerance_2:.1%}

📊 COMPARACIÓN REAL vs PREDICHO:
• Correlación: {np.corrcoef(actual, predictions)[0,1]:.3f}
• R²: {1 - np.sum((actual - predictions)**2) / np.sum((actual - actual.mean())**2):.3f}

"""
        
        # Mostrar primeras predicciones
        display_cols = []
        if 'file' in self.predictions_df.columns:
            display_cols.append('file')
        display_cols.append('vacancies_predicted')
        if has_real_vacancies:
            display_cols.append('vacancies')
        
        stats_text += f"""📁 PRIMERAS 10 PREDICCIONES:
{self.predictions_df[display_cols].head(10).to_string()}

✅ Predicciones completadas exitosamente
"""
        
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(1.0, stats_text)
        
        # También mostrar en pestaña de estadísticas
        self.stats_text.delete(1.0, tk.END)
        self.stats_text.insert(1.0, stats_text)
    
    def _format_value_counts(self, values, max_show=10):
        """Formatear conteo de valores"""
        value_counts = pd.Series(values).value_counts().sort_index()
        
        formatted = []
        for i, (value, count) in enumerate(value_counts.items()):
            if i >= max_show:
                formatted.append(f"  ... y {len(value_counts) - max_show} valores más")
                break
            formatted.append(f"  • {int(value)}: {count:,} casos")
        
        return "\n".join(formatted)
    
    def update_visualization(self):
        """Actualizar visualización"""
        if self.predictions_df is None:
            return
        
        # Limpiar axes
        for ax in self.axes.flat:
            ax.clear()
        
        predictions = self.predictions_df["vacancies_predicted"]
        has_real = "vacancies" in self.predictions_df.columns
        
        # Plot 1: Distribución de predicciones
        self.axes[0,0].hist(predictions, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
        self.axes[0,0].set_title('Distribución de Predicciones')
        self.axes[0,0].set_xlabel('Vacancies Predichas')
        self.axes[0,0].set_ylabel('Frecuencia')
        self.axes[0,0].grid(True, alpha=0.3)
        
        if has_real:
            actual = self.predictions_df["vacancies"]
            
            # Plot 2: Scatter plot predicciones vs reales
            self.axes[0,1].scatter(actual, predictions, alpha=0.6, color='coral')
            max_val = max(actual.max(), predictions.max())
            self.axes[0,1].plot([0, max_val], [0, max_val], 'r--', label='Predicción perfecta')
            self.axes[0,1].set_xlabel('Valores Reales')
            self.axes[0,1].set_ylabel('Predicciones')
            self.axes[0,1].set_title('Predicciones vs Valores Reales')
            self.axes[0,1].legend()
            self.axes[0,1].grid(True, alpha=0.3)
            
            # Plot 3: Distribución de errores
            errors = predictions - actual
            self.axes[1,0].hist(errors, bins=20, alpha=0.7, color='lightgreen', edgecolor='black')
            self.axes[1,0].set_title('Distribución de Errores')
            self.axes[1,0].set_xlabel('Error (Predicho - Real)')
            self.axes[1,0].set_ylabel('Frecuencia')
            self.axes[1,0].axvline(0, color='red', linestyle='--', alpha=0.7)
            self.axes[1,0].grid(True, alpha=0.3)
            
            # Plot 4: Box plot de errores por rango de vacancies
            try:
                # Crear bins para rangos de vacancies
                bins = pd.cut(actual, bins=5)
                error_data = [errors[bins == bin_val].values for bin_val in bins.categories]
                self.axes[1,1].boxplot(error_data, labels=[f'{int(cat.left)}-{int(cat.right)}' for cat in bins.categories])
                self.axes[1,1].set_title('Errores por Rango de Vacancies')
                self.axes[1,1].set_xlabel('Rango de Vacancies Reales')
                self.axes[1,1].set_ylabel('Error')
                self.axes[1,1].grid(True, alpha=0.3)
            except:
                # Si falla el boxplot, hacer un gráfico simple
                self.axes[1,1].text(0.5, 0.5, 'Gráfico no disponible', 
                                   transform=self.axes[1,1].transAxes, ha='center')
        else:
            # Sin valores reales, mostrar solo análisis de predicciones
            self.axes[0,1].text(0.5, 0.5, 'Sin valores reales\npara comparar', 
                               transform=self.axes[0,1].transAxes, ha='center', va='center')
            self.axes[1,0].text(0.5, 0.5, 'Sin valores reales\npara calcular errores', 
                               transform=self.axes[1,0].transAxes, ha='center', va='center')
            self.axes[1,1].text(0.5, 0.5, 'Sin valores reales\npara análisis', 
                               transform=self.axes[1,1].transAxes, ha='center', va='center')
        
        self.fig.tight_layout()
        self.canvas.draw()
    
    def plot_distribution(self):
        """Actualizar gráfico de distribución"""
        self.update_visualization()
    
    def plot_accuracy(self):
        """Mostrar gráfico de precisión"""
        self.update_visualization()
    
    def save_results(self):
        """Guardar resultados en CSV"""
        if self.predictions_df is None:
            messagebox.showwarning("Advertencia", "No hay resultados para guardar")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Guardar resultados",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")]
        )
        
        if file_path:
            try:
                self.show_progress("Guardando resultados...")
                
                self.predictions_df.to_csv(file_path, index=False)
                messagebox.showinfo("Éxito", 
                                   f"✅ Resultados guardados exitosamente:\n\n"
                                   f"📁 {file_path}\n"
                                   f"📊 {len(self.predictions_df):,} filas guardadas")
            except Exception as e:
                messagebox.showerror("Error", f"Error guardando:\n{str(e)}")
            finally:
                self.hide_progress()

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = PredictorGUI(root)
    root.mainloop()