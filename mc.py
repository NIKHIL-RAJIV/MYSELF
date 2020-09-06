from tkinter import ttk
from tkinter import *
import mysql.connector
from PIL import ImageTk,Image
import tkinter.messagebox as tm
from gui_backend import *


root=Tk()
username = 'root'
password = '#MORUS'
con = mysql.connector.connect(host='localhost',database="tablemaker",user=username,password=password)
cur =con.cursor()


try:
	mycursor.execute('select min(Date) from history')
	day_of_creation = mycursor.fetchone()[0]
	if day_of_creation is None:
		day_of_creation = '2020-01-01'
except :
	day_of_creation = '2020-01-01'

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
	except Exception as err:
		print(err)
		widgetdestroyer(frame)
		messagebox.showerror("error","invalid input . pls try again")	
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

	btn_search=button(frame,"search",colors,16,1,lambda:display(frame,2,(date_from.get(),date_to.get())))

	date_from.place(x=60,y=200)
	date_to.place(x=300,y=200)
	btn_search.place(x=10,y=300)
def fetch_by_datespan(date1,date2):
	try:
		mycursor.execute("select Bill_no,Product_ID,qty,Date from history where Date between %s and %s order by date",(date1,date2))
		data=mycursor.fetchall()
		print(data)
		return data
	except Exception as err:
		print(err)
		return False
def history(root):
	#bgc='#3574c4'
	colors = ('white',bgc)
	widgetdestroyer(root)

	#showcase_frame = LabelFrame(root,bg=bgc,height=500,width=550,bd=3)
	#showcase_frame.place(x=20,y=120)

	btn_2 = button(root,"date span",('white',bgc),20,1,lambda:datespan_func(showcase_frame))
	btn_2.place(x=140,y=20)
    




root = Tk()
root.geometry('800x800')
history(root)
root.mainloop()
