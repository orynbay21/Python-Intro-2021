from datetime import date, timedelta
x = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',x)
'''
date.today()
print elements in such a format:
year-month-day
"%d/%m/%Y"

timedelta(x) makes it easy to subtract
'''