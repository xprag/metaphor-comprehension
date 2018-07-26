from sqlalchemy import create_engine, func
from sqlalchemy.sql import select, text
import json, sys, os, csv
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
# my libs
from utility import Utility
from query import Query
query = Query(0)

db_file_name = 'arguments.db'
if os.path.isfile(db_file_name):
    engine = create_engine('///'.join(['sqlite:', db_file_name]))
else:
    raise Exception('The following file %s does not exist: ' % db_file_name)

conn = engine.connect()
utility = Utility(conn)

def getAnswersAnova():
    utility.write_file(query.get_accurancy_argumentType_middleTerm())
    print "\n\n####### getAnswersAnova #######"
    print anova_lm(utility.get_model(), typ=2)

def getResponseTimeAnova():
    print query.get_responseTime_argumentType_middleTerm()
    utility.write_file(query.get_responseTime_argumentType_middleTerm())
    print anova_lm(utility.get_model(), typ=2)

def getResponseTimeAnova_old():
    s = text("""
        SELECT person.id, avg(response_time), argument_type, tw_type
        FROM argument, person
        WHERE
        person.id = argument.person_id and
        argument_block <> 'P' and person.valid = 1 and
        tw_type <> 'distrattore'
	    group by person.id, argument_type, tw_type
        order by   person.id, argument_type, tw_type;
    """)
    file_name = 'responseTime.csv'

    with open(file_name, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['responseTime', 'argument', 'term'])
        for r in conn.execute(s).fetchall():
            spamwriter.writerow([ r[1], r[2], r[3] ])

    with open(file_name, 'r') as csvfile:
        data = pd.read_csv(file_name)
        formula = 'responseTime ~ C(argument) + C(term) + C(argument):C(term)'
        model = ols(formula, data).fit()
    print "\n\n####### getResponseTimeAnova #######"
    aov_table = anova_lm(model, typ=2)
    print aov_table
