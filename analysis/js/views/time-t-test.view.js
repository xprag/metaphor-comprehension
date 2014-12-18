(function (define) {
    'use strict';

    define([
        '../controllers/time-t-test.controller',
        'text!../../templates/time-t-test.html'
    ], function (timeTtestController, timeTtestTemplate) {

        var vendorDir = 'bower_components/';

        return {
            url: '/response-t-test',
            template: timeTtestTemplate,
            controller: timeTtestController
        };
    });

}(this.define));
