---
layout: post
title: 算法设计-图搜索之广度优先
keywords:
  - 广度优先

description: 学习图搜索之广度优先算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
将已发现结点与未发现结点之间的边界，沿其*广度*方向向外扩展。

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_bfs_graph01.PNG)


### 3.伪代码:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_bfs_pcode.PNG)

### 4.代码片段:
```
import  sys
from collections import  defaultdict

class queue:
    def __init__(self):
        self.items=[]
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return  self.items.pop(0)
    def empty(self):
        return  self.size() == 0
    def size(self):
        return  len(self.items)

class bfsNode:
    def __init__(self, v):
        self.v = v
        self.color = "WHITE"
        self.d = sys.maxint
        self.p = None

    def __gt__(self, other):
        return  self.v > other.v



class bfs:
    def __init__(self):
        self.v = []
        self.adj = defaultdict(list)



    def traverse(self, s):
        s.color = "GRAY"
        s.d = 0
        s.p = None
        q = queue()
        q.enqueue(s)
        while not q.empty():
            u = q.dequeue()
            adj_list = self.adj[u.v]
            for v in adj_list:
                if v.color == "WHITE":
                    v.color = "GRAY"
                    v.d = u.d + 1
                    v.p = u
                    q.enqueue(v)
            u.color = "BLACK"

    def printPath(self, s, v):
        if v.v==s.v:
            print s.v
        elif v.p == None:
            print "no path form s to v exists"
        else:
            self.printPath(s, v.p)
            print  v.v

if __name__ == '__main__':
    b = bfs()
    r = bfsNode('r')
    s = bfsNode('s')
    t = bfsNode('t')
    u = bfsNode('u')
    v = bfsNode('v')
    w = bfsNode('w')
    x = bfsNode('x')
    y = bfsNode('y')

    b.v.append(r)
    b.v.append(s)
    b.v.append(t)
    b.v.append(u)
    b.v.append(v)
    b.v.append(w)
    b.v.append(x)
    b.v.append(y)

    b.adj['r'].append(s)
    b.adj['r'].append(v)
    b.adj['s'].append(r)
    b.adj['s'].append(w)
    b.adj['t'].append(w)
    b.adj['t'].append(x)
    b.adj['t'].append(u)
    b.adj['u'].append(t)
    b.adj['u'].append(x)
    b.adj['u'].append(y)
    b.adj['v'].append(r)
    b.adj['w'].append(s)
    b.adj['w'].append(t)
    b.adj['w'].append(x)
    b.adj['x'].append(w)
    b.adj['x'].append(t)
    b.adj['x'].append(u)
    b.adj['x'].append(y)
    b.adj['y'].append(x)
    b.adj['y'].append(u)


    b.traverse(s)
    b.printPath(s, y)



```
