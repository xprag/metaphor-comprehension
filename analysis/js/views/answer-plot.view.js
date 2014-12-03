(function (define) {
    'use strict';

    define([
        '../controllers/answer-plot.controller',
        'text!../../templates/answer-plot.html',
    ], function (answerPlotController, answerPlotTemplate) {

        return {
            url: '/answer-plot',
            template: answerPlotTemplate,
            controller: answerPlotController
        };

    });
}(this.define));
