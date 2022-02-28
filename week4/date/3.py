#Write a Python program to drop microseconds from datetime
from datetime import datetime
now=datetime.now()
#print(now) 2022-02-28 20:15:42.552606
print(now.strftime('%d/%m/%Y %H:%M:%S')) #28/02/2022 20:15:42