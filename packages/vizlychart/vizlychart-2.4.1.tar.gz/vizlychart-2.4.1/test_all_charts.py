#!/usr/bin/env python3
"""
Comprehensive test of all chart rendering functions
===================================================
"""

import numpy as np
import traceback
from typing import Dict, List, Tuple

# Test all chart types
test_results = []

def test_chart(chart_name: str, chart_class, test_func):
    """Test a chart class and its rendering."""
    try:
        print(f"\n🔍 Testing {chart_name}...")

        # Create chart instance
        chart = chart_class(400, 300)
        print(f"   ✅ Chart instance created: {type(chart)}")

        # Run test function
        test_func(chart)
        print(f"   ✅ Test function executed")

        # Test render method
        if hasattr(chart, 'render'):
            svg_output = chart.render()
            print(f"   ✅ Render method returned: {len(svg_output)} characters")

            # Check if it's actually meaningful output
            if len(svg_output) < 200:
                print(f"   ⚠️  Short output - might be placeholder")
            elif 'No data' in svg_output or 'placeholder' in svg_output.lower():
                print(f"   ❌ Contains placeholder/no data message")
            else:
                print(f"   ✅ Appears to contain real chart data")

            test_results.append((chart_name, "PASS", len(svg_output), None))
        else:
            print(f"   ❌ No render method found!")
            test_results.append((chart_name, "FAIL", 0, "No render method"))

    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        traceback.print_exc()
        test_results.append((chart_name, "ERROR", 0, str(e)))

print("🚀 Starting comprehensive chart testing...")

# Professional Charts
print("\n" + "="*50)
print("PROFESSIONAL CHARTS (VizlyEngine)")
print("="*50)

try:
    from vizlychart.charts.professional_charts import (
        ProfessionalLineChart,
        ProfessionalScatterChart,
        ProfessionalBarChart
    )

    test_chart("ProfessionalLineChart", ProfessionalLineChart,
               lambda chart: chart.line([1, 2, 3], [1, 4, 2]))

    test_chart("ProfessionalScatterChart", ProfessionalScatterChart,
               lambda chart: chart.scatter([1, 2, 3], [1, 4, 2]))

    test_chart("ProfessionalBarChart", ProfessionalBarChart,
               lambda chart: chart.bar(['A', 'B', 'C'], [1, 4, 2]))

except ImportError as e:
    print(f"❌ Could not import professional charts: {e}")

# Enhanced Charts
print("\n" + "="*50)
print("ENHANCED CHARTS (matplotlib-like API)")
print("="*50)

try:
    from vizlychart.charts.enhanced_api import (
        EnhancedLineChart,
        EnhancedScatterChart,
        EnhancedBarChart
    )

    test_chart("EnhancedLineChart", EnhancedLineChart,
               lambda chart: chart.plot([1, 2, 3], [1, 4, 2]))

    test_chart("EnhancedScatterChart", EnhancedScatterChart,
               lambda chart: chart.plot([1, 2, 3], [1, 4, 2]))

    test_chart("EnhancedBarChart", EnhancedBarChart,
               lambda chart: chart.plot([1, 4, 2]))

except ImportError as e:
    print(f"❌ Could not import enhanced charts: {e}")

# Advanced Charts
print("\n" + "="*50)
print("ADVANCED CHARTS")
print("="*50)

# Test both HeatmapChart versions
try:
    from vizlychart.charts.advanced import HeatmapChart as OldHeatmapChart

    test_chart("HeatmapChart (advanced.py)", OldHeatmapChart,
               lambda chart: chart.heatmap(np.array([[1.0, 0.5], [0.5, 1.0]])))

except ImportError as e:
    print(f"❌ Could not import old HeatmapChart: {e}")

try:
    from vizlychart.charts.advanced_charts import HeatmapChart as NewHeatmapChart

    test_chart("HeatmapChart (advanced_charts.py)", NewHeatmapChart,
               lambda chart: chart.heatmap(np.array([[1.0, 0.5], [0.5, 1.0]])))

except ImportError as e:
    print(f"❌ Could not import new HeatmapChart: {e}")

# Test other advanced charts
try:
    from vizlychart.charts.advanced import (
        ViolinChart,
        RadarChart,
        TreemapChart,
        SankeyChart,
        SpectrogramChart,
        ClusterChart,
        ParallelCoordinatesChart,
        ConvexHullChart
    )

    test_chart("ViolinChart", ViolinChart,
               lambda chart: chart.plot([np.random.normal(0, 1, 100), np.random.normal(1, 1, 100)]))

    test_chart("RadarChart", RadarChart,
               lambda chart: chart.plot(np.array([0.8, 0.6, 0.7, 0.9]), ['A', 'B', 'C', 'D']))

    test_chart("TreemapChart", TreemapChart,
               lambda chart: chart.plot([10, 20, 30], ['A', 'B', 'C']))

    test_chart("SankeyChart", SankeyChart,
               lambda chart: chart.plot([('A', 'B', 10), ('A', 'C', 5), ('B', 'D', 8)]))

    # Spectrogram needs a longer signal
    signal = np.sin(2 * np.pi * 50 * np.linspace(0, 1, 1000))
    test_chart("SpectrogramChart", SpectrogramChart,
               lambda chart: chart.plot(signal, 1000))

    # Cluster chart needs 2D data
    cluster_data = np.random.randn(100, 2)
    test_chart("ClusterChart", ClusterChart,
               lambda chart: chart.plot(cluster_data))

    # Parallel coordinates needs multi-dimensional data
    parallel_data = np.random.randn(50, 4)
    test_chart("ParallelCoordinatesChart", ParallelCoordinatesChart,
               lambda chart: chart.plot(parallel_data))

    # Convex hull needs 2D points
    hull_points = np.random.randn(20, 2)
    test_chart("ConvexHullChart", ConvexHullChart,
               lambda chart: chart.plot(hull_points))

except ImportError as e:
    print(f"❌ Could not import some advanced charts: {e}")

# Financial Charts
print("\n" + "="*50)
print("FINANCIAL CHARTS")
print("="*50)

try:
    from vizlychart.charts.financial import (
        CandlestickChart,
        OHLCChart,
        VolumeProfileChart,
        RSIChart,
        MACDChart,
        PointAndFigureChart
    )

    # Financial data needs OHLC format
    ohlc_data = np.array([
        [100, 105, 98, 103],  # Open, High, Low, Close
        [103, 108, 102, 107],
        [107, 110, 105, 108]
    ])

    dates = [f"2023-01-{i+1:02d}" for i in range(len(ohlc_data))]  # Date strings
    test_chart("CandlestickChart", CandlestickChart,
               lambda chart: chart.plot(dates, ohlc_data[:, 0], ohlc_data[:, 1], ohlc_data[:, 2], ohlc_data[:, 3]))

    test_chart("OHLCChart", OHLCChart,
               lambda chart: chart.plot(dates, ohlc_data[:, 0], ohlc_data[:, 1], ohlc_data[:, 2], ohlc_data[:, 3]))

    volumes = np.array([1000, 1500, 1200])
    test_chart("VolumeProfileChart", VolumeProfileChart,
               lambda chart: chart.plot(np.array([100, 103, 107]), volumes))

    # Generate more data for MACD (needs at least 26 points for default periods)
    prices = np.array([100 + i + np.random.normal(0, 2) for i in range(30)])  # 30 price points
    dates = [f"2023-01-{i+1:02d}" for i in range(len(prices))]  # Simple date strings
    test_chart("RSIChart", RSIChart,
               lambda chart: chart.plot(dates, prices))

    test_chart("MACDChart", MACDChart,
               lambda chart: chart.plot(dates, prices))

    test_chart("PointAndFigureChart", PointAndFigureChart,
               lambda chart: chart.plot(prices))

except ImportError as e:
    print(f"❌ Could not import financial charts: {e}")

# Engineering Charts
print("\n" + "="*50)
print("ENGINEERING CHARTS")
print("="*50)

try:
    from vizlychart.charts.engineering import (
        BodePlot,
        StressStrainChart,
        PhaseDiagram,
        ContourChart
    )

    frequencies = np.logspace(0, 3, 100)  # 1 Hz to 1 kHz
    magnitude = 20 * np.log10(1 / np.sqrt(1 + frequencies**2))
    phase = -np.arctan(frequencies) * 180 / np.pi

    test_chart("BodePlot", BodePlot,
               lambda chart: chart.plot(frequencies, magnitude, phase))

    strain = np.linspace(0, 0.1, 100)
    stress = 200e9 * strain + 1e9 * strain**2  # Young's modulus + nonlinear

    test_chart("StressStrainChart", StressStrainChart,
               lambda chart: chart.plot(strain, stress))

    # Phase diagram needs temperature and composition data
    temperature = np.linspace(0, 1000, 50)
    composition = np.linspace(0, 1, 50)
    T, C = np.meshgrid(temperature, composition)
    phase_field = T + 100 * C

    test_chart("PhaseDiagram", PhaseDiagram,
               lambda chart: chart.plot(temperature, composition, phase_field))

    # Contour chart needs 2D data
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2

    test_chart("ContourChart", ContourChart,
               lambda chart: chart.plot(X, Y, Z))

except ImportError as e:
    print(f"❌ Could not import engineering charts: {e}")

# Data Science Charts
print("\n" + "="*50)
print("DATA SCIENCE CHARTS")
print("="*50)

try:
    from vizlychart.charts.datascience import (
        DistributionChart,
        CorrelationChart,
        RegressionChart
    )

    data = np.random.normal(0, 1, 1000)
    test_chart("DistributionChart", DistributionChart,
               lambda chart: chart.plot_distribution(data))

    # Correlation chart needs correlation matrix
    corr_data = np.random.randn(100, 5)
    corr_matrix = np.corrcoef(corr_data.T)

    test_chart("CorrelationChart", CorrelationChart,
               lambda chart: chart.plot_correlation_matrix(corr_data))

    # Regression chart needs X and y
    X = np.random.randn(100)  # 1D vector
    y = 2 * X + np.random.randn(100)

    test_chart("RegressionChart", RegressionChart,
               lambda chart: chart.plot(X, y))

except ImportError as e:
    print(f"❌ Could not import data science charts: {e}")

# Basic Charts
print("\n" + "="*50)
print("BASIC CHARTS")
print("="*50)

try:
    from vizlychart.charts.histogram import HistogramChart
    from vizlychart.charts.box import BoxChart

    hist_data = np.random.normal(0, 1, 1000)
    test_chart("HistogramChart", HistogramChart,
               lambda chart: chart.hist(hist_data))

    box_data = [np.random.normal(i, 1, 100) for i in range(3)]
    test_chart("BoxChart", BoxChart,
               lambda chart: chart.boxplot(box_data))

except ImportError as e:
    print(f"❌ Could not import basic charts: {e}")

# Surface Charts
print("\n" + "="*50)
print("3D CHARTS")
print("="*50)

try:
    from vizlychart.charts.surface import SurfaceChart

    x = np.linspace(-5, 5, 30)
    y = np.linspace(-5, 5, 30)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2

    test_chart("SurfaceChart", SurfaceChart,
               lambda chart: chart.plot(X, Y, Z))

except ImportError as e:
    print(f"❌ Could not import surface chart: {e}")

# Print Summary
print("\n" + "="*60)
print("FINAL SUMMARY")
print("="*60)

total_tests = len(test_results)
passed = len([r for r in test_results if r[1] == "PASS"])
failed = len([r for r in test_results if r[1] == "FAIL"])
errors = len([r for r in test_results if r[1] == "ERROR"])

print(f"📊 Total Charts Tested: {total_tests}")
print(f"✅ Passed: {passed}")
print(f"❌ Failed: {failed}")
print(f"💥 Errors: {errors}")
print(f"🎯 Success Rate: {passed/total_tests*100:.1f}%")

print(f"\n📋 Detailed Results:")
for chart_name, status, output_length, error in test_results:
    status_icon = "✅" if status == "PASS" else "❌" if status == "FAIL" else "💥"
    print(f"   {status_icon} {chart_name:<30} {status:<6} ({output_length} chars)")
    if error:
        print(f"      └─ {error}")

# Identify problem charts
problem_charts = [r for r in test_results if r[1] != "PASS"]
if problem_charts:
    print(f"\n🔧 Charts needing attention:")
    for chart_name, status, _, error in problem_charts:
        print(f"   • {chart_name}: {status}")
        if error:
            print(f"     └─ {error}")

print(f"\n🏁 Chart testing completed!")