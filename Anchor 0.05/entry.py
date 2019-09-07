from Tkinter import *
import pymysql
import json
import insert_campaings as whatsapps
import xlrd
#Connecting Database
db = pymysql.connect(host="localhost",user="root",passwd="1234",db="whatsapp")   
cur = db.cursor()

def spread_read(loc):
    d=[]
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0) 
    for i in range(sheet.nrows):
      try:  
       d.append(sheet.cell_value(i, 0))
      except Exception as e:
         print e
    return d

def enter_sheet(): #For Entry from spreadsheet
   sql = "INSERT INTO users(phone,catagory) VALUES (%s,%s);"
   n = str(txt2.get())
   loc = str(txt.get())
   c = spread_read(loc)
   for i in c:
    try:   
     cur.execute(sql,(i,n)) 
     db.commit()
    except Exception as e:
     print "Error",e
   
 
def enter(): #Enter Via single entry
 try:   
   sql = "INSERT INTO users(phone,catagory) VALUES (%s,%s);"
   n = str(txt2.get())
   c = str(txt.get())  
   cur.execute(sql,(c,n)) 
   db.commit()
   txt.delete(0,END)
 except Exception as e:
     print "Error",e

def send():#Run send code
  window.destroy()   
  whatsapps.run()

def refresh():
       window.destroy()
       execfile("entry.py",globals()) 

#GUI DESIGN
window = Tk()
window.title("Anchor 0.02")
l = Label(window,text="Enter Number/Sheet_loc")
l.grid(column=0,row=0)
l2 = Label(window,text="Enter Catagory")
l2.grid(column=0,row=1)
button = Button(window, text = "Refresh",command = refresh)
button.grid(column=0,row=6)
button2 = Button(window, text = "Use Sheet",command = enter_sheet)
button2.grid(column=1,row=7)
Button(window, text="Enter Data",command = enter).grid(column=1, row=6)
Button(window, text="Add campaings",command = send).grid(column=0, row=7)
txt2 = Entry(window,width=30)
txt2.grid(column=1, row=1)
txt = Entry(window,width=30)
txt.grid(column=1, row=0)
window.mainloop()
