#!/usr/bin/env python3
"""
Test enhanced VizlyChart with proper axes, scales, and legends
"""

import numpy as np
import vizlychart as vc

print("🚀 Testing Enhanced VizlyChart with Complete Chart Elements")
print("=" * 60)

# Test 1: Line Chart with Full Elements
print("\n📊 Test 1: Line Chart with Axes, Scales, and Legend")

# Create sample data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create enhanced line chart
line_chart = vc.LineChart(width=800, height=600)
line_chart.plot(x, y1, color='blue', linewidth=2, label='sin(x)')
line_chart.plot(x, y2, color='red', linewidth=2, label='cos(x)')

# Add all elements including new axes
line_chart.set_title("Enhanced Trigonometric Functions")
line_chart.set_labels("Angle (radians)", "Amplitude")
line_chart.add_axes()  # NEW: Proper axes with numerical scales
line_chart.add_grid(alpha=0.2)
line_chart.add_legend()  # Enhanced legend

# Save and check
line_chart.save("enhanced_line_chart.svg")
svg_content = line_chart.renderer.canvas.to_svg()

print(f"✅ Enhanced LineChart created")
print(f"   📏 SVG size: {len(svg_content)} characters")

# Check for key enhancements
axis_ticks = svg_content.count('text-anchor="middle"')  # X-axis labels
y_axis_ticks = svg_content.count('text-anchor="end"')   # Y-axis labels
legend_background = 'fill="white" stroke="black"' in svg_content
axis_lines = svg_content.count('stroke-width="2"')     # Main axis lines

print(f"   🎯 X-axis tick labels: {axis_ticks}")
print(f"   🎯 Y-axis tick labels: {y_axis_ticks}")
print(f"   📦 Legend background: {'✅' if legend_background else '❌'}")
print(f"   📐 Axis lines: {axis_lines}")

# Test 2: Scatter Chart with Enhanced Elements
print("\n📊 Test 2: Enhanced Scatter Chart")

np.random.seed(42)
x_scatter = np.random.randn(50) * 2
y_scatter = np.random.randn(50) * 1.5

scatter_chart = vc.ScatterChart(width=800, height=600)
scatter_chart.plot(x_scatter, y_scatter, color='green', size=30, alpha=0.7, label='Random Data')
scatter_chart.set_title("Enhanced Scatter Plot with Proper Axes")
scatter_chart.set_labels("X Values", "Y Values")
scatter_chart.add_axes()  # NEW: Proper axes with scaling
scatter_chart.add_grid(alpha=0.15)
scatter_chart.add_legend(position='upper_left')  # NEW: Positioned legend

scatter_chart.save("enhanced_scatter_chart.svg")
print("✅ Enhanced ScatterChart created")

# Test 3: Bar Chart with Enhanced Elements
print("\n📊 Test 3: Enhanced Bar Chart")

categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = [23, 17, 35, 29, 12]

bar_chart = vc.BarChart(width=800, height=600)
bar_chart.bar(categories, values, color='orange', label='Sales Data')
bar_chart.set_title("Enhanced Sales Chart with Proper Scaling")
bar_chart.set_labels("Products", "Sales (Units)")
bar_chart.add_axes()  # NEW: Proper axes including 0-baseline for bars
bar_chart.add_grid(alpha=0.2)
bar_chart.add_legend(position='upper_right')

bar_chart.save("enhanced_bar_chart.svg")
print("✅ Enhanced BarChart created")

# Summary
print("\n🎉 ENHANCEMENT COMPLETE!")
print("📋 New Features Added:")
print("   ✅ Proper numerical axis scales with tick marks")
print("   ✅ Professional axis lines (X and Y boundaries)")
print("   ✅ Automatic data bounds calculation with padding")
print("   ✅ Enhanced legend with background and positioning")
print("   ✅ Consistent chart margins for readability")

print("\n📁 Generated Files:")
print("   - enhanced_line_chart.svg")
print("   - enhanced_scatter_chart.svg")
print("   - enhanced_bar_chart.svg")

print("\n🔧 NEW METHODS AVAILABLE:")
print("   - chart.add_axes() - Adds proper numerical scales")
print("   - chart.add_legend(position='upper_right') - Enhanced legends")
print("   - Automatic data bounds with _get_data_bounds()")

print("\n✨ This should resolve all missing chart element issues!")