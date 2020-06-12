from flask import Blueprint
from webapp.models import db

nutritionUtils = Blueprint('nutritionUtils', __name__)


class NutritionUtils:
    def __init__(self):
        pass

    def save_plan(self, plan_details):
        sql = """ 
                    insert into NutritionPlan(personID, diet, tdee, allergies)
                    values(%s, '%s', '%s', '%s')
                            """ % (plan_details['personID'], plan_details['diet'], plan_details['tdee'],
                                   plan_details['allergies'])
        db.session.execute(sql)
        db.session.commit()

    def does_plan_exist(self, person_id):
        sql = """ 
                    select * from NutritionPlan
                    where personID = %s
                            """ % person_id
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
