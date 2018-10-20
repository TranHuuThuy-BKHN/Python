import datetime
import time
tday = datetime.date.today()

print('Today is ', tday)

t_delta = datetime.timedelta(days = 7)
print('Today is ', datetime.date.weekday(tday) + 2)

print('Thu', datetime.date.weekday(tday) + 2,'is', tday + t_delta)
print(tday.ctime())

date_time = datetime.datetime.today()

print(date_time)
print(float(date_time.microsecond))

now = datetime.datetime.now()
print(now)
