import bcrypt
from flask import *
from flask import Blueprint
from webapp.utils.Login import AdminUtil
from sqlalchemy.ext.declarative import DeclarativeMeta

admin_obj = AdminUtil()

login = Blueprint('login', __name__,
                  template_folder="./static/dist")


@login.route('/checkUser', methods=['GET', 'POST'])
def check_user():
    user_data = request.get_json()
    database_details = admin_obj.check_user(user_details=user_data['username'])
    if database_details:
        password = user_data['password'].encode("utf-8")
        hashed = database_details[0]['user_password'].encode("utf-8")
        password_check = admin_obj.check_password(password, hashed)
        if password_check:
            response = {'row': database_details, 'message': '', 'status': True}
            return response
        else:
            response = {'row': '', 'message': '', 'status': False}
            return response
    else:
        response = {'row': '', 'message': '', 'status': False}
        return response


@login.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('user_name', None)
    return True


@login.route('/registerUser', methods=['GET', 'POST'])
def register():
    data = request.get_json()
    if_user = admin_obj.if_user(data)
    if if_user is False:
        hashed_password = encrypt_password(data)
        data['password'] = hashed_password
        new_user = admin_obj.register_user(user_details=data)
        response = {'row': new_user, 'message': '', 'status': True}
        return response


def encrypt_password(data):
    password = data['password'].encode("utf-8")
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    hashed = hashed.decode("utf-8")
    return hashed
