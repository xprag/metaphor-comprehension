(function (define) {
    'use strict';

    define([
        'jquery',
        'text!../../json/response-time.json',
        'factories/explicit-name',
        'factories/get-histogram-plot'
    ], function ($, responseTimeData, explicitName, getPlot) {

        var data,
            categories,
            getHighchartConfig;

        data = [];
        categories = [
            'O_TPPC',
            'P_TPPC',
            'L_TPPC',
            'V_TPPC'
        ];
        getHighchartConfig = function (data) {
            var explicitCategories = [];

            categories.map(function (category) {
                explicitCategories.push(explicitName(category));
            });

            return getPlot(data, explicitCategories);
        };
        responseTimeData = JSON.parse(responseTimeData);
        categories.map(function (value) {
            data.push(responseTimeData[value]);
        });

        return ['$scope', function ($scope) {
            $scope.$on('$viewContentLoaded', function () {
                $('#reaction-time').highcharts(getHighchartConfig(data));
            });
        }];
    });
}(this.define));
