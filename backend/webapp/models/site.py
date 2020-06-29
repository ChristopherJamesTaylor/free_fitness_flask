from sqlalchemy import Column, String, ForeignKey, Float, DECIMAL, DateTime
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from webapp.models import db


class Exercises(db.Model):
    __tablename__ = 'exercises'

    id = Column(INTEGER(11), primary_key=True)
    ability = Column(String(255))
    sets = Column(String(255))
    reps = Column(INTEGER(255))
    type = Column(String(255))
    name = Column(String(255))
    body_part = Column(String(255))


# example of one to to one
# site = relationship('Exercises', primaryjoin='Exercises.id==PlanExercises.exerciseID', lazy='joined',
#                     foreign_keys='Exercises.id')


class FitnessPlan(db.Model):
    __tablename__ = 'FitnessPlan'

    id = Column(INTEGER(11), primary_key=True)
    personID = Column(INTEGER(11))
    type = Column(String(255))
    trainingLevel = Column(String(255))
    goal = Column(String(255))

    exercises = relationship('PlanExercises', primaryjoin='FitnessPlan.id == PlanExercises.planId', lazy='joined')


class PlanExercises(db.Model):
    __tablename__ = 'PlanExercises'

    id = Column(INTEGER(11), primary_key=True)
    planId = Column(INTEGER(11), ForeignKey('FitnessPlan.id'))
    ability = Column(String(255))
    sets = Column(INTEGER(255))
    reps = Column(INTEGER(255))
    type = Column(String(255))
    exerciseName = Column(String(255))
    bodyPart = Column(String(255))
    day = Column(String(255))


class GymFinder(db.Model):
    __tablename__ = 'GymFinder'

    id = Column(INTEGER(11), primary_key=True)
    gymName = Column(String(255))
    gymLocation = Column(String(255))
    distance = Column(Float(asdecimal=True))
    cost = Column(DECIMAL(10, 2))


class Macro(db.Model):
    __tablename__ = 'Macros'

    age = Column(INTEGER(11))
    sex = Column(String(255))
    height = Column(Float(asdecimal=True))
    weight = Column(Float(asdecimal=True))
    goal = Column(String(255))
    activity_level = Column('activity level', String(255))
    protein = Column(Float(asdecimal=True))
    carbohydrates = Column(Float(asdecimal=True))
    fat = Column(Float(asdecimal=True))
    diet_type = Column('diet type', String(255))
    id = Column(INTEGER(11), primary_key=True)


class TDEE(db.Model):
    __tablename__ = 'TDEE'

    id = Column(INTEGER(11), primary_key=True)
    age = Column(INTEGER(11))
    sex = Column(String(255))
    height = Column(Float(asdecimal=True))
    weight = Column(Float(asdecimal=True))
    activityLevel = Column(String(255))
    bodyFat = Column(Float(asdecimal=True))
    BMI = Column(Float(asdecimal=True))
    idealWeight = Column(Float(asdecimal=True))
    maintenanceCalories = Column(String(255))
    maximumMuscle = Column(String(255))


class Members(db.Model):
    __tablename__ = 'members'

    username = Column(String(255))
    email = Column(String(255))
    user_password = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    permissions = Column(String(255))
    id = Column(INTEGER(11), primary_key=True)


class Foods(db.Model):
    __tablename__ = 'Food'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))
    type = Column(String(255))
    diet = Column(String(255))
    carbohydrates = Column(String(255))
    protein = Column(String(255))
    fat = Column(String(255))
    fibre = Column(String(255))


class NutritionPlan(db.Model):
    __tablename__ = 'Nutrition'

    id = Column(INTEGER(11), primary_key=True)
    personID = Column(INTEGER(11))
    dietType = Column(String(255))
    totalDailyCalories = Column(INTEGER(255))
    mealDate = Column(DateTime)
    fasting = Column(String(255))
    cheatday = Column(String(255))
    macros = Column(String(255))
    breakfast = Column(String(255))
    lunch = Column(String(255))
    dinner = Column(String(255))


class NutritionPlanDetails(db.Model):
    __tablename__ = 'NutritionPlanDetails'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))
    type = Column(String(255))
    diet = Column(String(255))
    carbohydrates = Column(String(255))
    protein = Column(String(255))
    fat = Column(String(255))
    fibre = Column(String(255))
