from tkinter import ttk
from tkinter import *
import mysql.connector
from PIL import ImageTk,Image
import tkinter.messagebox as tm
from gui_backend import *
from admin_backend import *

root=Tk()
username = 'root'
password = '#MORUS'
con = mysql.connector.connect(host='localhost',database="tablemaker",user=username,password=password)
cur =con.cursor()
'''
try:
	mycursor.execute('select min(Date) from history')
	day_of_creation = mycursor.fetchone()[0]
	if day_of_creation is None:
		day_of_creation = '2020-01-01'
except :
	day_of_creation = '2020-01-01'
'''
def display(frame,option,parameters):
	try:
		widgetdestroyer(frame)

		scroll_bar = Scrollbar(frame)
		text_box   = Text(frame,height=21,width=48,bg=bgc,fg=FG,
			yscrollcommand=scroll_bar.set,font=("cooper",15))

		scroll_bar.pack(side=RIGHT,fill="y")
		text_box.pack()
		scroll_bar.config(command=text_box.yview)
		if option ==1:
			date1 = parameters[0]
			date2 = parameters[1]
			data  = fetch_by_datespan(date1,date2)
			temp = " bill no"+" "*10+"product id"+" "*16+"date"+" "*20+"quantity"+"\n\n"
			text_box.insert(END,temp)
			for row in data:
				bill_no,pid,qty,date = row
				pid = str(pid)
				qty = str(qty)
				date = str(date)
				row = bill_no+" "*19+pid+" "*15+date+" "*18+qty+"\n"
				text_box.insert(END,row)
		elif option ==2:
			date1 = parameters[0]
			date2 = parameters[1]
			data  = fetch_by_datespan(date1,date2)
			temp = " bill no"+" "*10+"product id"+" "*16+"date"+" "*20+"quantity"+"\n\n"
			text_box.insert(END,temp)
			for row in data:
				bill_no,pid,qty = row
				pid = str(pid)
				qty = str(qty)
				date = str(date)
				row = bill_no+" "*19+pid+" "*15+date+" "*18+qty+"\n"
				text_box.insert(END,row)
		elif option==3:
			name=cust_input.get()
			phone=custph_input.get()
			Customerlist=search_Customer(name,phone)
			try:
				text='Bill_no     : '+str(Customerlist[0][0])+'\nCustomer_name   : '+Customerlist[0][1]+'\nPh_no : '+Customerlist[0][2]
				messagebox.showinfo('Search result','Employee Details\n\n'+text)
			except :
				messagebox.showerror('Error','No Such Customer !')

	except Exception as err:
		print(err)
		widgetdestroyer(frame)
		messagebox.showerror("error","invalid input . pls try again")	
def date_func(frame):
    widgetdestroyer(frame)
    colors = ('white',bgc)
    t1="info info info info\n"
    t2="info info info info\n"
    t3="info info info info\n"
    t4="info info info info\n"
    text=t1+t2+t3+t4
    date = str(datetime.today()).split()[0]

    label(frame,text,colors,14).place(x=0,y=0)
    label(frame,"Date :",colors,14).place(x=0,y=200)

    date_input=entry(frame,10,colors,14,1)
    date_input.insert(END,date)
    
    btn_search=button(frame,"search",colors,16,1,lambda:display(frame,1,(date_input.get(),)))
    btn_search.place(x=10,y=300)
    date_input.place(x=60,y=200)
def datespan_func(frame):

	widgetdestroyer(frame)

	colors = ('white',bgc)
	t1="info info info info\n"
	t2="info info info info\n"
	t3="info info info info\n"
	t4="info info info info\n"
	text=t1+t2+t3+t4
	date = str(datetime.today()).split()[0]

	label(frame,text,colors,14).place(x=0,y=0)
	label(frame,"From:",colors,14).place(x=0,y=200)
	label(frame,"To:",colors,14).place(x=250,y=200)

	date_from=entry(frame,10,colors,14,1)
	date_to=entry(frame,10,colors,14,1)
	date_from.insert(END,day_of_creation)
	date_to.insert(END,date)
	messagebox.showerror('Error','Please Check What You Have Entered !')

	btn_search=button(frame,"search",colors,16,1,lambda:display(frame,2,(date_from.get(),date_to.get())))

	date_from.place(x=60,y=200)
	date_to.place(x=300,y=200)
	btn_search.place(x=10,y=300)

def searchcustomer(root):
	widgetdestroyer(root)
	colors = ('blue',bgc)

	widgetdestroyer(showcase_frame)
	showcase_frame.config(text='Search Customer')
	
	Label(showcase_frame,text='Enter Customer name',font=FONT_G_10,bg=BG,fg=FG).grid(row=0,column=0)
	Label(showcase_frame,text='Enter Phone number',font=FONT_G_10,bg=BG,fg=FG).grid(row=1,column=0)

	cust_input=Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)
	custph_input=Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)

	cust_input.grid(row=0,column=2)
	custph_input.grid(row=1,column=2)

	btn_search=button(frame,"search",colors,16,1,lambda:display(frame,3,(custph_input.get(),custph_input.get())))
	btn_search.place(x=10,y=300)

def search_Customer(CustomerName,CustomerPhonenum):

    try:
    	Customerlist=cur.fetchall()
    	print (Customerlist)
    	return Customerlist
    except Exception as err:
    	print (err)
    	return False   

	#Search_Button=Button(root,text='Search Employee',font=FONT_G_13,bg=BG,fg=FG,height=2,command=searchcustomer).place(x=10,y=6)
	#showcase_frame.place(x=10,y=100)
'''
def fetch_by_date(date):
    try:
        mycursor.execute("select bill_no,Product_ID,qty from history where Date=%s order by date",(date,))
        data=mycursor.fetchall()
        return data
    except Exception as err:
        print(err)
        return False

def fetch_by_datespan(date1,date2):
	try:
		mycursor.execute("select Bill_no,Product_ID,qty,Date from history where Date between %s and %s order by date",(date1,date2))
		data=mycursor.fetchall()
		print(data)
		return data
	except Exception as err:
		print(err)
		return False
'''
def search_Customer(CustomerName,CustomerPhonenum):
    try:
    	Customerlist=cur.fetchall()
    	print (Customerlist)
    	return Customerlist
    except Exception as err:
    	print (err)
    	return False

def history(root):
	#bgc='#3574c4'
	colors = ('white',bgc)
	widgetdestroyer(root)

	showcase_frame = LabelFrame(root,bg=bgc,height=500,width=550,bd=3)
	showcase_frame.place(x=20,y=120)
	btn_1 = button(root,"date",('white',bgc),20,1,lambda:date_func(showcase_frame))
	btn_1.place(x=20,y=20)

	btn_2 = button(root,"date span",('white',bgc),20,1,lambda:datespan_func(showcase_frame))
	btn_2.place(x=140,y=20)
	btn_3 = button(root,"customer",('white',bgc),20,1,lambda:searchcustomer(showcase_frame))
	btn_3.place(x=300,y=20)


root = Tk()
showcase_frame=LabelFrame(root,bd=3,width=600,bg=BG,fg=FG,font=FONT_G_12)

root.geometry('800x800')
history(root)
root.mainloop()
