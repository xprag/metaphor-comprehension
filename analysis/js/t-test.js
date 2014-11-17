(function (define) {
    'use strict';

    define([
        'jquery',
        'text!../templates/answer-t-test',
        'text!../templates/response-time-t-test',
        'factories/array-to-table',
        'stickyTableHeaders'
    ], function ($,  answerTTestTemplate, responseTimeTTestTemplate, arrayToTableFactory) {

        $(function () {
            // It loads the template
            $('.tab-content')
                .append(answerTTestTemplate)
                .append(responseTimeTTestTemplate);
            $.getJSON('./json/t-test.json', function (json) {
                $('.t-test.response-time').append(arrayToTableFactory(json.times));
                $('.t-test.response-time table').stickyTableHeaders({fixedOffset: $('.navbar-fixed-top')});
                $('.t-test.answers').append(arrayToTableFactory(json.answers));
                $('.t-test.answers table').stickyTableHeaders({fixedOffset: $('.navbar-fixed-top')});
            });
        });
    });
}(this.define));
