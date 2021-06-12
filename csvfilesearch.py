import csv
f=open('amitzqxcsv.csv','r')
read=csv.reader(f)
x=input("Enter your value : ")
for row in read:
    if(x==row[0]):
        print(row)
f.close()