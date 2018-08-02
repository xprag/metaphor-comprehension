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
    utility.write_file(query.get_accuracy_argumentType_middleTerm())
    print anova_lm(utility.get_model(), typ=2)

def getResponseTimeAnova():
    utility.write_file(query.get_responseTime_argumentType_middleTerm())
    print anova_lm(utility.get_model(), typ=2)
