class Query():

    def __init__(self, isCorrect = 0):
        self.correctText = '** Correct answers **' if isCorrect == 1 else ' ** Wrong answers **'
        self.isCorrect = str(isCorrect)

    def get_accurancy_argumentType(self):
        return self._get_query('response_to_question', 'argument_type')

    def get_accurancy_middleTerm(self):
        return self._get_query('response_to_question', 'tw_type')

    def get_accurancy_argumentType_middleTerm(self):
        return self._get_query('response_to_question', 'tw_type || "-" || argument_type')

    def get_accurancy_metafore(self):
        return self._get_query('response_to_question', '"CM+NM"', 'AND (tw_type = "CM" OR tw_type = "NM")')

    def get_responseTime_argumentType(self):
        return self._get_query('response_time', 'argument_type', 'AND response_to_question = ' + self.isCorrect)

    def get_responseTime_middleTerm(self):
        return self._get_query('response_time', 'tw_type', 'AND response_to_question = ' + self.isCorrect)

    def get_responseTime_argumentType_middleTerm(self):
        return self._get_query('response_time', 'tw_type || "-" || argument_type',\
            'AND response_to_question = ' + self.isCorrect)

    def _get_accurancy_letterali(self):
        return self._get_query('response_to_question', '"H+PM"', 'AND (tw_type = "H" OR tw_type = "P")')

    def get_accurancy_letterali_metafore(self):
        return self._get_accurancy_letterali().rstrip()[:-1] + ' UNION ' + self.get_accurancy_metafore()

    ###  argument_type (TC/FC/PC) vs literal (H+P) e metaphorical (CM+NM) middle terms
    def get_accurancy_argumentType_vs_literalAndMetaphor(self):
        return self._get_accurancy_argumentTypeAndLiteral().rstrip()[:-1] + ' UNION ' + self._get_accurancy_argumentTypeAndMetaphor()

    ###  argument_type (TC/FC/PC) vs literal (H+P) e metaphorical (CM+NM) middle terms
    def get_responseTime_argumentType_vs_literalAndMetaphor(self):
        return self._get_responseTime_argumentTypeAndLiteral().rstrip()[:-1] + ' UNION ' +\
            self._get_responseTime_argumentTypeAndMetaphor()

    def _get_accurancy_argumentTypeAndLiteral(self):
        return self._get_query('response_to_question', 'argument_type || "_" || "CM+NM"', 'AND (tw_type = "CM" OR tw_type = "NM")')

    def _get_accurancy_argumentTypeAndMetaphor(self):
        return self._get_query('response_to_question', 'argument_type || "_" || "H+P"', 'AND (tw_type = "H" OR tw_type = "P")')

    def _get_responseTime_argumentTypeAndLiteral(self):
        return self._get_query('response_time', 'argument_type || "_" || "CM+NM"', \
            'AND (tw_type = "CM" OR tw_type = "NM") AND response_to_question = ' + self.isCorrect)

    def _get_responseTime_argumentTypeAndMetaphor(self):
        return self._get_query('response_time', 'argument_type || "_" || "H+P"', \
            'AND (tw_type = "H" OR tw_type = "P")  AND response_to_question = ' + self.isCorrect)

    def _get_query(self, timeOrAccurancy, columns, condition = ''):
        str = '''
            SELECT
                person.id as user_id,
                avg(%s) AS value,
                %s AS key
            FROM argument, person
            WHERE
            person.id = argument.person_id AND
            argument_block <> 'P' AND
            person.valid = 1 AND
            tw_type <> 'distrattore'
            %s -- condition
            GROUP BY person.id, key;
        ''' % (timeOrAccurancy, columns, condition)
        return str

    # TODO rename or delete
    def get_response_to_question_sql(self):
        return '''
            SELECT
            tw_type, argument_type, group_concat(response_to_question) as responses
            FROM argument, person
            WHERE
            person.id = argument.person_id and
            argument_block <> 'P' and person.valid = 1 and
            tw_type <> 'distrattore'
            group by tw_type, argument_type;
        '''
    # TODO deprecated
    def get_response_time_sql(self):
        return '''
            SELECT tw_type, argument_type, group_concat(response_time) as responses
            FROM argument, person
            WHERE
            person.id = argument.person_id and
            response_to_question = 1 and
            argument_block <> 'P' and person.valid = 1 and
            tw_type <> 'distrattore'
            group by tw_type, argument_type
            order by person.id;
        '''
