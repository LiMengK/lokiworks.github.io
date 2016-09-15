---
layout: post
title: 算法设计-van Emde Boas 树
keywords:
  - van Emde Boas 树

description: 学习van Emde Boas 树算法的设计
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
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_vebtree_AdvDataStructures01.PNG)

### 3.伪代码:
* veb-member
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_vebtree_select_pcode.PNG)

* veb-minimum
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_vebtree_min_pcode.PNG)

* veb-successor
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_vebtree_successor_pcode.PNG)

* veb-predecessor
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_vebtree_predecessor_pcode.PNG)

* veb-insert
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_vebtree_insert_pcode.PNG)

* veb-delete
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_vebtree_delete_pcode.PNG)

### 4.代码片段:
```
class vEBTree:
    def __init__(self, u):
        self.u = u
        temp = u
        bitnum = -1
        while temp > 0:
            temp >>= 1
            bitnum +=1
        self.sqrt_h = 1 << ((bitnum+1)//2)
        self.sqrt_l = 1 << (bitnum//2)
        self.min = None
        self.max = None

        if not self.isLeaf():
            self.summary = vEBTree(self.sqrt_h)
            self.cluster=[]

            for _ in xrange(self.sqrt_h):
                self.cluster.append(vEBTree(self.sqrt_l))

    def isLeaf(self):
        return  self.u == 2

    def high(self, x):
        return x / self.sqrt_l
    def low(self, x):
        return  x % self.sqrt_l

    def index(self, x, y):
        return  x * self.sqrt_l + y

    def minimum(self):
        return  self.min

    def maximum(self):
        return  self.max

    def maximum(self):
        return  self.max
    def member(self, x):
        if x == self.min or x == self.max:
            return  True
        if self.isLeaf():
            return  False
        return  self.cluster[self.high(x)].member(self.low(x))

    def successor(self, x):
        if self.isLeaf():
            if x==0 and self.max == 1:
                return 1
            return  None
        if self.min is not None and x < self.min:
            return  self.min
        maxlow = self.cluster[self.high(x)].maximum()
        if maxlow is not None and self.low(x) < maxlow:
            offset = self.cluster[self.high(x)].successor(self.low(x))
            return self.index(self.high(x), offset)
        succ_cluster = self.summary.successor(self.high(x))
        if succ_cluster is None:
            return  None
        offset = self.cluster[succ_cluster].minimum()
        return  self.index(succ_cluster, offset)


    def predecessor(self, x):
        if self.isLeaf():
            if x == 1 and self.min == 0:
                return  0
            return None
        if self.max is None and x > self.max:
            return  self.max
        minlow = self.cluster[self.high(x)].minimum()
        if minlow is not None and self.low(x) > minlow:
            offset = self.cluster[self.high(x)].predecessor(self.low(x))
            return  self.index(self.high(x), offset)
        predCluster = self.summary.predecessor(self.high(x))
        if predCluster is None:
            if self.min is not None and x > self.min:
                return  self.min
            return  None
        offset = self.cluster[predCluster].maximum()
        return  self.index(predCluster, offset)

    def insertEmpty(self, x):
        self.min = x
        self.max = x

    def insert(self, x):
        if self.min is None:
            self.insertEmpty(x)
            return
        if x < self.min:
            x, self.min = self.min, x
        if not self.isLeaf():
            if self.cluster[self.high(x)].minimum() is None:
                self.summary.insert(self.high(x))
                self.cluster[self.high(x)].insertEmpty(self.low(x))
            else:
                self.cluster[self.high(x)].insert(self.low(x))
        if x > self.max:
            self.max = x


    def delete(self, x):
        if self.min == self.max:
            self.min = None
            self.max = None
            return
        if self.isLeaf():
            if x == 0:
                self.min = 1
            else:
                self.min = 0
            self.max = self.min
            return
        if x == self.min:
            firstcluster = self.summary.minimum()
            x = self.index(firstcluster, self.cluster[firstcluster].minimum())
            self.min = x
            self.cluster[self.high(x)].delete(self.low(x))
        if self.cluster[self.high(x)].minimum() is None:
            self.summary.delete(self.high(x))
            if x == self.max:
                summax = self.summary.maximum()
                if summax is None:
                    self.max = self.min
                else:
                    self.max = self.index(summax, self.cluster[summax].maximum())
        elif x == self.max:
            self.max = self.index(self.high(x), self.cluster[self.high(x)].maximum())

if __name__ == '__main__':

    veb = vEBTree(16)
    a = [2, 3, 4, 5, 7, 14, 15]
    for v in a:
        veb.insert(v)

    print  veb.minimum()  # 2
    veb.delete(2)
    print  veb.minimum()#3


```
