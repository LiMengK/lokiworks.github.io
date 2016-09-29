---
layout: post
title: 算法设计-最大流之ford fulkerson
keywords:
  - ford fulkerson

description: 学习最大流之ford fulkerson算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->

### 1.原理:
采用循环增加流的值，初始时所有结点的流值为0，每一次迭代中，对图中的流值进行增加，直到残存网络中不再存在增广路径为止。

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160930_fordfulkerson_maxflow_graph01.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160930_fordfulkerson_maxflow_graph02.PNG)
### 3.伪代码:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160930_fordfulkerson_maxflow_code.PNG)

### 4.代码片段:
```

class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.target = v
        self.capacity = w

    def __repr__(self):
        return  "%s->%s:%s" % (self.source, self.target, self.capacity)


class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}

    def AddVertex(self, vertex):
        self.adj[vertex] = []

    def GetEdges(self, v):
        return  self.adj[v]

    def AddEdge(self, u, v, w=0):
        if u==v:
            raise ValueError("u==v")

        edge = Edge(u, v, w)
        redge = Edge(v, u, 0)
        edge.redge = redge
        edge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)

        self.flow[edge] = 0
        self.flow[redge] = 0

    def FindPath(self, source, target, path):
        if source == target:
            return  path
        for edge in self.GetEdges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and not (edge, residual) in path:
                result = self.FindPath(edge.target, target, path + [(edge, residual)])
                if result != None:
                    return  result

    def MaxFlow(self, source, target):
        path = self.FindPath(source, target, [])
        print  'path after enter MaxFlow: %s' % path
        for key in self.flow:
            print  '%s:%s' % (key, self.flow[key])
        print  '-' * 20

        while path != None:
            flow = min(res for edge, res in path)
            for edge, res in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            for key in self.flow:
                print  '%s:%s' % (key, self.flow[key])
            path = self.FindPath(source, target, [])
            print  'path inside of while loop: %s' % path
            for key in self.flow:
                print  '%s:%s' % (key, self.flow[key])
            return  sum(self.flow[edge] for edge in self.GetEdges(source))



if __name__ == "__main__":
  g = FlowNetwork()
  map(g.AddVertex, ['s', 'o', 'p', 'q', 'r', 't'])
  g.AddEdge('s', 'o', 5)
  g.AddEdge('s', 'p', 3)
  g.AddEdge('o', 'p', 2)
  g.AddEdge('o', 'q', 3)
  g.AddEdge('p', 'r', 4)
  g.AddEdge('r', 't', 3)
  g.AddEdge('q', 'r', 4)
  g.AddEdge('q', 't', 2)
  print g.MaxFlow('s', 't')



```
