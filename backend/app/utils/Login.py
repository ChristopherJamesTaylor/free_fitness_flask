import bcrypt
from flask import Blueprint

from app.models import db

adminUtils = Blueprint('adminUtils', __name__)


class AdminUtil:
    def __init__(self):
        pass

    def check_user(self, user_details):
        sql = """ select * from Users
                  where username = '%s'
                            """ % (user_details['username'])
        result = db.session.execute(sql)
        return self.row2dict(result)

    def check_password(self, password, hashed):
        if bcrypt.checkpw(password, hashed):
            print("Password match!")
            return True
        else:
            print("Password didn't match")
            return False

    def if_user(self, user_details):
        print('This is the user data: ', user_details)
        sql = """ select * from Users 
                  where username = '%s'
                            """ % (user_details['username'])
        result = db.session.execute(sql)
        checked_user = self.row2dict(result)
        if checked_user is not None:
            return checked_user
        else:
            return False

    def register_user(self, user_details):
        try:
            print(user_details)
            print("The users details are:", user_details)
            sql = """ START TRANSACTION;    
                      INSERT INTO Users(username, email, password, first_name, last_name, permissions)VALUES ('%s', '%s', '%s', '%s', '%s', 'user');
                      COMMIT;
  """ % (
                user_details['username'], user_details['email'], user_details['password'],
                user_details['firstName'], user_details['lastName'])
            db.session.execute(sql)
        except:
            return False
        return True

    def row2dict(self, result):
        d, a = {}, []
        for rowproxy in result:
            # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
            for column, value in rowproxy.items():
                # build up the dictionary
                d = {**d, **{column: value}}
            return d
