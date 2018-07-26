# TODO improve code quality - is not readability
from create_db import Person, Base, Argument
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select, text
from scipy.stats import f_oneway
from itertools import combinations
from numpy import around, array, float, mean, std, ndarray
import json, sys, os, csv
# my libs
import ttest, anova, comparisons
from query import Query

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

def getParticipantsGroupedByGender():
    # this method gets participants grouped by gender
    s = text('SELECT  gender, count(id) FROM person GROUP BY  gender;')
    json_data = {}
    for r in conn.execute(s).fetchall():
        if r[0] == 'F':
            label = 'Female'
        else:
            label = 'Male'
        json_data[label] = r[1]
    print json_data

def getParticipantsGroupedByAge():
    # this method gets participants grouped by gender and age + standard deviation
    query = text('SELECT age FROM person WHERE person.valid = 1;')
    tpls = conn.execute(query).fetchall()
    data = [x[0] for x in tpls]
    print data

# Query to correct input data (M instead of m).
s = text('UPDATE person SET gender = "M" WHERE gender = "m"' )
conn.execute(s)
s = text('UPDATE person SET gender = "F" WHERE gender = "f"' )
conn.execute(s)

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




# TODO - create two distinct json files after fixing the following issue
# https://github.com/Homebrew/homebrew-core/issues/11713
json_data= {}
query = Query(0) # 0 -> wrong answers, 1 -> correct answers
json_data['answers'] = ttest.getTTest(query.get_response_to_question_sql())
json_data['times'] = ttest.getTTest(query.get_response_time_sql())
write_json_file('t-test.json', json_data)

getParticipantsGroupedByGender()
getParticipantsGroupedByAge()
# anova.getResponseTimeAnova()
#anova.getAnswersAnova()
print anova.getAnswersAnova()
print anova.getResponseTimeAnova()
exit(0)

print '\n\n\n ACCURACY per argumentType and middleTerm'
ttest.getTTest2(query.get_accurancy_argumentTypeAndMiddleTerm(), utility.get_comparisons())

print '\n\n\n ACCURACY per argumentType'
ttest.getTTest2(query.get_accurancy_argumentType(), utility.get_comparisons_argumentType())

print '\n\n\n ACCURACY per middleTerm'
ttest.getTTest2(query.get_accurancy_middleTerm(), utility.get_comparisons_middleTerm())

print '\n\n\n#### ResponseTime per argumentType and middleTerm #### ' + query.correctText
ttest.getTTest2(query.get_responseTime_argumentTypeAndMiddleTerm(), utility.get_comparisons())

print '\n\n\n#### ResponseTime per middleTerm #### ' + query.correctText
ttest.getTTest2(query.get_responseTime_middleTerm(), utility.get_comparisons_middleTerm())

print '\n\n\n#### ResponseTime per argumentType'
ttest.getTTest2(query.get_responseTime_argumentType(), utility.get_comparisons_argumentType())

print '\n\n\n ACCURACY per letterali_metafore'
ttest.getTTest2(query.get_accurancy_letterali_metafore(), utility.get_comparisons_letterali())

print '\n\n\n ACCURACY per TC / FC / PC comparando literal (H+P) e metaphorical (CM+NM) middle terms'
ttest.getTTest2(query.get_accurancy_argumentType_vs_literalAndMetaphor(), utility.get_comparisons_argumentType_vs_literalAndMetaphor())

#print '\n\n\n ResponseTime per TC / FC / PC comparando literal (H+P) e metaphorical (CM+NM) middle terms'
print '\n\n\n ### ResponseTime per TC / FC / PC comparando literal (H+P) e metaphorical (CM+NM) middle terms ' + query.correctText
ttest.getTTest2(query.get_responseTime_argumentType_vs_literalAndMetaphor(), utility.get_comparisons_argumentType_vs_literalAndMetaphor())
