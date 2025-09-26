#!/usr/bin/env python3
"""
Direct test of the HeatmapChart render method
============================================
"""

import numpy as np

# Direct import to avoid any confusion
from vizlychart.charts.advanced_charts import HeatmapChart

print("🎨 Testing HeatmapChart directly...")

# Create test data
data = np.array([
    [1.0, 0.8, -0.3],
    [0.8, 1.0, 0.1],
    [-0.3, 0.1, 1.0]
])

labels = ['A', 'B', 'C']

print(f"📊 Data shape: {data.shape}")
print(f"📋 Data:\n{data}")

# Create chart
chart = HeatmapChart(600, 400)
print(f"✅ Chart created: {chart}")

# Call heatmap method
print("🔥 Calling heatmap method...")
chart.heatmap(data, x_labels=labels, y_labels=labels,
              colormap="coolwarm", show_values=True)

# Check if data was stored
if hasattr(chart, '_heatmap_data'):
    print(f"✅ _heatmap_data exists: {chart._heatmap_data.shape}")
    print(f"   Data range: {chart._heatmap_data.min():.2f} to {chart._heatmap_data.max():.2f}")
else:
    print("❌ _heatmap_data not found!")

if hasattr(chart, '_x_labels'):
    print(f"✅ _x_labels: {chart._x_labels}")
else:
    print("❌ _x_labels not found!")

# Set title
chart.set_title("Direct Test Heatmap")

# Render
print("🖼️  Rendering...")
svg = chart.render()

print(f"📊 SVG length: {len(svg)}")

# Check content
if 'heatmap-cells' in svg:
    print("✅ Contains heatmap-cells")
else:
    print("❌ Missing heatmap-cells")

if any(label in svg for label in labels):
    print("✅ Contains labels")
else:
    print("❌ Missing labels")

if 'rgb(' in svg:
    print("✅ Contains colors")
else:
    print("❌ Missing colors")

# Save for inspection
with open('direct_heatmap_test.svg', 'w') as f:
    f.write(svg)

print("💾 Saved as direct_heatmap_test.svg")

# Print first 300 chars for debugging
print(f"\n📝 SVG preview:\n{svg[:300]}...")

print("\n✨ Direct test completed!")