class Query():

    def get_response_time_sql(self):
        return '''
            SELECT tw_type, argument_type, group_concat(response_time) as responses
            FROM argument, person
            WHERE
            person.id = argument.person_id and
            response_to_question = 1 and
            argument_block <> 'P' and person.valid = 0 and
            tw_type <> 'distrattore'
            group by tw_type, argument_type;
        '''
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
