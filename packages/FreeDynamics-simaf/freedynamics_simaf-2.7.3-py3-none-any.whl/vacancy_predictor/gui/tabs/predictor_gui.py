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

class PredictorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔮 Predictor de Vacancies - Mejorado")
        self.root.geometry("1000x750")
        
        # Variables para almacenar datos
        self.csv_path = None
        self.model_path = None
        self.df = None
        self.model = None
        self.feature_columns = None
        self.scaler = None
        self.predictions_df = None
        
        # Referencias a widgets
        self.predict_btn = None
        self.save_btn = None
        self.csv_label = None
        self.model_label = None
        
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
        title_label = ttk.Label(main_frame, text="🔮 Predictor de Vacancies ML", 
                               font=("Arial", 18, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Frame de controles
        control_frame = ttk.LabelFrame(main_frame, text="📂 Controles de Archivo", padding="15")
        control_frame.pack(fill="x", pady=(0, 15))
        
        # Botones de carga
        btn_frame = ttk.Frame(control_frame)
        btn_frame.pack(fill="x", pady=5)
        
        ttk.Button(btn_frame, text="📄 Cargar CSV", 
                  command=self.load_csv, width=18).pack(side="left", padx=(0, 10))
        ttk.Button(btn_frame, text="🤖 Cargar Modelo", 
                  command=self.load_model, width=18).pack(side="left", padx=(0, 10))
        
        # Botón de predicción
        self.predict_btn = ttk.Button(btn_frame, text="🔮 Predecir", 
                                     command=self.predict, width=15, state="disabled")
        self.predict_btn.pack(side="left", padx=(0, 10))
        
        # Botón de guardar
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
        
        # Pestaña de información
        self.create_info_tab()
        
        # Pestaña de resultados
        self.create_results_tab()
        
        # Pestaña de visualización
        self.create_viz_tab()
        
        # Pestaña de estadísticas
        self.create_stats_tab()
    
    def create_info_tab(self):
        """Crear pestaña de información"""
        info_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(info_frame, text="📋 Información")
        
        self.info_text = scrolledtext.ScrolledText(info_frame, height=20, wrap='word',
                                                  font=("Consolas", 10))
        self.info_text.pack(fill="both", expand=True)
        
        # Mensaje inicial
        welcome_msg = """🔮 PREDICTOR DE VACANCIES ML
=================================

👋 ¡Bienvenido! Esta aplicación te permite:

🔹 Cargar archivos CSV con datos de materiales
🔹 Usar modelos entrenados (.joblib) para predecir vacancies
🔹 Visualizar resultados y estadísticas
🔹 Exportar predicciones a CSV

📋 PASOS PARA USAR:
1️⃣ Carga un archivo CSV con los datos
2️⃣ Carga un modelo .joblib entrenado
3️⃣ Haz clic en "Predecir" 
4️⃣ Revisa los resultados en las pestañas
5️⃣ Guarda los resultados si lo deseas

⚠️  REQUISITOS:
• El CSV debe contener las mismas features que el modelo
• El modelo debe estar en formato .joblib con metadatos
• Las columnas deben tener nombres exactos

🚀 ¡Comienza cargando tus archivos!
"""
        self.info_text.insert(1.0, welcome_msg)
    
    def create_results_tab(self):
        """Crear pestaña de resultados"""
        results_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(results_frame, text="📊 Resultados")
        
        self.results_text = scrolledtext.ScrolledText(results_frame, height=20, wrap='word',
                                                     font=("Consolas", 10))
        self.results_text.pack(fill="both", expand=True)
    
    def create_viz_tab(self):
        """Crear pestaña de visualización"""
        viz_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(viz_frame, text="📈 Gráficos")
        
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
        self.notebook.add(stats_frame, text="📈 Estadísticas")
        
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
📍 Ubicación: {file_path}
📊 Dimensiones: {len(self.df):,} filas × {len(self.df.columns)} columnas

🔧 COLUMNAS DISPONIBLES ({len(self.df.columns)}):
{self._format_columns_list(self.df.columns.tolist())}

📋 INFORMACIÓN GENERAL:
• Memoria utilizada: {self.df.memory_usage(deep=True).sum() / 1024**2:.1f} MB
• Valores nulos: {self.df.isnull().sum().sum():,}
• Tipos de datos: {dict(self.df.dtypes.value_counts())}

🔍 PRIMERAS 5 FILAS:
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
📍 Ubicación: {file_path}
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
        
        stats_text += f"""🔍 PRIMERAS 10 PREDICCIONES:
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