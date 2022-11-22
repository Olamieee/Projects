from ast import Num, Return
from cProfile import label
from cgitb import enable, text
from distutils import command
from sqlite3 import PARSE_DECLTYPES
from tkinter import *
from tkinter import messagebox
from turtle import width

root = Tk()

Label(root, text= "madlib")
#creating a label
# #mylabekl = Label(root, text= 'heo world')
#ylabekl.grid(row=1, column=1)4

#treating a button and also interacting using botton

#def myclick():
 #   label1 = Label(root, text='i clicked').pack()

#mybutton = Button(root, text="hi", command=myclick(),  padx=10, pady=13).pack()

#how to create input fields using tkinter
'''e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name")
def result():
    label1 = Label(root, text=('hello ' + e.get())).pack()
    

mybuttuon = Button(root, text= 'what is your name',  command=result, fg= 'green', bg='red').pack()'''

#creating a calculator using tkinter
root.title('Simple Calculator')

e = Entry(root,  width=50,  borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
def button_click(number):
    #e.delete(0, END)
    current= e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def button_clear():
    e.delete(0, END)
def button_add():
    first_number =e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0, END)
    
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))
    
#define functions
button_1 = Button(root, text= '1', padx=40, pady=20, command= lambda: button_click(1))
button_2 = Button(root, text= '2', padx=40, pady=20, command= lambda: button_click(2))
button_3 = Button(root, text= '3', padx=40, pady=20, command= lambda: button_click(3))
button_4 = Button(root, text= '4', padx=40, pady=20, command= lambda: button_click(4))
button_5 = Button(root, text= '5', padx=40, pady=20, command= lambda: button_click(5))
button_6=  Button(root, text= '6', padx=40, pady=20, command= lambda : button_click(6))
button_7 = Button(root, text= '7', padx=40, pady=20, command= lambda: button_click(7))
button_8 = Button(root, text= '8', padx=40, pady=20, command= lambda: button_click(8))
button_9 = Button(root, text= '9', padx=40, pady=20, command= lambda : button_click(9))
button_0 = Button(root, text= '0', padx=40, pady=20, command= lambda: button_click(0))
button_add= Button(root, text= '+', padx=40, pady=20, command= button_add)
button_equal= Button(root, text= '=', padx=80, pady=20, command= button_equal)
button_clear= Button(root, text= 'clear', padx= 80, pady=20, command= button_clear)
#put the buttons on the screen 
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=3)
button_add.grid(row=5,column=0)
button_equal.grid(row=5, column=1, columnspan=3)
#def calc():
 #   label1= Label(root, text)


#creating a messagebox
#showinfo, shhowwarning, showerror, askquestion, askokcancel, askyesorno
"""def popup():
    resonse = messagebox.askokcancel("hello world", 'welcome')
    Label(root, text=resonse).pack()
    #using ask or no , 0 rep No and 1 rep Yes..... using askquestion, 'yes' is Yes and 'NO' IS No.......
    #if resonse == 1:
        #Label(root, text='You Clicked Yes!').pack()
    #else:
        #Label(root, text='You Clicked No!').pack()
    

Button(root, text= " hello", command= popup, bg= "green",).place(x=40, y=300)"""


root.mainloop()
