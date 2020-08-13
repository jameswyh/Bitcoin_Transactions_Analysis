import numpy as np

f = open("bh1.dat")
line = f.readline()
total = 0
while line :
    element = line.split()
    total = total + int(element[3])
    line = f.readline()
print(total / 212576)
f.close()
