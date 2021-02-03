from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

window=Tk()
window.geometry("900x600")
window.title("R&B")


#global variable for entries
usernamevar=StringVar()
passwordvar=StringVar()

#quantity field listener
def QFL(a,b,c):
	global quantityvar
	global costvar
	global itemrate
	quantity=quantityvar.get()
	if quantity != "":
		try:
			quantity=float(quantity)
			cost=quantity*itemrate
			quantityvar.set("%.2f"%quantity)
			costvar.set("%.2f"%cost)
		except ValueError:
			quantity=float(quantity[:-1])
			quantityvar.set("%.2f"%quantity)
	else:
		quantity=0
		quantityvar.set(quantity)		

#cost field listener
def CFL(a,b,c):
	global quantityvar
	global costvar
	global itemrate
	cost=costvar.get()
	if cost != "":
		try:
			cost=float(cost)
			quantity=cost/itemrate
			quantityvar.set("%.2f"%quantity)
			costvar.set("%.2f"%cost)
		except ValueError:
			cost=cost[:-1]
			costvar.set("%.2f"%cost)
	else:
		cost=0
		costvar.set(cost)		
#main window variable
options=[]
ratedict={}
itemvariable=StringVar()
quantityvar=StringVar()
quantityvar.trace('w',QFL)
itemrate=2
ratevar=StringVar()
ratevar.set("%.2f"%itemrate)
costvar=StringVar()
costvar.trace('w',CFL)

#main treeview-------
billsTv=ttk.Treeview(height=15,columns=('Item name','Quantity','Cost'))


#additem variable
storeoptions=["Frozen","Fresh"]
itemnamevar=StringVar()
itemratevar=StringVar()
itemtypevar=StringVar()
itemstorevar=StringVar()	
itemstorevar.set(storeoptions[0])

#=========funtion to read data from list of item
def readAllData():
    global options
    global ratedict
    global itemvariable
    global itemrate
    global rateVar
    options=[]
    ratedict={}
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="info")
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = "select * from itemlist"
    cursor.execute(query)
    data = cursor.fetchall()
    count=0
    for row in data:
        count+=1
        options.append(row['nameid'])
        ratedict[row['nameid']]=row['rate']
        itemvariable.set(options[0])
        itemrate=int(ratedict[options[0]])
    conn.close()
    ratevar.set("%.2f"%itemrate)
    if count ==0:
        remove_all_widgets()
        itemAddWindow()
    else:
        remove_all_widgets()
        mainwindow()


def optionMenuListener(event):
    global itemvariable
    global ratedict
    global itemrate
    item = itemvariable.get()
    itemrate= int(ratedict[item])
    ratevar.set("%.2f"%itemrate)

#==========function to remove all widget
def remove_all_widgets():
    global window
    for widget in window.winfo_children():
        widget.grid_remove()


#adminlogin function
def adminlogin():
	global usernamevar
	global passwordvar

	username=usernamevar.get()
	password=passwordvar.get()

	conn=pymysql.connect(host="localhost",user="root",passwd="",db="info")
	if conn:
		print("yes")
	else:
		print("no")	
	cursor=conn.cursor()
	query = "select * from users where username='{}' and password='{}'".format(username, password)
	cursor.execute(query)
	data=cursor.fetchall()
	print(data)
	admin=False
	count=0
	for row in data:
		admin = True
		count=count+1
	print(count)	
	conn.close()
	if admin:
		readAllData()
	else:
		messagebox.showerror("Invalid user or password")

def addItemListener():
    remove_all_widgets()
    itemAddWindow()

def addItem():
    global itemnamevar
    global itemratevar
    global itemtypevar
    global itemstorevar
    name = itemnamevar.get()
    rate = itemratevar.get()
    Type = itemtypevar.get()
    storeType= itemstorevar.get()
    nameId=name.replace(" ","_")
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="info")
    cursor = conn.cursor()
    query = "insert into itemlist (name,nameid,rate,type,storetype) value('{}','{}','{}','{}','{}')".format(name, nameId, rate,Type,storeType)
    cursor.execute(query)
    conn.commit()
    conn.close()
    itemnamevar.set("")
    itemratevar.set("")
    itemtypevar.set("")



def loginwindow():
	title=Label(window,text="Billing System")
	title.grid(row=0,column=0,columnspan=2,padx=40,pady=10)

	loginlabel=Label(window,text="Admin login")
	loginlabel.grid(row=1,column=2,padx=20,pady=10)

	usernamelabel=Label(window,text="Username")
	usernamelabel.grid(row=2,column=2)

	passwordlabel=Label(window,text="Password")
	passwordlabel.grid(row=3,column=2)

	usernamentry=Entry(window,textvariable=usernamevar)
	usernamentry.grid(row=2,column=3)

	passwordentry=Entry(window,textvariable=passwordvar,show="*")
	passwordentry.grid(row=3,column=3)

	loginbutton=Button(window,text="Login",width=10,height=1,command=lambda:adminlogin())
	loginbutton.grid(row=5,column=3)

def mainwindow():
	title=Label(window,text="Billing System")
	title.grid(row=0,column=0,columnspan=3,padx=40,pady=10)

	additem=Button(window,text="Add Item",width=20,height=2,command=lambda: addItemListener())
	additem.grid(row=1,column=0,padx=10,pady=10)

	logoutbtn=Button(window,text="Logout",width=20,height=2)
	logoutbtn.grid(row=1,column=4,padx=10,pady=10)
	
	itemlabel=Label(window,text="Select item")
	itemlabel.grid(row=2,column=0,padx=5,pady=10)

	itemdropdown=OptionMenu(window,itemvariable,*options,command=optionMenuListener)
	itemdropdown.grid(row=2,column=1,padx=10,pady=10)

	ratelabel=Label(window,text="Rate")
	ratelabel.grid(row=2,column=2,padx=10,pady=10)

	ratevalue=Label(window,textvariable=ratevar)
	ratevalue.grid(row=2,column=3,padx=10,pady=10)

	quantitylabel=Label(window,text="Quantity")
	quantitylabel.grid(row=3,column=0,padx=5,pady=5)

	quantityentry=Entry(window,textvariable=quantityvar)
	quantityentry.grid(row=3,column=1,padx=5,pady=5)

	costlabel=Label(window,text="Cost")
	costlabel.grid(row=3,column=2,padx=10,pady=10)

	costentry=Entry(window,textvariable=costvar)
	costentry.grid(row=3,column=3,padx=10,pady=10)

	billbtn=Button(window,text="Generate Bill")
	billbtn.grid(row=3,column=4,padx=5)

	billlabel=Label(window,text="Bills",font="Arial 25")
	billlabel.grid(row=4,column=2,padx=10,pady=10)

	billsTv.grid(row=5,column=0,columnspan=5)

	scrollbar=Scrollbar(window,orient="vertical",command=billsTv.yview)
	scrollbar.grid(row=5,column=4,sticky="NSE")

	billsTv.configure(yscrollcommand=scrollbar.set)

	billsTv.heading('#0',text="Item name")
	billsTv.heading('#1',text="Rate")
	billsTv.heading('#2',text="Quantity")
	billsTv.heading('#3',text="Cost")

def itemAddWindow():
	backbtn=Button(window,text="Back",command=lambda:readAllData())
	backbtn.grid(row=0,column=1)

	title=Label(window,text="Billing System",width=40)
	title.grid(row=0,column=0,columnspan=4,padx=40,pady=10)

	itemnamelabel=Label(window,text="Name")
	itemnamelabel.grid(row=1,column=1,pady=10)

	itemnamentry=Entry(window,textvariable=itemnamevar)
	itemnamentry.grid(row=1,column=2,pady=10)

	itemratelabel=Label(window,text="Rate")
	itemratelabel.grid(row=1,column=3,pady=10)

	itemratentry=Entry(window,textvariable=itemratevar)
	itemratentry.grid(row=1,column=4,pady=10)

	itemtypelabel=Label(window,text="Type")
	itemtypelabel.grid(row=2,column=1,pady=10)

	itemtypentry=Entry(window,textvariable=itemtypevar)
	itemtypentry.grid(row=2,column=2,pady=10)

	storetypelabel=Label(window,text="Stored Type")
	storetypelabel.grid(row=2,column=3,pady=10)

	storentry=OptionMenu(window,itemstorevar,*storeoptions)
	storentry.grid(row=2,column=4,pady=10)


	additembtn=Button(window,text="Add item",width=20,height=2,command=lambda: addItem())
	additembtn.grid(row=3,column=3,padx=10,pady=10)


loginwindow()
window.mainloop()
