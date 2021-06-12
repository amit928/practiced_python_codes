# '''Use of tkinter '''
# from tkinter import*
# # import tkinter
# w=Tk(className='Calculator')      #Title of the window
# # w=Tk()
# w.geometry('800x400')         #Size of the window
# w.title('New Calculator')      #title of the window

# # w.minsize(500,100)          #Fixed size of the window
# # w.maxsize(1000,800)

# lable=Label(text='My self Amit Kumar Mallick .\nI am an Engineer ',bg='blue',fg='white',padx=100,pady=100,font=19,borderwidth=20,relief='sunken')        #If you want to write something in window
# lable.pack(anchor=NE,side=TOP,fill=X,padx=120,pady=234)

# w.mainloop()







# from tkinter import *
# w=Tk()
# w.geometry('400x500')
# w2=Frame(w,bg='grey',borderwidth=5,padx=300)
# w2.pack(side=TOP)
# l2=Label(w2,text='project Tkinter 2',bg='yellow',fg='red')
# l2.pack()
# w1=Frame(w,bg='black',borderwidth=10)
# w1.pack(side=LEFT)
# l=Label(w1,text="Project Tkinter",font=(10),bg='blue',fg='yellow')
# l.pack()
# w.mainloop()





# from tkinter import *
# w=Tk()
# w.geometry('500x400')
# f1=Frame(w,borderwidth=5,bg='gray',relief='sunken',padx=10)
# f1.pack(anchor=NW)
# def sir():
#     print('Hey Amit Sir')
# def mam():
#     print('Hello Rachita Mam')
# b1=Button(f1,text='Amit',padx=10,font=('italic',20),command=sir)
# b1.pack(side=LEFT)
# b2=Button(f1,text='Rachita',padx=10,font=('bold',20),command=mam)
# b2.pack(side=LEFT)
# b3=Button(f1,text=3,padx=10,font=('bold',20))
# b3.pack(side=LEFT)
# b4=Button(f1,text=4,padx=10,font=('bold',20))
# b4.pack(side=LEFT)
# # w1=Label(w0,text='My name is Amit Kumar Mallick',font=('bold',20),bg='black',fg='white')
# # w1.pack()
# w.mainloop()


from tkinter import *
w=Tk()
def getvals():
    print(Name.get())
    print(Nonveg.get())
    print(Veg.get())
w.geometry('644x344')
Label(w,text='WELCOME',font='comicsansms,50,bold',pady=20).grid(row=0,column=3)
Label(w,text='Name',font='comicsansms,30').grid(row=1,column=0)
Name=StringVar()
Veg=BooleanVar()
Nonveg=BooleanVar()
Entry(w,textvariable=Name).grid(row=1,column=1)
Checkbutton(w,text="NonVeg",font=30,textvariable=Nonveg).grid(row=2,column=0)
Checkbutton(w,text="Veg",textvariable=Veg,font=30).grid(row=2,column=1)
Button(w,text='Submit',borderwidth=5,bg='white',fg='black',command=getvals).grid(row=3,column=3)
w.mainloop()