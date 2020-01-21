import urllib.request

import requests
from flask import Flask, request
from flask_cors import CORS
from utils.Login import AdminUtil
from models import db

admin_obj = AdminUtil()

app = Flask(__name__,
            static_folder="./static",
            template_folder="./static/dist")
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root@localhost/FreeFitness"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ApiUrl = "https://api.hippoapi.com/v3/more/json"
queryFormatString = "{0}/{1}/{2}"
YourAPIKey = '2CA872CD'


@app.route('/checkUser', methods=['GET', 'POST'])
def login():
    data = request.get_json()
    try:
        user_details = admin_obj.check_user(user_details=data)
    except TypeError:
        print("error")
        return ""
    return user_details


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
        user_details = admin_obj.register_user(user_details=data)
        if user_details:
            return data
    else:
        return {}


if __name__ == '__main__':
    app.run()
