import matplotlib.pyplot as plt
x1=[1,2,3,4,4,5,6,7,8,9,4,3,2,1,9]
y1=[4,3,2,1,4,6,6,7,8,9,7,5,4,3,2]
x2=[1,2,3,4,4,5,6,7,8,9,4,3,2,1,9]
y2=[4,3,2,1,4,6,6,7,8,9,7,5,4,3,2]
x3=[1,2,3,4]
y3=[20,14,35,67]
plt.subplot(1,4,1)
plt.plot(x1,y1)
plt.title("Line Graph")
plt.subplot(1,4,2)
plt.scatter(x2,y2)
plt.title("Scatter graph")
plt.subplot(1,4,3)
plt.bar(x3,y3)
plt.title("Bar graph")
plt.subplot(1,4,4)
labels='mobile','computer','laptop','television'
sales=[4,3,2,6]
colors=['yellow','black','blue','red']
plt.pie(sales,labels=labels,colors=colors)
plt.title("Pie chart")
plt.show()