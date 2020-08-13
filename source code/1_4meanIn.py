import numpy as np

f = open("txin1.dat")
line = f.readline()
addr = [0] * 8385065
while line :
    element = line.split()
    addr[int(element[4])] += 1
    line = f.readline()
print(np.mean(addr))
f.close()
