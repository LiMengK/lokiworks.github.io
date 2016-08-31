class bnode:
    def __init__(self, t, p):
        self.t = t
        self.p = p
        self.key = [0]*(2*t-1)
        self.child = [0]*(2*t)
        self.leaf = True
        self.n = 0
    def search(self, k):
        i = 0
        while i <= self.n and k > self.key:
            i = i + 1
        if i < self.n and k == self.key:
            return  (self, i)
        elif self.leaf:
            return  None
        else:
            return  self.child[i], k

    def splitchild(self,i):
        z = bnode(self.t, None)
        y = self.child[i]
        z.leaf = y.leaf
        z.n = self.t - 1
        for j in range(0, self.t-1):
            z.key[j] = y.key[j+self.t]
        if not y.leaf:
            for j in range(0, self.t):
                z.child[j] = y.child[j+self.t]
        y.n = self.t-1
        for j in range(self.n, i, -1):
            self.child[j+1] = self.child[j]
        self.child[i+1] = z
        for j in range(self.n-1, i, -1):
            self.key[j+1] = self.key[j]
        self.key[i] = y.key[self.t-1]
        self.n = self.n + 1

    def insertnonfull(self, k):
        i = self.n
        if self.leaf:
            while i >= 1 and k < self.key[i-1]:
                self.key[i] = self.key[i-1]
                i = i -1
            self.key[i] = k
            self.n = self.n + 1
        else:
            while i >= 1 and k < self.key[i-1]:
                i = i -1
            i = i + 1
            # if self.child[i].n == self.t*2 -1:
            #     self.child[i].splitchild(i)
            #     if k > self.key[i]:
            #         i = i + 1
            # self.child[i].insertnonfull(k)

    def printNode(self):
        for i in range(0, self.n):
            print self.key[i]
        if not self.leaf:
            for j in range(0, self.n+1):
                if self.child[j]:
                    print "\n"
                    self.child[j].printNode()


class btree:
    def __init__(self, t):
        self.t = t
        self.root = bnode(t, None)

    def insert(self, k):
        if self.root:
            r = self.root
            if r.n == self.t * 2 - 1:  # if is full
                s = bnode(self.t, None)
                self.root = s
                s.leaf = False
                s.n = 0
                s.child[0] = r
                s.splitchild(0)
                s.insertnonfull(k)
            else:
                self.root.insertnonfull(k)
    def search(self, k):
        if self.root:
            self.root.search(k)
    def printNode(self):
        if self.root:
            self.root.printNode()

if __name__ == '__main__':
    tr = btree(3)
    for i in range(0, 15):
        tr.insert(i+1)
    tr.printNode()






