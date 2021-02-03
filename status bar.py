from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Frame gui")
root.geometry('300x300')

frame=LabelFrame(root,text="Welcome!",bg="yellow",padx=20,pady=30)
frame.pack(padx=10, pady=10)

btn=Button(frame,text="this is a button",bg="crimson")
btn.grid(row=0,column=0,padx=5,pady=5)

btn1=Button(frame,text="this is a button1",bg="red")
btn1.grid(row=1,column=0,padx=5,pady=5)



root.mainloop()