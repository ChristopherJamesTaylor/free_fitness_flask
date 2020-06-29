import flask
from flask import Blueprint, jsonify
from sqlalchemy import and_

from webapp.models import db
from webapp.models.site import FitnessPlan, Exercises, PlanExercises
from webapp.utils.Login import AdminUtil
from webapp.utils.ORM import Utils

fitnessUtils = Blueprint('fitnessUtils', __name__)
adminObject = AdminUtil()
ormUtils = Utils()


class FitnessUtils:
    def __init__(self):
        pass

    @staticmethod
    def get_exercises(user_details):
        result = db.session.query(Exercises).filter(and_(Exercises.ability == user_details['ability']),
                                                    Exercises.type == user_details['type']).all()
        return ormUtils.result_to_dict(result)

    @staticmethod
    def get_mixed_exercises(user_details):
        result = db.session.query(Exercises).filter(Exercises.ability == user_details['ability']).all()
        return ormUtils.result_to_dict(result)

    @staticmethod
    def all_fitness_plans():
        result = db.session.query(FitnessPlan).all()
        return ormUtils.result_to_dict(result)

    @staticmethod
    def get_fitness_plan_id(user_details):
        result = db.session.query(FitnessPlan).filter(FitnessPlan.personID == user_details).first()
        return ormUtils.result_to_dict(result)

    @staticmethod
    def get_fitness_plan(plan_id):
        result = db.session.query(PlanExercises).filter(PlanExercises.planId == plan_id).first()
        return ormUtils.result_to_dict(result)

    @staticmethod
    def get_existing_plan(user_details):
        result = db.session.query(FitnessPlan).filter(FitnessPlan.personID == user_details['personID']).first()
        return ormUtils.result_to_dict(result)

    @staticmethod
    def get_plan_id():
        sql = """ SELECT LAST_INSERT_ID() from FitnessPlan
            """
        result = db.session.execute(sql)
        return ormUtils.result_to_dict(result)

    @staticmethod
    def save_fitness_plan(user_details):
        db.session.add(FitnessPlan(personID=user_details['personID'], type=user_details['type'],
                                   trainingLevel=user_details['ability'], goal=user_details['goals']))
        db.session.commit()
        db.session.query(FitnessPlan).filter(FitnessPlan.personID == user_details['personID']).first()

    @staticmethod
    def save_exercises_plan(exercises):
        db.session.add(PlanExercises(planId=exercises['planId'], ability=exercises['ability'], sets=exercises['sets'],
                                     reps=exercises['reps'], type=exercises['type'], exerciseName=exercises['name'],
                                     bodyPart=exercises['body_part'], day=exercises['day']))
        db.session.commit()

    @staticmethod
    def delete_fitness_plan(plan_id):
        db.session.query(FitnessPlan).filter(FitnessPlan.id == plan_id).delete()
        db.session.commit()

    @staticmethod
    def delete_fitness_plan_exercises(plan_id):
        db.session.query(PlanExercises).filter(PlanExercises.planId == plan_id).delete()
        db.session.commit()

    @staticmethod
    def save_edited_plan(user_details, plan_id):
        db.session.query(PlanExercises).filter(and_(PlanExercises.planId == plan_id, PlanExercises.id ==
                                                    user_details['id'])).update(
            {PlanExercises.ability: user_details['ability'],
             PlanExercises.sets: user_details['sets'],
             PlanExercises.reps: user_details['reps'],
             PlanExercises.exerciseName: user_details['exerciseName'],
             PlanExercises.bodyPart: user_details['bodyPart'],
             PlanExercises.day: user_details['day']})
        db.session.commit()
