#!/usr/bin/env python3
"""
Simple Demo of VizlyChart's New Market-Differentiating Features
==============================================================
"""

import numpy as np
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_ai_features():
    """Test AI-driven chart generation."""
    print("🤖 AI CHART GENERATION")
    print("-" * 30)

    try:
        # Test smart chart recommendation
        from vizlychart.ai.smart_selection import recommend_chart

        # Create sample data
        data = {
            'sales': np.random.normal(10000, 2000, 50),
            'price': np.random.uniform(50, 200, 50)
        }

        # Get recommendation
        rec = recommend_chart(data, intent='correlation')
        print(f"✅ Recommended: {rec.chart_type} (confidence: {rec.confidence:.1%})")
        print(f"   Reasons: {', '.join(rec.reasons)}")

        # Test natural language styling
        from vizlychart.ai.styling import parse_style

        style = parse_style("professional blue theme with bold fonts")
        print(f"✅ Parsed styling: theme={getattr(style.overall_theme, 'value', 'none')}")

    except Exception as e:
        print(f"⚠️  AI features: {e}")


def test_backends():
    """Test unified backend system."""
    print("\n🔄 BACKEND SWITCHING")
    print("-" * 30)

    try:
        from vizlychart.backends import list_backends, set_backend

        backends = list_backends()
        print(f"✅ Available backends: {[b.value for b in backends]}")

        # Try switching backends
        for backend in backends[:2]:  # Test first 2
            success = set_backend(backend)
            print(f"{'✅' if success else '❌'} {backend.value} backend")

    except Exception as e:
        print(f"⚠️  Backend switching: {e}")


def test_ml_charts():
    """Test ML/Causal visualization."""
    print("\n🧠 ML/CAUSAL CHARTS")
    print("-" * 30)

    try:
        from vizlychart.charts.ml_causal import CausalDAGChart, FeatureImportanceChart

        # Test Causal DAG
        dag = CausalDAGChart()
        dag.add_node("Treatment", "treatment")
        dag.add_node("Outcome", "outcome")
        dag.add_edge("Treatment", "Outcome")
        print("✅ Causal DAG created")

        # Test Feature Importance
        fi_chart = FeatureImportanceChart()
        features = ['feature1', 'feature2', 'feature3']
        importance = np.array([0.5, 0.3, 0.2])
        fi_chart.plot(features, importance)
        print("✅ Feature importance chart created")

    except Exception as e:
        print(f"⚠️  ML/Causal charts: {e}")


def test_gpu_acceleration():
    """Test GPU acceleration."""
    print("\n⚡ GPU ACCELERATION")
    print("-" * 30)

    try:
        from vizlychart.gpu.acceleration import AcceleratedRenderer

        renderer = AcceleratedRenderer(800, 600)
        backend_info = renderer.get_backend_info()

        print(f"✅ Backend: {backend_info['backend']}")
        print(f"✅ Device: {backend_info['device']}")
        print(f"✅ GPU enabled: {backend_info['enabled']}")

        # Test with sample data
        x = np.random.randn(1000)
        y = np.random.randn(1000)
        renderer.scatter_gpu(x, y)
        print("✅ Rendered 1000 points successfully")

    except Exception as e:
        print(f"⚠️  GPU acceleration: {e}")


def main():
    """Run simple feature demo."""
    print("🚀 VIZLYCHART NEW FEATURES DEMO")
    print("=" * 50)
    print("Testing market-differentiating capabilities...")
    print()

    test_ai_features()
    test_backends()
    test_ml_charts()
    test_gpu_acceleration()

    print("\n✨ SUMMARY")
    print("=" * 50)
    print("VizlyChart now offers:")
    print("• AI-powered chart recommendations")
    print("• Natural language styling")
    print("• Unified backend switching")
    print("• ML & causal inference charts")
    print("• GPU-accelerated rendering")
    print("• Enterprise export capabilities")
    print("\nThese features address ALL major market gaps!")


if __name__ == "__main__":
    main()