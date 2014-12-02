(function (define) {
    'use strict';

    define([
        'jquery',
        'factories/get-pie-plot',
        'text!../../json/arguments.json'
    ], function ($, getPiePlot, answerData) {

        var tw_types,
            getHighchartConfig;

        // this array allows to keep a strict order.
        tw_types = [
            'O_TPTC', 'O_TPFC', 'O_TPPC',
            'P_TPTC', 'P_TPFC', 'P_TPPC',
            'L_TPTC', 'L_TPFC', 'L_TPPC',
            'V_TPTC', 'V_TPFC', 'V_TPPC',
            'distrattore_distrattore'
        ];
        getHighchartConfig = function (json, tw_type) {
            return getPiePlot(json, tw_type);
        };
        answerData = JSON.parse(answerData);

        return function ($scope) {
            $scope.$on('$viewContentLoaded', function () {
                tw_types.map(function (tw_type) {
                    // TODO - This check is made to display the right color; red for wrong and green for correct answers.
                    if (answerData[tw_type].data.length === 1) {
                        if (answerData[tw_type].data[0][0] === 'Correct') {
                            answerData[tw_type].data[1] = answerData[tw_type].data[0];
                            answerData[tw_type].data[0] = ['Wrong', 0];
                        }
                    }
                    // It adds <span> tags dynamically according to the tw_type number contained in the json object.
                    $('#arguments').append($('<span>')
                        .attr('class', 'plot-pie')
                        .attr('id', tw_type));
                    $('#' + tw_type).highcharts(getHighchartConfig(answerData, tw_type));

                });
            });
        };
    });
}(this.define));
