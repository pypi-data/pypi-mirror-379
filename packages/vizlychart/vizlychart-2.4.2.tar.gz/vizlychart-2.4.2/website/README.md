# Vizly Website

A comprehensive PHP website for the Vizly visualization library, showcasing enterprise-grade features, interactive demos, and commercial offerings.

## 🚀 Features

- **Responsive Design**: Mobile-first approach with optimized layouts for all devices
- **Interactive Demos**: Live chart demonstrations with real Chart.js implementations
- **Comprehensive Documentation**: Complete API reference and tutorials
- **Enterprise Features**: Business-focused pages with pricing, contact forms, and enterprise solutions
- **Performance Optimized**: Fast loading with efficient CSS and JavaScript
- **Accessibility**: WCAG compliant with keyboard navigation and screen reader support

## 📁 Project Structure

```
website/
├── includes/
│   ├── config.php          # Site configuration and constants
│   ├── header.php          # Common header with navigation
│   └── footer.php          # Common footer with links
├── assets/
│   ├── css/
│   │   ├── main.css        # Core styles and components
│   │   └── responsive.css   # Mobile and tablet optimizations
│   └── js/
│       └── main.js         # Interactive functionality
├── index.php               # Homepage with hero and features
├── features.php            # Detailed feature showcase
├── pricing.php             # Pricing plans and calculator
├── gallery.php             # Interactive chart gallery
├── contact.php             # Contact forms and enterprise info
├── documentation.php       # Complete API documentation
└── README.md               # This file
```

## 🔧 Setup Instructions

### Requirements

- **PHP 7.4+** (for server-side form processing)
- **Web Server** (Apache, Nginx, or built-in PHP server)
- **Modern Browser** (Chrome, Firefox, Safari, Edge)

### Local Development

1. **Clone or download** the website files to your web server directory

2. **Start a local server**:
   ```bash
   # Using PHP built-in server
   cd website
   php -S localhost:8000

   # Or using Apache/Nginx
   # Place files in htdocs/www directory
   ```

3. **Open in browser**:
   ```
   http://localhost:8000
   ```

### Production Deployment

1. **Upload files** to your web hosting server
2. **Configure domain** to point to the website directory
3. **Set permissions** (755 for directories, 644 for files)
4. **Enable PHP** on your hosting account
5. **Configure SSL** for secure connections

### Environment Configuration

Edit `includes/config.php` to customize:

```php
// Site configuration
define('SITE_NAME', 'Your Company Name');
define('SITE_URL', 'https://your-domain.com');
define('CONTACT_EMAIL', 'your-email@company.com');

// Pricing (update as needed)
$pricing = [
    'professional' => [
        'price' => '$5,000/year',
        // ... other settings
    ]
];
```

## 🎨 Customization

### Styling

**Main styles** (`assets/css/main.css`):
- CSS custom properties for easy color/font changes
- Component-based architecture
- Dark/light mode support

**Responsive design** (`assets/css/responsive.css`):
- Mobile-first breakpoints
- Touch-friendly interactions
- Progressive enhancement

### Colors and Branding

Update CSS custom properties in `main.css`:

```css
:root {
    --primary-color: #2563eb;      /* Your brand color */
    --secondary-color: #10b981;    /* Accent color */
    --company-font: 'Your Font';   /* Custom font */
}
```

### Content Management

**Navigation** - Edit `includes/config.php`:
```php
$navigation = [
    'Home' => 'index.php',
    'Features' => 'features.php',
    'Custom Page' => 'custom.php',
    // Add your pages
];
```

**Pricing plans** - Update in `includes/config.php`:
```php
$pricing = [
    'starter' => [
        'name' => 'Starter Plan',
        'price' => '$99/month',
        'features' => ['Feature 1', 'Feature 2']
    ]
];
```

## 📊 Interactive Features

### Chart Demos

The website includes live Chart.js demonstrations:

- **Gallery page**: 50+ chart type previews
- **Homepage**: Performance comparison charts
- **Documentation**: Code examples with live output

### Performance Calculator

Interactive pricing calculator with:
- Team size selection
- Feature tier comparison
- Real-time cost estimation
- Enterprise volume discounts

### Contact Forms

Server-side PHP form processing:
- Form validation
- Email notifications (configure SMTP)
- Auto-response capabilities
- Enterprise inquiry handling

## 🔒 Security Features

### Form Security

- **CSRF Protection**: Token-based form validation
- **Input Sanitization**: HTML entity encoding
- **Email Validation**: Server-side verification
- **Rate Limiting**: Prevent spam submissions

### Server Security

```php
// In config.php
ini_set('display_errors', 0);          // Hide errors in production
header('X-Content-Type-Options: nosniff');
header('X-Frame-Options: DENY');
header('X-XSS-Protection: 1; mode=block');
```

## 📱 Mobile Optimization

### Responsive Breakpoints

- **Desktop**: 1200px+ (full layout)
- **Tablet**: 768px-1199px (adjusted grids)
- **Mobile**: 320px-767px (stacked layout)
- **Small Mobile**: <480px (minimal layout)

### Touch Interactions

- Minimum 44px touch targets
- Swipe-friendly galleries
- Optimized form inputs
- Fast tap responses

### Performance

- Compressed images
- Minified CSS/JS
- Lazy loading
- Service worker ready

## 🚀 Performance Optimization

### Core Web Vitals

- **LCP**: <2.5s (optimized images/fonts)
- **FID**: <100ms (efficient JavaScript)
- **CLS**: <0.1 (stable layouts)

### Loading Strategy

```html
<!-- Critical CSS inline -->
<style>/* Critical styles */</style>

<!-- Non-critical CSS deferred -->
<link rel="preload" href="assets/css/main.css" as="style" onload="this.onload=null;this.rel='stylesheet'">

<!-- JavaScript optimized -->
<script src="assets/js/main.js" defer></script>
```

## 🔧 Advanced Configuration

### Email Integration

Configure SMTP for contact forms:

```php
// In contact.php
$mail = new PHPMailer(true);
$mail->isSMTP();
$mail->Host = 'smtp.your-provider.com';
$mail->SMTPAuth = true;
$mail->Username = 'your-email@company.com';
$mail->Password = 'your-app-password';
```

### Analytics Integration

Add tracking codes in `includes/header.php`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### CDN Configuration

Optimize asset delivery:

```html
<!-- Use CDN for common libraries -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

## 🐛 Troubleshooting

### Common Issues

**Charts not displaying**:
- Check Chart.js CDN connection
- Verify canvas element IDs
- Ensure JavaScript is enabled

**Forms not submitting**:
- Verify PHP is enabled
- Check file permissions
- Review error logs

**Responsive issues**:
- Clear browser cache
- Check viewport meta tag
- Validate CSS syntax

### Debug Mode

Enable development mode in `config.php`:

```php
if ($_SERVER['HTTP_HOST'] === 'localhost') {
    ini_set('display_errors', 1);
    error_reporting(E_ALL);
    define('DEBUG_MODE', true);
}
```

## 📄 License

This website template is part of the Vizly project. See the main project license for usage terms.

---

## 🤝 Support

For technical support:
- **Documentation**: See individual PHP files for inline comments
- **Issues**: Report bugs through the main Vizly repository
- **Enterprise**: Contact sales for custom development

Built with ❤️ for the Vizly visualization library.