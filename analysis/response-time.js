$(function () {

    $.getJSON('./response-time.json', function (json) {

        // console.log(json);
        data =[];
        categories = [
            'Distrattore',
            'O_TPTC', 'O_TPFC', 'O_TPPC',
            'P_TPTC', 'P_TPFC', 'P_TPPC',
            'L_TPTC', 'L_TPFC', 'L_TPPC',
            'V_TPTC', 'V_TPFC', 'V_TPPC'
        ];

        $.each(categories, function( index, value ) {
            data.push(json[value]);
        });

        $('#container').highcharts({
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
        });
    });
});