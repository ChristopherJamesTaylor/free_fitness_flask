from operator import or_
import bcrypt
from flask import Blueprint
from webapp.models import db
from webapp.models.site import Members
from webapp.utils.ORM import Utils

adminUtils = Blueprint('adminUtils', __name__)
ormUtils = Utils()


class AdminUtil:
    def __init__(self):
        pass

    @staticmethod
    def check_user(user_details):
        result = db.session.query(Members).filter(
            or_(Members.username == user_details, Members.email == user_details)).all()
        return ormUtils.result_to_dict(result)

    @staticmethod
    def check_password(password, hashed):
        if bcrypt.checkpw(password, hashed):
            return True
        else:
            return False

    @staticmethod
    def if_user(user_details):
        result = db.session.query(Members).filter(Members.username == user_details['username']).first()
        checked_user = ormUtils.result_to_dict(result)
        if checked_user is not None:
            return checked_user
        else:
            return False

    @staticmethod
    def register_user(user_details):
        db.session.add(Members(username=user_details['username'], email=user_details['email'],
                               user_password=user_details['password'], first_name=user_details['firstName'],
                               last_name=user_details['lastName']))
        db.session.commit()
        result = db.session.query(Members).filter(Members.username == user_details['username']).first()
        response = ormUtils.result_to_dict(result)
        return response
