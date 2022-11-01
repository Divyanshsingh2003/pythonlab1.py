import mysql.connector
myconn = mysql.connector.connect(host="local host",user ="root",passwd="Abhi@123",database="myschool")
cur =myconn.cursor()
query="Insert into Stud values("{}","{}","{}")".Format(1,"ABC","X")
cur.execute(query)
myconn.commit()
print("Row inserted Sucessfully")
