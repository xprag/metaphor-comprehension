/*global Highcharts, $*/
$(function () {
    'use strict';

    $.getJSON('./summary.json', function (json) {

        var data = [];
        var categories = ['Good', 'Bad'];

        $.each(categories, function( index, value ) {
            data.push(json[value]);
        });
        categories.push('Total');
        data.push(eval(data.join('+')));

        console.log(data);

        $('#summary').highcharts({
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
                    text: 'Population (millions)',
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
                floating: true,
                borderWidth: 1,
                backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
                shadow: true
            },
            credits: {
                enabled: false
            },
            series: [{
                name: 'Number of students',
                data: data
            }]
        });
    }).fail(function( jqxhr, textStatus, error ) {
        var err = textStatus + ', ' + error;
        console.log( 'Request Failed: ' + err );
    });
});
