---
layout: post
title: 算法设计-最小生成树之Prim
keywords:
  - Prim

description: 学习最小生成树之Prim算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
遍历图中所有的顶点，使得边的权重的集合值最小。

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160916_prim_mst_graph01.PNG)

### 3.伪代码:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160916_prim_mst_pcode.PNG)

### 4.代码片段:
```
import  sys
def popmin(pqueue):
    lowest = sys.maxint
    keylowest = None
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            keylowest = key
    del  pqueue[keylowest]
    return  keylowest

def prim(graph, root):
    parents = {}
    keys = {}
    pqueue = {}
    for v in graph:
        parents[v] = None
        keys[v] = sys.maxint
    keys[root] = 0
    for v in graph:
        pqueue[v] = keys[v]

    while pqueue:
        u = popmin(pqueue)
        for v in graph[u]:
            if v in pqueue and graph[u][v] < keys[v]:
                parents[v] = u
                keys[v] = graph[u][v]
                pqueue[v] = graph[u][v]
    return  parents


graph = {0: {1: 6, 2: 8},
         1: {4: 11},
         2: {3: 9},
         3: {},
         4: {5: 3},
         5: {2: 7, 3: 4}}

pred = prim(graph, 0)
for v in pred: print "%s: %s" % (v, pred[v])




```
