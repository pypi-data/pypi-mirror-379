"""
REEMPLAZO DIRECTO de las funciones existentes con versiones mejoradas
Mantiene EXACTAMENTE los mismos nombres para copy-paste directo
"""
import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import KFold, cross_validate, learning_curve
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import make_scorer, mean_absolute_error, mean_squared_error, r2_score
from scipy import stats
import time
import warnings
warnings.filterwarnings('ignore')

def plot_kfold_results(model, X, y, cv_folds=5, random_state=42, figsize=(20, 16)):
    """
    VERSIÓN MEJORADA - Crear visualización completa de resultados K-Fold Cross Validation
    MANTIENE el mismo nombre y parámetros de la función original
    
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
    - stats: diccionario con estadísticas (AÑADIDO)
    """
    
    # Definir métricas personalizadas (MEJORADO)
    def rmse_score(y_true, y_pred):
        return np.sqrt(mean_squared_error(y_true, y_pred))
    
    def mape_score(y_true, y_pred):
        return np.mean(np.abs((y_true - y_pred) / np.where(y_true != 0, y_true, 1e-8))) * 100
    
    def median_ae_score(y_true, y_pred):
        return np.median(np.abs(y_true - y_pred))
    
    # Definir scoring completo (EXPANDIDO)
    scoring = {
        'r2': 'r2',
        'mae': 'neg_mean_absolute_error',
        'rmse': make_scorer(rmse_score, greater_is_better=False),
        'mape': make_scorer(mape_score, greater_is_better=False),
        'median_ae': make_scorer(median_ae_score, greater_is_better=False),
        'explained_var': 'explained_variance'
    }
    
    # Configurar K-Fold
    kfold = KFold(n_splits=cv_folds, shuffle=True, random_state=random_state)
    
    print(f"Realizando {cv_folds}-Fold Cross Validation MEJORADO...")
    
    # ANÁLISIS EXPANDIDO - Cross validation con tiempos
    start_time = time.time()
    cv_results = cross_validate(model, X, y, cv=kfold, scoring=scoring, 
                               return_train_score=True, n_jobs=-1)
    total_cv_time = time.time() - start_time
    
    # NUEVO - Análisis detallado por fold
    fold_detailed_results = []
    fold_predictions = []
    fold_feature_importances = []
    fold_training_times = []
    
    for fold_idx, (train_idx, test_idx) in enumerate(kfold.split(X), 1):
        print(f"  Procesando Fold {fold_idx}/{cv_folds}...")
        
        fold_start_time = time.time()
        
        # Dividir datos
        X_train_fold = X.iloc[train_idx] if hasattr(X, 'iloc') else X[train_idx]
        X_test_fold = X.iloc[test_idx] if hasattr(X, 'iloc') else X[test_idx]
        y_train_fold = y.iloc[train_idx] if hasattr(y, 'iloc') else y[train_idx]
        y_test_fold = y.iloc[test_idx] if hasattr(y, 'iloc') else y[test_idx]
        
        # Entrenar modelo para este fold
        fold_model = model.__class__(**model.get_params())
        fold_model.fit(X_train_fold, y_train_fold)
        
        fold_train_time = time.time() - fold_start_time
        fold_training_times.append(fold_train_time)
        
        # Predicciones
        y_pred_train = fold_model.predict(X_train_fold)
        y_pred_test = fold_model.predict(X_test_fold)
        
        # Calcular métricas detalladas
        train_metrics = {
            'r2': r2_score(y_train_fold, y_pred_train),
            'mae': mean_absolute_error(y_train_fold, y_pred_train),
            'rmse': rmse_score(y_train_fold, y_pred_train),
            'mape': mape_score(y_train_fold, y_pred_train),
            'median_ae': median_ae_score(y_train_fold, y_pred_train)
        }
        
        test_metrics = {
            'r2': r2_score(y_test_fold, y_pred_test),
            'mae': mean_absolute_error(y_test_fold, y_pred_test),
            'rmse': rmse_score(y_test_fold, y_pred_test),
            'mape': mape_score(y_test_fold, y_pred_test),
            'median_ae': median_ae_score(y_test_fold, y_pred_test)
        }
        
        # Guardar resultados detallados
        fold_result = {
            'fold': fold_idx,
            'train_size': len(X_train_fold),
            'test_size': len(X_test_fold),
            'training_time': fold_train_time,
            **{f'train_{k}': v for k, v in train_metrics.items()},
            **{f'test_{k}': v for k, v in test_metrics.items()},
            'r2_diff': train_metrics['r2'] - test_metrics['r2'],
            'mae_diff': test_metrics['mae'] - train_metrics['mae']
        }
        
        fold_detailed_results.append(fold_result)
        
        # Guardar predicciones para análisis de residuos
        fold_predictions.append({
            'fold': fold_idx,
            'y_true': y_test_fold,
            'y_pred': y_pred_test,
            'residuals': y_test_fold - y_pred_test if hasattr(y_test_fold, '__sub__') else np.array(y_test_fold) - y_pred_test
        })
        
        # Feature importance de este fold
        if hasattr(fold_model, 'feature_importances_'):
            fold_feature_importances.append(fold_model.feature_importances_)
    
    # Crear DataFrame con resultados (EXPANDIDO)
    results_df = pd.DataFrame(fold_detailed_results)
    
    # NUEVO - Learning Curves
    print("  Calculando learning curves...")
    try:
        train_sizes = np.logspace(np.log10(100), np.log10(len(X)), 6).astype(int)
        train_sizes_lc, train_scores_lc, test_scores_lc = learning_curve(
            model, X, y, train_sizes=train_sizes, cv=cv_folds, 
            scoring='r2', n_jobs=-1, random_state=random_state
        )
    except:
        train_sizes_lc = train_scores_lc = test_scores_lc = None
    
    # NUEVO - Análisis de feature importance
    feature_importance_stability = None
    if fold_feature_importances:
        feature_names = X.columns if hasattr(X, 'columns') else [f'feature_{i}' for i in range(X.shape[1])]
        importance_df = pd.DataFrame(fold_feature_importances, columns=feature_names)
        feature_importance_stability = pd.DataFrame({
            'feature': feature_names,
            'mean_importance': importance_df.mean(),
            'std_importance': importance_df.std(),
            'cv_importance': importance_df.std() / (importance_df.mean() + 1e-8)
        }).sort_values('mean_importance', ascending=False)
    
    # Crear figura EXPANDIDA (4x4 = 16 subplots)
    fig, axes = plt.subplots(4, 4, figsize=figsize)
    fig.suptitle(f'Análisis K-Fold Cross Validation COMPLETO ({cv_folds} folds)', 
                 fontsize=18, fontweight='bold', y=0.98)
    
    # Colores mejorados
    colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#00B4D8', '#7209B7']
    
    # ====================== FILA 1: MÉTRICAS PRINCIPALES ======================
    
    # 1.1 Box Plot de Métricas (Test) - MEJORADO
    ax = axes[0, 0]
    test_metrics_data = [
        results_df['test_r2'], 
        results_df['test_mae'], 
        results_df['test_rmse'], 
        results_df['test_mape']/10  # Escalar MAPE para visualización
    ]
    bp = ax.boxplot(test_metrics_data, labels=['R²', 'MAE', 'RMSE', 'MAPE/10'], patch_artist=True)
    for patch, color in zip(bp['boxes'], colors[:4]):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    ax.set_title('Distribución Métricas (Test)', fontweight='bold')
    ax.set_ylabel('Valor')
    ax.grid(True, alpha=0.3)
    
    # 1.2 R² Train vs Test por Fold - EXPANDIDO
    ax = axes[0, 1]
    folds = results_df['fold']
    ax.plot(folds, results_df['train_r2'], 'o-', label='Train R²', 
            color='green', linewidth=2, markersize=8)
    ax.plot(folds, results_df['test_r2'], 'o-', label='Test R²', 
            color='red', linewidth=2, markersize=8)
    ax.fill_between(folds, results_df['train_r2'], results_df['test_r2'], 
                    alpha=0.2, color='gray', label='Gap (Overfitting)')
    ax.set_title('R² por Fold: Train vs Test', fontweight='bold')
    ax.set_xlabel('Fold')
    ax.set_ylabel('R² Score')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xticks(folds)
    
    # 1.3 NUEVO - Indicadores de Overfitting
    ax = axes[0, 2]
    overfitting_r2 = results_df['r2_diff']
    bars = ax.bar(folds, overfitting_r2, color=colors[1], alpha=0.7)
    ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
    ax.axhline(y=0.1, color='red', linestyle='--', alpha=0.7, label='Threshold 0.1')
    ax.axhline(y=0.05, color='orange', linestyle='--', alpha=0.7, label='Threshold 0.05')
    ax.set_title('Overfitting por Fold', fontweight='bold')
    ax.set_xlabel('Fold')
    ax.set_ylabel('R² Diff (Train-Test)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xticks(folds)
    
    # Añadir valores
    for bar, val in zip(bars, overfitting_r2):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.005,
                f'{val:.3f}', ha='center', va='bottom', fontsize=9)
    
    # 1.4 NUEVO - Tiempos de Entrenamiento
    ax = axes[0, 3]
    bars = ax.bar(folds, fold_training_times, color=colors[2], alpha=0.7)
    ax.set_title('Tiempo Entrenamiento por Fold', fontweight='bold')
    ax.set_xlabel('Fold')
    ax.set_ylabel('Tiempo (s)')
    ax.grid(True, alpha=0.3)
    ax.set_xticks(folds)
    for bar, val in zip(bars, fold_training_times):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{val:.2f}s', ha='center', va='bottom', fontsize=8)
    
    # ====================== FILA 2: ANÁLISIS DE ERRORES ======================
    
    # 2.1 NUEVO - Histograma R² con distribución normal
    ax = axes[1, 0]
    r2_values = results_df['test_r2']
    ax.hist(r2_values, bins=max(3, cv_folds//2), alpha=0.7, color=colors[0], 
            edgecolor='black', density=True)
    
    if len(r2_values) > 1:
        mu, sigma = stats.norm.fit(r2_values)
        x = np.linspace(r2_values.min(), r2_values.max(), 100)
        ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2, 
                label=f'Normal (μ={mu:.3f}, σ={sigma:.3f})')
        ax.legend()
    
    ax.axvline(r2_values.mean(), color='red', linestyle='--', linewidth=2, 
               label=f'Media: {r2_values.mean():.3f}')
    ax.set_title('Distribución R² Scores', fontweight='bold')
    ax.set_xlabel('R² Score')
    ax.set_ylabel('Densidad')
    ax.grid(True, alpha=0.3)
    
    # 2.2 NUEVO - MAE vs RMSE scatter
    ax = axes[1, 1]
    scatter = ax.scatter(results_df['test_mae'], results_df['test_rmse'], 
                        s=100, c=folds, cmap='viridis', alpha=0.7)
    ax.set_title('MAE vs RMSE por Fold', fontweight='bold')
    ax.set_xlabel('MAE')
    ax.set_ylabel('RMSE')
    ax.grid(True, alpha=0.3)
    plt.colorbar(scatter, ax=ax, shrink=0.8, label='Fold')
    
    # 2.3 NUEVO - Estabilidad del Modelo
    ax = axes[1, 2]
    metrics_cv = []
    metric_names = ['R²', 'MAE', 'RMSE', 'MAPE']
    for metric in ['test_r2', 'test_mae', 'test_rmse', 'test_mape']:
        cv_coef = results_df[metric].std() / abs(results_df[metric].mean()) if results_df[metric].mean() != 0 else 0
        metrics_cv.append(cv_coef)
    
    bars = ax.bar(metric_names, metrics_cv, color=colors[:4], alpha=0.7)
    ax.axhline(y=0.1, color='red', linestyle='--', alpha=0.7, label='Threshold 0.1')
    ax.set_title('Estabilidad Modelo (CV)', fontweight='bold')
    ax.set_xlabel('Métrica')
    ax.set_ylabel('Coef. Variación')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    for bar, val in zip(bars, metrics_cv):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.005,
                f'{val:.3f}', ha='center', va='bottom', fontsize=9)
    
    # 2.4 NUEVO - Distribución tamaños de muestra
    ax = axes[1, 3]
    x = np.arange(len(folds))
    width = 0.35
    ax.bar(x - width/2, results_df['train_size'], width, 
           label='Train Size', color='lightblue', alpha=0.8)
    ax.bar(x + width/2, results_df['test_size'], width, 
           label='Test Size', color='lightcoral', alpha=0.8)
    ax.set_title('Tamaños Muestra por Fold', fontweight='bold')
    ax.set_xlabel('Fold')
    ax.set_ylabel('Nº Muestras')
    ax.set_xticks(x)
    ax.set_xticklabels([f'F{i}' for i in folds])
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # ====================== FILA 3: ANÁLISIS RESIDUOS ======================
    
    # 3.1 NUEVO - Residuos por Fold
    ax = axes[2, 0]
    all_residuals = []
    for pred_data in fold_predictions:
        residuals = pred_data['residuals']
        all_residuals.extend(residuals)
    
    residuals_by_fold = [fold_predictions[i]['residuals'] for i in range(cv_folds)]
    bp = ax.boxplot(residuals_by_fold, labels=[f'F{i+1}' for i in range(cv_folds)], 
                    patch_artist=True)
    for patch, color in zip(bp['boxes'], colors[:cv_folds]):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax.axhline(y=0, color='red', linestyle='--', linewidth=2)
    ax.set_title('Residuos por Fold', fontweight='bold')
    ax.set_xlabel('Fold')
    ax.set_ylabel('Residuos')
    ax.grid(True, alpha=0.3)
    
    # 3.2 NUEVO - Q-Q Plot de Residuos
    ax = axes[2, 1]
    if len(all_residuals) > 0:
        stats.probplot(all_residuals, dist="norm", plot=ax)
        ax.set_title('Q-Q Plot Residuos', fontweight='bold')
        ax.grid(True, alpha=0.3)
    
    # 3.3 NUEVO - Residuos vs Predicciones
    ax = axes[2, 2]
    for i, pred_data in enumerate(fold_predictions):
        ax.scatter(pred_data['y_pred'], pred_data['residuals'], 
                   alpha=0.6, s=30, c=colors[i % len(colors)], label=f'Fold {i+1}')
    ax.axhline(y=0, color='red', linestyle='--', linewidth=2)
    ax.set_title('Residuos vs Predicciones', fontweight='bold')
    ax.set_xlabel('Predicciones')
    ax.set_ylabel('Residuos')
    ax.legend(fontsize=8, ncol=2)
    ax.grid(True, alpha=0.3)
    
    # 3.4 NUEVO - Histograma de Residuos
    ax = axes[2, 3]
    if len(all_residuals) > 0:
        ax.hist(all_residuals, bins=20, alpha=0.7, color=colors[0], 
                edgecolor='black', density=True)
        
        mu, sigma = stats.norm.fit(all_residuals)
        x = np.linspace(min(all_residuals), max(all_residuals), 100)
        ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2, 
                label=f'Normal (μ={mu:.2f}, σ={sigma:.2f})')
        
        # Test de normalidad
        if len(all_residuals) <= 5000:
            try:
                shapiro_stat, shapiro_p = stats.shapiro(all_residuals)
                ax.text(0.05, 0.95, f'Shapiro p={shapiro_p:.3f}', 
                        transform=ax.transAxes, 
                        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
                        verticalalignment='top', fontsize=9)
            except:
                pass
        
        ax.set_title('Distribución Residuos', fontweight='bold')
        ax.set_xlabel('Residuos')
        ax.set_ylabel('Densidad')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    # ====================== FILA 4: ANÁLISIS AVANZADOS ======================
    
    # 4.1 NUEVO - Learning Curves
    ax = axes[3, 0]
    if train_sizes_lc is not None:
        train_mean = np.mean(train_scores_lc, axis=1)
        train_std = np.std(train_scores_lc, axis=1)
        test_mean = np.mean(test_scores_lc, axis=1)
        test_std = np.std(test_scores_lc, axis=1)
        
        ax.plot(train_sizes_lc, train_mean, 'o-', color='green', label='Training')
        ax.fill_between(train_sizes_lc, train_mean - train_std, train_mean + train_std, 
                        alpha=0.1, color='green')
        
        ax.plot(train_sizes_lc, test_mean, 'o-', color='red', label='Cross-Val')
        ax.fill_between(train_sizes_lc, test_mean - test_std, test_mean + test_std, 
                        alpha=0.1, color='red')
        
        ax.set_title('Learning Curves', fontweight='bold')
        ax.set_xlabel('Tamaño Entrenamiento')
        ax.set_ylabel('R² Score')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_xscale('log')
    else:
        ax.text(0.5, 0.5, 'Learning Curves\nno calculadas', 
                ha='center', va='center', transform=ax.transAxes)
    
    # 4.2 NUEVO - Feature Importance Estabilidad
    ax = axes[3, 1]
    if feature_importance_stability is not None:
        top_features = feature_importance_stability.head(10)
        x_pos = np.arange(len(top_features))
        bars = ax.barh(x_pos, top_features['mean_importance'], 
                       xerr=top_features['std_importance'], capsize=3, 
                       color=colors[0], alpha=0.7)
        ax.set_yticks(x_pos)
        ax.set_yticklabels(top_features['feature'], fontsize=9)
        ax.set_title('Feature Importance ±Std', fontweight='bold')
        ax.set_xlabel('Importancia')
        ax.grid(True, alpha=0.3)
        ax.invert_yaxis()
    else:
        ax.text(0.5, 0.5, 'Feature Importance\nno disponible', 
                ha='center', va='center', transform=ax.transAxes)
        ax.axis('off')
    
    # 4.3 NUEVO - Matriz correlación métricas
    ax = axes[3, 2]
    metrics_for_corr = results_df[['test_r2', 'test_mae', 'test_rmse', 'test_mape']]
    correlation_matrix = metrics_for_corr.corr()
    
    im = ax.imshow(correlation_matrix, cmap='RdBu_r', aspect='auto', vmin=-1, vmax=1)
    metric_labels = ['R²', 'MAE', 'RMSE', 'MAPE']
    ax.set_xticks(range(len(metric_labels)))
    ax.set_yticks(range(len(metric_labels)))
    ax.set_xticklabels(metric_labels)
    ax.set_yticklabels(metric_labels)
    ax.set_title('Correlación Métricas', fontweight='bold')
    
    for i in range(len(metric_labels)):
        for j in range(len(metric_labels)):
            ax.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}',
                    ha='center', va='center', color='white', fontweight='bold')
    
    plt.colorbar(im, ax=ax, shrink=0.8)
    
    # 4.4 EXPANDIDO - Resumen estadístico
    ax = axes[3, 3]
    ax.axis('off')
    
    # Estadísticas resumidas (EXPANDIDAS)
    r2_stats = results_df['test_r2'].describe()
    mae_stats = results_df['test_mae'].describe()
    stability_score = np.mean(metrics_cv)
    avg_overfitting = results_df['r2_diff'].mean()
    
    summary_text = f"""RESUMEN K-FOLD EXPANDIDO

CONFIGURACIÓN:
• Folds: {cv_folds}
• Muestras: {len(X)}
• Features: {X.shape[1] if hasattr(X, 'shape') else len(X[0])}
• Tiempo CV: {total_cv_time:.1f}s

MÉTRICAS PRINCIPALES:
• R²: {r2_stats['mean']:.4f} ± {r2_stats['std']:.4f}
• MAE: {mae_stats['mean']:.4f} ± {mae_stats['std']:.4f}
• Rango R²: [{r2_stats['min']:.3f}, {r2_stats['max']:.3f}]

DIAGNÓSTICOS:
• Estabilidad: {stability_score:.3f}
• Overfitting: {avg_overfitting:.3f}
• Tiempo/fold: {np.mean(fold_training_times):.2f}s

INTERPRETACIÓN:
• Calidad: {"Excelente" if r2_stats['mean'] > 0.9 else "Buena" if r2_stats['mean'] > 0.7 else "Moderada"}
• Estabilidad: {"Alta" if stability_score < 0.05 else "Media" if stability_score < 0.1 else "Baja"}
• Overfitting: {"Bajo" if avg_overfitting < 0.05 else "Moderado" if avg_overfitting < 0.1 else "Alto"}

NUEVAS CARACTERÍSTICAS:
✓ 16 visualizaciones
✓ Learning curves
✓ Análisis residuos
✓ Test normalidad
✓ Tiempos monitorizados
✓ Correlaciones métricas
"""
    
    ax.text(0.05, 0.95, summary_text, transform=ax.transAxes, fontsize=8,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8),
            verticalalignment='top', fontfamily='monospace')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    
    # Crear diccionario de estadísticas (EXPANDIDO)
    stats_summary = {
        'mean_r2': r2_stats['mean'],
        'std_r2': r2_stats['std'],
        'mean_mae': mae_stats['mean'],
        'std_mae': mae_stats['std'],
        'mean_rmse': results_df['test_rmse'].mean(),
        'std_rmse': results_df['test_rmse'].std(),
        'mean_mape': results_df['test_mape'].mean(),
        'std_mape': results_df['test_mape'].std(),
        'stability_score': stability_score,
        'avg_overfitting': avg_overfitting,
        'total_cv_time': total_cv_time,
        'avg_fold_time': np.mean(fold_training_times),
        'cv_folds': cv_folds
    }
    
    # Mostrar estadísticas expandidas en consola
    print("\n" + "="*70)
    print("RESULTADOS K-FOLD CROSS VALIDATION - VERSIÓN EXPANDIDA")
    print("="*70)
    
    print(f"\nCONFIGURACIÓN:")
    print(f"  Folds: {cv_folds} | Muestras: {len(X)} | Features: {X.shape[1] if hasattr(X, 'shape') else len(X[0])}")
    print(f"  Tiempo total: {total_cv_time:.2f}s | Tiempo/fold: {np.mean(fold_training_times):.2f}s")
    
    print(f"\nMÉTRICAS PRINCIPALES:")
    print(f"  R²:   {r2_stats['mean']:.4f} ± {r2_stats['std']:.4f}  [{r2_stats['min']:.3f}, {r2_stats['max']:.3f}]")
    print(f"  MAE:  {mae_stats['mean']:.4f} ± {mae_stats['std']:.4f}")
    print(f"  RMSE: {results_df['test_rmse'].mean():.4f} ± {results_df['test_rmse'].std():.4f}")
    print(f"  MAPE: {results_df['test_mape'].mean():.2f}% ± {results_df['test_mape'].std():.2f}%")
    
    print(f"\nDIAGNÓSTICOS AVANZADOS:")
    print(f"  Estabilidad (CV promedio): {stability_score:.3f}")
    print(f"  Overfitting promedio: {avg_overfitting:.3f}")
    
    quality = "Excelente" if r2_stats['mean'] > 0.9 else "Buena" if r2_stats['mean'] > 0.7 else "Moderada" if r2_stats['mean'] > 0.5 else "Pobre"
    stability = "Alta" if stability_score < 0.05 else "Media" if stability_score < 0.1 else "Baja"
    overfitting_level = "Bajo" if avg_overfitting < 0.05 else "Moderado" if avg_overfitting < 0.1 else "Alto"
    
    print(f"\nINTERPRETACIÓN AUTOMÁTICA:")
    print(f"  Calidad: {quality} (R² = {r2_stats['mean']:.3f})")
    print(f"  Estabilidad: {stability} (CV = {stability_score:.3f})")
    print(f"  Overfitting: {overfitting_level} (Gap = {avg_overfitting:.3f})")
    
    print(f"\nNUEVAS CARACTERÍSTICAS AÑADIDAS:")
    print("  ✓ 16 visualizaciones (vs 6 originales)")
    print("  ✓ Learning curves calculadas")
    print("  ✓ Análisis de residuos completo")
    print("  ✓ Tests de normalidad")
    print("  ✓ Tiempos de entrenamiento monitorizados")
    print("  ✓ Correlaciones entre métricas")
    print("  ✓ Estabilidad de feature importance")
    
    print("="*70)
    
    return fig, results_df, stats_summary


def visualize_kfold(self):
    """
    VERSIÓN MEJORADA - Visualización de K-Fold Cross Validation
    MANTIENE el mismo nombre del método original
    """
    if self.current_data is None or self.trained_model is None:
        messagebox.showwarning("Advertencia", "Carga datos y entrena un modelo primero")
        return
    
    try:
        # Actualizar estado
        self.kfold_status_label.config(text="🔄 Ejecutando K-Fold MEJORADO...", foreground="orange")
        self.kfold_btn.config(state="disabled")
        self.parent.update()
        
        # Preparar datos
        X = self.current_data[self.feature_columns]
        y = self.current_data[self.target_column]
        
        # Limpiar datos si es necesario
        if X.isnull().any().any():
            from sklearn.impute import SimpleImputer
            imputer = SimpleImputer(strategy='median')
            X_clean = pd.DataFrame(imputer.fit_transform(X), columns=X.columns, index=X.index)
        else:
            X_clean = X
        
        # Crear modelo con los mismos parámetros
        from sklearn.ensemble import RandomForestRegressor
        model = RandomForestRegressor(
            n_estimators=self.n_estimators_var.get(),
            random_state=self.random_state_var.get(),
            n_jobs=-1
        )
        
        # Llamar función MEJORADA de visualización K-Fold
        fig, results_df, stats = plot_kfold_results(
            model, X_clean, y, cv_folds=5, 
            random_state=self.random_state_var.get(),
            figsize=(20, 16)  # Tamaño aumentado para 16 subplots
        )
        
        # Mostrar en ventana separada
        plt.show()
        
        # Actualizar log EXPANDIDO en el área de resultados
        if hasattr(self, 'results_text'):
            kfold_summary = f"""

=== K-FOLD CROSS VALIDATION MEJORADO COMPLETADO ===
Fecha: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
Tiempo de ejecución: {stats['total_cv_time']:.2f}s

📊 MÉTRICAS PRINCIPALES ({stats['cv_folds']}-Fold):
   R²:   {stats['mean_r2']:.4f} ± {stats['std_r2']:.4f}
   MAE:  {stats['mean_mae']:.4f} ± {stats['std_mae']:.4f}
   RMSE: {stats['mean_rmse']:.4f} ± {stats['std_rmse']:.4f}
   MAPE: {stats['mean_mape']:.2f}% ± {stats['std_mape']:.2f}%

🔍 ANÁLISIS AVANZADO:
   Estabilidad general: {stats['stability_score']:.3f}
   Overfitting promedio: {stats['avg_overfitting']:.3f}
   Tiempo promedio/fold: {stats['avg_fold_time']:.2f}s

📈 INTERPRETACIÓN:
   Calidad: {'Excelente' if stats['mean_r2'] > 0.9 else 'Buena' if stats['mean_r2'] > 0.7 else 'Moderada'}
   Estabilidad: {'Alta' if stats['stability_score'] < 0.05 else 'Media' if stats['stability_score'] < 0.1 else 'Baja'}
   Overfitting: {'Bajo' if stats['avg_overfitting'] < 0.05 else 'Moderado' if stats['avg_overfitting'] < 0.1 else 'Alto'}

🆕 NUEVAS CARACTERÍSTICAS IMPLEMENTADAS:
   ✓ 16 visualizaciones detalladas (vs 6 originales)
   ✓ Learning curves para análisis de convergencia
   ✓ Análisis completo de residuos (Q-Q plots, normalidad)
   ✓ Correlaciones entre métricas
   ✓ Tiempos de entrenamiento monitorizados
   ✓ Estabilidad de feature importance
   ✓ Tests estadísticos automáticos
   ✓ Interpretación automática de resultados
   ✓ Diagnósticos de overfitting expandidos

💡 RECOMENDACIONES ESPECÍFICAS:
"""
            
            # Recomendaciones automáticas
            if stats['mean_r2'] > 0.8 and stats['stability_score'] < 0.1 and stats['avg_overfitting'] < 0.05:
                kfold_summary += "   ✅ Modelo robusto y estable - Listo para producción\n"
            else:
                kfold_summary += "   ⚠️ Considerar mejoras específicas:\n"
                if stats['mean_r2'] < 0.7:
                    kfold_summary += "      • Mejorar R² con feature engineering o hiperparámetros\n"
                if stats['stability_score'] > 0.1:
                    kfold_summary += "      • Aumentar estabilidad con más datos o regularización\n"
                if stats['avg_overfitting'] > 0.1:
                    kfold_summary += "      • Reducir overfitting con técnicas de regularización\n"
            
            self.results_text.insert(tk.END, kfold_summary)
        
        # Actualizar estado
        self.kfold_status_label.config(text="✅ K-Fold MEJORADO completado", foreground="green")
        
        # Guardar resultados para posible exportación futura
        self.kfold_expanded_results = {
            'fig': fig,
            'results_df': results_df, 
            'stats': stats,
            'timestamp': pd.Timestamp.now()
        }
        
        return fig, results_df, stats
        
    except Exception as e:
        messagebox.showerror("Error", f"Error en K-Fold mejorado:\n{str(e)}")
        self.kfold_status_label.config(text="❌ Error en K-Fold", foreground="red")
        print(f"Error K-Fold: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        self.kfold_btn.config(state="normal")


# Función de integración con tu código existente - MANTIENE NOMBRE ORIGINAL
def integrate_kfold_visualization(ml_tab_instance):
    """
    VERSIÓN MEJORADA - Integrar visualización k-fold en AdvancedMLTab
    MANTIENE el nombre original de la función
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
    from sklearn.ensemble import RandomForestRegressor
    model = RandomForestRegressor(
        n_estimators=ml_tab_instance.n_estimators_var.get(),
        random_state=ml_tab_instance.random_state_var.get(),
        n_jobs=-1
    )
    
    # Ejecutar visualización MEJORADA
    fig, results_df, stats_summary = plot_kfold_results(
        model, X_clean, y, cv_folds=5, 
        random_state=ml_tab_instance.random_state_var.get(),
        figsize=(20, 16)
    )
    
    return fig, results_df, stats_summary


# EJEMPLO DE USO - Exactamente igual que el original, pero mejorado
if __name__ == "__main__":
    # Generar datos de ejemplo
    from sklearn.datasets import make_regression
    
    print("Generando datos de ejemplo...")
    X, y = make_regression(n_samples=1000, n_features=20, noise=0.1, random_state=42)
    X_df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(20)])
    y_series = pd.Series(y, name='target')
    
    # Crear modelo
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    
    # Ejecutar visualización MEJORADA (usando la misma función que antes)
    fig, results_df, stats_summary = plot_kfold_results(
        rf_model, X_df, y_series, cv_folds=5, random_state=42
    )
    
    plt.show()
    
    print("\nDataFrame de resultados:")
    print(results_df.round(4))
    
    print(f"\nEstadísticas expandidas disponibles:")
    print(f"  - {len(stats_summary)} métricas estadísticas")
    print(f"  - Análisis de estabilidad incluido")
    print(f"  - Diagnósticos de overfitting incluidos")