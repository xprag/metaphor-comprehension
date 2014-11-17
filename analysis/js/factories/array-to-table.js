(function (define) {
    'use strict';

    define([
        'jquery',
        'factories/explicit-name'
    ], function ($, explicitName) {
        return function (json) {

            // TODO: make the code more readable.
            // You should change the json t-test object; the key should be an array
            // example: {"L_TPFC vs V_TPFC": [-0.574, 0.566]} should be {["L_TPFC","V_TPFC"]: [-0.574, 0.566]}
            // and then you should use JSON.stringify after sorting the array.
            var combinations,
                headers = [],
                rows = [],
                $table = $('<table>'),
                $tr,
                $td,
                tdSplit,
                td_inverse,
                pt_value;

            $.each(json, function (combination) {
                combinations = combination.split(' vs ');
                combinations.map(function (head_text) {
                    if (headers.indexOf(head_text) === -1) {
                        headers.push(head_text);
                    }
                });
            });
            headers.sort();
            rows[0] = [''];
            headers.map(function (value) {
                rows[0].push(value);
            });
            // It fills the rows starting from the second one
            headers.map(function (value, index) {
                // It creates the first column of the table
                rows[index + 1] = [];
                rows[index + 1].push(value);
                // It creates the cell starting from the second row and the second column
                headers.map(function (value2) {
                    rows[index + 1].push(value + ' vs ' + value2);
                });

            });
            // It appends elements to the table
            $table.append($('<thead>')).append($('<tbody>'));
            rows.map(function (tr, index_row) {
                $tr = $('<tr>');
                tr.map(function (td, index_column) {
                    if (index_row === 0 || index_column === 0) {
                        $td = $('<th>');
                        td = explicitName(td);
                    } else {
                        $td = $('<td>');
                        tdSplit = td.split(' ');
                        td_inverse = tdSplit[2] + ' vs ' + tdSplit[0];
                        if (tdSplit[2] !== tdSplit[0]) {
                            pt_value = json[td] || json[td_inverse];
                            td = 't = ' + pt_value[0] + '<br> p ' + ((pt_value[1] === 0) ? '< 0.001' : ' = ' + pt_value[1]);
                        } else {
                            td = '-';
                        }
                    }
                    $tr.append($td.html(td));
                });
                $table.find((index_row === 0) ? 'thead' : 'tbody').append($tr);
            });

            return $table;
        };
    });
}(this.define));
