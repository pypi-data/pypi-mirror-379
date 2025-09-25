"""
Dump Processor Tab CORREGIDO - Versión sin errores
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
from typing import Tuple, Dict, Any, List, Set, Optional
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
                    try:
                        n_atoms = int(lines[i + 1])
                    except ValueError:
                        pass
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

class AdvancedDumpFeatureExtractor:
    """Extractor avanzado de features para dumps LAMMPS"""
    
    def __init__(self, atm_total: int = 16384, energy_min: float = -4.0, 
                 energy_max: float = -3.0, energy_bins: int = 10):
        self.ATM_TOTAL = atm_total
        self.ENERGY_MIN = energy_min
        self.ENERGY_MAX = energy_max
        self.ENERGY_BINS = energy_bins
    
    def get_available_features(self) -> Dict[str, List[str]]:
        """Retorna todas las features disponibles organizadas por categoría"""
        return {
            'basic': [
                'n_atoms', 'estimated_vacancies', 'vacancy_fraction'
            ],
            'spatial': [
                'x_mean', 'x_std', 'x_range', 'x_skew', 'x_kurt',
                'y_mean', 'y_std', 'y_range', 'y_skew', 'y_kurt',
                'z_mean', 'z_std', 'z_range', 'z_skew', 'z_kurt',
                'center_of_mass_x', 'center_of_mass_y', 'center_of_mass_z',
                'spatial_density', 'volume_estimate'
            ],
            'energy': [
                *[f'pe_bin_{i}' for i in range(self.ENERGY_BINS)],
                'pe_mean', 'pe_std', 'pe_min', 'pe_max', 'pe_range',
                'pe_below_min', 'pe_above_max', 'pe_absolute_min',
                'pe_skew', 'pe_kurt', 'pe_median', 'pe_q25', 'pe_q75'
            ],
            'coordination': [
                *[f'coord_{i}' for i in range(1, 15)],
                'coord_mean', 'coord_std', 'coord_max', 'coord_defects'
            ],
            'stress': [
                'stress_xx_mean', 'stress_yy_mean', 'stress_zz_mean',
                'stress_xy_mean', 'stress_xz_mean', 'stress_yz_mean',
                'von_mises_mean', 'von_mises_std', 'von_mises_max'
            ],
            'voronoi': [
                'voro_volume_mean', 'voro_volume_std', 'voro_faces_mean',
                'voro_edges_mean', 'voro_area_mean'
            ],
            'bulk_indicators': [
                *[f'frac_coord_{i}' for i in range(1, 15)],
                'bulk_fraction', 'surface_fraction'
            ]
        }
    
    def get_default_features(self) -> List[str]:
        """Retorna features por defecto para procesamiento rápido"""
        return [
            'n_atoms', 'estimated_vacancies', 'vacancy_fraction',
            'x_mean', 'y_mean', 'z_mean', 'x_std', 'y_std', 'z_std',
            'pe_mean', 'pe_std', 'pe_min', 'pe_max', 'pe_range'
        ]
    
    def extract_features(self, atomic_df: pd.DataFrame, filename: str = "", 
                        selected_features: Optional[List[str]] = None) -> pd.Series:
        """Extraer features seleccionadas del DataFrame atómico"""
        if atomic_df.empty:
            raise ValueError("DataFrame vacío")
        
        if selected_features is None:
            selected_features = self.get_default_features()
        
        features = {'file': filename}
        
        # Calcular features por categoría
        all_available = self.get_available_features()
        
        for category, feature_list in all_available.items():
            requested_from_category = [f for f in selected_features if f in feature_list]
            if requested_from_category:
                try:
                    category_features = self._extract_category_features(
                        atomic_df, category, requested_from_category)
                    features.update(category_features)
                except Exception as e:
                    logger.warning(f"Error extracting {category} features: {e}")
                    # Llenar con valores por defecto en caso de error
                    for feat in requested_from_category:
                        features[feat] = 0.0
        
        return pd.Series(features)
    
    def _extract_category_features(self, df: pd.DataFrame, category: str, 
                                 requested_features: List[str]) -> Dict[str, float]:
        """Extraer features de una categoría específica"""
        
        if category == 'basic':
            return self._extract_basic_features(df, requested_features)
        elif category == 'spatial':
            return self._extract_spatial_features(df, requested_features)
        elif category == 'energy':
            return self._extract_energy_features(df, requested_features)
        elif category == 'coordination':
            return self._extract_coordination_features(df, requested_features)
        elif category == 'stress':
            return self._extract_stress_features(df, requested_features)
        elif category == 'voronoi':
            return self._extract_voronoi_features(df, requested_features)
        elif category == 'bulk_indicators':
            return self._extract_bulk_features(df, requested_features)
        else:
            return {}
    
    def _extract_basic_features(self, df: pd.DataFrame, requested: List[str]) -> Dict[str, float]:
        """Features básicas"""
        features = {}
        n_atoms = len(df)
        
        if 'n_atoms' in requested:
            features['n_atoms'] = float(n_atoms)
        if 'estimated_vacancies' in requested:
            features['estimated_vacancies'] = float(max(0, self.ATM_TOTAL - n_atoms))
        if 'vacancy_fraction' in requested:
            features['vacancy_fraction'] = float(max(0, self.ATM_TOTAL - n_atoms) / self.ATM_TOTAL)
        
        return features
    
    def _extract_spatial_features(self, df: pd.DataFrame, requested: List[str]) -> Dict[str, float]:
        """Features espaciales"""
        features = {}
        
        for coord in ['x', 'y', 'z']:
            if coord not in df.columns:
                continue
                
            data = df[coord].dropna()
            if len(data) == 0:
                continue
            
            try:
                if f'{coord}_mean' in requested:
                    features[f'{coord}_mean'] = float(data.mean())
                if f'{coord}_std' in requested:
                    features[f'{coord}_std'] = float(data.std()) if len(data) > 1 else 0.0
                if f'{coord}_range' in requested:
                    features[f'{coord}_range'] = float(data.max() - data.min())
                if f'{coord}_skew' in requested and len(data) > 2:
                    try:
                        features[f'{coord}_skew'] = float(data.skew())
                    except:
                        features[f'{coord}_skew'] = 0.0
                if f'{coord}_kurt' in requested and len(data) > 3:
                    try:
                        features[f'{coord}_kurt'] = float(data.kurtosis())
                    except:
                        features[f'{coord}_kurt'] = 0.0
            except Exception as e:
                logger.warning(f"Error calculating spatial features for {coord}: {e}")
        
        # Centro de masa
        try:
            if all(f'center_of_mass_{c}' in requested for c in ['x', 'y', 'z']):
                if all(c in df.columns for c in ['x', 'y', 'z']):
                    for coord in ['x', 'y', 'z']:
                        features[f'center_of_mass_{coord}'] = float(df[coord].mean())
        except Exception as e:
            logger.warning(f"Error calculating center of mass: {e}")
        
        # Volumen estimado
        try:
            if 'volume_estimate' in requested and all(c in df.columns for c in ['x', 'y', 'z']):
                x_range = df['x'].max() - df['x'].min()
                y_range = df['y'].max() - df['y'].min() 
                z_range = df['z'].max() - df['z'].min()
                features['volume_estimate'] = float(x_range * y_range * z_range)
            
            if 'spatial_density' in requested and 'volume_estimate' in features:
                if features['volume_estimate'] > 0:
                    features['spatial_density'] = float(len(df) / features['volume_estimate'])
                else:
                    features['spatial_density'] = 0.0
        except Exception as e:
            logger.warning(f"Error calculating volume features: {e}")
        
        return features
    
    def _extract_energy_features(self, df: pd.DataFrame, requested: List[str]) -> Dict[str, float]:
        """Features de energía"""
        features = {}
        
        pe_col = None
        for col in ['c_pe', 'pe', 'energy', 'potential']:
            if col in df.columns:
                pe_col = col
                break
        
        if pe_col is None:
            # Llenar con valores por defecto
            for feature in requested:
                features[feature] = 0.0
            return features
        
        pe_data = df[pe_col].replace([np.inf, -np.inf], np.nan).dropna()
        
        if len(pe_data) == 0:
            for feature in requested:
                features[feature] = 0.0
            return features
        
        try:
            # Estadísticas básicas
            if 'pe_mean' in requested:
                features['pe_mean'] = float(pe_data.mean())
            if 'pe_std' in requested:
                features['pe_std'] = float(pe_data.std()) if len(pe_data) > 1 else 0.0
            if 'pe_min' in requested:
                features['pe_min'] = float(pe_data.min())
            if 'pe_max' in requested:
                features['pe_max'] = float(pe_data.max())
            if 'pe_range' in requested:
                features['pe_range'] = float(pe_data.max() - pe_data.min())
            if 'pe_median' in requested:
                features['pe_median'] = float(pe_data.median())
            if 'pe_q25' in requested:
                features['pe_q25'] = float(pe_data.quantile(0.25))
            if 'pe_q75' in requested:
                features['pe_q75'] = float(pe_data.quantile(0.75))
            
            # Estadísticas avanzadas (pueden fallar con datos insuficientes)
            if 'pe_skew' in requested and len(pe_data) > 2:
                try:
                    features['pe_skew'] = float(pe_data.skew())
                except:
                    features['pe_skew'] = 0.0
            if 'pe_kurt' in requested and len(pe_data) > 3:
                try:
                    features['pe_kurt'] = float(pe_data.kurtosis())
                except:
                    features['pe_kurt'] = 0.0
        except Exception as e:
            logger.warning(f"Error calculating energy statistics: {e}")
        
        # Histograma
        histogram_features = [f for f in requested if f.startswith('pe_bin_')]
        if histogram_features:
            try:
                bin_edges = np.linspace(self.ENERGY_MIN, self.ENERGY_MAX, self.ENERGY_BINS + 1)
                hist, _ = np.histogram(pe_data, bins=bin_edges)
                total = len(pe_data)
                
                for i in range(self.ENERGY_BINS):
                    feature_name = f'pe_bin_{i}'
                    if feature_name in requested:
                        features[feature_name] = float(hist[i] / total) if total > 0 else 0.0
            except Exception as e:
                logger.warning(f"Error calculating energy histogram: {e}")
                for feat in histogram_features:
                    features[feat] = 0.0
        
        # Fuera de rango
        try:
            if 'pe_below_min' in requested:
                features['pe_below_min'] = float((pe_data < self.ENERGY_MIN).sum() / len(pe_data))
            if 'pe_above_max' in requested:
                features['pe_above_max'] = float((pe_data > self.ENERGY_MAX).sum() / len(pe_data))
            if 'pe_absolute_min' in requested:
                features['pe_absolute_min'] = float(pe_data.min())
        except Exception as e:
            logger.warning(f"Error calculating energy range features: {e}")
        
        return features
    
    def _extract_coordination_features(self, df: pd.DataFrame, requested: List[str]) -> Dict[str, float]:
        """Features de coordinación"""
        features = {}
        
        # Buscar columna de coordinación
        coord_cols = [col for col in df.columns if 'coord' in col.lower() or 'cn' in col.lower()]
        
        if not coord_cols:
            # Llenar con valores por defecto
            for feature in requested:
                features[feature] = 0.0
            return features
        
        coord_col = coord_cols[0]
        coord_data = df[coord_col].dropna()
        
        if len(coord_data) == 0:
            for feature in requested:
                features[feature] = 0.0
            return features
        
        try:
            # Estadísticas
            if 'coord_mean' in requested:
                features['coord_mean'] = float(coord_data.mean())
            if 'coord_std' in requested:
                features['coord_std'] = float(coord_data.std()) if len(coord_data) > 1 else 0.0
            if 'coord_max' in requested:
                features['coord_max'] = float(coord_data.max())
            if 'coord_defects' in requested:
                defects = (coord_data != 12).sum()
                features['coord_defects'] = float(defects / len(coord_data))
        except Exception as e:
            logger.warning(f"Error calculating coordination statistics: {e}")
        
        # Histograma
        try:
            for i in range(1, 15):
                feature_name = f'coord_{i}'
                if feature_name in requested:
                    count = (coord_data == i).sum()
                    features[feature_name] = float(count / len(coord_data))
        except Exception as e:
            logger.warning(f"Error calculating coordination histogram: {e}")
        
        return features
    
    def _extract_stress_features(self, df: pd.DataFrame, requested: List[str]) -> Dict[str, float]:
        """Features de stress - implementación básica"""
        features = {}
        
        # Componentes del tensor de stress
        stress_mapping = {
            'stress_xx_mean': ['stress_xx', 'sxx', 's_xx'],
            'stress_yy_mean': ['stress_yy', 'syy', 's_yy'],
            'stress_zz_mean': ['stress_zz', 'szz', 's_zz'],
            'stress_xy_mean': ['stress_xy', 'sxy', 's_xy'],
            'stress_xz_mean': ['stress_xz', 'sxz', 's_xz'],
            'stress_yz_mean': ['stress_yz', 'syz', 's_yz']
        }
        
        for feature_name, possible_cols in stress_mapping.items():
            if feature_name in requested:
                found_col = None
                for col_name in possible_cols:
                    matching_cols = [col for col in df.columns if col_name.lower() in col.lower()]
                    if matching_cols:
                        found_col = matching_cols[0]
                        break
                
                if found_col:
                    try:
                        stress_data = df[found_col].dropna()
                        features[feature_name] = float(stress_data.mean()) if len(stress_data) > 0 else 0.0
                    except:
                        features[feature_name] = 0.0
                else:
                    features[feature_name] = 0.0
        
        # Von Mises stress
        vm_features = ['von_mises_mean', 'von_mises_std', 'von_mises_max']
        if any(f in requested for f in vm_features):
            von_mises_cols = [col for col in df.columns if 'von_mises' in col.lower() or 'vm' in col.lower()]
            if von_mises_cols:
                try:
                    vm_data = df[von_mises_cols[0]].dropna()
                    if len(vm_data) > 0:
                        if 'von_mises_mean' in requested:
                            features['von_mises_mean'] = float(vm_data.mean())
                        if 'von_mises_std' in requested:
                            features['von_mises_std'] = float(vm_data.std()) if len(vm_data) > 1 else 0.0
                        if 'von_mises_max' in requested:
                            features['von_mises_max'] = float(vm_data.max())
                except:
                    for feat in vm_features:
                        if feat in requested:
                            features[feat] = 0.0
        
        return features
    
    def _extract_voronoi_features(self, df: pd.DataFrame, requested: List[str]) -> Dict[str, float]:
        """Features de Voronoi - implementación básica"""
        features = {}
        
        voronoi_mapping = {
            'voro_volume_mean': ['voro_vol', 'voronoi_volume', 'voro_volume'],
            'voro_volume_std': ['voro_vol', 'voronoi_volume', 'voro_volume'],
            'voro_faces_mean': ['voro_faces', 'voronoi_faces'],
            'voro_edges_mean': ['voro_edges', 'voronoi_edges'],
            'voro_area_mean': ['voro_area', 'voronoi_area']
        }
        
        for feature_name, possible_cols in voronoi_mapping.items():
            if feature_name in requested:
                found_col = None
                for col_name in possible_cols:
                    matching_cols = [col for col in df.columns if col_name in col.lower()]
                    if matching_cols:
                        found_col = matching_cols[0]
                        break
                
                if found_col:
                    try:
                        data = df[found_col].dropna()
                        if len(data) > 0:
                            if 'mean' in feature_name:
                                features[feature_name] = float(data.mean())
                            elif 'std' in feature_name:
                                features[feature_name] = float(data.std()) if len(data) > 1 else 0.0
                        else:
                            features[feature_name] = 0.0
                    except:
                        features[feature_name] = 0.0
                else:
                    features[feature_name] = 0.0
        
        return features
    
    def _extract_bulk_features(self, df: pd.DataFrame, requested: List[str]) -> Dict[str, float]:
        """Features bulk/surface"""
        features = {}
        
        # Buscar columna de coordinación para calcular bulk vs surface
        coord_cols = [col for col in df.columns if 'coord' in col.lower()]
        
        if coord_cols:
            try:
                coord_data = df[coord_cols[0]].dropna()
                if len(coord_data) > 0:
                    total = len(coord_data)
                    
                    # Fracciones de coordinación
                    for i in range(1, 15):
                        feature_name = f'frac_coord_{i}'
                        if feature_name in requested:
                            count = (coord_data == i).sum()
                            features[feature_name] = float(count / total)
                    
                    # Fracción bulk (coordinación 12) vs surface
                    if 'bulk_fraction' in requested or 'surface_fraction' in requested:
                        bulk_count = (coord_data == 12).sum()
                        
                        if 'bulk_fraction' in requested:
                            features['bulk_fraction'] = float(bulk_count / total)
                        if 'surface_fraction' in requested:
                            features['surface_fraction'] = float((total - bulk_count) / total)
            except Exception as e:
                logger.warning(f"Error calculating bulk features: {e}")
                for feat in requested:
                    features[feat] = 0.0
        else:
            # Sin datos de coordinación, llenar con 0
            for feat in requested:
                features[feat] = 0.0
        
        return features

class DumpProcessorTab:
    """Pestaña mejorada para procesamiento de dumps con selección de features"""
    
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
        
        # Features seleccionadas
        self.selected_features = set()
        self.feature_vars = {}
        
        # Variables de configuración - inicializar antes de crear widgets
        self.atm_total_var = None
        self.energy_min_var = None
        self.energy_max_var = None
        self.energy_bins_var = None
        
        # Configuración del extractor
        self.atm_total = 16384
        self.energy_min = -4.0
        self.energy_max = -3.0
        self.energy_bins = 10
        
        # Herramientas
        self.parser = LAMMPSFileParser()
        self.extractor = AdvancedDumpFeatureExtractor(
            self.atm_total, self.energy_min, self.energy_max, self.energy_bins)
        
        # Variables de UI - inicializar
        self.notebook = None
        self.features_notebook = None
        self.feature_count_var = None
        self.status_var = None
        self.progress_var = None
        
        self.create_widgets()
    
    def create_widgets(self):
        """Crear interfaz con notebook para secciones"""
        main_container = ttk.Frame(self.frame, padding="10")
        main_container.pack(fill="both", expand=True)
        
        # Título
        title_label = ttk.Label(main_container, text="🔥 Dump Processor Avanzado", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Crear notebook
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill="both", expand=True)
        
        # Crear pestañas
        self.create_config_tab()
        self.create_features_tab()
        self.create_processing_tab()
        self.create_prediction_tab()
    
    def create_config_tab(self):
        """Crear pestaña de configuración"""
        config_frame = ttk.Frame(self.notebook)
        self.notebook.add(config_frame, text="⚙️ Configuración")
        
        # Configuración LAMMPS
        lammps_frame = ttk.LabelFrame(config_frame, text="Configuración LAMMPS", padding="10")
        lammps_frame.pack(fill="x", padx=10, pady=10)
        
        # Variables de configuración - inicializar aquí
        self.atm_total_var = tk.IntVar(value=self.atm_total)
        self.energy_min_var = tk.DoubleVar(value=self.energy_min)
        self.energy_max_var = tk.DoubleVar(value=self.energy_max)
        self.energy_bins_var = tk.IntVar(value=self.energy_bins)
        
        # Grid de configuración
        ttk.Label(lammps_frame, text="Número total de átomos:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(lammps_frame, textvariable=self.atm_total_var, width=15).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(lammps_frame, text="Energía mínima (eV):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(lammps_frame, textvariable=self.energy_min_var, width=15).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(lammps_frame, text="Energía máxima (eV):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(lammps_frame, textvariable=self.energy_max_var, width=15).grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(lammps_frame, text="Bins de energía:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(lammps_frame, textvariable=self.energy_bins_var, width=15).grid(row=3, column=1, padx=5, pady=5)
        
        # Botón de aplicar configuración
        apply_btn = ttk.Button(lammps_frame, text="Aplicar Configuración", 
                              command=self.update_extractor_config)
        apply_btn.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Información de archivos
        files_frame = ttk.LabelFrame(config_frame, text="Archivos", padding="10")
        files_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        load_btn = ttk.Button(files_frame, text="📁 Cargar Dumps", 
                             command=self.load_dumps, width=20)
        load_btn.pack(pady=10)
        
        self.files_info = tk.Text(files_frame, height=10, font=("Courier", 9))
        self.files_info.pack(fill="both", expand=True)
        
        # Mensaje inicial
        initial_msg = """🔥 DUMP PROCESSOR AVANZADO

PASOS:
1. Configurar parámetros LAMMPS
2. Cargar archivos dump (.dump/.dump.gz)  
3. Seleccionar features a calcular
4. Procesar archivos
5. Cargar modelo y predecir

⚡ Listo para comenzar!
"""
        self.files_info.insert(1.0, initial_msg)
    
    def create_features_tab(self):
        """Crear pestaña de selección de features"""
        features_frame = ttk.Frame(self.notebook)
        self.notebook.add(features_frame, text="🎯 Selección Features")
        
        # Info y controles
        info_frame = ttk.Frame(features_frame)
        info_frame.pack(fill="x", padx=10, pady=5)
        
        self.feature_count_var = tk.StringVar(value="0 features seleccionadas")
        count_label = ttk.Label(info_frame, textvariable=self.feature_count_var, 
                               font=("Arial", 12, "bold"))
        count_label.pack(side="left")
        
        # Botones de control
        control_frame = ttk.Frame(info_frame)
        control_frame.pack(side="right")
        
        ttk.Button(control_frame, text="Todo", command=self.select_all_features).pack(side="left", padx=2)
        ttk.Button(control_frame, text="Nada", command=self.select_no_features).pack(side="left", padx=2)
        ttk.Button(control_frame, text="Por Defecto", command=self.select_default_features).pack(side="left", padx=2)
        
        # Notebook para categorías de features
        self.features_notebook = ttk.Notebook(features_frame)
        self.features_notebook.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.create_feature_categories()
    
    def create_feature_categories(self):
        """Crear tabs para cada categoría de features"""
        # Limpiar tabs existentes
        if self.features_notebook:
            for tab_id in self.features_notebook.tabs():
                self.features_notebook.forget(tab_id)
        
        # Limpiar variables existentes
        self.feature_vars.clear()
        self.selected_features.clear()
        
        available_features = self.extractor.get_available_features()
        
        for category, features in available_features.items():
            # Frame para la categoría
            cat_frame = ttk.Frame(self.features_notebook)
            self.features_notebook.add(cat_frame, text=category.title())
            
            # Frame principal con scrollbar
            main_frame = ttk.Frame(cat_frame)
            main_frame.pack(fill="both", expand=True)
            
            # Canvas y scrollbar
            canvas = tk.Canvas(main_frame)
            scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = ttk.Frame(canvas)
            
            def configure_scroll_region(event):
                canvas.configure(scrollregion=canvas.bbox("all"))
            
            scrollable_frame.bind("<Configure>", configure_scroll_region)
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            # Crear checkboxes para features
            for i, feature in enumerate(features):
                var = tk.BooleanVar()
                self.feature_vars[feature] = var
                
                # Crear callback específico para esta feature
                def create_callback(feature_name):
                    def callback(*args):
                        if self.feature_vars[feature_name].get():
                            self.selected_features.add(feature_name)
                        else:
                            self.selected_features.discard(feature_name)
                        self.update_feature_count()
                    return callback
                
                var.trace('w', create_callback(feature))
                
                cb = ttk.Checkbutton(scrollable_frame, text=feature, variable=var)
                cb.grid(row=i//2, column=i%2, sticky="w", padx=10, pady=2)
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
    
    def create_processing_tab(self):
        """Crear pestaña de procesamiento"""
        process_frame = ttk.Frame(self.notebook)
        self.notebook.add(process_frame, text="⚡ Procesamiento")
        
        # Controles
        control_frame = ttk.LabelFrame(process_frame, text="Controles", padding="10")
        control_frame.pack(fill="x", padx=10, pady=5)
        
        # Botones
        btn_frame = ttk.Frame(control_frame)
        btn_frame.pack(fill="x", pady=5)
        
        process_btn = ttk.Button(btn_frame, text="🚀 Procesar Dumps", 
                                command=self.process_dumps, width=20)
        process_btn.pack(side="left", padx=5)
        
        save_btn = ttk.Button(btn_frame, text="💾 Guardar Dataset", 
                             command=self.save_dataset, width=20)
        save_btn.pack(side="left", padx=5)
        
        # Estado
        self.status_var = tk.StringVar(value="Listo para procesar")
        self.status_label = ttk.Label(control_frame, textvariable=self.status_var)
        self.status_label.pack(pady=10)
        
        # Progreso
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(control_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(fill="x", pady=5)
        
        # Log de procesamiento
        log_frame = ttk.LabelFrame(process_frame, text="Log de Procesamiento", padding="10")
        log_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.process_log = scrolledtext.ScrolledText(log_frame, height=20, font=("Consolas", 10))
        self.process_log.pack(fill="both", expand=True)
    
    def create_prediction_tab(self):
        """Crear pestaña de predicción"""
        pred_frame = ttk.Frame(self.notebook)
        self.notebook.add(pred_frame, text="🔮 Predicción")
        
        # Controles de modelo
        model_frame = ttk.LabelFrame(pred_frame, text="Modelo", padding="10")
        model_frame.pack(fill="x", padx=10, pady=5)
        
        # Botones de modelo
        btn_frame = ttk.Frame(model_frame)
        btn_frame.pack(fill="x", pady=5)
        
        load_model_btn = ttk.Button(btn_frame, text="🤖 Cargar Modelo", 
                                   command=self.load_model, width=20)
        load_model_btn.pack(side="left", padx=5)
        
        self.predict_btn = ttk.Button(btn_frame, text="🔮 Predecir", 
                                     command=self.predict, width=20, state="disabled")
        self.predict_btn.pack(side="left", padx=5)
        
        self.save_predictions_btn = ttk.Button(btn_frame, text="💾 Guardar Predicciones", 
                                              command=self.save_predictions, width=20, state="disabled")
        self.save_predictions_btn.pack(side="left", padx=5)
        
        # Resultados
        results_frame = ttk.LabelFrame(pred_frame, text="Resultados", padding="10")
        results_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.prediction_results = scrolledtext.ScrolledText(results_frame, height=20, font=("Consolas", 10))
        self.prediction_results.pack(fill="both", expand=True)
    
    # Métodos de funcionalidad
    def update_extractor_config(self):
        """Actualizar configuración del extractor"""
        try:
            self.atm_total = self.atm_total_var.get()
            self.energy_min = self.energy_min_var.get()
            self.energy_max = self.energy_max_var.get()
            self.energy_bins = self.energy_bins_var.get()
            
            # Recrear extractor con nueva configuración
            self.extractor = AdvancedDumpFeatureExtractor(
                self.atm_total, self.energy_min, self.energy_max, self.energy_bins)
            
            # Recrear tabs de features con nueva configuración
            self.create_feature_categories()
            
            messagebox.showinfo("Configuración", "Configuración actualizada. Las features han sido recargadas.")
        except Exception as e:
            messagebox.showerror("Error", f"Error actualizando configuración: {e}")
    
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
            
            info = f"📁 ARCHIVOS CARGADOS ({len(files)}):\n\n"
            for i, f in enumerate(files[:20], 1):  # Mostrar solo 20
                info += f"  {i:2d}. {Path(f).name}\n"
            if len(files) > 20:
                info += f"  ... y {len(files)-20} archivos más\n"
            
            info += f"\n✅ {len(files)} archivos listos para procesar"
            
            self.files_info.delete(1.0, tk.END)
            self.files_info.insert(1.0, info)
            
            # Cambiar a tab de features si no hay features seleccionadas
            if not self.selected_features:
                self.notebook.select(1)  # Tab de features
                messagebox.showinfo("Siguiente paso", "Ahora selecciona las features a calcular en la pestaña 'Selección Features'")
    
    def select_all_features(self):
        """Seleccionar todas las features"""
        for var in self.feature_vars.values():
            var.set(True)
    
    def select_no_features(self):
        """Deseleccionar todas las features"""
        for var in self.feature_vars.values():
            var.set(False)
    
    def select_default_features(self):
        """Seleccionar features por defecto"""
        defaults = self.extractor.get_default_features()
        
        for feature, var in self.feature_vars.items():
            if feature in defaults:
                var.set(True)
            else:
                var.set(False)
    
    def update_feature_count(self):
        """Actualizar contador de features seleccionadas"""
        if self.feature_count_var:
            count = len(self.selected_features)
            self.feature_count_var.set(f"{count} features seleccionadas")
    
    def process_dumps(self):
        """Procesar archivos dump con features seleccionadas"""
        if not self.dump_files:
            messagebox.showwarning("Advertencia", "Primero carga archivos dump")
            return
        
        if not self.selected_features:
            messagebox.showwarning("Advertencia", "Selecciona al menos una feature para calcular")
            return
        
        try:
            self.status_var.set("⏳ Procesando...")
            self.process_log.delete(1.0, tk.END)
            self.log_message(f"🚀 Iniciando procesamiento de {len(self.dump_files)} archivos")
            self.log_message(f"📊 Features seleccionadas: {len(self.selected_features)}")
            self.log_message("")
            
            all_features = []
            errors = []
            
            for i, dump_file in enumerate(self.dump_files):
                try:
                    # Actualizar progreso
                    progress = (i / len(self.dump_files)) * 100
                    self.progress_var.set(progress)
                    
                    self.status_var.set(f"⏳ Procesando {i+1}/{len(self.dump_files)}: {Path(dump_file).name}")
                    self.frame.update_idletasks()  # Cambiar de update() a update_idletasks()
                    
                    # Parsear archivo
                    atomic_df, n_atoms, metadata = self.parser.parse_last_frame(dump_file)
                    
                    # Extraer features seleccionadas
                    features = self.extractor.extract_features(
                        atomic_df, Path(dump_file).name, list(self.selected_features))
                    all_features.append(features)
                    
                    # Log cada 10 archivos
                    if (i + 1) % 10 == 0:
                        self.log_message(f"✅ Procesados {i+1}/{len(self.dump_files)} archivos")
                        
                except Exception as e:
                    error_msg = f"❌ Error en {Path(dump_file).name}: {str(e)}"
                    errors.append((dump_file, str(e)))
                    self.log_message(error_msg)
                    logger.error(f"Error processing {dump_file}: {e}")
            
            if not all_features:
                raise RuntimeError("No se pudieron procesar archivos")
            
            # Crear DataFrame final
            self.processed_df = pd.DataFrame(all_features)
            
            # Mostrar resultados
            self.progress_var.set(100)
            self.status_var.set("✅ Procesamiento completado")
            
            self.show_processing_results(len(all_features), errors)
            
            # Cambiar a tab de predicción
            self.notebook.select(3)
            
            # Notificar callback
            if self.data_loaded_callback:
                self.data_loaded_callback(self.processed_df)
                
        except Exception as e:
            self.status_var.set("❌ Error procesando")
            self.log_message(f"\n❌ ERROR FATAL: {str(e)}")
            logger.error(f"Fatal error in processing: {e}")
            messagebox.showerror("Error", f"Error: {e}")
    
    def show_processing_results(self, processed_count, errors):
        """Mostrar resultados del procesamiento"""
        results = f"""
✅ PROCESAMIENTO COMPLETADO

📊 RESUMEN:
• Archivos procesados: {processed_count}
• Features calculadas: {len(self.selected_features)}
• Errores: {len(errors)}

📈 ESTADÍSTICAS DEL DATASET:
• Shape: {self.processed_df.shape}
• Memoria: {self.processed_df.memory_usage(deep=True).sum() / 1024:.1f} KB

🎯 FEATURES PRINCIPALES:
"""
        
        # Mostrar algunas estadísticas de features
        try:
            numeric_cols = self.processed_df.select_dtypes(include=[np.number]).columns
            for col in list(numeric_cols)[:10]:
                if col != 'file':
                    stats = self.processed_df[col]
                    results += f"• {col}: min={stats.min():.3f}, max={stats.max():.3f}, mean={stats.mean():.3f}\n"
        except Exception as e:
            logger.warning(f"Error calculating feature statistics: {e}")
        
        if len(errors) > 0:
            results += f"\n⚠️ ERRORES ({len(errors)}):\n"
            for file, error in errors[:5]:
                results += f"• {Path(file).name}: {error[:50]}...\n"
        
        results += "\n🔮 Ahora puedes cargar un modelo para predecir"
        
        self.log_message(results)
    
    def log_message(self, message):
        """Agregar mensaje al log"""
        self.process_log.insert(tk.END, message + "\n")
        self.process_log.see(tk.END)
        self.frame.update_idletasks()
    
    def save_dataset(self):
        """Guardar dataset procesado"""
        if self.processed_df is None:
            messagebox.showwarning("Advertencia", "No hay dataset para guardar")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Guardar Dataset",
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv"), ("Excel", "*.xlsx")]
        )
        
        if file_path:
            try:
                if file_path.endswith('.xlsx'):
                    self.processed_df.to_excel(file_path, index=False)
                else:
                    self.processed_df.to_csv(file_path, index=False)
                
                messagebox.showinfo("Éxito", f"Dataset guardado: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Error guardando: {e}")
    
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
                    self.model = model_data.get("model")
                    self.feature_columns = model_data.get("feature_columns", None)
                    self.scaler = model_data.get("scaler", None)
                else:
                    self.model = model_data
                    self.feature_columns = None
                    self.scaler = None
                
                info = f"""🤖 MODELO CARGADO: {Path(file_path).name}
• Tipo: {type(self.model).__name__}
• Features requeridas: {len(self.feature_columns) if self.feature_columns else 'Auto'}
• Escalador: {'Sí' if self.scaler else 'No'}

✅ Modelo listo para predicción
"""
                
                self.prediction_results.insert(tk.END, info)
                self.check_prediction_ready()
                self.status_var.set("✅ Modelo cargado")
                
            except Exception as e:
                self.status_var.set("❌ Error cargando modelo")
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
                # Usar features específicas del modelo
                available_features = [col for col in self.feature_columns 
                                    if col in self.processed_df.columns]
                missing_features = [col for col in self.feature_columns
                                  if col not in self.processed_df.columns]
                
                if missing_features:
                    warning_msg = f"⚠️ Features faltantes: {missing_features[:5]}"
                    self.prediction_results.insert(tk.END, warning_msg + "\n")
                
                if not available_features:
                    raise ValueError("No hay features compatibles con el modelo")
                
                X = self.processed_df[available_features].copy()
            else:
                # Usar todas las features numéricas disponibles
                exclude = ['file', 'estimated_vacancies']
                feature_cols = [col for col in self.processed_df.columns 
                              if col not in exclude and 
                                 self.processed_df[col].dtype in ['int64', 'float64']]
                X = self.processed_df[feature_cols].copy()
            
            # Aplicar escalado si existe
            if self.scaler:
                try:
                    X_scaled = self.scaler.transform(X)
                    X = pd.DataFrame(X_scaled, columns=X.columns, index=X.index)
                except Exception as e:
                    logger.warning(f"Error escalando datos: {e}")
                    self.prediction_results.insert(tk.END, f"⚠️ Error aplicando escalador: {e}\n")
            
            # Predecir
            predictions = self.model.predict(X)
            predictions = np.round(predictions).astype(int)
            
            # Crear resultado
            self.predictions = self.processed_df.copy()
            self.predictions["vacancies_predicted"] = predictions
            
            # Mostrar resultados
            self.show_prediction_results(predictions)
            
            self.save_predictions_btn.config(state="normal")
            self.status_var.set("✅ Predicciones completadas")
            
        except Exception as e:
            self.status_var.set("❌ Error prediciendo")
            error_msg = f"❌ Error en predicción: {str(e)}"
            self.prediction_results.insert(tk.END, error_msg + "\n")
            logger.error(f"Prediction error: {e}")
            messagebox.showerror("Error", f"Error en predicción: {e}")
    
    def show_prediction_results(self, predictions):
        """Mostrar resultados de predicción"""
        results = f"""
🔮 PREDICCIONES COMPLETADAS

📊 ESTADÍSTICAS:
• Total archivos: {len(predictions)}
• Rango predicciones: {predictions.min()} - {predictions.max()}
• Media: {predictions.mean():.2f}
• Desviación: {predictions.std():.2f}

📋 PRIMERAS 10 PREDICCIONES:
"""
        
        try:
            display_cols = ['file', 'vacancies_predicted']
            if 'estimated_vacancies' in self.predictions.columns:
                display_cols.append('estimated_vacancies')
            
            results += self.predictions[display_cols].head(10).to_string(index=False)
        except Exception as e:
            results += f"Error mostrando predicciones: {e}"
            
        results += "\n\n✅ Predicciones listas para guardar"
        
        self.prediction_results.insert(tk.END, results)
        self.prediction_results.see(tk.END)
    
    def save_predictions(self):
        """Guardar predicciones"""
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
                self.status_var.set("✅ Predicciones guardadas")
            except Exception as e:
                messagebox.showerror("Error", f"Error guardando: {e}")