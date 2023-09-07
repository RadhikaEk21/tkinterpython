from tkinter import *
 
 
root = Tk()
root.geometry("200x300")
root.title("main")
#create a label to dispaly the message in root
l = Label(root, text = "This is root window")
#create another window to display another content  in top
top = Toplevel()
top.geometry("180x100")
top.title("toplevel")
l2 = Label(top, text = "This is toplevel window")
 
l.pack()
l2.pack()
 
top.mainloop()
