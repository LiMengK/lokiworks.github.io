---
layout: post
title: 算法设计-图搜索之深度优先
keywords:
  - 深度优先

description: 学习图搜索之深度优先算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
总是对最近发现的结点的边进行探索，直到该结点的所有边都被发现。

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_dfs_graph01.PNG)


### 3.伪代码:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_dfs_pcode.PNG)

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
        self.d = 0
        self.p = None
        self.f = 0

    def __gt__(self, other):
        return  self.v > other.v



class bfs:
    def __init__(self):
        self.v = []
        self.adj = defaultdict(list)
        self.time = 0



    def traverse(self):
        for u in self.v:
            self.visit(u)


    def visit(self, u):
        self.time = self.time + 1
        u.d = self.time
        u.color = "GRAY"
        for v in self.adj[u.v]:
            if v.color == "WHITE":
                v.p = u
                self.visit(v)
        u.color = "BLACK"
        self.time = self.time + 1
        u.f = self.time

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


    b.traverse()
    b.printPath(s, y)


```
