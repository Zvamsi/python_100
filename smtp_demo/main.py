# import smtplib
#
my_email='testpython970@gmail.com'
password='xmvgltguxmoimcrx'
# with smtplib.SMTP('smtp.gmail.com',587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs='jkv5644@gmail.com',
#         msg='Subject:Hello\n\nThis is the body of email'
#     )









#
# import datetime as dt
#
# now =dt.datetime.now()
# print(now,type(now))
# year=now.year
# print(year,type(year))
# month=now.month
# print(month,type(month))
# day=now.day
# print(day,type(day))
# weekday=now.weekday()
# print(weekday,type(weekday))
#
#
# date_of_birth=dt.datetime(year=2003,month=9,day=13,hour=11,minute=30,second=30)
# print(date_of_birth)

import random
import smtplib
import datetime as dt

with open('quotes.txt') as file:
    data=file.readlines()
    # data=data.split('\n')
    msg=random.choice(data)
    print(msg)
    text_part,name_part=msg.split(' - ')
    # print(text_part)
    # print(name_part)

now=dt.datetime.now()
weekday=now.weekday()
if weekday==6:
    with smtplib.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs='jkv5644@gmail.com',msg=f'Subject:Sent by Vamshi don\'t mind\n\n{text_part}\n\n-{name_part}')
