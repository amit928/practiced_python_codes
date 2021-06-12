# import matplotlib.pyplot as plt
# x=[1,2,3,4]
# y=[10,12,25,50]
# plt.bar(x,y,color='black')
# plt.show()

# import matplotlib.pyplot as plt
# x=[10,12,25,50]
# y=[1,2,3,4]
# y1=('boys','girls','men','women')
# plt.barh(y,x,color='black')
# plt.yticks(y,y1)
# plt.show()

import matplotlib.pyplot as plt
x1=[1,3,5,7]
y1=[12,34,45,56]
x2=[2,4,6,8]
y2=[13,32,54,76]
x0=('pen','note','book','pencil')
x00=('phone','laptop','computer','led')
plt.subplot(1,2,1)
plt.bar(x1,y1,color='red')
plt.xticks(x1,x0)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Graph1')
plt.subplot(1,2,2)
plt.bar(x2,y2,color='green')
plt.xticks(x2,x00)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Graph2')
plt.show()
