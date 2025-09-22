import datetime as dt
import smtplib

now=dt.datetime.now()
year=now.year
monty= now.month
day_of_week=now.weekday()
print(day_of_week)

date_of_birth= dt.datetime(year=2002,month=3,day=22,hour=17)
print(date_of_birth)