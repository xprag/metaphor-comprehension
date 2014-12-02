(function (define) {
    'use strict';

    define([
        'angular',
        'route',
        'angularUiRouter',
        'uiRouterStyles'
    ], function (angular, route) {

        var app = angular.module('analysisApp', [
            'ui.router',
            'uiRouterStyles'
        ]);

        app.config(route);
        angular.element().ready(function () {
            angular.bootstrap(document, ['analysisApp']);
        });

        return app;
    });
}(this.define));
