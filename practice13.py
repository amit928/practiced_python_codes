'''Encapsulation variable'''

# class Encap:
#     def __init__(self):
#         self.a=213
#         self._b=345
#         self.__c=123
#     def getc(self):
#         print(self.__c)
#     def setc(self,c):
#         self.__c=c

# encap=Encap()
# print(encap.a)
# print(encap._b)
# encap.setc(123)
# encap.getc()

'''Encapsulation method'''

class Encap:
    def __init__(self):
        self.a=213
        self._b=345
        self.__c=123
    def getc(self):
        print(self.__c)
    def __setc(self,c):
        self.__c=c

encap=Encap()
print(encap.a)
print(encap._b)
encap._Encap__setc(123)
encap.getc()
