from tkinter import ttk
from tkinter import *
import mysql.connector
from PIL import ImageTk,Image
import tkinter.messagebox as tm
user = "root"
database = "tablemaker"
password = '#MORUS'

db = con = mysql.connector.connect(user = user,password=password,host = 'localhost',database = 'tablemaker')

cur = mycursor = con.cursor()
BG='#283848'
FG="white"
bgc=BG#'#3574c4'
BG_OFFSET = BG#"#304050"
FONT = ('impact',13)
FONT_C_12=("cooper",12)
FONT_C_16=("cooper",16)
FONT_G_10 = ('Georgia',10)
FONT_G_12 = ('Georgia',12)
FONT_G_13 = ('Georgia',13)
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
		if option == 1:
			date = parameters[0]
			data = fetch_date(date)
			temp = " bill no"+" "*10+"product id"+" "*10+"quantity"+"\n\n"
			text_box.insert(END,temp)
			for row in data:
				bill_no,pid,qty = row
				pid = str(pid)
				qty = str(qty)
				row = bill_no+" "*19+pid+" "*18+qty+"\n"
				text_box.insert(END,row)
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

def fetch_date(date):
    try:
        mycursor.execute("select bill_no,Product_ID,qty from history where Date=%s order by date",(date,))
        data=mycursor.fetchall()
        return data
    except Exception as err:
        print(err)
        return False

def clicked():
    print("clicked")
def button(window , text , colors , size=0 , bd=1 , command=clicked):
    if size == 0:
        return Button( window , text=text ,fg=colors[0] , bg=colors[1] , bd=bd ,  command=command )
    return Button( window , text=text ,fg=colors[0] , bg=colors[1] , bd=bd , font=("cooper" , size) , command=command )
def widgetdestroyer(frame):
	for widget in frame.winfo_children():
		widget.destroy()

def history(root):
	colors = ('white',bgc)
	widgetdestroyer(root)
	showcase_frame = LabelFrame(root,bg=bgc,height=500,width=550,bd=3)
	showcase_frame.place(x=20,y=120)
	btn_1 = button(root,"date",('white',bgc),20,1,lambda:date_func(showcase_frame))
	btn_1.place(x=20,y=20)


	#Search_Button=Button(root,text='date',('white',,lambda:date_func(showcase_frame))
	#Search_Button.place(x=20,y=20)
	

root=Tk()
root.geometry("600x600")
history(root)
root.mainloop()