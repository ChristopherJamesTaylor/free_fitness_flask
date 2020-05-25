from flask import *
from flask import Blueprint
from app.utils.Fitness import FitnessUtils

fitness_object = FitnessUtils()
simple_page = Blueprint('simple_page', __name__,
                        template_folder="./static/dist")


@simple_page.route('/deleteFitnessPlan', methods=['GET', 'POST'])
def delete_fitness_plan():
    user_details = request.get_json()
    fitness_plan_deleted = fitness_object.get_fitness_plan_id(user_details['id'])
    fitness_object.delete_fitness_plan(fitness_plan_deleted[0]['id'])
    print(fitness_plan_deleted[0]['id'])
    fitness_object.delete_fitness_plan_exercises(fitness_plan_deleted[0]['id'])
    response = {'data': fitness_plan_deleted, 'message': '', 'success': True}
    return response
