#!/usr/bin/env python3
"""
Step-by-step debug of HeatmapChart
==================================
"""

import numpy as np

# Direct import
from vizlychart.charts.advanced_charts import HeatmapChart

print("🔍 Step-by-step HeatmapChart debug...")

# Create test data
data = np.array([[1.0, 0.5], [0.5, 1.0]])
print(f"📊 Test data: {data}")

# Create chart
chart = HeatmapChart(400, 300)
print(f"✅ Chart created: {chart}")
print(f"   Chart attributes before heatmap: {[attr for attr in dir(chart) if not attr.startswith('__')]}")

# Check if heatmap method exists
if hasattr(chart, 'heatmap'):
    print("✅ heatmap method exists")
    print(f"   Method: {chart.heatmap}")
else:
    print("❌ heatmap method missing!")

# Call heatmap method
print("\n🔥 Calling heatmap method...")
try:
    result = chart.heatmap(data, x_labels=['X1', 'X2'], y_labels=['Y1', 'Y2'])
    print(f"✅ heatmap method returned: {result}")
    print(f"   Return type: {type(result)}")
    print(f"   Same object: {result is chart}")
except Exception as e:
    print(f"❌ heatmap method failed: {e}")
    import traceback
    traceback.print_exc()

# Check attributes after calling heatmap
print(f"\n📋 Chart attributes after heatmap:")
for attr in ['_heatmap_data', '_x_labels', '_y_labels', '_colormap', '_show_values']:
    if hasattr(chart, attr):
        value = getattr(chart, attr)
        print(f"   ✅ {attr}: {value}")
    else:
        print(f"   ❌ {attr}: NOT FOUND")

# Test render method
print(f"\n🖼️  Testing render method...")
if hasattr(chart, 'render'):
    print("✅ render method exists")
    try:
        svg = chart.render()
        print(f"✅ render returned {len(svg)} characters")
        print(f"   Preview: {svg[:100]}...")

        # Check specific content
        if hasattr(chart, '_heatmap_data') and svg.find('No heatmap data') != -1:
            print("   ⚠️  Contains 'No heatmap data' message")
        elif 'rgb(' in svg:
            print("   ✅ Contains RGB colors")
        else:
            print("   ❌ No RGB colors found")

    except Exception as e:
        print(f"❌ render failed: {e}")
        import traceback
        traceback.print_exc()
else:
    print("❌ render method missing!")

print("\n🏁 Step-by-step debug completed!")

# Also check parent class
print(f"\n🔍 Class hierarchy analysis:")
print(f"   MRO: {[cls.__name__ for cls in HeatmapChart.__mro__]}")
print(f"   Parent class: {HeatmapChart.__bases__}")

# Check if parent class has conflicting methods
parent = HeatmapChart.__bases__[0]
if hasattr(parent, 'heatmap'):
    print(f"   ⚠️  Parent {parent.__name__} also has heatmap method!")
else:
    print(f"   ✅ Parent {parent.__name__} doesn't have heatmap method")

if hasattr(parent, 'render'):
    print(f"   ⚠️  Parent {parent.__name__} has render method: {parent.render}")
else:
    print(f"   ✅ Parent {parent.__name__} doesn't have render method")