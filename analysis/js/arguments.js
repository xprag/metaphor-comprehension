(function ($) {
    'use strict';

    var tw_types,
        explicit_tw_type,
        getHighchartConfig;

    // this array allows to keep a strict order.
    tw_types = [
        'O_TPTC', 'O_TPFC', 'O_TPPC',
        'P_TPTC', 'P_TPFC', 'P_TPPC',
        'L_TPTC', 'L_TPFC', 'L_TPPC',
        'V_TPTC', 'V_TPFC', 'V_TPPC',
        'distrattore_distrattore'
    ];
    explicit_tw_type = function (tw_type) {
        tw_type = tw_type
            .replace(/^O_/, 'Omonimia<br>')
            .replace(/^P_/, 'Polisemia<br>')
            .replace(/^L_/, 'Metafore lessicalizzate<br>')
            .replace(/^V_/, 'Metafore vive<br>')
            .replace(/TPTC$/, 'True Premises, True Conclusion')
            .replace(/TPFC$/, 'True Premises, False Conclusion')
            .replace(/TPPC$/, 'True Premises, Plausible Conclusion')
            .replace(/distrattore_distrattore/, 'Distrattore');

        return tw_type;
    };
    getHighchartConfig = function (json, tw_type) {
        return {
            colors: ['#ED561B', '#50B432'],
            chart: {
                // plotBackgroundColor: '#aaa',
                plotBorderWidth: null,
                plotShadow: true,
                width: 400,
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 1, y2: 1 },
                    stops: [
                        [0, '#ddd'],
                        [1, '#eee']
                    ]
                }
            },
            title: {
                text: explicit_tw_type(tw_type)
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.y}</b> - <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: false
                    },
                    showInLegend: true
                }
            },
            series: [{
                type: 'pie',
                name: 'Answers',
                data: json[tw_type].data
            }]
        };
    };

    // Shorthand for $( document ).ready()
    $(function () {
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
}(this.jQuery));
