import requests
from flask import *
from flask_cors import CORS

from utils.Fitness import FitnessUtils
from utils.Login import AdminUtil
from models import db
import bcrypt
from utils.User import UserUtils

admin_obj = AdminUtil()
user_object = UserUtils()
fitness_object = FitnessUtils()
app = Flask(__name__,
            static_folder="./static",
            template_folder="./static/dist")

cors = CORS(app, resources={r"*": {"origins": "*"}})
app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root@localhost/FreeFitness"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ApiUrl = "https://api.hippoapi.com/v3/more/json"
queryFormatString = "{0}/{1}/{2}"
YourAPIKey = '2CA872CD'


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
    if 'user_name' in session:
        return 'Logged in as %s' % escape(session['username'])
    else:
        user_data = request.get_json()
        database_details = admin_obj.check_user(user_details=user_data)

        session["user_name"] = database_details['username']
        print(session.get('user_name'))
        session.modified = True

        password = user_data['password'].encode("utf-8")
        hashed = database_details['password'].encode("utf-8")
        password_check = admin_obj.check_password(password, hashed)

        if password_check:
            return database_details
        else:
            return False


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('user_name', None)
    return True


@app.route('/registerUser', methods=['GET', 'POST'])
def register():
    data = request.get_json()
    if_user = admin_obj.if_user(data)
    email = data['email']
    url = "https://api.hippoapi.com/v3/more/json/2CA872CD/" + email
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = response.json()
    if if_user is False and response_json['emailVerification']['syntaxVerification']['isSyntaxValid']:
        hashed_password = encrypt_password(data)
        data['password'] = hashed_password
        user_details = admin_obj.register_user(user_details=data)
        if user_details:
            return data


def encrypt_password(data):
    password = data['password'].encode("utf-8")
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    hashed = hashed.decode("utf-8")
    return hashed


if __name__ == '__main__':
    app.run()
