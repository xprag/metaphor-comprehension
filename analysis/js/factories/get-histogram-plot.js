(function (define) {
    'use strict';

    define([
    ], function () {
        return function (data, labels) {

            return {
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
                    categories: labels
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
        };
    });
}(this.define));
