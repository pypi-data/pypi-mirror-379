"""
Visualización completa de resultados K-Fold Cross Validation para Random Forest
Incluye múltiples métricas y gráficos informativos
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import KFold, cross_val_score, cross_validate
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import make_scorer, mean_absolute_error, mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

def plot_kfold_results(model, X, y, cv_folds=5, random_state=42, figsize=(18, 12)):
    """
    Crear visualización completa de resultados K-Fold Cross Validation
    
    Parámetros:
    - model: modelo de Random Forest
    - X: features (DataFrame o array)
    - y: target (Series o array)
    - cv_folds: número de folds para cross validation
    - random_state: semilla para reproducibilidad
    - figsize: tamaño de la figura
    
    Retorna:
    - fig: figura de matplotlib
    - results_df: DataFrame con resultados detallados
    """
    
    # Definir métricas personalizadas
    def rmse_score(y_true, y_pred):
        return np.sqrt(mean_squared_error(y_true, y_pred))
    
    def mape_score(y_true, y_pred):
        return np.mean(np.abs((y_true - y_pred) / np.where(y_true != 0, y_true, 1e-8))) * 100
    
    # Definir scoring
    scoring = {
        'r2': 'r2',
        'mae': 'neg_mean_absolute_error',
        'rmse': make_scorer(rmse_score, greater_is_better=False),
        'mape': make_scorer(mape_score, greater_is_better=False)
    }
    
    # Configurar K-Fold
    kfold = KFold(n_splits=cv_folds, shuffle=True, random_state=random_state)
    
    print(f"Realizando {cv_folds}-Fold Cross Validation...")
    
    # Realizar cross validation
    cv_results = cross_validate(model, X, y, cv=kfold, scoring=scoring, 
                               return_train_score=True, n_jobs=-1)
    
    # Procesar resultados
    results_data = []
    fold_metrics = []
    
    for fold in range(cv_folds):
        fold_result = {
            'fold': fold + 1,
            'train_r2': cv_results['train_r2'][fold],
            'test_r2': cv_results['test_r2'][fold],
            'train_mae': -cv_results['train_mae'][fold],
            'test_mae': -cv_results['test_mae'][fold],
            'train_rmse': -cv_results['train_rmse'][fold],
            'test_rmse': -cv_results['test_rmse'][fold],
            'train_mape': -cv_results['train_mape'][fold],
            'test_mape': -cv_results['test_mape'][fold],
        }
        
        # Calcular diferencia (overfitting indicator)
        fold_result['r2_diff'] = fold_result['train_r2'] - fold_result['test_r2']
        fold_result['mae_diff'] = fold_result['test_mae'] - fold_result['train_mae']
        fold_result['rmse_diff'] = fold_result['test_rmse'] - fold_result['train_rmse']
        
        results_data.append(fold_result)
        fold_metrics.append([
            fold_result['test_r2'],
            fold_result['test_mae'],
            fold_result['test_rmse'],
            fold_result['test_mape']
        ])
    
    # Crear DataFrame con resultados
    results_df = pd.DataFrame(results_data)
    
    # Calcular estadísticas resumidas
    stats_summary = {
        'R²': {
            'mean': results_df['test_r2'].mean(),
            'std': results_df['test_r2'].std(),
            'min': results_df['test_r2'].min(),
            'max': results_df['test_r2'].max()
        },
        'MAE': {
            'mean': results_df['test_mae'].mean(),
            'std': results_df['test_mae'].std(),
            'min': results_df['test_mae'].min(),
            'max': results_df['test_mae'].max()
        },
        'RMSE': {
            'mean': results_df['test_rmse'].mean(),
            'std': results_df['test_rmse'].std(),
            'min': results_df['test_rmse'].min(),
            'max': results_df['test_rmse'].max()
        },
        'MAPE': {
            'mean': results_df['test_mape'].mean(),
            'std': results_df['test_mape'].std(),
            'min': results_df['test_mape'].min(),
            'max': results_df['test_mape'].max()
        }
    }
    
    # Crear figura con subplots
    fig, axes = plt.subplots(3, 3, figsize=figsize)
    fig.suptitle(f'Análisis {cv_folds}-Fold Cross Validation - Random Forest', 
                 fontsize=16, fontweight='bold', y=0.98)
    
    # Colores para consistencia
    colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']
    
    # 1. Box Plot de Métricas de Test
    ax1 = axes[0, 0]
    metrics_data = [results_df['test_r2'], results_df['test_mae'], 
                   results_df['test_rmse'], results_df['test_mape']]
    metrics_names = ['R²', 'MAE', 'RMSE', 'MAPE']
    
    # Normalizar métricas para visualización (0-1 scale)
    normalized_metrics = []
    for i, metric_data in enumerate(metrics_data):
        if metrics_names[i] == 'R²':
            normalized = metric_data  # R² ya está en 0-1
        else:
            normalized = (metric_data - metric_data.min()) / (metric_data.max() - metric_data.min())
        normalized_metrics.append(normalized)
    
    bp = ax1.boxplot(normalized_metrics, labels=metrics_names, patch_artist=True)
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax1.set_title('Distribución de Métricas (Normalizadas)', fontweight='bold')
    ax1.set_ylabel('Valor Normalizado')
    ax1.grid(True, alpha=0.3)
    
    # 2. Líneas por Fold - Train vs Test R²
    ax2 = axes[0, 1]
    folds = results_df['fold']
    ax2.plot(folds, results_df['train_r2'], 'o-', label='Train R²', 
             color='green', linewidth=2, markersize=6)
    ax2.plot(folds, results_df['test_r2'], 'o-', label='Test R²', 
             color='red', linewidth=2, markersize=6)
    ax2.fill_between(folds, results_df['train_r2'], results_df['test_r2'], 
                     alpha=0.2, color='gray')
    ax2.set_title('R² por Fold: Train vs Test', fontweight='bold')
    ax2.set_xlabel('Fold')
    ax2.set_ylabel('R² Score')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xticks(folds)
    
    # 3. Barras de Error de Métricas
    ax3 = axes[0, 2]
    metrics_means = [stats_summary[m]['mean'] for m in ['R²', 'MAE', 'RMSE', 'MAPE']]
    metrics_stds = [stats_summary[m]['std'] for m in ['R²', 'MAE', 'RMSE', 'MAPE']]
    
    # Normalizar para visualización
    max_mean = max(metrics_means[1:])  # Excluir R² que ya está normalizado
    normalized_means = [metrics_means[0]] + [m/max_mean for m in metrics_means[1:]]
    normalized_stds = [metrics_stds[0]] + [s/max_mean for s in metrics_stds[1:]]
    
    bars = ax3.bar(metrics_names, normalized_means, yerr=normalized_stds, 
                   capsize=5, color=colors, alpha=0.7)
    ax3.set_title('Media ± Desviación Estándar', fontweight='bold')
    ax3.set_ylabel('Valor Normalizado')
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Añadir valores en las barras
    for bar, mean_val, std_val in zip(bars, metrics_means, metrics_stds):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{mean_val:.3f}±{std_val:.3f}',
                ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # 4. Histograma de R² (métrica principal)
    ax4 = axes[1, 0]
    ax4.hist(results_df['test_r2'], bins=max(3, cv_folds//2), alpha=0.7, 
             color='skyblue', edgecolor='black')
    ax4.axvline(results_df['test_r2'].mean(), color='red', linestyle='--', 
                linewidth=2, label=f'Media = {results_df["test_r2"].mean():.3f}')
    ax4.set_title('Distribución de R² Scores', fontweight='bold')
    ax4.set_xlabel('R² Score')
    ax4.set_ylabel('Frecuencia')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    # 5. Indicador de Overfitting
    ax5 = axes[1, 1]
    bars_r2 = ax5.bar(folds, results_df['r2_diff'], color='orange', alpha=0.7, 
                      label='R² Diff (Train - Test)')
    ax5.axhline(y=0, color='black', linestyle='-', linewidth=1)
    ax5.axhline(y=0.1, color='red', linestyle='--', alpha=0.7, label='Threshold 0.1')
    ax5.set_title('Indicador de Overfitting', fontweight='bold')
    ax5.set_xlabel('Fold')
    ax5.set_ylabel('Diferencia R² (Train - Test)')
    ax5.legend()
    ax5.grid(True, alpha=0.3)
    ax5.set_xticks(folds)
    
    # Añadir valores
    for bar, val in zip(bars_r2, results_df['r2_diff']):
        height = bar.get_height()
        ax5.text(bar.get_x() + bar.get_width()/2., height + 0.005,
                f'{val:.3f}', ha='center', va='bottom', fontsize=9)
    
    # 6. Matriz de Correlación entre Métricas
    ax6 = axes[1, 2]
    metrics_corr_data = results_df[['test_r2', 'test_mae', 'test_rmse', 'test_mape']]
    correlation_matrix = metrics_corr_data.corr()
    
    im = ax6.imshow(correlation_matrix, cmap='RdBu_r', aspect='auto', vmin=-1, vmax=1)
    ax6.set_xticks(range(len(metrics_names)))
    ax6.set_yticks(range(len(metrics_names)))
    ax6.set_xticklabels(metrics_names)
    ax6.set_yticklabels(metrics_names)
    ax6.set_title('Correlación entre Métricas', fontweight='bold')
    
    # Añadir valores de correlación
    for i in range(len(metrics_names)):
        for j in range(len(metrics_names)):
            ax6.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}',
                    ha='center', va='center', color='white', fontweight='bold')
    
    plt.colorbar(im, ax=ax6, shrink=0.6)
    
    # 7. Comparación Train vs Test (todas las métricas)
    ax7 = axes[2, 0]
    x = np.arange(cv_folds)
    width = 0.35
    
    bars1 = ax7.bar(x - width/2, results_df['train_mae'], width, label='Train MAE', 
                    color='lightgreen', alpha=0.8)
    bars2 = ax7.bar(x + width/2, results_df['test_mae'], width, label='Test MAE', 
                    color='lightcoral', alpha=0.8)
    
    ax7.set_title('MAE: Train vs Test por Fold', fontweight='bold')
    ax7.set_xlabel('Fold')
    ax7.set_ylabel('MAE')
    ax7.set_xticks(x)
    ax7.set_xticklabels([f'Fold {i+1}' for i in range(cv_folds)])
    ax7.legend()
    ax7.grid(True, alpha=0.3)
    
    # 8. Estabilidad del Modelo (CV de métricas)
    ax8 = axes[2, 1]
    cv_coefficients = []
    metric_labels = []
    
    for metric in ['test_r2', 'test_mae', 'test_rmse', 'test_mape']:
        cv_coef = results_df[metric].std() / abs(results_df[metric].mean())
        cv_coefficients.append(cv_coef)
        metric_labels.append(metric.replace('test_', '').upper())
    
    bars_cv = ax8.bar(metric_labels, cv_coefficients, color=['green', 'orange', 'red', 'purple'], 
                      alpha=0.7)
    ax8.axhline(y=0.1, color='red', linestyle='--', alpha=0.7, label='Threshold 0.1')
    ax8.set_title('Estabilidad del Modelo (CV)', fontweight='bold')
    ax8.set_xlabel('Métrica')
    ax8.set_ylabel('Coeficiente de Variación')
    ax8.legend()
    ax8.grid(True, alpha=0.3)
    
    # Añadir valores
    for bar, val in zip(bars_cv, cv_coefficients):
        height = bar.get_height()
        ax8.text(bar.get_x() + bar.get_width()/2., height + 0.005,
                f'{val:.3f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # 9. Tabla de Resultados Resumida
    ax9 = axes[2, 2]
    ax9.axis('off')
    
    # Crear tabla con estadísticas
    table_data = []
    for metric in ['R²', 'MAE', 'RMSE', 'MAPE']:
        stats = stats_summary[metric]
        table_data.append([
            metric,
            f"{stats['mean']:.3f}",
            f"±{stats['std']:.3f}",
            f"[{stats['min']:.3f}, {stats['max']:.3f}]"
        ])
    
    table = ax9.table(cellText=table_data,
                     colLabels=['Métrica', 'Media', 'Std', 'Rango'],
                     cellLoc='center',
                     loc='center',
                     bbox=[0.1, 0.3, 0.8, 0.6])
    
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2)
    
    # Colorear encabezados
    for i in range(4):
        table[(0, i)].set_facecolor('#4CAF50')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    ax9.set_title('Resumen Estadístico', fontweight='bold', pad=20)
    
    # Añadir texto informativo
    info_text = f"""
Configuración K-Fold:
• Folds: {cv_folds}
• Muestras: {len(X)}
• Features: {X.shape[1] if hasattr(X, 'shape') else len(X[0])}

Interpretación:
• CV < 0.1: Modelo estable
• |R² diff| < 0.1: Sin overfitting significativo
• R² > 0.7: Buen rendimiento
"""
    
    ax9.text(0.05, 0.15, info_text, transform=ax9.transAxes, fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5),
            verticalalignment='top')
    
    plt.tight_layout()
    
    # Mostrar estadísticas en consola
    print("\n" + "="*60)
    print("RESULTADOS K-FOLD CROSS VALIDATION")
    print("="*60)
    
    for metric in ['R²', 'MAE', 'RMSE', 'MAPE']:
        stats = stats_summary[metric]
        cv_coef = stats['std'] / abs(stats['mean'])
        print(f"{metric:5s}: {stats['mean']:6.3f} ± {stats['std']:6.3f} "
              f"(CV: {cv_coef:5.3f}) [{stats['min']:6.3f}, {stats['max']:6.3f}]")
    
    print("\nANÁLISIS DE ESTABILIDAD:")
    avg_r2_diff = results_df['r2_diff'].mean()
    print(f"Overfitting promedio (R² diff): {avg_r2_diff:.3f}")
    
    if avg_r2_diff < 0.05:
        print("✅ Modelo bien balanceado (poco overfitting)")
    elif avg_r2_diff < 0.1:
        print("⚠️  Overfitting moderado")
    else:
        print("❌ Overfitting significativo")
    
    stability_score = np.mean(cv_coefficients)
    print(f"Estabilidad general (CV promedio): {stability_score:.3f}")
    
    if stability_score < 0.1:
        print("✅ Modelo muy estable")
    elif stability_score < 0.2:
        print("⚠️  Modelo moderadamente estable")
    else:
        print("❌ Modelo inestable")
    
    return fig, results_df, stats_summary


# Función para integrar con tu código existente
def integrate_kfold_visualization(ml_tab_instance):
    """
    Integrar visualización k-fold en tu clase AdvancedMLTab
    """
    if ml_tab_instance.current_data is None:
        print("Error: No hay datos cargados")
        return None, None, None
    
    if ml_tab_instance.trained_model is None:
        print("Error: No hay modelo entrenado")
        return None, None, None
    
    # Preparar datos
    X = ml_tab_instance.current_data[ml_tab_instance.feature_columns]
    y = ml_tab_instance.current_data[ml_tab_instance.target_column]
    
    # Limpiar datos si es necesario
    if X.isnull().any().any():
        from sklearn.impute import SimpleImputer
        imputer = SimpleImputer(strategy='median')
        X_clean = pd.DataFrame(imputer.fit_transform(X), columns=X.columns, index=X.index)
    else:
        X_clean = X
    
    # Crear modelo con los mismos parámetros
    model = RandomForestRegressor(
        n_estimators=ml_tab_instance.n_estimators_var.get(),
        random_state=ml_tab_instance.random_state_var.get(),
        n_jobs=-1
    )
    
    # Ejecutar visualización
    fig, results_df, stats_summary = plot_kfold_results(
        model, X_clean, y, cv_folds=5, 
        random_state=ml_tab_instance.random_state_var.get()
    )
    
    return fig, results_df, stats_summary


# Ejemplo de uso directo
if __name__ == "__main__":
    # Generar datos de ejemplo
    from sklearn.datasets import make_regression
    
    print("Generando datos de ejemplo...")
    X, y = make_regression(n_samples=1000, n_features=20, noise=0.1, random_state=42)
    X_df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(20)])
    y_series = pd.Series(y, name='target')
    
    # Crear modelo
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    
    # Ejecutar visualización
    fig, results_df, stats_summary = plot_kfold_results(
        rf_model, X_df, y_series, cv_folds=5, random_state=42
    )
    
    plt.show()
    
    print("\nDataFrame de resultados:")
    print(results_df.round(4))