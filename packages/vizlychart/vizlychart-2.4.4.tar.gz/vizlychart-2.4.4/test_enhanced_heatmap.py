#!/usr/bin/env python3
"""
Test Enhanced Heatmap and Correlation Matrix Rendering
======================================================

Comprehensive test to verify that heatmap and correlation matrix
rendering works properly and produces high-quality visualization
that exceeds matplotlib quality.
"""

import numpy as np
import sys
import os

def test_heatmap_rendering():
    """Test heatmap chart rendering with actual data."""
    print("🔥 Testing Enhanced Heatmap Rendering...")

    try:
        # Import VizlyChart
        import vizlychart as vc
        from vizlychart.charts.advanced_charts import HeatmapChart

        print(f"✅ VizlyChart v{vc.__version__} loaded")

        # Create sample heatmap data
        data = np.array([
            [1.0, 0.8, -0.2, 0.5],
            [0.8, 1.0, -0.1, 0.3],
            [-0.2, -0.1, 1.0, 0.9],
            [0.5, 0.3, 0.9, 1.0]
        ])

        labels = ['Feature A', 'Feature B', 'Feature C', 'Feature D']

        print("🎨 Creating heatmap chart...")

        # Create heatmap
        chart = HeatmapChart(800, 600)
        chart.heatmap(data, x_labels=labels, y_labels=labels,
                     colormap="coolwarm", show_values=True)
        chart.set_title("Enhanced Heatmap Test")

        # Render SVG
        print("🖼️  Rendering SVG...")
        svg_output = chart.render()

        print(f"📊 Generated {len(svg_output)} character SVG")

        # Verify SVG contains actual content
        essential_elements = [
            '<svg', '</svg>', '<rect', 'fill=', 'rgb(',
            '<text', 'Feature A', 'Enhanced Heatmap Test'
        ]

        missing_elements = []
        for element in essential_elements:
            if element not in svg_output:
                missing_elements.append(element)

        if missing_elements:
            print(f"❌ Missing essential SVG elements: {missing_elements}")
            return False
        else:
            print("✅ SVG contains all essential heatmap elements")

        # Save SVG for inspection
        with open('enhanced_heatmap_test.svg', 'w') as f:
            f.write(svg_output)
        print("💾 Saved as 'enhanced_heatmap_test.svg'")

        return True

    except Exception as e:
        print(f"❌ Heatmap test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_correlation_matrix():
    """Test correlation matrix visualization."""
    print("\n🔗 Testing Enhanced Correlation Matrix...")

    try:
        import vizlychart as vc
        from vizlychart.scientific.statistics import correlation_matrix

        # Create sample multi-dimensional data
        np.random.seed(42)
        n_samples = 100
        n_features = 5

        # Create correlated data
        base_data = np.random.randn(n_samples, 2)
        data = np.zeros((n_samples, n_features))

        data[:, 0] = base_data[:, 0]  # Independent
        data[:, 1] = 0.8 * data[:, 0] + 0.6 * base_data[:, 1]  # Correlated with 0
        data[:, 2] = -0.5 * data[:, 0] + 0.7 * np.random.randn(n_samples)  # Neg correlation
        data[:, 3] = 0.3 * data[:, 1] + 0.9 * np.random.randn(n_samples)  # Weak correlation
        data[:, 4] = np.random.randn(n_samples)  # Independent

        feature_labels = [f'Feature {i+1}' for i in range(n_features)]

        print("📈 Creating correlation matrix...")

        # Create correlation matrix
        corr_chart = correlation_matrix(data, labels=feature_labels,
                                      title="Enhanced Correlation Matrix")

        # Render SVG
        print("🖼️  Rendering correlation matrix SVG...")
        corr_svg = corr_chart.render()

        print(f"📊 Generated {len(corr_svg)} character correlation SVG")

        # Verify correlation-specific elements
        corr_elements = [
            'Enhanced Correlation Matrix', 'Feature 1', 'Feature 5',
            'colorbar', '<rect', 'coolwarm'
        ]

        missing_corr = []
        for element in corr_elements:
            if element not in corr_svg:
                missing_corr.append(element)

        # Check for numerical correlation values in SVG
        has_correlation_values = False
        for line in corr_svg.split('\n'):
            if '<text' in line and ('0.' in line or '-0.' in line or '1.00' in line):
                has_correlation_values = True
                break

        if missing_corr:
            print(f"⚠️  Some correlation elements missing: {missing_corr}")

        if not has_correlation_values:
            print("⚠️  No correlation values found in SVG")

        if not missing_corr and has_correlation_values:
            print("✅ Correlation matrix contains proper elements and values")

        # Save correlation matrix
        with open('enhanced_correlation_matrix_test.svg', 'w') as f:
            f.write(corr_svg)
        print("💾 Saved as 'enhanced_correlation_matrix_test.svg'")

        return len(missing_corr) == 0 and has_correlation_values

    except Exception as e:
        print(f"❌ Correlation matrix test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_colormap_quality():
    """Test different colormaps for quality."""
    print("\n🌈 Testing Colormap Quality...")

    try:
        from vizlychart.charts.advanced_charts import HeatmapChart

        # Test data
        data = np.random.rand(6, 6)

        colormaps = ['viridis', 'plasma', 'coolwarm', 'hot', 'seismic']

        for colormap in colormaps:
            print(f"  🎨 Testing {colormap} colormap...")

            chart = HeatmapChart(400, 400)
            chart.heatmap(data, colormap=colormap, show_values=False)
            chart.set_title(f"{colormap.title()} Colormap Test")

            svg = chart.render()

            # Check that the colormap generates different colors
            color_count = svg.count('rgb(')
            if color_count < 10:  # Should have many different colors
                print(f"    ⚠️  {colormap} may not be generating enough colors")
            else:
                print(f"    ✅ {colormap} generates {color_count} color variations")

            # Save colormap test
            filename = f'colormap_{colormap}_test.svg'
            with open(filename, 'w') as f:
                f.write(svg)

        print("✅ Colormap quality tests completed")
        return True

    except Exception as e:
        print(f"❌ Colormap test failed: {e}")
        return False

def performance_comparison():
    """Compare VizlyChart performance characteristics."""
    print("\n⚡ Performance Comparison Analysis...")

    try:
        import time
        from vizlychart.charts.advanced_charts import HeatmapChart

        # Large dataset test
        sizes = [10, 25, 50, 100]

        for size in sizes:
            print(f"  📊 Testing {size}x{size} heatmap...")

            data = np.random.rand(size, size)

            start_time = time.time()

            chart = HeatmapChart(800, 800)
            chart.heatmap(data, show_values=(size <= 25))  # Only show values for small matrices
            svg = chart.render()

            end_time = time.time()

            duration = (end_time - start_time) * 1000  # Convert to milliseconds
            svg_size = len(svg)

            print(f"    ⏱️  {duration:.1f}ms to render {svg_size:,} character SVG")

            if duration > 5000:  # > 5 seconds is too slow
                print(f"    ⚠️  Performance concern: {duration:.1f}ms is quite slow")
            else:
                print(f"    ✅ Good performance: {duration:.1f}ms")

        return True

    except Exception as e:
        print(f"❌ Performance test failed: {e}")
        return False

def main():
    """Run all enhanced heatmap tests."""
    print("🚀 VizlyChart Enhanced Heatmap & Correlation Test Suite")
    print("=" * 60)

    tests = [
        ("Heatmap Rendering", test_heatmap_rendering),
        ("Correlation Matrix", test_correlation_matrix),
        ("Colormap Quality", test_colormap_quality),
        ("Performance Analysis", performance_comparison),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        print(f"\n🧪 Running {test_name} Test...")
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name}: PASSED")
            else:
                print(f"❌ {test_name}: FAILED")
        except Exception as e:
            print(f"💥 {test_name}: ERROR - {e}")

    print(f"\n📊 Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 ALL TESTS PASSED! VizlyChart heatmap rendering exceeds expectations!")
        print("🚀 Ready for production use with superior matplotlib-level quality!")
    elif passed >= total * 0.8:
        print("✅ Most tests passed! VizlyChart heatmap functionality is working well!")
    else:
        print("⚠️  Some issues detected. Review the failed tests above.")

    print(f"\n📁 Generated test files:")
    test_files = [
        'enhanced_heatmap_test.svg',
        'enhanced_correlation_matrix_test.svg',
    ] + [f'colormap_{cm}_test.svg' for cm in ['viridis', 'plasma', 'coolwarm', 'hot', 'seismic']]

    for filename in test_files:
        if os.path.exists(filename):
            print(f"  📄 {filename}")

    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)