'''Time Module'''

# import time
# t=time.time()
# print("Seconds since epoch : ",t)

'''Time.ctime()'''
# import time
# t=time.time()
# print('Local time =',time.ctime(t))

'''Use of strptime() and ctime()'''

# import time
# from datetime import datetime
# t1=time.time()
# t2=time.ctime(t1)
# print(t2)
# print(datetime.strptime(t2,"%a %b %d %H:%M:%S %Y"))

# import time
# t1=time.time()
# t2=time.localtime(t1)
# print(t2)
# print("Year=",t2.tm_year)
# print("Month=",t2.tm_mon)
# print("Day=",t2.tm_mday)
# print("Hour=",t2.tm_hour)
# print("Minute=",t2.tm_min)
# print("Second=",t2.tm_sec)
# print("Weekday=",t2.tm_wday)

'''time.sleep()'''

# import time
# print("It is printing immediately")
# time.sleep(4)
# print("It will print after 4 sec .")

'''pytZ module'''

# from datetime import datetime
# import pytz

# t=datetime.now()
# print("Local time =",t.strftime("%m/%d/%Y %H:%M:%S %p"))

# NY=pytz.timezone('America/New_york')
# t2=datetime.now(NY)
# print("NY =",t2.strftime("%m/%d/%Y %I:%M:%S %p"))

# London=pytz.timezone('Europe/London')
# t3=datetime.now(London)
# print("London =",t3.strftime("%m/%d/%Y %H:%M:%S %p"))

import pandas
# import datetime