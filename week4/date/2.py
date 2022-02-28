#Write a Python program to print yesterday, today, tomorrow.
from datetime import date,timedelta
print(date.today()-timedelta(1))
print(date.today())
print(date.today()+timedelta(1))


