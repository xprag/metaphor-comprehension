(function (requirejs, require) {
    'use strict';

    requirejs.config({
        urlArgs: 'bust=' + Date.now(),
        paths: {
            angular: '../bower_components/angularjs/angular',
            angularUiRouter: '../bower_components/ui-router/release/angular-ui-router',
            jquery: '../bower_components/jquery/dist/jquery',
            highcharts: '../bower_components/highcharts/highcharts',
            text: '../bower_components/text/text',
            stickyTableHeaders: '../bower_components/StickyTableHeaders/js/jquery.stickytableheaders'
        },
        shim: {
            angular : {exports : 'angular'},
            angularUiRouter: ['angular'],
            highcharts: ['jquery'],
            uiRouterStyles: ['angular'],
            stickyTableHeaders: ['jquery']
        },
        deps: ['app']
    });
}(this.requirejs, this.require));
