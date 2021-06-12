''' How Strp() time works ? '''
from datetime import datetime
t='09 January,2021 12:25'
print(datetime.strptime(t,"%d %B,%Y %H:%M"))