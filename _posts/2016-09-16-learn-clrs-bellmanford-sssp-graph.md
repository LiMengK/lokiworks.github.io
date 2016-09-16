---
layout: post
title: 算法设计-单源最短路径之Bellman Ford
keywords:
  - Bellman Ford

description: 学习单源最短路径之Bellman Ford算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
从给点结点到其他每个结点的路径最短。

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160916_bellmanford_sssp_graph01.PNG)

### 3.伪代码:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160916_bellmanford_sssp_pcode.PNG)

### 4.代码片段:
```
import pdb
def initialize(graph, source):
    d = {} # Stands for destination
    p = {} # Stands for predecessor

    for node in graph:
        d[node] = float('Inf')
        p[node] = None
    d[source] = 0
    return  d, p

def relax(node, neighbour, graph, d, p):
    if d[neighbour] > d[node] + graph[node][neighbour]:
        d[neighbour] = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)

    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return  d, p

if __name__ == '__main__':
    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  3, 'd':  2, 'e':  2},
        'c': {},
        'd': {'b':  1, 'c':  5},
        'e': {'d': -3}
        }

    d, p = bellman_ford(graph, 'a')

    assert d == {
        'a':  0,
        'b': -1,
        'c':  2,
        'd': -2,
        'e':  1
        }

    assert p == {
        'a': None,
        'b': 'a',
        'c': 'b',
        'd': 'e',
        'e': 'b'
        }

```
