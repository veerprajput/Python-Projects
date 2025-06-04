import requests
import datetime

TOKEN = 'abcdefghijklmnopqrstuvwxyz'
USERNAME = 'wishtoinvest'

pendpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': 'abcdefghijklmnopqrstuvwxyz',
    'username': 'wishtoinvest',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=endpoint, json=user_params)
# print(response.status_code)

gendpoint = f'{pendpoint}/{USERNAME}/graphs'

graph_config = {
    'id': 'marioodyssey',
    'name': 'Coding Graph',
    'unit': 'Minutes',
    'type': 'float',
    'color': 'momiji'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=gendpoint, json=graph_config, headers=headers)
# print(response.text)

pcendpoint = f'{pendpoint}/{USERNAME}/graphs/marioodyssey'

today = datetime.datetime.now()

pixel_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '59',
}

response = requests.post(url=pcendpoint, json=pixel_data, headers=headers)
print(response.text)
