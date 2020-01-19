import os

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


@app.route('/checkUser', methods=['GET', 'POST'])
def login():
    data = request.get_json()
    try:
        user_details = admin_obj.check_user(user_details=data)
    except TypeError:
        print("error")
        return ""
    return user_details


if __name__ == '__main__':
    app.run()
