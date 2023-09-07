from tkinter import *   
from tkinter import messagebox  
top = Tk()  
  
top.geometry("200x200")  
  
checkvar1 = IntVar()  
     
chkbtn1 = Checkbutton(top, text = "C", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 10)    
  
chkbtn1.pack()  


top.mainloop()  
