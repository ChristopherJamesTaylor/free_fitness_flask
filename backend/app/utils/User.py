from flask import Blueprint
from app.models import db
from app.utils.Login import AdminUtil

userUtils = Blueprint('userUtils', __name__)
adminObject = AdminUtil()


class UserUtils:
    def __init__(self):
        pass

    def get_user(self, user_details):
        sql = """ select * from members
                  where username = '%s'
                            """ % user_details['username']
        result = db.session.execute(sql)
        return self.row2dict(result)

    @staticmethod
    def all_profiles():
        sql = """ select * from members
                                """
        result = db.session.execute(sql)
        return adminObject.row2dict(result)

    @staticmethod
    def edit_profile(user_details, person_id):
        sql = """ UPDATE members
                  SET username = '%s', email = '%s', first_name = '%s', last_name='%s'  
                  WHERE id = %s
                            """ % (user_details['username'], user_details['email'], user_details['first_name'],
                                   user_details['last_name'], person_id)
        db.session.execute(sql)
        db.session.commit()

    def row2dict(self, result):
        d, a = {}, []
        for rowproxy in result:
            # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
            for column, value in rowproxy.items():
                # build up the dictionary
                d = {**d, **{column: value}}
            a.append(d)
        return a