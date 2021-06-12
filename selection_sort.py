a=[2,4,1,5,6,3]
for i in range(len(a)):
    minm=i
    for j in range(i,len(a)):
        if(a[j]<a[minm]):
            minm=j
    temp=a[i]
    a[i]=a[minm]
    a[minm]=temp
print(a)