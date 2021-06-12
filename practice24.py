# import datetime               '''Current datetime'''
# dt=datetime.datetime.now()
# print(dt)

'''Current date'''

# import datetime
# dt=datetime.date.today()
# print(dt)

'''Represent a date '''

# import datetime
# d=datetime.date(1954,3,23)
# print(d)

'''Today's year,month and date '''

# from datetime import date
# dt=date.today()
# print(dt.year)
# print(dt.month)
# print(dt.day)

'''Working with time'''
# from datetime import time
# a=time()
# print(a)
# b=time(12,34,59,238762)
# print(b)
# c=time(hour=23,minute=34,second=24)
# print(c)

'''Difference between datetime and date '''
# from datetime import datetime,date
# a=date(2021,11,13)
# b=date(2022,1,1)
# x=a-b
# print(x)
# c=datetime(2000,5,23,1,23,34)
# d=datetime(2001,12,3,10,16,17)
# print(c-d)

'''Negative timedelta object'''
# from datetime import timedelta
# t1=timedelta(seconds=33)
# t2=timedelta(seconds=45)
# print(t1-t2)
# print(abs(t1-t2))

'''Timeduration in seconds'''
# from datetime import timedelta
# t=timedelta(days=4,hours=5,minutes=23)
# print(t.total_seconds())

# import datetime
# x=datetime.strftime()
# print(x)

'''Python Datetime Module'''

# import datetime
# print(datetime.datetime.now())

# import datetime
# print(datetime.date.today())

# import datetime
# print(datetime.date(1999,4,6))

# from datetime import date
# x=date.today()
# print(x.year)
# print(x.month)
# print(x.day)

# from datetime import time
# print(time())
# print(time(12,23,43))
# print(time(hour=12,minute=45,second=23,microsecond=324234))
# print(time(12,23,43,345))

# from datetime import datetime,date
# a=datetime(2000,12,22,4,23,12)
# b=datetime(1432,1,27,3,23,42)
# x=a-b
# print(x)
# c=date(2432,4,6)
# d=date(1231,5,3)
# y=c-d
# print(y)
# print(type(x))
# print(type(y))

# from datetime import timedelta
# a=timedelta(days=45)
# b=timedelta(minutes=142134)
# print(a-b)
# c=a-b
# print(abs(c))

# from datetime import timedelta
# t=timedelta(days=5,minutes=52)
# print(t.total_seconds())