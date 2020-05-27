import requests
from flask import *
from flask import Blueprint

nutrition = Blueprint('nutrition', __name__,
                      template_folder="./static/dist")


@nutrition.route('/getMealPlan', methods=['GET', 'POST'])
def get_meal_plan():
    data = request.get_json()
    url = "https://api.spoonacular.com/mealplanner/generate?apiKey=3a07469279f3438bb054203338126b62"
    payload = {}
    if data['diet'] == "standard":
        querystring = {"timeFrame": "week", "targetCalories": data['calories'], "exclude": data['allergies']}
    elif data['diet'] == 'standard' and data['allergies'] == 'none':
        querystring = {"timeFrame": "week", "targetCalories": data['calories']}
    elif data['allergies'] == 'none':
        querystring = {"timeFrame": "week", "targetCalories": data['calories'], "diet": data['diet']}
    else:
        querystring = {"timeFrame": "week", "targetCalories": data['calories'], "diet": data['diet'],
                       "exclude": data['allergies']}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload, params=querystring)
    plan = response.json()
    meals = {
        'breakfast': '',
        'lunch': '',
        'dinner': '',
        "protein": '',
        "carbohydrates": '',
        "fat": '',
        "day": '',
        "cookInMinutes": []
    }
    meal_plan = make_meal_plan(plan, meals)
    return jsonify(meal_plan)


def make_meal_plan(response, meals):
    plan = []
    days = response['week'].keys()
    for i in days:
        meals['day'] = i
        meals['breakfast'] = response['week'][i]['meals'][0]['title']
        meals['lunch'] = response['week'][i]['meals'][1]['title']
        meals['dinner'] = response['week'][i]['meals'][2]['title']
        for j in response['week'][i]['meals']:
            meals['cookInMinutes'].append(j['readyInMinutes'])
        meals['protein'] = response['week'][i]['nutrients']['protein']
        meals['carbohydrates'] = response['week'][i]['nutrients']['carbohydrates']
        meals['fat'] = response['week'][i]['nutrients']['fat']
        plan.append(meals)
        meals = {
            'breakfast': '',
            'lunch': '',
            'dinner': '',
            "protein": '',
            "carbohydrates": '',
            "fat": '',
            "day": '',
            "cookInMinutes": []
        }
    return plan
