import requests
from flask import *
from flask_cors import CORS, cross_origin

from app.utils.Fitness import FitnessUtils
from app.utils.Login import AdminUtil
from app.models import db
from app.utils.User import UserUtils
from app.routes.fitness import simple_page
import bcrypt

admin_obj = AdminUtil()
user_object = UserUtils()
fitness_object = FitnessUtils()

app = Flask(__name__,
            static_folder="./static",
            template_folder="./static/dist")
app.register_blueprint(simple_page)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://freefitnessflask:chris@db/FreeFitness"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ApiUrl = "https://api.hippoapi.com/v3/more/json"
queryFormatString = "{0}/{1}/{2}"
YourAPIKey = '2CA872CD'


@app.route('/getGyms', methods=['GET', 'POST'])
def get_gyms():
    data = request.get_json()
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(data['lat']) + ',' + \
          str(data['long']) + "&radius=20000&type=gym&key=AIzaSyB6bC_OukDUo3yP4mV6DF9mZ5qFvOmKH-0"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


@app.route('/getMealPlan', methods=['GET', 'POST'])
def get_meal_plan():
    data = request.get_json()
    url = "https://api.spoonacular.com/mealplanner/generate?apiKey=3a07469279f3438bb054203338126b62"
    payload = {}
    if data['diet'] == "standard":
        querystring = {"timeFrame": "week", "targetCalories": data['calories'], "exclude": data['allergies']}
    elif data['diet'] == 'standard' and data['allergies'] == 'none':
        querystring = {"timeFrame": "week", "targetCalories": data['calories']}
    elif data['allergies'] == 'none':
        querystring = {"timeFrame": "week", "targetCalories": data['calories'], "diet": data['diet']}
    else:
        querystring = {"timeFrame": "week", "targetCalories": data['calories'], "diet": data['diet'],
                       "exclude": data['allergies']}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload, params=querystring)
    plan = response.json()
    meals = {
        'breakfast': '',
        'lunch': '',
        'dinner': '',
        "protein": '',
        "carbohydrates": '',
        "fat": '',
        "day": '',
        "cookInMinutes": []
    }
    meal_plan = make_meal_plan(plan, meals)
    return jsonify(meal_plan)


@app.route('/getUser', methods=['GET', 'POST'])
def get_user():
    user_details = request.get_json()
    return jsonify(user_object.get_user(user_details))


@app.route('/allProfiles', methods=['GET', 'POST'])
def all_profiles():
    return jsonify(user_object.all_profiles())


@app.route('/allFitnessPlans', methods=['GET', 'POST'])
def all_fitness_plans():
    return jsonify(fitness_object.all_fitness_plans())


@app.route('/editProfile', methods=['GET', 'POST'])
def edit_profile():
    user_details = request.get_json()
    person_id = request.get_json()
    user_object.edit_profile(user_details['profile'][0],
                             person_id['id'])
    return jsonify(user_object.get_user(user_details['profile'][0]))


@app.route('/getExercises', methods=['GET', 'POST'])
def get_exercises():
    user_details = request.get_json()
    all_exercises = None

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

    elif len(user_details['days']) == 5 and user_details['training'] != 'savage':
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
    elif user_details['training'] == 'savage' and len(user_details['days']) > 5:
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


@app.route('/getHomeWorkout', methods=['GET', 'POST'])
def get_home_workout():
    user_details = request.get_json()
    all_exercises = fitness_object.get_exercises(user_details)
    return jsonify(all_exercises)


@app.route('/getFitnessPlan', methods=['GET', 'POST'])
def get_fitness_plan():
    user_details = request.get_json()
    plan_id = fitness_object.get_fitness_plan_id(user_details['personID'])
    existing_plan = fitness_object.get_fitness_plan(plan_id[0]['id'])
    return jsonify(existing_plan)


@app.route('/checkUser', methods=['GET', 'POST'])
def login():
    user_data = request.get_json()
    database_details = admin_obj.check_user(user_details=user_data)
    print('the database is ', database_details)
    if database_details != {}:
        password = user_data['password'].encode("utf-8")
        hashed = database_details['user_password'].encode("utf-8")
        password_check = admin_obj.check_password(password, hashed)
        if password_check:
            return {'row': database_details,
                    'status': True
                    }
        else:
            return {
                'row': '',
                'status': False
            }
    else:
        return {
            'row': '',
            'status': False
        }


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('user_name', None)
    return True


@app.route('/registerUser', methods=['GET', 'POST'])
def register():
    user_details = {'status': False}
    data = request.get_json()
    if_user = admin_obj.if_user(data)
    if if_user is False:
        hashed_password = encrypt_password(data)
        data['password'] = hashed_password
        user_details['status'] = admin_obj.register_user(user_details=data)
        if user_details['status']:
            return user_details
        else:
            return user_details


def encrypt_password(data):
    password = data['password'].encode("utf-8")
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    hashed = hashed.decode("utf-8")
    return hashed


def make_meal_plan(response, meals):
    plan = []
    days = response['week'].keys()
    for i in days:
        meals['day'] = i
        meals['breakfast'] = response['week'][i]['meals'][0]['title']
        meals['lunch'] = response['week'][i]['meals'][1]['title']
        meals['dinner'] = response['week'][i]['meals'][2]['title']
        for j in response['week'][i]['meals']:
            meals['cookInMinutes'].append(j['readyInMinutes'])
        meals['protein'] = response['week'][i]['nutrients']['protein']
        meals['carbohydrates'] = response['week'][i]['nutrients']['carbohydrates']
        meals['fat'] = response['week'][i]['nutrients']['fat']
        plan.append(meals)
        meals = {
            'breakfast': '',
            'lunch': '',
            'dinner': '',
            "protein": '',
            "carbohydrates": '',
            "fat": '',
            "day": '',
            "cookInMinutes": []
        }
    return plan


@app.route('/getMacros', methods=['GET', 'POST'])
def get_macros():
    data = request.get_json()
    print(data)
    tdee = 0
    macros = {
        'protein': 0,
        'carbohydrates': 0,
        'fat': 0,
    }
    bmr = 0
    # calculate Basic Metabolic Rate first

    if data['unit'] == 'metric':
        if data['sex'] == 'male':
            bmr = 65 + (13.7 * float(data['weight'])) + (5 * float(data['height'])) - (6.8 * float(data['age']))
            print(bmr)
        else:
            print('Woman')
            bmr = 655 + (13.7 * float(data['weight'])) + (1.8 * float(data['height'])) - (4.7 * float(data['age']))

    elif data['unit'] == 'imperial':
        if data['sex'] == 'male':
            bmr = 66 + (6.23 * float(data['weight'])) + (12.7 * float(data['height'])) - (
                    6.8 * float(data['age']))
        else:
            print('Woman')
            bmr = 655.1 + (4.35 * float(data['weight'])) + (4.7 * float(data['height'])) - (
                    4.7 * float(data['age']))

    # calculate TDEE
    if data['activity'] == 'sedentary':
        tdee = bmr * 1.2
        print('The TDEE is:', tdee)
    #     Office worker getting little or no exercise
    elif data['activity'] == 'active':
        tdee = bmr * 1.55
    #     Construction worker or person running one hour daily
    else:
        tdee = bmr * 1.75
    #     	Agricultural worker (non mechanized) or person swimming two hours daily
    # calculate macros
    if data['goal'] == 'fatLoss':
        # 10% drop and increase in protein
        print('fat loss')
        drop = tdee * 0.1
        tdee = tdee - drop
        macros = {
            'tdee': tdee,
            'protein': (tdee * 0.3) / 4,
            'carbohydrates': (tdee * 0.5) / 4,
            'fat': (tdee * 0.2) / 9,
        }

    elif data['goal'] == 'muscleGain':
        # 10% increase and increase in protein
        print('bulk')
        gain = tdee * 0.1
        tdee = tdee + gain
        macros = {
            'tdee': tdee,
            'protein': (tdee * 0.4) / 4,
            'carbohydrates': (tdee * 0.4) / 4,
            'fat': (tdee * 0.2) / 9,
        }
    else:
        macros = {
            'tdee': tdee,
            'protein': (tdee * 0.3) / 4,
            'carbohydrates': (tdee * 0.5) / 4,
            'fat': (tdee * 0.2) / 9,
        }
    # The 95 % confidence range for men is ±213.0 kcal / day, and ±201.0 kcal / day for women.
    response = {
        'Macros': macros
    }
    return jsonify(response)


@app.route('/savePlan', methods=['GET', 'POST'])
def save_fitness_plan():
    user_details = request.get_json()
    seperator = ', '
    if isinstance(user_details['days'], list):
        user_details['days'] = seperator.join(user_details['days'])
    for e in user_details['exercises']:
        if 'day' in e:
            if isinstance(e['day'], list):
                e['day'] = seperator.join(e['day'])
                print(e['day'])
        else:
            e['day'] = ''
    plan_exist = fitness_object.get_fitness_plan_id(user_details['personID'])
    if not bool(plan_exist):
        plan_insert_bool = fitness_object.save_fitness_plan(user_details)
        if plan_insert_bool:
            plan_id = fitness_object.get_fitness_plan_id(user_details['personID'])
            for exercises in user_details['exercises']:
                exercises['planId'] = plan_id[0]['id']
                saved_plan = fitness_object.save_exercises_plan(exercises)
            if saved_plan:
                plan_id = fitness_object.get_fitness_plan_id(user_details['personID'])
                fitness_plan = fitness_object.get_fitness_plan(plan_id[0]['id'])
                return jsonify(fitness_plan)
    else:
        plan_id = fitness_object.get_fitness_plan_id(user_details['personID'])
        fitness_plan = fitness_object.get_fitness_plan(plan_id[0]['id'])
        return jsonify(fitness_plan)


@app.route('/editedPlan', methods=['GET', 'POST'])
def save_edited_plan():
    user_details = request.get_json()
    plan_id = fitness_object.get_fitness_plan_id(user_details['personID'])
    for exercise_id in user_details['plan']:
        current_index = user_details['plan'].index(exercise_id)
        fitness_object.save_edited_plan(user_details['plan'][current_index], plan_id[0]['id'])
    return jsonify(fitness_object.get_fitness_plan(plan_id[0]['id']))


if __name__ == '__main__':
    app.run()
