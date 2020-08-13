f = open("txh.dat")
line = f.readline()
n = 0
while line :
    element = line.split()
    if element[0] == "7553001":
        print(line, end = '')
        break
    line = f.readline()
f.close()
