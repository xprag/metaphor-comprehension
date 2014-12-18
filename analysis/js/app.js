(function (define) {
    'use strict';

    define([
        'angular',
        'route',
        'directives/navbar.directive',
        'angularUiRouter'
    ], function (angular, route, navbarDirective) {

        var app = angular.module('analysisApp', [
            'ui.router'
        ]);

        app.directive('navbar', navbarDirective);
        app.config(route);
        angular.element().ready(function () {
            angular.bootstrap(document, ['analysisApp']);
        });

        return app;
    });
}(this.define));
