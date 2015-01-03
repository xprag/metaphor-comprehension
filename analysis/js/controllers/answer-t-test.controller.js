(function (define) {
    'use strict';

    define([
        'jquery',
        'factories/array-to-table',
        'text!../../json/t-test.json',
        'stickyTableHeaders'
    ], function ($, arrayToTableFactory, tTestData) {

        tTestData = JSON.parse(tTestData);

        return ['$scope', function ($scope) {
            $scope.$on('$viewContentLoaded', function () {
                $('.t-test.answers')
                    .append(arrayToTableFactory(tTestData.answers));
                $('.t-test.answers table')
                    .stickyTableHeaders({
                        fixedOffset: $('.navbar-fixed-top')
                    });
            });
        }];
    });
}(this.define));
