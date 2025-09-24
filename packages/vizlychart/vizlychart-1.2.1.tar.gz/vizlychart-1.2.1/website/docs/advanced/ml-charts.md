# Machine Learning Visualizations

VizlyChart provides comprehensive support for machine learning visualizations, from model performance analysis to feature importance and explainability. These specialized charts help data scientists understand, debug, and communicate ML model insights.

## Overview

VizlyChart's ML visualization suite includes:

- **Model Performance**: ROC curves, precision-recall, confusion matrices
- **Feature Analysis**: Feature importance, correlation analysis, distribution plots
- **Model Explainability**: SHAP values, LIME explanations, partial dependence
- **Training Diagnostics**: Learning curves, validation plots, convergence analysis
- **Comparative Analysis**: Model comparison, A/B testing visualizations

## Model Performance Visualizations

### ROC Curves and AUC Analysis

```python
import vizlychart as vc
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import numpy as np

# Prepare sample data
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train multiple models
models = {
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Logistic Regression': LogisticRegression(random_state=42),
    'SVM': SVC(probability=True, random_state=42)
}

# Create ROC comparison chart
roc_chart = vc.charts.ROCChart()

for name, model in models.items():
    model.fit(X_train, y_train)
    y_proba = model.predict_proba(X_test)[:, 1]

    fpr, tpr, _ = roc_curve(y_test, y_proba)
    auc_score = auc(fpr, tpr)

    roc_chart.add_curve(fpr, tpr, label=f'{name} (AUC = {auc_score:.3f})')

roc_chart.set_title('ROC Curve Comparison')
roc_chart.add_diagonal_line()  # Random classifier baseline
roc_chart.show()
```

### Precision-Recall Curves

```python
from sklearn.metrics import precision_recall_curve, average_precision_score

# Create precision-recall chart
pr_chart = vc.charts.PrecisionRecallChart()

for name, model in models.items():
    y_proba = model.predict_proba(X_test)[:, 1]
    precision, recall, _ = precision_recall_curve(y_test, y_proba)
    avg_precision = average_precision_score(y_test, y_proba)

    pr_chart.add_curve(recall, precision,
                       label=f'{name} (AP = {avg_precision:.3f})')

pr_chart.set_title('Precision-Recall Curve Comparison')
pr_chart.add_baseline(np.mean(y_test))  # No-skill baseline
pr_chart.show()
```

### Confusion Matrix Heatmap

```python
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Enhanced confusion matrix visualization
def plot_confusion_matrix(y_true, y_pred, class_names, model_name):
    cm = confusion_matrix(y_true, y_pred)

    # Create confusion matrix heatmap
    cm_chart = vc.HeatmapChart()
    cm_chart.plot(cm,
                  annot=True,
                  fmt='d',
                  cmap='Blues',
                  xticklabels=class_names,
                  yticklabels=class_names,
                  square=True)

    cm_chart.set_title(f'Confusion Matrix - {model_name}')
    cm_chart.set_xlabel('Predicted Label')
    cm_chart.set_ylabel('True Label')

    # Add accuracy metrics
    accuracy = np.sum(np.diag(cm)) / np.sum(cm)
    cm_chart.add_text(0.5, -0.1, f'Accuracy: {accuracy:.3f}',
                      transform='axes', ha='center')

    return cm_chart

# Generate confusion matrices for all models
for name, model in models.items():
    y_pred = model.predict(X_test)
    cm_chart = plot_confusion_matrix(y_test, y_pred, ['Class 0', 'Class 1'], name)
    cm_chart.show()
```

## Feature Importance Analysis

### Feature Importance Charts

```python
from sklearn.inspection import permutation_importance

# Create comprehensive feature importance visualization
def analyze_feature_importance(model, X_train, X_test, y_test, feature_names):
    """Comprehensive feature importance analysis"""

    # Get built-in feature importance (if available)
    importance_chart = vc.charts.FeatureImportanceChart()

    if hasattr(model, 'feature_importances_'):
        builtin_importance = model.feature_importances_
        importance_chart.add_importance(
            feature_names, builtin_importance,
            label='Built-in Importance', color='blue'
        )

    # Calculate permutation importance
    perm_importance = permutation_importance(
        model, X_test, y_test, n_repeats=10, random_state=42
    )

    importance_chart.add_importance(
        feature_names, perm_importance.importances_mean,
        errors=perm_importance.importances_std,
        label='Permutation Importance', color='red'
    )

    importance_chart.set_title('Feature Importance Analysis')
    importance_chart.set_xlabel('Importance Score')
    importance_chart.legend()

    return importance_chart

# Analyze feature importance
feature_names = [f'Feature_{i}' for i in range(X.shape[1])]
rf_model = models['Random Forest']
importance_chart = analyze_feature_importance(
    rf_model, X_train, X_test, y_test, feature_names
)
importance_chart.show()
```

### Feature Correlation Analysis

```python
import pandas as pd

# Create feature correlation heatmap with clustering
def plot_feature_correlations(X, feature_names):
    """Plot feature correlations with hierarchical clustering"""

    df = pd.DataFrame(X, columns=feature_names)
    corr_matrix = df.corr()

    # Create clustered heatmap
    corr_chart = vc.charts.ClusteredHeatmapChart()
    corr_chart.plot(corr_matrix,
                    method='ward',  # Clustering method
                    cmap='RdBu_r',
                    center=0,
                    annot=False,  # Too crowded with many features
                    square=True,
                    cbar_kws={'label': 'Correlation Coefficient'})

    corr_chart.set_title('Feature Correlation Matrix (Clustered)')

    # Add dendrograms
    corr_chart.show_dendrograms(True)

    return corr_chart

correlation_chart = plot_feature_correlations(X, feature_names)
correlation_chart.show()
```

## Model Explainability with SHAP

### SHAP Waterfall Charts

```python
import shap

# SHAP analysis for model explainability
def create_shap_analysis(model, X_train, X_test, instance_idx=0):
    """Create comprehensive SHAP analysis"""

    # Initialize SHAP explainer
    explainer = shap.TreeExplainer(model)  # For tree-based models
    shap_values = explainer.shap_values(X_test)

    # SHAP waterfall chart for single prediction
    waterfall_chart = vc.charts.SHAPWaterfallChart()
    waterfall_chart.plot(
        shap_values[1][instance_idx],  # Class 1 SHAP values
        X_test[instance_idx],
        feature_names=feature_names,
        max_display=10
    )

    waterfall_chart.set_title(f'SHAP Explanation - Instance {instance_idx}')

    return waterfall_chart, shap_values

# Create SHAP waterfall chart
shap_chart, shap_vals = create_shap_analysis(rf_model, X_train, X_test, instance_idx=0)
shap_chart.show()
```

### SHAP Summary Plots

```python
# SHAP summary plot showing feature importance and effects
def create_shap_summary(shap_values, X_test, feature_names, class_names):
    """Create SHAP summary visualization"""

    summary_chart = vc.charts.SHAPSummaryChart()

    # For binary classification, use class 1 SHAP values
    if len(shap_values) == 2:
        shap_data = shap_values[1]
        class_label = class_names[1]
    else:
        shap_data = shap_values
        class_label = "Target"

    summary_chart.plot(
        shap_data, X_test,
        feature_names=feature_names,
        max_display=15,
        plot_type='dot'  # or 'violin', 'bar'
    )

    summary_chart.set_title(f'SHAP Summary - {class_label}')

    return summary_chart

# Create SHAP summary
summary_chart = create_shap_summary(
    shap_vals, X_test, feature_names, ['Class 0', 'Class 1']
)
summary_chart.show()
```

### SHAP Dependence Plots

```python
# SHAP partial dependence plots
def create_shap_dependence_plots(shap_values, X_test, feature_names, top_features=5):
    """Create SHAP dependence plots for top features"""

    # Get feature importance from SHAP values
    feature_importance = np.abs(shap_values[1]).mean(0)
    top_feature_indices = np.argsort(feature_importance)[-top_features:]

    dependence_charts = []

    for i, feature_idx in enumerate(top_feature_indices):
        dependence_chart = vc.charts.SHAPDependenceChart()

        dependence_chart.plot(
            shap_values[1][:, feature_idx],
            X_test[:, feature_idx],
            feature_name=feature_names[feature_idx],
            interaction_feature=X_test,  # Auto-select interaction feature
            alpha=0.6
        )

        dependence_chart.set_title(f'SHAP Dependence - {feature_names[feature_idx]}')
        dependence_charts.append(dependence_chart)

    return dependence_charts

# Create dependence plots
dependence_charts = create_shap_dependence_plots(
    shap_vals, X_test, feature_names, top_features=3
)

for chart in dependence_charts:
    chart.show()
```

## Training Diagnostics

### Learning Curves

```python
from sklearn.model_selection import learning_curve

def plot_learning_curves(model, X, y, cv=5):
    """Plot learning curves to diagnose overfitting"""

    train_sizes, train_scores, val_scores = learning_curve(
        model, X, y, cv=cv, n_jobs=-1,
        train_sizes=np.linspace(0.1, 1.0, 10),
        scoring='accuracy'
    )

    # Calculate means and standard deviations
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    val_mean = np.mean(val_scores, axis=1)
    val_std = np.std(val_scores, axis=1)

    # Create learning curve chart
    learning_chart = vc.LineChart()

    # Training scores
    learning_chart.plot(train_sizes, train_mean,
                       label='Training Score',
                       color='blue', linewidth=2)
    learning_chart.fill_between(train_sizes,
                               train_mean - train_std,
                               train_mean + train_std,
                               alpha=0.3, color='blue')

    # Validation scores
    learning_chart.plot(train_sizes, val_mean,
                       label='Validation Score',
                       color='red', linewidth=2)
    learning_chart.fill_between(train_sizes,
                               val_mean - val_std,
                               val_mean + val_std,
                               alpha=0.3, color='red')

    learning_chart.set_title('Learning Curves')
    learning_chart.set_xlabel('Training Set Size')
    learning_chart.set_ylabel('Accuracy Score')
    learning_chart.legend()
    learning_chart.grid(True, alpha=0.3)

    # Add interpretation
    final_gap = train_mean[-1] - val_mean[-1]
    if final_gap > 0.05:
        learning_chart.add_text(0.6, 0.2, 'Possible Overfitting',
                               transform='axes', fontsize=12,
                               bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow"))

    return learning_chart

# Plot learning curves for Random Forest
learning_chart = plot_learning_curves(rf_model, X, y)
learning_chart.show()
```

### Validation Curves

```python
from sklearn.model_selection import validation_curve

def plot_validation_curve(model, X, y, param_name, param_range, cv=5):
    """Plot validation curve for hyperparameter tuning"""

    train_scores, val_scores = validation_curve(
        model, X, y, param_name=param_name,
        param_range=param_range, cv=cv, n_jobs=-1
    )

    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    val_mean = np.mean(val_scores, axis=1)
    val_std = np.std(val_scores, axis=1)

    # Create validation curve chart
    val_chart = vc.LineChart()

    val_chart.plot(param_range, train_mean,
                   label='Training Score',
                   color='blue', marker='o')
    val_chart.fill_between(param_range,
                          train_mean - train_std,
                          train_mean + train_std,
                          alpha=0.3, color='blue')

    val_chart.plot(param_range, val_mean,
                   label='Validation Score',
                   color='red', marker='s')
    val_chart.fill_between(param_range,
                          val_mean - val_std,
                          val_mean + val_std,
                          alpha=0.3, color='red')

    val_chart.set_title(f'Validation Curve - {param_name}')
    val_chart.set_xlabel(param_name)
    val_chart.set_ylabel('Score')
    val_chart.legend()
    val_chart.grid(True, alpha=0.3)

    # Highlight optimal parameter
    best_param_idx = np.argmax(val_mean)
    best_param = param_range[best_param_idx]
    val_chart.axvline(best_param, color='green', linestyle='--',
                     label=f'Optimal: {best_param}')

    return val_chart

# Plot validation curve for n_estimators
param_range = [10, 50, 100, 200, 500]
val_chart = plot_validation_curve(
    RandomForestClassifier(random_state=42),
    X, y, 'n_estimators', param_range
)
val_chart.show()
```

## Advanced ML Visualizations

### t-SNE and UMAP for Dimensionality Reduction

```python
from sklearn.manifold import TSNE
import umap

def create_dimensionality_reduction_comparison(X, y, feature_names):
    """Compare t-SNE and UMAP for dimensionality reduction"""

    # Apply t-SNE
    tsne = TSNE(n_components=2, random_state=42, perplexity=30)
    X_tsne = tsne.fit_transform(X)

    # Apply UMAP
    umap_reducer = umap.UMAP(n_components=2, random_state=42)
    X_umap = umap_reducer.fit_transform(X)

    # Create comparison plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # t-SNE plot
    tsne_chart = vc.ScatterChart(ax=ax1)
    tsne_chart.plot(X_tsne[:, 0], X_tsne[:, 1],
                    c=y, cmap='viridis', alpha=0.6, s=30)
    tsne_chart.set_title('t-SNE Visualization')
    tsne_chart.set_xlabel('t-SNE 1')
    tsne_chart.set_ylabel('t-SNE 2')

    # UMAP plot
    umap_chart = vc.ScatterChart(ax=ax2)
    umap_chart.plot(X_umap[:, 0], X_umap[:, 1],
                    c=y, cmap='viridis', alpha=0.6, s=30)
    umap_chart.set_title('UMAP Visualization')
    umap_chart.set_xlabel('UMAP 1')
    umap_chart.set_ylabel('UMAP 2')

    plt.tight_layout()
    plt.show()

    return X_tsne, X_umap

# Create dimensionality reduction visualization
X_tsne, X_umap = create_dimensionality_reduction_comparison(X, y, feature_names)
```

### Model Comparison Dashboard

```python
def create_model_comparison_dashboard(models, X_test, y_test):
    """Create comprehensive model comparison dashboard"""

    metrics = {}
    for name, model in models.items():
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None

        # Calculate metrics
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
        metrics[name] = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'f1': f1_score(y_test, y_pred)
        }

        if y_proba is not None:
            metrics[name]['auc'] = roc_auc_score(y_test, y_proba)

    # Create radar chart for model comparison
    radar_chart = vc.charts.RadarChart()

    metric_names = list(metrics[list(models.keys())[0]].keys())
    for model_name in models.keys():
        values = [metrics[model_name][metric] for metric in metric_names]
        radar_chart.add_data(values, label=model_name)

    radar_chart.set_labels(metric_names)
    radar_chart.set_title('Model Performance Comparison')
    radar_chart.legend()

    # Create metrics comparison bar chart
    metrics_df = pd.DataFrame(metrics).T
    metrics_chart = vc.BarChart()

    x = np.arange(len(models))
    width = 0.15

    for i, metric in enumerate(metric_names):
        metrics_chart.plot(x + i*width, metrics_df[metric],
                          width, label=metric.title())

    metrics_chart.set_xlabel('Models')
    metrics_chart.set_ylabel('Score')
    metrics_chart.set_title('Detailed Metrics Comparison')
    metrics_chart.set_xticks(x + width * 2)
    metrics_chart.set_xticklabels(models.keys())
    metrics_chart.legend()

    radar_chart.show()
    metrics_chart.show()

    return metrics

# Create model comparison dashboard
comparison_metrics = create_model_comparison_dashboard(models, X_test, y_test)
```

## Time Series ML Visualizations

### Forecasting Model Diagnostics

```python
def plot_forecasting_diagnostics(y_true, y_pred, dates, model_name):
    """Comprehensive forecasting model diagnostics"""

    # Main prediction vs actual plot
    forecast_chart = vc.LineChart()
    forecast_chart.plot(dates, y_true, label='Actual', color='blue', linewidth=2)
    forecast_chart.plot(dates, y_pred, label='Predicted', color='red', linewidth=2, linestyle='--')

    forecast_chart.set_title(f'Forecast vs Actual - {model_name}')
    forecast_chart.set_xlabel('Date')
    forecast_chart.set_ylabel('Value')
    forecast_chart.legend()
    forecast_chart.grid(True, alpha=0.3)

    # Residual analysis
    residuals = y_true - y_pred
    residual_chart = vc.ScatterChart()
    residual_chart.plot(y_pred, residuals, alpha=0.6, s=30)
    residual_chart.axhline(y=0, color='red', linestyle='--', alpha=0.8)

    residual_chart.set_title('Residual Plot')
    residual_chart.set_xlabel('Predicted Values')
    residual_chart.set_ylabel('Residuals')
    residual_chart.grid(True, alpha=0.3)

    # Residual distribution
    residual_dist = vc.HistogramChart()
    residual_dist.plot(residuals, bins=30, alpha=0.7, density=True)
    residual_dist.set_title('Residual Distribution')
    residual_dist.set_xlabel('Residual Value')
    residual_dist.set_ylabel('Density')

    # Add normal distribution overlay
    from scipy.stats import norm
    x = np.linspace(residuals.min(), residuals.max(), 100)
    residual_dist.plot(x, norm.pdf(x, residuals.mean(), residuals.std()),
                      color='red', linewidth=2, label='Normal Fit')
    residual_dist.legend()

    forecast_chart.show()
    residual_chart.show()
    residual_dist.show()

    # Calculate and display metrics
    from sklearn.metrics import mean_squared_error, mean_absolute_error
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100

    print(f"{model_name} Metrics:")
    print(f"MSE: {mse:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"MAPE: {mape:.2f}%")

# Example usage with synthetic time series data
dates = pd.date_range('2020-01-01', periods=365, freq='D')
trend = np.linspace(100, 200, 365)
seasonal = 10 * np.sin(2 * np.pi * np.arange(365) / 365.25 * 4)  # Quarterly pattern
noise = np.random.normal(0, 5, 365)
y_true = trend + seasonal + noise

# Simulate predictions (with some error)
y_pred = y_true + np.random.normal(0, 3, 365)

plot_forecasting_diagnostics(y_true, y_pred, dates, 'Example Forecast Model')
```

## Best Practices for ML Visualizations

### 1. Comprehensive Model Evaluation

```python
class MLVisualizationSuite:
    """Comprehensive ML visualization suite"""

    def __init__(self, model, X_train, X_test, y_train, y_test, feature_names=None):
        self.model = model
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.feature_names = feature_names or [f'feature_{i}' for i in range(X_train.shape[1])]

    def full_evaluation(self):
        """Run complete evaluation suite"""

        print("Running comprehensive ML evaluation...")

        # 1. Performance metrics
        self._plot_performance_metrics()

        # 2. Feature analysis
        self._plot_feature_analysis()

        # 3. Model explainability
        self._plot_explainability()

        # 4. Training diagnostics
        self._plot_training_diagnostics()

        print("Evaluation complete!")

    def _plot_performance_metrics(self):
        """Plot performance metrics"""
        # ROC, Precision-Recall, Confusion Matrix
        pass  # Implementation as shown above

    def _plot_feature_analysis(self):
        """Plot feature analysis"""
        # Feature importance, correlations
        pass  # Implementation as shown above

    def _plot_explainability(self):
        """Plot model explainability"""
        # SHAP analysis
        pass  # Implementation as shown above

    def _plot_training_diagnostics(self):
        """Plot training diagnostics"""
        # Learning curves, validation curves
        pass  # Implementation as shown above

# Usage
ml_viz = MLVisualizationSuite(rf_model, X_train, X_test, y_train, y_test, feature_names)
ml_viz.full_evaluation()
```

### 2. Interactive ML Dashboard

```python
def create_interactive_ml_dashboard(models, X_test, y_test, feature_names):
    """Create interactive ML dashboard with widgets"""

    # Use AI to recommend best visualizations
    viz_recommendations = vc.ai.recommend_ml_visualizations(
        models=models,
        X_test=X_test,
        y_test=y_test,
        task_type='classification'
    )

    dashboard_charts = []
    for rec in viz_recommendations:
        chart = vc.ai.create(rec.description, data={
            'X_test': X_test,
            'y_test': y_test,
            'models': models
        })
        dashboard_charts.append(chart)

    # Create interactive dashboard
    dashboard = vc.enterprise.create_dashboard(
        charts=dashboard_charts,
        title="ML Model Analysis Dashboard",
        interactive=True,
        export_options=['pdf', 'html', 'pptx']
    )

    return dashboard

# Create interactive dashboard
dashboard = create_interactive_ml_dashboard(models, X_test, y_test, feature_names)
dashboard.show()
```

---

VizlyChart's ML visualization capabilities provide comprehensive tools for understanding, debugging, and communicating machine learning model insights. These visualizations help data scientists make informed decisions about model selection, feature engineering, and deployment strategies.