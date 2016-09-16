---
layout: post
title: 算法设计-单源最短路径之Dijkstra
keywords:
  - Dijkstra

description: 学习单源最短路径之Dijkstra算法的设计
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
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160916_dijkstra_sssp_graph01.PNG)

### 3.伪代码:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160916_dijkstra_sssp_pcode.PNG)

### 4.代码片段:
```
# returns a list with elements in order of the path
# between the start and end of a graph
# @param parent dict the mapping between node and parent
# @param start int the starting node
# @param end int the ending node
def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


# Uses dijkstra's algorithm to find the shortest path
# @param graph list of lists, adjacency list
# @param source int the source node to start the search
# @param target int the target node to search for
def dijkstra(graph, source, target):
    queue = []
    visited = {}
    distance = {}
    shortest_distance = {}
    parent = {}

    for node in xrange(len(graph)):
        distance[node] = None
        visited[node] = False
        parent[node] = None
        shortest_distance[node] = float("inf")

    queue.append(source)
    distance[source] = 0
    while len(queue) != 0:
        current = queue.pop(0)
        visited[current] = True
        if current == target:
            print backtrace(parent, source, target)
            # break
        for neighbor in graph[current]:
            if visited[neighbor] == False:
                distance[neighbor] = distance[current] + 1
                if distance[neighbor] < shortest_distance[neighbor]:
                    shortest_distance[neighbor] = distance[neighbor]
                    parent[neighbor] = current
                    queue.append(neighbor)
    print distance
    print shortest_distance
    print parent
    print target


adjList = [[1, 6, 8],
           [0, 4, 6, 9],
           [4, 6],
           [4, 5, 8],
           [1, 2, 3, 5, 9],
           [3, 4],
           [0, 1, 2],
           [8, 9],
           [0, 3, 7],
           [1, 4, 7]]
dijkstra(adjList, 0, 3)

```
