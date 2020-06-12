from flask import *
from flask_cors import CORS
from webapp.models import db
from webapp.routes.fitness import fitness
from webapp.routes.nutrition import nutrition
from webapp.routes.profile import profile
from webapp.routes.gym_finder import gym
from webapp.routes.macros import macros
from webapp.routes.login import login

app = Flask(__name__,
            static_folder="./static",
            template_folder="./static/dist")

app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://freefitnessflask:chris@db/FreeFitness"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(login)
app.register_blueprint(fitness)
app.register_blueprint(nutrition)
app.register_blueprint(profile)
app.register_blueprint(gym)
app.register_blueprint(macros)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
