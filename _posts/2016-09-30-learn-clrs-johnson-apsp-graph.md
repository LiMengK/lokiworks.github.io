---
layout: post
title: 算法设计-所有结点对最短路径之Johnson
keywords:
  - Johnson

description: 学习所有结点对最短路径之Johnson算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->

### 1.原理:
如果图中所有的边的权重为非负值，则对每个结点进行一次Dijkstra算法找到所有结点对之间的最短路径;如果图中包含权重为负的边，则先对边重新赋予权重再进行计算。

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160930_johnson_apsp_graph01.PNG)
### 3.伪代码:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160930_johnson_apsp_code.PNG)

### 4.代码片段:
```
from heapq import heappush, heappop
from datetime import datetime
from copy import deepcopy

graph = {
    'a': {'b': -2},
    'b': {'c': -1},
    'c': {'x': 2, 'a': 4, 'y': -3},
    'z': {'x': 1, 'y': -4},
    'x': {},
    'y': {},
}

inf = float('inf')
dist = {}


def dijkstra(graph, s):
    n = len(graph.keys())
    dist = dict()
    Q = list()

    for v in graph:
        dist[v] = inf
    dist[s] = 0

    heappush(Q, (dist[s], s))

    while Q:
        d, u = heappop(Q)
        if d < dist[u]:
            dist[u] = d
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                heappush(Q, (dist[v], v))
    return dist


def initialize_single_source(graph, s):
    for v in graph:
        dist[v] = inf
    dist[s] = 0


def relax(graph, u, v):
    if dist[v] > dist[u] + graph[u][v]:
        dist[v] = dist[u] + graph[u][v]


def bellman_ford(graph, s):
    initialize_single_source(graph, s)
    edges = [(u, v) for u in graph for v in graph[u].keys()]
    number_vertices = len(graph)
    for i in range(number_vertices - 1):
        for (u, v) in edges:
            relax(graph, u, v)
    for (u, v) in edges:
        if dist[v] > dist[u] + graph[u][v]:
            return False  # there exists a negative cycle
    return True


def add_extra_node(graph):
    graph[0] = dict()
    for v in graph.keys():
        if v != 0:
            graph[0][v] = 0


def reweighting(graph_new):
    add_extra_node(graph_new)
    if not bellman_ford(graph_new, 0):
        # graph contains negative cycles
        return False
    for u in graph_new:
        for v in graph_new[u]:
            if u != 0:
                graph_new[u][v] += dist[u] - dist[v]
    del graph_new[0]
    return graph_new


def johnsons(graph_new):
    graph = reweighting(graph_new)
    if not graph:
        return False
    final_distances = {}
    for u in graph:
        final_distances[u] = dijkstra(graph, u)

    for u in final_distances:
        for v in final_distances[u]:
            final_distances[u][v] += dist[v] - dist[u]
    return final_distances


def compute_min(final_distances):
    return min(final_distances[u][v] for u in final_distances for v in final_distances[u])


if __name__ == "__main__":
    graph_new = deepcopy(graph)
    t1 = datetime.utcnow()
    final_distances = johnsons(graph_new)
    if not final_distances:
        print "Negative cycle"
    else:
        print compute_min(final_distances)
    print datetime.utcnow() - t1

```
