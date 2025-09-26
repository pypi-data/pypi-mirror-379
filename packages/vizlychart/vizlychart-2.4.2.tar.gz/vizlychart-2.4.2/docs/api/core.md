# Core API Reference

This document covers the core VizlyChart API including chart classes, backend management, and fundamental functionality.

## Core Functions

### Chart Creation Functions

#### `create_chart(chart_type, **kwargs)`

Creates a chart of the specified type.

**Parameters:**
- `chart_type` (str): Type of chart to create ('line', 'scatter', 'bar', etc.)
- `**kwargs`: Additional arguments passed to the chart constructor

**Returns:**
- Chart object of the specified type

**Example:**
```python
import vizlychart as vc

# Create different chart types
line_chart = vc.create_chart('line')
scatter_chart = vc.create_chart('scatter', alpha=0.6)
bar_chart = vc.create_chart('bar', orientation='horizontal')
```

#### `recommend_chart(data, intent=None, **kwargs)`

Get AI-powered chart type recommendations based on your data.

**Parameters:**
- `data` (dict, DataFrame, array): Input data to analyze
- `intent` (str, optional): Analysis intent ('correlation', 'distribution', 'trend', etc.)
- `**kwargs`: Additional parameters for analysis

**Returns:**
- `ChartRecommendation`: Object containing chart type, confidence, and reasoning

**Example:**
```python
import vizlychart as vc
import numpy as np

# Sample data
data = {
    'x': np.random.randn(100),
    'y': np.random.randn(100)
}

# Get recommendation
rec = vc.recommend_chart(data, intent='correlation')
print(f"Recommended: {rec.chart_type}")
print(f"Confidence: {rec.confidence:.0%}")
print(f"Reasoning: {rec.reasoning}")

# Create recommended chart
chart = vc.create_chart(rec.chart_type)
```

### Backend Management

#### `set_backend(backend_name)`

Switch the rendering backend.

**Parameters:**
- `backend_name` (str): Backend to use ('matplotlib', 'plotly', 'pure')

**Returns:**
- `bool`: True if backend was set successfully

**Example:**
```python
# Switch to different backends
vc.set_backend('matplotlib')  # High-quality static images
vc.set_backend('plotly')      # Interactive web charts
vc.set_backend('pure')        # Pure Python rendering
```

#### `get_backend()`

Get the currently active backend.

**Returns:**
- `str`: Name of the current backend

#### `list_backends()`

List all available backends.

**Returns:**
- `list`: List of available backend names

**Example:**
```python
# Check available backends
backends = vc.list_backends()
print(f"Available: {backends}")

# Check current backend
current = vc.get_backend()
print(f"Current: {current}")
```

### Theme Management

#### `set_theme(theme)`

Set the global theme for all charts.

**Parameters:**
- `theme` (str or Theme): Built-in theme name or custom Theme object

**Available Themes:**
- `'default'`: Standard VizlyChart theme
- `'professional'`: Clean, business-ready styling
- `'scientific'`: Academic publication styling
- `'modern'`: Contemporary design
- `'dark'`: Dark mode theme
- `'minimal'`: Minimalist styling

**Example:**
```python
# Use built-in themes
vc.set_theme('professional')
vc.set_theme('scientific')
vc.set_theme('dark')

# Create custom theme
theme = vc.Theme(
    background_color='white',
    grid_color='#E0E0E0',
    text_color='#333333',
    accent_colors=['#1f77b4', '#ff7f0e', '#2ca02c']
)
vc.set_theme(theme)
```

#### `get_theme()`

Get the current theme.

**Returns:**
- `Theme`: Current theme object

## Base Chart Class

All VizlyChart chart types inherit from the `BaseChart` class.

### `BaseChart`

Base class for all chart types.

#### Methods

##### `plot(*args, **kwargs)`

Add data to the chart. Specific parameters vary by chart type.

**Common Parameters:**
- `label` (str): Legend label for the data series
- `color` (str): Color for the data series
- `alpha` (float): Transparency (0-1)
- `linewidth` (float): Width of lines (for line charts)
- `marker` (str): Marker style (for scatter/line charts)

##### `set_title(title, **kwargs)`

Set the chart title.

**Parameters:**
- `title` (str): Chart title
- `**kwargs`: Additional styling parameters (fontsize, fontweight, color)

##### `set_xlabel(label, **kwargs)`

Set the x-axis label.

**Parameters:**
- `label` (str): X-axis label
- `**kwargs`: Additional styling parameters

##### `set_ylabel(label, **kwargs)`

Set the y-axis label.

**Parameters:**
- `label` (str): Y-axis label
- `**kwargs`: Additional styling parameters

##### `legend(**kwargs)`

Add a legend to the chart.

**Parameters:**
- `**kwargs`: Legend styling parameters (loc, fontsize, frameon)

##### `grid(enable=True, **kwargs)`

Show or hide grid lines.

**Parameters:**
- `enable` (bool): Whether to show grid
- `**kwargs`: Grid styling parameters (alpha, color, linestyle)

##### `set_xlim(left=None, right=None)`

Set x-axis limits.

**Parameters:**
- `left` (float): Left limit
- `right` (float): Right limit

##### `set_ylim(bottom=None, top=None)`

Set y-axis limits.

**Parameters:**
- `bottom` (float): Bottom limit
- `top` (float): Top limit

##### `show(**kwargs)`

Display the chart.

**Parameters:**
- `**kwargs`: Display parameters (varies by backend)

##### `save(filename, **kwargs)`

Save the chart to a file.

**Parameters:**
- `filename` (str): Output filename
- `**kwargs`: Save parameters (dpi, width, height, format)

**Example:**
```python
# Common chart operations
chart = vc.LineChart()
chart.plot(x, y, label="Data", color="blue", linewidth=2)
chart.set_title("My Chart", fontsize=16)
chart.set_xlabel("X Values")
chart.set_ylabel("Y Values")
chart.legend()
chart.grid(True, alpha=0.3)
chart.show()
```

## Specific Chart Types

### `LineChart`

Line chart for continuous data and trends.

#### `plot(x, y, **kwargs)`

Plot line data.

**Parameters:**
- `x` (array-like): X-axis data
- `y` (array-like): Y-axis data
- `label` (str): Series label
- `color` (str): Line color
- `linewidth` (float): Line width
- `linestyle` (str): Line style ('-', '--', '-.', ':')
- `marker` (str): Marker style ('o', 's', '^', etc.)
- `markersize` (float): Marker size

**Example:**
```python
import vizlychart as vc
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

chart = vc.LineChart()
chart.plot(x, y1, label="sin(x)", color="blue", linewidth=2)
chart.plot(x, y2, label="cos(x)", color="red", linestyle="--")
chart.legend()
chart.show()
```

### `ScatterChart`

Scatter plot for correlations and distributions.

#### `plot(x, y, **kwargs)`

Plot scatter data.

**Parameters:**
- `x` (array-like): X-axis data
- `y` (array-like): Y-axis data
- `s` (float or array-like): Marker sizes
- `c` (color or array-like): Marker colors
- `alpha` (float): Transparency
- `marker` (str): Marker style
- `edgecolors` (str): Marker edge colors

**Example:**
```python
import numpy as np

# Generate sample data
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)
sizes = np.random.randint(20, 200, 100)
colors = np.random.rand(100)

chart = vc.ScatterChart()
chart.plot(x, y, s=sizes, c=colors, alpha=0.6, edgecolors='black')
chart.set_xlabel("X Variable")
chart.set_ylabel("Y Variable")
chart.show()
```

### `BarChart`

Bar chart for categorical data and comparisons.

#### `plot(x, y, **kwargs)`

Plot bar data.

**Parameters:**
- `x` (array-like): Category labels or positions
- `y` (array-like): Bar heights
- `width` (float): Bar width
- `color` (str or array-like): Bar colors
- `alpha` (float): Transparency
- `orientation` (str): 'vertical' or 'horizontal'

**Example:**
```python
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
colors = ['red', 'blue', 'green', 'orange', 'purple']

chart = vc.BarChart()
chart.plot(categories, values, color=colors, alpha=0.8)
chart.set_xlabel("Categories")
chart.set_ylabel("Values")
chart.show()
```

### `HeatmapChart`

Heatmap for 2D data visualization.

#### `plot(data, **kwargs)`

Plot heatmap data.

**Parameters:**
- `data` (2D array): Data matrix to visualize
- `cmap` (str): Colormap name
- `annot` (bool): Whether to annotate cells with values
- `fmt` (str): Annotation format string
- `cbar` (bool): Whether to show colorbar

**Example:**
```python
import numpy as np

# Create correlation matrix
data = np.random.randn(10, 12)
corr_matrix = np.corrcoef(data)

chart = vc.HeatmapChart()
chart.plot(corr_matrix,
           cmap='coolwarm',
           annot=True,
           fmt='.2f',
           cbar=True)
chart.set_title("Correlation Matrix")
chart.show()
```

## Utility Classes

### `ChartRecommendation`

Result object from `recommend_chart()` function.

#### Attributes
- `chart_type` (str): Recommended chart type
- `confidence` (float): Confidence score (0-1)
- `reasoning` (str): Explanation for recommendation
- `parameters` (dict): Suggested chart parameters

### `Theme`

Theme configuration object.

#### Parameters
- `background_color` (str): Chart background color
- `grid_color` (str): Grid line color
- `text_color` (str): Text color
- `accent_colors` (list): List of accent colors for data series
- `font_family` (str): Font family name
- `font_size` (int): Default font size

**Example:**
```python
# Create custom theme
theme = vc.Theme(
    background_color='#F5F5F5',
    grid_color='#CCCCCC',
    text_color='#333333',
    accent_colors=['#2E86AB', '#A23B72', '#F18F01', '#C73E1D'],
    font_family='Arial',
    font_size=12
)

# Apply theme
vc.set_theme(theme)
```

## Error Handling

VizlyChart provides specific exception types for different error conditions:

### `VizlyChartError`

Base exception class for all VizlyChart errors.

### `DataFormatError`

Raised when data format is invalid or incompatible.

**Attributes:**
- `suggestions` (list): List of suggested fixes

### `BackendError`

Raised when backend-related issues occur.

### `ThemeError`

Raised when theme-related issues occur.

**Example:**
```python
try:
    chart = vc.LineChart()
    chart.plot(invalid_data)
except vc.DataFormatError as e:
    print(f"Data error: {e}")
    for suggestion in e.suggestions:
        print(f"Try: {suggestion}")
except vc.BackendError as e:
    print(f"Backend error: {e}")
    # Try fallback backend
    vc.set_backend('matplotlib')
```

## Configuration

### Global Settings

You can configure VizlyChart behavior globally:

```python
# Set default figure size
vc.config.set('figure.figsize', (10, 6))

# Set default DPI for saves
vc.config.set('savefig.dpi', 300)

# Set default backend
vc.config.set('backend', 'matplotlib')

# Enable/disable AI features
vc.config.set('ai.enabled', True)
```

### Environment Variables

VizlyChart respects these environment variables:

- `VIZLYCHART_BACKEND`: Default backend to use
- `VIZLYCHART_THEME`: Default theme to apply
- `VIZLYCHART_CONFIG`: Path to configuration file

## Performance Tips

### Large Datasets
```python
# Use data reduction for large datasets
chart = vc.ScatterChart()
chart.plot(x, y, max_points=10000)  # Automatically samples

# Or use streaming for real-time data
chart = vc.LineChart(streaming=True)
for batch in data_batches:
    chart.add_data(batch)
```

### Memory Management
```python
# Clear chart data after saving
chart.save("output.png")
chart.clear()  # Free memory

# Use context manager for automatic cleanup
with vc.LineChart() as chart:
    chart.plot(x, y)
    chart.save("output.png")
# Chart automatically cleaned up
```

---

This covers the core VizlyChart API. For more specific functionality, see:

- [Chart-Specific APIs](charts.md)
- [AI Module API](ai.md)
- [Enterprise API](enterprise.md)
- [Advanced Features](../advanced/)