a = int(input("Number of students in the class:"))
f = open("Marks.txt","w")
for i in range(a):
    print("Enter details of students",i+1,":")
    r = int(input("Enter the roll no:"))
    m = float(input("Marks:"))
    rec = str(r)+","+n+","+str(m)+'/n'
    f.write(rec)
    f.close
