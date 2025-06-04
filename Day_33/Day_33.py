import requests
from datetime import datetime

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()

# longitude = response.json()['iss_position']['longitude']
# latitude = response.json()['iss_position']['latitude']


# print(longitude, latitude)

# MY_LAT = 38.55711921655077
# MY_LONG = -121.23578641546726

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
}


response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

time_now = datetime.now()

print(sunrise.split('T')[1].split(':')[0])
print(sunset.split('T')[1].split(':')[0])
print(time_now.hour)

