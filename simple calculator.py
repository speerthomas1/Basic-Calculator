#Python is object oriented
from tkinter import * #Library; GUI Toolkit for widgets & functions

root = Tk() #Root widget; In tkinter must define then set up for screen display
e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0,"Enter your name: ")

def myClick():
        varGreeting = "What's up! Welcome " + e.get()
        myLabel = Label (root, text= varGreeting)
        myLabel.pack()
myButton = Button(root, text="Enter Your Name", command=myClick, fg="#000000", bg="#FFFFFF")#1. Define (state; padx and/or pady, fg or bg(cann use color codes))
myButton.pack()#2. Display on screen

root.mainloop()