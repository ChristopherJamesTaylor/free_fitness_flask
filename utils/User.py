from flask import Blueprint
from models import db
from utils.Login import AdminUtil

userUtils = Blueprint('userUtils', __name__)
adminObject = AdminUtil()


class UserUtils:
    def __init__(self):
        pass

    def get_user(self, user_details):
        sql = """ select * from Users
                  where username = '%s'
                            """ % user_details['username']
        result = db.session.execute(sql)
        return adminObject.row2dict(result)
