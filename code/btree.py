#https://github.com/JPWKU/BTree/blob/master/BTree.java
class bnode:
    def __init__(self, t, parent):
        self.t = t
        self.parent = parent
        self.key = [0]*(2*t-1)
        self.child = [0]*(2*t)
        self.leaf = True

    def count(self):
        return len(self.key)

class btree:
    def __init__(self, t):
        self.t = t
        self.root = bnode(t, None)

    def search(self, x, k):
        i = 0
        while i < x.count and k > x.key[i]:
            ++i
        if i < x.count and k == x.key[i]:
            return (x, i)
        elif x.leaf:
            return  None
        else:
            return self.search(x.child[i], k)




