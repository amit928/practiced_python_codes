# x=int(input("Enter a number"))
# y=int(input("Enter a number"))
# try:
#     print(x/y)
# except((ZeroDivisionError)):
#     print("Zero Division Error")





#  x=[12,34,456,67,8,9,890]
# # y=int(input("Enter the number to search ."))
# # for y in x:
# #     pass
# print(x[10])

# x=int(input("Enter a number"))
# y=int(input("Enter a number"))
# try:
#     # if(y==0):
#     #     raise ValueError("You can't enter 0 for second number .")
#     print(x/y)
# except((ZeroDivisionError,NameError)):
#     print("Zero Division Error")

# class userexception(Exception):
#     pass
# class user:
#     name=input("Enter your name : ")
#     try:
#         if name=='':
#             raise userexception
#         else:
#             print(name)
#     except((userexception)):
#         print("User Exception ...Enter your name properly .")

x=int(input("Enter a number : "))
y=int(input("Enter a number : "))
try:
    print(x/y)
    print(int("Dog"))
except((ValueError)):
    print("This is a value error .")
except((ZeroDivisionError)):
    print("This is a zerodivisionerror . ")
