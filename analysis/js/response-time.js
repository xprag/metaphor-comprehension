(function (define) {
    'use strict';

    define([
        'jquery',
        'text!../templates/response-time-plot'
    ], function ($,  responseTimePlotTemplate) {

        var data,
            categories,
            highchartConfig;

        data = [];
        categories = [
            'O_TPPC',
            'P_TPPC',
            'L_TPPC',
            'V_TPPC'
        ];
        highchartConfig = {
            chart: {
                type: 'column',
                width: 1200
            },
            title: {
                text: 'Average Response Time'
            },
            subtitle: {
                text: 'Source: metaphor-comprehension experiment'
            },
            xAxis: {
                categories: categories
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Average time (seconds)'
                }
            },
            tooltip: {
                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                pointFormat: '<tr><td>{series.name}: </td>' +
                    '<td style="padding:0"><b>{point.y:.2f} seconds</b></td></tr>',
                footerFormat: '</table>',
                shared: true,
                useHTML: true
            },
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                    borderWidth: 0
                }
            },
            series: [{
                name: 'Response time',
                color: '#aaff99',
                data: data
            }]
        };

        // Shorthand for $( document ).ready()
        $(function () {
            // It loads the template
            $('.tab-content').append(responseTimePlotTemplate);
            $.getJSON('./json/response-time.json', function (json) {
                categories.map(function (value) {
                    data.push(json[value]);
                });
                // It does not load the plot.
                $('#reaction-time').highcharts(highchartConfig);
            });
        });
    });
}(this.define));
