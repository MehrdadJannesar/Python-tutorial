# Button

# widgets(master, option = value)

# import tkinter as tk
#
# root = tk.Tk()
# root.title("Conting Seconds")
# button = tk.Button(root, text = "Stop", width = 25, command = root.destroy)
# button.pack()
# root.mainloop()

# # Canvas
#
# from tkinter import *
#
# master = Tk()
#
# canvas = Canvas(master, width = 40, height = 60)
# canvas.pack()
# canvas_width = 200
# canvas_height = 20
#
# y = int(canvas_height / 2)
# canvas.create_line(0, y, canvas_width, y)
# master.mainloop()

#CheckButton


# from tkinter import *
#
# master = Tk()
#
# var1 = IntVar()
# Checkbutton(master, text = "Male", variable = var1).grid(row = 0, sticky = W)
# var2 = IntVar()
# Checkbutton(master, text = "Female", variable = var2).grid(row = 1, sticky = W)
# mainloop()

# Entry - Label

# from tkinter import *
#
# master = Tk()
# Label(master, text = "First Name :").grid(row = 0)
# Label(master, text = "Last Name :").grid(row = 1)
#
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row = 0 , column = 1)
# e2.grid(row = 1 , column = 1)
# mainloop()

# Frame
#
# from tkinter import *
#
# root = Tk()
# frame = Frame(root)
# frame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side = BOTTOM)
#
# redbutton = Button(frame, text = "Red", fg = "red")
# redbutton.pack(side = LEFT)
#
# greenbutton = Button(frame, text = "Green", fg = "green")
# greenbutton.pack(side = LEFT)
#
# bluebutton = Button(frame , text = "Blue", fg = "blue")
# bluebutton.pack(side = LEFT)
#
# blackbutton = Button(bottomFrame, text = "Black", fg = "black")
# blackbutton.pack(side = BOTTOM)
#
# root.mainloop()



#List Box

# Select Mode:
#
#     Browse
#     Single
#     Multiple
#     Extended

# from tkinter import *
#
# top = Tk()
#
# listbox = Listbox(top, selectmode = EXTENDED)
#
# listbox.insert(1, "Python")
# listbox.insert(2, "Perl")
# listbox.insert(3, "Dart")
# listbox.insert(4, "PHP")
# listbox.insert(5, "Kotlin")
# listbox.insert(6, "C#")
#
# listbox.pack()
#
# top.mainloop()

# Menu Button

# from tkinter import *
#
#
# top = Tk()
#
# menubutton = Menubutton(top, text = "Click Me!")
# menubutton.grid()
#
# menubutton.menu = Menu(menubutton, tearoff = 1)
# menubutton["menu"] = menubutton.menu
#
# cVar = IntVar()
# aVar = IntVar()
#
# menubutton.menu.add_checkbutton(label = "Contact", variable = cVar)
# menubutton.menu.add_checkbutton(label = "About", variable = aVar)
#
# menubutton.pack()
# top.mainloop()


#  Menu
#
# from tkinter import *
#
# def donothing():
#     filewin = Toplevel(root)
#     button = Button(filewin, text = "Do nothing Button")
#     button.pack()
#
#
# root = Tk()
# root.title("Test Menu")
# root.geometry("400x400")
# root.resizable(False,False)
#
# menubar = Menu(root)
#
# # File
#
# filemenu = Menu(menubar, tearoff = 0)
# filemenu.add_command(label = "New", command = donothing)
# filemenu.add_command(label = "Open", command = donothing)
# filemenu.add_command(label = "Save", command = donothing)
#
# filemenu.add_separator()
#
# filemenu.add_command(label = "Close", command = donothing)
# menubar.add_cascade(label = "File", menu = filemenu)

# Edit

# editmenu = Menu(menubar, tearoff = 0)
# editmenu.add_command(label = "Undo", command = donothing)
# editmenu.add_separator()
# editmenu.add_command(label = "Cut", command = donothing)
#
# menubar.add_cascade(label = "Edit", menu = editmenu)
#
# root.config(menu = menubar)
# root.mainloop()


# Message

# from tkinter import *
#
# main = Tk()
# ourMessage = "This is our message"
#
# messageVar = Message(main, text = ourMessage)
# messageVar.config(bg = "lightgreen")
# messageVar.pack()
# mainloop()


# RadioButton

# root = Tk()
# v = IntVar()
# Radiobutton(root, text = "Female", variable = v, value = 1).pack(anchor = W)
# Radiobutton(root, text = "Male", variable = v, value = 2).pack(anchor = W)
#
# mainloop()


# Scale

# from tkinter import *
#
# root = Tk()
#
# w = Scale(root, from_ = 0, to = 50)
# w.pack()
# w = Scale(root, from_ = 0, to = 200, orient = HORIZONTAL)
# w.pack()
# mainloop()


# Scrollbar
#
# from tkinter import *
#
# root = Tk()
# scrollbar = Scrollbar(root)
#
# scrollbar.pack(side = RIGHT, fill = Y)
# mylist = Listbox(root, yscrollcommand = scrollbar.set)
#
# for line in range(100):
#     mylist.insert(END, "This is line number " + str(line))
#
# mylist.pack(side = LEFT, fill = BOTH)
# scrollbar.config(command = mylist.yview)
# mainloop()

# Text

# from tkinter import *
#
# root = Tk()
#
# text = Text(root, height = 2, width = 30)
# text.pack()
# text.insert(END,"Python tutorial\nwith mehrdad jannesar")
# mainloop()

# Spinbox

from tkinter import *
master = Tk()
w = Spinbox(master, from_ = -10, to = 10)
w.pack()
mainloop()
