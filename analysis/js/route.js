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
            $urlRouterProvider.otherwise('/home');
            $stateProvider
                .state('home', navView)
                .state('home.trusted', trustedView)
                .state('home.time-t-test', timeTtestView)
                .state('home.time-plot', timePlotView)
                .state('home.answer-plot', answerPlotView)
                .state('home.answer-t-test', answerTtestView);
        };
    });
}(this.define));
