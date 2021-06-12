'''Single line'''

# import matplotlib.pyplot as plt
# a=[1,3]
# b=[2,7]
# plt.plot(a,b)
# plt.show()

'''Multiple lines'''

# import matplotlib.pyplot as plt
# x1=[1,3,5,7]
# y1=[2,6,10,14]
# x2=[2,4,6,8]
# y2=[3,5,7,9]
# plt.plot(x1,y1)
# plt.plot(x2,y2)
# plt.xlabel('X axis')
# plt.ylabel('Y axis')
# plt.title('My New Graph')
# plt.show()

'''Subplots'''

x1=[4,5,6]
y1=[2,6,3]
x2=[5,7,6]
y2=[8,9,5]
import matplotlib.pyplot as plt
plt.subplot(1,2,1)
plt.plot(x1,y1,'r')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('1st subplot')
plt.grid(True)
plt.subplot(2,2,2)
plt.plot(x2,y2,'b')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('2nd subplot')
plt.grid(True)
plt.show()