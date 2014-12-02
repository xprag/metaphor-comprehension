(function (define) {
    'use strict';

    define([
        '../controllers/nav.controller',
        '../controllers/trusted.controller',
        'text!../../templates/nav.html',
        'text!../../templates/trusted.html'
    ], function (navController, trustedController, navTemplate, trustedTemplate) {

        var vendorDir = 'bower_components/';

        return {
            url: '/trusted',
            data: {
                css: [
                    vendorDir + 'bootstrap/dist/css/bootstrap.min.css',
                    'css/main.css'
                ]
            },
            views: {
                navView: {
                    template: navTemplate,
                    controller: navController
                },
                containerView: {
                    template: trustedTemplate,
                    controller: trustedController
                }
            }
        };
    });

}(this.define));
