(function ($) {
    'use strict';

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
        $.getJSON('./json/t-test.json', function (json) {
            $.each(json.times, function (combination, value) {
                combination = combination
                    .replace(/O/, 'Omonimia')
                    .replace(/P/, 'Polisemiaimia')
                    .replace(/L/, 'Metafore lessicalizzate')
                    .replace(/V/, 'Metafore vive');
                $('#t-test .table-time tbody').append(fill_table(combination, value));
            });
            $.each(json.answers, function (combination, value) {
                combination = combination
                    .replace(/TPTC/g, '(True Premises, True Conclusion)')
                    .replace(/TPFC/g, '(True Premises, False Conclusion)')
                    .replace(/TPPC/g, '(True Premises, Plausible Conclusion)')
                    .replace(/O_/g, 'Omonimia ')
                    .replace(/P_/g, 'Polisemiaimia ')
                    .replace(/L_/g, 'Metafore lessicalizzate ')
                    .replace(/V_/g, 'Metafore vive ');
                $('#t-test .table-correct-answers tbody').append(fill_table(combination, value));
            });
        });
    });
}(this.jQuery));
