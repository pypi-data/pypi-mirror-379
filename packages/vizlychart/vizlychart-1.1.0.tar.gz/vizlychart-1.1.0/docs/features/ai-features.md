# AI-Powered Features

VizlyChart's AI features revolutionize how you create visualizations by bringing intelligence to every step of the process. From natural language chart generation to smart recommendations and intelligent styling, AI makes visualization creation faster, smarter, and more intuitive.

## Overview

VizlyChart's AI capabilities include:

- **🗣️ Natural Language Chart Generation**: Create charts from text descriptions
- **🧠 Smart Chart Recommendations**: AI suggests optimal chart types for your data
- **🎨 Intelligent Styling**: Apply themes using natural language descriptions
- **📊 Automated Data Analysis**: AI analyzes your data and suggests insights
- **🔍 Pattern Recognition**: Automatically detect trends, outliers, and relationships

## Natural Language Chart Generation

### Basic Usage

Create charts by simply describing what you want:

```python
import vizlychart as vc

# Generate charts from descriptions
chart1 = vc.ai.create("line chart showing temperature over time")
chart2 = vc.ai.create("scatter plot of price vs sales with trend line")
chart3 = vc.ai.create("bar chart comparing revenue by region")
```

### With Your Own Data

Combine natural language descriptions with your data:

```python
import pandas as pd
import numpy as np

# Sample sales data
data = pd.DataFrame({
    'date': pd.date_range('2023-01-01', periods=12, freq='M'),
    'revenue': [1000, 1200, 1100, 1300, 1500, 1400, 1600, 1800, 1700, 1900, 2000, 2100],
    'region': ['North', 'South', 'East', 'West'] * 3
})

# Create chart with natural language
chart = vc.ai.create(
    "line chart showing revenue growth over time with monthly data points",
    data=data
)
chart.show()
```

### Advanced Descriptions

Use detailed descriptions for complex visualizations:

```python
# Complex chart with multiple specifications
chart = vc.ai.create("""
    Create a scatter plot showing the relationship between marketing spend and sales revenue.
    Use blue circles for the data points with 50% transparency.
    Add a red trend line with confidence intervals.
    Include correlation coefficient in the title.
    Make the chart suitable for a business presentation.
""", data=marketing_data)
```

### Supported Chart Types

The AI can generate various chart types from natural language:

```python
# Line charts
vc.ai.create("time series plot of stock prices")
vc.ai.create("multi-line chart comparing three metrics over time")

# Scatter plots
vc.ai.create("scatter plot with correlation analysis")
vc.ai.create("bubble chart with size representing importance")

# Bar charts
vc.ai.create("horizontal bar chart of survey responses")
vc.ai.create("grouped bar chart comparing categories")

# Statistical charts
vc.ai.create("histogram showing distribution of ages")
vc.ai.create("box plot comparing groups")

# Advanced charts
vc.ai.create("heatmap of correlation matrix")
vc.ai.create("violin plot showing distribution by category")
```

## Smart Chart Recommendations

### Getting Recommendations

Let AI analyze your data and suggest the best chart types:

```python
import vizlychart as vc
import numpy as np

# Sample data
data = {
    'height': np.random.normal(170, 10, 100),
    'weight': np.random.normal(70, 15, 100),
    'age': np.random.randint(20, 60, 100),
    'gender': np.random.choice(['M', 'F'], 100)
}

# Get AI recommendation
rec = vc.recommend_chart(data, intent='correlation')

print(f"Recommended chart: {rec.chart_type}")
print(f"Confidence: {rec.confidence:.0%}")
print(f"Reasoning: {rec.reasoning}")

# Create the recommended chart
chart = rec.create_chart(data)
chart.show()
```

### Analysis Intents

Specify your analysis intent for better recommendations:

```python
# Different intents give different recommendations
correlation_rec = vc.recommend_chart(data, intent='correlation')
distribution_rec = vc.recommend_chart(data, intent='distribution')
trend_rec = vc.recommend_chart(time_series_data, intent='trend')
comparison_rec = vc.recommend_chart(category_data, intent='comparison')

print(f"For correlation: {correlation_rec.chart_type}")
print(f"For distribution: {distribution_rec.chart_type}")
print(f"For trends: {trend_rec.chart_type}")
print(f"For comparison: {comparison_rec.chart_type}")
```

**Available Intents:**
- `'correlation'`: Show relationships between variables
- `'distribution'`: Show data distribution patterns
- `'trend'`: Show trends over time
- `'comparison'`: Compare categories or groups
- `'composition'`: Show parts of a whole
- `'ranking'`: Show relative rankings

### Multiple Recommendations

Get multiple recommendations with confidence scores:

```python
# Get all recommendations
all_recs = vc.recommend_chart(data, return_all=True)

print("All recommendations:")
for i, rec in enumerate(all_recs):
    print(f"{i+1}. {rec.chart_type} (confidence: {rec.confidence:.0%})")
    print(f"   Reasoning: {rec.reasoning}")
    print()
```

### Interactive Selection

Create an interactive recommendation system:

```python
def interactive_chart_selection(data):
    """Interactive chart selection with AI recommendations"""

    # Get recommendations
    recommendations = vc.recommend_chart(data, return_all=True)

    print("AI Chart Recommendations:")
    print("=" * 40)

    for i, rec in enumerate(recommendations[:5]):
        print(f"{i+1}. {rec.chart_type.title()} Chart")
        print(f"   Confidence: {rec.confidence:.0%}")
        print(f"   Purpose: {rec.reasoning}")
        print()

    # User selection
    while True:
        try:
            choice = int(input("Select chart (1-5): ")) - 1
            if 0 <= choice < len(recommendations[:5]):
                break
            print("Please enter a number between 1 and 5")
        except ValueError:
            print("Please enter a valid number")

    # Create selected chart
    selected_rec = recommendations[choice]
    chart = selected_rec.create_chart(data)

    print(f"\nCreated {selected_rec.chart_type} chart!")
    return chart

# Usage
chart = interactive_chart_selection(your_data)
chart.show()
```

## Intelligent Styling

### Natural Language Styling

Apply styling using natural language descriptions:

```python
chart = vc.LineChart()
chart.plot(x, y, label="Data")

# Apply different styles with natural language
vc.style_chart(chart, "professional blue theme with bold fonts")
chart.show()

vc.style_chart(chart, "elegant pastel colors with shadows")
chart.show()

vc.style_chart(chart, "modern dark theme with neon accents")
chart.show()

vc.style_chart(chart, "minimalist black and white design")
chart.show()
```

### Style Categories

The AI understands various style categories:

```python
# Business/Professional styles
vc.style_chart(chart, "corporate presentation style")
vc.style_chart(chart, "executive dashboard theme")
vc.style_chart(chart, "professional report styling")

# Academic/Scientific styles
vc.style_chart(chart, "scientific publication format")
vc.style_chart(chart, "academic paper styling")
vc.style_chart(chart, "research presentation theme")

# Modern/Trendy styles
vc.style_chart(chart, "modern gradient design")
vc.style_chart(chart, "trendy flat design")
vc.style_chart(chart, "contemporary minimalist style")

# Specific color schemes
vc.style_chart(chart, "warm autumn colors")
vc.style_chart(chart, "cool ocean blues")
vc.style_chart(chart, "vibrant rainbow palette")
```

### Advanced Styling

Combine multiple styling elements:

```python
# Complex styling instructions
vc.style_chart(chart, """
    Apply a professional business theme with:
    - Navy blue and gold color scheme
    - Sans-serif fonts with medium weight
    - Subtle grid lines
    - Drop shadows on data elements
    - Clean white background
    - Legend positioned at the top
""")
```

### Contextual Styling

AI can apply styling based on context:

```python
# Context-aware styling
financial_chart = vc.ai.create("line chart of stock prices", data=stock_data)
vc.style_chart(financial_chart, "financial trading application style")

medical_chart = vc.ai.create("bar chart of patient outcomes", data=medical_data)
vc.style_chart(medical_chart, "medical research publication format")

marketing_chart = vc.ai.create("pie chart of campaign performance", data=campaign_data)
vc.style_chart(marketing_chart, "marketing presentation theme")
```

## Automated Data Analysis

### Comprehensive Data Analysis

Let AI analyze your data and provide insights:

```python
import vizlychart as vc
import pandas as pd

# Load your data
df = pd.read_csv('sales_data.csv')

# Get AI analysis
analysis = vc.ai.analyze_data(df)

print("Data Analysis Results:")
print("=" * 30)
print(f"Dataset shape: {analysis.shape}")
print(f"Variables: {list(analysis.variables.keys())}")
print(f"Data quality score: {analysis.quality_score:.2f}")

print("\nKey Insights:")
for insight in analysis.insights:
    print(f"- {insight}")

print("\nRecommended Visualizations:")
for rec in analysis.visualization_recommendations:
    print(f"- {rec.chart_type}: {rec.purpose}")
```

### Pattern Detection

AI automatically detects patterns in your data:

```python
# Pattern detection
patterns = vc.ai.detect_patterns(data)

print("Detected Patterns:")
for pattern in patterns:
    print(f"- {pattern.type}: {pattern.description}")
    print(f"  Confidence: {pattern.confidence:.0%}")
    print(f"  Variables: {pattern.variables}")
```

### Outlier Detection

Identify outliers and anomalies:

```python
# Outlier detection
outliers = vc.ai.detect_outliers(data)

print(f"Found {len(outliers)} outliers:")
for outlier in outliers:
    print(f"- Row {outlier.index}: {outlier.values}")
    print(f"  Reason: {outlier.reason}")

# Visualize outliers
chart = vc.ai.create("scatter plot highlighting outliers", data=data)
chart.show()
```

## Complete AI Workflow

### Automated Visualization Pipeline

Create a complete AI-powered visualization workflow:

```python
def ai_visualization_pipeline(data, title="AI Analysis"):
    """Complete AI-powered visualization pipeline"""

    print(f"🤖 AI Visualization Pipeline: {title}")
    print("=" * 50)

    # Step 1: Analyze data
    print("📊 Analyzing data...")
    analysis = vc.ai.analyze_data(data)

    print(f"✅ Analysis complete!")
    print(f"   - Data shape: {analysis.shape}")
    print(f"   - Quality score: {analysis.quality_score:.2f}")
    print(f"   - Key insights: {len(analysis.insights)}")

    # Step 2: Get visualization recommendations
    print("\n🎯 Getting chart recommendations...")
    recommendations = vc.ai.suggest_visualizations(data)

    print(f"✅ Found {len(recommendations)} recommendations!")

    # Step 3: Create charts for top recommendations
    print("\n📈 Creating visualizations...")
    charts = []

    for i, rec in enumerate(recommendations[:3]):  # Top 3 recommendations
        print(f"   Creating {rec.chart_type} chart...")

        # Create chart
        chart = vc.ai.create(rec.description, data=data)

        # Apply AI styling
        vc.style_chart(chart, "professional presentation theme")

        # Set title
        chart.set_title(f"{title} - {rec.chart_type.title()}")

        charts.append(chart)

    print("✅ Visualization pipeline complete!")
    return charts, analysis

# Usage
charts, analysis = ai_visualization_pipeline(sales_data, "Sales Analysis")

# Display all charts
for chart in charts:
    chart.show()

# Print insights
print("\n💡 Key Insights:")
for insight in analysis.insights:
    print(f"- {insight}")
```

### Business Intelligence Dashboard

Create an AI-powered dashboard:

```python
def create_ai_dashboard(datasets, dashboard_title="AI Dashboard"):
    """Create AI-powered business intelligence dashboard"""

    dashboard_charts = []

    for name, data in datasets.items():
        print(f"Processing {name}...")

        # Get best visualization for each dataset
        rec = vc.recommend_chart(data, intent='auto')

        # Create chart
        chart = vc.ai.create(
            f"{rec.chart_type} showing {name} data with insights",
            data=data
        )

        # Apply consistent styling
        vc.style_chart(chart, "modern business dashboard theme")

        chart.set_title(name.title())
        dashboard_charts.append(chart)

    return dashboard_charts

# Usage
business_data = {
    'sales_trends': sales_data,
    'customer_segments': customer_data,
    'performance_metrics': performance_data,
    'regional_analysis': regional_data
}

dashboard = create_ai_dashboard(business_data, "Q4 Business Review")

# Display dashboard
for chart in dashboard:
    chart.show()
```

## Advanced AI Features

### Custom AI Models

Configure custom AI models for specialized domains:

```python
# Use custom model for financial analysis
vc.ai.set_domain_model('financial')

# Financial-specific chart generation
chart = vc.ai.create("candlestick chart with technical indicators", data=stock_data)

# Use custom model for scientific data
vc.ai.set_domain_model('scientific')

# Scientific-specific analysis
chart = vc.ai.create("publication-quality scatter plot with error bars", data=experiment_data)
```

### Batch Processing

Process multiple datasets or descriptions at once:

```python
# Batch chart generation
descriptions = [
    "sales trend analysis over the past year",
    "customer segmentation visualization",
    "regional performance comparison",
    "product category breakdown"
]

datasets = [sales_data, customer_data, regional_data, product_data]

# Generate all charts at once
charts = vc.ai.batch_create(descriptions, datasets=datasets)

# Apply consistent styling to all
for chart in charts:
    vc.style_chart(chart, "corporate presentation theme")
    chart.show()
```

### AI-Assisted Exploration

Interactive data exploration with AI guidance:

```python
def ai_data_explorer(data):
    """AI-assisted data exploration"""

    while True:
        print("\n🤖 AI Data Explorer")
        print("=" * 25)
        print("1. Analyze data patterns")
        print("2. Get visualization suggestions")
        print("3. Create custom chart")
        print("4. Find correlations")
        print("5. Detect outliers")
        print("6. Exit")

        choice = input("Select option (1-6): ")

        if choice == '1':
            analysis = vc.ai.analyze_data(data)
            for insight in analysis.insights:
                print(f"📊 {insight}")

        elif choice == '2':
            suggestions = vc.ai.suggest_visualizations(data)
            for i, sug in enumerate(suggestions[:3]):
                print(f"{i+1}. {sug.chart_type}: {sug.purpose}")

        elif choice == '3':
            description = input("Describe the chart you want: ")
            chart = vc.ai.create(description, data=data)
            style = input("Describe styling (optional): ")
            if style:
                vc.style_chart(chart, style)
            chart.show()

        elif choice == '4':
            correlations = vc.ai.find_correlations(data)
            for corr in correlations:
                print(f"📈 {corr.variables}: {corr.strength:.2f}")

        elif choice == '5':
            outliers = vc.ai.detect_outliers(data)
            print(f"🔍 Found {len(outliers)} outliers")
            if outliers:
                chart = vc.ai.create("scatter plot highlighting outliers", data=data)
                chart.show()

        elif choice == '6':
            break

# Usage
ai_data_explorer(your_data)
```

## Best Practices

### 1. Descriptive Prompts

Use clear, descriptive prompts for better results:

```python
# Good: Specific and clear
chart = vc.ai.create(
    "line chart showing monthly sales revenue with trend line and seasonal indicators"
)

# Better: Include context and requirements
chart = vc.ai.create(
    "professional line chart displaying monthly sales revenue from January to December 2023, "
    "with trend line, confidence intervals, and highlighting of peak seasons"
)
```

### 2. Iterative Refinement

Refine charts iteratively with AI assistance:

```python
# Start with basic chart
chart = vc.ai.create("sales data visualization", data=sales_data)

# Refine with AI styling
vc.style_chart(chart, "make it more professional for executive presentation")

# Further refinement
vc.style_chart(chart, "add subtle animations and improve color contrast")
```

### 3. Combine AI with Manual Control

Use AI for initial creation, then manual fine-tuning:

```python
# AI creates the foundation
chart = vc.ai.create("correlation analysis chart", data=data)

# Manual refinements
chart.set_title("Customer Behavior Analysis", fontsize=16)
chart.set_xlabel("Purchase Frequency")
chart.set_ylabel("Customer Lifetime Value")
chart.add_trendline(color='red', alpha=0.8)
```

### 4. Domain-Specific Context

Provide domain context for better AI understanding:

```python
# Include domain context
chart = vc.ai.create(
    "financial performance chart suitable for investor presentation showing quarterly revenue growth",
    data=financial_data
)

# Or set domain globally
vc.ai.set_context("healthcare analytics")
chart = vc.ai.create("patient outcome analysis", data=patient_data)
```

## Troubleshooting

### Common Issues

**AI generates wrong chart type:**
```python
# Be more specific in description
# Instead of: "show my data"
# Use: "scatter plot showing correlation between variables X and Y"

# Or specify intent explicitly
rec = vc.recommend_chart(data, intent='correlation')
chart = rec.create_chart(data)
```

**Styling doesn't match expectations:**
```python
# Use more detailed styling descriptions
# Instead of: "make it pretty"
# Use: "professional blue theme with clean white background and subtle grid lines"

# Or use multiple styling steps
vc.style_chart(chart, "professional theme")
vc.style_chart(chart, "blue color scheme")
vc.style_chart(chart, "clean typography")
```

**Performance issues with large datasets:**
```python
# Enable AI optimization for large data
chart = vc.ai.create("scatter plot", data=large_data, optimize=True)

# Or use data sampling
sample_data = data.sample(n=10000)
chart = vc.ai.create("data analysis chart", data=sample_data)
```

---

VizlyChart's AI features transform visualization creation from a manual process to an intelligent, guided experience. The AI understands your intent, analyzes your data, and creates beautiful, meaningful visualizations with minimal effort from you.

**Next:** Explore [Backend Switching](backends.md) to learn how AI works across different rendering engines.