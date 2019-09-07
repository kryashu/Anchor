import time
import random
import re
import pymysql
from selenium import webdriver
import pandas as pd
db = pymysql.connect(host="localhost",
                     user="root",  
                     passwd="1234",
                     db="whatsapp")
cur = db.cursor()
def selectProfile():
      profile = "E:\Anchor\Anchor 0.0\Profiles\Profile 1"
      return profile
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir="+selectProfile())
driver = webdriver.Chrome(options=options,
                              executable_path="E:\Anchor\Anchor 0.05\chromedrivers\chromedriver1.exe")
def get_data(url):
    driver.get(url)
    time.sleep(5)
    for i in range(10,26):
       try:
        s = str([i])
        userid_element = driver.find_elements_by_xpath('//*[@id="post-30124"]/div[2]/div/div/h4'+s)[0]
        string = re.split(r'\d\d.\s',userid_element.text)[1]
        print s,string
        sql = "INSERT INTO campaings(camp_id,data) VALUES (%s,%s);"
        cur.execute(sql,(str(i),string))
        db.commit()
       except Exception as e:
           print i,e
get_data("https://www.mantelligence.com/text-conversation-starters/")
db.close()


