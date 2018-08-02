import csv, pandas
from statsmodels.formula.api import ols

class Utility():

    def __init__(self, connection = ''):
        self.connection = connection
        self.file_name = '/tmp/_temp.csv'

    def write_file(self, query):
        with open(self.file_name, 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['timeOrAccurancy', 'argument', 'middleTerm'])
            for r in self.connection.execute(query).fetchall():
                spamwriter.writerow([ r[1], r[2], r[3] ])

    def get_model(self):
        with open(self.file_name, 'r') as csvfile:
            data = pandas.read_csv(self.file_name)
            formula = 'timeOrAccurancy ~ C(argument) + C(middleTerm) + C(argument):C(middleTerm)'
            return ols(formula, data).fit()
