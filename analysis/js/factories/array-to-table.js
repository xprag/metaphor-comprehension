(function (define) {
    'use strict';

    define([
        'jquery',
        'factories/explicit-name',
        'factories/tw-type-list'
    ], function ($, explicitName, twTypeList) {
        return function (json) {

            // TODO: make the code more readable.
            // You should change the json t-test object; the key should be an array
            // example: {"L_TPFC vs V_TPFC": [-0.574, 0.566]} should be {["L_TPFC","V_TPFC"]: [-0.574, 0.566]}
            // and then you should use JSON.stringify after sorting the array.
            var rows = [],
                $table = $('<table>'),
                $tr,
                $td,
                tdSplit,
                td_inverse,
                pt_value;

            rows[0] = [''];
            twTypeList.map(function (value) {
                rows[0].push(value);
            });
            // It fills the rows starting from the second one
            twTypeList.map(function (value, index) {
                // It creates the first column of the table
                rows[index + 1] = [];
                rows[index + 1].push(value);
                // It creates the cell starting from the second row and the second column
                twTypeList.map(function (value2) {
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
                            td += '<br>avg1 = ' + pt_value[2];
                            td += '<br>std1 = ' + pt_value[3];
                            td += '<br>avg2 = ' + pt_value[4];
                            td += '<br>std2 = ' + pt_value[5];
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
