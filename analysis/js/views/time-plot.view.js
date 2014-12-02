(function (define) {
    'use strict';

    define([
        '../controllers/nav.controller',
        'text!../../templates/nav.html',
        '../controllers/time-plot.controller',
        'text!../../templates/time-plot.html',
    ], function (navController, navTemplate, timePlotController, timePlotTemplate) {

        var vendorDir = 'bower_components/';

        return {
            url: '/time-plot',
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
                    template: timePlotTemplate,
                    controller: timePlotController
                }
            }
        };

    });
}(this.define));
