(function (define) {
    'use strict';

    define([
        'jquery',
        'text!../templates/answer-plot',
        'factories/get-pie-plot'
    ], function ($,  answersTemplate, getPiePlot) {

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

        // Shorthand for $( document ).ready()
        $(function () {
            // It loads the template
            $('.tab-content').append(answersTemplate);
            $.getJSON('./json/arguments.json', function (json) {
                tw_types.map(function (tw_type) {
                    // TODO - This check is made to display the right color; red for wrong and green for correct answers.
                    if (json[tw_type].data.length === 1) {
                        if (json[tw_type].data[0][0] === 'Correct') {
                            json[tw_type].data[1] = json[tw_type].data[0];
                            json[tw_type].data[0] = ['Wrong', 0];
                        }
                    }
                    // It adds <span> tags dynamically according to the tw_type number contained in the json object.
                    $('#arguments').append($('<span>')
                        .attr('class', 'plot-pie')
                        .attr('id', tw_type));
                    $('#' + tw_type).highcharts(getHighchartConfig(json, tw_type));

                });
            }).fail(function (jqxhr, textStatus, error) {
                throw new Error(jqxhr +  textStatus + ', ' + error);
            });
        });
    });
}(this.define));
