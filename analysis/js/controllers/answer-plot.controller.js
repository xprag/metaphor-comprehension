(function (define) {
    'use strict';

    define([
        'jquery',
        'factories/get-pie-plot',
        'factories/tw-type-list',
        'text!../../json/arguments.json'
    ], function ($, getPiePlot, twTypeList, answerData) {

        answerData = JSON.parse(answerData);

        return function ($scope) {
            $scope.$on('$viewContentLoaded', function () {
                twTypeList.map(function (tw_type) {
                    // It adds <span> tags dynamically according to the tw_type number contained in the json object.
                    $('#arguments').append($('<span>')
                        .attr('class', 'plot-pie')
                        .attr('id', tw_type));
                    $('#' + tw_type).highcharts(getPiePlot(answerData, tw_type));

                });
            });
        };
    });
}(this.define));
