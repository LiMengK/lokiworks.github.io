# https://github.com/beniz/fiboheap/blob/master/fiboheap.h
class fibnode:
    def __init__(self, k, p):
        self.mark = False
        self.key = k
        self.p = p
        self.child = None
        self.degree = 0
        self.left = None
        self.right = None


class fibheap:
    def __init__(self):
        self.n = 0
        self.min = None

    def insert(self, x):
        x.degree = 0
        x.p = None
        x.child = None
        x.mark = False
        if not min:
            x.left = x
            x.right = x
            min = x
        else:
            self.min.left.right = x
            x.left = min.left
            self.min.left = x
            x.right = self.min
            if x.key < min.key:
                min = x
        self.n = self.n + 1
    def minimum(self):
        return  self.min

    @staticmethod
    def union_fiheap(H1, H2):
        H = fibheap();
        H.min = H1.min
        if H.min and H2.min:
            H.min.right.left = H2.min.left
            H.min.right.right = H2.min.right
            H.min.right = H2.min
            H2.min = H.min
        if (not H1.min) or (H2.min and H2.min.key < H1.min.key):
            H.min = H2.min
        H.n = H1.n + H2.n
        return H



