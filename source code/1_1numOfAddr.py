f = open("txout1.dat")
line = f.readline()
maxaddr = 0
while line :
    element = line.split()
    #print(line, end = '')
    if int(element[2]) > maxaddr:
        maxaddr = int(element[2])
    line = f.readline()
print(maxaddr)
f.close()
