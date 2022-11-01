import mysql.connector
myconn = mysql.connector.connect(host="Local host",user ="root",passwd="Abhi@123",database="my school")
cur = myconn.cursor()
cur.execute("Update Stud Class ={} WHERE staff={}".format("IX",II))
myconn.commit()
print("Table Updated Sucessfully")
