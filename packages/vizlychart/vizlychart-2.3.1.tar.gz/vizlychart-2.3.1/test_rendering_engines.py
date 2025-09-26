#!/usr/bin/env python3
"""
Test script for VizlyChart rendering engines
"""

import numpy as np
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_pure_engine():
    """Test the pure rendering engine"""
    print("🧪 Testing Pure Rendering Engine...")

    from vizlychart.charts.pure_charts import LineChart, ScatterChart, BarChart

    # Test line chart
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    line_chart = LineChart(800, 600)
    line_chart.plot(x, y, color='blue', label='sin(x)')
    line_chart.set_title("Pure Engine Line Chart")
    line_chart.add_axes()
    line_chart.add_grid()
    line_chart.set_labels("X-axis", "Y-axis")
    line_chart.add_legend()

    # Save test
    line_chart.save("test_pure_line.svg")
    print("✅ Pure line chart saved to test_pure_line.svg")

    # Test scatter chart
    x_scatter = np.random.randn(100)
    y_scatter = np.random.randn(100)

    scatter_chart = ScatterChart(800, 600)
    scatter_chart.plot(x_scatter, y_scatter, color='red', size=30, label='Random data')
    scatter_chart.set_title("Pure Engine Scatter Chart")
    scatter_chart.add_axes()
    scatter_chart.add_grid()
    scatter_chart.set_labels("X-axis", "Y-axis")
    scatter_chart.add_legend()

    scatter_chart.save("test_pure_scatter.svg")
    print("✅ Pure scatter chart saved to test_pure_scatter.svg")

    # Test bar chart
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]

    bar_chart = BarChart(800, 600)
    bar_chart.bar(categories, values, color='green', label='Sample data')
    bar_chart.set_title("Pure Engine Bar Chart")
    bar_chart.add_axes()
    bar_chart.set_labels("Categories", "Values")
    bar_chart.add_legend()

    bar_chart.save("test_pure_bar.svg")
    print("✅ Pure bar chart saved to test_pure_bar.svg")

def test_advanced_engine():
    """Test the advanced rendering engine"""
    print("\n🚀 Testing Advanced Rendering Engine...")

    try:
        from vizlychart.rendering.advanced_engine import AdvancedRenderer, ColorHDR, RenderQuality

        # Create renderer
        renderer = AdvancedRenderer(800, 600, quality=RenderQuality.HIGH)

        # Test line plotting
        x = np.linspace(0, 10, 100)
        y = np.sin(x) * np.exp(-x/10)

        color = ColorHDR.from_hex("#3498db")  # Blue
        renderer.set_data_bounds(0, 10, -1, 1)
        renderer.draw_axes_professional(0, 10, -1, 1)
        renderer.plot_line_series(x, y, color, width=2.0, smooth=True)

        # Save test
        renderer.save_svg_professional("test_advanced_line.svg")
        print("✅ Advanced line chart saved to test_advanced_line.svg")

    except ImportError as e:
        print(f"❌ Advanced engine import failed: {e}")
    except Exception as e:
        print(f"❌ Advanced engine test failed: {e}")

def test_integration():
    """Test integration between engines"""
    print("\n🔗 Testing Engine Integration...")

    try:
        # Test if both engines can coexist
        from vizlychart.charts.pure_charts import LineChart
        from vizlychart.rendering.advanced_engine import AdvancedRenderer

        print("✅ Both engines can be imported together")

        # Test basic compatibility
        pure_chart = LineChart()
        advanced_renderer = AdvancedRenderer(800, 600)

        print("✅ Both engines can be instantiated together")

    except Exception as e:
        print(f"❌ Integration test failed: {e}")

def main():
    """Run all rendering tests"""
    print("🎨 VizlyChart Rendering Engine Tests")
    print("=" * 40)

    try:
        test_pure_engine()
        test_advanced_engine()
        test_integration()

        print("\n✨ All rendering tests completed!")
        print("\nGenerated files:")
        print("- test_pure_line.svg")
        print("- test_pure_scatter.svg")
        print("- test_pure_bar.svg")
        print("- test_advanced_line.svg")

    except Exception as e:
        print(f"\n💥 Test suite failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()