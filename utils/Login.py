from flask import Blueprint
from models import db

adminUtils = Blueprint('adminUtils', __name__)


class AdminUtil:
    def __init__(self):
        pass

    def check_user(self, user_details):
        print('This is the user data: ', user_details)
        sql = """ select * from User 
                  where username = '%s' && password= '%s'
                            """ % (user_details['username'], user_details['password'])
        result = db.session.execute(sql)
        return self.row2dict(result)

    def row2dict(self, result):
        d, a = {}, []
        for rowproxy in result:
            # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
            for column, value in rowproxy.items():
                # build up the dictionary
                d = {**d, **{column: value}}
            return d
