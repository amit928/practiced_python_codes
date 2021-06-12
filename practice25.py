''' How Strftime() time works ? '''

from datetime import datetime
t=datetime.now()
# print("Today's weekday name : ",t.strftime('%a'))
# print("Today's weekday full name : ",t.strftime("%A"))
# print("Today's weekday number : ",t.strftime("%w"))
# print("Today's day number of the month : ",t.strftime("%d"))
# print("Today's month name : ",t.strftime("%b"))
# print("Today's month full name : ",t.strftime("%B"))
# print("Today's number of the month : ",t.strftime("%m"))
print("Today's number number of the month without century and zeropadded : ",t.strftime("%y"))
print("Today's number number of the month with century and zeropadded : ",t.strftime("%Y"))
print("Hour with zeropadded (24 hour) : ",t.strftime("%H"))
print("Hour with zeropadded (12 hour) : ",t.strftime("%I"))
print("Minute with zeropadded : ",t.strftime("%M"))
print("Second with zeropadded : ",t.strftime("%S"))
print("Microsecond with zeropadded : ",t.strftime("%f"))
print("AM/PM : ",t.strftime("%p"))
print("Appropreat datetime : ",t.strftime("%c"))
print("Appropreat date : ",t.strftime("%x"))
print("Appropreat time : ",t.strftime("%X"))
print("A litteral % character : ",t.strftime("%%"))

