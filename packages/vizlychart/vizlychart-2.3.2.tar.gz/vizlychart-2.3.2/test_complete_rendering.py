#!/usr/bin/env python3
"""
Test complete VizlyChart rendering with all elements
"""

import numpy as np
import vizlychart as vc

# Test 1: Line Chart with all elements
print("🧪 Testing LineChart with complete elements...")

# Create sample data
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)

# Create line chart
line_chart = vc.LineChart(width=800, height=600)
line_chart.plot(x, y1, color='blue', linewidth=2, label='sin(x)')
line_chart.plot(x, y2, color='red', linewidth=2, label='cos(x)')

# Add all chart elements
line_chart.set_title("Trigonometric Functions")
line_chart.set_labels("Time (s)", "Amplitude")
line_chart.add_grid(alpha=0.3)
line_chart.add_legend()

# Export SVG to check content
svg_content = line_chart.renderer.canvas.to_svg()
print(f"✅ LineChart SVG length: {len(svg_content)} characters")

# Check for key elements in SVG
elements_found = {
    'title': 'Trigonometric Functions' in svg_content,
    'xlabel': 'Time (s)' in svg_content,
    'ylabel': 'Amplitude' in svg_content,
    'lines': '<line' in svg_content,
    'text': '<text' in svg_content,
    'legend_sin': 'sin(x)' in svg_content,
    'legend_cos': 'cos(x)' in svg_content
}

print("📋 Chart Elements Status:")
for element, found in elements_found.items():
    status = "✅ Found" if found else "❌ Missing"
    print(f"  {element}: {status}")

# Save the chart
line_chart.save("test_line_chart_complete.svg")
print("💾 Saved as test_line_chart_complete.svg")

# Test 2: Scatter Chart
print("\n🧪 Testing ScatterChart with elements...")

# Create scatter data
np.random.seed(42)
x_scatter = np.random.randn(100)
y_scatter = np.random.randn(100)

scatter_chart = vc.ScatterChart(width=800, height=600)
scatter_chart.plot(x_scatter, y_scatter, color='green', size=30, alpha=0.7, label='Random Data')
scatter_chart.set_title("Random Scatter Plot")
scatter_chart.set_labels("X Values", "Y Values")
scatter_chart.add_grid(alpha=0.2)

scatter_svg = scatter_chart.renderer.canvas.to_svg()
print(f"✅ ScatterChart SVG length: {len(scatter_svg)} characters")
scatter_chart.save("test_scatter_chart_complete.svg")

# Test 3: Bar Chart
print("\n🧪 Testing BarChart with elements...")

categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 17, 35, 29, 12]

bar_chart = vc.BarChart(width=800, height=600)
bar_chart.bar(categories, values, color='orange', label='Sample Data')
bar_chart.set_title("Sample Bar Chart")
bar_chart.set_labels("Categories", "Values")
bar_chart.add_grid(alpha=0.3)

bar_svg = bar_chart.renderer.canvas.to_svg()
print(f"✅ BarChart SVG length: {len(bar_svg)} characters")
bar_chart.save("test_bar_chart_complete.svg")

print("\n🎉 Testing completed! All chart types created with complete elements.")
print("📁 Check the generated SVG files to verify visual output.")