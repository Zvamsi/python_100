import requests
import datetime as dt

day_=dt.datetime.now().day
month_=dt.datetime.now().month
if month_<10:
    month_='0'+str(month_)
if day_<10:
    day_='0'+str(day_)
year_=dt.datetime.now().year

today_str=f'{year_}{month_}{day_}'
today=dt.datetime.now()

TOKEN='---YOUR TOKEN---'
USER_NAME='-----YOUR USER NAME-----'
GRAPH="graph1"

create_user_url='https://pixe.la/v1/users'
user_params={
    'token':TOKEN,
    'username':USER_NAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

# response=requests.post(create_user_url,json=user_params)
# print(response.text)

create_graph_url=f'{create_user_url}/{USER_NAME}/graphs'
graph_params={
    'id':GRAPH,
    'name':'Meditation Time',
    'unit':'minute',
    'type':'int',
    'color':"shibafu",
}

headers={
    "X-USER-TOKEN":TOKEN
}

# graph_response=requests.post(create_graph_url,json=graph_params,headers=headers)
# print(graph_response.text)


pixel_url=f'{create_graph_url}/{GRAPH}'

pixel_params={
    'date':today.strftime('%Y%m%d'),
    'quantity':input("How many minutes did you meditate today ?."),
}

# pixel_response=requests.post(pixel_url,json=pixel_params,headers=headers)
# print(pixel_response.text)

update_pixel_url=f'{pixel_url}/{today.strftime("%Y%m%d")}'
update_params={
    'quantity':'1'
}

# update_pixel_response=requests.put(update_pixel_url,headers=headers,json=update_params)
# print(update_pixel_response.text)

delete_pixel=requests.delete(update_pixel_url,headers=headers)
print(delete_pixel.text)