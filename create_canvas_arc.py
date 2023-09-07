# import everything from tkinter module

from tkinter import *

# create a tkinter window root is a variable

root=Tk()

root.geometry("200x200")  
  
#creating a simple canvas  
c = Canvas(root,bg = "pink",height = "200")
arc=c.create_arc((5,10,150,200),start = 0,extent = 150, fill= "white")  
  
  
c.pack()  
#close the loop
root.mainloop()
