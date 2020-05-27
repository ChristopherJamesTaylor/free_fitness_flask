from flask import *
from flask_cors import CORS
from app.models import db
from app.routes.fitness import fitness
from app.routes.nutrition import nutrition
from app.routes.profile import profile
from app.routes.gym_finder import gym
from app.routes.macros import macros
from app.routes.login import login

app = Flask(__name__,
            static_folder="./static",
            template_folder="./static/dist")

app.register_blueprint(login)
app.register_blueprint(fitness)
app.register_blueprint(nutrition)
app.register_blueprint(profile)
app.register_blueprint(gym)
app.register_blueprint(macros)


app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://freefitnessflask:chris@db/FreeFitness"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app, resources={r"/*": {"origins": "*"}})
db.init_app(app)

if __name__ == '__main__':
    app.run()
