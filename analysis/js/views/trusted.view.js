(function (define) {
    'use strict';

    define([
        '../controllers/trusted.controller',
        'text!../../templates/trusted.html'
    ], function (trustedController, trustedTemplate) {

        var vendorDir = 'bower_components/';

        return {
            url: '/trusted',
            template: trustedTemplate,
            controller: trustedController
        };
    });

}(this.define));
