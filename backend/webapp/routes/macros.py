import requests
from flask import *
from flask import Blueprint

macros = Blueprint('macros', __name__,
                   template_folder="./static/dist")


@macros.route('/getMacros', methods=['GET', 'POST'])
def get_macros():
    data = request.get_json()
    print(data)
    tdee = 0
    macros = {
        'protein': 0,
        'carbohydrates': 0,
        'fat': 0,
    }
    bmr = 0
    # calculate Basic Metabolic Rate first

    if data['unit'] == 'metric':
        if data['sex'] == 'male':
            bmr = 65 + (13.7 * float(data['weight'])) + (5 * float(data['height'])) - (6.8 * float(data['age']))
            print(bmr)
        else:
            print('Woman')
            bmr = 655 + (13.7 * float(data['weight'])) + (1.8 * float(data['height'])) - (4.7 * float(data['age']))

    elif data['unit'] == 'imperial':
        if data['sex'] == 'male':
            bmr = 66 + (6.23 * float(data['weight'])) + (12.7 * float(data['height'])) - (
                    6.8 * float(data['age']))
        else:
            print('Woman')
            bmr = 655.1 + (4.35 * float(data['weight'])) + (4.7 * float(data['height'])) - (
                    4.7 * float(data['age']))

    # calculate TDEE
    if data['activity'] == 'sedentary':
        tdee = bmr * 1.2
        print('The TDEE is:', tdee)
    #     Office worker getting little or no exercise
    elif data['activity'] == 'active':
        tdee = bmr * 1.55
    #     Construction worker or person running one hour daily
    else:
        tdee = bmr * 1.75
    #     	Agricultural worker (non mechanized) or person swimming two hours daily
    # calculate macros
    if data['goal'] == 'fatLoss':
        # 10% drop and increase in protein
        print('fat loss')
        drop = tdee * 0.1
        tdee = tdee - drop
        macros = {
            'tdee': tdee,
            'protein': (tdee * 0.3) / 4,
            'carbohydrates': (tdee * 0.5) / 4,
            'fat': (tdee * 0.2) / 9,
        }

    elif data['goal'] == 'muscleGain':
        # 10% increase and increase in protein
        print('bulk')
        gain = tdee * 0.1
        tdee = tdee + gain
        macros = {
            'tdee': tdee,
            'protein': (tdee * 0.4) / 4,
            'carbohydrates': (tdee * 0.4) / 4,
            'fat': (tdee * 0.2) / 9,
        }
    else:
        macros = {
            'tdee': tdee,
            'protein': (tdee * 0.3) / 4,
            'carbohydrates': (tdee * 0.5) / 4,
            'fat': (tdee * 0.2) / 9,
        }
    # The 95 % confidence range for men is ±213.0 kcal / day, and ±201.0 kcal / day for women.
    response = {
        'Macros': macros
    }
    return jsonify(response)
