import webbrowser
import time
import urllib
import os
import pymysql
from Tkinter import *
def run():
 def send():
    db = pymysql.connect(host="localhost",    # your host, usually 192.168.43.216
                     user="root",         # your username
                     passwd="1234",  # your password
                     db="whatsapp")        # name of the data base
    cur = db.cursor()
    cat = txt.get()
    msg = txt2.get("1.0","end-1c")
    sql = "INSERT INTO campaings(camp_id,data) VALUES (%s,%s);"
    cur.execute(sql,(msg,cat))
    db.commit()
   
 def refresh():
       window.destroy()
       execfile("insert_campaings.py",globals())

 
 window = Tk()
 window.title("Anchor 0.02")
 l = Label(window,text="Enter Campaing's ID")
 l.grid(column=0,row=0)
 l2 = Label(window,text="Enter Message")
 l2.grid(column=0,row=1)
 button = Button(window, text = "Refresh",command = refresh)
 button.grid(column=0,row=6)
 Button(window, text="Add", command=send).grid(column=1, row=6)
 txt2 = Text(window,height=5,width=30)
 txt2.grid(column=1, row=1)
 txt = Entry(window,width=30)
 txt.grid(column=1, row=0)
 window.mainloop()
run()