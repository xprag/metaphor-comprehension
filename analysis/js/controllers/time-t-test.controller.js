(function (define) {
    'use strict';

    define([
        'jquery',
        'factories/array-to-table',
        'text!../../json/t-test.json',
        'stickyTableHeaders'
    ], function ($, arrayToTableFactory, tTestData) {

        tTestData = JSON.parse(tTestData);

        return function ($scope) {
            $scope.$on('$viewContentLoaded', function () {
                $('.t-test.response-time')
                    .append(arrayToTableFactory(tTestData.times));
                $('.t-test.response-time table')
                    .stickyTableHeaders({
                        fixedOffset: $('.navbar-fixed-top')
                    });
            });
        };
    });
}(this.define));
