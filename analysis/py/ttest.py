from sqlalchemy import create_engine, func
from sqlalchemy.sql import select, text
import os
from numpy import around, array, float, mean, std, ndarray
from itertools import combinations
from scipy.stats import ttest_ind, f_oneway
from collections import defaultdict

db_file_name = 'arguments.db'
if os.path.isfile(db_file_name):
    engine = create_engine('///'.join(['sqlite:', db_file_name]))
else:
    raise Exception('The following file %s does not exist: ' % db_file_name)

conn = engine.connect()

def print_dictionary(dict):
    for k, v in dict.iteritems():
        print k,': ', v

def getTTest2(sql, comparisons):
    s = text(sql)
    dict = {}
    for row in conn.execute(s).fetchall():
        if not row['key'] in dict:
            dict[row['key']] = []
        dict[row['key']].append(row['value'])
    for comparison in comparisons:
        print '\n', comparison[0], '/' ,comparison[1]
        print_dictionary(__getStats(dict[comparison[0]], dict[comparison[1]]))

def __getStats(range1, range2):
    t, p = ttest_ind(range1, range2, equal_var=True)
    return {
        't': round(t, 2),
        'p': round(p * 6, 4),
        'mean1': round(mean(range1), 2),
        'mean2': round(mean(range2), 2),
        'std1': round(std(range1), 2),
        'std2': round(std(range2), 2)
    }

def getTTest(sql):
    s = text(sql)
    twType_vs_times = {}
    twTypes = []
    result = {}
    for r in conn.execute(s).fetchall():
        tw_type = r['tw_type'] + '_' + r['argument_type']
        twTypes.append(tw_type)
        # it converts an array of strings to an array of floats in numpy.
        times = r['responses'].split(',')
        twType_vs_times[tw_type] = array(times, dtype='|S4').astype(float)
    twTypes_combinations = list(combinations(twTypes, 2))
    for twTypes_combination in twTypes_combinations:
        a = twType_vs_times[twTypes_combination[0]]
        b = twType_vs_times[twTypes_combination[1]]
        label = ' vs '.join([twTypes_combination[0], twTypes_combination[1]])
        mean_a = round(mean(a), 2)
        mean_b = round(mean(b), 2)
        std_a = round(std(a), 2)
        std_b = round(std(b), 2)
        t, p = ttest_ind(a, b, equal_var=True)
        result[label] = around([t , p * 18, mean_a, std_a, mean_b, std_b], decimals=3).tolist()
    return result
