(function (define) {
    'use strict';

    define([
        'jquery',
        'text!../templates/answer-t-test',
        'text!../templates/response-time-t-test'
    ], function ($,  answerTTestTemplate, responseTimeTTestTemplate) {

        var fill_table = function (combination, value) {
            var td_combination,
                p_value,
                t_value;

            td_combination = $('<td>').html(combination).prop('outerHTML');
            value[1] = value[1] <= 0 ? '<0.001' : value[1];
            t_value = $('<td>').html(value[0]).prop('outerHTML');
            p_value = $('<td>').html(value[1]).prop('outerHTML');

            return $('<tr>').html(td_combination + t_value + p_value);
        };

        $(function () {
            // It loads the template
            $('.tab-content')
                .append(answerTTestTemplate)
                .append(responseTimeTTestTemplate);
            $.getJSON('./json/t-test.json', function (json) {
                $.each(json.times, function (combination, value) {
                    combination = combination
                        .replace(/O_/, 'Omonimia ')
                        .replace(/P_/, 'Polisemia ')
                        .replace(/L_/, 'Metafore lessicalizzate ')
                        .replace(/V_/, 'Metafore vive ')
                        .replace(/TPTC/g, '(True Premises, True Conclusion)')
                        .replace(/TPFC/g, '(True Premises, False Conclusion)')
                        .replace(/TPPC/g, '(True Premises, Plausible Conclusion)');
                    $('.t-test .table-time tbody').append(fill_table(combination, value));
                });
                $.each(json.answers, function (combination, value) {
                    if ((combination.match(/TPPC/g) || []).length === 2) {
                        combination = combination
                            .replace(/TPTC/g, '(True Premises, True Conclusion)')
                            .replace(/TPFC/g, '(True Premises, False Conclusion)')
                            .replace(/TPPC/g, '(True Premises, Plausible Conclusion)')
                            .replace(/O_/g, 'Omonimia ')
                            .replace(/P_/g, 'Polisemia ')
                            .replace(/L_/g, 'Metafore lessicalizzate ')
                            .replace(/V_/g, 'Metafore vive ');
                        $('.t-test .table-correct-answers tbody').append(fill_table(combination, value));
                    }
                });
            });
        });
    });
}(this.define));
