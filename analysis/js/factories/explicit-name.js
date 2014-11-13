(function (define) {
    'use strict';

    define([
    ], function () {
        return function (label) {
            label = label
                .replace(/^O_/, 'Omonimia<br>')
                .replace(/^P_/, 'Polisemia<br>')
                .replace(/^L_/, 'Metafore lessicalizzate<br>')
                .replace(/^V_/, 'Metafore vive<br>')
                .replace(/TPTC$/, 'True Premises, True Conclusion')
                .replace(/TPFC$/, 'True Premises, False Conclusion')
                .replace(/TPPC$/, 'True Premises, Plausible Conclusion')
                .replace(/distrattore_distrattore/, 'Distrattore');

            return label;
        };
    });
}(this.define));
