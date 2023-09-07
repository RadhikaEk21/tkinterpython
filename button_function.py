# import everything from tkinter module

from tkinter import *
from tkinter import messagebox

# create a tkinter window root is a variable

root=Tk()

#create a function

def msg():
    messagebox.showinfo("hi" ,"tkinter")
    


# create a button
#click the button to close(terminate)the tkinter window
btn1 = Button(root, text ="Button 1", command = msg,activeforeground = "red",activebackground = "pink")
btn1.pack(pady = 10)
#close the loop
root.mainloop()
