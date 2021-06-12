class Myclass:
    '''This is my 1st class and this is a docstring of the class and it defines about the class .'''
    x=1
    def fun1(self):
        print("This is fun1 ",self.x)

obj1=Myclass()
obj1.fun1()
# print(Myclass.fun1())