(function (define) {
    'use strict';

    define([
        'angular'
    ], function (angular) {

        return function () {

            return {
                link: function (scope, element) {

                    var $lis = element.find('li');

                    $lis.bind('click', function () {
                        $lis.removeClass('active');
                        angular.element(this).addClass('active');
                    });
                }
            };
        };
    });
}(this.define));
