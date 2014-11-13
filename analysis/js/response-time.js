(function (define) {
    'use strict';

    define([
        'jquery',
        'text!../templates/response-time-plot',
        'factories/explicit-name',
        'factories/get-histogram-plot'
    ], function ($,  responseTimePlotTemplate, explicitName, getPlot) {

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

        // Shorthand for $( document ).ready()
        $(function () {
            // It loads the template
            $('.tab-content').append(responseTimePlotTemplate);
            $.getJSON('./json/response-time.json', function (json) {
                categories.map(function (value) {
                    data.push(json[value]);
                });
                $('#reaction-time').highcharts(getHighchartConfig(data));
            });
        });
    });
}(this.define));
