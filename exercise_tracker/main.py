import requests
import datetime as dt
from requests.auth import HTTPBasicAuth
import os

end_point='https://trackapi.nutritionix.com/v2/natural/exercise'
headers={
   'x-app-id': os.environ.get('x-app-id'),
    'x-app-key':os.environ.get('x-app-key')
}
print(os.environ.get('x-app-id'))
print(os.environ.get('x-app-key'))
params={
    'query':input("Enter what have you done ..?")
}

today=dt.datetime.now().strftime('%d/%m/%Y')
today_time=dt.datetime.now().time().strftime('%H:%M:%S')

# GET USER QUERY TO MAKE A REQUEST
response=requests.post(end_point,headers=headers,json=params)
response.raise_for_status()
data=response.json()
exercises=data['exercises']

# GET ALL DETAILS FROM EXCEL SHEET
get_details='https://api.sheety.co/0464ebb1991f9d3edb5615fce24c07dc/myWorkouts/workouts'

# details_response=requests.get(get_details)
# print(details_response.json())

# POST A EXERCISE
post_details='https://api.sheety.co/0464ebb1991f9d3edb5615fce24c07dc/myWorkouts/workouts'

for ex in exercises:
    post_params={
        'workout':{
        'date':today,
        'time':today_time,
        'exercise':ex['name'].title(),
        'duration':f'{round(ex['duration_min'],0)} mins',
        "calories":ex['nf_calories']
        }
    }

    post_response=requests.post(post_details,json=post_params,auth=HTTPBasicAuth(os.environ['username'], os.environ['password']))
    print(post_response.text)