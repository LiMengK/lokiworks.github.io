---
layout: post
title: 算法设计-B树
keywords:
  - B树

description: 学习B树算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
属于***平衡树*** 中的一种，具有以下性质:
* 每个结点x有下面的属性
* * x.n, 当前存储在结点x中的关键字的个数
* * x.n个关键字满足x.key1 <= .. <= x.keyn
* * x.leaf, 布尔值，如果为叶子结点则为true, 否则为false
* 每个内部结点x包含x.n+1个指向孩子的指针x.c1..x.cn+1
* 每个叶子结点具有相同的高度
* 除了根结点每个结点至少有t-1个关键字，至多包含2t-1个关键字

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160911_Btree_AdvDataStructures01.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160911_Btree_AdvDataStructures02.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160911_Btree_AdvDataStructures03.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160911_Btree_AdvDataStructures04.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160911_Btree_AdvDataStructures05.PNG)

### 3.伪代码:
```
B-TREE-SEARCH(x, k)
i = 1
while i<=x.n and k > x.keyi
    i = i + 1
if i<=x.n and k == x.keyi
    return (x.i)
elseif x.leaf
    return NIL
else DISK-READ(x.ci)
return B-TREE-SEARCH(x.ci, k)


B-TREE-CREATE(T)
x = ALLOCATE-NODE()
x.leaf = TRUE
x.n = 0
DISK-WRITE(x)
T.root = x


B-TREE-SPLIT-CHILD(x,i)
z = ALLOCATE-NODE()
y = x.ci
z.leaf = y.leaf
z.n = t-1
for j = 1 to t-1
    z.keyj = y.keyj+t
if not y.leaf
    for j = 1 to t
        z.cj = y.cj+t
y.n = t-1
for j = x.n+1 downto i+1
    x.cj+1 = x.cj
x.ci+1 = z
for j = x.n downto i
    x.keyj+1 = x.keyj
x.keyi = y.keyt
x.n = x.n + 1
DISK-WRITE(y)
DISK-WRITE(z)
DISK-WRITE(x)



B-TREE-INSERT(T, k)
r = T.root
if r.n == 2t-1
    s = ALLOCATE-NODE()
    T.root = s
    s.leaf = FALSE
    s.n = 0
    s.c1 = r
    B-TREE-SPLIT-CHILD(s,1)
    B-TREE-INSERT-NONFULL(s, k)
else B-TREE-INSERT-NONFULL(r, k)


B-TREE-INSERT-NONFULL(x, k)
i = x.n
if x.leaf
    while i>=1 an= k < x.keyi
        x.keyi+1 = x.keyi
        i = i-1
    x.keyi+1 = k
    x.n = x.n + 1
    DISK-WRITE.x/
else while i>=1 and k < x.keyi
        i = i-1
    i = i + 1
    DISK-READ(x.ci)
    if x.ci.n == 2t-1
        B-TREE-SPLIT-CHILD(x,i)
        if k > x.keyi
            i = i + 1
    B-TREE-INSERT-NONFULL(x.ci,k)

``` 

### 4.代码片段:
```
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

            if self.child[i].n == self.t*2 -1:
                self.splitchild(i)
                if k > self.key[i]:
                    i = i + 1
            self.child[i].insertnonfull(k)

    def printNode(self):
        for i in range(0, self.n):
            print self.key[i],
        if not self.leaf:
            for j in range(0, self.n+1):
                if self.child[j]:
                    print "[",
                    self.child[j].printNode()
                    print "]",


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


```
