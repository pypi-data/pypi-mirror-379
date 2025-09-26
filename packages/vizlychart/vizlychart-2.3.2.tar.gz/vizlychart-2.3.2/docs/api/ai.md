# AI Module API Reference

VizlyChart's AI module provides intelligent chart generation, smart recommendations, and natural language styling capabilities. This document covers all AI-powered features and their APIs.

## Overview

The AI module consists of three main components:

- **Natural Language Processing**: Convert text descriptions to charts
- **Smart Selection**: Analyze data and recommend optimal chart types
- **Intelligent Styling**: Apply themes using natural language descriptions

```python
import vizlychart as vc
from vizlychart.ai import SmartChartSelector, NaturalLanguageStylist
```

## Natural Language Chart Generation

### `vc.ai.create(description, data=None, **kwargs)`

Generate charts from natural language descriptions.

**Parameters:**
- `description` (str): Natural language description of the desired chart
- `data` (dict, DataFrame, optional): Data to visualize
- `**kwargs`: Additional parameters for chart creation

**Returns:**
- Chart object based on the description

**Examples:**
```python
# Simple chart generation
chart = vc.ai.create("line chart showing temperature over time")

# With specific data
data = {
    'date': ['2023-01', '2023-02', '2023-03', '2023-04'],
    'revenue': [1000, 1200, 1100, 1300]
}
chart = vc.ai.create("bar chart of monthly revenue", data=data)

# Complex descriptions
chart = vc.ai.create(
    "scatter plot of price vs sales with trend line and correlation coefficient"
)
```

### `vc.ai.parse_description(description)`

Parse a natural language description and extract chart intent.

**Parameters:**
- `description` (str): Natural language description

**Returns:**
- `ChartIntent`: Object containing parsed intent details

**Attributes of ChartIntent:**
- `chart_type` (str): Detected chart type
- `variables` (list): Identified variables
- `styling` (dict): Styling preferences
- `analysis` (list): Requested analysis types

**Example:**
```python
intent = vc.ai.parse_description(
    "create a scatter plot of height vs weight with red dots and trend line"
)

print(f"Chart type: {intent.chart_type}")      # "scatter"
print(f"Variables: {intent.variables}")        # ["height", "weight"]
print(f"Styling: {intent.styling}")           # {"color": "red"}
print(f"Analysis: {intent.analysis}")         # ["trend_line"]
```

## Smart Chart Selection

### `vc.recommend_chart(data, intent=None, **kwargs)`

Get AI-powered chart type recommendations.

**Parameters:**
- `data` (dict, DataFrame, array): Data to analyze
- `intent` (str, optional): Analysis intent
- `**kwargs`: Additional analysis parameters

**Intent Options:**
- `'correlation'`: Show relationships between variables
- `'distribution'`: Show data distribution patterns
- `'trend'`: Show trends over time
- `'comparison'`: Compare categories or groups
- `'composition'`: Show parts of a whole
- `'ranking'`: Show relative rankings

**Returns:**
- `ChartRecommendation`: Primary recommendation
- Or list of recommendations if `return_all=True`

**Example:**
```python
import numpy as np

# Sample data
data = {
    'x': np.random.randn(100),
    'y': 2 * np.random.randn(100) + 0.5,
    'category': np.random.choice(['A', 'B', 'C'], 100)
}

# Get recommendation
rec = vc.recommend_chart(data, intent='correlation')
print(f"Recommended: {rec.chart_type}")
print(f"Confidence: {rec.confidence:.0%}")
print(f"Reasoning: {rec.reasoning}")

# Get multiple recommendations
recs = vc.recommend_chart(data, return_all=True)
for i, rec in enumerate(recs):
    print(f"{i+1}. {rec.chart_type} (confidence: {rec.confidence:.0%})")
```

### `SmartChartSelector`

Advanced chart selection with customizable analysis.

#### `SmartChartSelector(config=None)`

**Parameters:**
- `config` (dict, optional): Configuration for selection algorithm

#### Methods

##### `analyze_data(data, **kwargs)`

Perform detailed data analysis.

**Parameters:**
- `data`: Input data to analyze
- `**kwargs`: Analysis options

**Returns:**
- `DataProfile`: Detailed analysis results

**Example:**
```python
selector = SmartChartSelector()

# Analyze data characteristics
profile = selector.analyze_data(data)
print(f"Data type: {profile.data_type}")
print(f"Variables: {profile.variables}")
print(f"Relationships: {profile.relationships}")
print(f"Patterns: {profile.patterns}")
```

##### `recommend(data, intent=None, **kwargs)`

Generate chart recommendations.

**Parameters:**
- `data`: Input data
- `intent` (str, optional): Analysis intent
- `**kwargs`: Additional parameters

**Returns:**
- `ChartRecommendation` or list of recommendations

##### `explain_recommendation(recommendation)`

Get detailed explanation for a recommendation.

**Parameters:**
- `recommendation` (ChartRecommendation): Recommendation to explain

**Returns:**
- `str`: Detailed explanation

**Example:**
```python
selector = SmartChartSelector()
rec = selector.recommend(data, intent='correlation')

# Get detailed explanation
explanation = selector.explain_recommendation(rec)
print(explanation)
```

## Natural Language Styling

### `vc.style_chart(chart, description, **kwargs)`

Apply styling to a chart using natural language.

**Parameters:**
- `chart`: Chart object to style
- `description` (str): Natural language styling description
- `**kwargs`: Additional styling parameters

**Example:**
```python
chart = vc.LineChart()
chart.plot(x, y)

# Apply styling with natural language
vc.style_chart(chart, "professional blue theme with bold fonts")
vc.style_chart(chart, "elegant pastel colors with shadows")
vc.style_chart(chart, "modern dark theme with neon accents")
```

### `vc.ai.parse_style(description)`

Parse natural language styling description.

**Parameters:**
- `description` (str): Styling description

**Returns:**
- `StyleConfig`: Parsed styling configuration

**Example:**
```python
style = vc.ai.parse_style("professional blue theme with bold fonts")

print(f"Theme: {style.overall_theme}")      # "professional"
print(f"Colors: {style.color_scheme}")      # "blue"
print(f"Fonts: {style.font_weight}")        # "bold"
```

### `NaturalLanguageStylist`

Advanced styling engine with customization options.

#### `NaturalLanguageStylist(model=None)`

**Parameters:**
- `model` (str, optional): AI model to use for style parsing

#### Methods

##### `parse(description)`

Parse styling description into actionable configuration.

**Parameters:**
- `description` (str): Natural language styling description

**Returns:**
- `StyleConfig`: Detailed styling configuration

##### `apply_style(chart, style_config)`

Apply parsed style configuration to a chart.

**Parameters:**
- `chart`: Chart object to style
- `style_config` (StyleConfig): Style configuration to apply

**Example:**
```python
stylist = NaturalLanguageStylist()

# Parse style description
style_config = stylist.parse("minimalist black and white with thin lines")

# Apply to chart
chart = vc.LineChart()
chart.plot(x, y)
stylist.apply_style(chart, style_config)
```

## Data Analysis

### `vc.ai.analyze_data(data, **kwargs)`

Perform comprehensive data analysis.

**Parameters:**
- `data`: Data to analyze
- `**kwargs`: Analysis options

**Returns:**
- `DataAnalysis`: Comprehensive analysis results

**Example:**
```python
analysis = vc.ai.analyze_data(data)

print(f"Data shape: {analysis.shape}")
print(f"Variable types: {analysis.variable_types}")
print(f"Missing values: {analysis.missing_values}")
print(f"Correlations: {analysis.correlations}")
print(f"Outliers: {analysis.outliers}")
print(f"Patterns: {analysis.patterns}")
```

### `vc.ai.suggest_visualizations(data, **kwargs)`

Get comprehensive visualization suggestions.

**Parameters:**
- `data`: Data to analyze
- `**kwargs`: Suggestion parameters

**Returns:**
- `list`: List of visualization suggestions with explanations

**Example:**
```python
suggestions = vc.ai.suggest_visualizations(data)

for suggestion in suggestions:
    print(f"Chart: {suggestion.chart_type}")
    print(f"Purpose: {suggestion.purpose}")
    print(f"Insights: {suggestion.potential_insights}")
    print(f"Code: {suggestion.code_example}")
    print("---")
```

## Configuration Classes

### `ChartRecommendation`

Result object containing chart recommendation details.

#### Attributes
- `chart_type` (str): Recommended chart type
- `confidence` (float): Confidence score (0-1)
- `reasoning` (str): Explanation for recommendation
- `parameters` (dict): Suggested chart parameters
- `data_mapping` (dict): How to map data to chart elements
- `styling_suggestions` (dict): Recommended styling options

#### Methods

##### `create_chart(data=None)`

Create the recommended chart.

**Parameters:**
- `data` (optional): Data to plot

**Returns:**
- Chart object of the recommended type

**Example:**
```python
rec = vc.recommend_chart(data, intent='correlation')

# Create chart from recommendation
chart = rec.create_chart(data)
chart.show()
```

### `StyleConfig`

Configuration object for chart styling.

#### Attributes
- `overall_theme` (str): Overall theme category
- `color_scheme` (str): Color scheme name
- `font_family` (str): Font family
- `font_weight` (str): Font weight
- `background_color` (str): Background color
- `grid_style` (dict): Grid styling options
- `legend_style` (dict): Legend styling options

### `DataProfile`

Detailed data analysis results.

#### Attributes
- `data_type` (str): Type of dataset
- `shape` (tuple): Data dimensions
- `variables` (dict): Variable information
- `relationships` (dict): Variable relationships
- `patterns` (list): Detected patterns
- `quality_issues` (list): Data quality problems
- `recommendations` (list): Analysis recommendations

## Advanced Features

### Custom AI Models

You can configure VizlyChart to use custom AI models:

```python
# Configure custom model for chart generation
vc.ai.config.set_model('chart_generation', 'custom-model-name')

# Configure custom model for styling
vc.ai.config.set_model('styling', 'custom-styling-model')

# Use local models
vc.ai.config.set_local_model('chart_generation', '/path/to/model')
```

### Batch Processing

Process multiple datasets or descriptions at once:

```python
# Batch chart generation
descriptions = [
    "line chart of sales over time",
    "scatter plot of price vs demand",
    "bar chart of regional performance"
]

charts = vc.ai.batch_create(descriptions, datasets=[data1, data2, data3])

# Batch recommendations
datasets = [sales_data, performance_data, survey_data]
recommendations = vc.ai.batch_recommend(datasets, intents=['trend', 'comparison', 'distribution'])
```

### Custom Analysis Functions

Register custom analysis functions:

```python
@vc.ai.register_analyzer('custom_correlation')
def custom_correlation_analysis(data):
    """Custom correlation analysis"""
    # Your custom analysis logic
    return analysis_results

# Use in recommendations
rec = vc.recommend_chart(data, analyzers=['custom_correlation'])
```

## Error Handling

AI module specific exceptions:

### `AIError`

Base exception for AI-related errors.

### `ModelNotAvailableError`

Raised when requested AI model is not available.

### `ParseError`

Raised when natural language parsing fails.

**Example:**
```python
try:
    chart = vc.ai.create("invalid chart description")
except vc.ai.ParseError as e:
    print(f"Parse error: {e}")
    print("Suggestions:")
    for suggestion in e.suggestions:
        print(f"- {suggestion}")
except vc.ai.ModelNotAvailableError as e:
    print(f"Model error: {e}")
    # Fallback to rule-based system
    chart = vc.ai.create_fallback(description)
```

## Performance Optimization

### Caching

AI results are cached for better performance:

```python
# Enable/disable caching
vc.ai.config.set('caching.enabled', True)

# Set cache size
vc.ai.config.set('caching.max_size', 1000)

# Clear cache
vc.ai.clear_cache()
```

### Async Operations

Use async operations for better performance:

```python
import asyncio

async def generate_multiple_charts():
    tasks = [
        vc.ai.create_async("line chart of data1"),
        vc.ai.create_async("scatter plot of data2"),
        vc.ai.create_async("bar chart of data3")
    ]

    charts = await asyncio.gather(*tasks)
    return charts
```

## Examples

### Complete AI Workflow

```python
import vizlychart as vc
import pandas as pd

# Load data
df = pd.read_csv('sales_data.csv')

# Get AI analysis
analysis = vc.ai.analyze_data(df)
print(f"Data summary: {analysis.summary}")

# Get visualization suggestions
suggestions = vc.ai.suggest_visualizations(df)

# Create recommended chart
best_suggestion = suggestions[0]
chart = vc.ai.create(best_suggestion.description, data=df)

# Apply AI styling
vc.style_chart(chart, "professional business theme")

# Show result
chart.show()
```

### Interactive AI Assistant

```python
def ai_chart_assistant(data):
    """Interactive chart creation assistant"""

    # Analyze data
    analysis = vc.ai.analyze_data(data)
    print(f"Data Analysis:")
    print(f"- Shape: {analysis.shape}")
    print(f"- Variables: {list(analysis.variables.keys())}")

    # Get recommendations
    recommendations = vc.ai.suggest_visualizations(data)

    print("\nVisualization Suggestions:")
    for i, rec in enumerate(recommendations[:5]):
        print(f"{i+1}. {rec.chart_type}: {rec.purpose}")

    # User selection
    choice = int(input("Select visualization (1-5): ")) - 1
    selected = recommendations[choice]

    # Create and style chart
    chart = vc.ai.create(selected.description, data=data)
    style = input("Describe styling (optional): ")
    if style:
        vc.style_chart(chart, style)

    return chart

# Usage
chart = ai_chart_assistant(your_data)
chart.show()
```

---

The AI module makes VizlyChart uniquely powerful by bringing intelligence to every aspect of visualization creation. For more examples, see the [AI Features Tutorial](../features/ai-features.md).