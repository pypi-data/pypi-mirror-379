# Basic Concepts

Understanding VizlyChart's core concepts will help you use the library effectively and take advantage of its advanced features.

## Architecture Overview

VizlyChart is built around several key components that work together to provide a powerful visualization experience:

```
VizlyChart
├── Core Charts          # Traditional chart types
├── AI Module           # Natural language processing
├── Backend System      # Rendering engines
├── Enterprise Tools    # Professional features
└── Advanced Charts     # ML and statistical visualizations
```

## Core Components

### 1. Charts

Charts are the fundamental building blocks of VizlyChart. Each chart type is designed for specific data visualization needs:

```python
import vizlychart as vc

# Basic chart types
line_chart = vc.LineChart()      # Time series, trends
scatter_chart = vc.ScatterChart()  # Correlations, distributions
bar_chart = vc.BarChart()        # Categories, comparisons
heatmap = vc.HeatmapChart()      # 2D data, correlations
```

### 2. Backends

VizlyChart uses a unified API that works with multiple rendering engines:

- **Matplotlib**: High-quality static charts, perfect for publications
- **Plotly**: Interactive web charts with zoom, pan, and hover
- **Pure Python**: Lightweight rendering without external dependencies

```python
# Switch backends seamlessly
vc.set_backend('matplotlib')  # Static, high-quality
chart = vc.LineChart()

vc.set_backend('plotly')     # Interactive
chart = vc.LineChart()       # Same API, different output
```

### 3. AI Module

The AI module provides intelligent features that make chart creation effortless:

```python
# Natural language chart creation
chart = vc.ai.create("scatter plot of price vs sales with trend line")

# Smart recommendations
rec = vc.recommend_chart(data, intent='show_distribution')

# Intelligent styling
vc.style_chart(chart, "modern dark theme with accent colors")
```

## Key Concepts

### Chart Lifecycle

Every VizlyChart follows a consistent lifecycle:

1. **Creation** - Instantiate a chart object
2. **Data Binding** - Add data to the chart
3. **Styling** - Apply visual customization
4. **Display/Export** - Show or save the chart

```python
# 1. Create
chart = vc.LineChart()

# 2. Add data
chart.plot(x_data, y_data, label="My Data")

# 3. Style
chart.set_title("My Chart")
chart.set_xlabel("X Axis")
chart.set_ylabel("Y Axis")

# 4. Display
chart.show()
```

### Data Compatibility

VizlyChart works with all common Python data structures:

```python
import numpy as np
import pandas as pd

# NumPy arrays
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Pandas DataFrames
df = pd.DataFrame({'x': x, 'y': y})

# Python lists
x_list = [1, 2, 3, 4, 5]
y_list = [2, 4, 6, 8, 10]

# All work the same way
chart = vc.LineChart()
chart.plot(x, y)  # or df['x'], df['y'] or x_list, y_list
```

### Theme System

VizlyChart uses a powerful theming system that controls all visual aspects:

```python
# Apply built-in themes
vc.set_theme('professional')  # Clean, business-ready
vc.set_theme('scientific')    # Academic publications
vc.set_theme('modern')        # Contemporary design

# Create custom themes
theme = vc.Theme(
    background_color='white',
    grid_color='#E0E0E0',
    text_color='#333333',
    accent_colors=['#1f77b4', '#ff7f0e', '#2ca02c']
)
vc.set_theme(theme)
```

## Advanced Concepts

### Backend Independence

One of VizlyChart's unique features is backend independence. Your code remains the same regardless of the rendering engine:

```python
def create_analysis_chart(data):
    """This function works with any backend"""
    chart = vc.LineChart()
    chart.plot(data['x'], data['y'])
    chart.set_title("Analysis Results")
    return chart

# Use with different backends
vc.set_backend('matplotlib')
chart1 = create_analysis_chart(data)  # Static PNG
chart1.save("static.png")

vc.set_backend('plotly')
chart2 = create_analysis_chart(data)  # Interactive HTML
chart2.save("interactive.html")
```

### AI Integration

VizlyChart's AI features are designed to augment, not replace, your visualization decisions:

```python
# Get AI suggestions but maintain control
recommendations = vc.analyze_data(data)

# Review recommendations
for rec in recommendations:
    print(f"Suggestion: {rec.chart_type}")
    print(f"Reason: {rec.reasoning}")
    print(f"Confidence: {rec.confidence}")

# Choose the best recommendation
best_rec = max(recommendations, key=lambda r: r.confidence)
chart = vc.create_chart(best_rec.chart_type)
```

### Enterprise Integration

VizlyChart is designed for enterprise environments:

```python
from vizlychart.enterprise import EnterpriseExporter, ComplianceTracker

# Apply corporate branding
branding = vc.load_branding("company_brand.json")
vc.set_branding(branding)

# Track chart usage for compliance
tracker = ComplianceTracker()
with tracker.track_chart_creation():
    chart = vc.LineChart()
    chart.plot(sensitive_data)

# Export with audit trail
exporter = EnterpriseExporter()
exporter.export_powerpoint(chart, "report.pptx", include_metadata=True)
```

## Chart Types Deep Dive

### Basic Charts

**Line Charts** - Perfect for continuous data and trends
```python
chart = vc.LineChart()
chart.plot(time, temperature, label="Temperature")
chart.plot(time, humidity, label="Humidity")
```

**Scatter Plots** - Ideal for correlations and distributions
```python
chart = vc.ScatterChart()
chart.plot(height, weight, s=age, c=gender)  # Size by age, color by gender
```

**Bar Charts** - Great for categories and comparisons
```python
chart = vc.BarChart()
chart.plot(categories, values, color='steelblue')
```

### Advanced Charts

**Heatmaps** - Show 2D data patterns
```python
chart = vc.HeatmapChart()
chart.plot(correlation_matrix, annot=True, cmap='coolwarm')
```

**Box Plots** - Statistical distributions
```python
chart = vc.BoxPlotChart()
chart.plot([group1_data, group2_data, group3_data], labels=['A', 'B', 'C'])
```

**Surface Plots** - 3D data visualization
```python
chart = vc.SurfaceChart()
chart.plot(x_grid, y_grid, z_values, alpha=0.8)
```

## Best Practices

### 1. Choose the Right Chart Type

```python
# Use AI recommendations when unsure
rec = vc.recommend_chart(data, intent='comparison')
chart = vc.create_chart(rec.chart_type)

# Or follow these guidelines:
# - Line charts: Time series, continuous data
# - Scatter plots: Correlations, distributions
# - Bar charts: Categories, discrete comparisons
# - Heatmaps: 2D relationships, correlation matrices
```

### 2. Optimize for Your Audience

```python
# For executives - simple, clear
vc.set_theme('executive')
chart = vc.BarChart()
chart.plot(quarters, revenue)
chart.set_title("Quarterly Revenue", fontsize=16)

# For researchers - detailed, precise
vc.set_theme('scientific')
chart = vc.ScatterChart()
chart.plot(x, y, s=10, alpha=0.6)
chart.add_trendline(method='linear')
chart.add_confidence_interval()
```

### 3. Use Consistent Styling

```python
# Define chart factory with consistent styling
class CompanyCharts:
    def __init__(self):
        vc.set_theme('company_theme')

    def revenue_chart(self, data):
        chart = vc.LineChart()
        chart.plot(data['date'], data['revenue'],
                   color='#1E40AF', linewidth=3)
        chart.set_title("Revenue Trend")
        return chart

    def performance_chart(self, data):
        chart = vc.BarChart()
        chart.plot(data['metric'], data['value'],
                   color='#1E40AF')
        chart.set_title("Performance Metrics")
        return chart
```

### 4. Handle Large Datasets

```python
# Automatic optimization for large data
if len(data) > 100000:
    # VizlyChart automatically optimizes
    chart = vc.ScatterChart(optimize_for_size=True)
    chart.plot(x, y, alpha=0.1)  # Reduce alpha for overplotting
else:
    chart = vc.ScatterChart()
    chart.plot(x, y)
```

## Common Patterns

### Interactive Analysis
```python
def explore_data(df):
    """Interactive data exploration pattern"""

    # Get AI recommendations
    suggestions = vc.analyze_dataframe(df)

    for i, suggestion in enumerate(suggestions):
        print(f"{i+1}. {suggestion.description}")

    choice = int(input("Select chart: ")) - 1
    selected = suggestions[choice]

    # Create recommended chart
    chart = vc.create_chart(selected.chart_type)
    chart.plot_dataframe(df, **selected.plot_kwargs)
    chart.show()

    return chart
```

### Batch Chart Generation
```python
def generate_report_charts(data_dict):
    """Generate multiple charts for reporting"""
    charts = {}

    vc.set_backend('matplotlib')  # High quality for reports
    vc.set_theme('professional')

    for name, data in data_dict.items():
        # Get AI recommendation
        rec = vc.recommend_chart(data)

        # Create chart
        chart = vc.create_chart(rec.chart_type)
        chart.plot(data)
        chart.set_title(f"{name.title()} Analysis")

        charts[name] = chart

    return charts
```

## Performance Considerations

### Backend Selection
- **Matplotlib**: Best for static, high-quality images
- **Plotly**: Best for interactive web applications
- **Pure Python**: Best for minimal dependencies, server environments

### Memory Management
```python
# For large datasets, use streaming
chart = vc.LineChart(streaming=True)
for batch in data_batches:
    chart.add_data(batch)

# Or use data reduction
chart = vc.ScatterChart()
chart.plot(x, y, max_points=10000)  # Automatically samples data
```

### Export Optimization
```python
# Optimize exports for different uses
chart.save("web_version.png", dpi=96)      # Web display
chart.save("print_version.png", dpi=300)   # Print quality
chart.save("presentation.png", dpi=150)    # Presentations
```

## Error Handling

VizlyChart provides helpful error messages and suggestions:

```python
try:
    chart = vc.LineChart()
    chart.plot(x, y)
    chart.show()
except vc.DataFormatError as e:
    print(f"Data issue: {e}")
    print("Suggestions:")
    for suggestion in e.suggestions:
        print(f"- {suggestion}")
except vc.BackendError as e:
    print(f"Backend issue: {e}")
    # Automatically try fallback backend
    vc.set_backend('matplotlib')  # Fallback
    chart.show()
```

## Next Steps

Now that you understand VizlyChart's concepts:

1. **Explore Chart Types**: [Complete chart reference](../features/chart-types.md)
2. **Try AI Features**: [Natural language visualization](../features/ai-features.md)
3. **Learn Enterprise Features**: [Professional exports and branding](../enterprise/exports.md)
4. **See Examples**: [Real-world use cases](../examples/index.md)

---

**Understanding these concepts will help you leverage VizlyChart's full power for your data visualization needs.**