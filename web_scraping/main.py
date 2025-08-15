import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response=requests.get(URL)
data=response.text

soup=BeautifulSoup(data,'html.parser')
# print(soup)

movies=soup.find_all(name='h3',class_='title')
movie_title=[]
for movie in movies:
    movie_title.append(movie.get_text())
movie_title.reverse()


with open('movies.txt','w',encoding='utf-8') as file:
    for movie in movie_title:
        file.write(f'{movie}\n')
