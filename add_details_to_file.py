f = open("Marks.txt","a")
for i in range(2):
    print("Enter the details for students",i+1,":")
    r = int(input("Enter roll number :"))
    n = input("Enter Name:")
    m = float(input("Marks :"))
    rec = str(r)+","+n+","+str(m)+'/n'
    f.write(rec)
    f.close()
