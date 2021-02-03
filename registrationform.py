from tkinter import *
import sqlite3

root=Tk()
root.geometry('500x500')
root.title("Registration form")

name_var=StringVar()
email_var=StringVar()
gender_var=StringVar()
country_var=StringVar()
prog_var=StringVar()

def database():
    name=name_var.get()
    email=email_var.get()
    gender=gender_var.get()
    country=country_var.get()
    prog=prog_var.get()

    conn=sqlite3.connect('Regform.db')
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS info 
        (   
            Fullname TEXT,
            Email TEXT,
            Gender TEXT,
            Country TEXT,
            Programming TEXT
        )''')
    cursor.execute('INSERT INTO info (Fullname,Email,Gender,Country,Programming) VALUES(?,?,?,?,?)',(name,email,gender,country,prog,))
    cursor.close()
    conn.commit()
    conn.close()

label_reg=Label(root,text="Registration form",width=20,font=("bold",20))
label_reg.grid(row=1,column=3,columnspan=6,padx=10,pady=10)

label_name=Label(root,text="Full Name",width=10,font=("bold",15))
label_name.grid(row=2,column=0,padx=10,pady=10)

entry_name=Entry(root,textvariable=name_var).grid(row=2,column=6,padx=10,pady=10)

label_email=Label(root,text="Email",width=10,font=("bold",15))
label_email.grid(row=3,column=0,padx=10,pady=10)

entry_email=Entry(root,textvariable=email_var).grid(row=3,column=6,padx=10,pady=5)

label_gender=Label(root,text="Gender",width=10,font=("bold",15))
label_gender.grid(row=4,column=0,padx=10,pady=10)

entry_gender=Entry(root,textvariable=gender_var).grid(row=4,column=6,padx=10,pady=5)

label_country=Label(root,text="Country",width=10,font=("bold",15))
label_country.grid(row=5,column=0,padx=10,pady=10)

entry_country=Entry(root,textvariable=country_var).grid(row=5,column=6,padx=10,pady=5)

label_programming=Label(root,text="Programming",width=10,font=("bold",15))
label_programming.grid(row=6,column=0,padx=10,pady=10)

entry_programming=Entry(root,textvariable=prog_var).grid(row=6,column=6,padx=10,pady=5)

btn_submit=Button(root,text="Submit",width=6,bg="crimson",font=("bold",15),command=database)
btn_submit.grid(row=7,column=3,padx=5,pady=5)

root.mainloop()
