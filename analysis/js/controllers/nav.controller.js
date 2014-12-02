(function (define) {
    'use strict';

    define([
        'jquery'
    ], function ($) {
        return function ($scope) {
            $scope.$on('$viewContentLoaded', function () {
                $('.nav.nav-tabs li').click(function () {
                    $(this).addClass('active');
                });
            });
        };
    });
}(this.define));
