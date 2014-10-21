$(function () {

    Highcharts.setOptions({
     colors: ['#ED561B', '#50B432']
    });

    $.getJSON('./arguments.json', function (json) {

        tw_types = ['distrattore', 'O', 'P', 'L', 'V'];

        $.each(tw_types, function(index, tw_type) {

            $('#container').append($('<span>').attr('id', tw_type));

            $('#' + tw_type).highcharts({
                chart: {
                    plotBackgroundColor: null,
                    plotBorderWidth: 1,//null,
                    plotShadow: false,
                    width: 310
                },
                title: {
                    text: tw_type
                },
                tooltip: {
                    pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
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
        var err = textStatus + ", " + error;
        console.log( "Request Failed: " + err );
    });

    setTimeout(function() {
        $('#container').css('display','inline');
        $('.highcharts-container').css('display','inline-block');
    }, 300);
});
