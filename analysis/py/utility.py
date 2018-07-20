def get_comparisons():
    # L -> CM
    # V -> NM
    # O -> H
    return [
        ['H-TPTC', 'P-TPTC'],
        ['H-TPFC', 'P-TPFC'],
        ['H-TPPC', 'P-TPPC'],
        ['H-TPTC', 'CM-TPTC'],
        ['H-TPFC', 'CM-TPFC'],
        ['H-TPPC', 'CM-TPPC'],
        ['H-TPTC', 'NM-TPTC'],
        ['H-TPFC', 'NM-TPFC'],
        ['H-TPPC', 'NM-TPPC'],
        ['P-TPTC', 'CM-TPTC'],
        ['P-TPFC', 'CM-TPFC'],
        ['P-TPPC', 'CM-TPPC'],
        ['P-TPTC', 'NM-TPTC'],
        ['P-TPFC', 'NM-TPFC'],
        ['P-TPPC', 'NM-TPPC'],
        ['CM-TPTC', 'NM-TPTC'],
        ['CM-TPFC', 'NM-TPFC'],
        ['CM-TPPC', 'NM-TPPC']
    ]

def get_comparisons_middleTerm():
    return [
        ['H', 'P'],
        ['H', 'CM'],
        ['H', 'NM'],
        ['P', 'CM'],
        ['P', 'NM'],
        ['CM', 'NM']
    ]

def get_comparisons_argumentType():
    return [
        ['TPTC', 'TPFC'],
        ['TPTC', 'TPPC'],
        ['TPFC', 'TPPC']
    ]

def get_comparisons_letterali():
    return [
        ['H+PM', 'CM+NM']
    ]
