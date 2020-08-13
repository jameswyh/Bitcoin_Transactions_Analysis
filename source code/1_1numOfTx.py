f = open("tx1.dat")
line = f.readline()
totaltx = 0
while line :
    element = line.split()
    totaltx = totaltx + 1
    line = f.readline()
print(totaltx)
f.close()
