# Code Examples

This section provides comprehensive, working examples of VizlyChart features. All examples include complete, runnable code that demonstrates real-world usage scenarios.

## Quick Start Examples

### Basic Chart Creation
```python
import vizlychart as vc
import numpy as np

# Create sample data
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)

# Create line chart
chart = vc.LineChart()
chart.plot(x, y, label="Noisy Sine Wave", color='blue', linewidth=2)
chart.set_title("Basic Line Chart")
chart.set_xlabel("X Values")
chart.set_ylabel("Y Values")
chart.legend()
chart.grid(True, alpha=0.3)
chart.show()
```

### Multiple Data Series
```python
import vizlychart as vc
import numpy as np

# Generate data for multiple series
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x + np.pi/4)

# Create chart with multiple series
chart = vc.LineChart()
chart.plot(x, y1, label="sin(x)", color='blue', linewidth=2)
chart.plot(x, y2, label="cos(x)", color='red', linewidth=2, linestyle='--')
chart.plot(x, y3, label="sin(x+π/4)", color='green', linewidth=2, linestyle='-.')

chart.set_title("Trigonometric Functions")
chart.set_xlabel("X")
chart.set_ylabel("Y")
chart.legend()
chart.grid(True, alpha=0.3)
chart.show()
```

## AI-Powered Examples

### Natural Language Chart Generation
```python
import vizlychart as vc
import pandas as pd
import numpy as np

# Create sample business data
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=12, freq='M')
revenue = np.cumsum(np.random.normal(10000, 2000, 12)) + 50000
customers = np.cumsum(np.random.normal(100, 20, 12)) + 1000

data = pd.DataFrame({
    'date': dates,
    'revenue': revenue,
    'customers': customers
})

# Generate chart with natural language
chart = vc.ai.create(
    "professional line chart showing revenue growth over time with monthly data points",
    data=data
)

# Apply professional styling
vc.style_chart(chart, "corporate presentation theme with blue accents")

chart.show()
```

### Smart Chart Recommendations
```python
import vizlychart as vc
import numpy as np

# Create correlation data
np.random.seed(123)
marketing_spend = np.random.uniform(1000, 10000, 50)
sales = 2.5 * marketing_spend + np.random.normal(0, 5000, 50)
region = np.random.choice(['North', 'South', 'East', 'West'], 50)

data = {
    'marketing_spend': marketing_spend,
    'sales': sales,
    'region': region
}

# Get AI recommendation
rec = vc.recommend_chart(data, intent='correlation')

print(f"AI Recommendation:")
print(f"Chart Type: {rec.chart_type}")
print(f"Confidence: {rec.confidence:.0%}")
print(f"Reasoning: {rec.reasoning}")

# Create recommended chart
chart = rec.create_chart(data)
chart.set_title(f"Marketing ROI Analysis (AI Recommended: {rec.chart_type})")
chart.show()
```

## Chart Type Examples

### Scatter Plot with Analysis
```python
import vizlychart as vc
import numpy as np
from scipy import stats

# Generate correlated data
np.random.seed(42)
n_points = 200
x = np.random.normal(100, 15, n_points)
y = 1.5 * x + np.random.normal(0, 10, n_points)

# Create scatter plot
chart = vc.ScatterChart()
chart.plot(x, y, alpha=0.6, s=50, color='steelblue', edgecolors='navy')

# Add trend line
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
line_x = np.array([x.min(), x.max()])
line_y = slope * line_x + intercept
chart.plot(line_x, line_y, color='red', linewidth=2, label=f'Trend (r={r_value:.3f})')

chart.set_title("Scatter Plot with Correlation Analysis")
chart.set_xlabel("X Variable")
chart.set_ylabel("Y Variable")
chart.legend()
chart.grid(True, alpha=0.3)
chart.show()

print(f"Correlation coefficient: {r_value:.3f}")
print(f"R-squared: {r_value**2:.3f}")
```

### Bar Chart with Categories
```python
import vizlychart as vc
import numpy as np

# Sales data by category and region
categories = ['Electronics', 'Clothing', 'Books', 'Home & Garden', 'Sports']
q1_sales = [45000, 32000, 18000, 28000, 22000]
q2_sales = [48000, 35000, 16000, 31000, 25000]
q3_sales = [52000, 38000, 19000, 29000, 27000]
q4_sales = [55000, 42000, 21000, 33000, 30000]

# Create grouped bar chart
x = np.arange(len(categories))
width = 0.2

chart = vc.BarChart()
chart.plot(x - 1.5*width, q1_sales, width, label='Q1', color='#FF6B6B', alpha=0.8)
chart.plot(x - 0.5*width, q2_sales, width, label='Q2', color='#4ECDC4', alpha=0.8)
chart.plot(x + 0.5*width, q3_sales, width, label='Q3', color='#45B7D1', alpha=0.8)
chart.plot(x + 1.5*width, q4_sales, width, label='Q4', color='#96CEB4', alpha=0.8)

chart.set_xlabel('Product Categories')
chart.set_ylabel('Sales ($)')
chart.set_title('Quarterly Sales by Product Category')
chart.set_xticks(x)
chart.set_xticklabels(categories)
chart.legend()
chart.grid(True, axis='y', alpha=0.3)
chart.show()
```

### Heatmap Visualization
```python
import vizlychart as vc
import numpy as np
import pandas as pd

# Create correlation matrix
np.random.seed(42)
variables = ['Sales', 'Marketing', 'Customer_Sat', 'Price', 'Competition', 'Season']
data = np.random.randn(100, len(variables))

# Add some correlations
data[:, 1] = 0.7 * data[:, 0] + 0.3 * np.random.randn(100)  # Marketing correlated with Sales
data[:, 2] = -0.5 * data[:, 3] + 0.5 * np.random.randn(100)  # Customer Satisfaction vs Price

df = pd.DataFrame(data, columns=variables)
correlation_matrix = df.corr()

# Create heatmap
chart = vc.HeatmapChart()
chart.plot(correlation_matrix,
           annot=True,
           fmt='.2f',
           cmap='RdBu_r',
           center=0,
           square=True,
           cbar_kws={'label': 'Correlation Coefficient'})

chart.set_title('Business Metrics Correlation Matrix')
chart.show()
```

## Real-World Use Cases

### Financial Analysis Dashboard
```python
import vizlychart as vc
import pandas as pd
import numpy as np

# Generate sample financial data
np.random.seed(42)
dates = pd.date_range('2020-01-01', '2023-12-31', freq='M')
n_months = len(dates)

# Create realistic financial metrics
revenue = np.cumsum(np.random.normal(50000, 10000, n_months)) + 500000
profit_margin = np.random.uniform(0.1, 0.3, n_months)
profit = revenue * profit_margin
expenses = revenue - profit

data = pd.DataFrame({
    'date': dates,
    'revenue': revenue,
    'profit': profit,
    'expenses': expenses,
    'profit_margin': profit_margin * 100
})

# Revenue trend
revenue_chart = vc.LineChart()
revenue_chart.plot(data['date'], data['revenue'],
                   color='#2E86AB', linewidth=3, marker='o', markersize=4)
revenue_chart.set_title('Revenue Trend (2020-2023)', fontsize=14, fontweight='bold')
revenue_chart.set_ylabel('Revenue ($)')
revenue_chart.grid(True, alpha=0.3)

# Profit vs Expenses
comparison_chart = vc.LineChart()
comparison_chart.plot(data['date'], data['profit'],
                     label='Profit', color='#A23B72', linewidth=2)
comparison_chart.plot(data['date'], data['expenses'],
                     label='Expenses', color='#F18F01', linewidth=2)
comparison_chart.set_title('Profit vs Expenses Over Time')
comparison_chart.set_ylabel('Amount ($)')
comparison_chart.legend()
comparison_chart.grid(True, alpha=0.3)

# Profit margin
margin_chart = vc.LineChart()
margin_chart.plot(data['date'], data['profit_margin'],
                  color='#C73E1D', linewidth=2, marker='s', markersize=3)
margin_chart.set_title('Profit Margin Trend')
margin_chart.set_ylabel('Profit Margin (%)')
margin_chart.grid(True, alpha=0.3)

# Display all charts
revenue_chart.show()
comparison_chart.show()
margin_chart.show()
```

### Scientific Data Visualization
```python
import vizlychart as vc
import numpy as np
from scipy.stats import norm

# Generate experimental data
np.random.seed(123)

# Control and treatment groups
control_group = np.random.normal(100, 15, 50)
treatment_group = np.random.normal(110, 12, 50)

# Create comparison visualization
comparison_chart = vc.BoxPlotChart()
comparison_chart.plot([control_group, treatment_group],
                     labels=['Control', 'Treatment'],
                     patch_artist=True,
                     boxprops={'facecolor': '#E8F4FD', 'alpha': 0.7},
                     medianprops={'color': '#2E86AB', 'linewidth': 2})

comparison_chart.set_title('Treatment Effect Analysis', fontsize=14)
comparison_chart.set_ylabel('Response Value')
comparison_chart.grid(True, alpha=0.3)

# Distribution overlay
dist_chart = vc.LineChart()

# Plot histograms as lines
x = np.linspace(60, 140, 100)
control_density = norm.pdf(x, np.mean(control_group), np.std(control_group))
treatment_density = norm.pdf(x, np.mean(treatment_group), np.std(treatment_group))

dist_chart.plot(x, control_density, label='Control Distribution',
               color='#A23B72', linewidth=2, alpha=0.8)
dist_chart.plot(x, treatment_density, label='Treatment Distribution',
               color='#2E86AB', linewidth=2, alpha=0.8)

dist_chart.fill_between(x, 0, control_density, alpha=0.3, color='#A23B72')
dist_chart.fill_between(x, 0, treatment_density, alpha=0.3, color='#2E86AB')

dist_chart.set_title('Distribution Comparison')
dist_chart.set_xlabel('Response Value')
dist_chart.set_ylabel('Probability Density')
dist_chart.legend()
dist_chart.grid(True, alpha=0.3)

comparison_chart.show()
dist_chart.show()

# Statistical summary
print(f"Control Group: Mean = {np.mean(control_group):.2f}, SD = {np.std(control_group):.2f}")
print(f"Treatment Group: Mean = {np.mean(treatment_group):.2f}, SD = {np.std(treatment_group):.2f}")
print(f"Effect Size (Cohen's d): {(np.mean(treatment_group) - np.mean(control_group)) / np.sqrt((np.var(control_group) + np.var(treatment_group)) / 2):.2f}")
```

### Marketing Analytics
```python
import vizlychart as vc
import pandas as pd
import numpy as np

# Marketing campaign data
np.random.seed(456)
campaigns = ['Email', 'Social Media', 'PPC', 'Content', 'Direct Mail']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Generate realistic campaign performance data
data = {}
for campaign in campaigns:
    # Different campaigns have different patterns
    if campaign == 'Email':
        base = 5000
        growth = np.cumsum(np.random.normal(200, 50, len(months)))
    elif campaign == 'Social Media':
        base = 8000
        growth = np.cumsum(np.random.normal(400, 100, len(months)))
    elif campaign == 'PPC':
        base = 3000
        growth = np.cumsum(np.random.normal(150, 75, len(months)))
    elif campaign == 'Content':
        base = 6000
        growth = np.cumsum(np.random.normal(300, 80, len(months)))
    else:  # Direct Mail
        base = 2000
        growth = np.cumsum(np.random.normal(100, 30, len(months)))

    data[campaign] = base + growth

df = pd.DataFrame(data, index=months)

# Campaign performance over time
performance_chart = vc.LineChart()
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

for i, campaign in enumerate(campaigns):
    performance_chart.plot(months, df[campaign],
                          label=campaign,
                          color=colors[i],
                          linewidth=2,
                          marker='o',
                          markersize=6)

performance_chart.set_title('Marketing Campaign Performance', fontsize=14, fontweight='bold')
performance_chart.set_xlabel('Month')
performance_chart.set_ylabel('Conversions')
performance_chart.legend(loc='upper left')
performance_chart.grid(True, alpha=0.3)

# Campaign comparison (latest month)
latest_performance = df.iloc[-1]
comparison_chart = vc.BarChart()
comparison_chart.plot(campaigns, latest_performance.values,
                     color=colors, alpha=0.8, edgecolor='black')

comparison_chart.set_title('Latest Month Performance Comparison')
comparison_chart.set_xlabel('Campaign Type')
comparison_chart.set_ylabel('Conversions')
comparison_chart.grid(True, axis='y', alpha=0.3)

# ROI analysis (assuming different costs per campaign)
costs = [1000, 2000, 3000, 1500, 500]  # Campaign costs
roi = [(latest_performance[camp] * 10 - cost) / cost * 100
       for camp, cost in zip(campaigns, costs)]

roi_chart = vc.BarChart()
roi_colors = ['green' if r > 0 else 'red' for r in roi]
roi_chart.plot(campaigns, roi, color=roi_colors, alpha=0.7, edgecolor='black')

roi_chart.set_title('Campaign ROI Analysis')
roi_chart.set_xlabel('Campaign Type')
roi_chart.set_ylabel('ROI (%)')
roi_chart.grid(True, axis='y', alpha=0.3)

# Show all charts
performance_chart.show()
comparison_chart.show()
roi_chart.show()

# Print summary
print("Marketing Campaign Summary:")
print("=" * 30)
for i, campaign in enumerate(campaigns):
    print(f"{campaign}:")
    print(f"  Latest conversions: {latest_performance[campaign]:.0f}")
    print(f"  ROI: {roi[i]:.1f}%")
    print()
```

## Backend Switching Examples

### Same Chart, Different Backends
```python
import vizlychart as vc
import numpy as np

# Create sample data
x = np.linspace(0, 10, 50)
y = np.sin(x) * np.exp(-x/10)

def create_sample_chart():
    """Create a sample chart - same code works with any backend"""
    chart = vc.LineChart()
    chart.plot(x, y, label='Damped Sine Wave', color='blue', linewidth=2)
    chart.set_title('Backend Demonstration')
    chart.set_xlabel('X')
    chart.set_ylabel('Y')
    chart.legend()
    chart.grid(True, alpha=0.3)
    return chart

# Create with matplotlib backend (static, high quality)
print("Creating chart with matplotlib backend...")
vc.set_backend('matplotlib')
chart1 = create_sample_chart()
chart1.save('matplotlib_chart.png', dpi=300)
chart1.show()

# Switch to plotly backend (interactive)
print("Creating chart with plotly backend...")
vc.set_backend('plotly')
chart2 = create_sample_chart()
chart2.save('plotly_chart.html')
chart2.show()

# Switch to pure python backend (lightweight)
print("Creating chart with pure backend...")
vc.set_backend('pure')
chart3 = create_sample_chart()
chart3.save('pure_chart.png')
chart3.show()

print("Same code, three different rendering engines!")
```

### Backend Selection Strategy
```python
import vizlychart as vc
import numpy as np

def choose_optimal_backend(data_size, use_case):
    """Choose the best backend based on requirements"""

    if use_case == 'web_interactive':
        return 'plotly'
    elif use_case == 'publication':
        return 'matplotlib'
    elif data_size > 100000:
        return 'pure'  # Fastest for large datasets
    else:
        return 'matplotlib'  # Default for quality

# Example usage
large_data = np.random.randn(200000, 2)
medium_data = np.random.randn(1000, 2)

# For large dataset
optimal_backend = choose_optimal_backend(len(large_data), 'analysis')
print(f"For large dataset: using {optimal_backend} backend")

vc.set_backend(optimal_backend)
chart = vc.ScatterChart()
chart.plot(large_data[:, 0], large_data[:, 1], alpha=0.1, s=1)
chart.set_title(f'Large Dataset Visualization ({optimal_backend} backend)')
chart.show()

# For web deployment
vc.set_backend(choose_optimal_backend(len(medium_data), 'web_interactive'))
web_chart = vc.LineChart()
x = np.arange(len(medium_data))
web_chart.plot(x, np.cumsum(medium_data[:, 0]), label='Cumulative Sum')
web_chart.set_title('Interactive Web Chart')
web_chart.show()
```

## Advanced Styling Examples

### Custom Themes
```python
import vizlychart as vc
import numpy as np

# Create sample data
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)

# Define custom theme
custom_theme = vc.Theme(
    background_color='#1E1E1E',
    grid_color='#333333',
    text_color='#FFFFFF',
    accent_colors=['#00D4FF', '#FF6B35', '#32CD32', '#FFD700'],
    font_family='Arial',
    font_size=11
)

# Apply custom theme
vc.set_theme(custom_theme)

chart = vc.LineChart()
chart.plot(x, y1, label='sin(x)', linewidth=3)
chart.plot(x, y2, label='cos(x)', linewidth=3)
chart.set_title('Custom Dark Theme Example', fontsize=16)
chart.set_xlabel('X Values')
chart.set_ylabel('Y Values')
chart.legend()
chart.grid(True, alpha=0.5)
chart.show()

# Reset to default theme
vc.set_theme('default')
```

### Professional Report Styling
```python
import vizlychart as vc
import numpy as np

# Professional styling for business reports
def apply_professional_style(chart, title):
    """Apply consistent professional styling"""
    chart.set_title(title, fontsize=14, fontweight='bold', pad=20)
    chart.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)

    # Styling for axes
    chart.set_xlabel(chart.get_xlabel(), fontsize=11)
    chart.set_ylabel(chart.get_ylabel(), fontsize=11)

    # Remove top and right spines for cleaner look
    chart.spines['top'].set_visible(False)
    chart.spines['right'].set_visible(False)

    return chart

# Sample business data
quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023']
revenue = [2.1, 2.4, 2.7, 3.1]  # in millions
profit = [0.3, 0.4, 0.5, 0.7]

# Revenue chart
revenue_chart = vc.BarChart()
revenue_chart.plot(quarters, revenue,
                  color='#2E86AB', alpha=0.8,
                  edgecolor='#1B5E83', linewidth=1)

revenue_chart = apply_professional_style(revenue_chart, 'Quarterly Revenue Growth')
revenue_chart.set_ylabel('Revenue ($ Millions)')

# Add value labels on bars
for i, v in enumerate(revenue):
    revenue_chart.text(i, v + 0.05, f'${v}M',
                      ha='center', va='bottom', fontweight='bold')

revenue_chart.show()

# Profit trend
profit_chart = vc.LineChart()
profit_chart.plot(quarters, profit,
                  color='#A23B72', linewidth=3,
                  marker='o', markersize=8, markerfacecolor='white',
                  markeredgecolor='#A23B72', markeredgewidth=2)

profit_chart = apply_professional_style(profit_chart, 'Profit Trend Analysis')
profit_chart.set_ylabel('Profit ($ Millions)')

profit_chart.show()
```

## Performance Examples

### Large Dataset Handling
```python
import vizlychart as vc
import numpy as np
import time

# Generate large dataset
print("Generating large dataset...")
n_points = 1_000_000
x = np.random.randn(n_points)
y = np.random.randn(n_points)

# Performance comparison
backends = ['matplotlib', 'plotly', 'pure']
times = {}

for backend in backends:
    print(f"\nTesting {backend} backend...")

    vc.set_backend(backend)
    start_time = time.time()

    chart = vc.ScatterChart()
    if backend == 'plotly':
        # Sample data for plotly to avoid browser performance issues
        sample_indices = np.random.choice(n_points, 50000, replace=False)
        chart.plot(x[sample_indices], y[sample_indices],
                  alpha=0.1, s=1, rasterized=True)
    else:
        chart.plot(x, y, alpha=0.1, s=1, rasterized=True)

    chart.set_title(f'Large Dataset Visualization - {backend.title()}')
    chart.set_xlabel('X Values')
    chart.set_ylabel('Y Values')

    end_time = time.time()
    times[backend] = end_time - start_time

    print(f"Time taken: {times[backend]:.2f} seconds")
    chart.show()

# Performance summary
print("\nPerformance Summary:")
print("=" * 20)
for backend, time_taken in times.items():
    print(f"{backend}: {time_taken:.2f} seconds")

fastest = min(times, key=times.get)
print(f"\nFastest backend for large data: {fastest}")
```

### Memory Optimization
```python
import vizlychart as vc
import numpy as np
import psutil
import os

def get_memory_usage():
    """Get current memory usage in MB"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024

# Memory usage tracking
initial_memory = get_memory_usage()
print(f"Initial memory usage: {initial_memory:.1f} MB")

# Create multiple charts efficiently
charts = []
for i in range(10):
    # Generate data
    x = np.random.randn(10000)
    y = np.random.randn(10000)

    # Create chart with memory optimization
    chart = vc.ScatterChart(optimize_memory=True)
    chart.plot(x, y, alpha=0.3, s=5)
    chart.set_title(f'Chart {i+1}')

    charts.append(chart)

    # Check memory usage
    current_memory = get_memory_usage()
    print(f"After chart {i+1}: {current_memory:.1f} MB")

# Clean up charts to free memory
print("\nCleaning up charts...")
for chart in charts:
    chart.clear()  # Free chart data

final_memory = get_memory_usage()
print(f"Final memory usage: {final_memory:.1f} MB")
print(f"Memory saved: {current_memory - final_memory:.1f} MB")
```

## Integration Examples

### Jupyter Notebook Integration
```python
# In Jupyter notebooks
import vizlychart as vc
import numpy as np

# Enable inline display
%matplotlib inline

# Create interactive charts that display automatically
chart = vc.LineChart()
x = np.linspace(0, 10, 100)
chart.plot(x, np.sin(x), label='sin(x)')
chart.plot(x, np.cos(x), label='cos(x)')
chart.legend()

# Chart will display automatically in notebook
chart.show()

# For interactive plotly charts in Jupyter
vc.set_backend('plotly')
interactive_chart = vc.ScatterChart()
interactive_chart.plot(np.random.randn(100), np.random.randn(100))
interactive_chart.show()  # Shows interactive plot in notebook
```

### Web Application Integration
```python
# Flask web application example
from flask import Flask, render_template, jsonify
import vizlychart as vc
import numpy as np
import json

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/chart/<chart_type>')
def generate_chart(chart_type):
    # Generate sample data
    x = np.linspace(0, 10, 50)
    y = np.sin(x) + np.random.normal(0, 0.1, 50)

    # Use plotly backend for web
    vc.set_backend('plotly')

    if chart_type == 'line':
        chart = vc.LineChart()
        chart.plot(x, y, name='Data')
    elif chart_type == 'scatter':
        chart = vc.ScatterChart()
        chart.plot(x, y, name='Data')
    else:
        return jsonify({'error': 'Unsupported chart type'})

    chart.set_title(f'{chart_type.title()} Chart')

    # Convert to JSON for web response
    chart_json = chart.to_json()
    return jsonify(chart_json)

if __name__ == '__main__':
    app.run(debug=True)
```

---

These examples demonstrate the full range of VizlyChart capabilities. Each example includes complete, runnable code that you can adapt for your specific use cases.

**Next Steps:**
- [Best Practices](best-practices.md) - Learn optimization techniques
- [Advanced Features](../advanced/) - Explore ML and statistical visualizations
- [API Reference](../api/) - Detailed function documentation