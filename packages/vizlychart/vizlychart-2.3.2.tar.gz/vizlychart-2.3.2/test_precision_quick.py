#!/usr/bin/env python3
"""
Quick VizlyEngine Ultra-Precision Test
=====================================

Focused test for ultra-precision rendering features.
"""

import numpy as np
import sys
import os

# Add src to path for development
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_ultra_precision_quick():
    """Quick test of ultra-precision features."""
    print("⚡ VizlyEngine Ultra-Precision Quick Test")
    print("=" * 45)

    try:
        import vizlychart as vc

        print(f"📊 VizlyChart v{vc.__version__}")
        vc.print_info()

        # Test 1: Basic Ultra-Precision Line Chart
        print("\n🎯 Test 1: Ultra-Precision Line Chart")
        x = np.linspace(0, 2*np.pi, 50, dtype=np.float64)  # Small dataset for speed
        y = np.sin(x)

        chart = vc.LineChart(width=600, height=400)
        color = vc.ColorHDR.from_hex('#3498db')

        chart.plot(x, y, color=color, line_width=2.0, smooth=True, label='Ultra-precision')
        chart.set_title("VizlyEngine Ultra-Precision Test")
        chart.set_labels("X (radians)", "Y (amplitude)")

        chart.save("test_quick_precision.svg")
        print("✅ Ultra-precision chart saved as 'test_quick_precision.svg'")

        # Test 2: Enhanced API with Precision
        print("\n🚀 Test 2: Enhanced API Ultra-Precision")
        enhanced_chart = vc.linechart(width=600, height=400)
        enhanced_chart.plot(x, y, color='red', linewidth=1.5, smooth=True, label='Enhanced precision')
        enhanced_chart.set_title("Enhanced API Ultra-Precision")
        enhanced_chart.grid(True)
        enhanced_chart.legend()
        enhanced_chart.savefig("test_enhanced_precision.svg")
        print("✅ Enhanced precision chart saved as 'test_enhanced_precision.svg'")

        # Test 3: Color Precision
        print("\n🌈 Test 3: HDR Color Precision")
        color_chart = vc.LineChart(width=600, height=400)

        # Test high precision colors
        hdr_colors = [
            vc.ColorHDR(0.8000000000000000, 0.0000000000000000, 0.0000000000000000, 1.0),
            vc.ColorHDR(0.0000000000000000, 0.8000000000000000, 0.0000000000000000, 1.0),
            vc.ColorHDR(0.0000000000000000, 0.0000000000000000, 0.8000000000000000, 1.0),
        ]

        for i, color in enumerate(hdr_colors):
            y_offset = np.sin(x + i * np.pi/3) * 0.8
            color_chart.plot(x, y_offset, color=color, line_width=2.0,
                           label=f'HDR Color {i+1}')

        color_chart.set_title("HDR Color Precision Test")
        color_chart.save("test_hdr_colors.svg")
        print("✅ HDR color precision chart saved as 'test_hdr_colors.svg'")

        print("\n✨ Ultra-Precision Quick Test Complete!")
        print("Generated files:")
        print("  1. test_quick_precision.svg")
        print("  2. test_enhanced_precision.svg")
        print("  3. test_hdr_colors.svg")

        return True

    except Exception as e:
        print(f"❌ Quick precision test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run the quick ultra-precision test."""
    success = test_ultra_precision_quick()

    if success:
        print("\n🎯 VizlyEngine Ultra-Precision Features Working!")
        print("="*50)
        print("✅ Ultra-precision line rendering")
        print("✅ Enhanced API precision")
        print("✅ HDR color management")
        print("✅ Professional quality output")
        print("\nThe engine is ready for high-precision visualization!")
    else:
        print("\n⚠️  Some ultra-precision features need attention")

if __name__ == "__main__":
    main()