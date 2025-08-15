from bs4 import BeautifulSoup
import requests

response=requests.get('https://news.ycombinator.com/news')
yc_soup=response.text

soup=BeautifulSoup(yc_soup,'html.parser')

articles=soup.select('.titleline')
article_links=[]
article_texts=[]
for article_ in articles:
    article=article_.select_one('a')
    article_texts.append(article.get_text())
    article_links.append(article.get('href'))
article_upvotes=[score.get_text() for score in soup.select('.score')]

votes=[]
for vote in article_upvotes:
    votes.append(int(vote.split(' ')[0]))

print(article_links)
print(article_texts)
print(votes)

max_votes=votes[0]
max_index=0
i=0
while i<len(votes):
    num=votes[i]
    if num>max_votes:
        max_votes=num
        max_index=i
    i+=1
print(max_index)
print(article_texts[max_index])
print(article_links[max_index])
print(article_upvotes[max_index])




# with open('website.html','r') as file:
#     contents=file.read()
#
# soup=BeautifulSoup(contents,'html.parser')
