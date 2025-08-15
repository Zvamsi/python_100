##################### Normal Starting Project ######################

import datetime as dt
import smtplib
from email.message import EmailMessage
import pandas
import random
from email.mime.text import MIMEText

details={}
# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

now=dt.datetime.now()
now_day=now.day
# print(now_day)
now_month=now.month
# print(now_month)
today=(now_month,now_day)


# HINT 2: Use pandas to read the birthdays.csv

data=pandas.read_csv('birthdays.csv')
# print(data)

dict1=data.to_dict(orient='records')
# print(dict1)

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

birthday_dict={(item['month'],item['day']):item.items() for item in dict1}
# print(birthday_dict)

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

if today in birthday_dict:
    details=dict(birthday_dict.get(today))
#     print(details)

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

filepath=f'letter_templates/letter_{random.randint(1,18)}.txt'
with open(filepath, "r", encoding="utf-8") as file:
    wish_template=file.read()
#     # print(wish_template)
    wishes=wish_template.replace('[NAME]',details['name'])
#     print(wishes)

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

my_email='testpython970@gmail.com'
password='xmvgltguxmoimcrx'

msg = EmailMessage()
msg.set_content(wishes)
msg['Subject'] = "🎂 A Birthday Wish Just for You!"
msg['From'] = my_email
msg['To'] = details['email']

with smtplib.SMTP('smtp.gmail.com',587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.send_message(msg)
    # connection.sendmail(from_addr=my_email,to_addrs='jkv5644@gmail.com',msg=f'Subject:Surprise...\n\n{encoded_wish.as_string()}')
