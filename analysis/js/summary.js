(function (define) {
    'use strict';

    define([
        'jquery',
        'text!../templates/trusted-students'
    ], function ($, trustedStudentsTemplate) {
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
                text: 'Summary'
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

        // Shorthand for $( document ).ready()
        $(function () {
            // It loads the template
            $('.tab-content').append(trustedStudentsTemplate);
            $.getJSON('./json/summary.json', function (json) {
                categories.map(function (category) {
                    data.push(json[category]);
                });
                categories.push('Total');
                data.push(data.reduce(function (previousValue, currentValue) {
                    return previousValue + currentValue;
                }));
                $('#summary').highcharts(highchartsObject);
            }).fail(function (jqxhr, textStatus, error) {
                throw new Error(jqxhr +  textStatus + ', ' + error);
            });
        });
    });
}(this.define));
