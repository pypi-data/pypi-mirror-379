#!/usr/bin/env python3
"""
Test Core VizlyChart Functionality
==================================

Test the core features that users expect to work without GPU dependencies.
"""

import sys
import os
import traceback
import numpy as np

# Add the source directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_basic_import():
    """Test basic import functionality."""
    print("🧪 Testing Basic Import...")
    try:
        import vizlychart as vc
        print(f"  ✅ VizlyChart v{vc.__version__} imported successfully")
        return True
    except Exception as e:
        print(f"  ❌ Import failed: {e}")
        traceback.print_exc()
        return False

def test_professional_charts():
    """Test professional chart creation."""
    print("🧪 Testing Professional Charts...")
    try:
        from vizlychart.charts.professional_charts import ProfessionalLineChart, ProfessionalScatterChart, ProfessionalBarChart

        # Test LineChart
        line_chart = ProfessionalLineChart(800, 600)
        print("  ✅ ProfessionalLineChart created")

        # Test ScatterChart
        scatter_chart = ProfessionalScatterChart(800, 600)
        print("  ✅ ProfessionalScatterChart created")

        # Test BarChart
        bar_chart = ProfessionalBarChart(800, 600)
        print("  ✅ ProfessionalBarChart created")

        return True
    except Exception as e:
        print(f"  ❌ Professional charts failed: {e}")
        traceback.print_exc()
        return False

def test_advanced_charts():
    """Test advanced chart types."""
    print("🧪 Testing Advanced Chart Types...")
    try:
        from vizlychart.charts.advanced_charts import ContourChart, HeatmapChart, BoxPlot, ViolinPlot

        # Test ContourChart
        contour = ContourChart(800, 600)
        print("  ✅ ContourChart created")

        # Test HeatmapChart
        heatmap = HeatmapChart(800, 600)
        print("  ✅ HeatmapChart created")

        # Test BoxPlot
        box_plot = BoxPlot(800, 600)
        print("  ✅ BoxPlot created")

        # Test ViolinPlot
        violin_plot = ViolinPlot(800, 600)
        print("  ✅ ViolinPlot created")

        return True
    except Exception as e:
        print(f"  ❌ Advanced charts failed: {e}")
        traceback.print_exc()
        return False

def test_3d_charts():
    """Test 3D chart functionality."""
    print("🧪 Testing 3D Charts...")
    try:
        from vizlychart.charts.chart_3d import Chart3D, Surface3D, Scatter3D, Line3D

        # Test Chart3D
        chart_3d = Chart3D(800, 600)
        print("  ✅ Chart3D created")

        # Test Surface3D
        surface_3d = Surface3D(800, 600)
        print("  ✅ Surface3D created")

        # Test Scatter3D
        scatter_3d = Scatter3D(800, 600)
        print("  ✅ Scatter3D created")

        # Test Line3D
        line_3d = Line3D(800, 600)
        print("  ✅ Line3D created")

        return True
    except Exception as e:
        print(f"  ❌ 3D charts failed: {e}")
        traceback.print_exc()
        return False

def test_scientific_visualization():
    """Test scientific visualization functions."""
    print("🧪 Testing Scientific Visualization...")
    try:
        from vizlychart.scientific.statistics import qqplot, residual_plot, correlation_matrix, pca_plot

        # Generate test data
        data = np.random.normal(0, 1, 100)

        # Test Q-Q plot
        qq_chart = qqplot(data, title="Test Q-Q Plot")
        print("  ✅ Q-Q plot created")

        # Test residual plot
        y_true = np.random.normal(0, 1, 50)
        y_pred = y_true + np.random.normal(0, 0.1, 50)
        residual_chart = residual_plot(y_true, y_pred, title="Test Residual Plot")
        print("  ✅ Residual plot created")

        # Test correlation matrix
        matrix_data = np.random.multivariate_normal([0, 0, 0], [[1, 0.5, 0.2], [0.5, 1, 0.3], [0.2, 0.3, 1]], 50)
        corr_chart = correlation_matrix(matrix_data, labels=['A', 'B', 'C'])
        print("  ✅ Correlation matrix created")

        # Test PCA plot
        pca_data = np.random.multivariate_normal([0, 0, 0, 0], np.eye(4), 100)
        labels = np.random.choice(['X', 'Y', 'Z'], 100)
        pca_chart = pca_plot(pca_data, labels=labels, title="Test PCA")
        print("  ✅ PCA plot created")

        return True
    except Exception as e:
        print(f"  ❌ Scientific visualization failed: {e}")
        traceback.print_exc()
        return False

def test_pandas_integration():
    """Test pandas integration if available."""
    print("🧪 Testing Pandas Integration...")
    try:
        import pandas as pd
        from vizlychart.integrations.pandas_integration import DataFramePlotter

        # Create test DataFrame
        df = pd.DataFrame({
            'x': np.linspace(0, 10, 50),
            'y': np.sin(np.linspace(0, 10, 50)) + np.random.normal(0, 0.1, 50),
            'category': np.random.choice(['A', 'B', 'C'], 50)
        })

        # Test DataFrame plotter
        plotter = DataFramePlotter(df)
        line_chart = plotter.line('x', 'y', title="Test DataFrame Line Plot")
        print("  ✅ Pandas DataFrame integration working")

        return True
    except ImportError:
        print("  ⚠️  Pandas not available, skipping pandas tests")
        return True
    except Exception as e:
        print(f"  ❌ Pandas integration failed: {e}")
        traceback.print_exc()
        return False

def test_rendering_and_export():
    """Test chart rendering and export functionality."""
    print("🧪 Testing Rendering and Export...")
    try:
        from vizlychart.charts.professional_charts import ProfessionalLineChart

        # Create a simple chart
        chart = ProfessionalLineChart(800, 600)

        # Test rendering
        svg_content = chart.render()
        print("  ✅ Chart rendering works")

        # Test SVG export
        chart.save_svg("test_chart.svg")
        print("  ✅ SVG export works")

        # Test to_svg method
        svg_str = chart.to_svg()
        print("  ✅ to_svg method works")

        return True
    except Exception as e:
        print(f"  ❌ Rendering and export failed: {e}")
        traceback.print_exc()
        return False

def test_animation_system():
    """Test animation functionality."""
    print("🧪 Testing Animation System...")
    try:
        from vizlychart.animation.animation_core import Animation, AnimationFrame
        from vizlychart.charts.professional_charts import ProfessionalLineChart

        # Create base chart
        chart = ProfessionalLineChart(800, 600)

        # Create animation
        animation = Animation(chart)

        # Add test frame
        frame_data = {'title': 'Test Frame', 'x_data': [1, 2, 3], 'y_data': [1, 4, 9]}
        animation.add_frame(frame_data, duration=1.0)
        print("  ✅ Animation system works")

        return True
    except Exception as e:
        print(f"  ❌ Animation system failed: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all core functionality tests."""
    print("🧪 VizlyChart Core Functionality Test Suite")
    print("=" * 60)

    tests = [
        ("Basic Import", test_basic_import),
        ("Professional Charts", test_professional_charts),
        ("Advanced Charts", test_advanced_charts),
        ("3D Charts", test_3d_charts),
        ("Scientific Visualization", test_scientific_visualization),
        ("Pandas Integration", test_pandas_integration),
        ("Rendering and Export", test_rendering_and_export),
        ("Animation System", test_animation_system),
    ]

    results = {}
    for name, test_func in tests:
        print(f"\n{name}:")
        try:
            result = test_func()
            results[name] = result
        except Exception as e:
            print(f"  ❌ Test failed with exception: {e}")
            results[name] = False

    # Summary
    passed_tests = sum(results.values())
    total_tests = len(results)

    print(f"\n📊 Test Summary:")
    print(f"   Passed: {passed_tests}/{total_tests}")
    print(f"   Success Rate: {passed_tests/total_tests*100:.1f}%")

    if passed_tests == total_tests:
        print(f"\n🎉 ALL TESTS PASSED! VizlyChart core functionality is working.")
    else:
        print(f"\n⚠️  Some tests failed. Please check the errors above.")

    return passed_tests == total_tests

if __name__ == "__main__":
    main()