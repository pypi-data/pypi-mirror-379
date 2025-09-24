# Quick Start Tutorial

Welcome to VizlyChart! This tutorial will help you create your first chart in just a few minutes. By the end, you'll understand the basics of VizlyChart and be ready to create stunning visualizations.

## Your First Chart

Let's start with a simple line chart:

```python
import vizlychart as vc
import numpy as np

# Create sample data
x = np.linspace(0, 10, 50)
y = np.sin(x)

# Create and display chart
chart = vc.LineChart()
chart.plot(x, y, label="Sine Wave")
chart.set_title("My First VizlyChart")
chart.set_xlabel("X Values")
chart.set_ylabel("Y Values")
chart.show()
```

That's it! You've created your first VizlyChart visualization.

## Basic Chart Types

VizlyChart supports many chart types. Here are the most common ones:

### Line Chart
```python
import vizlychart as vc
import numpy as np

# Sample data
x = np.arange(10)
y1 = np.random.randn(10).cumsum()
y2 = np.random.randn(10).cumsum()

# Create line chart
chart = vc.LineChart()
chart.plot(x, y1, label="Series 1", color="blue")
chart.plot(x, y2, label="Series 2", color="red")
chart.set_title("Multi-Series Line Chart")
chart.legend()
chart.show()
```

### Scatter Plot
```python
# Generate random data
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)

# Create scatter plot
chart = vc.ScatterChart()
chart.plot(x, y, alpha=0.6, s=50)
chart.set_title("Scatter Plot Example")
chart.set_xlabel("X Variable")
chart.set_ylabel("Y Variable")
chart.show()
```

### Bar Chart
```python
# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

# Create bar chart
chart = vc.BarChart()
chart.plot(categories, values, color='steelblue')
chart.set_title("Bar Chart Example")
chart.set_xlabel("Categories")
chart.set_ylabel("Values")
chart.show()
```

## AI-Powered Features

One of VizlyChart's unique features is AI-powered chart generation:

### Natural Language Chart Creation
```python
import vizlychart as vc

# Create charts from text descriptions
chart = vc.ai.create("line chart showing temperature over time")

# Or with your own data
data = {
    'temperature': [20, 22, 25, 23, 21, 24, 26],
    'time': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
}
chart = vc.ai.create("bar chart of temperature by day", data=data)
chart.show()
```

### Smart Chart Recommendations
```python
# Get AI recommendations for your data
data = {
    'sales': [100, 120, 140, 110, 160, 180, 200],
    'marketing_spend': [10, 15, 20, 12, 25, 30, 35]
}

# Ask for recommendations
rec = vc.recommend_chart(data, intent='correlation')
print(f"Recommended chart: {rec.chart_type}")
print(f"Confidence: {rec.confidence:.0%}")
print(f"Reasoning: {rec.reasoning}")

# Create the recommended chart
chart = vc.create_chart(rec.chart_type)
chart.plot(data['marketing_spend'], data['sales'])
chart.set_title("Sales vs Marketing Spend")
chart.show()
```

## Backend Switching

VizlyChart can use different rendering engines seamlessly:

```python
import vizlychart as vc

# List available backends
backends = vc.list_backends()
print(f"Available backends: {backends}")

# Use matplotlib for high-quality static images
vc.set_backend('matplotlib')
chart = vc.LineChart()
chart.plot([1, 2, 3, 4], [1, 4, 2, 3])
chart.save("static_chart.png")

# Switch to Plotly for interactive web charts
vc.set_backend('plotly')
chart = vc.LineChart()  # Same API!
chart.plot([1, 2, 3, 4], [1, 4, 2, 3])
chart.save("interactive_chart.html")
```

## Styling and Theming

### Basic Styling
```python
# Create a styled chart
chart = vc.LineChart()
chart.plot(x, y,
          color='#2E86AB',
          linewidth=3,
          linestyle='--',
          marker='o',
          markersize=8,
          alpha=0.8)

# Customize appearance
chart.set_title("Styled Line Chart", fontsize=16, fontweight='bold')
chart.set_xlabel("X Axis", fontsize=12)
chart.set_ylabel("Y Axis", fontsize=12)
chart.grid(True, alpha=0.3)
chart.show()
```

### AI-Powered Styling
```python
# Apply styling with natural language
chart = vc.LineChart()
chart.plot(x, y)

# Use AI to apply professional styling
vc.style_chart(chart, "professional blue theme with bold fonts")
chart.show()

# Or try different styles
vc.style_chart(chart, "elegant pastel colors with shadows")
chart.show()
```

## Working with Data

VizlyChart works with various data formats:

### NumPy Arrays
```python
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

chart = vc.LineChart()
chart.plot(x, y)
chart.show()
```

### Pandas DataFrames
```python
import pandas as pd

# Create sample DataFrame
df = pd.DataFrame({
    'x': range(10),
    'y1': np.random.randn(10).cumsum(),
    'y2': np.random.randn(10).cumsum()
})

# Plot directly from DataFrame
chart = vc.LineChart()
chart.plot(df['x'], df['y1'], label='Series 1')
chart.plot(df['x'], df['y2'], label='Series 2')
chart.legend()
chart.show()
```

### Python Lists
```python
# Simple Python lists work too
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 1, 5, 3]

chart = vc.BarChart()
chart.plot(x_values, y_values)
chart.show()
```

## Saving Charts

VizlyChart supports multiple export formats:

```python
chart = vc.LineChart()
chart.plot(x, y)
chart.set_title("Export Example")

# Save in different formats
chart.save("chart.png")        # PNG image
chart.save("chart.svg")        # Vector graphics
chart.save("chart.pdf")        # PDF document
chart.save("chart.html")       # Interactive web page

# High-resolution for publications
chart.save("chart_hires.png", dpi=300, width=10, height=6)
```

## Interactive Features

### Adding Interactivity
```python
# Enable zoom and pan
chart = vc.ScatterChart()
chart.plot(x, y)
chart.enable_zoom()
chart.enable_pan()
chart.show()

# Add hover information
chart.add_hover_data(['X: {:.2f}', 'Y: {:.2f}'])
```

### Jupyter Notebook Integration
```python
# In Jupyter notebooks, charts display automatically
import vizlychart as vc

# Enable inline plotting
%matplotlib inline

# Charts will display directly in cells
chart = vc.LineChart()
chart.plot(x, y)
chart.show()  # Displays inline
```

## Next Steps

Now that you know the basics, explore these advanced features:

### 🤖 AI Features
- [Natural Language Chart Generation](../features/ai-features.md)
- [Smart Chart Recommendations](../features/ai-features.md#smart-recommendations)
- [Intelligent Styling](../features/ai-features.md#natural-language-styling)

### 🏢 Enterprise Features
- [Professional Exports](../enterprise/exports.md) (PowerPoint, Excel)
- [Corporate Branding](../enterprise/theming.md)
- [Compliance Tools](../enterprise/compliance.md)

### 🧠 Advanced Visualizations
- [Machine Learning Charts](../advanced/ml-charts.md)
- [Causal Inference](../advanced/causal.md)
- [Statistical Analysis](../advanced/statistical.md)

### 📚 Learning Resources
- [Complete Examples](../examples/index.md)
- [Best Practices](../examples/best-practices.md)
- [API Reference](../api/core.md)

## Common Patterns

Here are some patterns you'll use frequently:

### Quick Analysis Chart
```python
def quick_plot(x, y, title="Quick Plot"):
    """Create a quick analysis chart"""
    chart = vc.LineChart() if len(x) > 20 else vc.ScatterChart()
    chart.plot(x, y)
    chart.set_title(title)
    return chart

# Usage
chart = quick_plot(time_data, value_data, "Performance Over Time")
chart.show()
```

### Comparison Charts
```python
def compare_series(data_dict, title="Comparison"):
    """Compare multiple data series"""
    chart = vc.LineChart()
    for label, (x, y) in data_dict.items():
        chart.plot(x, y, label=label)

    chart.set_title(title)
    chart.legend()
    return chart

# Usage
data = {
    'Actual': (dates, actual_values),
    'Predicted': (dates, predicted_values)
}
chart = compare_series(data, "Actual vs Predicted")
chart.show()
```

## Troubleshooting

### Common Issues

**Chart doesn't display**
```python
# Make sure to call show()
chart.show()

# In Jupyter, you might need:
import matplotlib.pyplot as plt
plt.show()
```

**Import errors**
```python
# Check installation
import vizlychart as vc
print(vc.__version__)

# Reinstall if needed
# !pip install --upgrade vizlychart
```

**Performance issues with large datasets**
```python
# Use sampling for exploration
if len(data) > 10000:
    sample_indices = np.random.choice(len(data), 5000, replace=False)
    data_sample = data[sample_indices]
    chart.plot(data_sample)
```

---

**Great job!** You've completed the quick start tutorial. You're now ready to create beautiful visualizations with VizlyChart.

**Next:** Learn more about [VizlyChart's concepts and architecture](concepts.md).