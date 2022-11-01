import mysql.connector
m = mysql.connector.connect(host="localhost",user="root",password="Abhi@123",database="test")
c = m.cursor()
c.execute("select from student")
d = c.fetchmany(3)
for a in d:
    print(a)
