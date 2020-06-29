from flask import Blueprint
from webapp.models import db
from webapp.models.site import Members
from webapp.utils.Login import AdminUtil
from webapp.utils.ORM import Utils

userUtils = Blueprint('userUtils', __name__)
adminObject = AdminUtil()
ormObject = Utils()


class UserUtils:
    def __init__(self):
        pass

    @staticmethod
    def get_user(user_details):
        result = db.session.query(Members).filter(Members.username == user_details['username']).all()
        return ormObject.result_to_dict(result)

    @staticmethod
    def all_profiles():
        result = db.session.query(Members).all()
        return ormObject.result_to_dict(result)

    @staticmethod
    def edit_profile(user_details, person_id):
        db.session.query(Members).filter(Members.id == person_id).update(
            {Members.username: user_details['username'], Members.email: user_details['email'],
             Members.first_name: user_details['first_name'],
             Members.last_name: user_details['last_name']})
        db.session.commit()
