let mix = require('laravel-mix');

mix.js('src/js/app.js', 'js')
    .css('src/css/app.css','css')
    .setPublicPath('dist')
    .vue({version: 3})