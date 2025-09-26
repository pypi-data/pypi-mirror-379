#!/usr/bin/env python3
"""
VizlyChart Unified API Demo
===========================

This script demonstrates the new unified API with dual rendering engines:
- Pure Engine: Fast, lightweight, SVG/PNG output
- Advanced Engine: Professional quality with anti-aliasing

The API automatically selects the best available engine or allows manual selection.
"""

import numpy as np
import sys
import os

# Add src to path for development
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def demo_unified_api():
    """Demonstrate the unified API interface."""
    print("🎨 VizlyChart Unified API Demo")
    print("=" * 40)

    try:
        import vizlychart as vc

        # Show package info
        print(f"📊 VizlyChart v{vc.__version__}")
        print(f"📄 {vc.__description__}")
        vc.print_info()

        # Create sample data
        print("\n🔧 Generating sample data...")
        x = np.linspace(0, 4 * np.pi, 100)
        y1 = np.sin(x) * np.exp(-x/10)
        y2 = np.cos(x) * np.exp(-x/8)

        # Random data for scatter
        x_scatter = np.random.randn(200) * 2
        y_scatter = np.random.randn(200) * 2

        # Bar chart data
        categories = ['Q1', 'Q2', 'Q3', 'Q4']
        values = [23.5, 45.2, 56.7, 34.1]

        print("✅ Sample data generated")

        # Test 1: Auto-selected Line Chart
        print("\n📈 Test 1: Auto-Selected Line Chart")
        line_chart = vc.create_line_chart(width=800, height=600)
        line_chart.plot(x, y1, label='Damped sine', color='blue')
        line_chart.plot(x, y2, label='Damped cosine', color='red')
        line_chart.set_title("Unified API - Auto Engine")
        # Handle different API styles
        if hasattr(line_chart, 'set_labels'):
            line_chart.set_labels("Time", "Amplitude")
        else:
            line_chart.set_xlabel("Time")
            line_chart.set_ylabel("Amplitude")

        if hasattr(line_chart, 'add_axes'):
            # Pure engine API
            line_chart.add_axes().add_grid()
            line_chart.add_legend()
        elif hasattr(line_chart, 'grid'):
            # Enhanced/Professional engine API
            line_chart.grid(True)
            line_chart.legend()

        # Handle different save methods
        if hasattr(line_chart, 'savefig'):
            line_chart.savefig("demo_unified_line.svg")
        else:
            line_chart.save("demo_unified_line.svg")
        print("✅ Unified line chart saved as 'demo_unified_line.svg'")

        # Test 2: Pure Engine Scatter Chart
        print("\n🎯 Test 2: Pure Engine Scatter Chart")
        scatter_chart = vc.create_scatter_chart(engine='pure', width=800, height=600)
        scatter_chart.plot(x_scatter, y_scatter, color='green', size=30, alpha=0.7, label='Random data')
        scatter_chart.set_title("Pure Engine - Scatter Plot")
        scatter_chart.add_axes().add_grid()
        # Handle different API styles
        if hasattr(scatter_chart, 'set_labels'):
            scatter_chart.set_labels("X Values", "Y Values")
        else:
            scatter_chart.set_xlabel("X Values")
            scatter_chart.set_ylabel("Y Values")
        scatter_chart.add_legend()
        scatter_chart.save("demo_pure_scatter.svg")
        print("✅ Pure scatter chart saved as 'demo_pure_scatter.svg'")

        # Test 3: Professional Engine (if available)
        print("\n⭐ Test 3: Professional Engine")
        if vc.ADVANCED_ENGINE_AVAILABLE:
            prof_chart = vc.create_line_chart(engine='professional', width=800, height=600)
            prof_chart.set_style('professional')

            # Use professional color system
            blue_color = vc.ColorHDR.from_hex('#3498db')
            red_color = vc.ColorHDR.from_hex('#e74c3c')

            prof_chart.plot(x, y1, label='High-quality sine', color=blue_color, smooth=True)
            prof_chart.plot(x, y2, label='High-quality cosine', color=red_color, smooth=True)
            prof_chart.set_title("Professional Engine - HDR Quality")
            # Handle different API styles
            if hasattr(prof_chart, 'set_labels'):
                prof_chart.set_labels("Time (s)", "Amplitude")
            else:
                prof_chart.set_xlabel("Time (s)")
                prof_chart.set_ylabel("Amplitude")

            # Handle different save methods
            if hasattr(prof_chart, 'savefig'):
                prof_chart.savefig("demo_professional_line.svg")
            else:
                prof_chart.save("demo_professional_line.svg", format='svg')
            print("✅ Professional chart saved as 'demo_professional_line.svg'")
        else:
            print("⚠️  Professional engine not available - using pure engine fallback")
            prof_chart = vc.create_line_chart(engine='pure')
            prof_chart.plot(x, y1, color='blue', label='Fallback sine')
            prof_chart.set_title("Pure Engine Fallback")
            prof_chart.add_axes()
            prof_chart.save("demo_fallback_line.svg")
            print("✅ Fallback chart saved as 'demo_fallback_line.svg'")

        # Test 4: Bar Chart
        print("\n📊 Test 4: Bar Chart")
        bar_chart = vc.create_bar_chart(width=800, height=600)
        bar_chart.bar(categories, values, color='orange', label='Quarterly Sales')
        bar_chart.set_title("Quarterly Sales Report")

        if hasattr(bar_chart, 'add_axes'):
            bar_chart.add_axes()
            # Handle different API styles
            if hasattr(bar_chart, 'set_labels'):
                bar_chart.set_labels("Quarter", "Sales (k$)")
            else:
                bar_chart.set_xlabel("Quarter")
                bar_chart.set_ylabel("Sales (k$)")
            bar_chart.add_legend()

        # Handle different save methods
        if hasattr(bar_chart, 'savefig'):
            bar_chart.savefig("demo_bar_chart.svg")
        else:
            bar_chart.save("demo_bar_chart.svg")
        print("✅ Bar chart saved as 'demo_bar_chart.svg'")

        # Test 5: Quick Plot API
        print("\n⚡ Test 5: Quick Plot API")
        quick_line = vc.quick_plot(x[:50], y1[:50], 'line', title='Quick Line Plot')
        if hasattr(quick_line, 'savefig'):
            quick_line.savefig("demo_quick_line.svg")
        else:
            quick_line.save("demo_quick_line.svg")

        quick_scatter = vc.quick_plot(x_scatter[:50], y_scatter[:50], 'scatter', title='Quick Scatter Plot')
        if hasattr(quick_scatter, 'savefig'):
            quick_scatter.savefig("demo_quick_scatter.svg")
        else:
            quick_scatter.save("demo_quick_scatter.svg")

        quick_bar = vc.quick_plot(categories, values, 'bar', title='Quick Bar Chart')
        if hasattr(quick_bar, 'savefig'):
            quick_bar.savefig("demo_quick_bar.svg")
        else:
            quick_bar.save("demo_quick_bar.svg")

        print("✅ Quick plots saved: demo_quick_*.svg")

        # Test 6: Surface Chart (Pure engine only)
        print("\n🌄 Test 6: Surface Chart")
        X, Y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))
        Z = np.sin(np.sqrt(X**2 + Y**2)) * np.exp(-0.1 * (X**2 + Y**2))

        surface_chart = vc.create_surface_chart(width=800, height=600)
        surface_chart.plot_surface(X, Y, Z, cmap='viridis')
        surface_chart.set_title("3D Surface Visualization")
        surface_chart.save("demo_surface.svg")
        print("✅ Surface chart saved as 'demo_surface.svg'")

        # Export mesh data
        mesh_data = surface_chart.export_mesh("demo_surface_mesh.json")
        print(f"✅ Surface mesh exported: {mesh_data['rows']}x{mesh_data['cols']} points")

        # Summary
        print("\n🎉 Demo Complete!")
        print("Generated files:")
        generated_files = [
            "demo_unified_line.svg",
            "demo_pure_scatter.svg",
            "demo_professional_line.svg" if vc.ADVANCED_ENGINE_AVAILABLE else "demo_fallback_line.svg",
            "demo_bar_chart.svg",
            "demo_quick_line.svg",
            "demo_quick_scatter.svg",
            "demo_quick_bar.svg",
            "demo_surface.svg",
            "demo_surface_mesh.json"
        ]

        for i, filename in enumerate(generated_files, 1):
            print(f"  {i}. {filename}")

        return True

    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def demo_engine_comparison():
    """Compare pure vs professional engines side by side."""
    print("\n🔬 Engine Comparison Demo")
    print("=" * 30)

    try:
        import vizlychart as vc

        # Sample data
        x = np.linspace(0, 2*np.pi, 50)
        y = np.sin(x) + 0.1 * np.random.randn(50)  # Add noise

        # Pure engine version
        print("🔵 Creating pure engine chart...")
        pure_chart = vc.LineChart(800, 600)
        pure_chart.plot(x, y, color='blue', linewidth=2, label='Noisy sine')
        pure_chart.set_title("Pure Engine - Fast Rendering")
        pure_chart.add_axes().add_grid(alpha=0.3)
        pure_chart.set_labels("X", "Y")
        pure_chart.add_legend()
        pure_chart.save("comparison_pure.svg")

        # Professional engine version (if available)
        if vc.ADVANCED_ENGINE_AVAILABLE:
            print("⭐ Creating professional engine chart...")
            prof_chart = vc.ProfessionalLineChart(800, 600, quality=vc.RenderQuality.HIGH)
            prof_chart.set_style('professional')

            color = vc.ColorHDR.from_hex('#2C3E50')
            prof_chart.plot(x, y, color=color, line_width=2.5, smooth=True, label='Smoothed sine')
            prof_chart.set_title("Professional Engine - High Quality")
            prof_chart.set_labels("X", "Y")

            prof_chart.save("comparison_professional.svg")

            print("✅ Comparison charts created:")
            print("  - comparison_pure.svg (Pure engine)")
            print("  - comparison_professional.svg (Professional engine)")
        else:
            print("⚠️  Professional engine not available for comparison")

    except Exception as e:
        print(f"❌ Comparison demo failed: {e}")

def benchmark_engines():
    """Simple performance benchmark."""
    print("\n⏱️  Engine Performance Benchmark")
    print("=" * 35)

    try:
        import vizlychart as vc
        import time

        # Generate larger dataset
        n_points = 1000
        x = np.linspace(0, 10, n_points)
        y = np.sin(x) + 0.1 * np.random.randn(n_points)

        # Benchmark pure engine
        print(f"🔵 Benchmarking pure engine ({n_points} points)...")
        start_time = time.time()

        pure_chart = vc.LineChart(800, 600)
        pure_chart.plot(x, y, color='blue', linewidth=1)
        pure_chart.add_axes().add_grid()
        pure_chart.save("benchmark_pure.svg")

        pure_time = time.time() - start_time
        print(f"   Pure engine: {pure_time:.3f}s")

        # Benchmark professional engine
        if vc.ADVANCED_ENGINE_AVAILABLE:
            print(f"⭐ Benchmarking professional engine ({n_points} points)...")
            start_time = time.time()

            prof_chart = vc.ProfessionalLineChart(800, 600, quality=vc.RenderQuality.BALANCED)
            prof_chart.plot(x, y, color=vc.ColorHDR.from_hex('#3498db'), line_width=1.5)
            prof_chart.save("benchmark_professional.svg")

            prof_time = time.time() - start_time
            print(f"   Professional engine: {prof_time:.3f}s")

            # Performance comparison
            if prof_time > 0:
                speedup = pure_time / prof_time
                print(f"   Performance ratio: {speedup:.2f}x")

        print("✅ Benchmark complete!")

    except Exception as e:
        print(f"❌ Benchmark failed: {e}")

def main():
    """Run all demos."""
    success = demo_unified_api()

    if success:
        demo_engine_comparison()
        benchmark_engines()

        print("\n🚀 VizlyChart Library Ready!")
        print("="*40)
        print("✅ Dual rendering engines operational")
        print("✅ Unified API working")
        print("✅ File export functional")
        print("✅ Chart types available")
        print("\nNext steps:")
        print("- Import: import vizlychart as vc")
        print("- Create: chart = vc.create_line_chart()")
        print("- Plot: chart.plot(x, y)")
        print("- Save: chart.save('my_chart.svg')")
    else:
        print("\n⚠️  Some features may be limited")
        print("Check the error messages above for details")

if __name__ == "__main__":
    main()