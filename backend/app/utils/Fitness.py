import flask
from flask import Blueprint, jsonify
from app.models import db
from app.utils.Login import AdminUtil

fitnessUtils = Blueprint('fitnessUtils', __name__)
adminObject = AdminUtil()


class FitnessUtils:
    def __init__(self):
        pass

    def get_exercises(self, user_details):
        sql = """ SELECT *
                    FROM exercises
                    WHERE ability = '%s' AND type = '%s'
                            """ % (user_details['training'], user_details['type'])
        result = db.session.execute(sql)
        return self.row2dict(result)

    def get_mixed_exercises(self, user_details):
        sql = """ SELECT *
                    FROM exercises
                    WHERE ability = '%s'
                            """ % (user_details['training'])
        result = db.session.execute(sql)
        return self.row2dict(result)

    def all_fitness_plans(self):
        sql = """ SELECT *
                  FROM FitnessPlan
                            """
        result = db.session.execute(sql)
        return self.row2dict(result)

    def get_plan_id(self):
        sql = """ SELECT LAST_INSERT_ID() from FitnessPlan
            """
        result = db.session.execute(sql)
        return self.row2dict(result)

    def save_fitness_plan(self, user_details):
        print(user_details['personID'])
        sql = """ 
            INSERT INTO FitnessPlan ( personID, type, trainingLevel, goal )
            VALUES ( %s, '%s', '%s', '%s' );
                            """ % (user_details['personID'], user_details['type'],
                                   user_details['training'], user_details['goals'])
        result = db.session.execute(sql)
        db.session.commit()
        if result:
            return True
        else:
            return False

    def save_exercises_plan(self, exercises):
        sql = """ 
            insert into PlanExercises (planId, ability, sets, reps, type, exerciseName, bodypart, day)
            values (%s, '%s', %s, '%s', '%s','%s', '%s','%s')
                            """ % (exercises['planId'], exercises['ability'],
                                   exercises['sets'], exercises['reps'],
                                   exercises['type'], exercises['name'], exercises['body_part'],
                                   exercises['day'])
        result = db.session.execute(sql)
        db.session.commit()
        if result:
            return True
        else:
            return False

    def get_fitness_plan_id(self, user_details):
        sql = """ SELECT id
                    FROM FitnessPlan
                    WHERE personID = %s
                            """ % user_details
        result = db.session.execute(sql)
        return self.row2dict(result)

    def get_fitness_plan(self, plan_id):
        sql = """ SELECT *
                    FROM PlanExercises
                    WHERE  planId = %s
                            """ % plan_id
        result = db.session.execute(sql)
        return self.row2dict(result)

    def get_existing_plan(self, user_details):
        sql = """ select * from FitnessPlan
                  where personID = %s
                            """ % user_details['personID']
        result = db.session.execute(sql)
        return self.row2dict(result)

    @staticmethod
    def save_edited_plan(user_details, plan_id):
        sql = """ 
            UPDATE PlanExercises
            SET ability= '%s', sets = %s, reps = %s, exerciseName = '%s', bodyPart = '%s', day = '%s' 
            WHERE planId = %s and id = %s
                            """ % (user_details['ability'], user_details['sets'],
                                   user_details['reps'], user_details['exerciseName'],
                                   user_details['bodyPart'], user_details['day'], plan_id, user_details['id'])
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
            a.append(d)
        return a

