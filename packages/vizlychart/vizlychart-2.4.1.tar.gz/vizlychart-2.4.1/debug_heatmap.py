#!/usr/bin/env python3
"""
Debug Heatmap Import Issue
==========================
"""

import numpy as np

print("🔍 Debugging HeatmapChart import...")

# Test 1: Direct import from advanced_charts
print("\n1️⃣ Direct import from advanced_charts:")
try:
    from vizlychart.charts.advanced_charts import HeatmapChart as HeatmapAdvanced
    print(f"✅ Successfully imported: {HeatmapAdvanced}")
    print(f"   Module: {HeatmapAdvanced.__module__}")
    print(f"   MRO: {[cls.__name__ for cls in HeatmapAdvanced.__mro__]}")

    # Test the render method
    chart = HeatmapAdvanced(400, 300)
    data = np.array([[1, 2], [3, 4]])
    chart.heatmap(data, show_values=True)
    svg = chart.render()
    print(f"   Render result: {len(svg)} chars")
    print(f"   Has data: {'Feature A' in svg or 'heatmap-cells' in svg}")

except Exception as e:
    print(f"❌ Failed: {e}")

# Test 2: Import from vizlychart main module
print("\n2️⃣ Import from main vizlychart module:")
try:
    import vizlychart as vc
    print(f"✅ VizlyChart loaded: {vc.__version__}")

    # Check which HeatmapChart is imported
    heatmap_class = vc.HeatmapChart
    print(f"   HeatmapChart class: {heatmap_class}")
    print(f"   Module: {heatmap_class.__module__}")
    print(f"   MRO: {[cls.__name__ for cls in heatmap_class.__mro__]}")

    # Test render
    chart = heatmap_class(400, 300)
    data = np.array([[1, 2], [3, 4]])

    if hasattr(chart, 'heatmap'):
        print("   ✅ Has heatmap method")
        chart.heatmap(data, show_values=True)
    else:
        print("   ❌ No heatmap method")

    svg = chart.render()
    print(f"   Render result: {len(svg)} chars")
    if len(svg) < 500:
        print(f"   Content preview: {svg[:200]}...")

    # Check if it has _heatmap_data attribute
    if hasattr(chart, '_heatmap_data'):
        print("   ✅ Has _heatmap_data")
    else:
        print("   ❌ No _heatmap_data attribute")

except Exception as e:
    print(f"❌ Failed: {e}")
    import traceback
    traceback.print_exc()

# Test 3: Import from scientific.statistics
print("\n3️⃣ Import via correlation_matrix function:")
try:
    from vizlychart.scientific.statistics import correlation_matrix

    data = np.random.rand(10, 4)
    labels = ['A', 'B', 'C', 'D']

    chart = correlation_matrix(data, labels=labels)
    print(f"✅ Correlation chart created: {chart}")
    print(f"   Class: {chart.__class__}")
    print(f"   Module: {chart.__class__.__module__}")

    svg = chart.render()
    print(f"   Render result: {len(svg)} chars")
    print(f"   Has labels: {'A' in svg or 'B' in svg}")

    # Save for inspection
    with open('debug_correlation.svg', 'w') as f:
        f.write(svg)
    print("   💾 Saved as debug_correlation.svg")

except Exception as e:
    print(f"❌ Failed: {e}")
    import traceback
    traceback.print_exc()

print("\n🏁 Debug completed!")