from create_db import Person, Base, Argument
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select, text
import json
import sys
import os

db_file_name = 'arguments.db'
if os.path.isfile(db_file_name):
    engine = create_engine('///'.join(['sqlite:', db_file_name]))
else:
    raise Exception('The following file %s does not exist: ' % db_file_name)

Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
conn = engine.connect()
json_path = '../json'
threshold = sys.argv[1]


def write_json_file(file_name, json_data):
    f = open('/'.join([json_path, file_name]), 'w')
    f.write(json.dumps(json_data))

# Query to set the untrusted users.
s = text('UPDATE person SET valid = 1')
conn.execute(s)
s = text("""
UPDATE person SET valid = 0 where person.id in (
    SELECT person.id
    FROM argument, person
    where
    response_to_question = 0 and
    person.id = argument.person_id and tw_type = 'distrattore'
    and argument_block <> 'P'
    group by person.id, person.name, response_to_question
    HAVING COUNT(*) > """ + threshold + """);
""")
conn.execute(s)

# query to get the summary
s = text('SELECT valid, count(id) FROM person GROUP BY valid;')
json_data = {}
for r in conn.execute(s).fetchall():
    if r[0] == 0:
        label = 'Untrusted'
    else:
        label = 'Trusted'
    json_data[label] = r[1]
write_json_file('summary.json', json_data)

# Query to get the questions response divided per argument.
s = text("""
    SELECT tw_type, argument_type, response_to_question, COUNT(*) as frequency
    FROM argument, person
    WHERE
    person.id = argument.person_id and
    argument_block <> 'P' and person.valid = 1
    group by tw_type, argument_type, response_to_question;
""")
json_data = {}
for r in conn.execute(s).fetchall():
    tw_type = str(r['tw_type'] + '_' + r['argument_type'])
    if r['response_to_question'] == 0:
        label = 'Wrong'
    else:
        label = 'Correct'
    try:
        json_data[tw_type]['title'] = tw_type
        json_data[tw_type]['data'] += [[label, r['frequency']]]
    except:
        json_data[tw_type] = {}
        json_data[tw_type]['data'] = [[label, r['frequency']]]
write_json_file('arguments.json', json_data)

# Query to get the average response time divided per argument.
s = text("""
    SELECT tw_type, argument_type, avg(response_time) as response_time_avg, COUNT(*)
    FROM argument, person
    WHERE
    person.id = argument.person_id and
    argument_block <> 'P' and person.valid = 1 and
    argument_type = 'TPPC'
    group by tw_type, argument_type;
""")
json_data = {}
for r in conn.execute(s).fetchall():
    if r['tw_type'] == 'distrattore':
        tw_type = 'Distrattore'
    else:
        tw_type = str(r['tw_type'] + '_' + r['argument_type'])
    json_data[tw_type] = r['response_time_avg']
write_json_file('response-time.json', json_data)

# Query to get the t-test between two sample on response_time
# http://stackoverflow.com/questions/22611446/perform-2-sample-t-test
# http://docs.scipy.org/doc/scipy-0.13.0/reference/generated/scipy.stats.ttest_ind.html
from scipy.stats import ttest_ind
from itertools import combinations
import numpy as np
s = text("""
    SELECT tw_type, argument_type, group_concat(response_time) as times
    FROM argument, person
    WHERE
    person.id = argument.person_id and
    argument_block <> 'P' and person.valid = 1 and
    tw_type <> 'distrattore' and argument_type = 'TPPC'
    group by tw_type;
""")
twType_vs_times = {}
twTypes = []
json_data = {}
json_data['times'] = {}
for r in conn.execute(s).fetchall():
    tw_type = r['tw_type'] + '_' + r['argument_type']
    twTypes.append(tw_type)
    # it converts an array of strings to an array of floats in numpy.
    times = r['times'].split(',')
    twType_vs_times[tw_type] = np.array(times, dtype='|S4').astype(np.float)
twTypes_combinations = list(combinations(twTypes, 2))
for twTypes_combination in twTypes_combinations:
    a = twType_vs_times[twTypes_combination[0]]
    b = twType_vs_times[twTypes_combination[1]]
    label = ' vs '.join([twTypes_combination[0], twTypes_combination[1]])
    t, p = ttest_ind(a, b, equal_var=True)
    json_data['times'][label] = np.around([t, p], decimals=3).tolist()

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
json_data['answers'] = {}
for r in conn.execute(s).fetchall():
    tw_type = r['tw_type'] + '_' + r['argument_type']
    twTypes.append(tw_type)
    # it converts an array of strings to an array of floats in numpy.
    times = r['responses'].split(',')
    twType_vs_times[tw_type] = np.array(times, dtype='|S4').astype(np.float)
twTypes_combinations = list(combinations(twTypes, 2))
for twTypes_combination in twTypes_combinations:
    a = twType_vs_times[twTypes_combination[0]]
    b = twType_vs_times[twTypes_combination[1]]
    label = ' vs '.join([twTypes_combination[0], twTypes_combination[1]])
    t, p = ttest_ind(a, b, equal_var=True)
    json_data['answers'][label] = np.around([t, p], decimals=3).tolist()
write_json_file('t-test.json', json_data)
