import MySQLdb
import json
import time
db = MySQLdb.connect("localhost","root","zch123","so" )
cursor = db.cursor()
sql = " select user_id,reputation from user_info"
cursor.execute(sql)
results = cursor.fetchall()
list=[]
for each in results:
    dict={}
    dict["id"]=each[0]
    dict["rep"]=int(each[1])
    list.append(dict)
list.sort(key=lambda k: k["rep"],reverse=True)
i=1
for each in list:
    sql2="update user_info set rank="+str(i)+" where user_id="+str(each["id"])
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        print "failed+++++++++++++++++++++++++++++++/n/n/n/n/n/n/n/+++++++++++++++++++++++++++++++++++++++"
    i=i+1
    print str(i)+"\n"

