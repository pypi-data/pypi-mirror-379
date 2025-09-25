"""
Dump Processor Tab para Vacancy Predictor - VERSIÓN SIMPLIFICADA
Archivo: vacancy_predictor/gui/tabs/dump_processor_tab.py
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import pandas as pd
import joblib
import numpy as np
from pathlib import Path
import traceback
import gzip
import io
from typing import Tuple, Dict, Any, List
import logging

logger = logging.getLogger(__name__)

class LAMMPSFileParser:
    """Parser simple para archivos LAMMPS dump"""
    
    def _open_file(self, path: str):
        """Abrir archivo, detectando compresión"""
        p = Path(path)
        if p.suffix == ".gz":
            return io.TextIOWrapper(gzip.open(p, "rb"), encoding="utf-8")
        return open(p, "r", encoding="utf-8")
    
    def parse_last_frame(self, path: str) -> Tuple[pd.DataFrame, int, Dict[str, Any]]:
        """Parser básico del último frame"""
        try:
            with self._open_file(path) as f:
                lines = f.read().splitlines()
        except Exception as e:
            raise RuntimeError(f"Error leyendo {path}: {e}")
        
        # Buscar última sección ATOMS
        atoms_indices = [i for i, line in enumerate(lines) if line.startswith("ITEM: ATOMS")]
        if not atoms_indices:
            raise RuntimeError(f"No encontré 'ITEM: ATOMS' en {path}")
        
        start_idx = atoms_indices[-1]
        header = lines[start_idx].replace("ITEM: ATOMS", "").strip().split()
        
        # Determinar número de átomos
        n_atoms = 0
        for i in range(max(0, start_idx - 20), start_idx):
            if i < len(lines) and "ITEM: NUMBER OF ATOMS" in lines[i]:
                if i + 1 < len(lines):
                    n_atoms = int(lines[i + 1])
                break
        
        if n_atoms == 0:
            # Contar hasta la siguiente sección
            for i in range(start_idx + 1, len(lines)):
                if lines[i].strip() and not lines[i].startswith("ITEM:"):
                    n_atoms += 1
                else:
                    break
        
        # Parsear datos
        data_rows = []
        for i in range(start_idx + 1, min(start_idx + 1 + n_atoms, len(lines))):
            if not lines[i].strip():
                continue
            parts = lines[i].split()
            if len(parts) >= len(header):
                row = []
                for j, part in enumerate(parts[:len(header)]):
                    try:
                        row.append(float(part))
                    except ValueError:
                        row.append(np.nan)
                data_rows.append(row)
        
        df = pd.DataFrame(data_rows, columns=header) if data_rows else pd.DataFrame()
        return df, len(df), {}

class DumpFeatureExtractor:
    """Extractor simple de features"""
    
    def __init__(self):
        self.ATM_TOTAL = 16384
    
    def extract_features(self, atomic_df: pd.DataFrame, filename: str = "") -> pd.Series:
        """Extraer features básicas"""
        if atomic_df.empty:
            raise ValueError("DataFrame vacío")
        
        features = {'file': filename, 'n_atoms': len(atomic_df)}
        
        # Features de energía
        if 'c_pe' in atomic_df.columns:
            energies = atomic_df['c_pe'].dropna()
            if len(energies) > 0:
                features.update({
                    'energy_mean': energies.mean(),
                    'energy_std': energies.std() if len(energies) > 1 else 0.0,
                    'energy_min': energies.min(),
                    'energy_max': energies.max(),
                })
        
        # Features espaciales
        for col in ['x', 'y', 'z']:
            if col in atomic_df.columns:
                coords = atomic_df[col].dropna()
                if len(coords) > 0:
                    features.update({
                        f'{col}_mean': coords.mean(),
                        f'{col}_std': coords.std() if len(coords) > 1 else 0.0,
                        f'{col}_range': coords.max() - coords.min()
                    })
        
        # Estimación de vacancies
        features['estimated_vacancies'] = max(0, self.ATM_TOTAL - len(atomic_df))
        
        return pd.Series(features)

class DumpProcessorTab:
    """Pestaña simplificada para procesamiento de dumps"""
    
    def __init__(self, parent, data_loaded_callback):
        self.parent = parent
        self.data_loaded_callback = data_loaded_callback
        
        self.frame = ttk.Frame(parent)
        
        # Variables
        self.dump_files = []
        self.processed_df = None
        self.model = None
        self.feature_columns = None
        self.scaler = None
        self.predictions = None
        
        # Herramientas
        self.parser = LAMMPSFileParser()
        self.extractor = DumpFeatureExtractor()
        
        self.create_widgets()
    
    def create_widgets(self):
        """Crear interfaz"""
        main_container = ttk.Frame(self.frame, padding="10")
        main_container.pack(fill="both", expand=True)
        
        # Título
        ttk.Label(main_container, text="🔥 Dump Processor", 
                 font=("Arial", 16, "bold")).pack(pady=(0, 20))
        
        # Controles
        control_frame = ttk.LabelFrame(main_container, text="Controles", padding="10")
        control_frame.pack(fill="x", pady=(0, 10))
        
        # Botones principales
        btn_frame = ttk.Frame(control_frame)
        btn_frame.pack(fill="x", pady=5)
        
        ttk.Button(btn_frame, text="📁 Cargar Dumps", 
                  command=self.load_dumps, width=15).pack(side="left", padx=(0, 10))
        ttk.Button(btn_frame, text="🔄 Procesar", 
                  command=self.process_dumps, width=15).pack(side="left", padx=(0, 10))
        ttk.Button(btn_frame, text="🤖 Cargar Modelo", 
                  command=self.load_model, width=15).pack(side="left", padx=(0, 10))
        
        # Segunda fila
        btn_frame2 = ttk.Frame(control_frame)
        btn_frame2.pack(fill="x", pady=5)
        
        self.predict_btn = ttk.Button(btn_frame2, text="🔮 Predecir", 
                                     command=self.predict, width=15, state="disabled")
        self.predict_btn.pack(side="left", padx=(0, 10))
        
        self.save_btn = ttk.Button(btn_frame2, text="💾 Guardar", 
                                  command=self.save_results, width=15, state="disabled")
        self.save_btn.pack(side="left", padx=(0, 10))
        
        # Estado
        self.status_var = tk.StringVar(value="Listo")
        ttk.Label(control_frame, textvariable=self.status_var).pack(pady=10)
        
        # Área de resultados
        self.results_text = scrolledtext.ScrolledText(main_container, height=20, 
                                                     font=("Consolas", 10))
        self.results_text.pack(fill="both", expand=True)
        
        # Mensaje inicial
        welcome = """🔥 DUMP PROCESSOR - Procesamiento de Archivos LAMMPS

PASOS:
1. Cargar Dumps → Selecciona archivos .dump/.dump.gz
2. Procesar → Extrae features automáticamente  
3. Cargar Modelo → Carga modelo .joblib entrenado
4. Predecir → Predicciones de vacancies
5. Guardar → Exporta resultados

FORMATOS SOPORTADOS:
• .dump, .dump.gz, .lammpstrj

🚀 ¡Comienza cargando archivos dump!
"""
        self.results_text.insert(1.0, welcome)
    
    def load_dumps(self):
        """Cargar archivos dump"""
        files = filedialog.askopenfilenames(
            title="Seleccionar archivos dump",
            filetypes=[
                ("LAMMPS files", "*.dump *.dump.gz *.lammpstrj"),
                ("Todos", "*.*")
            ]
        )
        
        if files:
            self.dump_files = list(files)
            self.status_var.set(f"✅ {len(files)} archivos cargados")
            
            info = f"\n📁 ARCHIVOS CARGADOS ({len(files)}):\n"
            for i, f in enumerate(files[:10], 1):  # Mostrar solo 10
                info += f"  {i}. {Path(f).name}\n"
            if len(files) > 10:
                info += f"  ... y {len(files)-10} más\n"
            
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(1.0, info + "\n🔄 Haz clic en 'Procesar' para extraer features")
    
    def process_dumps(self):
        """Procesar archivos a features"""
        if not self.dump_files:
            messagebox.showwarning("Advertencia", "Primero carga archivos dump")
            return
        
        try:
            self.status_var.set("⏳ Procesando...")
            all_features = []
            errors = []
            
            for i, dump_file in enumerate(self.dump_files):
                try:
                    # Parsear
                    atomic_df, n_atoms, metadata = self.parser.parse_last_frame(dump_file)
                    
                    # Extraer features
                    features = self.extractor.extract_features(atomic_df, Path(dump_file).name)
                    all_features.append(features)
                    
                    if i % 10 == 0:  # Actualizar cada 10 archivos
                        self.status_var.set(f"⏳ Procesando {i+1}/{len(self.dump_files)}")
                        self.frame.update()
                        
                except Exception as e:
                    errors.append((dump_file, str(e)))
            
            if not all_features:
                raise RuntimeError("No se pudieron procesar archivos")
            
            # Crear DataFrame
            self.processed_df = pd.DataFrame(all_features)
            
            # Mostrar resultados
            results = f"""✅ PROCESAMIENTO COMPLETADO

📊 RESUMEN:
• Archivos procesados: {len(all_features)}
• Features extraídas: {len(self.processed_df.columns)}
• Archivos fallidos: {len(errors)}

🔧 FEATURES DISPONIBLES:
"""
            
            feature_cols = [col for col in self.processed_df.columns if col != 'file']
            for i, col in enumerate(feature_cols[:10]):  # Mostrar solo 10
                results += f"  • {col}\n"
            if len(feature_cols) > 10:
                results += f"  ... y {len(feature_cols)-10} más\n"
            
            if 'estimated_vacancies' in self.processed_df.columns:
                vac_stats = self.processed_df['estimated_vacancies']
                results += f"""
🔍 VACANCIES ESTIMADAS:
• Min: {vac_stats.min():.0f}
• Max: {vac_stats.max():.0f}
• Media: {vac_stats.mean():.1f}
"""
            
            if errors:
                results += f"\n⚠️ ERRORES ({len(errors)}):\n"
                for file, error in errors[:3]:
                    results += f"  • {Path(file).name}: {error[:50]}...\n"
            
            results += "\n🤖 Carga un modelo .joblib para predecir"
            
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(1.0, results)
            
            self.status_var.set("✅ Procesamiento completado")
            
            # Notificar callback
            if self.data_loaded_callback:
                self.data_loaded_callback(self.processed_df)
                
        except Exception as e:
            self.status_var.set("❌ Error procesando")
            messagebox.showerror("Error", f"Error: {e}")
    
    def load_model(self):
        """Cargar modelo ML"""
        file_path = filedialog.askopenfilename(
            title="Seleccionar modelo .joblib",
            filetypes=[("Joblib", "*.joblib"), ("Todos", "*.*")]
        )
        
        if file_path:
            try:
                self.status_var.set("⏳ Cargando modelo...")
                
                model_data = joblib.load(file_path)
                
                if isinstance(model_data, dict):
                    self.model = model_data["model"]
                    self.feature_columns = model_data.get("feature_columns", None)
                    self.scaler = model_data.get("scaler", None)
                else:
                    self.model = model_data
                    self.feature_columns = None
                    self.scaler = None
                
                info = f"""
🤖 MODELO CARGADO: {Path(file_path).name}
• Tipo: {type(self.model).__name__}
• Features requeridas: {len(self.feature_columns) if self.feature_columns else 'Auto'}
• Escalador: {'Sí' if self.scaler else 'No'}

✅ Modelo listo para predicción
"""
                
                self.results_text.insert(tk.END, info)
                self.check_prediction_ready()
                self.status_var.set("✅ Modelo cargado")
                
            except Exception as e:
                messagebox.showerror("Error", f"Error cargando modelo: {e}")
    
    def check_prediction_ready(self):
        """Verificar si se puede predecir"""
        if self.processed_df is not None and self.model is not None:
            self.predict_btn.config(state="normal")
        else:
            self.predict_btn.config(state="disabled")
    
    def predict(self):
        """Realizar predicciones"""
        if self.processed_df is None or self.model is None:
            return
        
        try:
            self.status_var.set("⏳ Prediciendo...")
            
            # Preparar datos
            if self.feature_columns:
                feature_cols = [col for col in self.feature_columns 
                              if col in self.processed_df.columns]
                X = self.processed_df[feature_cols].copy()
            else:
                exclude = ['file', 'estimated_vacancies']
                feature_cols = [col for col in self.processed_df.columns 
                              if col not in exclude and 
                                 self.processed_df[col].dtype in ['int64', 'float64']]
                X = self.processed_df[feature_cols].copy()
            
            # Aplicar escalado
            if self.scaler:
                try:
                    X = pd.DataFrame(self.scaler.transform(X), 
                                   columns=X.columns, index=X.index)
                except Exception as e:
                    logger.warning(f"Error escalando: {e}")
            
            # Predecir
            predictions = self.model.predict(X)
            predictions = np.round(predictions).astype(int)
            
            # Crear resultado
            self.predictions = self.processed_df.copy()
            self.predictions["vacancies_predicted"] = predictions
            
            # Mostrar resultados
            results = f"""
🔮 PREDICCIONES COMPLETADAS

📊 ESTADÍSTICAS:
• Total archivos: {len(predictions)}
• Rango predicciones: {predictions.min()} - {predictions.max()}
• Media: {predictions.mean():.2f}
• Desviación: {predictions.std():.2f}

📋 PRIMERAS 10 PREDICCIONES:
"""
            
            display_cols = ['file', 'vacancies_predicted']
            if 'estimated_vacancies' in self.predictions.columns:
                display_cols.append('estimated_vacancies')
            
            results += self.predictions[display_cols].head(10).to_string(index=False)
            results += "\n\n✅ Predicciones listas para guardar"
            
            self.results_text.insert(tk.END, results)
            self.save_btn.config(state="normal")
            self.status_var.set("✅ Predicciones completadas")
            
        except Exception as e:
            self.status_var.set("❌ Error prediciendo")
            messagebox.showerror("Error", f"Error en predicción: {e}")
    
    def save_results(self):
        """Guardar resultados"""
        if self.predictions is None:
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Guardar predicciones",
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv"), ("Excel", "*.xlsx")]
        )
        
        if file_path:
            try:
                if file_path.endswith('.xlsx'):
                    self.predictions.to_excel(file_path, index=False)
                else:
                    self.predictions.to_csv(file_path, index=False)
                
                messagebox.showinfo("Éxito", 
                                   f"✅ Guardado: {file_path}\n"
                                   f"📊 {len(self.predictions)} predicciones")
                self.status_var.set("✅ Resultados guardados")
            except Exception as e:
                messagebox.showerror("Error", f"Error guardando: {e}")