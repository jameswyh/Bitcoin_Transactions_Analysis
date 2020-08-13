import sys
import numpy as np

sys.setrecursionlimit(10**6)

class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.parent = [-1]*n
        for i in range(n):
            self.parent[i] = i

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            self.parent[yroot]= xroot

    def get_count(self):
        total = set()
        #print(self.parent)
        for i in range(self.n):
            total.add(self.find(i))
        #print("total", total)
        return len(total)

    def get_total(self):
        total = set()
        for i in range(self.n):
            total.add(self.find(i))
        return total

user = 0
addr = [0] * 8385065
tx = [0] * 10000055
uf = UnionFind(8385065)

f1 = open("txin1.dat")
line1 = f1.readline()
pre_tx = -1
pre_addr = -1
i = 0
while line1 :
    element1 = line1.split()
    if int(element1[0]) == pre_tx:
        uf.union(int(element1[4]), pre_addr)
    tx[int(element1[0])] = int(element1[4])
    pre_tx = int(element1[0])
    pre_addr = int(element1[4])
    line1 = f1.readline()
f1.close()

f2 = open("txout1.dat")
line2 = f2.readline()
pre_tx2 = -1
pre_addr2 = -1
pre_out = -1
while line2 :
    element2 = line2.split()
    if int(element2[1]) == 0 and pre_out == 0:
        uf.union(pre_addr2, tx[pre_tx2])
    pre_tx2 = int(element2[0])
    pre_addr2 = int(element2[2])
    pre_out = int(element2[1])
    line2 = f2.readline()
f2.close()

userindex = list(uf.get_total())
userlist = [0] * 4241424

f3 = open("txout1.dat")
line3 = f3.readline()
while line3 :
    element3 = line3.split()
    user = uf.find(int(element3[2]))
    userlist[userindex.index(user)] += int(element3[3])
    line3 = f3.readline()
f3.close()

f4 = open("txin1.dat")
line4 = f4.readline()
while line4:
    element4 = line4.split( )
    user = uf.find(int(element4[4]))
    userlist[userindex.index(user)] -= int(element4[5])
    line4 = f4.readline()
f4.close()

userparent = userindex[userlist.index(max(userlist))]

print(userparent)
print(np.mean(userlist))
