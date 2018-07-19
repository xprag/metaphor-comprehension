class Query():

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

    def get_rt_sql(self):
        return '''
            SELECT
                person.id as user_id, tw_type || '-' || argument_type as key,
                avg(response_time) AS value
            FROM argument, person
            WHERE
            person.id = argument.person_id AND
            response_to_question = 1 AND
            argument_block <> 'P' AND
            person.valid = 1 AND
            tw_type <> 'distrattore'
            GROUP BY person.id, key;
            --ORDER BY tw_type, argument_type, argument.id;
        '''
