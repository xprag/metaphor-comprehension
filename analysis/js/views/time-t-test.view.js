(function (define) {
    'use strict';

    define([
        '../controllers/nav.controller',
        '../controllers/time-t-test.controller',
        'text!../../templates/nav.html',
        'text!../../templates/time-t-test.html'
    ], function (navController, timeTtestController, navTemplate, timeTtestTemplate) {

        var vendorDir = 'bower_components/';

        return {
            url: '/response-t-test',
            data: {
                css: [
                    vendorDir + 'bootstrap/dist/css/bootstrap.min.css',
                    'css/main.css',
                    'css/table.css'
                ]
            },
            views: {
                navView: {
                    template: navTemplate,
                    controller: navController
                },
                containerView: {
                    template: timeTtestTemplate,
                    controller: timeTtestController
                }
            }
        };
    });

}(this.define));
