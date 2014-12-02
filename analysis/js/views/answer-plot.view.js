(function (define) {
    'use strict';

    define([
        '../controllers/nav.controller',
        'text!../../templates/nav.html',
        '../controllers/answer-plot.controller',
        'text!../../templates/answer-plot.html',
    ], function (navController, navTemplate, answerPlotController, answerPlotTemplate) {

        var vendorDir = 'bower_components/';

        return {
            url: '/answer-plot',
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
                    template: answerPlotTemplate,
                    controller: answerPlotController
                }
            }
        };

    });
}(this.define));
