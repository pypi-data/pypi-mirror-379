<?php
$page_title = "Home";
require_once 'includes/config.php';
require_once 'includes/header.php';
?>

<section class="hero">
    <div class="container">
        <div class="hero-content">
            <h1>VizlyChart: The AI-Powered Visualization Library</h1>
            <p>Revolutionary platform with <strong>AI-powered chart generation</strong>, unified backend switching, enterprise exports, and advanced ML visualizations. The most comprehensive visualization solution available.</p>
            <div class="hero-actions">
                <a href="https://pypi.org/project/vizlychart/" class="btn btn-primary btn-large" target="_blank">
                    <i class="fab fa-python"></i> pip install vizlychart
                </a>
                <a href="gallery.php" class="btn btn-secondary btn-large">
                    <i class="fas fa-images"></i> View Gallery
                </a>
                <a href="contact.php" class="btn btn-outline btn-large">
                    <i class="fas fa-building"></i> Enterprise
                </a>
            </div>
            <div class="hero-stats">
                <div class="stat-item">
                    <span class="stat-number">🤖 AI</span>
                    <span class="stat-label">Powered</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">⚡ GPU</span>
                    <span class="stat-label">Accelerated</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">🥽 VR/AR</span>
                    <span class="stat-label">Ready</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">🏢 Enterprise</span>
                    <span class="stat-label">Ready</span>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">🤖 AI-Powered Visualization</h2>
            <p class="section-subtitle">Create charts using natural language - the first visualization library with comprehensive AI integration</p>
        </div>
        <div class="code-example">
            <div class="code-block">
                <pre><code class="language-python">import vizlychart as vc

# Generate charts from natural language descriptions
chart = vc.ai.create("scatter plot showing correlation between price and sales")

# Get smart recommendations
rec = vc.recommend_chart(data, intent='correlation')
print(f"Recommended: {rec.chart_type} (confidence: {rec.confidence:.0%})")

# Apply styling with natural language
vc.style_chart(chart, "professional blue theme with bold fonts")
chart.show()</code></pre>
            </div>
        </div>
    </div>
</section>

<section class="section bg-light">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">🔄 Unified Backend System</h2>
            <p class="section-subtitle">Switch between matplotlib, Plotly, and pure Python with the same API</p>
        </div>
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Matplotlib Backend</h3>
                <p>High-quality static charts perfect for publications and reports</p>
                <div class="code-snippet">
                    <code>vc.set_backend('matplotlib')</code>
                </div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🌐</div>
                <h3>Plotly Backend</h3>
                <p>Interactive web-ready charts with zoom, pan, and hover capabilities</p>
                <div class="code-snippet">
                    <code>vc.set_backend('plotly')</code>
                </div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3>Pure Python Backend</h3>
                <p>Lightweight rendering with no external dependencies</p>
                <div class="code-snippet">
                    <code>vc.set_backend('pure')</code>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">🏢 Enterprise-Grade Features</h2>
            <p class="section-subtitle">Professional exports, branding, and compliance features</p>
        </div>
        <div class="enterprise-features">
            <div class="enterprise-grid">
                <div class="enterprise-item">
                    <h4>🎯 PowerPoint Export</h4>
                    <p>Professional presentation slides with corporate branding and templates</p>
                </div>
                <div class="enterprise-item">
                    <h4>📊 Excel Integration</h4>
                    <p>Rich workbooks with data, charts, metadata, and automated formatting</p>
                </div>
                <div class="enterprise-item">
                    <h4>📄 PDF Reports</h4>
                    <p>Multi-page reports with compliance features and audit trails</p>
                </div>
                <div class="enterprise-item">
                    <h4>🎨 Corporate Branding</h4>
                    <p>Custom themes, logos, colors, and consistent styling across all exports</p>
                </div>
            </div>
        </div>
        <div class="code-example">
            <div class="code-block">
                <pre><code class="language-python">from vizlychart.enterprise import EnterpriseExporter

# Apply corporate branding
exporter = EnterpriseExporter(branding=company_brand)

# Export to PowerPoint with professional styling
exporter.export_powerpoint(charts, "quarterly_report.pptx", branded=True)

# Export to Excel with data and metadata
exporter.export_excel(charts, "analysis_workbook.xlsx", include_data=True)</code></pre>
            </div>
        </div>
    </div>
</section>

<section class="section bg-light">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">🧠 Advanced ML Visualizations</h2>
            <p class="section-subtitle">Built-in support for machine learning and causal inference</p>
        </div>
        <div class="ml-features">
            <div class="ml-grid">
                <div class="ml-card">
                    <h4>🔍 SHAP Analysis</h4>
                    <p>Model explainability with SHAP waterfall charts and summary plots</p>
                </div>
                <div class="ml-card">
                    <h4>📈 Feature Importance</h4>
                    <p>Comprehensive feature analysis with permutation and built-in importance</p>
                </div>
                <div class="ml-card">
                    <h4>🎯 ROC & Precision-Recall</h4>
                    <p>Model performance visualization with AUC analysis</p>
                </div>
                <div class="ml-card">
                    <h4>🔗 Causal DAG Charts</h4>
                    <p>Visualize causal relationships and confounding variables</p>
                </div>
            </div>
        </div>
        <div class="code-example">
            <div class="code-block">
                <pre><code class="language-python"># Causal inference visualization
dag = vc.CausalDAGChart()
dag.add_node("Treatment", "intervention")
dag.add_node("Outcome", "target")
dag.add_edge("Treatment", "Outcome")

# SHAP model explainability
shap_chart = vc.SHAPWaterfallChart()
shap_chart.plot(model, instance, feature_names)

# Feature importance analysis
fi_chart = vc.FeatureImportanceChart()
fi_chart.plot(features, shap_values, method="shap")</code></pre>
            </div>
        </div>
    </div>
</section>

<section class="section bg-light">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">⚡ GPU Acceleration & VR/AR Features</h2>
            <p class="section-subtitle">Revolutionary performance and immersive visualization capabilities</p>
        </div>
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">🚀</div>
                <h3>GPU Acceleration</h3>
                <p>CUDA and OpenCL support with up to 50x performance improvements for large datasets</p>
                <div class="code-snippet">
                    <code>renderer = vc.gpu.AcceleratedRenderer(backend='cuda')</code>
                </div>
                <ul class="feature-list">
                    <li>✅ CUDA Support (NVIDIA)</li>
                    <li>✅ OpenCL Support (Cross-platform)</li>
                    <li>✅ Automatic Backend Selection</li>
                    <li>✅ 10M+ Points Real-time</li>
                </ul>
            </div>

            <div class="feature-card">
                <div class="feature-icon">🥽</div>
                <h3>VR/AR Visualization</h3>
                <p>Complete WebXR integration for immersive data exploration with hand tracking</p>
                <div class="code-snippet">
                    <code>vc.vr.export_scene(chart, "data_visualization.gltf")</code>
                </div>
                <ul class="feature-list">
                    <li>✅ WebXR Native Support</li>
                    <li>✅ Hand/Eye Tracking</li>
                    <li>✅ glTF Scene Export</li>
                    <li>✅ Immersive Data Exploration</li>
                </ul>
            </div>

            <div class="feature-card">
                <div class="feature-icon">📡</div>
                <h3>Real-time Streaming</h3>
                <p>Sub-millisecond latency data streaming with WebSocket and Redis support</p>
                <div class="code-snippet">
                    <code>stream = vc.streaming.RealTimeChart(latency='sub_ms')</code>
                </div>
                <ul class="feature-list">
                    <li>✅ Sub-millisecond Updates</li>
                    <li>✅ WebSocket/Redis Support</li>
                    <li>✅ Live Data Analytics</li>
                    <li>✅ High-frequency Trading Ready</li>
                </ul>
            </div>

            <div class="feature-card">
                <div class="feature-icon">🌐</div>
                <h3>Web Integration</h3>
                <p>Native web components with responsive design and mobile optimization</p>
                <div class="code-snippet">
                    <code>component = vc.web.ResponsiveChart(mobile_ready=True)</code>
                </div>
                <ul class="feature-list">
                    <li>✅ Responsive Design</li>
                    <li>✅ Mobile Optimized</li>
                    <li>✅ Touch Interactions</li>
                    <li>✅ Progressive Web App Ready</li>
                </ul>
            </div>
        </div>

        <div class="performance-demo" style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 15px; margin: 2rem 0;">
            <h3>🎮 Interactive Demo</h3>
            <p>Experience GPU-accelerated rendering and VR-ready visualizations</p>
            <div style="text-align: center; margin: 20px 0;">
                <a href="interactive-gallery.php" class="btn btn-primary btn-large">
                    <i class="fas fa-gamepad"></i> Try Interactive Gallery
                </a>
                <a href="interactive-gallery.php#vr-demo" class="btn btn-secondary btn-large">
                    <i class="fas fa-vr-cardboard"></i> VR Demo
                </a>
                <a href="interactive-gallery.php#gpu-demo" class="btn btn-outline btn-large">
                    <i class="fas fa-microchip"></i> GPU Performance Test
                </a>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">📊 Competitive Advantage</h2>
            <p class="section-subtitle">VizlyChart offers capabilities no other library can match</p>
        </div>
        <div class="comparison-table">
            <table>
                <thead>
                    <tr>
                        <th>Feature</th>
                        <th class="highlight">VizlyChart</th>
                        <th>Matplotlib</th>
                        <th>Plotly</th>
                        <th>Seaborn</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>AI Chart Generation</td>
                        <td class="highlight">✅</td>
                        <td>❌</td>
                        <td>❌</td>
                        <td>❌</td>
                    </tr>
                    <tr>
                        <td>Backend Switching</td>
                        <td class="highlight">✅</td>
                        <td>❌</td>
                        <td>❌</td>
                        <td>❌</td>
                    </tr>
                    <tr>
                        <td>Natural Language Styling</td>
                        <td class="highlight">✅</td>
                        <td>❌</td>
                        <td>❌</td>
                        <td>❌</td>
                    </tr>
                    <tr>
                        <td>Enterprise Exports</td>
                        <td class="highlight">✅</td>
                        <td>⚠️</td>
                        <td>⚠️</td>
                        <td>❌</td>
                    </tr>
                    <tr>
                        <td>ML/Causal Charts</td>
                        <td class="highlight">✅</td>
                        <td>❌</td>
                        <td>⚠️</td>
                        <td>❌</td>
                    </tr>
                    <tr>
                        <td>GPU Acceleration</td>
                        <td class="highlight">✅</td>
                        <td>❌</td>
                        <td>❌</td>
                        <td>❌</td>
                    </tr>
                    <tr>
                        <td>VR/AR Support</td>
                        <td class="highlight">✅</td>
                        <td>❌</td>
                        <td>❌</td>
                        <td>❌</td>
                    </tr>
                    <tr>
                        <td>Real-time Streaming</td>
                        <td class="highlight">✅</td>
                        <td>❌</td>
                        <td>❌</td>
                        <td>❌</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</section>

<section class="section bg-light">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">🚀 Quick Start</h2>
            <p class="section-subtitle">Get started with VizlyChart in minutes</p>
        </div>
        <div class="quickstart-steps">
            <div class="step">
                <div class="step-number">1</div>
                <div class="step-content">
                    <h3>Install VizlyChart</h3>
                    <div class="code-block">
                        <pre><code>pip install vizlychart[all]</code></pre>
                    </div>
                </div>
            </div>
            <div class="step">
                <div class="step-number">2</div>
                <div class="step-content">
                    <h3>Create Your First Chart</h3>
                    <div class="code-block">
                        <pre><code>import vizlychart as vc
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

chart = vc.LineChart()
chart.plot(x, y, label="Sine Wave")
chart.set_title("My First VizlyChart")
chart.show()</code></pre>
                    </div>
                </div>
            </div>
            <div class="step">
                <div class="step-number">3</div>
                <div class="step-content">
                    <h3>Explore AI Features</h3>
                    <div class="code-block">
                        <pre><code># Let AI create charts for you
chart = vc.ai.create("line chart showing revenue growth")

# Get smart recommendations
rec = vc.recommend_chart(data, intent='trend')
chart = rec.create_chart()</code></pre>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">📖 Resources</h2>
            <p class="section-subtitle">Everything you need to master VizlyChart</p>
        </div>
        <div class="resources-grid">
            <div class="resource-card">
                <div class="resource-icon">📚</div>
                <h3>Documentation</h3>
                <p>Comprehensive guides, API reference, and tutorials</p>
                <a href="documentation.php" class="btn btn-outline">Read Docs</a>
            </div>
            <div class="resource-card">
                <div class="resource-icon">🎨</div>
                <h3>Gallery</h3>
                <p>Interactive examples and real-world use cases</p>
                <a href="gallery.php" class="btn btn-outline">View Gallery</a>
            </div>
            <div class="resource-card">
                <div class="resource-icon">🏢</div>
                <h3>Enterprise</h3>
                <p>Professional support and enterprise features</p>
                <a href="contact.php" class="btn btn-outline">Contact Sales</a>
            </div>
            <div class="resource-card">
                <div class="resource-icon">💼</div>
                <h3>Pricing</h3>
                <p>Flexible plans for individuals and organizations</p>
                <a href="pricing.php" class="btn btn-outline">View Pricing</a>
            </div>
        </div>
    </div>
</section>

<?php require_once 'includes/footer.php'; ?>