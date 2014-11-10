from create_db import Person, Base, Argument
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select, text
import json, sys, os

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
threshold = sys.argv[1] or 0

# Query to set the untrusted users.
s = text('UPDATE person SET valid = 1')
conn.execute(s)
s = text("""
UPDATE person SET valid = 0 where person.id in (
	SELECT person.id
	FROM argument, person
	where
	response_to_question = 0 and
	person.id = argument.person_id and tw_type = 'distrattore' and argument_block <> 'P'
	group by person.id, person.name, response_to_question
	HAVING COUNT(*) > """ + threshold + """);
""")
conn.execute(s)

#query to get the summary
s = text('SELECT valid, count(id) FROM person GROUP BY valid;')
json_data = {}
for r in conn.execute(s).fetchall():
	if r[0] == 0:
		label = 'Untrusted'
	else:
		label = 'Trusted'
	json_data[label] = r[1]
# f = open(json_path + 'summary.json', 'w')
f = open('/'.join([json_path, 'summary.json']), 'w')
f.write(json.dumps(json_data))

# Query to get the questions response divided per argument.
s = text("""
	SELECT tw_type, argument_type, response_to_question, COUNT(*)
	FROM argument, person
	where
	person.id = argument.person_id and argument_block <> 'P' and person.valid = 1
	group by tw_type, argument_type, response_to_question;
""")
json_data = {}
for r in conn.execute(s).fetchall():
	tw_type = str(r[0] + '_' + r[1])
	if r[2] == 0:
		label = 'Wrong'
	else:
		label = 'Correct'
	try:
		json_data[tw_type]['title'] = tw_type
		json_data[tw_type]['data'] += [[label, r[3]]]
	except:
		json_data[tw_type] = {}
		json_data[tw_type]['data'] = [[label, r[3]]]
f = open('/'.join([json_path, 'arguments.json']), 'w')
f.write(json.dumps(json_data))

# Query to get the average response time divided per argument.
s = text("""
	SELECT tw_type, avg(response_time) as response_time_avg, COUNT(*)
	FROM argument, person
	where person.id = argument.person_id and argument_block <> 'P' and person.valid = 1
	group by tw_type;
""")
json_data = {}
for r in conn.execute(s).fetchall():
	if r[0] == 'distrattore':
		tw_type = 'Distrattore'
	else:
		tw_type = str(r[0])
	json_data[tw_type] = r[1]
f = open('/'.join([json_path, 'response-time.json']), 'w')
f.write(json.dumps(json_data))
