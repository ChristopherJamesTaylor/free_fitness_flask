import requests
from flask import *
from flask import Blueprint

gym = Blueprint('gym', __name__,
                template_folder="./static/dist")


@gym.route('/getGyms', methods=['GET', 'POST'])
def get_gyms():
    data = request.get_json()
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(data['lat']) + ',' + \
          str(data['long']) + "&radius=20000&type=gym&key=AIzaSyB6bC_OukDUo3yP4mV6DF9mZ5qFvOmKH-0"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()
