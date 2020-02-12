from flask import Blueprint
from models import db
from utils.Login import AdminUtil

fitnessUtils = Blueprint('fitnessUtils', __name__)
adminObject = AdminUtil()


class FitnessUtils:
    def __init__(self):
        pass

    def get_exercises(self, user_details):
        sql = """ select * from Exercises
                  where ability = '%s', 
                  type = '%s', 
                            """ % (user_details['training'], user_details['type'])
        result = db.session.execute(sql)
        return adminObject.row2dict(result)
