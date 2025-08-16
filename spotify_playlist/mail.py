import requests
from bs4 import BeautifulSoup

input_date='2025-08-09'
# input_date=input('what year you would like to travel to in YYYY-MM-DD format...?')
url=f'https://www.billboard.com/charts/hot-100/{input_date}/'

response=requests.get(url)
data=response.text
# print(data)

soup=BeautifulSoup(data,'html.parser')


divs=soup.select('.chart-results-list .o-chart-results-list-row-container')


song_titles_list=[div.select('.c-title')[0].get_text() for div in divs]
song_titles=[item.strip() for item in song_titles_list]

print(song_titles)

# song_title=[item.get_text().strip() for item in song_titles]
# print(song_title)