f = open("txin1.dat")
line = f.readline()
addr = [0] * 10000055
while line :
    element = line.split()
    addr[int(element[0])] += 1
    line = f.readline()
maxin = max(addr)
print(maxin)
f.close()
for i in range(len(addr)):
    if addr[i] == maxin:
        print(i)
