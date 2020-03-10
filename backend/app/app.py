import requests
from flask import *
from flask_cors import CORS, cross_origin

from app.utils.Fitness import FitnessUtils
from app.utils.Login import AdminUtil
from app.models import db
from app.utils.User import UserUtils
import bcrypt

admin_obj = AdminUtil()
user_object = UserUtils()
fitness_object = FitnessUtils()
app = Flask(__name__,
            static_folder="./static",
            template_folder="./static/dist")

cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://freefitnessflask:chris@db/FreeFitness"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ApiUrl = "https://api.hippoapi.com/v3/more/json"
queryFormatString = "{0}/{1}/{2}"
YourAPIKey = '2CA872CD'


@app.route('/getMealPlan', methods=['GET', 'POST'])
def get_meal_plan():
    data = request.get_json()
    url = "https://api.spoonacular.com/mealplanner/generate?apiKey=3a07469279f3438bb054203338126b62"
    payload = {}
    print('This is the data:', data)
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
    return user_object.get_user(user_details)


@app.route('/getExercises', methods=['GET', 'POST'])
def get_exercises():
    user_details = request.get_json()
    all_exercises = fitness_object.get_exercises(user_details)
    for e in all_exercises:
        if e['body_part'] == 'chest':
            e['day'] = 'Monday and Friday'
        elif e['body_part'] == 'legs':
            e['day'] = 'Tuesday'
        elif e['body_part'] == 'shoulders':
            e['day'] = 'Wednesday'
        elif e['body_part'] == 'arms':
            e['day'] = 'Thursday'
        elif e['body_part'] == 'back':
            e['day'] = 'Monday and Friday'
        elif e['body_part'] == 'fullbody':
            e['day'] = 'Saturday'
        e['rest_days'] = 7 - len(user_details['days'])
    print(all_exercises)
    return jsonify(all_exercises)


@app.route('/getFitnessPlan', methods=['GET', 'POST'])
def get_fitness_plan():
    user_details = request.get_json()
    existing_plan = user_object.get_fitness_plan(user_details)
    if existing_plan:
        return {'exists': True, 'plan': existing_plan}
    else:
        return {'exists': False}


@app.route('/checkUser', methods=['GET', 'POST'])
def login():
    user_data = request.get_json()
    database_details = admin_obj.check_user(user_details=user_data)
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


if __name__ == '__main__':
    app.run()
