from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pymysql

root=Tk()


usernameVar=StringVar()
passwordVar=StringVar()
nidVar=StringVar()
nameVar=StringVar()
postcodeVar=StringVar()
genderVar=StringVar()
phonenoVar=StringVar()
addressVar=StringVar()
relief_id_Var=StringVar()
foods_goods_Var=StringVar()
quantity_Var=StringVar()

relief_slip=ttk.Treeview()
slip_list=[]



def remove_all_widgets():
    global root
    for widget in root.winfo_children():
        widget.destroy()

def logout():
	remove_all_widgets()
	loginWindow()



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
    	remove_all_widgets()
    	Consumer()
    else:
        messagebox.showerror("Invalid user", "Credentials enters are invalid")

def Addconsumerinfo():
	global nidVar
	global nameVar
	global postcodeVar
	global genderVar
	global phonenoVar
	global addressVar

	nid=nidVar.get()
	name=nameVar.get()
	postcode=postcodeVar.get()
	gender=genderVar.get()
	phone=phonenoVar.get()
	address=addressVar.get()

	conn=pymysql.connect(host="localhost",user="root",passwd="",db="login")
	cursor=conn.cursor()

	query="insert into userinfo (nid,name,postcode,gender,phone,address) values('{}','{}','{}','{}','{}','{}')".format(nid,name,postcode,gender,phone,address)
	cursor.execute(query)
	conn.commit()
	conn.close()
	nidVar.set("")
	nameVar.set("")
	postcodeVar.set("")
	genderVar.set("")
	phonenoVar.set("")
	addressVar.set("")



def Addslipdata():

	global relief_id_Var
	global foods_goods_Var
	global quantity_Var
	global slip_list
	relief_id=relief_id_Var.get()
	foods_goods=foods_goods_Var.get()
	quantity=quantity_Var.get()

	conn=pymysql.connect(host="localhost",user="root",passwd="",db="login")
	cursor=conn.cursor()
	query="insert into slip (relief_id,foods_goods,quantity) values('{}','{}','{}')".format(relief_id,foods_goods,quantity)
	cursor.execute(query)
	conn.commit()
	conn.close()
	slip_list_dict={"relief_id":relief_id,"foods_goods":foods_goods,"quantity":quantity}
	slip_list.append(slip_list_dict)
	fetchslipdata()




def fetchslipdata():
	y=relief_slip.get_children()
	for data in y:
		relief_slip.delete(data)

	for items in slip_list:
		relief_slip.insert('',END,values=(items["relief_id"],items["foods_goods"],items["quantity"]))


def clear_slip_info():

	global relief_id_Var
	global foods_goods_Var
	global quantity_Var
	relief_id_Var.set("")
	foods_goods_Var.set("")
	quantity_Var.set("")

def make_slip():
    global slip_list

    print_slip=""
    print_slip+="\tRelief Receipt\t\n\n\n"
    print_slip+="{:<20}{:<20}{:<20}\n".format("Relief ID","Foods or Goods","Relief Quantity(kg/number)")

    for data in slip_list:
    	print_slip+="{:<20}{:<20}{:<20}\n".format(data["relief_id"],data["foods_goods"],data["quantity"])

    make_file=filedialog.asksaveasfile(mode='w',defaultextension=".txt")

    if make_file!="":
    	make_file.write(print_slip)
    	make_file.close()

    else:
    	messagebox.showerror("Invalid file")

    print(print_slip)

    slip_list=[]




def loginWindow():

    titleLabel = Label(root,text="Relief Program",font="Arial 22",fg="green")
    titleLabel.grid(row=0,column=0,columnspan=4, padx=(40,0),pady=(20,0))

    loginLabel = Label(root,text="Admin Login",font="Arial 20",fg="green")
    loginLabel.grid(row=1, column=2,padx=(50,0),columnspan=2, pady=10)

    usernameLabel = Label(root, text="Username",fg="green",font="Arial 15")
    usernameLabel.grid(row=2, column=2,padx=20,pady=5)

    passwordLabel = Label(root, text="Password",fg="green",font="Arial 15")
    passwordLabel.grid(row=3, column=2,padx=20,pady=5)

    usernameEntry= Entry(root, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=3,padx=20,pady=5)

    passwordEntry = Entry (root, textvariable=passwordVar,show="*")
    passwordEntry.grid(row=3,column=3,padx=20,pady=5)

    loginButton=Button(root, text="Login",fg="green",width=20, height=2, command=lambda:adminLogin())
    loginButton.grid(row=4, column=2, columnspan=2)




def Consumer():
	root.title("Consumer Chart")
	root.geometry("1350x700+0+0")

	title=Label(root,text="Consumer Info",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),fg="green")
	title.grid(row=0,column=2)

	manage_frame=Frame(root,bd=4,relief=RIDGE,bg="black")
	manage_frame.place(x=20,y=100,width=450,height=560)

	f_title=Label(manage_frame,text="Consumer Entry",bg="crimson",fg="white",font=("times new roman",30,"bold"))
	f_title.grid(row=1,columnspan=2,pady=20)

	nid=Label(manage_frame,text="NID No",bg="crimson",fg="white",font=("times new roman",20,"bold"))
	nid.grid(row=2,column=0,pady=10,padx=20,sticky="w")

	nid_entry=Entry(manage_frame,textvariable=nidVar,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
	nid_entry.grid(row=2,column=1,pady=10,padx=20,sticky="w")

	name=Label(manage_frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
	name.grid(row=3,column=0,pady=10,padx=20,sticky="w")

	name_entry=Entry(manage_frame,textvariable=nameVar,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
	name_entry.grid(row=3,column=1,pady=10,padx=20,sticky="w")

	post_code=Label(manage_frame,text="Post Code",bg="crimson",fg="white",font=("times new roman",20,"bold"))
	post_code.grid(row=4,column=0,pady=10,padx=20,sticky="w")

	postcode_entry=Entry(manage_frame,textvariable=postcodeVar,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
	postcode_entry.grid(row=4,column=1,pady=10,padx=20,sticky="w")

	gender=Label(manage_frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
	gender.grid(row=5,column=0,pady=10,padx=20,sticky="w")

	gender_entry=ttk.Combobox(manage_frame,textvariable=genderVar,font=("times new roman",15,"bold"),state='readonly')
	gender_entry['values']=('Male','Female','Others')
	gender_entry.grid(row=5,column=1,pady=10,padx=20,sticky="w")

	phone=Label(manage_frame,text="Phone No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
	phone.grid(row=6,column=0,pady=10,padx=20,sticky="w")

	phone_entry=Entry(manage_frame,textvariable=phonenoVar,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
	phone_entry.grid(row=6,column=1,pady=10,padx=20,sticky="w")

	address=Label(manage_frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
	address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

	address_entry=Entry(manage_frame,textvariable=addressVar,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
	address_entry.grid(row=7,column=1,pady=10,padx=20,sticky="w")

	btn_frame=Frame(manage_frame,bd=1,relief=RIDGE,bg="crimson")
	btn_frame.place(x=10,y=500,width=200)

	consumer_add_btn=Button(btn_frame,text="Add Consumer",bg="green",font=("times new roman",20,"bold"),command=lambda:Addconsumerinfo())
	consumer_add_btn.grid(row=0,column=1)
	relief_frame=Frame(root,bd=4,relief=RIDGE,bg="crimson")
	relief_frame.place(x=510,y=100,width=820,height=560)

	consumer_label=Label(relief_frame,text="Relief ID",bg="crimson",fg="white",font=("times new roman",17,"bold"))
	consumer_label.grid(row=0,column=0,pady=10,padx=20,sticky="w")

	consumer_label_entry=Entry(relief_frame,textvariable=relief_id_Var,font=("times new roman",14,"bold"),bd=4,relief=GROOVE)
	consumer_label_entry.grid(row=0,column=1,pady=10,padx=20,sticky="w")

	food_goods=Label(relief_frame,text="Foods & Goods",bg="crimson",fg="white",font=("times new roman",17,"bold"))
	food_goods.grid(row=1,column=0,pady=10,padx=20,sticky="w")

	food_goods_entry=ttk.Combobox(relief_frame,textvariable=foods_goods_Var,font=("times new roman",14,"bold"),state='readonly')
	food_goods_entry['values']=('Rice','Salt','Oil','Saline','Potatoes','Pulse')
	food_goods_entry.grid(row=1,column=1,pady=10,padx=20,sticky="w")

	quantity=Label(relief_frame,text="Quantity(kg/number)",bg="crimson",fg="white",font=("times new roman",17,"bold"))
	quantity.grid(row=2,column=0,pady=10,padx=20,sticky="w")

	quantity_entry=ttk.Combobox(relief_frame,textvariable=quantity_Var,font=("times new roman",14,"bold"),state='readonly')
	quantity_entry['values']=('1','2','3','4','5','6','7','8','9','10')
	quantity_entry.grid(row=2,column=1,pady=10,padx=20,sticky="w")

	add_to_slip=Button(relief_frame,text="Add To Slip",bg="green",fg="white",font=("times new roman",17,"bold"),command=lambda:Addslipdata())
	add_to_slip.grid(row=2,column=2,pady=10,padx=20,sticky="w")

	btn_logout=Button(relief_frame,text="Log Out",bg="green",command=lambda:logout(),fg="white",font=("times new roman",17,"bold"))
	btn_logout.grid(row=0,column=2,pady=10,padx=20,sticky="w")

	btn_clear_slip=Button(relief_frame,text="Clear Slip",command=clear_slip_info,bg="green",font=("times new roman",17,"bold"))
	btn_clear_slip.grid(row=1,column=2,pady=10,padx=20,sticky="w")

	slip_label=Label(relief_frame,text="Relief Slip",bg="green",font=("times new roman",17,"bold"))
	slip_label.grid(row=3,column=0,pady=10,padx=20,sticky="w")

	global relief_slip

	relief_slip= ttk.Treeview(relief_frame,height=14, columns=('Consumer NID','Foods & Goods','Quantity'))
	relief_slip.grid(row=4,column=0,columnspan=4)

	scroll_slip=Scrollbar(relief_frame,orient="vertical",command=relief_slip.yview)
	scroll_slip.grid(row=4,column=3,sticky="NSE")

	relief_slip.configure(yscrollcommand=scroll_slip.set)

	relief_slip.heading("#0",text="Relief ID")
	relief_slip.heading("#1",text="Foods & Goods")
	relief_slip.heading("#2",text="Quantity")

	fetchslipdata()

	make_slip_btn=Button(relief_frame,text="Make Slip",command=make_slip,bg="green",font=("times new roman",17,"bold"))
	make_slip_btn.grid(row=3,column=2,padx=20,pady=10,sticky="w")


loginWindow()
root.mainloop()		