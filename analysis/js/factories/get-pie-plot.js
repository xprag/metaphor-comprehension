(function (define) {
    'use strict';

    define([
        'factories/explicit-name'
    ], function (explicitNameFactory) {
        return function (json, label) {
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
                    text: explicitNameFactory(label)
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
                    data: json[label].data
                }]
            };
        };
    });
}(this.define));
