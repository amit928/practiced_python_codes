#Single Inheritance
'''class A:
    def method1(self):
        print("This is class A and method1 .") 
class B(A):
    def method2(self):
        print("This is class B and method2 .")
b=B()
b.method1() 
'''
#Multilevel Inheritance 

'''class A:
    def method1(self):
        print("This is class A and method1 .") 
class B(A):
    def method2(self):
        print("This is class B and method2 .")
class C(B):
    def method3(self):
        print("This is class C and method3 .")
c=C()
c.method3()
c.method2()
c.method1()
'''
#Multiple Inheritance
'''class A:
    def method1(self):
        print("This is class A and method1 .") 
class B:
    def method2(self):
        print("This is class B and method2 .")
class C(A,B):
    def method3(self):
        print("This is class C and method3 .")
c=C()
c.method1()
c.method2()
c.method3()
# print(C.__mro__)
print(C.mro())
'''
#Hierarchical Inheritance

'''class A:
    def method1(self):
        print("This is class A and method1 .") 
class B(A):
    def method2(self):
        print("This is class B and method2 .")
class C(A):
    def method3(self):
        print("This is class C and method3 .")
b=B()
c=C()
b.method1()
c.method1()
'''
#Hybrid Inheritance
class A:
    def method1(self):
        print("This is class A and method1 .") 
class B(A):
    def method2(self):
        print("This is class B and method2 .")
class C(A):
    def method3(self):
        print("This is class C and method3 .")
class D(B,C):
    def method4(self):
        print("This is class d and method4 .")
d=D()
d.method1()