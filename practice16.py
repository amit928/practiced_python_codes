# file1=open('amit.txt')
# print('file name : ',file1.name)
# print('file mode : ',file1.mode)
# print('Is file readable : ',file1.readable())
# print('Is file closed : ',file1.closed)
# file1.close()
# print('Is file closed : ',file1.closed)

# f=open('practice16.txt')
# print(f.readlines(1))
# f.close()

# f=open('practice17.txt','r')
# # f.write("\nKumar ")
# x=f.readlines()
# f=open('practice17.txt','w')
# for line in x:
#     if line!="":
#         f.write(line)
# f.close()

# f=open('practice17.txt','r')
# print(f.readlines())

'''To delete a sentence from a file .'''

# with open("mark2.txt",'w') as f2:
#     f2.write("My name is Amit Kumar Mallick .\n")
#     f2.write("What's Your Name ?\n")
# f2.close()

# with open("mark2.txt",'r') as f2:
#     data=f2.readlines()
# print(data)
# # f2.close()

# with open("mark2.txt",'a') as f2:
#     f2.write("My name is Rachita Priyadarseeni Rout .")
# f2.close()

# with open("mark2.txt",'r') as f2:
#     x=f2.readlines()
# with open("mark2.txt",'w') as f2:
#     for line in x:
#         if line!="What's Your Name ?\n":
#             f2.write(line)
# f2.close()

# with open("mark2.txt",'r') as f2:
#     print(f2.read())
# f2.close()