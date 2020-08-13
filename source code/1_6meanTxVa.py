import numpy as np

f = open("txout1.dat")
line = f.readline()
maxaddr = ""
maxamount = 0
addr = [0] * 10000055
while line :
    element = line.split()
    addr[int(element[0])] += int(element[3])
    line = f.readline()
print(np.mean(addr))
f.close()
