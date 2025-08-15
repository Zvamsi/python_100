import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth

SHEETY_URL = 'https://api.sheety.co/0464ebb1991f9d3edb5615fce24c07dc/flightDeals/prices'


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.headers = {
            "Authorization": "Basic dmFtc2hpOnZhbXNoaUAxMjM="
        }

        # self.response=requests.get(SHEETY_URL,headers=self.headers)
        # print(self.response.json())
        # self.data1=self.response.json()['prices']


    def get_destination(self):
        response1=requests.get(SHEETY_URL,headers=self.headers)
        data2=response1.json()
        print(data2)
        self.destination_data=data2['prices']
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data={
                'price':{
                'iataCode':city['iataCode']
                }
            }
            update_response=requests.put(f'{SHEETY_URL}/{city['id']}',headers=self.headers,json=new_data)
            print(update_response.text)

data=DataManager()

