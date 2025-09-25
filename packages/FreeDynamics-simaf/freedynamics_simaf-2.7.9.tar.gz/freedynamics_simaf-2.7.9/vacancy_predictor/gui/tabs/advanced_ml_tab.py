import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns

class AdvancedMLTabWithPlots:
    """Advanced ML Tab con visualizaciones integradas"""
    
    def __init__(self, parent, data_loaded_callback):
        self.parent = parent
        self.data_loaded_callback = data_loaded_callback
        
        self.frame = ttk.Frame(parent)
        
        # Variables de entrenamiento
        self.n_estimators_var = tk.IntVar(value=100)
        self.test_size_var = tk.DoubleVar(value=0.2)
        self.random_state_var = tk.IntVar(value=42)
        
        # Estado actual
        self.current_data = None
        self.trained_model = None
        self.feature_columns = []
        self.target_column = 'vacancies'
        self.X_test = None
        self.y_test = None
        self.test_predictions = None
        
        self.create_widgets()
    
    def create_widgets(self):
        """Crear widgets del tab"""
        main_container = ttk.Frame(self.frame, padding="10")
        main_container.pack(fill="both", expand=True)
        
        # Crear notebook para sub-tabs
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill="both", expand=True)
        
        self.create_data_tab()
        self.create_training_tab()
        self.create_results_tab()
        self.create_feature_analysis_tab()
        self.create_prediction_tab()
    
    def create_data_tab(self):
        """Tab de carga y exploración de datos"""
        data_frame = ttk.Frame(self.notebook)
        self.notebook.add(data_frame, text="📊 Datos")
        
        # Sección de carga
        load_frame = ttk.LabelFrame(data_frame, text="Cargar Dataset", padding="10")
        load_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Button(load_frame, text="Cargar CSV/Excel", 
                  command=self.load_dataset).pack(side="left", padx=5)
        
        # Información del dataset
        info_frame = ttk.LabelFrame(data_frame, text="Información del Dataset", padding="10")
        info_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.info_text = scrolledtext.ScrolledText(info_frame, height=20, wrap='word')
        self.info_text.pack(fill="both", expand=True)
    
    def create_training_tab(self):
        """Tab de entrenamiento"""
        train_frame = ttk.Frame(self.notebook)
        self.notebook.add(train_frame, text="🤖 Entrenamiento")
        
        # Panel izquierdo - Controles
        left_panel = ttk.Frame(train_frame)
        left_panel.pack(side="left", fill="y", padx=(10, 5))
        
        # Parámetros
        params_group = ttk.LabelFrame(left_panel, text="Parámetros Random Forest", padding="10")
        params_group.pack(fill='x', pady=(0, 10))
        
        ttk.Label(params_group, text="N° Estimadores:").grid(row=0, column=0, sticky='w', padx=5, pady=2)
        ttk.Spinbox(params_group, from_=50, to=500, textvariable=self.n_estimators_var, width=10).grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(params_group, text="Test Size:").grid(row=1, column=0, sticky='w', padx=5, pady=2)
        ttk.Entry(params_group, textvariable=self.test_size_var, width=10).grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(params_group, text="Random State:").grid(row=2, column=0, sticky='w', padx=5, pady=2)
        ttk.Entry(params_group, textvariable=self.random_state_var, width=10).grid(row=2, column=1, padx=5, pady=2)
        
        # Botones
        buttons_group = ttk.LabelFrame(left_panel, text="Acciones", padding="10")
        buttons_group.pack(fill='x', pady=(0, 10))
        
        self.train_btn = ttk.Button(buttons_group, text="Entrenar Modelo", 
                                   command=self.train_model)
        self.train_btn.pack(fill='x', pady=2)
        
        self.save_btn = ttk.Button(buttons_group, text="Guardar Modelo", 
                                  command=self.save_model, state="disabled")
        self.save_btn.pack(fill='x', pady=2)
        
        ttk.Button(buttons_group, text="Cargar Modelo", 
                  command=self.load_model).pack(fill='x', pady=2)
        
        # Panel derecho - Resultados de texto
        right_panel = ttk.Frame(train_frame)
        right_panel.pack(side="right", fill="both", expand=True, padx=(5, 10))
        
        results_group = ttk.LabelFrame(right_panel, text="Métricas del Entrenamiento", padding="10")
        results_group.pack(fill='both', expand=True)
        
        self.results_text = scrolledtext.ScrolledText(results_group, height=20, wrap='word')
        self.results_text.pack(fill='both', expand=True)
    

    def create_results_tab(self):
        """Tab de resultados con visualizaciones"""
        results_frame = ttk.Frame(self.notebook)
        self.notebook.add(results_frame, text="📊 Resultados")
        
        # Botones de control de gráficos - MEJORADOS
        control_frame = ttk.Frame(results_frame)
        control_frame.pack(fill="x", padx=10, pady=5)
        
        # Primera fila de botones principales
        row1_frame = ttk.Frame(control_frame)
        row1_frame.pack(fill='x', pady=2)
        
        ttk.Button(row1_frame, text="Actualizar Gráficos", 
                command=self.update_plots).pack(side="left", padx=5)
        ttk.Button(row1_frame, text="Guardar Gráficos", 
                command=self.save_plots).pack(side="left", padx=5)
        
        # Segunda fila - Análisis avanzados
        row2_frame = ttk.Frame(control_frame)
        row2_frame.pack(fill='x', pady=5)
        
        # BOTÓN K-FOLD PROMINENTE
        self.kfold_btn = ttk.Button(row2_frame, 
                                text="🔄 K-Fold Cross Validation", 
                                command=self.visualize_kfold,
                                width=25,
                                style="Accent.TButton")
        self.kfold_btn.pack(side='left', padx=5)
        
        # Estado del K-Fold
        self.kfold_status_label = ttk.Label(row2_frame, text="(Requiere modelo entrenado)", 
                                        foreground="gray")
        self.kfold_status_label.pack(side='left', padx=10)
        
        # Botón para limpiar
        ttk.Button(row2_frame, text="🧹 Limpiar", 
                command=self.clear_main_plots).pack(side='right', padx=5)
        
        # Frame para los gráficos principales
        self.plots_frame = ttk.Frame(results_frame)
        self.plots_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Crear figura de matplotlib
        self.fig, self.axes = plt.subplots(2, 3, figsize=(18, 12))
        self.fig.tight_layout(pad=3.0)
        
        # Canvas para mostrar los gráficos
        self.canvas = FigureCanvasTkAgg(self.fig, self.plots_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        
        # Inicializar estado del botón K-Fold
        self.update_kfold_button_state()
    
    def create_feature_analysis_tab(self):
        """Tab de análisis detallado de features"""
        analysis_frame = ttk.Frame(self.notebook)
        self.notebook.add(analysis_frame, text="🔍 Análisis Features")
        
        # Botones de control
        control_frame = ttk.Frame(analysis_frame)
        control_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Button(control_frame, text="Actualizar Análisis", 
                  command=self.update_feature_analysis).pack(side="left", padx=5)
        ttk.Button(control_frame, text="Exportar Feature Importance", 
                  command=self.export_feature_importance).pack(side="left", padx=5)
        ttk.Button(control_frame, text="Exportar Modelo RF", 
                  command=self.export_rf_model).pack(side="left", padx=5)
        
        # Crear notebook interno para diferentes análisis
        self.analysis_notebook = ttk.Notebook(analysis_frame)
        self.analysis_notebook.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Sub-tab 1: Feature Importance
        self.create_importance_subtab()
        
        # Sub-tab 2: Correlación de Features
        self.create_correlation_subtab()
        
        # Sub-tab 3: Métricas del Modelo
        self.create_model_metrics_subtab()
    
    def create_importance_subtab(self):
        """Sub-tab de importancia de features"""
        importance_frame = ttk.Frame(self.analysis_notebook)
        self.analysis_notebook.add(importance_frame, text="Feature Importance")
        
        # Área de gráfico de importancia
        self.importance_fig, self.importance_ax = plt.subplots(figsize=(12, 8))
        self.importance_canvas = FigureCanvasTkAgg(self.importance_fig, importance_frame)
        self.importance_canvas.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)
        
        # Tabla de importancia
        table_frame = ttk.LabelFrame(importance_frame, text="Top Features", padding="5")
        table_frame.pack(fill="x", padx=5, pady=5)
        
        # Crear tabla con scrollbar
        table_container = ttk.Frame(table_frame)
        table_container.pack(fill="both", expand=True)
        
        # Columnas de la tabla
        columns = ('Rank', 'Feature', 'Importance', 'Cumulative %')
        self.importance_tree = ttk.Treeview(table_container, columns=columns, show='headings', height=8)
        
        # Configurar encabezados
        self.importance_tree.heading('Rank', text='#')
        self.importance_tree.heading('Feature', text='Feature')
        self.importance_tree.heading('Importance', text='Importancia')
        self.importance_tree.heading('Cumulative %', text='Acumulado %')
        
        # Configurar anchos
        self.importance_tree.column('Rank', width=50, anchor='center')
        self.importance_tree.column('Feature', width=300, anchor='w')
        self.importance_tree.column('Importance', width=100, anchor='center')
        self.importance_tree.column('Cumulative %', width=100, anchor='center')
        
        # Scrollbar para tabla
        importance_scrollbar = ttk.Scrollbar(table_container, orient="vertical", 
                                           command=self.importance_tree.yview)
        self.importance_tree.configure(yscrollcommand=importance_scrollbar.set)
        
        self.importance_tree.pack(side="left", fill="both", expand=True)
        importance_scrollbar.pack(side="right", fill="y")

    def visualize_kfold(self):
        """Visualización de K-Fold Cross Validation con ventana separada"""
        if self.current_data is None or self.trained_model is None:
            messagebox.showwarning("Advertencia", "Carga datos y entrena un modelo primero")
            return
        
        try:
            # Actualizar estado
            self.kfold_status_label.config(text="🔄 Ejecutando K-Fold...", foreground="orange")
            self.kfold_btn.config(state="disabled")
            self.parent.update()
            
            # Preparar datos
            X = self.current_data[self.feature_columns]
            y = self.current_data[self.target_column]
            
            # Crear modelo con los mismos parámetros que el entrenado
            from sklearn.ensemble import RandomForestRegressor
            model = RandomForestRegressor(
                n_estimators=self.n_estimators_var.get(),
                random_state=self.random_state_var.get(),
                n_jobs=-1
            )
            
            # Llamar función de visualización K-Fold
            fig, results_df, stats = self.plot_kfold_results(model, X, y, cv_folds=5)
            
            # Mostrar en ventana separada
            plt.show()
            
            # Actualizar log en el área de resultados si existe
            if hasattr(self, 'results_text'):
                kfold_summary = f"""

    === K-FOLD CROSS VALIDATION COMPLETADO ===
    Fecha: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

    MÉTRICAS PROMEDIO (5-Fold):
    • MAE: {stats['mean_mae']:.4f} ± {stats['std_mae']:.4f}
    • RMSE: {stats['mean_rmse']:.4f} ± {stats['std_rmse']:.4f}
    • R²: {stats['mean_r2']:.4f} ± {stats['std_r2']:.4f}

    CONSISTENCIA:
    • Coef. Var. MAE: {(stats['std_mae']/stats['mean_mae']*100):.1f}%
    • Coef. Var. R²: {(stats['std_r2']/stats['mean_r2']*100):.1f}%

    INTERPRETACIÓN:
    • Calidad: {'Excelente' if stats['mean_r2'] > 0.9 else 'Buena' if stats['mean_r2'] > 0.7 else 'Moderada'}
    • Estabilidad: {'Alta' if stats['std_r2'] < 0.05 else 'Media' if stats['std_r2'] < 0.1 else 'Baja'}
    """
                self.results_text.insert(tk.END, kfold_summary)
            
            # Actualizar estado
            self.kfold_status_label.config(text="✅ K-Fold completado", foreground="green")
            
            return fig, results_df, stats
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en visualización K-Fold:\n{str(e)}")
            self.kfold_status_label.config(text="❌ Error en K-Fold", foreground="red")
            print(f"Error K-Fold: {str(e)}")
        finally:
            self.kfold_btn.config(state="normal")

    def plot_kfold_results(self, model, X, y, cv_folds=5):
        """
        Genera visualización completa de K-Fold Cross Validation
        
        Returns:
            fig: figura de matplotlib
            results_df: DataFrame con resultados por fold
            stats: diccionario con estadísticas
        """
        from sklearn.model_selection import KFold
        from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
        import matplotlib.pyplot as plt
        import seaborn as sns
        
        # Configurar K-Fold
        kfold = KFold(n_splits=cv_folds, shuffle=True, random_state=self.random_state_var.get())
        
        # Almacenar resultados
        fold_results = []
        all_y_true = []
        all_y_pred = []
        
        print(f"Iniciando {cv_folds}-Fold Cross Validation...")
        
        # Iterar por cada fold
        for fold_idx, (train_idx, test_idx) in enumerate(kfold.split(X), 1):
            print(f"Procesando Fold {fold_idx}/{cv_folds}...")
            
            # Dividir datos
            X_train_fold, X_test_fold = X.iloc[train_idx], X.iloc[test_idx]
            y_train_fold, y_test_fold = y.iloc[train_idx], y.iloc[test_idx]
            
            # Entrenar modelo
            fold_model = model.__class__(**model.get_params())
            fold_model.fit(X_train_fold, y_train_fold)
            
            # Predicciones
            y_pred_fold = fold_model.predict(X_test_fold)
            
            # Calcular métricas
            mae = mean_absolute_error(y_test_fold, y_pred_fold)
            rmse = np.sqrt(mean_squared_error(y_test_fold, y_pred_fold))
            r2 = r2_score(y_test_fold, y_pred_fold)
            
            # Guardar resultados
            fold_results.append({
                'fold': fold_idx,
                'mae': mae,
                'rmse': rmse,
                'r2': r2,
                'n_train': len(X_train_fold),
                'n_test': len(X_test_fold)
            })
            
            # Acumular predicciones para gráfico global
            all_y_true.extend(y_test_fold.values)
            all_y_pred.extend(y_pred_fold)
        
        # Crear DataFrame con resultados
        results_df = pd.DataFrame(fold_results)
        
        # Calcular estadísticas generales
        stats = {
            'mean_mae': results_df['mae'].mean(),
            'std_mae': results_df['mae'].std(),
            'mean_rmse': results_df['rmse'].mean(),
            'std_rmse': results_df['rmse'].std(),
            'mean_r2': results_df['r2'].mean(),
            'std_r2': results_df['r2'].std(),
            'cv_folds': cv_folds
        }
        
        # CREAR VISUALIZACIÓN
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle(f'{cv_folds}-Fold Cross Validation Results', fontsize=16, fontweight='bold')
        
        # 1. Métricas por Fold
        ax1 = axes[0, 0]
        x_pos = np.arange(len(results_df))
        ax1.bar(x_pos - 0.25, results_df['mae'], 0.25, label='MAE', alpha=0.8, color='red')
        ax1.bar(x_pos, results_df['rmse'], 0.25, label='RMSE', alpha=0.8, color='blue')
        ax1.bar(x_pos + 0.25, results_df['r2'] * 10, 0.25, label='R² × 10', alpha=0.8, color='green')
        ax1.set_xlabel('Fold')
        ax1.set_ylabel('Valor de Métrica')
        ax1.set_title('Métricas por Fold')
        ax1.set_xticks(x_pos)
        ax1.set_xticklabels([f'Fold {i+1}' for i in range(cv_folds)])
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Boxplot de métricas
        ax2 = axes[0, 1]
        metrics_data = [results_df['mae'], results_df['rmse'], results_df['r2']]
        ax2.boxplot(metrics_data, labels=['MAE', 'RMSE', 'R²'])
        ax2.set_title('Distribución de Métricas')
        ax2.set_ylabel('Valor')
        ax2.grid(True, alpha=0.3)
        
        # 3. Predicciones vs Reales (global)
        ax3 = axes[0, 2]
        ax3.scatter(all_y_true, all_y_pred, alpha=0.6, color='purple', s=30)
        min_val = min(min(all_y_true), min(all_y_pred))
        max_val = max(max(all_y_true), max(all_y_pred))
        ax3.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Predicción Perfecta')
        ax3.set_xlabel('Valores Reales')
        ax3.set_ylabel('Predicciones')
        ax3.set_title(f'Predicciones vs Reales (Global)\nR² = {r2_score(all_y_true, all_y_pred):.3f}')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # 4. Consistencia de R²
        ax4 = axes[1, 0]
        ax4.plot(range(1, cv_folds + 1), results_df['r2'], 'o-', linewidth=2, markersize=8, color='darkgreen')
        ax4.axhline(y=results_df['r2'].mean(), color='red', linestyle='--', alpha=0.7, label=f'Promedio: {results_df["r2"].mean():.3f}')
        ax4.fill_between(range(1, cv_folds + 1), 
                        results_df['r2'].mean() - results_df['r2'].std(),
                        results_df['r2'].mean() + results_df['r2'].std(),
                        alpha=0.2, color='red', label=f'±1 Desv.Est.')
        ax4.set_xlabel('Fold')
        ax4.set_ylabel('R² Score')
        ax4.set_title('Consistencia del R² por Fold')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        ax4.set_xticks(range(1, cv_folds + 1))
        
        # 5. Distribución de residuos (global)
        ax5 = axes[1, 1]
        residuals = np.array(all_y_true) - np.array(all_y_pred)
        ax5.hist(residuals, bins=20, alpha=0.7, color='orange', edgecolor='black')
        ax5.axvline(x=0, color='red', linestyle='--', linewidth=2)
        ax5.set_xlabel('Residuos (Real - Predicho)')
        ax5.set_ylabel('Frecuencia')
        ax5.set_title('Distribución de Residuos (Global)')
        ax5.grid(True, alpha=0.3)
        
        # 6. Tabla de estadísticas
        ax6 = axes[1, 2]
        ax6.axis('off')
        
        # Crear tabla de texto con estadísticas
        stats_text = f"""Estadísticas K-Fold Cross Validation

    Configuración:
    • Folds: {cv_folds}
    • Muestras totales: {len(X)}
    • Random State: {self.random_state_var.get()}

    Métricas Promedio:
    • MAE: {stats['mean_mae']:.4f} ± {stats['std_mae']:.4f}
    • RMSE: {stats['mean_rmse']:.4f} ± {stats['std_rmse']:.4f}
    • R²: {stats['mean_r2']:.4f} ± {stats['std_r2']:.4f}

    Consistencia del Modelo:
    • Coef. Var. MAE: {(stats['std_mae']/stats['mean_mae']*100):.1f}%
    • Coef. Var. R²: {(stats['std_r2']/stats['mean_r2']*100):.1f}%

    Interpretación:
    • Calidad: {'Excelente' if stats['mean_r2'] > 0.9 else 'Buena' if stats['mean_r2'] > 0.7 else 'Moderada'}
    • Estabilidad: {'Alta' if stats['std_r2'] < 0.05 else 'Media' if stats['std_r2'] < 0.1 else 'Baja'}
    """
        
        ax6.text(0.1, 0.9, stats_text, transform=ax6.transAxes, fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8),
                verticalalignment='top', fontfamily='monospace')
        
        plt.tight_layout()
        
        print(f"K-Fold completado:")
        print(f"  R²: {stats['mean_r2']:.3f} ± {stats['std_r2']:.3f}")
        print(f"  MAE: {stats['mean_mae']:.3f} ± {stats['std_mae']:.3f}")
        print(f"  RMSE: {stats['mean_rmse']:.3f} ± {stats['std_rmse']:.3f}")
        
        return fig, results_df, stats



    def clear_main_plots(self):
        """Limpiar los gráficos principales"""
        if hasattr(self, 'axes'):
            for ax in self.axes.flat:
                ax.clear()
                ax.text(0.5, 0.5, 'Gráfico limpio\nUsa los botones para visualizar', 
                    ha='center', va='center', transform=ax.transAxes, fontsize=12, 
                    bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
                ax.set_xticks([])
                ax.set_yticks([])
            
            if hasattr(self, 'canvas'):
                self.canvas.draw()
        
        print("Gráficos principales limpiados")    
    def create_correlation_subtab(self):
        """Sub-tab de correlación entre features"""
        correlation_frame = ttk.Frame(self.analysis_notebook)
        self.analysis_notebook.add(correlation_frame, text="Correlaciones")
        
        # Área de texto para correlaciones
        corr_text_frame = ttk.LabelFrame(correlation_frame, text="Correlaciones con Target", padding="10")
        corr_text_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.correlation_text = scrolledtext.ScrolledText(corr_text_frame, height=20, wrap='word')
        self.correlation_text.pack(fill="both", expand=True)
    
    def create_model_metrics_subtab(self):
        """Sub-tab de métricas detalladas del modelo"""
        metrics_frame = ttk.Frame(self.analysis_notebook)
        self.analysis_notebook.add(metrics_frame, text="Métricas del Modelo")
        
        # Área de métricas detalladas
        detailed_metrics_frame = ttk.LabelFrame(metrics_frame, text="Métricas Detalladas Random Forest", padding="10")
        detailed_metrics_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.detailed_metrics_text = scrolledtext.ScrolledText(detailed_metrics_frame, height=20, wrap='word')
        self.detailed_metrics_text.pack(fill="both", expand=True)
    
    def create_prediction_tab(self):
        """Tab de predicción"""
        pred_frame = ttk.Frame(self.notebook)
        self.notebook.add(pred_frame, text="🔮 Predicción")
        
        # Predicción individual
        single_group = ttk.LabelFrame(pred_frame, text="Predicción Individual", padding="10")
        single_group.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(single_group, text="Ingrese valores para las features principales:").pack(anchor='w')
        
        # Frame para inputs de features
        self.features_frame = ttk.Frame(single_group)
        self.features_frame.pack(fill='x', pady=10)
        
        ttk.Button(single_group, text="Predecir", command=self.predict_single).pack()
        
        # Resultados de predicción
        pred_results_group = ttk.LabelFrame(pred_frame, text="Resultados", padding="10")
        pred_results_group.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.prediction_text = scrolledtext.ScrolledText(pred_results_group, height=15, wrap='word')
        self.prediction_text.pack(fill='both', expand=True)
    
    def load_dataset(self):
        """Cargar dataset desde archivo"""
        file_path = filedialog.askopenfilename(
            title="Cargar Dataset",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
        )
        
        if file_path:
            try:
                if file_path.endswith('.xlsx'):
                    data = pd.read_excel(file_path)
                else:
                    data = pd.read_csv(file_path, index_col=0)
                
                self.load_dataset_from_dataframe(data)
                
            except Exception as e:
                messagebox.showerror("Error", f"Error cargando dataset:\n{str(e)}")
    
    def load_dataset_from_dataframe(self, data):
        """Cargar dataset desde un DataFrame"""
        try:
            self.current_data = data.copy()
            
            # Identificar columnas de texto y numéricas
            text_columns = []
            numeric_columns = []
            
            for col in data.columns:
                if data[col].dtype == 'object' or data[col].dtype.name == 'string':
                    text_columns.append(col)
                else:
                    numeric_columns.append(col)
            
            # Verificar que existe la columna target
            if self.target_column not in data.columns:
                raise ValueError(f"No se encontró la columna target '{self.target_column}' en el dataset")
            
            # Definir feature columns (numéricas, excluyendo target)
            self.feature_columns = [col for col in numeric_columns if col != self.target_column]
            
            if not self.feature_columns:
                raise ValueError("No se encontraron columnas numéricas para usar como features")
            
            # Actualizar información
            self.update_dataset_info(text_columns)
            
            # Notificar al callback
            self.data_loaded_callback(data)
            
            # Actualizar interfaz de predicción
            self.update_prediction_interface()
            
            messagebox.showinfo("Éxito", 
                               f"Dataset cargado exitosamente!\n\n"
                               f"Filas: {len(data)}\n"
                               f"Features numéricas: {len(self.feature_columns)}\n"
                               f"Columnas de texto excluidas: {len(text_columns)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error procesando dataset:\n{str(e)}")
    
    def update_dataset_info(self, text_columns):
        """Actualizar información del dataset"""
        if self.current_data is None:
            return
        
        info_lines = [
            "INFORMACIÓN DEL DATASET",
            "=" * 40,
            f"Filas: {len(self.current_data)}",
            f"Columnas totales: {len(self.current_data.columns)}",
            "",
            f"TARGET COLUMN: {self.target_column}",
            f"Valores únicos de target: {self.current_data[self.target_column].nunique()}",
            f"Rango de target: {self.current_data[self.target_column].min()} - {self.current_data[self.target_column].max()}",
            "",
            f"FEATURE COLUMNS ({len(self.feature_columns)}):",
            "-" * 20
        ]
        
        # Mostrar primeras 20 features
        for i, col in enumerate(self.feature_columns[:20]):
            info_lines.append(f"  {i+1:2d}. {col}")
        
        if len(self.feature_columns) > 20:
            info_lines.append(f"  ... y {len(self.feature_columns) - 20} más")
        
        if text_columns:
            info_lines.extend([
                "",
                f"COLUMNAS DE TEXTO EXCLUIDAS ({len(text_columns)}):",
                "-" * 25
            ])
            for col in text_columns:
                info_lines.append(f"  • {col}")
        
        # Estadísticas básicas del target
        target_stats = self.current_data[self.target_column].describe()
        info_lines.extend([
            "",
            "ESTADÍSTICAS DEL TARGET:",
            "-" * 25,
            f"  Media: {target_stats['mean']:.2f}",
            f"  Mediana: {target_stats['50%']:.2f}",
            f"  Desv. estándar: {target_stats['std']:.2f}",
            f"  Min: {target_stats['min']:.0f}",
            f"  Max: {target_stats['max']:.0f}"
        ])
        
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(1.0, "\n".join(info_lines))
    
    def update_kfold_button_state(self):
        """Actualizar estado del botón K-Fold según disponibilidad del modelo"""
        print(f"Debug - Modelo: {self.trained_model is not None}, Datos: {self.current_data is not None}")  # Línea de debug
        
        if hasattr(self, 'kfold_btn') and hasattr(self, 'kfold_status_label'):
            if self.trained_model is not None and self.current_data is not None:
                self.kfold_btn.config(state="normal")
                self.kfold_status_label.config(text="✅ Listo para K-Fold", foreground="green")
            else:
                self.kfold_btn.config(state="disabled") 
                self.kfold_status_label.config(text="⚠ Requiere modelo entrenado", foreground="red")
        else:
            print("Advertencia: botones K-Fold no inicializados")
    def train_model(self):
        """Entrenar modelo Random Forest"""
        if self.current_data is None:
            messagebox.showwarning("Advertencia", "Primero carga un dataset")
            return
        
        try:
            self.train_btn.config(state="disabled")
            
            # Preparar datos
            X = self.current_data[self.feature_columns]
            y = self.current_data[self.target_column]
            
            # Verificar que no hay valores NaN
            if X.isnull().any().any():
                from sklearn.impute import SimpleImputer
                imputer = SimpleImputer(strategy='median')
                X_clean = pd.DataFrame(imputer.fit_transform(X), columns=X.columns, index=X.index)
            else:
                X_clean = X
            
            # División train/test
            from sklearn.model_selection import train_test_split
            X_train, self.X_test, y_train, self.y_test = train_test_split(
                X_clean, y, 
                test_size=self.test_size_var.get(),
                random_state=self.random_state_var.get()
            )
            
            # Crear y entrenar modelo
            from sklearn.ensemble import RandomForestRegressor
            from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
            
            self.trained_model = RandomForestRegressor(
                n_estimators=self.n_estimators_var.get(),
                random_state=self.random_state_var.get(),
                n_jobs=-1
            )
            
            self.trained_model.fit(X_train, y_train)
            
            # Evaluar modelo
            train_pred = self.trained_model.predict(X_train)
            self.test_predictions = self.trained_model.predict(self.X_test)
            self.update_kfold_button_state()
            train_mae = mean_absolute_error(y_train, train_pred)
            test_mae = mean_absolute_error(self.y_test, self.test_predictions)
            train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))
            test_rmse = np.sqrt(mean_squared_error(self.y_test, self.test_predictions))
            train_r2 = r2_score(y_train, train_pred)
            test_r2 = r2_score(self.y_test, self.test_predictions)
            
            # Validación cruzada
            from sklearn.model_selection import cross_val_score
            cv_mae = -cross_val_score(self.trained_model, X_clean, y, cv=5, scoring='neg_mean_absolute_error')
            cv_r2 = cross_val_score(self.trained_model, X_clean, y, cv=5, scoring='r2')
            
            # Feature importance
            self.feature_importance = pd.DataFrame({
                'feature': self.feature_columns,
                'importance': self.trained_model.feature_importances_
            }).sort_values('importance', ascending=False)
            
            # Mostrar resultados de texto
            results_text = f"""RESULTADOS DEL ENTRENAMIENTO
===========================

CONFIGURACIÓN:
  Random Forest con {self.n_estimators_var.get()} estimadores
  Test size: {self.test_size_var.get():.1%}
  Features utilizadas: {len(self.feature_columns)}
  Muestras de entrenamiento: {len(X_train)}
  Muestras de prueba: {len(self.X_test)}

MÉTRICAS DE RENDIMIENTO:
  Train MAE:  {train_mae:.3f}
  Test MAE:   {test_mae:.3f}
  Train RMSE: {train_rmse:.3f}
  Test RMSE:  {test_rmse:.3f}
  Train R²:   {train_r2:.3f}
  Test R²:    {test_r2:.3f}

VALIDACIÓN CRUZADA (5-fold):
  CV MAE:  {cv_mae.mean():.3f} ± {cv_mae.std():.3f}
  CV R²:   {cv_r2.mean():.3f} ± {cv_r2.std():.3f}

TOP 15 FEATURES MÁS IMPORTANTES:
"""
            
            for i, row in self.feature_importance.head(15).iterrows():
                results_text += f"  {row['feature'][:40]:40s}: {row['importance']:.4f}\n"
            
            results_text += f"""

INTERPRETACIÓN:
  {'🟢 Excelente' if test_r2 > 0.9 else '🟡 Bueno' if test_r2 > 0.7 else '🔴 Mejorable'} (R² = {test_r2:.3f})
  {'🟢 Bajo error' if test_mae < 5 else '🟡 Error moderado' if test_mae < 10 else '🔴 Error alto'} (MAE = {test_mae:.1f})
"""
            
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(1.0, results_text)
            self.update_kfold_button_state()
            # Habilitar botón de guardado
            self.save_btn.config(state="normal")
            
            # Actualizar gráficos
            self.update_plots()
            
            # Cambiar al tab de resultados para mostrar gráficos
            self.notebook.select(2)  # Tab de Resultados
            
            # Actualizar interfaz de predicción con features importantes
            self.update_prediction_interface_with_importance()
            
            messagebox.showinfo("Entrenamiento Completado", 
                               f"Modelo entrenado exitosamente!\n\n"
                               f"Test R²: {test_r2:.3f}\n"
                               f"Test MAE: {test_mae:.3f}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error entrenando modelo:\n{str(e)}")
        finally:
            self.train_btn.config(state="normal")
    
    def update_feature_analysis(self):
        """Actualizar análisis de features"""
        if self.trained_model is None or not hasattr(self, 'feature_importance'):
            messagebox.showwarning("Advertencia", "Primero entrena un modelo")
            return
        
        try:
            # Actualizar gráfico de importancia
            self.update_importance_plot()
            
            # Actualizar tabla de importancia
            self.update_importance_table()
            
            # Actualizar correlaciones
            self.update_correlations()
            
            # Actualizar métricas detalladas
            self.update_detailed_metrics()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error actualizando análisis:\n{str(e)}")

    def update_importance_plot(self):
        """Actualizar gráfico de importancia de features"""
        self.importance_ax.clear()
        
        # Tomar top 20 features
        top_features = self.feature_importance.head(20)
        
        # Crear gráfico de barras horizontales
        bars = self.importance_ax.barh(range(len(top_features)), top_features['importance'], 
                                      color='steelblue', alpha=0.8)
        
        # Configurar ejes
        self.importance_ax.set_yticks(range(len(top_features)))
        self.importance_ax.set_yticklabels(top_features['feature'], fontsize=10)
        self.importance_ax.set_xlabel('Importancia', fontsize=12)
        self.importance_ax.set_title('Top 20 importancias de features (RF)', fontsize=14, fontweight='bold')
        
        # Invertir eje Y para mostrar más importante arriba
        self.importance_ax.invert_yaxis()
        
        # Agregar valores en las barras
        for i, bar in enumerate(bars):
            width = bar.get_width()
            self.importance_ax.text(width + 0.001, bar.get_y() + bar.get_height()/2, 
                                  f'{width:.3f}', ha='left', va='center', fontsize=9)
        
        # Mejorar apariencia
        self.importance_ax.grid(axis='x', alpha=0.3)
        self.importance_ax.spines['top'].set_visible(False)
        self.importance_ax.spines['right'].set_visible(False)
        
        self.importance_fig.tight_layout()
        self.importance_canvas.draw()
    
    def update_importance_table(self):
        """Actualizar tabla de importancia"""
        # Limpiar tabla anterior
        for item in self.importance_tree.get_children():
            self.importance_tree.delete(item)
        
        # Calcular porcentaje acumulativo
        cumulative_importance = np.cumsum(self.feature_importance['importance'])
        total_importance = cumulative_importance.iloc[-1]
        cumulative_percent = (cumulative_importance / total_importance) * 100
        
        # Llenar tabla con todas las features
        for i, (_, row) in enumerate(self.feature_importance.iterrows()):
            self.importance_tree.insert('', 'end', values=(
                i + 1,
                row['feature'],
                f"{row['importance']:.4f}",
                f"{cumulative_percent.iloc[i]:.1f}%"
            ))
    
    def update_correlations(self):
        """Actualizar análisis de correlaciones"""
        if self.current_data is None:
            return
        
        # Calcular correlaciones con el target
        correlations = self.current_data[self.feature_columns + [self.target_column]].corr()[self.target_column]
        correlations = correlations.drop(self.target_column).sort_values(key=abs, ascending=False)
        
        # Generar texto de correlaciones
        corr_text = """CORRELACIONES CON TARGET (VACANCIES)
=====================================

Las correlaciones muestran la relación lineal entre cada feature y el target.
Valores cercanos a ±1 indican fuerte correlación, cercanos a 0 indican poca correlación.

TOP 20 CORRELACIONES MÁS ALTAS:
"""
        
        for i, (feature, corr) in enumerate(correlations.head(20).items()):
            direction = "Positiva" if corr > 0 else "Negativa"
            strength = "Muy fuerte" if abs(corr) > 0.8 else "Fuerte" if abs(corr) > 0.6 else "Moderada" if abs(corr) > 0.4 else "Débil"
            corr_text += f"{i+1:2d}. {feature[:40]:40s}: {corr:+.4f} ({direction}, {strength})\n"
        
        corr_text += "\n\nTOP 10 CORRELACIONES MÁS BAJAS (MENOS INFORMATIVAS):\n"
        
        for i, (feature, corr) in enumerate(correlations.tail(10).items()):
            corr_text += f"{i+1:2d}. {feature[:40]:40s}: {corr:+.4f}\n"
        
        # Estadísticas de correlaciones
        corr_text += f"""

ESTADÍSTICAS DE CORRELACIONES:
  Media absoluta: {abs(correlations).mean():.4f}
  Mediana absoluta: {abs(correlations).median():.4f}
  Máxima correlación: {correlations.max():.4f} ({correlations.idxmax()})
  Mínima correlación: {correlations.min():.4f} ({correlations.idxmin()})
  
  Features con correlación > 0.5: {sum(abs(correlations) > 0.5)}
  Features con correlación > 0.7: {sum(abs(correlations) > 0.7)}
  Features con correlación > 0.9: {sum(abs(correlations) > 0.9)}
"""
        
        self.correlation_text.delete(1.0, tk.END)
        self.correlation_text.insert(1.0, corr_text)
    
    def update_detailed_metrics(self):
        """Actualizar métricas detalladas del modelo"""
        if self.trained_model is None:
            return
        
        # Obtener información detallada del Random Forest
        rf_info = f"""INFORMACIÓN DETALLADA DEL RANDOM FOREST
======================================

CONFIGURACIÓN DEL MODELO:
  Número de estimadores: {self.trained_model.n_estimators}
  Criterio de división: {self.trained_model.criterion}
  Profundidad máxima: {self.trained_model.max_depth if self.trained_model.max_depth else 'Sin límite'}
  Min muestras por split: {self.trained_model.min_samples_split}
  Min muestras por hoja: {self.trained_model.min_samples_leaf}
  Max features por split: {self.trained_model.max_features}
  Bootstrap: {'Sí' if self.trained_model.bootstrap else 'No'}
  Random state: {self.trained_model.random_state}

ESTADÍSTICAS DE LOS ÁRBOLES:
"""
        
        if hasattr(self.trained_model, 'estimators_'):
            tree_depths = [tree.tree_.max_depth for tree in self.trained_model.estimators_]
            tree_nodes = [tree.tree_.node_count for tree in self.trained_model.estimators_]
            tree_leaves = [tree.tree_.n_leaves for tree in self.trained_model.estimators_]
            
            rf_info += f"""  Profundidad promedio: {np.mean(tree_depths):.1f} ± {np.std(tree_depths):.1f}
  Profundidad mínima: {min(tree_depths)}
  Profundidad máxima: {max(tree_depths)}
  
  Nodos promedio por árbol: {np.mean(tree_nodes):.1f} ± {np.std(tree_nodes):.1f}
  Hojas promedio por árbol: {np.mean(tree_leaves):.1f} ± {np.std(tree_leaves):.1f}

ANÁLISIS DE FEATURES:
  Total features disponibles: {len(self.feature_columns)}
  Features con importancia > 0.01: {sum(self.feature_importance['importance'] > 0.01)}
  Features con importancia > 0.05: {sum(self.feature_importance['importance'] > 0.05)}
  Features con importancia > 0.10: {sum(self.feature_importance['importance'] > 0.10)}
  
  Top 5 features representan: {self.feature_importance.head(5)['importance'].sum():.1%} de la importancia
  Top 10 features representan: {self.feature_importance.head(10)['importance'].sum():.1%} de la importancia
  Top 20 features representan: {self.feature_importance.head(20)['importance'].sum():.1%} de la importancia
"""
        
        # Información de rendimiento si está disponible
        if self.X_test is not None and self.y_test is not None:
            # Calcular métricas adicionales
            from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, explained_variance_score
            
            mae = mean_absolute_error(self.y_test, self.test_predictions)
            rmse = np.sqrt(mean_squared_error(self.y_test, self.test_predictions))
            r2 = r2_score(self.y_test, self.test_predictions)
            evs = explained_variance_score(self.y_test, self.test_predictions)
            
            # Error percentual absoluto medio (MAPE)
            mape = np.mean(np.abs((self.y_test - self.test_predictions) / self.y_test)) * 100
            
            # Error mediano absoluto
            median_ae = np.median(np.abs(self.y_test - self.test_predictions))
            
            rf_info += f"""

MÉTRICAS DE RENDIMIENTO DETALLADAS:
  R² Score: {r2:.6f}
  Explained Variance Score: {evs:.6f}
  Mean Absolute Error: {mae:.4f}
  Root Mean Squared Error: {rmse:.4f}
  Mean Absolute Percentage Error: {mape:.2f}%
  Median Absolute Error: {median_ae:.4f}
  
  Error estándar: {np.std(self.y_test - self.test_predictions):.4f}
  Error mínimo: {np.min(np.abs(self.y_test - self.test_predictions)):.4f}
  Error máximo: {np.max(np.abs(self.y_test - self.test_predictions)):.4f}

DISTRIBUCIÓN DE ERRORES:
  25% de predicciones tienen error < {np.percentile(np.abs(self.y_test - self.test_predictions), 25):.2f}
  50% de predicciones tienen error < {np.percentile(np.abs(self.y_test - self.test_predictions), 50):.2f}
  75% de predicciones tienen error < {np.percentile(np.abs(self.y_test - self.test_predictions), 75):.2f}
  90% de predicciones tienen error < {np.percentile(np.abs(self.y_test - self.test_predictions), 90):.2f}
  95% de predicciones tienen error < {np.percentile(np.abs(self.y_test - self.test_predictions), 95):.2f}
"""
        
        self.detailed_metrics_text.delete(1.0, tk.END)
        self.detailed_metrics_text.insert(1.0, rf_info)
    
    def export_feature_importance(self):
        """Exportar tabla de feature importance"""
        if not hasattr(self, 'feature_importance'):
            messagebox.showwarning("Advertencia", "No hay feature importance para exportar")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Exportar Feature Importance",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
        )
        
        if file_path:
            try:
                # Añadir porcentaje acumulativo
                cumulative_importance = np.cumsum(self.feature_importance['importance'])
                total_importance = cumulative_importance.iloc[-1]
                cumulative_percent = (cumulative_importance / total_importance) * 100
                
                export_df = self.feature_importance.copy()
                export_df['cumulative_importance'] = cumulative_importance
                export_df['cumulative_percent'] = cumulative_percent
                export_df['rank'] = range(1, len(export_df) + 1)
                
                # Reordenar columnas
                export_df = export_df[['rank', 'feature', 'importance', 'cumulative_importance', 'cumulative_percent']]
                
                if file_path.endswith('.xlsx'):
                    export_df.to_excel(file_path, index=False)
                else:
                    export_df.to_csv(file_path, index=False)
                
                messagebox.showinfo("Éxito", f"Feature importance exportado a:\n{file_path}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Error exportando feature importance:\n{str(e)}")
    
    def export_rf_model(self):
        """Exportar modelo Random Forest completo con metadatos"""
        if self.trained_model is None:
            messagebox.showwarning("Advertencia", "No hay modelo entrenado para exportar")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Exportar Modelo Random Forest",
            defaultextension=".joblib",
            filetypes=[("Joblib files", "*.joblib")]
        )
        
        if file_path:
            try:
                import joblib
                from datetime import datetime
                
                # Crear paquete completo del modelo
                model_package = {
                    'model': self.trained_model,
                    'feature_columns': self.feature_columns,
                    'target_column': self.target_column,
                    'feature_importance': self.feature_importance,
                    'training_params': {
                        'n_estimators': self.n_estimators_var.get(),
                        'test_size': self.test_size_var.get(),
                        'random_state': self.random_state_var.get()
                    },
                    'model_info': {
                        'n_features': len(self.feature_columns),
                        'n_samples_train': len(self.current_data) if self.current_data is not None else None,
                        'training_date': datetime.now().isoformat(),
                        'model_type': 'RandomForestRegressor',
                        'sklearn_version': None  # Se puede añadir si se importa sklearn
                    }
                }
                
                # Añadir métricas de rendimiento si están disponibles
                if self.X_test is not None and self.y_test is not None:
                    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
                    
                    mae = mean_absolute_error(self.y_test, self.test_predictions)
                    rmse = np.sqrt(mean_squared_error(self.y_test, self.test_predictions))
                    r2 = r2_score(self.y_test, self.test_predictions)
                    
                    model_package['performance_metrics'] = {
                        'test_mae': mae,
                        'test_rmse': rmse,
                        'test_r2': r2,
                        'n_test_samples': len(self.X_test)
                    }
                
                # Guardar modelo
                joblib.dump(model_package, file_path)
                
                messagebox.showinfo("Éxito", 
                                   f"Modelo Random Forest exportado exitosamente!\n\n"
                                   f"Archivo: {file_path}\n"
                                   f"Incluye: modelo, features, importancia, métricas\n"
                                   f"Features: {len(self.feature_columns)}\n"
                                   f"Estimadores: {self.trained_model.n_estimators}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Error exportando modelo:\n{str(e)}")
    
    def update_plots(self):
        """Actualizar todos los gráficos con residuos normalizados"""
        if self.trained_model is None or self.X_test is None:
            # Limpiar gráficos si no hay modelo
            for ax in self.axes.flat:
                ax.clear()
                ax.text(0.5, 0.5, 'Entrena un modelo\npara ver gráficos', 
                       ha='center', va='center', transform=ax.transAxes, fontsize=12)
                ax.set_xticks([])
                ax.set_yticks([])
            self.canvas.draw()
            return
        
        try:
            # Limpiar gráficos anteriores
            for ax in self.axes.flat:
                ax.clear()
            
            # Configurar estilo
            plt.style.use('default')
            sns.set_palette("husl")
            
            # CALCULAR RESIDUOS NORMALIZADOS: 1 - pred/real
            # Evitar división por cero
            y_test_safe = self.y_test.copy()
            y_test_safe[y_test_safe == 0] = 1e-10  # Reemplazar ceros con valor muy pequeño
            
            normalized_residuals = 1 - (self.test_predictions / y_test_safe)
            
            # 1. Predicciones vs Valores Reales
            ax1 = self.axes[0, 0]
            ax1.scatter(self.y_test, self.test_predictions, alpha=0.6, color='red', s=50)
            
            # Línea diagonal perfecta
            min_val = min(self.y_test.min(), self.test_predictions.min())
            max_val = max(self.y_test.max(), self.test_predictions.max())
            ax1.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Predicción perfecta')
            
            ax1.set_xlabel('Valores Reales (y_true)')
            ax1.set_ylabel('Predicciones (y_pred)')
            ax1.set_title('Predicciones vs Valores Reales')
            ax1.legend()
            ax1.grid(True, alpha=0.3)
            
            # Calcular y mostrar métricas
            from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
            r2 = r2_score(self.y_test, self.test_predictions)
            mae = mean_absolute_error(self.y_test, self.test_predictions)
            rmse = np.sqrt(mean_squared_error(self.y_test, self.test_predictions))
            
            ax1.text(0.05, 0.95, f'R² = {r2:.3f}\nMAE = {mae:.3f}\nRMSE = {rmse:.3f}', 
                    transform=ax1.transAxes, bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
                    verticalalignment='top')
            
            # 2. Gráfico de Residuos NORMALIZADOS
            ax2 = self.axes[0, 1]
            ax2.scatter(self.test_predictions, normalized_residuals, alpha=0.6, color='red', s=50)
            ax2.axhline(y=0, color='red', linestyle='--', linewidth=2)
            ax2.set_xlabel('Valores Predichos (y_pred)')
            ax2.set_ylabel('Residuos Normalizados (1 - pred/real)')
            ax2.set_title('Gráfico de Residuos Normalizados')
            ax2.grid(True, alpha=0.3)
            
            # 3. Distribución de Residuos NORMALIZADOS
            ax3 = self.axes[0, 2]
            ax3.hist(normalized_residuals, bins=20, alpha=0.7, color='red', edgecolor='black')
            ax3.axvline(x=0, color='red', linestyle='--', linewidth=2)
            ax3.set_xlabel('Residuos Normalizados')
            ax3.set_ylabel('Frecuencia')
            ax3.set_title('Distribución de Residuos Normalizados')
            ax3.grid(True, alpha=0.3)
            
            # 4. Serie de Predicciones por Muestra
            ax4 = self.axes[1, 0]
            indices = range(len(self.y_test))
            ax4.plot(indices, self.y_test.values, 'o-', label='Valores Reales', color='orange', alpha=0.7)
            ax4.plot(indices, self.test_predictions, 'o-', label='Predicciones', color='blue', alpha=0.7)
            ax4.set_xlabel('Índice de Muestra')
            ax4.set_ylabel('Valor')
            ax4.set_title('Serie de Predicciones por Muestra')
            ax4.legend()
            ax4.grid(True, alpha=0.3)
            
            # 5. Errores Absolutos NORMALIZADOS por Muestra
            ax5 = self.axes[1, 1]
            abs_normalized_errors = np.abs(normalized_residuals)
            ax5.bar(indices, abs_normalized_errors, alpha=0.7, color='purple')
            ax5.set_xlabel('Índice de Muestra')
            ax5.set_ylabel('Error Absoluto Normalizado')
            ax5.set_title('Errores Absolutos Normalizados por Muestra')
            ax5.grid(True, alpha=0.3)
            
            # 6. Métricas de Evaluación ACTUALIZADAS
            ax6 = self.axes[1, 2]
            ax6.axis('off')  # Sin ejes para este panel
            
            # Calcular métricas adicionales con residuos normalizados
            mean_norm_error = np.mean(np.abs(normalized_residuals))
            std_norm_error = np.std(normalized_residuals)
            max_norm_error = np.max(abs_normalized_errors)
            
            # MAPE usando la fórmula original
            mape = np.mean(np.abs((self.y_test - self.test_predictions) / self.y_test)) * 100 if (self.y_test != 0).all() else 0
            
            metrics_text = f"""Métricas de Evaluación

MAE: {mae:.4f}
RMSE: {rmse:.4f}
R²: {r2:.4f}
MAPE: {mape:.2f}%
Max Error: {np.max(np.abs(self.y_test - self.test_predictions)):.4f}

Residuos Normalizados:
Mean |Error Norm|: {mean_norm_error:.4f}
Std Error Norm: {std_norm_error:.4f}
Max Error Norm: {max_norm_error:.4f}

Muestras: {len(self.y_test)}
Rango real: [{self.y_test.min():.2f}, {self.y_test.max():.2f}]
Rango pred: [{self.test_predictions.min():.2f}, {self.test_predictions.max():.2f}]"""
            
            ax6.text(0.1, 0.9, metrics_text, transform=ax6.transAxes, fontsize=10,
                    bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8),
                    verticalalignment='top', fontfamily='monospace')
            
            # Ajustar layout
            self.fig.tight_layout(pad=2.0)
            self.canvas.draw()
            
            # Actualizar análisis de features si está disponible
            if hasattr(self, 'update_feature_analysis'):
                self.update_feature_analysis()
            
        except Exception as e:
            print(f"Error actualizando gráficos: {e}")
    
    def save_plots(self):
        """Guardar gráficos como imagen"""
        if self.trained_model is None:
            messagebox.showwarning("Advertencia", "No hay gráficos para guardar")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Guardar Gráficos",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("PDF files", "*.pdf"), ("SVG files", "*.svg")]
        )
        
        if file_path:
            try:
                self.fig.savefig(file_path, dpi=300, bbox_inches='tight')
                messagebox.showinfo("Éxito", f"Gráficos guardados en:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Error guardando gráficos:\n{str(e)}")
    
    def update_prediction_interface(self):
        """Actualizar interfaz de predicción con features principales"""
        # Limpiar frame anterior
        for widget in self.features_frame.winfo_children():
            widget.destroy()
        
        # Mostrar las primeras 10 features
        display_features = self.feature_columns[:10]
        self.feature_vars = {}
        
        for i, feature in enumerate(display_features):
            row = i // 2
            col = (i % 2) * 3
            
            ttk.Label(self.features_frame, text=f"{feature}:").grid(row=row, column=col, sticky='w', padx=5, pady=2)
            
            var = tk.DoubleVar(value=0.0)
            self.feature_vars[feature] = var
            
            entry = ttk.Entry(self.features_frame, textvariable=var, width=15)
            entry.grid(row=row, column=col+1, padx=5, pady=2)
    
    def update_prediction_interface_with_importance(self):
        """Actualizar interfaz de predicción con features más importantes"""
        if not hasattr(self, 'feature_importance'):
            return
        
        # Limpiar frame anterior
        for widget in self.features_frame.winfo_children():
            widget.destroy()
        
        # Mostrar top 10 features más importantes
        top_features = self.feature_importance.head(10)['feature'].tolist()
        self.feature_vars = {}
        
        for i, feature in enumerate(top_features):
            row = i // 2
            col = (i % 2) * 3
            
            # Obtener valor promedio para sugerir
            avg_value = self.current_data[feature].mean()
            
            label_text = f"{feature} (avg: {avg_value:.2f}):"
            ttk.Label(self.features_frame, text=label_text).grid(row=row, column=col, sticky='w', padx=5, pady=2)
            
            var = tk.DoubleVar(value=avg_value)
            self.feature_vars[feature] = var
            
            entry = ttk.Entry(self.features_frame, textvariable=var, width=15)
            entry.grid(row=row, column=col+1, padx=5, pady=2)
    
    def predict_single(self):
        """Realizar predicción individual"""
        if self.trained_model is None:
            messagebox.showwarning("Advertencia", "Primero entrena un modelo")
            return
        
        try:
            # Crear vector de features con valores por defecto
            feature_vector = []
            input_features = []
            
            for feature in self.feature_columns:
                if feature in self.feature_vars:
                    value = self.feature_vars[feature].get()
                    input_features.append(f"{feature}: {value:.3f}")
                else:
                    value = self.current_data[feature].mean()
                
                feature_vector.append(value)
            
            # Realizar predicción
            X_pred = np.array(feature_vector).reshape(1, -1)
            prediction = self.trained_model.predict(X_pred)[0]
            
            # Obtener intervalo de confianza aproximado
            tree_predictions = [tree.predict(X_pred)[0] for tree in self.trained_model.estimators_]
            pred_std = np.std(tree_predictions)
            
            # Mostrar resultado
            result_text = f"""PREDICCIÓN INDIVIDUAL
====================

VALORES DE ENTRADA (top features):
"""
            
            for input_feat in input_features:
                result_text += f"  • {input_feat}\n"
            
            result_text += f"""

RESULTADO:
  Vacancias predichas: {prediction:.2f}
  Rango estimado: {prediction - 1.96*pred_std:.2f} - {prediction + 1.96*pred_std:.2f}
  Incertidumbre: ± {1.96*pred_std:.2f}

INTERPRETACIÓN:
  El modelo predice {prediction:.0f} vacancias con una 
  incertidumbre de ±{1.96*pred_std:.1f} vacancias (95% confianza).
"""
            
            self.prediction_text.delete(1.0, tk.END)
            self.prediction_text.insert(1.0, result_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en predicción:\n{str(e)}")
    
    def save_model(self):
        """Guardar modelo entrenado"""
        if self.trained_model is None:
            messagebox.showwarning("Advertencia", "No hay modelo entrenado")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Guardar Modelo",
            defaultextension=".joblib",
            filetypes=[("Joblib files", "*.joblib")]
        )
        
        if file_path:
            try:
                import joblib
                
                # Guardar modelo con metadatos
                model_data = {
                    'model': self.trained_model,
                    'feature_columns': self.feature_columns,
                    'target_column': self.target_column,
                    'training_params': {
                        'n_estimators': self.n_estimators_var.get(),
                        'test_size': self.test_size_var.get(),
                        'random_state': self.random_state_var.get()
                    },
                    'feature_importance': self.feature_importance if hasattr(self, 'feature_importance') else None
                }
                
                joblib.dump(model_data, file_path)
                messagebox.showinfo("Éxito", f"Modelo guardado en:\n{file_path}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Error guardando modelo:\n{str(e)}")
    
    def load_model(self):
        """Cargar modelo previamente entrenado"""
        file_path = filedialog.askopenfilename(
            title="Cargar Modelo",
            filetypes=[("Joblib files", "*.joblib")]
        )
        
        if file_path:
            try:
                import joblib
                
                model_data = joblib.load(file_path)
                
                if isinstance(model_data, dict):
                    self.trained_model = model_data['model']
                    
                    # Verificar compatibilidad de features
                    saved_features = model_data.get('feature_columns', [])
                    if self.current_data is not None:
                        missing_features = set(saved_features) - set(self.current_data.columns)
                        if missing_features:
                            messagebox.showwarning("Advertencia", 
                                                 f"El dataset actual no tiene las features:\n{missing_features}")
                        else:
                            self.feature_columns = saved_features
                    else:
                        self.feature_columns = saved_features
                    
                    # Restaurar parámetros
                    params = model_data.get('training_params', {})
                    self.n_estimators_var.set(params.get('n_estimators', 100))
                    self.test_size_var.set(params.get('test_size', 0.2))
                    self.random_state_var.set(params.get('random_state', 42))
                    
                    # Restaurar feature importance si está disponible
                    if 'feature_importance' in model_data:
                        self.feature_importance = model_data['feature_importance']
                    
                    self.save_btn.config(state="normal")
                    messagebox.showinfo("Éxito", f"Modelo cargado desde:\n{file_path}")
                    
                else:
                    # Modelo legacy sin metadatos
                    self.trained_model = model_data
                    messagebox.showinfo("Éxito", "Modelo legacy cargado")
                
            except Exception as e:
                messagebox.showerror("Error", f"Error cargando modelo:\n{str(e)}")
    
    def export_model(self):
        """Exportar modelo (wrapper para compatibilidad)"""
        self.save_model()
    
    def reset(self):
        """Reset del tab"""
        self.current_data = None
        self.trained_model = None
        self.feature_columns = []
        self.X_test = None
        self.y_test = None
        self.test_predictions = None
        
        # Reset displays
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(1.0, "Carga un dataset para comenzar")
        
        self.results_text.delete(1.0, tk.END)
        self.prediction_text.delete(1.0, tk.END)
        
        # Reset botones
        self.save_btn.config(state="disabled")
        
        # Limpiar interfaz de predicción
        for widget in self.features_frame.winfo_children():
            widget.destroy()
        
        # Limpiar gráficos
        for ax in self.axes.flat:
            ax.clear()
            ax.text(0.5, 0.5, 'Carga un dataset\ny entrena un modelo', 
                   ha='center', va='center', transform=ax.transAxes, fontsize=12)
            ax.set_xticks([])
            ax.set_yticks([])
        self.canvas.draw()


# Función adicional para crear gráfico de feature importance como en tu imagen
def create_feature_importance_plot():
    """Crear gráfico separado de feature importance (similar a tu imagen)"""
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    def plot_feature_importance_standalone(feature_importance_df, top_n=20):
        """
        Crear gráfico de barras horizontales de feature importance
        Parámetros:
        - feature_importance_df: DataFrame con columnas 'feature' e 'importance'  
        - top_n: número de features a mostrar
        """
        # Configurar estilo
        plt.style.use('default')
        sns.set_palette("husl")
        
        # Tomar top N features
        top_features = feature_importance_df.head(top_n)
        
        # Crear figura
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Crear gráfico de barras horizontales
        bars = ax.barh(range(len(top_features)), top_features['importance'], 
                      color='steelblue', alpha=0.8)
        
        # Configurar ejes
        ax.set_yticks(range(len(top_features)))
        ax.set_yticklabels(top_features['feature'])
        ax.set_xlabel('Importancia', fontsize=12)
        ax.set_title(f'Top {top_n} importancias de features (RF)', fontsize=14, fontweight='bold')
        
        # Invertir eje Y para mostrar más importante arriba
        ax.invert_yaxis()
        
        # Agregar valores en las barras
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax.text(width + 0.001, bar.get_y() + bar.get_height()/2, 
                   f'{width:.3f}', ha='left', va='center', fontsize=9)
        
        # Mejorar apariencia
        ax.grid(axis='x', alpha=0.3)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        plt.tight_layout()
        return fig, ax
    
    return plot_feature_importance_standalone


# Ejemplo de uso principal
if __name__ == "__main__":
    """
    Ejemplo de cómo usar la clase AdvancedMLTabWithPlots
    """
    import tkinter as tk
    from tkinter import ttk
    
    def data_callback(data):
        print(f"Dataset cargado: {data.shape}")
    
    # Crear ventana principal
    root = tk.Tk()
    root.title("Advanced ML with Plots - Ejemplo")
    root.geometry("1400x900")
    
    # Crear notebook
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Crear instancia del tab avanzado
    ml_tab = AdvancedMLTabWithPlots(notebook, data_callback)
    notebook.add(ml_tab.frame, text="Advanced ML")
    
    # Iniciar aplicación
    root.mainloop()


# Funciones auxiliares adicionales para análisis
def calculate_feature_stability(model, X_data, y_data, n_bootstraps=100):
    """
    Calcular estabilidad de importancia de features usando bootstrap
    
    Parámetros:
    - model: modelo Random Forest entrenado
    - X_data: datos de features para bootstrap
    - y_data: datos de target correspondientes
    - n_bootstraps: número de iteraciones bootstrap
    
    Retorna:
    - DataFrame con estadísticas de estabilidad por feature
    """
    from sklearn.utils import resample
    
    feature_importances = []
    
    for _ in range(n_bootstraps):
        # Bootstrap sample
        X_bootstrap, y_bootstrap = resample(X_data, y_data, random_state=None)
        
        # Re-entrenar modelo en muestra bootstrap
        bootstrap_model = type(model)(**model.get_params())
        bootstrap_model.fit(X_bootstrap, y_bootstrap)
        
        # Guardar importancias
        feature_importances.append(bootstrap_model.feature_importances_)
    
    # Convertir a DataFrame
    importances_df = pd.DataFrame(feature_importances, columns=X_data.columns)
    
    # Calcular estadísticas
    stability_stats = pd.DataFrame({
        'feature': X_data.columns,
        'mean_importance': importances_df.mean(),
        'std_importance': importances_df.std(),
        'cv_importance': importances_df.std() / importances_df.mean(),  # Coeficiente de variación
        'min_importance': importances_df.min(),
        'max_importance': importances_df.max()
    }).sort_values('mean_importance', ascending=False)
    
    return stability_stats


def generate_model_report(ml_tab_instance, output_path=None):
    """
    Generar reporte completo del modelo en formato texto
    
    Parámetros:
    - ml_tab_instance: instancia de AdvancedMLTabWithPlots
    - output_path: ruta para guardar reporte (opcional)
    
    Retorna:
    - String con reporte completo
    """
    if ml_tab_instance.trained_model is None:
        return "No hay modelo entrenado para generar reporte"
    
    from datetime import datetime
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    
    # Calcular métricas
    mae = mean_absolute_error(ml_tab_instance.y_test, ml_tab_instance.test_predictions)
    rmse = np.sqrt(mean_squared_error(ml_tab_instance.y_test, ml_tab_instance.test_predictions))
    r2 = r2_score(ml_tab_instance.y_test, ml_tab_instance.test_predictions)
    
    # Calcular residuos normalizados
    y_test_safe = ml_tab_instance.y_test.copy()
    y_test_safe[y_test_safe == 0] = 1e-10
    normalized_residuals = 1 - (ml_tab_instance.test_predictions / y_test_safe)
    
    report = f"""
REPORTE DE MODELO RANDOM FOREST
===============================
Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

CONFIGURACIÓN DEL MODELO:
  Estimadores: {ml_tab_instance.trained_model.n_estimators}
  Criterio: {ml_tab_instance.trained_model.criterion}
  Features utilizadas: {len(ml_tab_instance.feature_columns)}
  Target: {ml_tab_instance.target_column}

DATOS:
  Total muestras: {len(ml_tab_instance.current_data)}
  Muestras entrenamiento: {len(ml_tab_instance.y_test) * (1 / ml_tab_instance.test_size_var.get() - 1):.0f}
  Muestras prueba: {len(ml_tab_instance.y_test)}
  Test size: {ml_tab_instance.test_size_var.get():.1%}

MÉTRICAS DE RENDIMIENTO:
  R² Score: {r2:.4f}
  MAE: {mae:.4f}
  RMSE: {rmse:.4f}
  MAPE: {np.mean(np.abs((ml_tab_instance.y_test - ml_tab_instance.test_predictions) / ml_tab_instance.y_test)) * 100:.2f}%

RESIDUOS NORMALIZADOS (1 - pred/real):
  Error normalizado medio: {np.mean(np.abs(normalized_residuals)):.4f}
  Desviación estándar: {np.std(normalized_residuals):.4f}
  Error máximo normalizado: {np.max(np.abs(normalized_residuals)):.4f}

TOP 10 FEATURES MÁS IMPORTANTES:
"""
    
    for i, (_, row) in enumerate(ml_tab_instance.feature_importance.head(10).iterrows()):
        report += f"  {i+1:2d}. {row['feature'][:50]:50s}: {row['importance']:.4f}\n"
    
    report += f"""

DISTRIBUCIÓN DE ERRORES:
  P25: {np.percentile(np.abs(ml_tab_instance.y_test - ml_tab_instance.test_predictions), 25):.2f}
  P50: {np.percentile(np.abs(ml_tab_instance.y_test - ml_tab_instance.test_predictions), 50):.2f}
  P75: {np.percentile(np.abs(ml_tab_instance.y_test - ml_tab_instance.test_predictions), 75):.2f}
  P90: {np.percentile(np.abs(ml_tab_instance.y_test - ml_tab_instance.test_predictions), 90):.2f}
  P95: {np.percentile(np.abs(ml_tab_instance.y_test - ml_tab_instance.test_predictions), 95):.2f}

INTERPRETACIÓN:
  Calidad del modelo: {'Excelente' if r2 > 0.9 else 'Bueno' if r2 > 0.7 else 'Moderado' if r2 > 0.5 else 'Pobre'}
  Precisión: {'Alta' if mae < 5 else 'Media' if mae < 10 else 'Baja'}
  
RECOMENDACIONES:
"""
    
    if r2 < 0.7:
        report += "  - Considerar más features o ingeniería de features\n"
        report += "  - Probar hiperparámetros diferentes\n"
    if mae > 10:
        report += "  - Revisar outliers en los datos\n"
        report += "  - Considerar transformaciones de datos\n"
    if np.std(normalized_residuals) > 0.3:
        report += "  - Alta variabilidad en errores normalizados\n"
        report += "  - Considerar estratificación por rangos de target\n"
    
    # Guardar reporte si se especifica ruta
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Reporte guardado en: {output_path}")
    
    return report