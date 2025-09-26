#!/usr/bin/env python3
"""
Inspect HeatmapChart method source
=================================
"""

import inspect
from vizlychart.charts.advanced_charts import HeatmapChart

print("🔍 Inspecting HeatmapChart.heatmap method...")

chart = HeatmapChart(400, 300)

# Get the heatmap method
heatmap_method = chart.heatmap
print(f"Method: {heatmap_method}")
print(f"Method type: {type(heatmap_method)}")

# Try to get source
try:
    source = inspect.getsource(heatmap_method)
    print(f"\n📝 Method source:\n{source}")
except Exception as e:
    print(f"❌ Could not get source: {e}")

# Check method attributes
print(f"\n🔍 Method attributes:")
print(f"   __func__: {heatmap_method.__func__}")
print(f"   __self__: {heatmap_method.__self__}")

# Check if method is defined in the class
print(f"\n📋 Class method check:")
if 'heatmap' in HeatmapChart.__dict__:
    print("✅ heatmap is in HeatmapChart.__dict__")
    class_method = HeatmapChart.__dict__['heatmap']
    print(f"   Class method: {class_method}")
    try:
        class_source = inspect.getsource(class_method)
        print(f"   Class method source:\n{class_source}")
    except Exception as e:
        print(f"   ❌ Could not get class method source: {e}")
else:
    print("❌ heatmap not in HeatmapChart.__dict__")

# Check parent classes
for cls in HeatmapChart.__mro__[1:]:  # Skip self
    if hasattr(cls, 'heatmap'):
        print(f"⚠️  {cls.__name__} also has heatmap method")
    else:
        print(f"✅ {cls.__name__} doesn't have heatmap method")

print("\n🏁 Method inspection completed!")