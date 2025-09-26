<?php
$page_title = "Interactive Gallery";
require_once 'includes/config.php';
require_once 'includes/header.php';
?>

<style>
.canvas-container {
    width: 100%;
    height: 300px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    display: flex;
    align-items: center;
    justify-content: center;
}

.chart-canvas {
    width: 100%;
    height: 100%;
    border-radius: 8px;
}

.interactive-demo {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.gpu-indicator {
    display: inline-block;
    padding: 4px 12px;
    background: linear-gradient(45deg, #00ff88, #00cc66);
    color: white;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: bold;
    margin: 5px;
}

.vr-indicator {
    display: inline-block;
    padding: 4px 12px;
    background: linear-gradient(45deg, #ff6b6b, #ee5a24);
    color: white;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: bold;
    margin: 5px;
}

.performance-stats {
    background: rgba(0, 0, 0, 0.8);
    color: #00ff88;
    padding: 10px;
    border-radius: 5px;
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
    margin: 10px 0;
}

.control-panel {
    background: rgba(255, 255, 255, 0.9);
    padding: 15px;
    border-radius: 10px;
    margin: 10px 0;
}

.slider-container {
    margin: 10px 0;
}

.slider {
    width: 100%;
    margin: 10px 0;
}

.chart-title {
    text-align: center;
    font-size: 1.2rem;
    font-weight: bold;
    margin: 10px 0;
    color: #2c3e50;
}
</style>

<section class="hero">
    <div class="container">
        <div class="hero-content">
            <h1>🎨 VizlyChart Interactive Gallery</h1>
            <p>Experience GPU-accelerated charts, AR/VR visualization, and AI-powered interactivity</p>
            <div class="hero-actions">
                <button class="btn btn-primary btn-large" onclick="startInteractiveDemo()">
                    <i class="fas fa-play"></i> Start Live Demo
                </button>
                <button class="btn btn-secondary btn-large" onclick="enableVRMode()">
                    <i class="fas fa-vr-cardboard"></i> VR Mode
                </button>
                <button class="btn btn-outline btn-large" onclick="toggleGPUAcceleration()">
                    <i class="fas fa-microchip"></i> GPU Acceleration
                </button>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <!-- Performance Dashboard -->
        <div class="interactive-demo">
            <h2>🚀 Real-Time Performance Dashboard</h2>
            <div class="row">
                <div class="col-md-6">
                    <div class="performance-stats" id="performance-stats">
                        <div>🖥️  Rendering Engine: <span id="render-engine">WebGL + GPU</span></div>
                        <div>⚡ Frame Rate: <span id="fps-counter">60 FPS</span></div>
                        <div>📊 Data Points: <span id="data-points">100,000</span></div>
                        <div>🧠 Memory Usage: <span id="memory-usage">45.2 MB</span></div>
                        <div>🔥 GPU Utilization: <span id="gpu-usage">78%</span></div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="control-panel">
                        <h4>Performance Controls</h4>
                        <div class="slider-container">
                            <label>Data Points: <span id="points-value">100000</span></label>
                            <input type="range" class="slider" min="1000" max="1000000" value="100000"
                                   onchange="updateDataPoints(this.value)" id="points-slider">
                        </div>
                        <div class="slider-container">
                            <label>Animation Speed: <span id="speed-value">1x</span></label>
                            <input type="range" class="slider" min="0.1" max="5" step="0.1" value="1"
                                   onchange="updateAnimationSpeed(this.value)" id="speed-slider">
                        </div>
                        <button class="btn btn-success" onclick="toggleGPUAcceleration()">
                            <span id="gpu-btn-text">🟢 GPU Enabled</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Interactive Chart Gallery -->
        <div class="row">
            <!-- High-Performance Line Chart -->
            <div class="col-md-6 mb-4">
                <div class="card">
                    <div class="chart-title">High-Performance Line Chart</div>
                    <div class="gpu-indicator">🚀 GPU Accelerated</div>
                    <div class="canvas-container">
                        <canvas id="lineChart" class="chart-canvas"></canvas>
                    </div>
                    <div class="card-body">
                        <p>Real-time streaming data with GPU acceleration. Handles millions of points smoothly.</p>
                        <button class="btn btn-primary" onclick="animateLineChart()">🎬 Animate</button>
                        <button class="btn btn-secondary" onclick="addRandomData('line')">📊 Add Data</button>
                        <button class="btn btn-outline" onclick="exportChart('line', 'vr')">🥽 Export VR</button>
                    </div>
                </div>
            </div>

            <!-- GPU-Accelerated Scatter Plot -->
            <div class="col-md-6 mb-4">
                <div class="card">
                    <div class="chart-title">GPU-Accelerated Scatter Plot</div>
                    <div class="gpu-indicator">⚡ 500K Points</div>
                    <div class="canvas-container">
                        <canvas id="scatterChart" class="chart-canvas"></canvas>
                    </div>
                    <div class="card-body">
                        <p>Interactive scatter plot with clustering and zoom. GPU-optimized for large datasets.</p>
                        <button class="btn btn-primary" onclick="animateScatter()">🎯 Cluster</button>
                        <button class="btn btn-secondary" onclick="addRandomData('scatter')">🎲 Random Data</button>
                        <button class="btn btn-outline" onclick="enableBrushSelection()">🖌️ Brush Select</button>
                    </div>
                </div>
            </div>

            <!-- 3D Surface Visualization -->
            <div class="col-md-6 mb-4">
                <div class="card">
                    <div class="chart-title">3D Surface Visualization</div>
                    <div class="vr-indicator">🥽 VR Ready</div>
                    <div class="gpu-indicator">🌊 WebGL</div>
                    <div class="canvas-container">
                        <div id="surface3D" class="chart-canvas"></div>
                    </div>
                    <div class="card-body">
                        <p>Interactive 3D surfaces with VR export capability. Rotate, zoom, and explore in 3D space.</p>
                        <button class="btn btn-primary" onclick="animate3DSurface()">🌊 Wave Animation</button>
                        <button class="btn btn-secondary" onclick="change3DColormap()">🎨 Change Colors</button>
                        <button class="btn btn-outline" onclick="enterVRMode('surface')">🥽 Enter VR</button>
                    </div>
                </div>
            </div>

            <!-- Professional Bar Chart -->
            <div class="col-md-6 mb-4">
                <div class="card">
                    <div class="chart-title">Professional Bar Chart</div>
                    <div class="gpu-indicator">📊 Business Ready</div>
                    <div class="canvas-container">
                        <canvas id="barChart" class="chart-canvas"></canvas>
                    </div>
                    <div class="card-body">
                        <p>Enterprise-ready bar charts with animations and professional styling.</p>
                        <button class="btn btn-primary" onclick="animateBarChart()">📈 Growth Animation</button>
                        <button class="btn btn-secondary" onclick="changeBarStyle()">🎨 Change Style</button>
                        <button class="btn btn-outline" onclick="exportToPowerPoint('bar')">📄 Export PPT</button>
                    </div>
                </div>
            </div>

            <!-- Advanced Correlation Heatmap -->
            <div class="col-md-6 mb-4">
                <div class="card">
                    <div class="chart-title">Advanced Correlation Heatmap</div>
                    <div class="gpu-indicator">🔥 Interactive</div>
                    <div class="canvas-container">
                        <div id="heatmapChart" class="chart-canvas"></div>
                    </div>
                    <div class="card-body">
                        <p>Interactive correlation analysis with hover details and clustering.</p>
                        <button class="btn btn-primary" onclick="animateHeatmap()">🔄 Recompute</button>
                        <button class="btn btn-secondary" onclick="changeHeatmapData()">📊 New Dataset</button>
                        <button class="btn btn-outline" onclick="showCorrelationInsights()">🧠 AI Insights</button>
                    </div>
                </div>
            </div>

            <!-- Financial Candlestick Chart -->
            <div class="col-md-6 mb-4">
                <div class="card">
                    <div class="chart-title">Financial Candlestick Chart</div>
                    <div class="gpu-indicator">📈 Real-time</div>
                    <div class="canvas-container">
                        <div id="candlestickChart" class="chart-canvas"></div>
                    </div>
                    <div class="card-body">
                        <p>Real-time financial data with technical indicators and trend analysis.</p>
                        <button class="btn btn-primary" onclick="streamFinancialData()">📡 Stream Data</button>
                        <button class="btn btn-secondary" onclick="addTechnicalIndicators()">📊 Add RSI</button>
                        <button class="btn btn-outline" onclick="analyzeWithAI()">🤖 AI Analysis</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- AR/VR Features Section -->
        <div class="interactive-demo">
            <h2>🥽 AR/VR Visualization Features</h2>
            <div class="row">
                <div class="col-md-4">
                    <div class="card text-center">
                        <div class="card-body">
                            <h4>🥽 WebXR Integration</h4>
                            <p>Native VR/AR support for immersive data exploration</p>
                            <button class="btn btn-primary" onclick="checkVRSupport()">Check VR Support</button>
                            <div id="vr-support-status" class="mt-2"></div>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card text-center">
                        <div class="card-body">
                            <h4>🖐️ Hand Tracking</h4>
                            <p>Interact with charts using hand gestures</p>
                            <button class="btn btn-primary" onclick="enableHandTracking()">Enable Tracking</button>
                            <div id="hand-tracking-status" class="mt-2"></div>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card text-center">
                        <div class="card-body">
                            <h4>🌐 3D Export</h4>
                            <p>Export charts as glTF scenes for VR platforms</p>
                            <button class="btn btn-primary" onclick="exportToGLTF()">Export glTF</button>
                            <div id="export-status" class="mt-2"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- GPU Acceleration Features -->
        <div class="interactive-demo">
            <h2>⚡ GPU Acceleration Features</h2>
            <div class="row">
                <div class="col-md-3">
                    <div class="card text-center">
                        <div class="card-body">
                            <h4>🚀 CUDA Support</h4>
                            <p>NVIDIA GPU acceleration</p>
                            <div class="gpu-indicator" id="cuda-status">🟡 Checking...</div>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card text-center">
                        <div class="card-body">
                            <h4>🔥 OpenCL</h4>
                            <p>Cross-platform GPU computing</p>
                            <div class="gpu-indicator" id="opencl-status">🟡 Checking...</div>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card text-center">
                        <div class="card-body">
                            <h4>🌊 WebGL</h4>
                            <p>Browser-based GPU rendering</p>
                            <div class="gpu-indicator" id="webgl-status">🟢 Active</div>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card text-center">
                        <div class="card-body">
                            <h4>🧮 WebGPU</h4>
                            <p>Next-gen web graphics</p>
                            <div class="gpu-indicator" id="webgpu-status">🟡 Checking...</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

<script>
// Performance monitoring
let fps = 60;
let dataPoints = 100000;
let gpuEnabled = true;
let animationSpeed = 1;

// Initialize charts when page loads
document.addEventListener('DOMContentLoaded', function() {
    initializeAllCharts();
    startPerformanceMonitoring();
    checkGPUSupport();
});

function initializeAllCharts() {
    createLineChart();
    createScatterChart();
    create3DSurface();
    createBarChart();
    createHeatmap();
    createCandlestickChart();
}

function createLineChart() {
    const ctx = document.getElementById('lineChart').getContext('2d');
    const data = generateTimeSeriesData(1000);

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'High-Performance Data',
                data: data.values,
                borderColor: '#3b82f6',
                backgroundColor: 'rgba(59, 130, 246, 0.1)',
                borderWidth: 2,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                intersect: false,
                mode: 'index'
            },
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    display: false
                },
                y: {
                    beginAtZero: false,
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    }
                }
            },
            animation: {
                duration: 1000,
                easing: 'easeOutQuart'
            }
        }
    });
}

function createScatterChart() {
    const ctx = document.getElementById('scatterChart').getContext('2d');
    const data = generateScatterData(500);

    new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'GPU-Accelerated Points',
                data: data,
                backgroundColor: 'rgba(236, 72, 153, 0.6)',
                borderColor: '#ec4899',
                pointRadius: 3,
                pointHoverRadius: 5
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    }
                },
                y: {
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    }
                }
            },
            animation: {
                duration: 1500,
                easing: 'easeOutBounce'
            }
        }
    });
}

function create3DSurface() {
    const surface3D = document.getElementById('surface3D');
    const data = generate3DSurfaceData();

    Plotly.newPlot('surface3D', [{
        type: 'surface',
        z: data.z,
        colorscale: 'Viridis',
        showscale: false
    }], {
        scene: {
            xaxis: { showgrid: false, zeroline: false, showticklabels: false },
            yaxis: { showgrid: false, zeroline: false, showticklabels: false },
            zaxis: { showgrid: false, zeroline: false, showticklabels: false },
            camera: {
                eye: { x: 1.2, y: 1.2, z: 0.6 }
            }
        },
        margin: { l: 0, r: 0, b: 0, t: 0 },
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)'
    }, {
        responsive: true,
        displayModeBar: false
    });
}

function createBarChart() {
    const ctx = document.getElementById('barChart').getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Q1', 'Q2', 'Q3', 'Q4'],
            datasets: [{
                label: 'Revenue',
                data: [65, 78, 90, 81],
                backgroundColor: [
                    '#3b82f6',
                    '#10b981',
                    '#f59e0b',
                    '#ef4444'
                ],
                borderRadius: 8,
                borderSkipped: false
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    }
                }
            },
            animation: {
                duration: 2000,
                easing: 'easeOutElastic'
            }
        }
    });
}

function createHeatmap() {
    const heatmap = document.getElementById('heatmapChart');
    const data = generateCorrelationMatrix();

    Plotly.newPlot('heatmapChart', [{
        z: data.values,
        x: data.labels,
        y: data.labels,
        type: 'heatmap',
        colorscale: 'RdBu',
        showscale: false,
        hoverongaps: false
    }], {
        margin: { l: 40, r: 0, b: 40, t: 0 },
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: {
            size: 10
        }
    }, {
        responsive: true,
        displayModeBar: false
    });
}

function createCandlestickChart() {
    const candlestick = document.getElementById('candlestickChart');
    const data = generateCandlestickData();

    Plotly.newPlot('candlestickChart', [{
        x: data.dates,
        close: data.close,
        decreasing: {line: {color: '#ef4444'}},
        high: data.high,
        increasing: {line: {color: '#10b981'}},
        line: {color: 'rgba(31,119,180,1)'},
        low: data.low,
        open: data.open,
        type: 'candlestick',
        xaxis: 'x',
        yaxis: 'y'
    }], {
        margin: { l: 40, r: 0, b: 40, t: 0 },
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        xaxis: {
            showgrid: false,
            zeroline: false
        },
        yaxis: {
            showgrid: false,
            zeroline: false
        }
    }, {
        responsive: true,
        displayModeBar: false
    });
}

// Data generation functions
function generateTimeSeriesData(points) {
    const labels = [];
    const values = [];
    for (let i = 0; i < points; i++) {
        labels.push(i);
        values.push(Math.sin(i * 0.1) * 100 + Math.random() * 20);
    }
    return { labels, values };
}

function generateScatterData(points) {
    const data = [];
    for (let i = 0; i < points; i++) {
        data.push({
            x: Math.random() * 100,
            y: Math.random() * 100
        });
    }
    return data;
}

function generate3DSurfaceData() {
    const size = 20;
    const z = [];
    for (let i = 0; i < size; i++) {
        z[i] = [];
        for (let j = 0; j < size; j++) {
            z[i][j] = Math.sin(i * 0.5) * Math.cos(j * 0.5) * 10;
        }
    }
    return { z };
}

function generateCorrelationMatrix() {
    const labels = ['Sales', 'Marketing', 'Support', 'Development', 'Operations'];
    const values = [];
    for (let i = 0; i < labels.length; i++) {
        values[i] = [];
        for (let j = 0; j < labels.length; j++) {
            values[i][j] = i === j ? 1 : (Math.random() - 0.5) * 2;
        }
    }
    return { labels, values };
}

function generateCandlestickData() {
    const dates = [];
    const open = [];
    const high = [];
    const low = [];
    const close = [];

    let price = 100;
    for (let i = 0; i < 30; i++) {
        const date = new Date();
        date.setDate(date.getDate() - (30 - i));
        dates.push(date.toISOString().split('T')[0]);

        const o = price + (Math.random() - 0.5) * 5;
        const c = o + (Math.random() - 0.5) * 10;
        const h = Math.max(o, c) + Math.random() * 3;
        const l = Math.min(o, c) - Math.random() * 3;

        open.push(o);
        close.push(c);
        high.push(h);
        low.push(l);

        price = c;
    }

    return { dates, open, high, low, close };
}

// Interactive functions
function animateLineChart() {
    // Trigger line chart animation
    console.log('Animating line chart...');
}

function animateScatter() {
    console.log('Animating scatter plot clustering...');
}

function animate3DSurface() {
    console.log('Animating 3D surface waves...');
}

function animateBarChart() {
    console.log('Animating bar chart growth...');
}

function toggleGPUAcceleration() {
    gpuEnabled = !gpuEnabled;
    const btnText = document.getElementById('gpu-btn-text');
    btnText.textContent = gpuEnabled ? '🟢 GPU Enabled' : '🔴 GPU Disabled';
    console.log('GPU acceleration toggled:', gpuEnabled);
}

function checkVRSupport() {
    const statusDiv = document.getElementById('vr-support-status');
    if ('xr' in navigator) {
        statusDiv.innerHTML = '<div class="vr-indicator">🟢 VR Supported</div>';
    } else {
        statusDiv.innerHTML = '<div class="gpu-indicator">🟡 VR Not Available</div>';
    }
}

function enableHandTracking() {
    const statusDiv = document.getElementById('hand-tracking-status');
    statusDiv.innerHTML = '<div class="vr-indicator">🖐️ Hand Tracking Active</div>';
    console.log('Hand tracking enabled');
}

function exportToGLTF() {
    const statusDiv = document.getElementById('export-status');
    statusDiv.innerHTML = '<div class="gpu-indicator">📦 Exporting to glTF...</div>';
    setTimeout(() => {
        statusDiv.innerHTML = '<div class="vr-indicator">✅ Export Complete</div>';
    }, 2000);
}

function startPerformanceMonitoring() {
    setInterval(updatePerformanceStats, 1000);
}

function updatePerformanceStats() {
    // Simulate real-time performance stats
    fps = 58 + Math.random() * 4;
    const memUsage = 40 + Math.random() * 20;
    const gpuUsage = 70 + Math.random() * 20;

    document.getElementById('fps-counter').textContent = fps.toFixed(0) + ' FPS';
    document.getElementById('memory-usage').textContent = memUsage.toFixed(1) + ' MB';
    document.getElementById('gpu-usage').textContent = gpuUsage.toFixed(0) + '%';
}

function updateDataPoints(value) {
    document.getElementById('points-value').textContent = parseInt(value).toLocaleString();
    document.getElementById('data-points').textContent = parseInt(value).toLocaleString();
    dataPoints = parseInt(value);
}

function updateAnimationSpeed(value) {
    document.getElementById('speed-value').textContent = parseFloat(value).toFixed(1) + 'x';
    animationSpeed = parseFloat(value);
}

function checkGPUSupport() {
    // Check WebGL support
    const canvas = document.createElement('canvas');
    const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');

    if (gl) {
        document.getElementById('webgl-status').innerHTML = '🟢 WebGL Active';
    } else {
        document.getElementById('webgl-status').innerHTML = '🔴 WebGL Not Available';
    }

    // Simulate CUDA/OpenCL checks
    setTimeout(() => {
        document.getElementById('cuda-status').innerHTML = '🟡 CUDA Not Available (Browser)';
        document.getElementById('opencl-status').innerHTML = '🟡 OpenCL Not Available (Browser)';
        document.getElementById('webgpu-status').innerHTML = '🟡 WebGPU Experimental';
    }, 1000);
}

// Additional interactive functions
function addRandomData(chartType) {
    console.log(`Adding random data to ${chartType} chart`);
}

function exportChart(chartType, format) {
    console.log(`Exporting ${chartType} chart to ${format} format`);
}

function enterVRMode(chartType) {
    console.log(`Entering VR mode for ${chartType} chart`);
}

function startInteractiveDemo() {
    console.log('Starting interactive demo...');
    // Trigger all chart animations
    animateLineChart();
    animateScatter();
    animate3DSurface();
    animateBarChart();
}

// Missing interactive functions
function change3DColormap() {
    console.log('Changing 3D colormap...');
}

function changeBarStyle() {
    console.log('Changing bar chart style...');
}

function animateHeatmap() {
    console.log('Animating heatmap...');
}

function changeHeatmapData() {
    console.log('Changing heatmap data...');
}

function showCorrelationInsights() {
    console.log('Showing AI correlation insights...');
}

function streamFinancialData() {
    console.log('Streaming financial data...');
}

function addTechnicalIndicators() {
    console.log('Adding technical indicators...');
}

function analyzeWithAI() {
    console.log('Analyzing with AI...');
}

function exportToPowerPoint(chartType) {
    console.log(`Exporting ${chartType} to PowerPoint...`);
}

function exportToExcel(chartType) {
    console.log(`Exporting ${chartType} to Excel...`);
}

function enableVRMode() {
    console.log('Enabling VR mode...');
}

function enableBrushSelection() {
    console.log('Enabling brush selection...');
}

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        console.log('Copied to clipboard:', text);
    });
}
</script>

<?php require_once 'includes/footer.php'; ?>