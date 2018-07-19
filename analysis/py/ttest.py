from sqlalchemy import create_engine, func
from sqlalchemy.sql import select, text
import os
from numpy import around, array, float, mean, std, ndarray
from itertools import combinations
from scipy.stats import ttest_ind, f_oneway

db_file_name = 'arguments.db'
if os.path.isfile(db_file_name):
    engine = create_engine('///'.join(['sqlite:', db_file_name]))
else:
    raise Exception('The following file %s does not exist: ' % db_file_name)

conn = engine.connect()

def getAnswersTTest():
    # Query to get the t-test between two sample of answers
    s = text("""
        SELECT
        tw_type, argument_type, group_concat(response_to_question) as responses
        FROM argument, person
        WHERE
        person.id = argument.person_id and
        argument_block <> 'P' and person.valid = 1 and
        tw_type <> 'distrattore'
        group by tw_type, argument_type;
    """)
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

# TODO:  avoid redundancy between getResponseTimeTTest and getAnswersTTest
def getResponseTimeTTest():
    # Method to get the t-test between two sample on response_time
    # http://stackoverflow.com/questions/22611446/perform-2-sample-t-test
    # http://docs.scipy.org/doc/scipy-0.13.0/reference/generated/scipy.stats.ttest_ind.html
    s = text("""
        SELECT tw_type, argument_type, group_concat(response_time) as times
        FROM argument, person
        WHERE
        person.id = argument.person_id and
        response_to_question = 1 and
        argument_block <> 'P' and person.valid = 0 and
        tw_type <> 'distrattore'
        group by tw_type, argument_type;
    """)
    result = {}
    twType_vs_times = {}
    twTypes = []
    for r in conn.execute(s).fetchall():
        tw_type = r['tw_type'] + '_' + r['argument_type']
        twTypes.append(tw_type)
        # it converts an array of strings to an array of floats in numpy.
        times = r['times'].split(',')
        twType_vs_times[tw_type] = array(times, dtype='|S4').astype(float)
    twTypes_combinations = list(combinations(twTypes, 2))
    for twTypes_combination in twTypes_combinations:
        a = twType_vs_times[twTypes_combination[0]]
        b = twType_vs_times[twTypes_combination[1]]
        label = ' vs '.join([twTypes_combination[0], twTypes_combination[1]])
        t, p = ttest_ind(a, b)
        mean_a = round(mean(a), 2)
        mean_b = round(mean(b), 2)
        std_a = round(std(a), 2)
        std_b = round(std(b), 2)
        result[label] = around([t, p * 18, mean_a, std_a, mean_b, std_b], decimals = 3).tolist()
    return result
