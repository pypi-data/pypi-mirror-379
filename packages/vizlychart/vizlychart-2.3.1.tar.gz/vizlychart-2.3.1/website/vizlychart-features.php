<?php
$page_title = "Features";
require_once 'includes/config.php';
require_once 'includes/header.php';
?>

<section class="hero hero-small">
    <div class="container">
        <div class="hero-content text-center">
            <h1>VizlyChart Features</h1>
            <p>Comprehensive visualization capabilities with AI-powered intelligence</p>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="features-overview">
            <div class="feature-category">
                <h2>🤖 AI-Powered Features</h2>
                <div class="grid grid-2">
                    <div class="card">
                        <div class="card-icon" style="background: var(--gradient-primary);">
                            <i class="fas fa-brain"></i>
                        </div>
                        <h3>Natural Language Chart Generation</h3>
                        <p>Create charts from text descriptions like "scatter plot showing correlation between price and sales with trend line"</p>
                        <div class="code-example">
                            <pre><code>chart = vc.ai.create("line chart showing revenue over time")</code></pre>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-icon" style="background: var(--gradient-secondary);">
                            <i class="fas fa-lightbulb"></i>
                        </div>
                        <h3>Smart Chart Recommendations</h3>
                        <p>AI analyzes your data and recommends optimal chart types with confidence scoring</p>
                        <div class="code-example">
                            <pre><code>rec = vc.recommend_chart(data, intent='correlation')
print(f"Recommended: {rec.chart_type} ({rec.confidence:.0%})")</code></pre>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-icon" style="background: var(--gradient-success);">
                            <i class="fas fa-palette"></i>
                        </div>
                        <h3>Intelligent Styling</h3>
                        <p>Apply themes using natural language like "professional blue theme with bold fonts"</p>
                        <div class="code-example">
                            <pre><code>vc.style_chart(chart, "modern dark theme with neon accents")</code></pre>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-icon" style="background: var(--gradient-warning);">
                            <i class="fas fa-chart-line"></i>
                        </div>
                        <h3>Automated Data Analysis</h3>
                        <p>AI automatically analyzes your data and suggests insights and patterns</p>
                        <div class="code-example">
                            <pre><code>analysis = vc.ai.analyze_data(df)
for insight in analysis.insights:
    print(insight)</code></pre>
                        </div>
                    </div>
                </div>
            </div>

            <div class="feature-category">
                <h2>🔄 Unified Backend System</h2>
                <div class="grid grid-3">
                    <div class="card">
                        <div class="card-icon" style="background: var(--gradient-primary);">
                            <i class="fas fa-chart-bar"></i>
                        </div>
                        <h3>Matplotlib Backend</h3>
                        <ul class="feature-list">
                            <li>High-quality static images</li>
                            <li>Publication-ready output</li>
                            <li>Vector graphics support</li>
                            <li>LaTeX integration</li>
                        </ul>
                        <div class="code-snippet">
                            <code>vc.set_backend('matplotlib')</code>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-icon" style="background: var(--gradient-secondary);">
                            <i class="fas fa-globe"></i>
                        </div>
                        <h3>Plotly Backend</h3>
                        <ul class="feature-list">
                            <li>Interactive web charts</li>
                            <li>Zoom, pan, hover</li>
                            <li>Animation support</li>
                            <li>Mobile responsive</li>
                        </ul>
                        <div class="code-snippet">
                            <code>vc.set_backend('plotly')</code>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-icon" style="background: var(--gradient-success);">
                            <i class="fas fa-rocket"></i>
                        </div>
                        <h3>Pure Python Backend</h3>
                        <ul class="feature-list">
                            <li>Zero dependencies</li>
                            <li>Lightweight rendering</li>
                            <li>GPU acceleration</li>
                            <li>Custom optimization</li>
                        </ul>
                        <div class="code-snippet">
                            <code>vc.set_backend('pure')</code>
                        </div>
                    </div>
                </div>
            </div>

            <div class="feature-category">
                <h2>🏢 Enterprise Features</h2>
                <div class="grid grid-2">
                    <div class="card">
                        <div class="card-icon" style="background: var(--gradient-gold);">
                            <i class="fas fa-file-powerpoint"></i>
                        </div>
                        <h3>PowerPoint Export</h3>
                        <ul class="feature-list">
                            <li>Professional presentation slides</li>
                            <li>Corporate branding and templates</li>
                            <li>Custom slide layouts</li>
                            <li>Speaker notes integration</li>
                        </ul>
                        <div class="code-example">
                            <pre><code>exporter = EnterpriseExporter(branding=company_brand)
exporter.export_powerpoint(charts, "report.pptx")</code></pre>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-icon" style="background: var(--gradient-success);">
                            <i class="fas fa-file-excel"></i>
                        </div>
                        <h3>Excel Integration</h3>
                        <ul class="feature-list">
                            <li>Rich workbooks with data</li>
                            <li>Automated formatting</li>
                            <li>Pivot tables and formulas</li>
                            <li>Metadata tracking</li>
                        </ul>
                        <div class="code-example">
                            <pre><code>exporter.export_excel(
    chart, "analysis.xlsx",
    include_data=True,
    add_formulas=['SUM', 'AVERAGE']
)</code></pre>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-icon" style="background: var(--gradient-danger);">
                            <i class="fas fa-file-pdf"></i>
                        </div>
                        <h3>PDF Reports</h3>
                        <ul class="feature-list">
                            <li>Multi-page reports</li>
                            <li>Compliance features</li>
                            <li>Digital signatures</li>
                            <li>Audit trails</li>
                        </ul>
                        <div class="code-example">
                            <pre><code>pdf_reporter = PDFReporter(compliance=True)
pdf_reporter.generate_report(sections, "report.pdf")</code></pre>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-icon" style="background: var(--gradient-purple);">
                            <i class="fas fa-paint-brush"></i>
                        </div>
                        <h3>Corporate Branding</h3>
                        <ul class="feature-list">
                            <li>Custom brand colors</li>
                            <li>Logo integration</li>
                            <li>Font and typography</li>
                            <li>Consistent styling</li>
                        </ul>
                        <div class="code-example">
                            <pre><code>branding = BrandingConfig(
    primary_color="#1E40AF",
    logo_path="logo.png"
)</code></pre>
                        </div>
                    </div>
                </div>
            </div>

            <div class="feature-category">
                <h2>🧠 Advanced ML Visualizations</h2>
                <div class="grid grid-2">
                    <div class="card">
                        <div class="card-icon" style="background: var(--gradient-primary);">
                            <i class="fas fa-search"></i>
                        </div>
                        <h3>SHAP Analysis</h3>
                        <ul class="feature-list">
                            <li>Model explainability</li>
                            <li>Waterfall charts</li>
                            <li>Summary plots</li>
                            <li>Feature interactions</li>
                        </ul>
                        <div class="code-example">
                            <pre><code>shap_chart = vc.SHAPWaterfallChart()
shap_chart.plot(model, instance, feature_names)</code></pre>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-icon" style="background: var(--gradient-secondary);">
                            <i class="fas fa-chart-line"></i>
                        </div>
                        <h3>Feature Importance</h3>
                        <ul class="feature-list">
                            <li>Built-in importance</li>
                            <li>Permutation importance</li>
                            <li>Error bars</li>
                            <li>Statistical significance</li>
                        </ul>
                        <div class="code-example">
                            <pre><code>fi_chart = vc.FeatureImportanceChart()
fi_chart.add_importance(features, importance)</code></pre>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-icon" style="background: var(--gradient-success);">
                            <i class="fas fa-target"></i>
                        </div>
                        <h3>Model Performance</h3>
                        <ul class="feature-list">
                            <li>ROC curves with AUC</li>
                            <li>Precision-Recall curves</li>
                            <li>Confusion matrices</li>
                            <li>Learning curves</li>
                        </ul>
                        <div class="code-example">
                            <pre><code>roc_chart = vc.ROCChart()
roc_chart.add_curve(fpr, tpr, label=f'AUC={auc:.3f}')</code></pre>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-icon" style="background: var(--gradient-warning);">
                            <i class="fas fa-project-diagram"></i>
                        </div>
                        <h3>Causal Inference</h3>
                        <ul class="feature-list">
                            <li>Causal DAG charts</li>
                            <li>Confounding visualization</li>
                            <li>Treatment effects</li>
                            <li>Mediation analysis</li>
                        </ul>
                        <div class="code-example">
                            <pre><code>dag = vc.CausalDAGChart()
dag.add_node("Treatment", "intervention")
dag.add_edge("Treatment", "Outcome")</code></pre>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section bg-light">
    <div class="container">
        <div class="section-header text-center">
            <h2>🎯 Market Leadership</h2>
            <p>VizlyChart offers unique capabilities no other library provides</p>
        </div>
        <div class="comparison-table-container">
            <table class="comparison-table">
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
                        <td><strong>AI Chart Generation</strong></td>
                        <td class="highlight">✅ Full</td>
                        <td>❌</td>
                        <td>❌</td>
                        <td>❌</td>
                    </tr>
                    <tr>
                        <td><strong>Backend Switching</strong></td>
                        <td class="highlight">✅ 3 Backends</td>
                        <td>❌</td>
                        <td>❌</td>
                        <td>❌</td>
                    </tr>
                    <tr>
                        <td><strong>Natural Language Styling</strong></td>
                        <td class="highlight">✅ Advanced</td>
                        <td>❌</td>
                        <td>❌</td>
                        <td>❌</td>
                    </tr>
                    <tr>
                        <td><strong>Enterprise Exports</strong></td>
                        <td class="highlight">✅ PowerPoint/Excel</td>
                        <td>⚠️ Basic</td>
                        <td>⚠️ Limited</td>
                        <td>❌</td>
                    </tr>
                    <tr>
                        <td><strong>ML/Causal Charts</strong></td>
                        <td class="highlight">✅ Comprehensive</td>
                        <td>❌</td>
                        <td>⚠️ Some</td>
                        <td>⚠️ Basic</td>
                    </tr>
                    <tr>
                        <td><strong>GPU Acceleration</strong></td>
                        <td class="highlight">✅ CUDA/OpenCL</td>
                        <td>❌</td>
                        <td>❌</td>
                        <td>❌</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-header text-center">
            <h2>🚀 Get Started Today</h2>
            <p>Experience the future of data visualization</p>
        </div>
        <div class="cta-actions text-center">
            <a href="https://pypi.org/project/vizlychart/" class="btn btn-primary btn-large" target="_blank">
                <i class="fab fa-python"></i> Install VizlyChart
            </a>
            <a href="gallery.php" class="btn btn-secondary btn-large">
                <i class="fas fa-images"></i> View Examples
            </a>
            <a href="documentation.php" class="btn btn-outline btn-large">
                <i class="fas fa-book"></i> Read Documentation
            </a>
        </div>
    </div>
</section>

<?php require_once 'includes/footer.php'; ?>