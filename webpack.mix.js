const mix = require('laravel-mix');

mix.sass('resources/scss/dashboard/dashboard.scss', 'static/dashboard/css/')
    .sass('resources/scss/frontend/styles.scss', 'static/shop/css/')
   .setPublicPath('static');
