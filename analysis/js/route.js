(function (define) {
    'use strict';

    define([
        'views/nav.view',
        'views/trusted.view',
        'views/time-t-test.view',
        'views/time-plot.view',
        'views/answer-plot.view',
        'views/answer-t-test.view'
    ], function (navView, trustedView, timeTtestView, timePlotView, answerPlotView, answerTtestView) {
        return function ($stateProvider, $urlRouterProvider) {
            $urlRouterProvider.otherwise('/');
            $stateProvider
                .state('/', navView)
                .state('trusted', trustedView)
                .state('time-t-test', timeTtestView)
                .state('time-plot', timePlotView)
                .state('answer-plot', answerPlotView)
                .state('answer-t-test', answerTtestView);
        };
    });
}(this.define));
