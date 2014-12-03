(function (define) {
    'use strict';

    define([
        '../controllers/answer-t-test.controller',
        'text!../../templates/answer-t-test.html'
    ], function (answerTtestController, answerTtestTemplate) {

        var vendorDir = 'bower_components/';

        return {
            url: '/response-t-test',
            data: {
                css: [
                    'css/table.css'
                ]
            },
            template: answerTtestTemplate,
            controller: answerTtestController
        };
    });

}(this.define));
