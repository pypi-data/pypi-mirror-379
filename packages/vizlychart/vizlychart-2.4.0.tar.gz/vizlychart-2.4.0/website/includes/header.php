<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="<?php echo SITE_DESCRIPTION; ?>">
    <meta name="keywords" content="visualization, plotting, charts, gpu acceleration, vr, ar, python, c#, java, c++, enterprise">
    <meta name="author" content="<?php echo COMPANY_NAME; ?>">

    <title><?php echo isset($page_title) ? $page_title . ' - ' . SITE_NAME : SITE_TITLE; ?></title>

    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="assets/favicon.ico">

    <!-- CSS -->
    <link rel="stylesheet" href="assets/css/main.css">
    <link rel="stylesheet" href="assets/css/responsive.css">

    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

    <!-- Chart.js for demos -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="<?php echo SITE_URL; ?>">
    <meta property="og:title" content="<?php echo SITE_TITLE; ?>">
    <meta property="og:description" content="<?php echo SITE_DESCRIPTION; ?>">
    <meta property="og:image" content="<?php echo SITE_URL; ?>/assets/images/og-image.png">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="<?php echo SITE_URL; ?>">
    <meta property="twitter:title" content="<?php echo SITE_TITLE; ?>">
    <meta property="twitter:description" content="<?php echo SITE_DESCRIPTION; ?>">
    <meta property="twitter:image" content="<?php echo SITE_URL; ?>/assets/images/og-image.png">
</head>
<body>
    <header class="header">
        <nav class="navbar">
            <div class="container">
                <div class="nav-brand">
                    <a href="index.php" class="logo">
                        <i class="fas fa-chart-line"></i>
                        <span><?php echo SITE_NAME; ?></span>
                        <span class="version">v<?php echo VIZLYCHART_VERSION; ?></span>
                    </a>
                </div>

                <div class="nav-menu" id="nav-menu">
                    <?php foreach ($navigation as $title => $url): ?>
                        <a href="<?php echo $url; ?>" class="nav-link <?php echo basename($_SERVER['PHP_SELF']) == $url ? 'active' : ''; ?>">
                            <?php echo $title; ?>
                        </a>
                    <?php endforeach; ?>
                </div>

                <div class="nav-actions">
                    <a href="https://pypi.org/project/vizlychart/" class="btn btn-outline" target="_blank">
                        <i class="fab fa-python"></i> Install
                    </a>
                    <a href="contact.php" class="btn btn-primary">
                        Get Enterprise
                    </a>
                    <button class="nav-toggle" id="nav-toggle">
                        <span></span>
                        <span></span>
                        <span></span>
                    </button>
                </div>
            </div>
        </nav>
    </header>

    <main class="main-content">