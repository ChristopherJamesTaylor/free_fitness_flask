from sqlite3 import DatabaseError, InterfaceError

import bcrypt
from flask import Blueprint, jsonify

from app.models import db

adminUtils = Blueprint('adminUtils', __name__)


class AdminUtil:
    def __init__(self):
        pass

    def check_user(self, user_details):
        sql = """ select * from members
                  where username = '%s'
                            """ % (user_details['username'])
        result = db.session.execute(sql)
        return self.row2dict(result)

    def check_password(self, password, hashed):
        print("Check password!", flush=True)
        if bcrypt.checkpw(password, hashed):
            print("Password match!", flush=True)
            return True
        else:
            print("Password didn't match", flush=True)
            return False

    def if_user(self, user_details):
        sql = """ select * from members 
                  where username = '%s'
                            """ % (user_details['username'])
        result = db.session.execute(sql)
        checked_user = self.row2dict(result)
        if checked_user != {}:
            return checked_user
        else:
            return False

    def register_user(self, user_details):
        sql = """  
                                INSERT INTO members(username, email, user_password, first_name, last_name, permissions) 
                                VALUES ('%s', '%s', '%s', '%s', '%s', 'user');
              """ % (user_details['username'], user_details['email'], user_details['password'], user_details['firstName'], user_details['lastName'])
        result = db.session.execute(sql)
        db.session.commit()
        if result:
            return True
        else:
            return False

    def row2dict(self, result):
        d, a = {}, []
        for rowproxy in result:
            # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
            for column, value in rowproxy.items():
                # build up the dictionary
                d = {**d, **{column: value}}
        return d
