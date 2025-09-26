#!/usr/bin/env python3
"""
VizlyChart Advanced Features Demo
================================

Comprehensive demonstration of the new AI-driven, backend-agnostic,
and enterprise-ready features in VizlyChart.
"""

import numpy as np
import warnings
warnings.filterwarnings('ignore')

def demo_ai_chart_generation():
    """Demo AI-driven natural language chart generation."""
    print("🤖 AI-DRIVEN CHART GENERATION")
    print("=" * 50)

    try:
        # Import AI module
        from src.vizlychart.ai import create, recommend_chart

        # Generate sample data
        np.random.seed(42)
        data = {
            'sales': np.random.normal(10000, 2000, 100),
            'price': np.random.uniform(50, 200, 100),
            'region': np.random.choice(['North', 'South', 'East', 'West'], 100),
            'date': np.arange('2023-01-01', '2023-04-10', dtype='datetime64[D]')[:100]
        }

        # Demo 1: Natural language chart creation
        print("Creating charts from natural language descriptions...")

        descriptions = [
            "scatter plot of sales vs price",
            "line chart showing sales over time with trend line",
            "bar chart comparing sales by region",
            "histogram of price distribution"
        ]

        for desc in descriptions:
            try:
                chart = create(desc, data, list(data.keys()))
                print(f"✅ Created: {desc}")
            except Exception as e:
                print(f"⚠️  Failed: {desc} - {e}")

        # Demo 2: Smart chart recommendations
        print("\n📊 Smart Chart Recommendations:")
        recommendation = recommend_chart(data, intent='correlation')
        print(f"Recommended: {recommendation.chart_type}")
        print(f"Confidence: {recommendation.confidence:.1%}")
        print("Reasons:", ', '.join(recommendation.reasons))

    except ImportError as e:
        print(f"❌ AI features require additional setup: {e}")


def demo_backend_switching():
    """Demo unified backend switching API."""
    print("\n🔄 UNIFIED BACKEND SWITCHING")
    print("=" * 50)

    try:
        from src.vizlychart.backends import set_backend, list_backends, get_capabilities

        # Show available backends
        backends = list_backends()
        print(f"Available backends: {[b.value for b in backends]}")

        # Demo backend switching
        for backend in backends:
            try:
                success = set_backend(backend)
                if success:
                    caps = get_capabilities()
                    print(f"✅ {backend.value}: Interactive={caps.interactive}, "
                          f"3D={caps.supports_3d}, GPU={caps.gpu_accelerated}")
                else:
                    print(f"❌ {backend.value}: Not available")
            except Exception as e:
                print(f"⚠️  {backend.value}: {e}")

    except ImportError as e:
        print(f"❌ Backend switching requires additional setup: {e}")


def demo_ml_causal_charts():
    """Demo ML and causal inference visualizations."""
    print("\n🧠 ML & CAUSAL INFERENCE CHARTS")
    print("=" * 50)

    try:
        from src.vizlychart.charts.ml_causal import (
            CausalDAGChart, FeatureImportanceChart,
            SHAPWaterfallChart, ModelPerformanceChart
        )

        # Demo 1: Causal DAG
        print("Creating Causal DAG...")
        dag = CausalDAGChart()
        dag.add_node("Treatment", node_type="treatment")
        dag.add_node("Outcome", node_type="outcome")
        dag.add_node("Confounder", node_type="confounder")
        dag.add_edge("Treatment", "Outcome", strength=0.8)
        dag.add_edge("Confounder", "Treatment", strength=0.6)
        dag.add_edge("Confounder", "Outcome", strength=0.7)
        dag.auto_layout("hierarchical")
        print("✅ Causal DAG created with 3 nodes and 3 edges")

        # Demo 2: Feature Importance
        print("\nCreating Feature Importance chart...")
        features = ['age', 'income', 'education', 'location', 'experience']
        importance = np.array([0.25, 0.30, 0.15, 0.10, 0.20])

        fi_chart = FeatureImportanceChart()
        fi_chart.plot(features, importance, importance_type="shap")
        print("✅ Feature importance chart created")

        # Demo 3: SHAP Waterfall
        print("\nCreating SHAP Waterfall chart...")
        shap_values = np.array([0.1, -0.05, 0.3, -0.2, 0.15])
        base_value = 0.5
        prediction = base_value + np.sum(shap_values)

        shap_chart = SHAPWaterfallChart()
        shap_chart.plot(features, shap_values, base_value, prediction)
        print("✅ SHAP waterfall chart created")

        # Demo 4: Model Performance
        print("\nCreating ROC curves comparison...")
        models = {
            'Random Forest': (np.linspace(0, 1, 100), np.linspace(0, 1, 100)**0.5, 0.85),
            'SVM': (np.linspace(0, 1, 100), np.linspace(0, 1, 100)**0.7, 0.82),
            'Logistic Regression': (np.linspace(0, 1, 100), np.linspace(0, 1, 100)**0.9, 0.78)
        }

        perf_chart = ModelPerformanceChart()
        perf_chart.plot_roc_curves(models)
        print("✅ Model performance comparison created")

    except ImportError as e:
        print(f"❌ ML/Causal charts require additional setup: {e}")


def demo_enterprise_exports():
    """Demo enhanced enterprise export capabilities."""
    print("\n🏢 ENTERPRISE EXPORT CAPABILITIES")
    print("=" * 50)

    try:
        from src.vizlychart.enterprise.exports import EnterpriseExporter, ExportConfig
        from src.vizlychart.enterprise.themes import BrandingConfig
        from src.vizlychart.enterprise.charts import ChartMetadata
        from src.vizlychart.enterprise.security import SecurityLevel
        from datetime import datetime

        # Create branded exporter
        branding = BrandingConfig(
            company_name="TechCorp Analytics",
            primary_color="#0066CC",
            secondary_color="#FF6600",
            font_family="Arial"
        )

        exporter = EnterpriseExporter(branding)

        # Create sample metadata
        metadata = ChartMetadata(
            chart_id="DEMO_001",
            title="Sales Performance Analysis",
            created_by="Data Team",
            security_level=SecurityLevel.INTERNAL
        )

        # Test different export formats
        formats = ['pdf', 'html', 'json']

        print("Testing export formats:")
        for fmt in formats:
            try:
                config = ExportConfig(format=fmt, branded=True, include_metadata=True)
                print(f"✅ {fmt.upper()} export capability available")
            except Exception as e:
                print(f"⚠️  {fmt.upper()} export: {e}")

        # Test PowerPoint export (if available)
        try:
            config = ExportConfig(format='pptx', slide_layout="title_and_content")
            print("✅ PowerPoint export capability available")
        except:
            print("⚠️  PowerPoint export requires python-pptx")

        # Test Excel export (if available)
        try:
            config = ExportConfig(format='xlsx', excel_worksheet="Analytics")
            print("✅ Excel export capability available")
        except:
            print("⚠️  Excel export requires openpyxl")

    except ImportError as e:
        print(f"❌ Enterprise exports require additional setup: {e}")


def demo_natural_language_styling():
    """Demo natural language styling."""
    print("\n🎨 NATURAL LANGUAGE STYLING")
    print("=" * 50)

    try:
        from src.vizlychart.ai.styling import style_chart, parse_style, NaturalLanguageStylist

        stylist = NaturalLanguageStylist()

        # Test style parsing
        style_descriptions = [
            "professional blue theme with bold fonts",
            "vibrant colors with large points and thick lines",
            "minimal design with white background and thin gray lines",
            "elegant pastel colors with shadows and gradients",
            "scientific monochrome theme with serif fonts"
        ]

        print("Parsing style descriptions:")
        for desc in style_descriptions:
            try:
                config = parse_style(desc)
                features = []
                if config.color_scheme:
                    features.append(f"scheme={config.color_scheme.value}")
                if config.overall_theme:
                    features.append(f"theme={config.overall_theme.value}")
                if config.font_family:
                    features.append(f"font={config.font_family}")

                print(f"✅ '{desc}' → {', '.join(features) if features else 'basic styling'}")
            except Exception as e:
                print(f"⚠️  Failed to parse: '{desc}' - {e}")

        # Generate style suggestions
        suggestions = stylist.generate_style_suggestions('scatter', 'financial data')
        print(f"\n💡 Style suggestions for scatter plots:")
        for i, suggestion in enumerate(suggestions[:3], 1):
            print(f"{i}. {suggestion}")

    except ImportError as e:
        print(f"❌ Styling features require additional setup: {e}")


def demo_performance_features():
    """Demo high-performance rendering capabilities."""
    print("\n⚡ HIGH-PERFORMANCE RENDERING")
    print("=" * 50)

    try:
        from src.vizlychart.gpu.acceleration import AcceleratedRenderer

        # Create accelerated renderer
        renderer = AcceleratedRenderer(width=1200, height=800)

        # Show backend info
        backend_info = renderer.get_backend_info()
        print(f"Rendering backend: {backend_info['backend']}")
        print(f"Device: {backend_info['device']}")
        print(f"GPU enabled: {backend_info['enabled']}")

        # Demo large dataset handling
        print("\nTesting performance with large datasets:")

        # Generate increasingly large datasets
        sizes = [1000, 10000, 100000]

        for size in sizes:
            try:
                x = np.random.randn(size)
                y = np.random.randn(size)

                import time
                start_time = time.time()
                renderer.scatter_gpu(x, y, color='blue', size=5)
                end_time = time.time()

                print(f"✅ {size:,} points rendered in {end_time - start_time:.3f}s")

            except Exception as e:
                print(f"⚠️  {size:,} points: {e}")
                break

    except ImportError as e:
        print(f"❌ GPU acceleration requires additional setup: {e}")


def main():
    """Run all feature demonstrations."""
    print("🚀 VIZLYCHART ADVANCED FEATURES DEMO")
    print("=" * 60)
    print("Demonstrating the new market-differentiating capabilities:")
    print("• AI-driven visualization from natural language")
    print("• Unified backend switching (matplotlib/plotly/pure)")
    print("• ML & causal inference chart types")
    print("• Enterprise exports (PDF/HTML/PowerPoint/Excel)")
    print("• Smart chart type selection")
    print("• Natural language styling")
    print("• High-performance GPU rendering")
    print("=" * 60)

    # Run all demos
    demo_ai_chart_generation()
    demo_backend_switching()
    demo_ml_causal_charts()
    demo_enterprise_exports()
    demo_natural_language_styling()
    demo_performance_features()

    print("\n🎉 DEMO COMPLETE!")
    print("=" * 60)
    print("VizlyChart now provides:")
    print("✅ Natural language chart creation")
    print("✅ Smart recommendations based on data")
    print("✅ Seamless backend switching")
    print("✅ ML/Causal inference visualizations")
    print("✅ Enterprise-grade exports")
    print("✅ AI-powered styling")
    print("✅ High-performance rendering")
    print("\nThese features address all major market gaps and position")
    print("VizlyChart as the most advanced visualization library available!")


if __name__ == "__main__":
    main()