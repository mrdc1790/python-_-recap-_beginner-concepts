from datetime import date
import datetime

mytime = datetime.time(2, 20)
print(mytime)
print(type(mytime))
today = datetime.date.today()
print(today)
print(today.ctime())

date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)

result = date1 - date2
print(type(result))
print(result.days)