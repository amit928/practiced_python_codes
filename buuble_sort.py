# a=[2,5,4,1,6,7,3]
# a.sort()
# print(a)

a=[2,5,4,1,6,7,3]
while True:
    print("Type  1  to sort in assending order and type  0  to sort in descending order .")
    x=int(input())
    if(x==1):
        for i in range(6,0,-1):
            for j in range(i):
                if(a[j]>a[j+1]):
                    temp=a[j]
                    a[j]=a[j+1]
                    a[j+1]=temp
        print(a)
    elif(x==0):
        for i in range(6,0,-1):
            for j in range(i):
                if(a[j]<a[j+1]):
                    temp=a[j]
                    a[j]=a[j+1]
                    a[j+1]=temp

        print(a)
    else:
        print("Please enter the right choice .....")
    print("If you want to stop the iteration press ' q ' : ")
    y=input()
    if(y=='q'):
        break
    else:
        pass
    
