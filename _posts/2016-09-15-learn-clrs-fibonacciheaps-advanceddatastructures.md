---
layout: post
title: 算法设计-斐波那契堆
keywords:
  - 斐波那契堆

description: 学习斐波那契堆算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
它是一组最小堆序(每个结点的关键字总是大于或等于其父结点的关键字)的根树的集合,斐波那契的性质主要体现在合并堆上

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_FibonacciHeap_AdvDataStructures01.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_FibonacciHeap_AdvDataStructures02.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_FibonacciHeap_AdvDataStructures03.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_FibonacciHeap_AdvDataStructures04.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_FibonacciHeap_AdvDataStructures05.PNG)

### 3.伪代码:
* Insert a node
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_protovebtree_select_pcode.PNG)

* Union heap
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_FibonacciHeap_unionheap_pcode.PNG)

* extract minimum node
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_FibonacciHeap_extractminnode_pcode.PNG)

* consolidate heap
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_FibonacciHeap_consolidate_pcode.PNG)

* decrease key
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_FibonacciHeap_decreasekey_pcode.PNG)

* delete node
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_FibonacciHeap_deletenode_pcode.PNG)


### 4.代码片段:
```

import  math
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

    def iterate(self, head):
        node = stop = head
        flag = False
        while True:
            if node == stop and flag:
                break
            elif node == stop:
                flag = True
            yield  node
            node = node.right

    def insert(self, x):
        x.degree = 0
        x.p = None
        x.child = None
        x.mark = False
        if not self.min:
            x.left = x
            x.right = x
            self.min = x
        else:
            self.min.left.right = x
            x.left = self.min.left
            self.min.left = x
            x.right = self.min
            if x.key < self.min.key:
                self.min = x
        self.n = self.n + 1

    def minimum(self):
        return  self.min

    def heaplink(self, y, x):
        y.left.right = y.left
        y.right.left = y.right
        if x.child:
            x.child.left.right = y
            y.left = x.child.left
            x.child.left = y
            y.right = x.child
        else:
            x.child = y
            y.right = y
            y.left = y
        y.p = x
        x.degree = x.degree + 1
        y.mark = False

    def consolidate(self):
        max_degree = (int)(math.log(self.n)/math.log((1+math.sqrt(5))/2))
        A = [None]*(max_degree+2)

        w = self.min
        rootsize = 0
        next = w
        rootList = []
        while True:
            rootsize = rootsize + 1
            rootList.append(next)
            next = next.right
            if next == w:
                break

        for i in range(0, rootsize):
            w = rootList[i]
            x = w
            d = x.degree
            while A[d]:
                y = A[d]
                if x.key > y.key:
                    x,y = y, x
                self.heaplink(y,x)
                A[d] = None
                d = d + 1
            A[d] = x
        self.min = None
        for i in xrange(0, max_degree+2):
            if A[i]:
                if not self.min:
                    self.min = A[i].left = A[i].right = A[i]
                else:
                    self.min.left.right = A[i]
                    A[i].left = self.min.left
                    self.min.left = A[i]
                    A[i].right = self.min
                    if A[i].key < self.min.key:
                        self.min = A[i]







    def extractMin(self):
        z = self.min
        if z:
            x = z.child
            if x:
                children = [x for x in self.iterate(z.child)]
                for i in xrange(0, len(children)):
                    x = children[i]
                    self.min.left.right = x
                    x.left = self.min.left
                    self.min.left = x
                    x.right = self.min
                    x.p = None
            z.left.right = z.right
            z.right.left = z.left
            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self.consolidate()
            self.n -= 1
        return  z





    @staticmethod
    def union_fiheap(H1, H2):
        H = fibheap()
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


if __name__ == '__main__':
    f = fibheap()
    f.insert(fibnode(10, None))
    f.insert(fibnode(2, None))
    f.insert(fibnode(15, None))
    f.insert(fibnode(6, None))

    q = f.extractMin()
    print  q.key #2
    q = f.extractMin()
    print  q.key #6

    f2 = fibheap()
    f2.insert(fibnode(100, None))
    f2.insert(fibnode(56, None))

    H = fibheap.union_fiheap(f, f2)
    q = H.extractMin()
    print  q.key #10

```
