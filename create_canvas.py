# import everything from tkinter module

from tkinter import *
from tkinter import messagebox

# create a tkinter window root is a variable

root=Tk()

root.geometry("200x200")  
  
#creating a simple canvas  
c = Canvas(root,bg = "pink",height = "200")  
  
  
c.pack()  
#close the loop
root.mainloop()
