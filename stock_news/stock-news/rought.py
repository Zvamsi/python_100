import datetime
from datetime import timedelta


yesterday=(datetime.datetime.now()-timedelta(1)).date()
before_yesterday=(datetime.datetime.now()-timedelta(2)).date()
print(yesterday)
print(before_yesterday)