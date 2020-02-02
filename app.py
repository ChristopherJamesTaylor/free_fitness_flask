import urllib.request

import requests
from flask import Flask, request, session
from flask_cors import CORS
from utils.Login import AdminUtil
from models import db
import bcrypt

admin_obj = AdminUtil()

app = Flask(__name__,
            static_folder="./static",
            template_folder="./static/dist")
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root@localhost/FreeFitness"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ApiUrl = "https://api.hippoapi.com/v3/more/json"
queryFormatString = "{0}/{1}/{2}"
YourAPIKey = '2CA872CD'


@app.route('/getSession', methods=['GET', 'POST'])
def get_session():
    session_data = request.get_json()
    user = admin_obj.check_user(session_data)
    session['user_details'] = user
    value = {}
    for key in session.keys():
        value[key] = session[key]
    return value


@app.route('/checkUser', methods=['GET', 'POST'])
def login():
    user_data = request.get_json()
    database_details = admin_obj.check_user(user_details=user_data)
    password = user_data['password'].encode("utf-8")
    hashed = database_details['password'].encode("utf-8")
    password_check = admin_obj.check_password(password, hashed)
    if password_check:
        session['user_details'] = database_details
        value = {}
        for key in session.keys():
            value[key] = session[key]
        return value
    else:
        return False


@app.route('/registerUser', methods=['GET', 'POST'])
def register():
    data = request.get_json()
    if_user = admin_obj.if_user(data)
    print(if_user)
    email = data['email']
    url = "https://api.hippoapi.com/v3/more/json/2CA872CD/" + email
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = response.json()
    print(response_json['emailVerification']['syntaxVerification']['isSyntaxValid'])
    if if_user is False and response_json['emailVerification']['syntaxVerification']['isSyntaxValid']:
        hashed_password = encrypt_password(data)
        print(hashed_password)
        data['password'] = hashed_password
        user_details = admin_obj.register_user(user_details=data)
        if user_details:
            return data
    else:
        return {}


def encrypt_password(data):
    password = data['password'].encode("utf-8")
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    print(hashed)
    hashed = hashed.decode("utf-8")
    print(hashed)
    return hashed


if __name__ == '__main__':
    app.run()
