(function (define) {
    'use strict';

    define([
        'angular',
        'text!../../templates/navbar.html'
    ], function (angular, bootstrapNavbarTemplate) {
        return function () {
            return {
                compile: function (element) {
                    var $lis = element.find('li');

                    $lis.bind('click', function () {
                        $lis.removeClass('active');
                        angular.element(this).addClass('active');
                    });
                },
                restrict: 'E',
                replace: true,
                transclude: true,
                template: bootstrapNavbarTemplate
            };
        };
    });
}(this.define));
