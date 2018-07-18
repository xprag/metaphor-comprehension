(function (define) {
    'use strict';

    define([
    ], function () {
        return function (label) {
            label = label
                .replace(/^O_/, 'H<br>')
                .replace(/^P_/, 'P<br>')
                .replace(/^L_/, 'CM<br>')
                .replace(/^V_/, 'NM<br>')
                .replace(/TPTC$/, 'TP, TC')
                .replace(/TPFC$/, 'TP, FC')
                .replace(/TPPC$/, 'TP, PC')
                .replace(/distrattore_distrattore/, 'Distrattore');

            return label;
        };
    });
}(this.define));
