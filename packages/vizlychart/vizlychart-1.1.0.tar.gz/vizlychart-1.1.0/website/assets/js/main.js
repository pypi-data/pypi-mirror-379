// Vizly Website - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, initializing components...');
    console.log('Chart.js available:', typeof Chart !== 'undefined');

    // Initialize all components
    initNavigation();

    // Wait for Chart.js to be available
    if (typeof Chart !== 'undefined') {
        initChartDemos();
    } else {
        console.log('Chart.js not immediately available, waiting...');
        setTimeout(() => {
            if (typeof Chart !== 'undefined') {
                console.log('Chart.js now available, initializing charts...');
                initChartDemos();
            } else {
                console.error('Chart.js failed to load');
            }
        }, 1000);
    }

    initScrollAnimations();
    initPerformanceCounters();
    initCodeCopyButtons();
});

// Navigation
function initNavigation() {
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            navToggle.classList.toggle('active');
        });
    }

    // Close mobile menu when clicking on links
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            navToggle.classList.remove('active');
        });
    });

    // Header scroll effect
    let lastScroll = 0;
    const header = document.querySelector('.header');

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll <= 0) {
            header.classList.remove('scroll-up');
            return;
        }

        if (currentScroll > lastScroll && !header.classList.contains('scroll-down')) {
            header.classList.remove('scroll-up');
            header.classList.add('scroll-down');
        } else if (currentScroll < lastScroll && header.classList.contains('scroll-down')) {
            header.classList.remove('scroll-down');
            header.classList.add('scroll-up');
        }
        lastScroll = currentScroll;
    });
}

// Chart Demos
function initChartDemos() {
    console.log('Initializing chart demos...');

    if (typeof Chart === 'undefined') {
        console.error('Chart.js is not available');
        return;
    }

    try {
        // Line Chart Demo
        const lineChartCtx = document.getElementById('lineChart');
        if (lineChartCtx) {
            console.log('Creating line chart...');
            new Chart(lineChartCtx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                datasets: [{
                    label: 'GPU Accelerated',
                    data: [12, 19, 3, 5, 2, 3],
                    borderColor: 'rgb(37, 99, 235)',
                    backgroundColor: 'rgba(37, 99, 235, 0.1)',
                    tension: 0.4,
                    fill: true
                }, {
                    label: 'Standard',
                    data: [2, 3, 20, 5, 1, 4],
                    borderColor: 'rgb(239, 68, 68)',
                    backgroundColor: 'rgba(239, 68, 68, 0.1)',
                    tension: 0.4,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Performance Comparison'
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    // Scatter Chart Demo
    const scatterChartCtx = document.getElementById('scatterChart');
    if (scatterChartCtx) {
        const scatterData = Array.from({length: 100}, () => ({
            x: Math.random() * 100,
            y: Math.random() * 100
        }));

        new Chart(scatterChartCtx, {
            type: 'scatter',
            data: {
                datasets: [{
                    label: 'VR Data Points',
                    data: scatterData,
                    backgroundColor: 'rgba(16, 185, 129, 0.6)',
                    borderColor: 'rgb(16, 185, 129)',
                    pointRadius: 5
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: '3D VR Visualization'
                    }
                },
                scales: {
                    x: {
                        type: 'linear',
                        position: 'bottom',
                        title: {
                            display: true,
                            text: 'X Axis'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Y Axis'
                        }
                    }
                }
            }
        });
    }

    // Real-time Chart Demo
    const realtimeChartCtx = document.getElementById('realtimeChart');
    if (realtimeChartCtx) {
        const realtimeChart = new Chart(realtimeChartCtx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'Real-time Data',
                    data: [],
                    borderColor: 'rgb(245, 158, 11)',
                    backgroundColor: 'rgba(245, 158, 11, 0.1)',
                    tension: 0.4,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Live Streaming Data'
                    }
                },
                scales: {
                    x: {
                        type: 'linear',
                        title: {
                            display: true,
                            text: 'Time (ms)'
                        }
                    },
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Value'
                        }
                    }
                },
                animation: {
                    duration: 0
                }
            }
        });

        // Simulate real-time data
        let time = 0;
        setInterval(() => {
            time += 100;
            const value = Math.sin(time / 1000) * 50 + 50 + (Math.random() - 0.5) * 10;

            realtimeChart.data.labels.push(time);
            realtimeChart.data.datasets[0].data.push(value);

            // Keep only last 50 points
            if (realtimeChart.data.labels.length > 50) {
                realtimeChart.data.labels.shift();
                realtimeChart.data.datasets[0].data.shift();
            }

            realtimeChart.update('none');
        }, 100);
    }

    // Performance Chart Demo
    const performanceChartCtx = document.getElementById('performanceChart');
    if (performanceChartCtx) {
        new Chart(performanceChartCtx, {
            type: 'bar',
            data: {
                labels: ['10K Points', '100K Points', '1M Points', '10M Points'],
                datasets: [{
                    label: 'CPU (ms)',
                    data: [200, 2000, 20000, 200000],
                    backgroundColor: 'rgba(239, 68, 68, 0.8)',
                    borderColor: 'rgb(239, 68, 68)',
                    borderWidth: 1
                }, {
                    label: 'GPU (ms)',
                    data: [25, 100, 500, 4000],
                    backgroundColor: 'rgba(37, 99, 235, 0.8)',
                    borderColor: 'rgb(37, 99, 235)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'CPU vs GPU Performance'
                    }
                },
                scales: {
                    y: {
                        type: 'logarithmic',
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Time (ms) - Log Scale'
                        }
                    }
                }
            }
        });
        } else {
            console.log('Line chart canvas not found');
        }
    } catch (error) {
        console.error('Error initializing chart demos:', error);
    }
}

// Scroll Animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, observerOptions);

    // Observe all cards and sections
    const elements = document.querySelectorAll('.card, .section-header, .hero-stats');
    elements.forEach(el => observer.observe(el));
}

// Performance Counters
function initPerformanceCounters() {
    const counters = document.querySelectorAll('.stat-number');

    counters.forEach(counter => {
        const target = parseInt(counter.textContent.replace(/[^\d]/g, ''));
        const suffix = counter.textContent.replace(/[\d]/g, '');
        let current = 0;
        const increment = target / 100;
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            counter.textContent = Math.floor(current) + suffix;
        }, 20);
    });
}

// Code Copy Buttons
function initCodeCopyButtons() {
    const codeBlocks = document.querySelectorAll('.code-block');

    codeBlocks.forEach(block => {
        const copyBtn = document.createElement('button');
        copyBtn.className = 'copy-code-btn';
        copyBtn.innerHTML = '<i class="fas fa-copy"></i>';
        copyBtn.title = 'Copy code';

        copyBtn.addEventListener('click', () => {
            const code = block.textContent;
            navigator.clipboard.writeText(code).then(() => {
                copyBtn.innerHTML = '<i class="fas fa-check"></i>';
                copyBtn.style.color = '#10b981';
                setTimeout(() => {
                    copyBtn.innerHTML = '<i class="fas fa-copy"></i>';
                    copyBtn.style.color = '';
                }, 2000);
            });
        });

        block.style.position = 'relative';
        block.appendChild(copyBtn);
    });
}

// Chart Type Filter
function filterCharts(category) {
    const charts = document.querySelectorAll('.chart-item');
    const buttons = document.querySelectorAll('.filter-btn');

    buttons.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    charts.forEach(chart => {
        if (category === 'all' || chart.dataset.category === category) {
            chart.style.display = 'block';
            chart.classList.add('fade-in-up');
        } else {
            chart.style.display = 'none';
        }
    });
}

// Live Demo Functions
function runDemo(demoType) {
    const demoContainer = document.getElementById('demo-container');
    const demoCode = document.getElementById('demo-code');

    const demos = {
        basic: {
            code: `import vizly as vz

# Create high-performance line chart
fig = vz.Figure()
chart = vz.LineChart(fig)
chart.plot([1, 2, 3, 4], [1, 4, 2, 3])
fig.show()`,
            description: 'Basic line chart with GPU acceleration'
        },
        gpu: {
            code: `import vizly as vz

# GPU-accelerated scatter plot
fig = vz.Figure(gpu=True)
chart = vz.ScatterChart(fig)

# 1M points rendered in <100ms
x = vz.random(1_000_000)
y = vz.random(1_000_000)
chart.scatter(x, y, alpha=0.6)
fig.show()`,
            description: '1M point scatter plot with 50x GPU speedup'
        },
        vr: {
            code: `import vizly as vz

# VR/AR 3D visualization
fig = vz.Figure(mode='vr')
scene = vz.Scene3D(fig)

# Create immersive 3D surface
scene.surface(x, y, z, interactive=True)
scene.enable_hand_tracking()
fig.export_webxr('my_vr_viz.html')`,
            description: 'WebXR VR visualization with hand tracking'
        },
        streaming: {
            code: `import vizly as vz

# Real-time streaming visualization
fig = vz.Figure()
stream = vz.DataStream('ws://localhost:8080')

# Sub-millisecond latency updates
chart = vz.LineChart(fig)
stream.connect(chart.update)
fig.show_live()`,
            description: 'Real-time data streaming with <1ms latency'
        }
    };

    const demo = demos[demoType];
    if (demo) {
        demoCode.textContent = demo.code;
        demoContainer.querySelector('.demo-description').textContent = demo.description;

        // Highlight active demo button
        document.querySelectorAll('.demo-btn').forEach(btn => btn.classList.remove('active'));
        event.target.classList.add('active');
    }
}

// SDK Download
function downloadSDK(language) {
    const downloads = {
        python: 'https://pypi.org/project/vizly/',
        csharp: 'mailto:durai@infinidatum.net?subject=C# SDK Download Request',
        cpp: 'mailto:durai@infinidatum.net?subject=C++ SDK Download Request',
        java: 'mailto:durai@infinidatum.net?subject=Java SDK Download Request'
    };

    if (downloads[language]) {
        window.open(downloads[language], '_blank');
    }
}

// Contact Form
function submitContactForm(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    // Simple form validation
    if (!data.name || !data.email || !data.message) {
        showToast('Please fill in all required fields', 'error');
        return;
    }

    // Simulate form submission
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Sending...';
    submitBtn.disabled = true;

    setTimeout(() => {
        showToast('Message sent successfully! We\'ll get back to you within 24 hours.', 'success');
        form.reset();
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    }, 2000);
}

// Toast Notifications
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;

    document.body.appendChild(toast);

    setTimeout(() => toast.classList.add('show'), 100);

    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => document.body.removeChild(toast), 300);
    }, 5000);
}

// Pricing Calculator
function calculatePricing() {
    const users = parseInt(document.getElementById('users').value) || 1;
    const features = document.getElementById('features').value;
    const support = document.getElementById('support').value;

    let basePrice = 0;

    switch (features) {
        case 'community':
            basePrice = 0;
            break;
        case 'professional':
            basePrice = 5000;
            break;
        case 'enterprise':
            basePrice = 15000;
            break;
    }

    // User scaling
    if (users > 10) {
        basePrice += (users - 10) * 500;
    }

    // Support tier adjustment
    if (support === 'premium') {
        basePrice += 2000;
    }

    const resultElement = document.getElementById('pricing-result');
    if (resultElement) {
        if (basePrice === 0) {
            resultElement.textContent = 'Free';
        } else {
            resultElement.textContent = `$${basePrice.toLocaleString()}/year`;
        }
    }
}

// Search functionality
function searchDocs() {
    const query = document.getElementById('search-input').value.toLowerCase();
    const results = document.getElementById('search-results');

    // Mock search results
    const mockResults = [
        { title: 'Getting Started with Vizly', url: '#getting-started' },
        { title: 'GPU Acceleration Guide', url: '#gpu-guide' },
        { title: 'VR/AR Visualization', url: '#vr-guide' },
        { title: 'Real-time Streaming', url: '#streaming-guide' },
        { title: 'API Reference', url: '#api-reference' }
    ];

    const filtered = mockResults.filter(item =>
        item.title.toLowerCase().includes(query)
    );

    results.innerHTML = filtered.map(item =>
        `<a href="${item.url}" class="search-result">${item.title}</a>`
    ).join('');
}

// Global error handling
window.addEventListener('error', function(e) {
    console.error('Global error:', e.error);
    showToast('An error occurred. Please refresh the page.', 'error');
});

// Performance monitoring
if ('performance' in window) {
    window.addEventListener('load', function() {
        setTimeout(() => {
            const perfData = performance.getEntriesByType('navigation')[0];
            console.log('Page load time:', perfData.loadEventEnd - perfData.loadEventStart, 'ms');
        }, 0);
    });
}