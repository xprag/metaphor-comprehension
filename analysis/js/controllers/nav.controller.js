(function (define) {
    'use strict';

    define([
        'jquery'
    ], function ($) {
        return function () {

            var $navList = $('.nav.nav-tabs li');

            $navList.click(function () {
                $navList.each(function (index) {
                    $($navList[index]).removeClass('active');
                });
                $(this).addClass('active');
            });
        };
    });
}(this.define));
