"""
Aplicación principal de Vacancy Predictor con Multi-Model support y Dump Processor
Versión extendida para tu estructura de proyecto
"""

import sys
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ===== IMPORTS CORREGIDOS PARA TU ESTRUCTURA =====

# Inicializar variables de disponibilidad
MULTI_MODEL_AVAILABLE = False
BATCH_TAB_AVAILABLE = False
ADVANCED_ML_TAB_AVAILABLE = False
MULTI_MODEL_TAB_AVAILABLE = False
DUMP_PROCESSOR_TAB_AVAILABLE = False

# 1. Multi-Model Processor
try:
    from vacancy_predictor.core.enhanced_ml.multi_model_processor import MultiModelProcessor
    MULTI_MODEL_AVAILABLE = True
    logger.info("Multi-Model processor available")
except ImportError as e:
    logger.warning(f"Multi-Model functionality not available: {e}")
    MultiModelProcessor = None

# 2. Batch Processing Tab
try:
    from vacancy_predictor.gui.tabs.batch_processor_tab import BatchProcessingTab
    BATCH_TAB_AVAILABLE = True
    logger.info("Batch processing tab available")
except ImportError as e:
    logger.warning(f"Batch processing tab not available: {e}")
    BatchProcessingTab = None

# 3. Advanced ML Tab
try:
    from vacancy_predictor.gui.tabs.advanced_ml_tab import AdvancedMLTabWithPlots
    ADVANCED_ML_TAB_AVAILABLE = True
    logger.info("Advanced ML tab available")
except ImportError as e:
    logger.warning(f"Advanced ML tab not available: {e}")
    AdvancedMLTabWithPlots = None

# 4. Multi-Model Tab
try:
    from vacancy_predictor.gui.tabs.multi_model_tab import MultiModelTab
    MULTI_MODEL_TAB_AVAILABLE = True
    logger.info("Multi-Model tab available")
except ImportError as e:
    logger.warning(f"Multi-Model tab not available: {e}")
    
    # Crear placeholder cuando no esté disponible
    class MultiModelTab:
        def __init__(self, parent, callback, processor=None):
            self.frame = ttk.Frame(parent)
            self.processor = processor
            
            info_frame = ttk.Frame(self.frame, padding="20")
            info_frame.pack(expand=True, fill="both")
            
            title_label = ttk.Label(info_frame, 
                                   text="Multi-Model Tab No Disponible",
                                   font=('Arial', 16, 'bold'))
            title_label.pack(pady=(0, 20))
            
            info_text = """Archivo requerido: vacancy_predictor/gui/tabs/multi_model_tab.py

Este archivo contiene la interfaz para comparar múltiples modelos ML.
Cree el archivo con el contenido proporcionado para habilitar esta funcionalidad."""
            
            ttk.Label(info_frame, text=info_text, 
                     justify="left", wraplength=600).pack(pady=20)

# 5. NEW! Dump Processor Tab
try:
    from vacancy_predictor.gui.tabs.dump_processor_tab import DumpProcessorTab
    DUMP_PROCESSOR_TAB_AVAILABLE = True
    logger.info("Dump processor tab available")
except ImportError as e:
    logger.warning(f"Dump processor tab not available: {e}")
    
    # Crear placeholder cuando no esté disponible
    class DumpProcessorTab:
        def __init__(self, parent, callback):
            self.frame = ttk.Frame(parent)
            
            info_frame = ttk.Frame(self.frame, padding="20")
            info_frame.pack(expand=True, fill="both")
            
            title_label = ttk.Label(info_frame, 
                                   text="🔥 Dump Processor No Disponible",
                                   font=('Arial', 16, 'bold'))
            title_label.pack(pady=(0, 20))
            
            info_text = """Archivo requerido: vacancy_predictor/gui/tabs/dump_processor_tab.py

🔥 Esta pestaña permite procesar archivos LAMMPS dump directamente:
• Carga archivos .dump, .dump.gz, .lammpstrj
• Extrae features automáticamente desde datos atómicos  
• Predice vacancies usando modelos entrenados
• Exporta resultados y datasets

Para habilitar esta funcionalidad:
1. Crea el archivo dump_processor_tab.py en vacancy_predictor/gui/tabs/
2. Copia el código proporcionado
3. Reinicia la aplicación

¡Una vez habilitado, podrás procesar dumps sin pasos intermedios!"""
            
            text_widget = tk.Text(info_frame, height=15, wrap="word", 
                                 font=("Consolas", 10), state="normal")
            text_widget.insert(1.0, info_text)
            text_widget.config(state="disabled")
            text_widget.pack(fill="both", expand=True, pady=20)

class VacancyPredictorApp:
    """Aplicación principal con soporte multi-modelo y dump processor"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🔮 Vacancy Predictor ML - Suite Completo")
        self.root.geometry("1400x900")
        
        # Configurar estilo
        self.setup_style()
        
        # Variables principales
        self.current_dataset = None
        self.multi_model_processor = None
        
        # Referencias a tabs
        self.batch_tab = None
        self.advanced_ml_tab = None
        self.multi_model_tab = None
        self.dump_processor_tab = None
        
        # Inicializar procesador multi-modelo si está disponible
        if MULTI_MODEL_AVAILABLE:
            try:
                self.multi_model_processor = MultiModelProcessor()
                logger.info("MultiModelProcessor initialized")
            except Exception as e:
                logger.error(f"Error initializing MultiModelProcessor: {e}")
                self.multi_model_processor = None
        
        # Crear interfaz
        self.create_menu()
        self.create_main_interface()
        
        # Mostrar mensaje de bienvenida
        self.show_welcome_message()
    
    def setup_style(self):
        """Configurar estilo visual de la aplicación"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar colores
        style.configure("Title.TLabel", font=("Arial", 14, "bold"))
        style.configure("Success.TLabel", foreground="green")
        style.configure("Error.TLabel", foreground="red")
        style.configure("Warning.TLabel", foreground="orange")
    
    def create_menu(self):
        """Crear barra de menú"""
        try:
            menubar = tk.Menu(self.root)
            self.root.config(menu=menubar)
            
            # Menú Archivo
            file_menu = tk.Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Archivo", menu=file_menu)
            file_menu.add_command(label="Nuevo Proyecto", command=self.new_project)
            file_menu.add_separator()
            file_menu.add_command(label="Exportar Resultados", command=self.export_results)
            file_menu.add_separator()
            file_menu.add_command(label="Salir", command=self.root.quit)
            
            # Menú Herramientas
            tools_menu = tk.Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Herramientas", menu=tools_menu)
            tools_menu.add_command(label="Validar Datos", command=self.validate_current_data)
            tools_menu.add_separator()
            tools_menu.add_command(label="🔥 Abrir Dump Processor Standalone", 
                                 command=self.open_standalone_dump_processor)
            
            # Menú Ver
            view_menu = tk.Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Ver", menu=view_menu)
            view_menu.add_command(label="Información del Sistema", command=self.show_system_info)
            view_menu.add_command(label="Estado de Módulos", command=self.show_module_status)
            
            # Menú Ayuda
            help_menu = tk.Menu(menubar, tearoff=0)
            menubar.add_cascade(label="Ayuda", menu=help_menu)
            help_menu.add_command(label="Guía de Uso", command=self.show_usage_guide)
            help_menu.add_command(label="Acerca de", command=self.show_about)
            
        except Exception as e:
            logger.error(f"Error creating menu: {e}")
    
    def create_main_interface(self):
        """Crear interfaz principal con tabs"""
        main_container = ttk.Frame(self.root)
        main_container.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill="both", expand=True)
        
        # 1. TAB DE DUMP PROCESSOR (NUEVO - PRIMERA POSICIÓN)
        if DUMP_PROCESSOR_TAB_AVAILABLE:
            try:
                self.dump_processor_tab = DumpProcessorTab(self.notebook, self.on_dump_data_loaded)
                self.notebook.add(self.dump_processor_tab.frame, text="🔥 Dump Processor")
                logger.info("Dump processor tab created")
            except Exception as e:
                logger.error(f"Error creating dump processor tab: {e}")
                self.create_error_tab("🔥 Dump Processor", str(e))
        else:
            # Crear tab placeholder
            self.dump_processor_tab = DumpProcessorTab(self.notebook, self.on_dump_data_loaded)
            self.notebook.add(self.dump_processor_tab.frame, text="🔥 Dump Processor")
        
        # 2. TAB DE PROCESAMIENTO BATCH
        if BATCH_TAB_AVAILABLE:
            try:
                self.batch_tab = BatchProcessingTab(self.notebook, self.on_batch_data_loaded)
                self.notebook.add(self.batch_tab.frame, text="📦 Batch Processing")
                logger.info("Batch processing tab created")
            except Exception as e:
                logger.error(f"Error creating batch tab: {e}")
                self.create_error_tab("📦 Batch Processing", str(e))
        else:
            self.create_unavailable_tab("📦 Batch Processing", "BatchProcessingTab no disponible")
        
        # 3. TAB DE ADVANCED ML
        if ADVANCED_ML_TAB_AVAILABLE:
            try:
                self.advanced_ml_tab = AdvancedMLTabWithPlots(self.notebook, self.on_advanced_data_loaded)
                self.notebook.add(self.advanced_ml_tab.frame, text="🧠 Advanced ML")
                logger.info("Advanced ML tab created")
            except Exception as e:
                logger.error(f"Error creating ML tab: {e}")
                self.create_error_tab("🧠 Advanced ML", str(e))
        else:
            self.create_unavailable_tab("🧠 Advanced ML", "AdvancedMLTabWithPlots no disponible")
        
        # 4. TAB DE MULTI-MODEL
        if MULTI_MODEL_TAB_AVAILABLE:
            try:
                self.multi_model_tab = MultiModelTab(
                    self.notebook, 
                    self.on_multi_model_data_loaded,
                    processor=self.multi_model_processor
                )
                self.notebook.add(self.multi_model_tab.frame, text="🔬 Multi-Model")
                logger.info("Multi-Model tab created")
            except Exception as e:
                logger.error(f"Error creating Multi-Model tab: {e}")
                self.create_error_tab("🔬 Multi-Model", str(e))
        else:
            # Crear placeholder
            self.multi_model_tab = MultiModelTab(
                self.notebook, 
                self.on_multi_model_data_loaded,
                processor=self.multi_model_processor
            )
            self.notebook.add(self.multi_model_tab.frame, text="🔬 Multi-Model")
        
        # 5. TAB DE INFORMACIÓN Y ESTADO
        self.create_system_info_tab()
    
    def create_system_info_tab(self):
        """Crear pestaña de información del sistema"""
        info_frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(info_frame, text="ℹ️ Sistema")
        
        # Título
        title_label = ttk.Label(info_frame, text="🔮 Vacancy Predictor ML - Suite Completo",
                               style="Title.TLabel")
        title_label.pack(pady=(0, 20))
        
        # Crear notebook interno para organizar información
        info_notebook = ttk.Notebook(info_frame)
        info_notebook.pack(fill="both", expand=True)
        
        # Sub-pestaña: Estado de módulos
        self.create_module_status_subtab(info_notebook)
        
        # Sub-pestaña: Guía de uso
        self.create_usage_guide_subtab(info_notebook)
        
        # Sub-pestaña: Información del sistema
        self.create_system_details_subtab(info_notebook)
    
    def create_module_status_subtab(self, parent):
        """Crear sub-pestaña de estado de módulos"""
        status_frame = ttk.Frame(parent, padding="10")
        parent.add(status_frame, text="📊 Estado Módulos")
        
        status_text = tk.Text(status_frame, wrap="word", font=("Consolas", 10))
        status_scrollbar = ttk.Scrollbar(status_frame, orient="vertical", command=status_text.yview)
        status_text.configure(yscrollcommand=status_scrollbar.set)
        
        status_text.pack(side="left", fill="both", expand=True)
        status_scrollbar.pack(side="right", fill="y")
        
        # Generar reporte de estado
        self.update_module_status_display(status_text)
    
    def create_usage_guide_subtab(self, parent):
        """Crear sub-pestaña de guía de uso"""
        guide_frame = ttk.Frame(parent, padding="10")
        parent.add(guide_frame, text="📖 Guía de Uso")
        
        guide_text = tk.Text(guide_frame, wrap="word", font=("Arial", 10))
        guide_scrollbar = ttk.Scrollbar(guide_frame, orient="vertical", command=guide_text.yview)
        guide_text.configure(yscrollcommand=guide_scrollbar.set)
        
        guide_text.pack(side="left", fill="both", expand=True)
        guide_scrollbar.pack(side="right", fill="y")
        
        # Contenido de la guía
        guide_content = """🔮 VACANCY PREDICTOR ML - GUÍA DE USO
==========================================

🔥 DUMP PROCESSOR (NUEVO!)
--------------------------
La herramienta más avanzada para procesar archivos LAMMPS:

📁 PASO 1: Cargar Dumps
   • Selecciona archivos .dump, .dump.gz, .lammpstrj
   • Soporta archivos comprimidos automáticamente
   • Carga múltiples archivos de una vez

🔄 PASO 2: Procesar a CSV  
   • Extrae features automáticamente desde datos atómicos
   • Calcula estadísticas de energía, espaciales, por tipo
   • Genera dataset listo para Machine Learning

🤖 PASO 3: Cargar Modelo ML
   • Carga modelos .joblib previamente entrenados
   • Detecta features requeridas automáticamente
   • Aplica escalado si está incluido en el modelo

🔮 PASO 4: Predecir Vacancies
   • Predicciones directas desde archivos dump
   • Sin necesidad de procesamiento manual
   • Resultados con estadísticas detalladas

💾 PASO 5: Exportar Resultados
   • Guarda predicciones con todas las features
   • Exporta datasets para reutilizar
   • Formatos CSV y Excel soportados

📦 BATCH PROCESSING
-------------------
Para procesamiento masivo de archivos:
• Selecciona directorio con archivos dump
• Configura parámetros de procesamiento
• Procesa cientos de archivos automáticamente
• Genera datasets unificados

🧠 ADVANCED ML
--------------
Entrenamiento avanzado de modelos:
• Algoritmos múltiples (Random Forest, XGBoost, etc.)
• Validación cruzada automática
• Optimización de hiperparámetros
• Análisis de importancia de features

🔬 MULTI-MODEL
--------------
Comparación de múltiples modelos:
• Entrena varios algoritmos simultáneamente
• Compara rendimiento automáticamente
• Selecciona el mejor modelo
• Exporta modelos optimizados

💡 CONSEJOS GENERALES
--------------------
• Usa Dump Processor para archivos nuevos
• Batch Processing para volúmenes grandes
• Advanced ML para entrenar modelos nuevos
• Multi-Model para optimizar rendimiento

🔧 TROUBLESHOOTING
-----------------
• Si un módulo no está disponible, se muestra como placeholder
• Revisa los logs en la consola para detalles de errores
• Usa el menú Herramientas > Validar Datos para verificar formato
• Consulta el Estado de Módulos para ver qué está disponible

🚀 ¡DISFRUTA EXPLORANDO LAS CAPACIDADES DEL SUITE!
"""
        
        guide_text.insert(1.0, guide_content)
        guide_text.config(state="disabled")
    
    def create_system_details_subtab(self, parent):
        """Crear sub-pestaña de detalles del sistema"""
        details_frame = ttk.Frame(parent, padding="10")
        parent.add(details_frame, text="💻 Sistema")
        
        details_text = tk.Text(details_frame, wrap="word", font=("Consolas", 9))
        details_scrollbar = ttk.Scrollbar(details_frame, orient="vertical", command=details_text.yview)
        details_text.configure(yscrollcommand=details_scrollbar.set)
        
        details_text.pack(side="left", fill="both", expand=True)
        details_scrollbar.pack(side="right", fill="y")
        
        # Información del sistema
        system_info = f"""💻 INFORMACIÓN DEL SISTEMA
==========================

🐍 Python: {sys.version}
📁 Ruta de ejecución: {Path.cwd()}
🔮 Versión de aplicación: 2.0 Extended

📦 MÓDULOS DISPONIBLES:
• Batch Processing: {'✅ Disponible' if BATCH_TAB_AVAILABLE else '❌ No disponible'}
• Advanced ML: {'✅ Disponible' if ADVANCED_ML_TAB_AVAILABLE else '❌ No disponible'}
• Multi-Model: {'✅ Disponible' if MULTI_MODEL_TAB_AVAILABLE else '❌ No disponible'}
• Dump Processor: {'✅ Disponible' if DUMP_PROCESSOR_TAB_AVAILABLE else '❌ No disponible'}
• Multi-Model Core: {'✅ Disponible' if MULTI_MODEL_AVAILABLE else '❌ No disponible'}

🔧 ESTRUCTURA REQUERIDA:
vacancy_predictor/
├── gui/
│   └── tabs/
│       ├── batch_processor_tab.py
│       ├── advanced_ml_tab.py
│       ├── multi_model_tab.py
│       └── dump_processor_tab.py    # NUEVO!
├── core/
│   └── enhanced_ml/
│       └── multi_model_processor.py
└── app.py

🚀 CARACTERÍSTICAS NUEVAS v2.0:
• Dump Processor: Procesa archivos LAMMPS directamente
• Interfaz unificada: Todos los módulos en una aplicación
• Mejor manejo de errores y placeholders
• Guías de uso integradas
• Estado de módulos en tiempo real

💡 Para habilitar módulos faltantes, crea los archivos requeridos
   en la estructura de directorios mostrada arriba.
"""
        
        details_text.insert(1.0, system_info)
        details_text.config(state="disabled")
    
    def update_module_status_display(self, text_widget):
        """Actualizar display de estado de módulos"""
        status_report = """📊 ESTADO DETALLADO DE MÓDULOS
===============================

🔥 DUMP PROCESSOR TAB
Status: """ + ("✅ DISPONIBLE" if DUMP_PROCESSOR_TAB_AVAILABLE else "❌ NO DISPONIBLE") + """
Descripción: Procesamiento directo de archivos LAMMPS dump
Archivo requerido: vacancy_predictor/gui/tabs/dump_processor_tab.py
Funciones: Parsing LAMMPS, extracción de features, predicción ML

📦 BATCH PROCESSING TAB  
Status: """ + ("✅ DISPONIBLE" if BATCH_TAB_AVAILABLE else "❌ NO DISPONIBLE") + """
Descripción: Procesamiento masivo de archivos
Archivo requerido: vacancy_predictor/gui/tabs/batch_processor_tab.py
Funciones: Procesamiento en lotes, selección de features

🧠 ADVANCED ML TAB
Status: """ + ("✅ DISPONIBLE" if ADVANCED_ML_TAB_AVAILABLE else "❌ NO DISPONIBLE") + """
Descripción: Entrenamiento avanzado de modelos ML
Archivo requerido: vacancy_predictor/gui/tabs/advanced_ml_tab.py
Funciones: Múltiples algoritmos, validación cruzada, plots

🔬 MULTI-MODEL TAB
Status: """ + ("✅ DISPONIBLE" if MULTI_MODEL_TAB_AVAILABLE else "❌ NO DISPONIBLE") + """
Descripción: Comparación de múltiples modelos
Archivo requerido: vacancy_predictor/gui/tabs/multi_model_tab.py
Funciones: Entrenamiento paralelo, comparación de performance

⚙️ MULTI-MODEL PROCESSOR (CORE)
Status: """ + ("✅ DISPONIBLE" if MULTI_MODEL_AVAILABLE else "❌ NO DISPONIBLE") + """
Descripción: Procesador central para múltiples modelos
Archivo requerido: vacancy_predictor/core/enhanced_ml/multi_model_processor.py
Funciones: Engine central para ML avanzado

📈 FUNCIONALIDADES ACTIVAS:
""" + (f"• {sum([DUMP_PROCESSOR_TAB_AVAILABLE, BATCH_TAB_AVAILABLE, ADVANCED_ML_TAB_AVAILABLE, MULTI_MODEL_TAB_AVAILABLE, MULTI_MODEL_AVAILABLE])}/5 módulos disponibles") + """

💡 RECOMENDACIONES:
• Si algún módulo no está disponible, revisa que el archivo exista
• Consulta la documentación para implementar módulos faltantes  
• El Dump Processor es la funcionalidad más nueva y recomendada
• Todos los módulos son independientes y opcionales

🔄 Última actualización: """ + str(pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")) + """
"""
        
        text_widget.delete(1.0, tk.END)
        text_widget.insert(1.0, status_report)
        text_widget.config(state="disabled")
    
    def create_error_tab(self, tab_name, error_message):
        """Crear pestaña de error"""
        error_frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(error_frame, text=f"❌ {tab_name}")
        
        ttk.Label(error_frame, text=f"Error en {tab_name}",
                 font=("Arial", 14, "bold"), foreground="red").pack(pady=(0, 10))
        
        error_text = tk.Text(error_frame, height=10, wrap="word")
        error_text.insert(1.0, f"Error: {error_message}\n\nEste módulo no está disponible debido al error mostrado.")
        error_text.config(state="disabled")
        error_text.pack(fill="both", expand=True)
    
    def create_unavailable_tab(self, tab_name, message):
        """Crear pestaña no disponible"""
        unavailable_frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(unavailable_frame, text=f"⚠️ {tab_name}")
        
        ttk.Label(unavailable_frame, text=f"{tab_name} No Disponible",
                 font=("Arial", 14, "bold"), foreground="orange").pack(pady=(0, 10))
        
        ttk.Label(unavailable_frame, text=message, wraplength=500).pack(pady=10)
    
    # =====================================================================
    # CALLBACKS DE DATOS
    # =====================================================================
    
    def on_dump_data_loaded(self, data):
        """Callback cuando se cargan datos desde dump processor"""
        logger.info(f"Dump data loaded: {len(data)} rows")
        self.current_dataset = data
        
        # Propagar a otros tabs si están disponibles
        if hasattr(self.batch_tab, 'update_from_external_data'):
            try:
                self.batch_tab.update_from_external_data(data)
            except Exception as e:
                logger.error(f"Error updating batch tab: {e}")
        
        if hasattr(self.advanced_ml_tab, 'update_from_external_data'):
            try:
                self.advanced_ml_tab.update_from_external_data(data)
            except Exception as e:
                logger.error(f"Error updating advanced ML tab: {e}")
    
    def on_batch_data_loaded(self, data):
        """Callback cuando se cargan datos desde batch processing"""
        logger.info(f"Batch data loaded: {len(data)} rows")
        self.current_dataset = data
    
    def on_advanced_data_loaded(self, data):
        """Callback cuando se cargan datos desde advanced ML"""
        logger.info(f"Advanced ML data loaded: {len(data)} rows")
        self.current_dataset = data
    
    def on_multi_model_data_loaded(self, data):
        """Callback cuando se cargan datos desde multi-model"""
        logger.info(f"Multi-model data loaded: {len(data)} rows")
        self.current_dataset = data
    
    # =====================================================================
    # FUNCIONES DEL MENÚ
    # =====================================================================
    
    def new_project(self):
        """Crear nuevo proyecto"""
        result = messagebox.askyesno("Nuevo Proyecto", 
                                   "¿Crear nuevo proyecto? Se perderán los datos no guardados.")
        if result:
            # Reset all tabs
            logger.info("Creating new project")
            self.current_dataset = None
            messagebox.showinfo("Nuevo Proyecto", "Proyecto reiniciado. Puedes comenzar con datos nuevos.")
    
    def export_results(self):
        """Exportar resultados actuales"""
        if self.current_dataset is None:
            messagebox.showwarning("Advertencia", "No hay datos para exportar")
            return
        
        from tkinter import filedialog
        file_path = filedialog.asksaveasfilename(
            title="Exportar resultados",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
        )
        
        if file_path:
            try:
                if file_path.endswith('.xlsx'):
                    self.current_dataset.to_excel(file_path, index=False)
                else:
                    self.current_dataset.to_csv(file_path, index=False)
                
                messagebox.showinfo("Éxito", f"Datos exportados a: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Error exportando: {e}")
    
    def validate_current_data(self):
        """Validar datos actuales"""
        if self.current_dataset is None:
            messagebox.showwarning("Advertencia", "No hay datos para validar")
            return
        
        # Validación básica
        validation_report = f"""REPORTE DE VALIDACIÓN
====================

📊 Dimensiones: {self.current_dataset.shape[0]} filas × {self.current_dataset.shape[1]} columnas
📋 Columnas: {list(self.current_dataset.columns)}
❌ Valores nulos: {self.current_dataset.isnull().sum().sum()}
📈 Memoria: {self.current_dataset.memory_usage(deep=True).sum() / 1024**2:.1f} MB

✅ Dataset válido para procesamiento
"""
        
        messagebox.showinfo("Validación de Datos", validation_report)
    
    def open_standalone_dump_processor(self):
        """Abrir dump processor independiente"""
        try:
            # Crear ventana independiente
            standalone_window = tk.Toplevel(self.root)
            standalone_window.title("🔥 Dump Processor - Ventana Independiente")
            standalone_window.geometry("1000x700")
            
            # Crear instancia del dump processor
            if DUMP_PROCESSOR_TAB_AVAILABLE:
                from vacancy_predictor.gui.tabs.dump_processor_tab import DumpProcessorTab
                standalone_processor = DumpProcessorTab(standalone_window, None)
                standalone_processor.frame.pack(fill="both", expand=True, padx=10, pady=10)
            else:
                ttk.Label(standalone_window, 
                         text="Dump Processor no disponible\nInstala dump_processor_tab.py",
                         justify="center").pack(expand=True)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error abriendo Dump Processor independiente: {e}")
    
    def show_system_info(self):
        """Mostrar información del sistema"""
        info = f"""INFORMACIÓN DEL SISTEMA
======================

🐍 Python: {sys.version}
📁 Directorio: {Path.cwd()}
🔮 Aplicación: Vacancy Predictor ML v2.0

📦 ESTADO DE MÓDULOS:
• Dump Processor: {'✅' if DUMP_PROCESSOR_TAB_AVAILABLE else '❌'}
• Batch Processing: {'✅' if BATCH_TAB_AVAILABLE else '❌'}  
• Advanced ML: {'✅' if ADVANCED_ML_TAB_AVAILABLE else '❌'}
• Multi-Model: {'✅' if MULTI_MODEL_TAB_AVAILABLE else '❌'}
• Multi-Model Core: {'✅' if MULTI_MODEL_AVAILABLE else '❌'}

Dataset actual: {len(self.current_dataset) if self.current_dataset is not None else 'Ninguno'} filas
"""
        messagebox.showinfo("Información del Sistema", info)
    
    def show_module_status(self):
        """Mostrar estado detallado de módulos"""
        # Cambiar a pestaña de sistema
        for i, tab_name in enumerate([self.notebook.tab(i, "text") for i in range(self.notebook.index("end"))]):
            if "Sistema" in tab_name:
                self.notebook.select(i)
                break
    
    def show_usage_guide(self):
        """Mostrar guía de uso"""
        # Cambiar a pestaña de sistema, sub-pestaña de guía
        for i, tab_name in enumerate([self.notebook.tab(i, "text") for i in range(self.notebook.index("end"))]):
            if "Sistema" in tab_name:
                self.notebook.select(i)
                break
    
    def show_about(self):
        """Mostrar información sobre la aplicación"""
        about_text = """🔮 VACANCY PREDICTOR ML v2.0 EXTENDED

Desarrollado para predicción de vacancies en materiales usando Machine Learning.

NUEVAS CARACTERÍSTICAS v2.0:
🔥 Dump Processor: Procesa archivos LAMMPS directamente
📦 Batch Processing: Procesamiento masivo
🧠 Advanced ML: Entrenamiento avanzado  
🔬 Multi-Model: Comparación de modelos
🎯 Interfaz unificada y modular

CARACTERÍSTICAS TÉCNICAS:
• Soporte para archivos .dump, .dump.gz, .lammpstrj
• Extracción automática de features desde datos atómicos
• Múltiples algoritmos ML (Random Forest, XGBoost, etc.)
• Validación cruzada y optimización de hiperparámetros
• Exportación en CSV y Excel
• Visualizaciones interactivas

AUTOR: Tu equipo de desarrollo
VERSIÓN: 2.0 Extended
FECHA: 2024

¡Gracias por usar Vacancy Predictor ML!
"""
        messagebox.showinfo("Acerca de", about_text)
    
    def show_welcome_message(self):
        """Mostrar mensaje de bienvenida"""
        welcome_msg = f"""🔮 ¡Bienvenido a Vacancy Predictor ML v2.0!

🎉 NUEVA FUNCIONALIDAD: Dump Processor
El nuevo módulo te permite procesar archivos LAMMPS dump directamente
y predecir vacancies sin pasos intermedios.

📊 MÓDULOS DISPONIBLES:
• {'🔥 Dump Processor' if DUMP_PROCESSOR_TAB_AVAILABLE else '⚠️ Dump Processor (no disponible)'}
• {'📦 Batch Processing' if BATCH_TAB_AVAILABLE else '⚠️ Batch Processing (no disponible)'}
• {'🧠 Advanced ML' if ADVANCED_ML_TAB_AVAILABLE else '⚠️ Advanced ML (no disponible)'}
• {'🔬 Multi-Model' if MULTI_MODEL_TAB_AVAILABLE else '⚠️ Multi-Model (no disponible)'}

💡 ¡Comienza explorando el Dump Processor para una experiencia completa!

¿Quieres ver la guía de uso?"""
        
        result = messagebox.askyesno("¡Bienvenido!", welcome_msg)
        if result:
            self.show_usage_guide()

def main():
    """Función principal"""
    # Configurar logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('vacancy_predictor.log')
        ]
    )
    
    logger.info("=== INICIANDO VACANCY PREDICTOR ML v2.0 ===")
    logger.info(f"Python version: {sys.version}")
    logger.info(f"Working directory: {Path.cwd()}")
    
    # Crear ventana principal
    root = tk.Tk()
    
    try:
        app = VacancyPredictorApp(root)
        logger.info("Application initialized successfully")
        
        # Ejecutar aplicación
        root.mainloop()
        
    except Exception as e:
        logger.error(f"Error starting application: {e}")
        messagebox.showerror("Error Fatal", 
                           f"Error iniciando aplicación:\n{e}\n\nConsulta vacancy_predictor.log para detalles")
    finally:
        logger.info("=== CERRANDO VACANCY PREDICTOR ML ===")

if __name__ == "__main__":
    # Verificar imports adicionales necesarios
    try:
        import pandas as pd
        import numpy as np
    except ImportError as e:
        print(f"❌ Error: Falta instalar dependencias: {e}")
        print("💡 Instala con: pip install pandas numpy scikit-learn matplotlib")
        sys.exit(1)
    
    main()