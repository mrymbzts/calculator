#first need to import tkinter library
import tkinter as tk #tk is a common alias for tkinter 
from tkinter import *

def addition(): 
    num1= int(box1.get()) #we get the value from box1 and convert it to int
    num2= int(box2.get()) #we get the value from box2 and convert it to int
    result = num1 + num2
    label.config(text=f"result: {result}")#the label is updated with the result by using config function

def subtraction():
    num1= int(box1.get()) 
    num2= int(box2.get())
    result = num1 - num2
    label.config(text=f"result: {result}")

def multiplication():
    num1= int(box1.get()) 
    num2= int(box2.get())
    result = num1 * num2
    label.config(text=f"result: {result}")

def division():
    num1= int(box1.get()) 
    num2= int(box2.get())
    if num2 != 0:
        result = num1 / num2
        label.config(text=f"result: {result}")
    else:
        label.config(text="Error: you cannot divide by zero. Please enter a non-zero number in the second box.")

#firstly we need a main window
window = tk.Tk() 
window.geometry("400x300") #we set the size of the window
window.title("calculator")#we set the title of the window for user to understand what it is



#we need two entry classes to get two numbers from the user. 
tag1 = tk.Label(window, text="Please enter a number")# we explain what to do with this box
box1 = tk.Entry(window, width= 10)# we set the width of the entry box
tag2 = tk.Label(window, text="Please enter another number")
box2 = tk.Entry(window, width= 20)
#wrote 'window' in the parenthesis to show that it is in the window what we named before


#lets create a button to do the operation and write a function for command(the function is at the top of the code)
button_add= tk.Button(window, text="add", command=addition)
label = tk.Label(window, text="result:")

button_sub = tk.Button(window, text="subtract", command=subtraction)
label = tk.Label(window, text="result:")

button_mul = tk.Button(window, text="multiply", command=multiplication)
label= tk.Label(window, text="result:")

button_div = tk.Button(window, text="divide", command=division)
label = tk.Label(window, text="result:")


#we use pack() method to show them
tag1.pack()
box1.pack(pady=5)#we use 'pady' to add space between the widgets
tag2.pack()
box2.pack(pady=5)
button_add.pack()
button_sub.pack()
button_mul.pack()
button_div.pack()
label.pack()


window.mainloop() #if we don't use this line, the window will be closed immediately after running the code. 
#we want to keep it open until we close it manually.

