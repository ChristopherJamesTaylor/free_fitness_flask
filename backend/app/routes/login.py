import bcrypt
from flask import *
from flask import Blueprint
from app.utils.Login import AdminUtil

admin_obj = AdminUtil()

login = Blueprint('login', __name__,
                  template_folder="./static/dist")


@login.route('/checkUser', methods=['GET', 'POST'])
def check_user():
    print('check user')
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


@login.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('user_name', None)
    return True


@login.route('/registerUser', methods=['GET', 'POST'])
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
