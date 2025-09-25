<?php
$page_title = "Contact";
require_once 'includes/config.php';
require_once 'includes/header.php';

// Handle form submission (basic server-side processing)
$form_submitted = false;
$form_message = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name'] ?? '');
    $email = trim($_POST['email'] ?? '');
    $company = trim($_POST['company'] ?? '');
    $title = trim($_POST['title'] ?? '');
    $inquiry_type = $_POST['inquiry_type'] ?? '';
    $message = trim($_POST['message'] ?? '');

    // Basic validation
    if (empty($name) || empty($email) || empty($message)) {
        $form_message = 'Please fill in all required fields.';
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $form_message = 'Please enter a valid email address.';
    } else {
        // In a real application, you would process the form data here
        // For demo purposes, we'll just show a success message
        $form_submitted = true;
        $form_message = 'Thank you for your message! We\'ll get back to you within 24 hours.';

        // Here you would typically:
        // - Send email to sales team
        // - Save to database
        // - Integrate with CRM
        // - Send auto-reply email
    }
}
?>

<section class="hero">
    <div class="container">
        <div class="hero-content">
            <h1>Get in Touch</h1>
            <p>Ready to transform your data visualization? Contact our team for demos, pricing, and enterprise solutions.</p>
            <div class="contact-highlights">
                <div class="highlight-item">
                    <i class="fas fa-clock"></i>
                    <span>24-hour response time</span>
                </div>
                <div class="highlight-item">
                    <i class="fas fa-shield-alt"></i>
                    <span>Enterprise security certified</span>
                </div>
                <div class="highlight-item">
                    <i class="fas fa-globe"></i>
                    <span>Global support available</span>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="contact-grid">
            <div class="contact-form-section">
                <div class="form-header">
                    <h2>Send us a Message</h2>
                    <p>Fill out the form below and we'll get back to you within 24 hours</p>
                </div>

                <?php if ($form_message): ?>
                <div class="form-message <?php echo $form_submitted ? 'success' : 'error'; ?>">
                    <i class="fas <?php echo $form_submitted ? 'fa-check-circle' : 'fa-exclamation-circle'; ?>"></i>
                    <?php echo htmlspecialchars($form_message); ?>
                </div>
                <?php endif; ?>

                <form class="contact-form" method="POST" action="">
                    <div class="form-row">
                        <div class="form-group">
                            <label for="name">Full Name *</label>
                            <input type="text" id="name" name="name" required
                                   value="<?php echo htmlspecialchars($_POST['name'] ?? ''); ?>">
                        </div>
                        <div class="form-group">
                            <label for="email">Email Address *</label>
                            <input type="email" id="email" name="email" required
                                   value="<?php echo htmlspecialchars($_POST['email'] ?? ''); ?>">
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="form-group">
                            <label for="company">Company</label>
                            <input type="text" id="company" name="company"
                                   value="<?php echo htmlspecialchars($_POST['company'] ?? ''); ?>">
                        </div>
                        <div class="form-group">
                            <label for="title">Job Title</label>
                            <input type="text" id="title" name="title"
                                   value="<?php echo htmlspecialchars($_POST['title'] ?? ''); ?>"
                                   placeholder="e.g., Data Scientist, CTO">
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="inquiry_type">Inquiry Type</label>
                        <select id="inquiry_type" name="inquiry_type">
                            <option value="">Select inquiry type</option>
                            <option value="sales" <?php echo ($_POST['inquiry_type'] ?? '') === 'sales' ? 'selected' : ''; ?>>
                                Sales & Pricing
                            </option>
                            <option value="technical" <?php echo ($_POST['inquiry_type'] ?? '') === 'technical' ? 'selected' : ''; ?>>
                                Technical Support
                            </option>
                            <option value="enterprise" <?php echo ($_POST['inquiry_type'] ?? '') === 'enterprise' ? 'selected' : ''; ?>>
                                Enterprise Solutions
                            </option>
                            <option value="partnership" <?php echo ($_POST['inquiry_type'] ?? '') === 'partnership' ? 'selected' : ''; ?>>
                                Partnership
                            </option>
                            <option value="demo" <?php echo ($_POST['inquiry_type'] ?? '') === 'demo' ? 'selected' : ''; ?>>
                                Request Demo
                            </option>
                            <option value="other" <?php echo ($_POST['inquiry_type'] ?? '') === 'other' ? 'selected' : ''; ?>>
                                Other
                            </option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="message">Message *</label>
                        <textarea id="message" name="message" rows="6" required
                                  placeholder="Tell us about your project and requirements..."><?php echo htmlspecialchars($_POST['message'] ?? ''); ?></textarea>
                    </div>

                    <div class="form-group">
                        <label class="checkbox-label">
                            <input type="checkbox" name="newsletter" value="1"
                                   <?php echo !empty($_POST['newsletter']) ? 'checked' : ''; ?>>
                            <span class="checkmark"></span>
                            Subscribe to our newsletter for updates and new features
                        </label>
                    </div>

                    <div class="form-actions">
                        <button type="submit" class="btn btn-primary btn-large">
                            <i class="fas fa-paper-plane"></i> Send Message
                        </button>
                        <p class="form-note">
                            By submitting this form, you agree to our
                            <a href="#" onclick="showPrivacyPolicy()">Privacy Policy</a>
                        </p>
                    </div>
                </form>
            </div>

            <div class="contact-info-section">
                <div class="contact-methods">
                    <h3>Contact Information</h3>

                    <div class="contact-method">
                        <div class="method-icon">
                            <i class="fas fa-envelope"></i>
                        </div>
                        <div class="method-info">
                            <h4>Email</h4>
                            <p><a href="mailto:<?php echo CONTACT_EMAIL; ?>"><?php echo CONTACT_EMAIL; ?></a></p>
                            <span class="response-time">Response within 24 hours</span>
                        </div>
                    </div>

                    <div class="contact-method">
                        <div class="method-icon">
                            <i class="fas fa-headset"></i>
                        </div>
                        <div class="method-info">
                            <h4>Support</h4>
                            <p><a href="mailto:durai@infinidatum.net">Professional Support</a></p>
                            <span class="response-time">24-hour response time</span>
                        </div>
                    </div>

                    <div class="contact-method">
                        <div class="method-icon">
                            <i class="fas fa-comments"></i>
                        </div>
                        <div class="method-info">
                            <h4>Live Chat</h4>
                            <p>Available on our website</p>
                            <span class="response-time">Mon-Fri 9AM-6PM PST</span>
                        </div>
                    </div>

                    <div class="contact-method">
                        <div class="method-icon">
                            <i class="fab fa-github"></i>
                        </div>
                        <div class="method-info">
                            <h4>GitHub</h4>
                            <p><a href="https://github.com/vizly/vizly" target="_blank">github.com/vizly/vizly</a></p>
                            <span class="response-time">Community support</span>
                        </div>
                    </div>
                </div>

                <div class="enterprise-contact">
                    <h3>Enterprise Sales</h3>
                    <div class="enterprise-card">
                        <div class="enterprise-icon">
                            <i class="fas fa-building"></i>
                        </div>
                        <h4>Custom Enterprise Solutions</h4>
                        <p>Get dedicated support, custom development, and volume pricing for your organization.</p>
                        <ul>
                            <li><i class="fas fa-check"></i> Dedicated account manager</li>
                            <li><i class="fas fa-check"></i> 24/7 enterprise support</li>
                            <li><i class="fas fa-check"></i> Custom feature development</li>
                            <li><i class="fas fa-check"></i> On-site training programs</li>
                        </ul>
                        <a href="mailto:<?php echo CONTACT_EMAIL; ?>?subject=Enterprise%20Inquiry" class="btn btn-secondary">
                            <i class="fas fa-envelope"></i> Contact Enterprise Sales
                        </a>
                    </div>
                </div>

                <div class="support-resources">
                    <h3>Self-Service Resources</h3>
                    <div class="resource-links">
                        <a href="documentation.php" class="resource-link">
                            <i class="fas fa-book"></i>
                            <div>
                                <h4>Documentation</h4>
                                <p>Complete API reference and guides</p>
                            </div>
                        </a>
                        <a href="gallery.php" class="resource-link">
                            <i class="fas fa-images"></i>
                            <div>
                                <h4>Examples Gallery</h4>
                                <p>Live demos and code samples</p>
                            </div>
                        </a>
                        <a href="https://pypi.org/project/vizly/" class="resource-link" target="_blank">
                            <i class="fab fa-python"></i>
                            <div>
                                <h4>PyPI Package</h4>
                                <p>Installation and version info</p>
                            </div>
                        </a>
                        <a href="#" onclick="showFAQ()" class="resource-link">
                            <i class="fas fa-question-circle"></i>
                            <div>
                                <h4>FAQ</h4>
                                <p>Common questions and answers</p>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section" style="background: var(--bg-light-secondary);">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">Office Locations</h2>
            <p class="section-subtitle">Global presence with local support</p>
        </div>

        <div class="offices-grid">
            <div class="office-card">
                <div class="office-flag">🇺🇸</div>
                <h3>Hartford, Connecticut</h3>
                <div class="office-details">
                    <p><strong>US Operations</strong></p>
                    <p>Hartford, CT</p>
                    <p><i class="fas fa-clock"></i> EST (UTC-5)</p>
                </div>
                <div class="office-features">
                    <span class="feature">Sales</span>
                    <span class="feature">Engineering</span>
                    <span class="feature">Support</span>
                </div>
            </div>

            <div class="office-card">
                <div class="office-flag">🇮🇳</div>
                <h3>Chennai, Tamil Nadu</h3>
                <div class="office-details">
                    <p><strong>Development Center</strong></p>
                    <p>Chennai, TN, India</p>
                    <p><i class="fas fa-clock"></i> IST (UTC+5:30)</p>
                </div>
                <div class="office-features">
                    <span class="feature">Development</span>
                    <span class="feature">Engineering</span>
                    <span class="feature">Support</span>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">Frequently Asked Questions</h2>
            <p class="section-subtitle">Quick answers to common questions</p>
        </div>

        <div class="faq-container">
            <div class="faq-item">
                <div class="faq-question" onclick="toggleFAQ(this)">
                    <h4>How quickly can I get started with Vizly?</h4>
                    <i class="fas fa-plus"></i>
                </div>
                <div class="faq-answer">
                    <p>You can start immediately! Install the community edition with <code>pip install vizlychart</code> and begin creating charts in minutes. For enterprise features, contact us for a demo and we can have you set up within 24 hours.</p>
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question" onclick="toggleFAQ(this)">
                    <h4>What's the difference between community and enterprise editions?</h4>
                    <i class="fas fa-plus"></i>
                </div>
                <div class="faq-answer">
                    <p>Community edition includes basic chart types and Python SDK. Enterprise adds GPU acceleration, VR/AR features, real-time streaming, multi-language SDKs, 24/7 support, and custom development services.</p>
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question" onclick="toggleFAQ(this)">
                    <h4>Do you offer training and implementation services?</h4>
                    <i class="fas fa-plus"></i>
                </div>
                <div class="faq-answer">
                    <p>Yes! We provide comprehensive training programs, implementation consulting, and dedicated support for enterprise customers. Our team can help you integrate Vizly into your existing workflows and maximize its potential.</p>
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question" onclick="toggleFAQ(this)">
                    <h4>What are your security and compliance certifications?</h4>
                    <i class="fas fa-plus"></i>
                </div>
                <div class="faq-answer">
                    <p>Vizly Enterprise is GDPR, HIPAA, and SOX compliant. We provide enterprise-grade security features including data encryption, access controls, audit logging, and support for on-premise deployments.</p>
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question" onclick="toggleFAQ(this)">
                    <h4>Can I try enterprise features before purchasing?</h4>
                    <i class="fas fa-plus"></i>
                </div>
                <div class="faq-answer">
                    <p>Absolutely! We offer a 30-day free trial of all enterprise features. Contact us to set up your trial environment and get hands-on experience with GPU acceleration, VR/AR, and streaming capabilities.</p>
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question" onclick="toggleFAQ(this)">
                    <h4>What support options are available?</h4>
                    <i class="fas fa-plus"></i>
                </div>
                <div class="faq-answer">
                    <p>Community users get forum support. Professional users receive email support with 48-hour response. Enterprise customers get 24/7 support with 4-hour response guarantee, dedicated support engineer, and priority access.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<style>
.contact-highlights {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 2rem;
    flex-wrap: wrap;
}

.highlight-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: rgba(255,255,255,0.9);
    font-size: var(--font-size-sm);
}

.highlight-item i {
    color: var(--accent-color);
}

.contact-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 4rem;
    align-items: start;
}

.contact-form-section {
    background: white;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: var(--shadow-lg);
}

.form-header {
    margin-bottom: 2rem;
    text-align: center;
}

.form-header h2 {
    color: var(--text-light);
    margin-bottom: 0.5rem;
}

.form-header p {
    color: var(--text-light-secondary);
}

.form-message {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 2rem;
    font-weight: 500;
}

.form-message.success {
    background: rgba(16, 185, 129, 0.1);
    color: var(--secondary-color);
    border: 1px solid rgba(16, 185, 129, 0.2);
}

.form-message.error {
    background: rgba(239, 68, 68, 0.1);
    color: var(--danger-color);
    border: 1px solid rgba(239, 68, 68, 0.2);
}

.contact-form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.form-group label {
    font-weight: 500;
    color: var(--text-light);
}

.form-group input,
.form-group select,
.form-group textarea {
    padding: 0.75rem;
    border: 2px solid var(--bg-light-secondary);
    border-radius: 0.5rem;
    font-size: var(--font-size-base);
    transition: var(--transition-fast);
    background: white;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-group textarea {
    resize: vertical;
    min-height: 120px;
}

.checkbox-label {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    cursor: pointer;
    font-size: var(--font-size-sm);
    color: var(--text-light-secondary);
}

.checkbox-label input[type="checkbox"] {
    display: none;
}

.checkmark {
    width: 20px;
    height: 20px;
    border: 2px solid var(--bg-light-secondary);
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: var(--transition-fast);
    flex-shrink: 0;
}

.checkbox-label input[type="checkbox"]:checked + .checkmark {
    background: var(--primary-color);
    border-color: var(--primary-color);
}

.checkbox-label input[type="checkbox"]:checked + .checkmark::after {
    content: '✓';
    color: white;
    font-size: 12px;
    font-weight: bold;
}

.form-actions {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    align-items: center;
    margin-top: 1rem;
}

.form-note {
    font-size: var(--font-size-sm);
    color: var(--text-light-secondary);
    text-align: center;
}

.form-note a {
    color: var(--primary-color);
    text-decoration: none;
}

.form-note a:hover {
    text-decoration: underline;
}

.contact-info-section {
    display: flex;
    flex-direction: column;
    gap: 2rem;
}

.contact-methods {
    background: white;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: var(--shadow-lg);
}

.contact-methods h3 {
    margin-bottom: 1.5rem;
    color: var(--text-light);
}

.contact-method {
    display: flex;
    gap: 1rem;
    padding: 1rem 0;
    border-bottom: 1px solid var(--bg-light-secondary);
}

.contact-method:last-child {
    border-bottom: none;
}

.method-icon {
    width: 50px;
    height: 50px;
    background: var(--gradient-primary);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1.25rem;
    flex-shrink: 0;
}

.method-info h4 {
    margin-bottom: 0.25rem;
    color: var(--text-light);
}

.method-info p {
    margin-bottom: 0.25rem;
}

.method-info a {
    color: var(--primary-color);
    text-decoration: none;
}

.method-info a:hover {
    text-decoration: underline;
}

.response-time {
    font-size: var(--font-size-sm);
    color: var(--text-light-secondary);
}

.enterprise-contact {
    background: white;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: var(--shadow-lg);
}

.enterprise-contact h3 {
    margin-bottom: 1.5rem;
    color: var(--text-light);
}

.enterprise-card {
    text-align: center;
}

.enterprise-icon {
    width: 80px;
    height: 80px;
    background: var(--gradient-secondary);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 2rem;
    margin: 0 auto 1rem;
}

.enterprise-card h4 {
    margin-bottom: 1rem;
    color: var(--text-light);
}

.enterprise-card p {
    margin-bottom: 1.5rem;
    color: var(--text-light-secondary);
}

.enterprise-card ul {
    list-style: none;
    padding: 0;
    margin-bottom: 2rem;
    text-align: left;
}

.enterprise-card li {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
    color: var(--text-light-secondary);
}

.enterprise-card li i {
    color: var(--secondary-color);
    width: 16px;
}

.support-resources {
    background: white;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: var(--shadow-lg);
}

.support-resources h3 {
    margin-bottom: 1.5rem;
    color: var(--text-light);
}

.resource-links {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.resource-link {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
    border-radius: 0.5rem;
    text-decoration: none;
    color: var(--text-light);
    transition: var(--transition-fast);
    border: 1px solid var(--bg-light-secondary);
}

.resource-link:hover {
    background: var(--bg-light-secondary);
    transform: translateX(5px);
}

.resource-link i {
    color: var(--primary-color);
    font-size: 1.25rem;
    width: 20px;
}

.resource-link h4 {
    margin-bottom: 0.25rem;
    color: var(--text-light);
}

.resource-link p {
    margin: 0;
    font-size: var(--font-size-sm);
    color: var(--text-light-secondary);
}

.offices-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.office-card {
    background: white;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: var(--shadow-lg);
    text-align: center;
    transition: var(--transition-normal);
}

.office-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-xl);
}

.office-flag {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.office-card h3 {
    margin-bottom: 1rem;
    color: var(--text-light);
}

.office-details {
    margin-bottom: 1.5rem;
}

.office-details p {
    margin-bottom: 0.5rem;
    color: var(--text-light-secondary);
}

.office-details strong {
    color: var(--text-light);
}

.office-features {
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    flex-wrap: wrap;
}

.office-features .feature {
    background: var(--gradient-primary);
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: var(--font-size-sm);
    font-weight: 500;
}

.faq-container {
    max-width: 800px;
    margin: 0 auto;
}

.faq-item {
    background: white;
    border-radius: 1rem;
    margin-bottom: 1rem;
    box-shadow: var(--shadow-lg);
    overflow: hidden;
}

.faq-question {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem;
    cursor: pointer;
    transition: var(--transition-fast);
}

.faq-question:hover {
    background: var(--bg-light-secondary);
}

.faq-question h4 {
    margin: 0;
    color: var(--text-light);
}

.faq-question i {
    color: var(--primary-color);
    transition: var(--transition-fast);
}

.faq-question.active i {
    transform: rotate(45deg);
}

.faq-answer {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
}

.faq-answer.active {
    max-height: 300px;
}

.faq-answer p {
    padding: 0 1.5rem 1.5rem;
    margin: 0;
    color: var(--text-light-secondary);
    line-height: 1.6;
}

.faq-answer code {
    background: var(--bg-light-secondary);
    padding: 0.25rem 0.5rem;
    border-radius: 0.25rem;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: var(--font-size-sm);
    color: var(--primary-color);
}

@media (prefers-color-scheme: dark) {
    .contact-form-section,
    .contact-methods,
    .enterprise-contact,
    .support-resources,
    .office-card,
    .faq-item {
        background: var(--bg-dark-secondary);
        border: 1px solid rgba(255,255,255,0.05);
    }

    .form-header h2,
    .contact-methods h3,
    .enterprise-contact h3,
    .support-resources h3,
    .office-card h3,
    .faq-question h4 {
        color: var(--text-dark);
    }

    .form-group label,
    .method-info h4,
    .enterprise-card h4,
    .resource-link h4,
    .office-details strong {
        color: var(--text-dark);
    }

    .form-group input,
    .form-group select,
    .form-group textarea {
        background: var(--bg-dark);
        border-color: rgba(255,255,255,0.1);
        color: var(--text-dark);
    }

    .form-group input:focus,
    .form-group select:focus,
    .form-group textarea:focus {
        border-color: var(--primary-color);
    }

    .checkmark {
        border-color: rgba(255,255,255,0.1);
    }

    .resource-link {
        color: var(--text-dark);
        border-color: rgba(255,255,255,0.1);
    }

    .resource-link:hover {
        background: var(--bg-dark);
    }

    .faq-question:hover {
        background: var(--bg-dark);
    }

    .faq-answer code {
        background: var(--bg-dark);
    }
}

@media (max-width: 768px) {
    .contact-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
    }

    .form-row {
        grid-template-columns: 1fr;
    }

    .contact-highlights {
        flex-direction: column;
        align-items: center;
    }

    .offices-grid {
        grid-template-columns: 1fr;
    }

    .contact-form-section,
    .contact-methods,
    .enterprise-contact,
    .support-resources {
        padding: 1.5rem;
    }
}
</style>

<script>
function toggleFAQ(element) {
    const answer = element.nextElementSibling;
    const icon = element.querySelector('i');

    // Close all other FAQs
    document.querySelectorAll('.faq-question').forEach(q => {
        if (q !== element) {
            q.classList.remove('active');
            q.nextElementSibling.classList.remove('active');
            q.querySelector('i').style.transform = 'rotate(0deg)';
        }
    });

    // Toggle current FAQ
    element.classList.toggle('active');
    answer.classList.toggle('active');

    if (answer.classList.contains('active')) {
        icon.style.transform = 'rotate(45deg)';
    } else {
        icon.style.transform = 'rotate(0deg)';
    }
}

function showPrivacyPolicy() {
    alert('Privacy Policy: We respect your privacy and will only use your information to respond to your inquiry and provide relevant updates if you opt in. We do not sell or share your data with third parties.');
}

function showFAQ() {
    document.querySelector('.faq-container').scrollIntoView({ behavior: 'smooth' });
}

// Form validation enhancement
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.contact-form');
    const inputs = form.querySelectorAll('input[required], textarea[required]');

    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (this.value.trim() === '') {
                this.style.borderColor = 'var(--danger-color)';
            } else {
                this.style.borderColor = 'var(--secondary-color)';
            }
        });

        input.addEventListener('input', function() {
            if (this.value.trim() !== '') {
                this.style.borderColor = 'var(--secondary-color)';
            }
        });
    });

    // Email validation
    const emailInput = document.getElementById('email');
    emailInput.addEventListener('blur', function() {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(this.value)) {
            this.style.borderColor = 'var(--danger-color)';
        } else {
            this.style.borderColor = 'var(--secondary-color)';
        }
    });
});
</script>

<?php require_once 'includes/footer.php'; ?>