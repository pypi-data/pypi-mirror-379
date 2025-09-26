#!/usr/bin/env python3
"""
Debug VizlyChart rendering issues
"""

import numpy as np
import vizlychart as vc

print("🔍 DEBUGGING VizlyChart Rendering Issues")
print("=" * 50)

# Create simple test case
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 3, 5, 1])

print("📊 Creating simple line chart...")

# Test basic chart creation
chart = vc.LineChart(width=400, height=300)
chart.plot(x, y, color='blue', label='Test Data')

print("✅ Chart object created")
print(f"   - Chart has {len(chart.lines)} line(s)")
print(f"   - Renderer type: {type(chart.renderer)}")
print(f"   - Canvas type: {type(chart.renderer.canvas)}")

# Test individual components
print("\n🧪 Testing chart components...")

try:
    chart.set_title("Test Chart")
    print("✅ Title set successfully")
except Exception as e:
    print(f"❌ Title failed: {e}")

try:
    chart.set_labels("X Values", "Y Values")
    print("✅ Labels set successfully")
except Exception as e:
    print(f"❌ Labels failed: {e}")

try:
    chart.add_axes()
    print("✅ Axes added successfully")
except Exception as e:
    print(f"❌ Axes failed: {e}")

try:
    chart.add_legend()
    print("✅ Legend added successfully")
except Exception as e:
    print(f"❌ Legend failed: {e}")

# Get SVG output
print("\n📄 Analyzing SVG output...")
svg_content = chart.renderer.canvas.to_svg()

print(f"SVG length: {len(svg_content)} characters")

# Check what's actually in the SVG
print("\n🔍 SVG content analysis:")
print(f"  - Contains <line> tags: {svg_content.count('<line')}")
print(f"  - Contains <text> tags: {svg_content.count('<text')}")
print(f"  - Contains <rect> tags: {svg_content.count('<rect')}")
print(f"  - Contains 'stroke=' attributes: {svg_content.count('stroke=')}")

# Save and show first 50 lines of SVG
chart.save("debug_chart.svg")

print("\n📋 First 20 lines of SVG:")
svg_lines = svg_content.split('\n')
for i, line in enumerate(svg_lines[:20]):
    print(f"{i+1:2d}: {line}")

print("\n📋 Last 20 lines of SVG:")
for i, line in enumerate(svg_lines[-20:]):
    print(f"{len(svg_lines)-20+i+1:2d}: {line}")

print(f"\n💾 Debug chart saved as: debug_chart.svg")
print("🔍 Please check the SVG file to see what's actually being rendered")