import requests
import os
from twilio.rest import Client

api_key='---api key----'
lat=12.986662
lon=77.552659

parameters={
    'lat':lat,
    'lon':lon,
    'appid':api_key,
    'cnt':5
}

os.environ["TWILIO_ACCOUNT_SID"]="----YOUR API SID------"
os.environ["TWILIO_AUTH_TOKEN"]="----YOUR API AUTH-----"




account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]


response=requests.get('https://api.openweathermap.org/data/2.5/forecast',params=parameters)
response.raise_for_status()
print(response.status_code)

weather_data=response.json()
# print(weather_data)
will_rain=False
weather_list=weather_data['list']
# print(weather_list)
for item in weather_list:
    id_=item['weather'][0]['id']
    if id_<800:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's Going to rain 🌧️, Please Bring the umbrella ☔",
        from_="+14582365048",
        to="+919363071055",
    )

    print(message.status)
