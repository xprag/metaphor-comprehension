$(function () {

    Highcharts.setOptions({
     colors: ['#ED561B', '#50B432']
    });

    $.getJSON('./arguments.json', function (json) {

        // this array allows to keep a strict order.
        tw_types = [
            'O_TPTC', 'O_TPFC', 'O_TPPC',
            'P_TPTC', 'P_TPFC', 'P_TPPC',
            'L_TPTC', 'L_TPFC', 'L_TPPC',
            'V_TPTC', 'V_TPFC', 'V_TPPC',
            'distrattore_distrattore'
        ];

        $.each(tw_types, function(index, tw_type) {

            // TODO - This check is made to display the right color; red for wrong and green for correct answers.
            if(json[tw_type].data.length === 1) {
                if(json[tw_type].data[0][0] === 'Correct') {
                    json[tw_type].data[1] = json[tw_type].data[0];
                    json[tw_type].data[0] = ['Wrong', 0];
                }
            }

            // It adds <span> tags dynamically according to the tw_type number contained in the json object.
            $('#reaction-time').append($('<span>').attr('id', tw_type));

            $('#' + tw_type).highcharts({
                chart: {
                    plotBackgroundColor: null,
                    plotBorderWidth: 1,//null,
                    plotShadow: false,
                    width: 400
                },
                title: {
                    text: tw_type
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
            });

        });

    }).fail(function( jqxhr, textStatus, error ) {
        var err = textStatus + ', ' + error;
        console.log( 'Request Failed: ' + err );
    });

    setTimeout(function() {
        $('#container').css('display','inline');
        $('.highcharts-container').css('display','inline-block');
    }, 300);
});
