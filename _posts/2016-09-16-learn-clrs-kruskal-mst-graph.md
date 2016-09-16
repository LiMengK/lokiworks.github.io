---
layout: post
title: 算法设计-最小生成树之Kruskal
keywords:
  - Kruskal

description: 学习最小生成树之Kruskal算法的设计
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
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160916_kruskal_mst_graph01.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160916_kruskal_mst_graph02.PNG)

### 3.伪代码:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160916_kruskal_mst_pcode.PNG)

### 4.代码片段:
```
parent = dict()
rank = dict()

def makeset(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return  parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] +=1

def kruskal(graph):
    for v in graph['vertices']:
        makeset(v)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for e in edges:
        weight, v1, v2 = e
        if find(v1) != find(v2):
            union(v1, v2)
            minimum_spanning_tree.add(e)
    return  minimum_spanning_tree

graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges': set([
            (1, 'A', 'B'),
            (5, 'A', 'C'),
            (3, 'A', 'D'),
            (4, 'B', 'C'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
        }
minimum_spanning_tree = set([
            (1, 'A', 'B'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
assert kruskal(graph) == minimum_spanning_tree



```
