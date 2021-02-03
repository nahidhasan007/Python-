from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pymysql

root=Tk()

usernameVar=StringVar()
passwordVar=StringVar()

def remove_all_widgets():
    global root
    for widget in root.winfo_children():
        widget.grid_remove()


def adminLogin():
    global usernameVar
    global passwordVar

    username = usernameVar.get()
    password = passwordVar.get()

    conn = pymysql.connect(host="localhost", user="root", passwd="", db="login")
    cursor = conn.cursor()

    query = "select * from users where username='{}' and password='{}'".format(username, password)
    cursor.execute(query)
    data = cursor.fetchall()
    admin = False
    for row in data:
        admin = True
    conn.close()
    if admin:
        Student()
        remove_all_widgets()
    else:
        messagebox.showerror("Invalid user", "Credentials enters are invalid")


def loginWindow():
    titleLabel = Label(root,text="Union Relief Chart",font="Arial 40",fg="green")
    titleLabel.grid(row=0,column=0,columnspan=4, padx=(40,0),pady=(10,0))

    loginLabel = Label(root,text="Admin Login",font="Arial 30")
    loginLabel.grid(row=1, column=2,padx=(50,0),columnspan=2, pady=10)

    usernameLabel = Label(root, text="Username")
    usernameLabel.grid(row=2, column=2,padx=20,pady=5)

    passwordLabel = Label(root, text="Password")
    passwordLabel.grid(row=3, column=2,padx=20,pady=5)

    usernameEntry= Entry(root, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=3,padx=20,pady=5)

    passwordEntry = Entry (root, textvariable=passwordVar,show="*")
    passwordEntry.grid(row=3,column=3,padx=20,pady=5)

    loginButton=Button(root, text="Login",width=20, height=2, command=lambda:adminLogin())
    loginButton.grid(row=4, column=2, columnspan=2)

def Student():
	root.title("Student Management System!")
	root.geometry("900x900+1400+400")

	title=Label(root,text="Student Management System!",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="red",fg="yellow")
	title.grid(row=0,column=0,padx=20,pady=20)

	manage_frame=Frame(root,bd=4,relief=RIDGE,bg="crimson")
	manage_frame.place(x=20,y=100,width=450,height=560)

	manage_detail_frame=Frame(root,bd=4,relief=RIDGE,bg="crimson")
	manage_detail_frame.place(x=510,y=100,width=810,height=560)

	m_title=Label(manage_frame,text="Manage Student",bg="crimson",fg="white",font=("times new roman",30,"bold"))
	m_title.grid(row=0,columnspan=2,pady=20)

	l_roll=Label(manage_frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
	l_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

	text_roll=Entry(manage_frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
	text_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

	l_name=Label(manage_frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
	l_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

	text_name=Entry(manage_frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
	text_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

	l_email=Label(manage_frame,text="Email;",bg="crimson",fg="white",font=("times new roman",20,"bold"))
	l_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

	text_email=Entry(manage_frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
	text_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

	l_gender=Label(manage_frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
	l_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

	combo_gender=ttk.Combobox(manage_frame,font=("times new roman",14,"bold"),state="readonly")
	combo_gender['values']=("Male","Female","Othres")
	combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

	l_phone=Label(manage_frame,text="Phone No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
	l_phone.grid(row=5,column=0,pady=10,padx=20,sticky="w")

	text_phone=Entry(manage_frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
	text_phone.grid(row=5,column=1,pady=10,padx=20,sticky="w")

	l_dob=Label(manage_frame,text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold"))
	l_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

	text_dob=Entry(manage_frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
	text_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

	l_address=Label(manage_frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
	l_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

	text_address=Entry(manage_frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
	text_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")



loginWindow()
root.mainloop()		