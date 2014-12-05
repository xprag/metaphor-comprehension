(function (define) {
    'use strict';

    define([
        'angular',
        'route',
        'directives/active-tab',
        'angularUiRouter',
        'uiRouterStyles'
    ], function (angular, route, activeTabDirective) {

        var app = angular.module('analysisApp', [
            'ui.router',
            'uiRouterStyles'
        ]);

        app.directive('activeTab', activeTabDirective);
        app.config(route);
        angular.element().ready(function () {
            angular.bootstrap(document, ['analysisApp']);
        });

        return app;
    });
}(this.define));
