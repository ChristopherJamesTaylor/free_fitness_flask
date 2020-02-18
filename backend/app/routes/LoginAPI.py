from flask import request, Flask
from flask import Blueprint
from app.utils.Login import AdminUtil

app = Flask(__name__)
app.config.from_object(__name__)
login = Blueprint('login', __name__)
admin_obj = AdminUtil


@login.route('/checkUser', methods=['GET', 'POST'])
def login():
    print("Your data in python is: " + request.get_json())
    # data = request.get_json()
    # print(data)
    # # if needed json.dumps(data)
    # user_details = admin_obj.check_user(data)
    # return user_details
