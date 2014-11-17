(function (requirejs, require) {
    'use strict';

    var vendorDir = '../bower_components/';

    requirejs.config({
        urlArgs: 'bust=' + Date.now(),
        paths: {
            jquery: vendorDir + 'jquery/dist/jquery.min',
            bootstrap: vendorDir + 'bootstrap/dist/js/bootstrap.min',
            highcharts: vendorDir + 'highcharts/highcharts',
            text: vendorDir + 'text/text',
            stickyTableHeaders: vendorDir + 'StickyTableHeaders/js/jquery.stickytableheaders'
        },
        shim: {
            bootstrap: {
                deps: ['jquery']
            }
        }
    });

    require([
        'app'
    ], function (app) {
        // TODO bootstrap the application. You should use angularjs or backbone.
        app.start();
    });
}(this.requirejs, this.require));
