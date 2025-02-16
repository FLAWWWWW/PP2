from datetime import date, timedelta, datetime

# TASK 1
'''
x = date.today() - timedelta(5)

print('Current Date :', date.today())

print('5 days before Current Date :', x) 
'''

# TASK 2
'''
yesterday = date.today() - timedelta(1)
tomorrow = date.today() + timedelta(1)

print(f"Yesterday: {yesterday} Today: {date.today()} Tomorrow: {tomorrow}" )
'''

# TASK 3
'''
x = datetime.now()
print(x.strftime("%f"))
'''

# TASK 4
now = datetime.now()

yesterday = now - timedelta(days=1)

difference_in_seconds = (now - yesterday).total_seconds()

print(f"Difference in seconds: {difference_in_seconds}")