#https://github.com/CyberZHG/CLRS/blob/master/Chapter_20_van_Emde_Boas_Trees/20.2-1.py
import  math
class protoveb:
    def __init__(self, u):
        self.u = u
        self.sqrt = int(math.sqrt(u))
        if self.isLeaf():
            self.a = [0,0]
        else:
            self.summary = protoveb(self.sqrt)
            self.cluster = []
            for _ in xrange(self.sqrt):
                self.cluster.append(protoveb(self.sqrt))

    def isLeaf(self):
        return  self.u == 2

    def high(self, x):
        return  x/self.sqrt
    def low(self, x):
        return  x%self.sqrt
    def index(self, x, y):
        return  x*self.sqrt + y

    def member(self, x):
        if self.isLeaf():
            return  self.a[x]
        return  self.cluster[self.high(x)].member(self.low(x))

    def minimum(self):
        if self.isLeaf():
            if self.a[0] > 0:
                return  0
            if self.a[1] > 0:
                return  1
            return  None
        minCluster = self.summary.minimum()
        if minCluster is None:
            return  None
        offset = self.cluster[minCluster].minimum()
        return  self.index(minCluster, offset)

    def successor(self, x):
        if self.isLeaf():
            if x == 0 and self.a[1] == 1:
                return  1
            return  None
        offset = self.cluster[self.high(x)].successor(self.low(x))
        if offset is not None:
            return  self.index(self.high(x), offset)
        succCluster = self.summary.successor(self.high(x))
        if succCluster is None:
            return  None
        offset = self.cluster[succCluster].minimum()
        return  self.index(succCluster, offset)



