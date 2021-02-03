from tkinter import *
root=Tk()
root.title("My Calculator")


e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_get(num):
	current = e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(num))

def clear():
	e.delete(0,END)

def button_ad():
	first_number = e.get()
	global f_num 
	f_num = int(first_number)
	e.delete(0,END)

def equal():
	second_number = e.get()
	e.delete(0,END)
	e.insert(0, f_num + int(second_number))


btn1=Button(root,text="1",padx=40,pady=20,command=lambda :button_get(1))
btn2=Button(root,text="2",padx=40,pady=20,command=lambda :button_get(2))		
btn3=Button(root,text="3",padx=40,pady=20,command=lambda :button_get(3))		
btn4=Button(root,text="4",padx=40,pady=20,command=lambda :button_get(4))		
btn5=Button(root,text="5",padx=40,pady=20,command=lambda :button_get(5))		
btn6=Button(root,text="6",padx=40,pady=20,command=lambda :button_get(6))		
btn7=Button(root,text="7",padx=40,pady=20,command=lambda :button_get(7))		
btn8=Button(root,text="8",padx=40,pady=20,command=lambda :button_get(8))		
btn9=Button(root,text="9",padx=40,pady=20,command=lambda :button_get(9))
btn0=Button(root,text="0",padx=40,pady=20,command=lambda :button_get(0))
btn_add=Button(root,text="+",padx=40,pady=20,command=button_ad)
btn_clear=Button(root,text="Clear",padx=80,pady=20,command=clear)
btn_equal=Button(root,text="Equal",padx=80,pady=20,command=equal)


btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)


btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)


btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)

btn0.grid(row=4,column=0)
btn_add.grid(row=5,column=0)
btn_clear.grid(row=4,column=1,columnspan=2)
btn_equal.grid(row=5,column=1,columnspan=2)










root.mainloop()