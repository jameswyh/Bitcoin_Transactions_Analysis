f = open("tx1.dat")
line = f.readline()
total = 0
while line :
    element = line.split()
    if int(element[2]) == 0:
        total = total + 1
    line = f.readline()
print(total)
f.close()
