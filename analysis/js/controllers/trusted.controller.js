(function (define) {
    'use strict';

    define([
        'jquery',
        'text!../../json/summary.json',
        'highcharts'
    ], function ($, summaryData) {

        var data,
            categories,
            highchartsObject;

        data = [];
        categories = ['Trusted', 'Untrusted'];
        highchartsObject = {
            chart: {
                type: 'bar'
            },
            title: {
                text: 'Total number of participants divided into good and poor group according to performance criteria.'
            },
            subtitle: {
                text: 'Source: metaphor-comprehension experiment - 24 October 2014 - Cagliari'
            },
            xAxis: {
                categories: categories,
                title: {
                    text: null
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Students (number)',
                    align: 'high'
                },
                labels: {
                    overflow: 'justify'
                }
            },
            plotOptions: {
                bar: {
                    dataLabels: {
                        enabled: true
                    }
                }
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -40,
                y: 100,
                floating: false,
                borderWidth: 1,
                shadow: true
            },
            credits: {
                enabled: false
            },
            series: [{
                name: 'Number of students',
                data: data
            }]
        };
        summaryData = JSON.parse(summaryData);
        categories.map(function (category) {
            data.push(summaryData[category]);
        });
        categories.push('Total');
        data.push(data.reduce(function (previousValue, currentValue) {
            return previousValue + currentValue;
        }));

        return ['$scope', function ($scope) {
            $scope.$on('$viewContentLoaded', function () {
                $('#summary').highcharts(highchartsObject);
            });
        }];
    });
}(this.define));
