from flask import Blueprint
from webapp.models import db
from webapp.models.site import NutritionPlan
from webapp.utils.ORM import Utils

nutritionUtils = Blueprint('nutritionUtils', __name__)
ormUtils = Utils()


class NutritionUtils:
    def __init__(self):
        pass

    @staticmethod
    def save_plan(plan_details):
        db.session.add(NutritionPlan(personID=plan_details['personID'], dietType=plan_details['diet'],
                                     totalDailyCalories=plan_details['calories'], mealDate=plan_details['mealDate'],
                                     fasting=plan_details['fasting'], cheatday=plan_details['cheat'],
                                     macros=plan_details['macros'], breakfast=plan_details['breakfast'], lunch=
                                     plan_details['lunch'], dinner=plan_details['dinner']))
        db.session.commit()

    @staticmethod
    def does_plan_exist(person_id):
        result = db.session.query(NutritionPlan).filter(NutritionPlan.personID == person_id)
        return ormUtils.result_to_dict(result)
