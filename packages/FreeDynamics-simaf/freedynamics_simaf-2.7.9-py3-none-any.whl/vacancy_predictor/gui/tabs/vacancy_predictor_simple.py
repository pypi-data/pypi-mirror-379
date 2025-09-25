import pandas as pd
import joblib
import numpy as np
from pathlib import Path
import argparse
import sys

class VacancyPredictor:
    def __init__(self):
        self.model = None
        self.feature_columns = None
        self.scaler = None
        self.model_info = None
    
    def load_model(self, model_path):
        """Cargar modelo .joblib"""
        try:
            print(f"Cargando modelo desde: {model_path}")
            
            # Cargar el archivo joblib
            model_data = joblib.load(model_path)
            
            # El modelo puede estar guardado de diferentes formas
            if isinstance(model_data, dict):
                # Formato con metadatos (recomendado)
                self.model = model_data["model"]
                self.feature_columns = model_data["feature_columns"]
                self.scaler = model_data.get("scaler", None)
                self.model_info = model_data.get("training_params", {})
                
                print(f"✓ Modelo cargado: {type(self.model).__name__}")
                print(f"✓ Features requeridas: {len(self.feature_columns)}")
                print(f"✓ Scaler incluido: {'Sí' if self.scaler else 'No'}")
                
            else:
                # Formato simple (solo el modelo)
                self.model = model_data
                print("⚠️  Modelo cargado sin metadatos. Se necesitarán las features manualmente.")
                return False
                
            return True
            
        except Exception as e:
            print(f"❌ Error cargando modelo: {e}")
            return False
    
    def load_data(self, csv_path):
        """Cargar datos CSV"""
        try:
            print(f"Cargando datos desde: {csv_path}")
            
            df = pd.read_csv(csv_path)
            print(f"✓ Datos cargados: {len(df)} filas, {len(df.columns)} columnas")
            
            # Verificar que las features necesarias están presentes
            if self.feature_columns:
                missing_features = [col for col in self.feature_columns if col not in df.columns]
                if missing_features:
                    print(f"❌ Features faltantes en el CSV: {missing_features}")
                    return None
                
                print(f"✓ Todas las features requeridas están presentes")
            
            return df
            
        except Exception as e:
            print(f"❌ Error cargando CSV: {e}")
            return None
    
    def predict_vacancies(self, df):
        """Predecir vacancies para todas las filas del DataFrame"""
        try:
            print("\n🔮 Iniciando predicciones...")
            
            # Preparar features
            X = df[self.feature_columns].copy()
            
            # Aplicar escalado si existe
            if self.scaler is not None:
                print("📊 Aplicando escalado a los datos...")
                X_scaled = self.scaler.transform(X)
                X = pd.DataFrame(X_scaled, columns=self.feature_columns, index=X.index)
            
            # Realizar predicciones
            predictions = self.model.predict(X)
            
            # Redondear a enteros (las vacancies son números enteros)
            predictions = np.round(predictions).astype(int)
            
            # Agregar predicciones al DataFrame
            result_df = df.copy()
            result_df['vacancies_predicted'] = predictions
            
            print(f"✓ Predicciones completadas para {len(predictions)} filas")
            
            # Mostrar estadísticas
            print(f"\n📈 ESTADÍSTICAS DE PREDICCIÓN:")
            print(f"   Rango de predicciones: {predictions.min()} - {predictions.max()}")
            print(f"   Media de predicciones: {predictions.mean():.2f}")
            print(f"   Desviación estándar: {predictions.std():.2f}")
            
            # Si existe columna de vacancies reales, calcular métricas
            if 'vacancies' in df.columns:
                real_vacancies = df['vacancies'].values
                mae = np.mean(np.abs(predictions - real_vacancies))
                rmse = np.sqrt(np.mean((predictions - real_vacancies)**2))
                
                print(f"\n🎯 MÉTRICAS DE EVALUACIÓN:")
                print(f"   MAE (Error Absoluto Medio): {mae:.2f}")
                print(f"   RMSE (Raíz Error Cuadrático Medio): {rmse:.2f}")
                
                # Precisión exacta
                exact_matches = np.sum(predictions == real_vacancies)
                accuracy = exact_matches / len(predictions)
                print(f"   Precisión exacta: {accuracy:.1%} ({exact_matches}/{len(predictions)})")
            
            return result_df
            
        except Exception as e:
            print(f"❌ Error en predicción: {e}")
            return None
    
    def save_results(self, df, output_path):
        """Guardar resultados en CSV"""
        try:
            df.to_csv(output_path, index=False)
            print(f"💾 Resultados guardados en: {output_path}")
            return True
        except Exception as e:
            print(f"❌ Error guardando resultados: {e}")
            return False

def main():
    parser = argparse.ArgumentParser(description='Predictor de Vacancies usando modelo ML')
    parser.add_argument('--csv', required=True, help='Ruta al archivo CSV con datos')
    parser.add_argument('--model', required=True, help='Ruta al modelo .joblib')
    parser.add_argument('--output', help='Ruta para guardar resultados (opcional)')
    
    args = parser.parse_args()
    
    # Verificar que los archivos existen
    if not Path(args.csv).exists():
        print(f"❌ Archivo CSV no encontrado: {args.csv}")
        sys.exit(1)
    
    if not Path(args.model).exists():
        print(f"❌ Archivo de modelo no encontrado: {args.model}")
        sys.exit(1)
    
    # Crear predictor
    predictor = VacancyPredictor()
    
    # Cargar modelo
    if not predictor.load_model(args.model):
        sys.exit(1)
    
    # Cargar datos
    df = predictor.load_data(args.csv)
    if df is None:
        sys.exit(1)
    
    # Realizar predicciones
    result_df = predictor.predict_vacancies(df)
    if result_df is None:
        sys.exit(1)
    
    # Guardar resultados
    if args.output:
        output_path = args.output
    else:
        # Generar nombre automático
        csv_path = Path(args.csv)
        output_path = csv_path.parent / f"{csv_path.stem}_predictions.csv"
    
    if predictor.save_results(result_df, output_path):
        print(f"\n🎉 ¡Proceso completado exitosamente!")
        print(f"📄 Consulta los resultados en: {output_path}")

# Función para usar desde script o interactivamente
def predict_from_files(csv_path, model_path, output_path=None):
    """
    Función simplificada para usar en notebooks o scripts
    
    Args:
        csv_path: Ruta al archivo CSV
        model_path: Ruta al modelo .joblib
        output_path: Ruta para guardar (opcional)
    
    Returns:
        DataFrame con predicciones
    """
    predictor = VacancyPredictor()
    
    # Cargar modelo
    if not predictor.load_model(model_path):
        return None
    
    # Cargar datos
    df = predictor.load_data(csv_path)
    if df is None:
        return None
    
    # Predecir
    result_df = predictor.predict_vacancies(df)
    
    # Guardar si se especifica ruta
    if output_path and result_df is not None:
        predictor.save_results(result_df, output_path)
    
    return result_df

if __name__ == "__main__":
    # Ejemplo de uso directo (sin argumentos)
    if len(sys.argv) == 1:
        print("🔮 PREDICTOR DE VACANCIES")
        print("="*50)
        print("\nUso desde línea de comandos:")
        print("python predictor.py --csv datos.csv --model modelo.joblib [--output resultados.csv]")
        print("\nUso desde Python:")
        print("result_df = predict_from_files('datos.csv', 'modelo.joblib')")
        print("\nEjemplo interactivo:")
        
        # Ejemplo interactivo si los archivos existen
        if Path("dataset_ovito_convexhull.csv").exists():
            csv_file = "dataset_ovito_convexhull.csv"
            print(f"\n📁 Archivo CSV encontrado: {csv_file}")
            
            # Buscar archivos .joblib en el directorio actual
            joblib_files = list(Path(".").glob("*.joblib"))
            if joblib_files:
                model_file = str(joblib_files[0])
                print(f"🤖 Archivo modelo encontrado: {model_file}")
                print("\n🚀 Ejecutando predicción de ejemplo...")
                
                result = predict_from_files(csv_file, model_file, "ejemplo_predicciones.csv")
                if result is not None:
                    print("\n📊 Primeras 5 predicciones:")
                    cols_to_show = ['file'] if 'file' in result.columns else []
                    cols_to_show.extend(['vacancies_predicted'])
                    if 'vacancies' in result.columns:
                        cols_to_show.append('vacancies')
                    print(result[cols_to_show].head())
            else:
                print("🔍 No se encontraron archivos .joblib para el ejemplo")
        else:
            print("🔍 No se encontró dataset_ovito_convexhull.csv para el ejemplo")
    else:
        main()