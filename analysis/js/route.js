(function (define) {
    'use strict';

    define([
        'views/trusted.view',
        'views/time-t-test.view',
        'views/time-plot.view',
        'views/answer-plot.view',
        'views/answer-t-test.view'
    ], function (trustedView, timeTtestView, timePlotView, answerPlotView, answerTtestView) {
        return function ($stateProvider, $urlRouterProvider) {
            $urlRouterProvider.otherwise('/home');
            $stateProvider
                .state('trusted', trustedView)
                .state('time-t-test', timeTtestView)
                .state('time-plot', timePlotView)
                .state('answer-plot', answerPlotView)
                .state('answer-t-test', answerTtestView);
        };
    });
}(this.define));
