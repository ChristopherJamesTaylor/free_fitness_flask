from flask import Blueprint
from app.models import db
from app.utils.Login import AdminUtil

fitnessUtils = Blueprint('fitnessUtils', __name__)
adminObject = AdminUtil()


class FitnessUtils:
    def __init__(self):
        pass

    def get_exercises(self, user_details):
        sql = """ SELECT *
                    FROM Exercises
                    WHERE ability = '%s' AND type = '%s'
                            """ % (user_details['training'], user_details['type'])
        result = db.session.execute(sql)
        return self.row2dict(result)

    def row2dict(self, result):
        d, a = {}, []
        for rowproxy in result:
            # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
            for column, value in rowproxy.items():
                # build up the dictionary
                d = {**d, **{column: value}}
            a.append(d)
        return a
