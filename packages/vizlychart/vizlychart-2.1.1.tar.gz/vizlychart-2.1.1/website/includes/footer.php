    </main>

    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3><i class="fas fa-chart-line"></i> <?php echo SITE_NAME; ?></h3>
                    <p>The world's most advanced visualization library with GPU acceleration, VR/AR support, and zero dependencies.</p>
                    <div class="social-links">
                        <a href="https://github.com/vizly/vizly" target="_blank"><i class="fab fa-github"></i></a>
                        <a href="https://pypi.org/project/vizly/" target="_blank"><i class="fab fa-python"></i></a>
                        <a href="mailto:<?php echo CONTACT_EMAIL; ?>"><i class="fas fa-envelope"></i></a>
                    </div>
                </div>

                <div class="footer-section">
                    <h4>Product</h4>
                    <ul>
                        <li><a href="features.php">Features</a></li>
                        <li><a href="pricing.php">Pricing</a></li>
                        <li><a href="gallery.php">Gallery</a></li>
                        <li><a href="documentation.php">Documentation</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h4>SDKs</h4>
                    <ul>
                        <li><a href="https://pypi.org/project/vizly/" target="_blank">Python (PyPI)</a></li>
                        <li><a href="contact.php">C# (.NET)</a></li>
                        <li><a href="contact.php">C++</a></li>
                        <li><a href="contact.php">Java</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h4>Enterprise</h4>
                    <ul>
                        <li><a href="contact.php">Contact Sales</a></li>
                        <li><a href="contact.php">Custom Development</a></li>
                        <li><a href="contact.php">24/7 Support</a></li>
                        <li><a href="contact.php">Licensing</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h4>Quick Start</h4>
                    <div class="quick-install">
                        <code>pip install vizly</code>
                        <button class="copy-btn" onclick="copyToClipboard('pip install vizly')">
                            <i class="fas fa-copy"></i>
                        </button>
                    </div>
                    <p class="version-info">Version <?php echo VIZLY_VERSION; ?> • <?php echo RELEASE_DATE; ?></p>
                </div>
            </div>

            <div class="footer-bottom">
                <div class="footer-legal">
                    <p>&copy; 2024 <?php echo COMPANY_NAME; ?>. All rights reserved.</p>
                    <p>Commercial license required for enterprise features.</p>
                </div>
                <div class="footer-performance">
                    <span class="performance-badge">
                        <i class="fas fa-rocket"></i>
                        50x GPU Speedup
                    </span>
                    <span class="performance-badge">
                        <i class="fas fa-vr-cardboard"></i>
                        VR/AR Ready
                    </span>
                    <span class="performance-badge">
                        <i class="fas fa-globe"></i>
                        Multi-Language
                    </span>
                </div>
            </div>
        </div>
    </footer>

    <!-- JavaScript -->
    <script src="assets/js/main.js"></script>

    <script>
        // Copy to clipboard functionality
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(function() {
                showToast('Copied to clipboard!');
            });
        }

        // Toast notification
        function showToast(message) {
            const toast = document.createElement('div');
            toast.className = 'toast';
            toast.textContent = message;
            document.body.appendChild(toast);

            setTimeout(() => {
                toast.classList.add('show');
            }, 100);

            setTimeout(() => {
                toast.classList.remove('show');
                setTimeout(() => document.body.removeChild(toast), 300);
            }, 2000);
        }
    </script>
</body>
</html>