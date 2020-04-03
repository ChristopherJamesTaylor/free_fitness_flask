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
        return adminObject.row2dict(result)

