import time
import os
import datetime
import random
import pymysql
import multiprocessing
from threading import Thread
from random import shuffle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.chrome.service as service
bots=[]
db = pymysql.connect(host="localhost",
                     user="root",  
                     passwd="1234",
                     db="whatsapp")
cur = db.cursor()
sql = "select phone from bots;"
cur.execute(sql)
for row in cur.fetchall():
    bots.append(row[0])
db.close()
def selectdriver():
     profile_list=[] 
     path = "E:\Main()\work\Anchor\Anchor 0.05\chromedrivers"
     for i in os.listdir(path):
                profile = path+"\\"+i
                profile_list.append(profile)   
     return profile_list
def selectprofile():
     profile_list=[] 
     path = "E:\Main()\work\Anchor\Anchor 0.0\Profiles"
     for i in os.listdir(path):
                profile = path+"\\"+i
                profile_list.append(profile)   
     return profile_list
def dump(phone,msg,profile):
      time = str(datetime.datetime.now())
      print "dumping",phone,msg
      f = open("dump.txt",'a+')
      f.write (phone+" "+msg+" "+time+" "+profile+"\n")
      f.close()
def dump_error(phone,msg,profile):
      time = str(datetime.datetime.now())
      print "dumping",phone,msg
      f = open("Untitled-2.txt",'a+')
      f.write (phone+" "+msg+" "+time+" "+profile+"\n")
      f.close()
def index():
    d=[]
    db = pymysql.connect(host="localhost",
                     user="root",  
                     passwd="1234",
                     db="whatsapp")
    cur = db.cursor()
    sql = "select * from users where verified = \"1\" and invalid = \"0\";"
    cur.execute(sql)
    for row in cur.fetchall(): 
             d.append({'phone':row[0],'catagory':row[1]})
    db.close()
    shuffle(d)
    return d[:13]

def selectCamp():
      db = pymysql.connect(host="localhost",
                     user="root",  
                     passwd="1234",
                     db="whatsapp")
      cur = db.cursor()
      i = str(random.randint(1, 336))
      sql = "Select data from campaings where camp_id ="+i
      cur.execute(sql)
      for row in cur.fetchall():
            r = row[0]
            break
      db.close()
      return r
def get_bot():
      i = random.randint(0, (len(bots)-1))
      return bots[i]

def run(profile,d):
       data = index()
       options = webdriver.ChromeOptions()
       options.add_argument("--user-data-dir="+profile)
       driver = webdriver.Chrome(options=options,
                                                 executable_path= d)
       counter = 0
       for i in data:
              msg = selectCamp()
              phone = i["phone"]
              url =  'https://api.whatsapp.com/send?phone=91'+phone+'&text='+msg  
              try: 
                    driver.get(url)
                    action_button=driver.find_element_by_id("action-button")
                    action_button.click()
                    time.sleep(15)    
                    send_button = driver.find_element_by_class_name('_3M-N-')
                    if send_button is not None:
                            print "found"
                            dump(phone,msg,profile)
                            send_button.click()
              except Exception as e:
                         print e
                         dump_error(phone,str(e),profile)
              counter+=1
              k = random.randint(10,30)
              time.sleep(k)
              if counter == 3 :
                  msg = selectCamp()
                  num = get_bot()
                  url = 'https://api.whatsapp.com/send?phone=91'+num+'&text='+msg
                  try: 
                    driver.get(url)
                    action_button=driver.find_element_by_id("action-button")
                    action_button.click()
                    time.sleep(10)    
                    send_button = driver.find_element_by_class_name('_3M-N-')
                    if send_button is not None:
                            print "found"
                            dump(num,msg,profile)
                            #send_button.click()
                  except Exception as e:
                         dump_error(num,e,profile)
                         print e
                  counter = 0
                  
       driver.close()
profile_list = selectprofile()
driver_list = selectdriver()

jobs = []
for i in range(0,len(profile_list)):   
    if __name__ == '__main__':    
      p1 = multiprocessing.Process(target=run,args=[profile_list[i],driver_list[i]])
      jobs.append(p1)
      p1.start()
      time.sleep(3)
for j in jobs:
      j.join()
print "Processing Complete"