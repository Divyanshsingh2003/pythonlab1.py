import csv
f = open("compresult.csv","w")
c = csv.writer(f)
cd=[
    ['Name','Point','Rank'],
    ['Shradha',4500,23],
    ['Nishchay',4800,31],
    ['Ali',4500,25],
    ['Adi',5100,14]]
c = writerows(rd)
f.close()
