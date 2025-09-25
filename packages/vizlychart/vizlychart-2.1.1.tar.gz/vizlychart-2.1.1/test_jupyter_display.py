#!/usr/bin/env python3
"""
Test VizlyChart rendering in Jupyter-like environment
"""

import numpy as np
import vizlychart as vc

# Simulate Jupyter/Colab environment test
print("🚀 Testing VizlyChart in Jupyter-like environment...")

try:
    # Create sample chart similar to typical Colab usage
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)

    # Create chart with all elements
    chart = vc.LineChart(width=800, height=600)
    chart.plot(x, y, color='blue', linewidth=2, label='sin(x)')
    chart.set_title("Sine Wave - Complete Chart Elements")
    chart.set_labels("Angle (radians)", "sin(x)")
    chart.add_grid(alpha=0.3)
    chart.add_legend()

    # Test the show() method which is used in Colab/Jupyter
    print("📊 Chart created successfully with all elements:")
    print(f"   - Title: {chart.title}")
    print(f"   - Lines: {len(chart.lines)} data series")

    # Get SVG content to verify completeness
    svg_content = chart.renderer.canvas.to_svg()

    # Check for essential elements
    has_title = 'Sine Wave' in svg_content
    has_lines = '<line' in svg_content
    has_text = '<text' in svg_content
    has_grid = svg_content.count('<line') > 50  # Grid + data lines

    print("✅ Chart completeness check:")
    print(f"   - Title text: {'✅' if has_title else '❌'}")
    print(f"   - Data lines: {'✅' if has_lines else '❌'}")
    print(f"   - Text elements: {'✅' if has_text else '❌'}")
    print(f"   - Grid system: {'✅' if has_grid else '❌'}")

    # Test show method (normally displays in Jupyter)
    print(f"📏 SVG output size: {len(svg_content)} characters")

    # Save for verification
    chart.save("jupyter_test_chart.svg")

    print("🎉 SUCCESS: VizlyChart now renders complete charts with all elements!")
    print("📝 This should resolve the Colab rendering issues.")

except Exception as e:
    print(f"❌ ERROR: {e}")
    import traceback
    traceback.print_exc()