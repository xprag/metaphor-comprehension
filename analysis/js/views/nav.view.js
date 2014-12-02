(function (define) {
    'use strict';

    define([
        'text!../../templates/nav.html',
        '../controllers/nav.controller'
    ], function (indexTemplate, navController) {

        var vendorDir = 'bower_components/';

        return {
            url: '/',
            data: {
                css: [
                    vendorDir + 'bootstrap/dist/css/bootstrap.min.css',
                    'css/main.css'
                ]
            },
            views: {
                navView: {
                    template: indexTemplate,
                    controller: navController
                }
            }
        };
    });
}(this.define))
