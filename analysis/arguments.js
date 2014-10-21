$(function () {

    Highcharts.setOptions({
     colors: ['#ED561B', '#50B432']
    });

    $.getJSON('./arguments.json', function (json) {

        $.each(json, function(index, json) {

            $('#container').append($('<span>').attr('id', json['title']));

            $('#' + json['title']).highcharts({
                chart: {
                    plotBackgroundColor: null,
                    plotBorderWidth: 1,//null,
                    plotShadow: false,
                    width: 400
                },
                title: {
                    text: json.title
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
                    data: json.data
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
    }, 100);
});
