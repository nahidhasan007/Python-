from tkinter import *
import tkinter.messagebox as messagebox
import mysql.connector as mysql

def insert():
	id=e_id.get()
	name=e_name.get()
	phone=e_phone.get()

	if(id=="" or name=="" or phone==""):
		messagebox.showinfo("insert status","all field are required")
	else:
		conn=pymysql.connect(host="localhost",user="root", passwd="",db="studentinfo")
		cursor=conn.cursor()
		cursor.execute("insert into student values('"+ id +"','"+ name +"','"+ phone +"')")
        ##cursor.execute("commit")
        #messagebox.showinfo("Insert status","Inserted Successfully")
        #onn.close()

root=Tk()
root.geometry("600x350")
root.title("database @ tkinter")

id=Label(root,text="Enter Id",font=('bold', 10))
id.place(x=20,y=30)

name=Label(root,text="Enter Name",font=('bold', 10))
name.place(x=20,y=60)

phone=Label(root,text="Enter phone",font=('bold', 10))
phone.place(x=20,y=90)

e_id=Entry()
e_id.place(x=150,y=30)

e_name=Entry()
e_name.place(x=150,y=60)

e_phone=Entry()
e_phone.place(x=150,y=90)

btn_insert=Button(root,text="Insert").place(x=10,y=140,command=insert)
btn_update=Button(root,text="Update").place(x=60,y=140)
btn_delete=Button(root,text="Delete").place(x=120,y=140)
btn_search=Button(root,text="Search").place(x=180,y=140)

root.mainloop()
