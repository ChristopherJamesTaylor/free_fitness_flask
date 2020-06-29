import requests
from flask import *
from flask import Blueprint

macros = Blueprint('macros', __name__,
                   template_folder="./static/dist")


@macros.route('/getMacros', methods=['GET', 'POST'])
def get_macros():
    data = request.get_json()
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
            # Mifflin St Jeor
            bmr = (10 * float(data['weight'])) + (6.25 * float(data['height'])) - (5 * float(data['age'])) + 5
            # Harris - Benedict(Revised)
            # bmr = 65 + (13.7 * float(data['weight'])) + (5 * float(data['height'])) - (6.8 * float(data['age']))
        else:
            # Mifflin St Jeor
            bmr = (10 * float(data['weight'])) + (6.25 * float(data['height'])) - (5 * float(data['age'])) - 161
            # Harris - Benedict(Revised)
            # bmr = 655 + (13.7 * float(data['weight'])) + (1.8 * float(data['height'])) - (4.7 * float(data['age']))
    elif data['unit'] == 'imperial':
        if data['sex'] == 'male':
            print(data['age'])
            bmr = ((10 * float(data['weight'])) / 0.15747) + ((6.25 * float(data['height'])) / 0.032808) - (
                        5 * float(data['age'])) + 5
            # Harris - Benedict(Revised)
            # bmr = 66 + (6.23 * float(data['weight'])) + (12.7 * float(data['height'])) - (
            #         6.8 * float(data['age']))
        else:
            bmr = ((10 * float(data['weight'])) / 0.15747) + ((6.25 * float(data['height'])) / 0.032808) - (
                        5 * float(data['age'])) - 161
            # bmr = 655.1 + (4.35 * float(data['weight'])) + (4.7 * float(data['height'])) - (
            #         4.7 * float(data['age']))

    # calculate TDEE
    if data['activity'] == 'Sedentary':
        tdee = bmr * 1.2
        print('The TDEE is:', tdee)
    #     Office worker getting little or no exercise
    elif data['activity'] == 'Slightly active':
        tdee = bmr * 1.375
        print('The TDEE is:', tdee)
    #     Office worker getting little or no exercise
    elif data['activity'] == 'Lightly Active':
        tdee = bmr * 1.425
    elif data['activity'] == 'Moderately Active':
        tdee = bmr * 1.55
    #     Construction worker or person running one hour daily
    elif data['activity'] == 'Very Active':
        tdee = bmr * 1.75
    elif data['activity'] == 'Extremely Active':
        tdee = bmr * 1.9
    #     	Agricultural worker (non mechanized) or person swimming two hours daily

    # calculate macros
    if data['goal'] == 'fatLoss':
        # 10% drop and increase in protein
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
