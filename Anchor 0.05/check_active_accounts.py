import time
from random import shuffle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pymysql
db = pymysql.connect(host="localhost",
                     user="root",  
                     passwd="1234",
                     db="whatsapp")
cur = db.cursor()
def check(url,i,check_counter):
  try:
       driver.get(url)
       action_button=driver.find_element_by_id("action-button")
       action_button.click()
       time.sleep(20)
       element=driver.find_element_by_class_name("_2Vo52")
       if element is not None:
        val = element.text
        print val
        if val == "Phone number shared via url is invalid.":
          print True
          remove(i["phone"])
        else:
         print False
         if check_counter <= 5:
             check_counter+=1
             print url , "Attempt:-"+str(check_counter)
             check(url,i,check_counter)     
         else:
           check_counter=0
           remove(i["phone"])
    
  except Exception as e:
          print type(e)
          print "Phone number shared via url is valid:-"
          sql="update users set verified = \'1\' WHERE phone = (%s) ;"
          print i
          cur.execute(sql,(i["phone"]))
          db.commit()
          print "verified"
def index():
    d =[]
    sql = "select * from users where invalid = \'0\';"
    cur.execute(sql)
    for row in cur.fetchall():
         d.append({'phone':row[0],'mesaage':row[1]})
    shuffle(d)     
    return d
def remove(num):
    sql="update users set invalid = \'1\', verified = \'1\' WHERE phone = (%s);"
    cur.execute(sql,(num))
    db.commit()
data = index()
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=E:\Anchor\Anchor 0.0\Profiles\Profile 1")
driver = webdriver.Chrome(options=options,
                              executable_path="E:\Anchor\Anchor 0.05\chromedrivers\chromedriver1.exe")
for i in data:
      print i["phone"]
      url =  'https://api.whatsapp.com/send?phone=91'+i["phone"] 
      check(url,i,0)
      
      
