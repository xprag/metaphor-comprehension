(function (requirejs, require) {
    'use strict';

    var vendorDir = '../bower_components/';

    requirejs.config({
        urlArgs: 'bust=' + Date.now(),
        paths: {
            angular: vendorDir + 'angular/angular',
            angularUiRouter: vendorDir + 'angular-ui-router/release/angular-ui-router',
            uiRouterStyles: vendorDir + 'angular-ui-router-styles/ui-router-styles',
            jquery: vendorDir + 'jquery/dist/jquery.min',
            highcharts: vendorDir + 'highcharts/highcharts',
            text: vendorDir + 'text/text',
            stickyTableHeaders: vendorDir + 'StickyTableHeaders/js/jquery.stickytableheaders'
        },
        shim: {
            angular : {exports : 'angular'},
            angularUiRouter: ['angular'],
            uiRouterStyles: ['angular']
        },
        deps: ['app']
    });
}(this.requirejs, this.require));
