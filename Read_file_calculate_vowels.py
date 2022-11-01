f = open("Myfile.txt","r")
a = " "
v = 0
c = 0
while a:
    a = f.read(1)
    if a in['A','a','E','e','I','i','O','o','U','u']:
        v = v+1
        else:
            c = c+1
            print("vowels in file :",v)
            print("Consonates in the file")
            f.close()




