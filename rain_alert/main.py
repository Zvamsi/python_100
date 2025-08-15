import requests
import os
from twilio.rest import Client

api_key='bba7acfeadcf523f7639e0257cc7e442'
lat=12.986662
lon=77.552659

parameters={
    'lat':lat,
    'lon':lon,
    'appid':api_key,
    'cnt':5
}

os.environ["TWILIO_ACCOUNT_SID"]="AC3c5f21c7db087511a3965e8152435ced"
os.environ["TWILIO_AUTH_TOKEN"]="05cc7f55cf1a35077cdb0cb8cc7ec31e"




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
