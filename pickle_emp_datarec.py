import pickle
e1 = {"Empno":1201,"Name":"Neha","Sal":50000}
e2 = {"Empno":1202,"Name":"Simar","Sal":40000}
e3 = {"Empno":1203,"Name":"Meera","Sal":55000}
e4 = {"Empno":1204,"Name":"Ajay","Sal":70000}
f = open("Emp.dat","wb")
pickle.dump(e1,f)
pickle.dump(e2,f)
pickle.dump(e3,f)
pickle.dump(e4,f)
f.close()
