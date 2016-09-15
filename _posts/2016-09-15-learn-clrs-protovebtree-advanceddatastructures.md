---
layout: post
title: 算法设计-proto van Emde Boas 树
keywords:
  - proto van Emde Boas 树

description: 学习proto van Emde Boas 树算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
支持优先队列操作的数据结构,该数据结构限制关键字必须为0~n-1的整数且无重复

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_protovebtree_AdvDataStructures01.PNG)

### 3.伪代码:
* veb-member
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_protovebtree_select_pcode.PNG)

* veb-minimum
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_protovebtree_min_pcode.PNG)

* veb-successor
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_protovebtree_successor_pcode.PNG)

* veb-insert
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_protovebtree_insert_pcode.PNG)

### 4.代码片段:
```


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

    def insert(self, x):
        if self.isLeaf():
            self.a[x] = 1
        else:
            self.summary.insert(self.high(x))
            self.cluster[self.high(x)].insert(self.low(x))

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

if __name__ == '__main__':
    veb = protoveb(16)
    a = [2, 3, 4, 5, 7, 14, 15]
    for v in a:
        veb.insert(v)

    print  veb.minimum() #2



    s =  veb.successor(14)
    print  s

```
