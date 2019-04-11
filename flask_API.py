from flask import Flask
import pymysql
import json

db = pymysql.connect(host="localhost",
                     user="root",  
                     passwd="1234",
                     db="whatsapp")   
app = Flask(__name__)
cur = db.cursor()
@app.route('/phone')
def index():
    d =[]
    sql = "select phone,msg from users where msg is not null;"
    cur.execute(sql)
    for row in cur.fetchall():
      d.append({'phone':row[0],'mesaage':row[1]})
    data = json.dumps(d)
    d=[]
    return data
@app.route('/message/<num>')
def set_null(num):
    sql = "Update users set msg = NULL where phone = %s"
    cur.execute(sql,(num))
    db.commit()
    return ''
if __name__ == '__main__':
    app.run(host='localhost',port='8080',debug=True)
