(function (define) {
    'use strict';

    define([
        '../controllers/nav.controller',
        '../controllers/answer-t-test.controller',
        'text!../../templates/nav.html',
        'text!../../templates/answer-t-test.html'
    ], function (navController, answerTtestController, navTemplate, answerTtestTemplate) {

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
                    template: answerTtestTemplate,
                    controller: answerTtestController
                }
            }
        };
    });

}(this.define));
