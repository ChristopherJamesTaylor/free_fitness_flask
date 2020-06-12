import requests
from flask import *
from flask import Blueprint
from webapp.utils.nutrition import NutritionUtils

nutrition = Blueprint('nutrition', __name__,
                      template_folder="./static/dist")

nutritionObject = NutritionUtils()


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
    if plan is not {}:
        print("plan exists")

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


def get_recipe_plan(meals, meal_id):
    url = "https://api.spoonacular.com/recipes/" + meal_id + "/information?apiKey=3a07469279f3438bb054203338126b62" \
                                                             "&includeNutrition=false"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


@nutrition.route('/saveNutritionPlan', methods=['GET', 'POST'])
def save_plan():
    data = request.get_json()
    plan_exist = nutritionObject.does_plan_exist(data['personID'])
    if plan_exist == {}:
        nutritionObject.save_plan(data)
        plan = nutritionObject.does_plan_exist(data['personID'])
        response = {'data': plan, 'message': '', 'success': True}
        return response
    else:
        response = {'data': {}, 'message': '', 'success': True}
        return response


