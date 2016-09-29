---
layout: post
title: 算法设计-所有结点对最短路径之Floyd warshall
keywords:
  - Floyd warshall

description: 学习所有结点对最短路径之Floyd warshall算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->

### 1.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160930_floydwarshall_apsp_graph01.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160930_floydwarshall_apsp_graph02.PNG)
### 2.伪代码:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160930_floydwarshall_apsp_code.PNG)

### 3.代码片段:
```
INF = 999999999
def floywarshall(graph):
    nodes = graph.keys()
    distance = {}
    for n in nodes:
        distance[n] = {}
        for k in nodes:
            distance[n][k] = graph[n][k]

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k]+distance[k][j]

    return  distance

def printSolution(distGraph):
    string = "inf"
    nodes = distGraph.keys()
    for n in nodes:
        print "\t%6s" % (n),
    print " "
    for i in nodes:
        print"%s" % (i),
        for j in nodes:
            if distGraph[i][j] == INF:
                print "%10s" % (string),
            else:
                print "%10s" % (distGraph[i][j]),
        print " "


if __name__ == '__main__':

    graph = {'A':{'A':0,'B':6,'C':INF,'D':6,'E':7},

             'B':{'A':INF,'B':0,'C':5,'D':INF,'E':INF},

             'C':{'A':INF,'B':INF,'C':0,'D':9,'E':3},

             'D':{'A':INF,'B':INF,'C':9,'D':0,'E':7},

             'E':{'A':INF,'B':4,'C':INF,'D':INF,'E':0}

             }

    distGraph = floywarshall(graph)
    printSolution(distGraph)

```
