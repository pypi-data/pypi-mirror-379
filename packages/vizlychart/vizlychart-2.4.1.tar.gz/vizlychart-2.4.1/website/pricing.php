<?php
$page_title = "Pricing";
require_once 'includes/config.php';
require_once 'includes/header.php';
?>

<section class="hero">
    <div class="container">
        <div class="hero-content">
            <h1>Simple, Transparent Pricing</h1>
            <p>Choose the plan that fits your needs. From free community access to enterprise-grade solutions.</p>
            <div class="pricing-toggle">
                <span class="toggle-label">Monthly</span>
                <label class="toggle-switch">
                    <input type="checkbox" id="annual-toggle">
                    <span class="toggle-slider"></span>
                </label>
                <span class="toggle-label">
                    Annual <span class="discount-badge">Save 20%</span>
                </span>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="pricing-grid">
            <?php foreach ($pricing as $key => $plan): ?>
            <div class="pricing-card <?php echo $key === 'professional' ? 'featured' : ''; ?>">
                <?php if ($key === 'professional'): ?>
                <div class="popular-badge">Most Popular</div>
                <?php endif; ?>

                <div class="plan-header">
                    <h3 class="plan-name"><?php echo $plan['name']; ?></h3>
                    <div class="plan-price">
                        <?php if ($key === 'community'): ?>
                            <span class="price-amount">Free</span>
                            <span class="price-period">Forever</span>
                        <?php elseif ($key === 'professional'): ?>
                            <span class="price-amount monthly-price">$417</span>
                            <span class="price-amount annual-price">$333</span>
                            <span class="price-period">/month</span>
                            <div class="price-note">
                                <span class="monthly-note">$5,000 billed annually</span>
                                <span class="annual-note">$4,000 billed annually (20% off)</span>
                            </div>
                        <?php else: ?>
                            <span class="price-amount">Custom</span>
                            <span class="price-period">Contact us</span>
                        <?php endif; ?>
                    </div>
                </div>

                <div class="plan-features">
                    <ul>
                        <?php foreach ($plan['features'] as $feature): ?>
                        <li><i class="fas fa-check"></i> <?php echo $feature; ?></li>
                        <?php endforeach; ?>
                    </ul>
                </div>

                <div class="plan-action">
                    <?php if ($key === 'community'): ?>
                        <a href="https://pypi.org/project/vizly/" class="btn btn-outline btn-large" target="_blank">
                            <i class="fab fa-python"></i> Install Now
                        </a>
                    <?php elseif ($key === 'professional'): ?>
                        <a href="contact.php" class="btn btn-primary btn-large">
                            <i class="fas fa-rocket"></i> Get Started
                        </a>
                    <?php else: ?>
                        <a href="contact.php" class="btn btn-secondary btn-large">
                            <i class="fas fa-envelope"></i> Contact Sales
                        </a>
                    <?php endif; ?>
                </div>

                <?php if ($key === 'professional'): ?>
                <div class="plan-guarantee">
                    <i class="fas fa-shield-alt"></i>
                    <span>30-day money-back guarantee</span>
                </div>
                <?php endif; ?>
            </div>
            <?php endforeach; ?>
        </div>
    </div>
</section>

<section class="section" style="background: var(--bg-light-secondary);">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">Pricing Calculator</h2>
            <p class="section-subtitle">Estimate your costs based on team size and requirements</p>
        </div>

        <div class="pricing-calculator">
            <div class="calculator-inputs">
                <div class="input-group">
                    <label for="team-size">Team Size</label>
                    <select id="team-size" onchange="calculatePricing()">
                        <option value="1">1-5 developers</option>
                        <option value="10">6-15 developers</option>
                        <option value="25">16-50 developers</option>
                        <option value="100">51+ developers</option>
                    </select>
                </div>

                <div class="input-group">
                    <label for="feature-tier">Feature Tier</label>
                    <select id="feature-tier" onchange="calculatePricing()">
                        <option value="community">Community (Free)</option>
                        <option value="professional" selected>Professional</option>
                        <option value="enterprise">Enterprise</option>
                    </select>
                </div>

                <div class="input-group">
                    <label for="support-level">Support Level</label>
                    <select id="support-level" onchange="calculatePricing()">
                        <option value="standard">Standard Support</option>
                        <option value="premium">Premium 24/7 Support (+$2,000)</option>
                    </select>
                </div>

                <div class="input-group">
                    <label for="deployment">Deployment</label>
                    <select id="deployment" onchange="calculatePricing()">
                        <option value="cloud">Cloud Deployment</option>
                        <option value="onprem">On-Premise (+$3,000)</option>
                        <option value="hybrid">Hybrid Cloud (+$5,000)</option>
                    </select>
                </div>
            </div>

            <div class="calculator-result">
                <div class="result-summary">
                    <h3>Estimated Annual Cost</h3>
                    <div class="result-price" id="calculated-price">$5,000</div>
                    <p class="result-note">Includes all selected features and support</p>
                </div>

                <div class="result-breakdown">
                    <h4>Cost Breakdown</h4>
                    <div class="breakdown-item">
                        <span>Base Professional License</span>
                        <span id="base-cost">Contact for pricing</span>
                    </div>
                    <div class="breakdown-item">
                        <span>Additional Developers</span>
                        <span id="dev-cost">Variable</span>
                    </div>
                    <div class="breakdown-item">
                        <span>Premium Support</span>
                        <span id="support-cost">Optional</span>
                    </div>
                    <div class="breakdown-item">
                        <span>Deployment Options</span>
                        <span id="deployment-cost">Custom</span>
                    </div>
                    <div class="breakdown-total">
                        <span>Total Annual Cost</span>
                        <span id="total-cost">Contact for quote</span>
                    </div>
                </div>

                <a href="contact.php" class="btn btn-primary btn-large">
                    <i class="fas fa-calculator"></i> Get Custom Quote
                </a>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">Feature Comparison</h2>
            <p class="section-subtitle">See what's included in each plan</p>
        </div>

        <div class="comparison-table">
            <table>
                <thead>
                    <tr>
                        <th>Features</th>
                        <th>Community</th>
                        <th>Professional</th>
                        <th>Enterprise</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Python SDK</td>
                        <td><i class="fas fa-check text-success"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                    </tr>
                    <tr>
                        <td>Basic Chart Types (4)</td>
                        <td><i class="fas fa-check text-success"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                    </tr>
                    <tr>
                        <td>PNG/SVG Export</td>
                        <td><i class="fas fa-check text-success"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                    </tr>
                    <tr>
                        <td>All Chart Types (50+)</td>
                        <td><i class="fas fa-times text-danger"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                    </tr>
                    <tr>
                        <td>GPU Acceleration</td>
                        <td><i class="fas fa-times text-danger"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                    </tr>
                    <tr>
                        <td>VR/AR Features</td>
                        <td><i class="fas fa-times text-danger"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                    </tr>
                    <tr>
                        <td>Multi-Language SDKs</td>
                        <td><i class="fas fa-times text-danger"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                    </tr>
                    <tr>
                        <td>Real-time Streaming</td>
                        <td><i class="fas fa-times text-danger"></i></td>
                        <td><i class="fas fa-times text-danger"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                    </tr>
                    <tr>
                        <td>Enterprise Security</td>
                        <td><i class="fas fa-times text-danger"></i></td>
                        <td><i class="fas fa-times text-danger"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                    </tr>
                    <tr>
                        <td>24/7 Support</td>
                        <td><i class="fas fa-times text-danger"></i></td>
                        <td><i class="fas fa-times text-danger"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                    </tr>
                    <tr>
                        <td>Custom Development</td>
                        <td><i class="fas fa-times text-danger"></i></td>
                        <td><i class="fas fa-times text-danger"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                    </tr>
                    <tr>
                        <td>SLA Guarantee</td>
                        <td><i class="fas fa-times text-danger"></i></td>
                        <td><i class="fas fa-times text-danger"></i></td>
                        <td><i class="fas fa-check text-success"></i></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</section>

<section class="section" style="background: var(--gradient-primary); color: white;">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title" style="color: white;">Enterprise Volume Discounts</h2>
            <p class="section-subtitle" style="color: rgba(255,255,255,0.9);">Special pricing for large organizations</p>
        </div>

        <div class="volume-discounts">
            <div class="discount-tier">
                <div class="tier-header">
                    <h3>Growth Organizations</h3>
                    <span class="tier-range">10-50 licenses</span>
                </div>
                <div class="tier-discount">10% Discount</div>
                <ul class="tier-benefits">
                    <li>Volume licensing agreement</li>
                    <li>Dedicated account manager</li>
                    <li>Priority support queue</li>
                    <li>Quarterly business reviews</li>
                </ul>
            </div>

            <div class="discount-tier featured">
                <div class="tier-header">
                    <h3>Enterprise Organizations</h3>
                    <span class="tier-range">50-200 licenses</span>
                </div>
                <div class="tier-discount">20% Discount</div>
                <ul class="tier-benefits">
                    <li>Custom licensing terms</li>
                    <li>On-site training programs</li>
                    <li>24/7 enterprise support</li>
                    <li>Custom feature development</li>
                </ul>
            </div>

            <div class="discount-tier">
                <div class="tier-header">
                    <h3>Global Organizations</h3>
                    <span class="tier-range">200+ licenses</span>
                </div>
                <div class="tier-discount">30% Discount</div>
                <ul class="tier-benefits">
                    <li>Global licensing agreement</li>
                    <li>Dedicated support team</li>
                    <li>Custom deployment architecture</li>
                    <li>White-label solutions available</li>
                </ul>
            </div>
        </div>

        <div class="enterprise-cta">
            <h3>Ready to Scale Your Visualization Capabilities?</h3>
            <p>Contact our enterprise team for custom pricing and deployment options</p>
            <div class="cta-actions">
                <a href="contact.php" class="btn btn-secondary btn-large">
                    <i class="fas fa-envelope"></i> Contact Enterprise Sales
                </a>
                <a href="mailto:durai@infinidatum.net" class="btn btn-outline btn-large">
                    <i class="fas fa-calendar"></i> Schedule Demo
                </a>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">Frequently Asked Questions</h2>
            <p class="section-subtitle">Common questions about pricing and licensing</p>
        </div>

        <div class="faq-grid">
            <div class="faq-item">
                <h4>Can I upgrade or downgrade my plan?</h4>
                <p>Yes, you can change your plan at any time. Upgrades take effect immediately, and downgrades take effect at the next billing cycle. Contact support for assistance.</p>
            </div>

            <div class="faq-item">
                <h4>What payment methods do you accept?</h4>
                <p>We accept all major credit cards, wire transfers, and purchase orders for enterprise customers. Annual plans offer a 20% discount.</p>
            </div>

            <div class="faq-item">
                <h4>Is there a free trial for paid plans?</h4>
                <p>Yes, we offer a 30-day free trial of all Professional and Enterprise features. No credit card required to start your trial.</p>
            </div>

            <div class="faq-item">
                <h4>What's included in enterprise support?</h4>
                <p>Enterprise support includes 24/7 availability, 4-hour response guarantee, dedicated support engineer, on-site training, and custom development services.</p>
            </div>

            <div class="faq-item">
                <h4>Can I use Vizly for commercial projects?</h4>
                <p>Community edition is for personal and educational use. Commercial use requires a Professional or Enterprise license. Contact us for specific licensing questions.</p>
            </div>

            <div class="faq-item">
                <h4>Do you offer academic discounts?</h4>
                <p>Yes, we offer 50% discounts for academic institutions and students. Contact us with your academic email for verification and special pricing.</p>
            </div>
        </div>
    </div>
</section>

<style>
.pricing-toggle {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    margin-top: 2rem;
}

.toggle-label {
    color: rgba(255,255,255,0.9);
    font-weight: 500;
}

.toggle-switch {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 30px;
}

.toggle-switch input {
    opacity: 0;
    width: 0;
    height: 0;
}

.toggle-slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(255,255,255,0.3);
    transition: var(--transition-normal);
    border-radius: 30px;
}

.toggle-slider:before {
    position: absolute;
    content: "";
    height: 22px;
    width: 22px;
    left: 4px;
    bottom: 4px;
    background-color: white;
    transition: var(--transition-normal);
    border-radius: 50%;
}

input:checked + .toggle-slider {
    background-color: var(--secondary-color);
}

input:checked + .toggle-slider:before {
    transform: translateX(30px);
}

.discount-badge {
    background: var(--accent-color);
    color: white;
    padding: 0.25rem 0.5rem;
    border-radius: 1rem;
    font-size: var(--font-size-xs);
    font-weight: 500;
}

.pricing-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.pricing-card {
    background: white;
    border-radius: 1rem;
    padding: 2rem;
    box-shadow: var(--shadow-lg);
    position: relative;
    transition: var(--transition-normal);
    border: 2px solid transparent;
}

.pricing-card.featured {
    border-color: var(--primary-color);
    transform: scale(1.05);
    z-index: 1;
}

.pricing-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-xl);
}

.pricing-card.featured:hover {
    transform: scale(1.05) translateY(-5px);
}

.popular-badge {
    position: absolute;
    top: -10px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--gradient-primary);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 1rem;
    font-size: var(--font-size-sm);
    font-weight: 500;
}

.plan-header {
    text-align: center;
    margin-bottom: 2rem;
}

.plan-name {
    font-size: var(--font-size-2xl);
    margin-bottom: 1rem;
    color: var(--text-light);
}

.plan-price {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.price-amount {
    font-size: 3rem;
    font-weight: 700;
    color: var(--primary-color);
    line-height: 1;
}

.price-period {
    color: var(--text-light-secondary);
    font-size: var(--font-size-lg);
}

.price-note {
    margin-top: 0.5rem;
    font-size: var(--font-size-sm);
    color: var(--text-light-secondary);
}

.annual-price,
.annual-note {
    display: none;
}

.plan-features {
    margin-bottom: 2rem;
}

.plan-features ul {
    list-style: none;
    padding: 0;
}

.plan-features li {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0.75rem;
    color: var(--text-light-secondary);
}

.plan-features li i {
    color: var(--secondary-color);
    width: 16px;
}

.plan-action {
    margin-bottom: 1rem;
}

.plan-guarantee {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    color: var(--text-light-secondary);
    font-size: var(--font-size-sm);
}

.plan-guarantee i {
    color: var(--secondary-color);
}

.pricing-calculator {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    background: white;
    border-radius: 1rem;
    padding: 2rem;
    box-shadow: var(--shadow-lg);
}

.calculator-inputs {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.input-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.input-group label {
    font-weight: 500;
    color: var(--text-light);
}

.input-group select {
    padding: 0.75rem;
    border: 2px solid var(--bg-light-secondary);
    border-radius: 0.5rem;
    font-size: var(--font-size-base);
    background: white;
    transition: var(--transition-fast);
}

.input-group select:focus {
    outline: none;
    border-color: var(--primary-color);
}

.calculator-result {
    display: flex;
    flex-direction: column;
    gap: 2rem;
}

.result-summary {
    text-align: center;
    padding: 2rem;
    background: var(--gradient-primary);
    color: white;
    border-radius: 1rem;
}

.result-price {
    font-size: 3rem;
    font-weight: 700;
    margin: 1rem 0;
}

.result-breakdown {
    background: var(--bg-light-secondary);
    padding: 1.5rem;
    border-radius: 0.5rem;
}

.breakdown-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.75rem;
    color: var(--text-light-secondary);
}

.breakdown-total {
    display: flex;
    justify-content: space-between;
    padding-top: 0.75rem;
    border-top: 2px solid var(--primary-color);
    font-weight: 600;
    color: var(--text-light);
}

.comparison-table {
    overflow-x: auto;
    background: white;
    border-radius: 1rem;
    box-shadow: var(--shadow-lg);
}

.comparison-table table {
    width: 100%;
    border-collapse: collapse;
}

.comparison-table th,
.comparison-table td {
    padding: 1rem;
    text-align: center;
    border-bottom: 1px solid var(--bg-light-secondary);
}

.comparison-table th {
    background: var(--gradient-primary);
    color: white;
    font-weight: 600;
}

.comparison-table th:first-child,
.comparison-table td:first-child {
    text-align: left;
    font-weight: 500;
}

.text-success {
    color: var(--secondary-color);
}

.text-danger {
    color: var(--danger-color);
}

.volume-discounts {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
}

.discount-tier {
    background: rgba(255,255,255,0.1);
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    border: 2px solid transparent;
    transition: var(--transition-normal);
}

.discount-tier.featured {
    border-color: var(--accent-color);
    transform: scale(1.05);
}

.discount-tier:hover {
    transform: translateY(-5px);
    background: rgba(255,255,255,0.15);
}

.discount-tier.featured:hover {
    transform: scale(1.05) translateY(-5px);
}

.tier-header {
    margin-bottom: 1.5rem;
}

.tier-header h3 {
    color: white;
    margin-bottom: 0.5rem;
}

.tier-range {
    color: rgba(255,255,255,0.8);
    font-size: var(--font-size-sm);
}

.tier-discount {
    font-size: var(--font-size-3xl);
    font-weight: 700;
    color: var(--accent-color);
    margin-bottom: 1.5rem;
}

.tier-benefits {
    list-style: none;
    padding: 0;
    text-align: left;
}

.tier-benefits li {
    margin-bottom: 0.5rem;
    color: rgba(255,255,255,0.9);
    position: relative;
    padding-left: 1.5rem;
}

.tier-benefits li::before {
    content: '✓';
    position: absolute;
    left: 0;
    color: var(--accent-color);
    font-weight: bold;
}

.enterprise-cta {
    text-align: center;
    padding: 3rem 0;
    border-top: 1px solid rgba(255,255,255,0.2);
}

.enterprise-cta h3 {
    color: white;
    margin-bottom: 1rem;
}

.enterprise-cta p {
    color: rgba(255,255,255,0.9);
    margin-bottom: 2rem;
}

.cta-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}

.faq-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
}

.faq-item {
    background: white;
    border-radius: 1rem;
    padding: 2rem;
    box-shadow: var(--shadow-lg);
    transition: var(--transition-normal);
}

.faq-item:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-xl);
}

.faq-item h4 {
    color: var(--text-light);
    margin-bottom: 1rem;
}

.faq-item p {
    color: var(--text-light-secondary);
    line-height: 1.6;
}

/* Annual toggle behavior */
#annual-toggle:checked ~ .pricing-grid .monthly-price {
    display: none;
}

#annual-toggle:checked ~ .pricing-grid .annual-price {
    display: block;
}

#annual-toggle:checked ~ .pricing-grid .monthly-note {
    display: none;
}

#annual-toggle:checked ~ .pricing-grid .annual-note {
    display: block;
}

@media (prefers-color-scheme: dark) {
    .pricing-card,
    .pricing-calculator,
    .comparison-table,
    .faq-item {
        background: var(--bg-dark-secondary);
        border: 1px solid rgba(255,255,255,0.05);
    }

    .plan-name {
        color: var(--text-dark);
    }

    .input-group label {
        color: var(--text-dark);
    }

    .input-group select {
        background: var(--bg-dark);
        border-color: rgba(255,255,255,0.1);
        color: var(--text-dark);
    }

    .result-breakdown {
        background: var(--bg-dark);
    }

    .breakdown-total {
        color: var(--text-dark);
    }

    .comparison-table th {
        background: var(--gradient-primary);
    }

    .comparison-table td {
        color: var(--text-dark-secondary);
    }

    .comparison-table td:first-child {
        color: var(--text-dark);
    }

    .faq-item h4 {
        color: var(--text-dark);
    }
}

@media (max-width: 768px) {
    .pricing-grid {
        grid-template-columns: 1fr;
    }

    .pricing-card.featured {
        transform: none;
    }

    .pricing-calculator {
        grid-template-columns: 1fr;
        gap: 2rem;
    }

    .cta-actions {
        flex-direction: column;
        align-items: center;
    }

    .volume-discounts {
        grid-template-columns: 1fr;
    }

    .discount-tier.featured {
        transform: none;
    }

    .faq-grid {
        grid-template-columns: 1fr;
    }
}
</style>

<script>
function calculatePricing() {
    const teamSize = parseInt(document.getElementById('team-size').value);
    const featureTier = document.getElementById('feature-tier').value;
    const supportLevel = document.getElementById('support-level').value;
    const deployment = document.getElementById('deployment').value;

    let baseCost = 0;
    let devCost = 0;
    let supportCost = 0;
    let deploymentCost = 0;

    // Base cost calculation
    switch (featureTier) {
        case 'community':
            baseCost = 0;
            break;
        case 'professional':
            baseCost = 5000;
            break;
        case 'enterprise':
            baseCost = 15000;
            break;
    }

    // Additional developers
    if (teamSize > 5 && featureTier !== 'community') {
        devCost = (teamSize - 5) * 500;
    }

    // Support level
    if (supportLevel === 'premium' && featureTier !== 'community') {
        supportCost = 2000;
    }

    // Deployment options
    if (featureTier !== 'community') {
        switch (deployment) {
            case 'onprem':
                deploymentCost = 3000;
                break;
            case 'hybrid':
                deploymentCost = 5000;
                break;
        }
    }

    const totalCost = baseCost + devCost + supportCost + deploymentCost;

    // Update display
    document.getElementById('calculated-price').textContent = totalCost === 0 ? 'Free' : `$${totalCost.toLocaleString()}`;
    document.getElementById('base-cost').textContent = `$${baseCost.toLocaleString()}`;
    document.getElementById('dev-cost').textContent = `$${devCost.toLocaleString()}`;
    document.getElementById('support-cost').textContent = `$${supportCost.toLocaleString()}`;
    document.getElementById('deployment-cost').textContent = `$${deploymentCost.toLocaleString()}`;
    document.getElementById('total-cost').textContent = totalCost === 0 ? 'Free' : `$${totalCost.toLocaleString()}`;
}

// Initialize calculator
document.addEventListener('DOMContentLoaded', function() {
    calculatePricing();

    // Annual toggle functionality
    const annualToggle = document.getElementById('annual-toggle');
    if (annualToggle) {
        annualToggle.addEventListener('change', function() {
            const monthlyPrices = document.querySelectorAll('.monthly-price');
            const annualPrices = document.querySelectorAll('.annual-price');
            const monthlyNotes = document.querySelectorAll('.monthly-note');
            const annualNotes = document.querySelectorAll('.annual-note');

            if (this.checked) {
                monthlyPrices.forEach(el => el.style.display = 'none');
                annualPrices.forEach(el => el.style.display = 'block');
                monthlyNotes.forEach(el => el.style.display = 'none');
                annualNotes.forEach(el => el.style.display = 'block');
            } else {
                monthlyPrices.forEach(el => el.style.display = 'block');
                annualPrices.forEach(el => el.style.display = 'none');
                monthlyNotes.forEach(el => el.style.display = 'block');
                annualNotes.forEach(el => el.style.display = 'none');
            }
        });
    }
});
</script>

<?php require_once 'includes/footer.php'; ?>