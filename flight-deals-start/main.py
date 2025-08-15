#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time

from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData


# Taking the data from excel data.
data_obj=DataManager()
sheet_data=data_obj.get_destination()
flight_obj=FlightSearch()

for row in sheet_data:
    print(row['iataCode'])
    flight_data_obj=FlightData(row['iataCode']
    # row['iataCode']=flight_obj.get_destination_code(row['city'].upper())
    # time.sleep(2)

# print(f'sheet data {sheet_data}')

# TO UPDATE THE IATA CODES IN EXCEL.
# data_obj.destination_data=sheet_data
# data_obj.update_destination_data()



