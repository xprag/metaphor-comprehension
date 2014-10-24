from create_db import Person, Base, Argument
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select, text
import json

engine = create_engine('sqlite:///arguments.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
conn = engine.connect()

s = text("""
SELECT tw_type, argument_type, response_to_question, COUNT(*)
FROM argument, person
where person.id = argument.person_id
group by tw_type, argument_type, response_to_question
""")
json_data = {}
for r in conn.execute(s).fetchall():
	tw_type = str(r[0] + '_' + r[1])
	if r[2] == 0:
		label = "Wrong"
	else:
		label = "Correct"
	try:
		json_data[tw_type]["title"] = tw_type
		json_data[tw_type]["data"] += [[label, r[3]]]
	except:
		json_data[tw_type] = {}
		json_data[tw_type]["data"] = [[label, r[3]]]

f = open('arguments.json', 'w')
f.write(json.dumps(json_data))
