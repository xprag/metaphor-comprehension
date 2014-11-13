(function (define) {
    'use strict';

    define([
        'jquery',
        'text!../templates/nav-tabs',
        'bootstrap',
        'highcharts',
        'summary',
        'response-time',
        'arguments',
        't-test'
    ], function ($, navTabsTemplate) {

        $(function () {
            $('body').prepend(navTabsTemplate);
        });

        return {
            start: function () {
                $('#analysis-tabs a:last').tab('show');
            }
        };
    });
}(this.define));
