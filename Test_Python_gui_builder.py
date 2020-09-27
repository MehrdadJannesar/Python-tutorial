import tkinter as tk
from tkinter import ttk
from tkinter import *

# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is a function which returns the selected spin box value
def getSelectedSpinBoxValue():
	return spinBoxOne.get()



root = Tk()

# This is the section of code which creates the main window
root.geometry('543x456')
root.configure(background='#F0F8FF')
root.title('Hello, I\'m the main window')


# This is the section of code which creates a button
Button(root, text='Click Me!', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=200, y=336)


# This is the section of code which creates a spin box
spinBoxOne= Spinbox(root, from_=1, to=50, font=('arial', 12, 'normal'), bg = '#F0F8FF', width=10)
spinBoxOne.place(x=242, y=61)


root.mainloop()
