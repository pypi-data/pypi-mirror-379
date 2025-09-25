#!/usr/bin/env python3
"""
Ejemplo de uso del Predictor de Vacancies
Muestra cómo usar tanto la versión simple como la GUI
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Importar las versiones del predictor
# from vacancy_predictor_simple import predict_from_files
# from predictor_gui_mejorado import PredictorGUI

def ejemplo_uso_simple():
    """Ejemplo usando la versión simple (sin GUI)"""
    print("🔮 EJEMPLO - PREDICTOR SIMPLE")
    print("=" * 40)
    
    # Rutas de archivos
    csv_file = "dataset_ovito_convexhull.csv"
    model_file = "modelo_vacancies.joblib"  # Reemplaza con tu archivo .joblib
    output_file = "predicciones_resultado.csv"
    
    # Verificar que los archivos existen
    if not Path(csv_file).exists():
        print(f"❌ No se encuentra el archivo CSV: {csv_file}")
        return
    
    if not Path(model_file).exists():
        print(f"❌ No se encuentra el modelo: {model_file}")
        print("💡 Asegúrate de tener un archivo .joblib con el modelo entrenado")
        return
    
    try:
        # Usar la función simple
        from vacancy_predictor.gui.tabs.vacancy_predictor_simple import predict_from_files
        
        print(f"📂 Cargando CSV: {csv_file}")
        print(f"🤖 Cargando modelo: {model_file}")
        
        # Realizar predicción
        result_df = predict_from_files(csv_file, model_file, output_file)
        
        if result_df is not None:
            print("\n✅ Predicción completada exitosamente!")
            print(f"📊 Resultados guardados en: {output_file}")
            
            # Mostrar resumen
            print(f"\n📈 RESUMEN:")
            print(f"   Filas procesadas: {len(result_df):,}")
            print(f"   Predicciones: {result_df['vacancies_predicted'].min()} - {result_df['vacancies_predicted'].max()}")
            
            if 'vacancies' in result_df.columns:
                mae = np.mean(np.abs(result_df['vacancies_predicted'] - result_df['vacancies']))
                print(f"   Error promedio: {mae:.2f}")
        
    except ImportError:
        print("❌ No se pudo importar vacancy_predictor_simple")
        print("💡 Asegúrate de que el archivo esté en el mismo directorio")
    except Exception as e:
        print(f"❌ Error: {e}")

def ejemplo_uso_gui():
    """Ejemplo usando la GUI"""
    print("\n🖥️  EJEMPLO - PREDICTOR GUI")
    print("=" * 40)
    
    try:
        import tkinter as tk
        from vacancy_predictor.gui.tabs.predictor_gui import PredictorGUI
        
        print("🚀 Iniciando interfaz gráfica...")
        print("💡 Usa la interfaz para:")
        print("   1. Cargar tu archivo CSV")
        print("   2. Cargar tu modelo .joblib") 
        print("   3. Hacer predicciones")
        print("   4. Ver gráficos y estadísticas")
        
        root = tk.Tk()
        app = PredictorGUI(root)
        root.mainloop()
        
    except ImportError as e:
        print(f"❌ Error importando GUI: {e}")
        print("💡 Asegúrate de que tkinter esté instalado")
    except Exception as e:
        print(f"❌ Error iniciando GUI: {e}")

def crear_modelo_ejemplo():
    """Crear un modelo de ejemplo para testing"""
    print("\n🔬 CREANDO MODELO DE EJEMPLO")
    print("=" * 40)
    
    try:
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
        import joblib
        
        # Verificar que tenemos el CSV
        if not Path("dataset_ovito_convexhull.csv").exists():
            print("❌ No se encuentra dataset_ovito_convexhull.csv")
            return
        
        print("📂 Cargando datos para entrenamiento...")
        df = pd.read_csv("dataset_ovito_convexhull.csv")
        
        # Preparar features y target
        exclude_cols = ['file', 'vacancies', 'file_processed', 'n_atoms_surface']
        feature_cols = [col for col in df.columns 
                       if col not in exclude_cols and df[col].dtype in ['int64', 'float64']]
        
        X = df[feature_cols]
        y = df['vacancies']
        
        print(f"🔧 Features seleccionadas: {len(feature_cols)}")
        print(f"📊 Datos de entrenamiento: {len(X)} muestras")
        
        # Dividir datos
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Escalar datos
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Entrenar modelo
        print("🤖 Entrenando Random Forest...")
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train_scaled, y_train)
        
        # Evaluar
        train_score = model.score(X_train_scaled, y_train)
        test_score = model.score(X_test_scaled, y_test)
        
        print(f"📈 Score entrenamiento: {train_score:.3f}")
        print(f"📈 Score test: {test_score:.3f}")
        
        # Guardar modelo con metadatos
        model_data = {
            'model': model,
            'feature_columns': feature_cols,
            'scaler': scaler,
            'training_params': {
                'n_estimators': 100,
                'test_size': 0.2,
                'random_state': 42
            }
        }
        
        model_file = "modelo_vacancies_ejemplo.joblib"
        joblib.dump(model_data, model_file)
        
        print(f"💾 Modelo guardado en: {model_file}")
        print("✅ ¡Modelo de ejemplo creado exitosamente!")
        
        return model_file
        
    except ImportError as e:
        print(f"❌ Falta instalar: {e}")
        print("💡 Instala con: pip install scikit-learn")
    except Exception as e:
        print(f"❌ Error creando modelo: {e}")
        return None

def main():
    """Función principal con menú interactivo"""
    print("🔮 PREDICTOR DE VACANCIES ML")
    print("=" * 50)
    print("Herramientas para predecir vacancies usando Machine Learning")
    print()
    
    while True:
        print("\n📋 MENÚ DE OPCIONES:")
        print("1. 🚀 Ejecutar predictor simple (línea de comandos)")
        print("2. 🖥️  Ejecutar predictor con GUI")
        print("3. 🔬 Crear modelo de ejemplo") 
        print("4. 📖 Ver información de archivos")
        print("5. 🚪 Salir")
        
        try:
            opcion = input("\n👉 Selecciona una opción (1-5): ").strip()
            
            if opcion == "1":
                ejemplo_uso_simple()
            elif opcion == "2":
                ejemplo_uso_gui()
            elif opcion == "3":
                crear_modelo_ejemplo()
            elif opcion == "4":
                mostrar_info_archivos()
            elif opcion == "5":
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def mostrar_info_archivos():
    """Mostrar información sobre los archivos necesarios"""
    print("\n📖 INFORMACIÓN DE ARCHIVOS")
    print("=" * 40)
    
    # Verificar CSV
    csv_file = "dataset_ovito_convexhull.csv"
    if Path(csv_file).exists():
        df = pd.read_csv(csv_file)
        print(f"✅ CSV encontrado: {csv_file}")
        print(f"   📊 Dimensiones: {len(df)} filas × {len(df.columns)} columnas")
        print(f"   🎯 Target 'vacancies': {'Sí' if 'vacancies' in df.columns else 'No'}")
    else:
        print(f"❌ CSV no encontrado: {csv_file}")
    
    # Verificar modelos .joblib
    joblib_files = list(Path(".").glob("*.joblib"))
    if joblib_files:
        print(f"\n🤖 Modelos .joblib encontrados:")
        for model_file in joblib_files:
            print(f"   • {model_file.name}")
    else:
        print(f"\n❌ No se encontraron archivos .joblib")
        print("💡 Usa la opción 3 para crear un modelo de ejemplo")
    
    print(f"\n📁 ESTRUCTURA RECOMENDADA:")
    print("   proyecto/")
    print("   ├── dataset_ovito_convexhull.csv")
    print("   ├── modelo_vacancies.joblib") 
    print("   ├── vacancy_predictor_simple.py")
    print("   ├── predictor_gui_mejorado.py")
    print("   └── ejemplo_uso.py (este archivo)")

if __name__ == "__main__":
    main()