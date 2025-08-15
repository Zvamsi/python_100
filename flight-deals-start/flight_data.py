import requests
from flight_search import FlightSearch
import datetime as dt

FLIGHT_ENDPOINT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

that_day=dt.datetime.now().date()
print(that_day)
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,dest_iata_code):
        self.body={
            'originLocationCode':'LON',
            'destinationLocationCode':dest_iata_code,
            'departureDate':that_day,
            'adults':1,
            'max':20,
            'currencyCode':'GBP'
        }
        flight_obj=FlightSearch()
        self.headers = {"Authorization": f"Bearer {flight_obj.api_token}"}


        flight_response=requests.get(FLIGHT_ENDPOINT,params=self.body,headers=self.headers)
        data_model=flight_response.json()['data']
        for flight_data in data_model:
            print(min(flight_data['price']['total']))

flight_search=FlightData('PAR')