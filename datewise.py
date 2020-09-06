from tkinter import ttk
from tkinter import *
import mysql.connector
from PIL import ImageTk,Image
import tkinter.messagebox as tm
from datetime import datetime
from gui_backend import *


root = Tk()
username = 'root'
password = '#MORUS'
con = mysql.connector.connect(host='localhost',database="tablemaker",user=username,password=password)
cur =con.cursor()

def customers(root):
	widgetdestroyer(root)
	showcase_frame=LabelFrame(root,bd=3,width=600,bg=BG,fg=FG,font=FONT_G_12)



	def searchcustomer():
		widgetdestroyer(showcase_frame)
		showcase_frame.config(text='Search Customer')
		
		Label(showcase_frame,text='Enter Customer name',font=FONT_G_10,bg=BG,fg=FG).grid(row=0,column=0)

	
		Label(showcase_frame,text='Enter Phone number',font=FONT_G_10,bg=BG,fg=FG).grid(row=1,column=0)

		cust_input=Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)
		custph_input=Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)

		cust_input.grid(row=0,column=2)
		custph_input.grid(row=1,column=2)
		def search():
			try:
				name=cust_input.get()
				phone=custph_input.get()
				Customerlist=search_Customer(name,phone)
			 
				try:
					text='Bill_no     : '+str(Customerlist[0][0])+'\nCustomer_name   : '+Customerlist[0][1]+'\nPh_no : '+Customerlist[0][2]
					messagebox.showinfo('Search result','Employee Details\n\n'+text)
				except :
					messagebox.showerror('Error','No Such Customer !')
			except:
				messagebox.showerror('Error','Please Check What You Have Entered !')

		showcase_emp_button=Button(showcase_frame,text='   Search   ',font=FONT_G_10,command=search,bg=BG_OFFSET,fg=FG).grid(row=2,column=0)


	Search_Button=Button(root,text='Search Employee',font=FONT_G_13,bg=BG,fg=FG,height=2,command=searchcustomer).place(x=10,y=6)
	showcase_frame.place(x=10,y=100)

def search_Customer(CustomerName,CustomerPhonenum):
    try:
    	Customerlist=cur.fetchall()
    	print (Customerlist)
    	return Customerlist
    except Exception as err:
    	print (err)
    	return False



def widgetdestroyer(frame):
	for widget in frame.winfo_children():
		widget.destroy()


root = Tk()
root.geometry("600x600")
customers(root)
root.mainloop()