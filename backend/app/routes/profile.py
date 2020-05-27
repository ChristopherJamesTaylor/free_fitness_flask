import requests
from flask import *
from flask import Blueprint
from app.utils.User import UserUtils

user_object = UserUtils()

profile = Blueprint('profile', __name__,
                    template_folder="./static/dist")


@profile.route('/allProfiles', methods=['GET', 'POST'])
def all_profiles():
    return jsonify(user_object.all_profiles())


@profile.route('/editProfile', methods=['GET', 'POST'])
def edit_profile():
    user_details = request.get_json()
    person_id = request.get_json()
    user_object.edit_profile(user_details['profile'][0],
                             person_id['id'])
    return jsonify(user_object.get_user(user_details['profile'][0]))


@profile.route('/getUser', methods=['GET', 'POST'])
def get_user():
    user_details = request.get_json()
    return jsonify(user_object.get_user(user_details))
