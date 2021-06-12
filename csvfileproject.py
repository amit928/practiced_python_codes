import csv
file=open('amitzqxcsv.csv','r')
read=csv.reader(file)
x=input("Enter your marks : ")
for row in read:
    if(row[3]==x):
        print(row)
file.close()
    