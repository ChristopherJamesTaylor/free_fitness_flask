from flask import *
from flask import Blueprint
from webapp.utils.Fitness import FitnessUtils

fitness_object = FitnessUtils()
fitness = Blueprint('simple_page', __name__,
                    template_folder="./static/dist")


@fitness.route('/allFitnessPlans', methods=['GET', 'POST'])
def all_fitness_plans():
    plans = fitness_object.all_fitness_plans()
    response = {'row': plans, 'message': '', 'status': True}
    return response


@fitness.route('/getHomeWorkout', methods=['GET', 'POST'])
def get_home_workout():
    user_details = request.get_json()
    all_exercises = fitness_object.get_exercises(user_details)
    return jsonify(all_exercises)


@fitness.route('/getFitnessPlan', methods=['GET', 'POST'])
def get_fitness_plan():
    user_details = request.get_json()
    plan_id = fitness_object.get_fitness_plan_id(user_details['personID'])
    existing_plan = fitness_object.get_fitness_plan(plan_id[0]['id'])
    return jsonify(existing_plan)


@fitness.route('/Exercises', methods=['GET', 'POST'])
def exercises():
    user_details = request.get_json()
    if user_details['type'] == 'mixed':
        all_exercises = fitness_object.get_mixed_exercises(user_details)
    else:
        all_exercises = fitness_object.get_exercises(user_details)
    if len(user_details['days']) == 3:
        for e in all_exercises:
            if e['body_part'] == 'chest':
                e['day'] = user_details['days'][0]
            elif e['body_part'] == 'abs':
                e['day'] = user_details['days']
            elif e['body_part'] == 'legs':
                e['day'] = user_details['days'][1]
            elif e['body_part'] == 'shoulders':
                e['day'] = user_details['days'][2]
            elif e['body_part'] == 'arms':
                e['day'] = user_details['days'][2]
            elif e['body_part'] == 'back':
                e['day'] = user_details['days'][0]
            elif e['body_part'] == 'fullbody':
                e['day'] = user_details['days'][1]
    elif len(user_details['days']) == 4:
        for e in all_exercises:
            if e['body_part'] == 'chest':
                e['day'] = user_details['days'][0] + '\t' + user_details['days'][2]
            elif e['body_part'] == 'abs':
                e['day'] = user_details['days']
            elif e['body_part'] == 'legs':
                e['day'] = user_details['days'][1] + '\t' + user_details['days'][3]
            elif e['body_part'] == 'shoulders':
                e['day'] = user_details['days'][1] + '\t' + user_details['days'][3]
            elif e['body_part'] == 'arms':
                e['day'] = user_details['days'][1] + '\t' + user_details['days'][2]
            elif e['body_part'] == 'back':
                e['day'] = user_details['days'][0] + '\t' + user_details['days'][2]

    elif len(user_details['days']) == 5 and user_details['ability'] != 'savage':
        for e in all_exercises:
            if e['body_part'] == 'chest':
                e['day'] = user_details['days'][0]
            elif e['body_part'] == 'abs':
                e['day'] = user_details['days']
            elif e['body_part'] == 'legs':
                e['day'] = user_details['days'][1]
            elif e['body_part'] == 'shoulders':
                e['day'] = user_details['days'][2]
            elif e['body_part'] == 'arms':
                e['day'] = user_details['days'][3]
            elif e['body_part'] == 'back':
                e['day'] = user_details['days'][0]
            elif e['body_part'] == 'fullbody' and len(user_details['days']) > 5:
                e['day'] = user_details['days'][5]
    elif user_details['ability'] == 'savage' and len(user_details['days']) > 5:
        for e in all_exercises:
            if e['body_part'] == 'chest':
                e['day'] = user_details['days'][0] + '\t' + user_details['days'][4]
            elif e['body_part'] == 'abs':
                e['day'] = user_details['days']
            elif e['body_part'] == 'legs':
                e['day'] = user_details['days'][1]
            elif e['body_part'] == 'shoulders':
                e['day'] = user_details['days'][2] + '\t' + user_details['days'][3]
            elif e['body_part'] == 'arms':
                e['day'] = user_details['days'][3] + '\t' + user_details['days'][2]
            elif e['body_part'] == 'back':
                e['day'] = user_details['days'][0] + '\t' + user_details['days'][4]
            elif e['body_part'] == 'fullbody':
                e['day'] = user_details['days'][6]
    return jsonify(all_exercises)


@fitness.route('/savePlan', methods=['GET', 'POST'])
def save_fitness_plan():
    user_details = request.get_json()
    seperator = ', '
    if isinstance(user_details['days'], list):
        user_details['days'] = seperator.join(user_details['days'])
    for e in user_details['exercises']:
        if 'day' in e:
            if isinstance(e['day'], list):
                e['day'] = seperator.join(e['day'])
        else:
            e['day'] = ''
    exist_fitness_plan = fitness_object.get_fitness_plan(user_details)
    if exist_fitness_plan is not {}:
        return exist_fitness_plan
    else:
        fitness_object.save_fitness_plan(user_details)
        plan_id = fitness_object.get_fitness_plan_id(user_details['personID'])
        for exercise in user_details['exercises']:
            exercise['planId'] = plan_id['id']
            fitness_object.save_exercises_plan(exercise)
        plan = fitness_object.get_fitness_plan(plan_id['id'])
        return plan


@fitness.route('/editedPlan', methods=['GET', 'POST'])
def save_edited_plan():
    user_details = request.get_json()
    plan_id = fitness_object.get_fitness_plan_id(user_details['personID'])
    for exercise_id in user_details['plan']:
        current_index = user_details['plan'].index(exercise_id)
        fitness_object.save_edited_plan(user_details['plan'][current_index], plan_id['id'])
    return jsonify(fitness_object.get_fitness_plan(plan_id['id']))


@fitness.route('/deleteFitnessPlan', methods=['GET', 'POST'])
def delete_fitness_plan():
    user_details = request.get_json()
    fitness_plan_deleted = fitness_object.get_fitness_plan_id(user_details['id'])
    fitness_object.delete_fitness_plan(fitness_plan_deleted['id'])
    fitness_object.delete_fitness_plan_exercises(fitness_plan_deleted['id'])
    response = {'data': fitness_plan_deleted, 'message': '', 'success': True}
    return response
