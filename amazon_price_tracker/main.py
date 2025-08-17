import os
from itertools import product

from dotenv import load_dotenv,find_dotenv
from bs4 import BeautifulSoup
import requests
import smtplib
THRESHOLD=2500


 # LOADING .ENV FILE AND GETTING DATA FROM IT

dotenv_path=find_dotenv()
print(dotenv_path)

load_dotenv(dotenv_path)

send_mail=os.getenv('SEND_MAIL')
password=os.getenv('PASSWORD')
receive_mail='jkv5644@gmail.com'
print(send_mail,password)


# GET PRICE FROM AMAZON WEBSITE

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
amazon_url='https://www.amazon.in/PLANAL-Stylish-Casual-Sneaker-Shoes/dp/B0F8BPGLKF/ref=pd_ci_mcx_mh_mcx_views_0_image?psc=1'
amazon_response=requests.get(amazon_url,headers=headers)
amazon_response.raise_for_status()
data=amazon_response.text
# print(data)

soup=BeautifulSoup(data,'html.parser')
product_price=int(soup.find(id='twister-plus-price-data-price').get('value'))
product_name=soup.find(id='productTitle').get_text().strip()
print(product_name)
print(product_price)


# SEND A MAIL
if product_price<THRESHOLD:
    with smtplib.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login(user=send_mail,password=password)
        connection.sendmail(from_addr=send_mail,to_addrs=receive_mail,
                            msg=f'subject:AMAZON Price alert..!\nThe {product_name} of the product is {product_price} INR .\nAnd it is very very LOWWWWWW.\n Here\'s your Link : {amazon_url}')

