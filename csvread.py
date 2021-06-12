import csv
f=open('amitzqxcsv.csv','r')
read=csv.reader(f)
for row in read:
    print(row)