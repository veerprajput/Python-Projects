import requests
from datetime import datetime

API_KEY = 'e50554948eaf31e1ced6dac9fa3734af'

Exercises = input('Tell me which exercises you did: ')

params = {
    'query': Exercises,
    'gender': 'male',
    'weight_kg': 25,
    'height_cm': 129,
    'age': 14
    
}

headers = {
    'X-APP-ID': 'e4474525',
    'X-APP-KEY': API_KEY,
}

Nutritionix = 'https://trackapi.nutritionix.com/v2/natural/exercise'
Sheety = 'https://api.sheety.co/e381dfd4958f1996e4a67649d7a62588/workouts/workouts'

response = requests.post(Nutritionix, json=params, headers=headers)
data = response.json()

print(data)

date = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime('%I:%M%p')

headers = {
    'Authorization': 'Bearer M',
}

for e in data['exercises']:
    row = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': e['name'].title(),
            'duration': e['duration_min'],
            'calories': e['nf_calories'] * 2
            
        }
    }

    response2 = requests.post(Sheety, json=row, headers=headers)
    print(response2.text)
