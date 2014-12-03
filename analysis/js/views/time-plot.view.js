(function (define) {
    'use strict';

    define([
        '../controllers/time-plot.controller',
        'text!../../templates/time-plot.html',
    ], function (timePlotController, timePlotTemplate) {

        return {
            url: '/time-plot',
            template: timePlotTemplate,
            controller: timePlotController
        };

    });
}(this.define));
