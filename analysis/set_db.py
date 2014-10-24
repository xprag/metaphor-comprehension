# http://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/
import xlrd, math
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import Argument, Base, Person

def read_and_store(data_file):
	data_dir = '../data/'
	data_opened = xlrd.open_workbook(''.join([data_dir, data_file]))

	print "The number of worksheets is", data_opened.nsheets
	print "Worksheet name(s):", data_opened.sheet_names()
	sh = data_opened.sheet_by_index(0)
	print sh.name, sh.nrows, sh.ncols

	name = sh.cell_value(rowx=138, colx=1)
	# Insert a Person in the person table
	new_person = Person(name = name)
	session.add(new_person)
	session.commit()

	# Insert Arguments  in the argument table
	for rx in range(1, sh.nrows):
		if (sh.cell(rx, 15).value != ''):
			tw_type = sh.cell(rx, 1).value
			argument_type = sh.cell(rx, 4).value
			response_to_question = math.trunc(sh.cell(rx, 15).value)
			response_time = sh.cell(rx, 18).value
			new_argument = Argument(tw_type = tw_type, response_to_question = response_to_question, response_time = response_time, argument_type = argument_type, person = new_person)
			session.add(new_argument)
			session.commit()

#TODO - the sqlite file should be taken from a configuration file
engine = create_engine('sqlite:///arguments.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# It returns a list with the data xlsx files
def get_data_files_list():
	import glob
	return glob.glob("../data/*xlsx")

data_files = get_data_files_list()
for data_file in data_files:
	read_and_store(data_file)

