import numpy as np

f = open("txout1.dat")
line = f.readline()
addr = [0] * 8385065
while line :
    element = line.split()
    addr[int(element[2])] += int(element[3])
    line = f.readline()
f.close()

f1 = open("txin1.dat")
line1 = f1.readline()
while line1:
    element1 = line1.split( )
    addr[int(element1[4])] -= int(element1[5])
    line1 = f1.readline()
maxindex = addr.index(max(addr))
print(max(addr))
print(maxindex)
f1.close()

f2 = open("addresses.dat")
line2 = f2.readline()
while line2 :
    element2 = line2.split()
    if int(element2[0]) == maxindex:
        print(line2, end = '')
        break
    line2 = f2.readline()
f2.close()
