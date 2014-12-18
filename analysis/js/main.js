(function (requirejs, require) {
    'use strict';

    var vendorDir = '../bower_components/';

    requirejs.config({
        urlArgs: 'bust=' + Date.now(),
        paths: {
            angular: vendorDir + 'angularjs/angular',
            angularUiRouter: vendorDir + 'ui-router/release/angular-ui-router',
            jquery: vendorDir + 'jquery/dist/jquery',
            highcharts: vendorDir + 'highcharts/highcharts',
            text: vendorDir + 'text/text',
            stickyTableHeaders: vendorDir + 'StickyTableHeaders/js/jquery.stickytableheaders'
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
