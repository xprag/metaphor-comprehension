(function (define) {
    'use strict';

    define([
        'text!../../templates/nav.html'
    ], function (indexTemplate, navController) {

        var vendorDir = 'bower_components/';

        return {
            url: '/home',
            data: {
                css: [
                    vendorDir + 'bootstrap/dist/css/bootstrap.min.css',
                    'css/main.css'
                ]
            },
            template: indexTemplate
        };
    });
}(this.define))
