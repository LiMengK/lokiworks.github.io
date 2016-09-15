---
layout: post
title: 算法设计-Disjoint-sets森林
keywords:
  - Disjoint-sets森林

description: 学习Disjoint-sets森林算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
按秩合并和路径压缩，得到一个渐进最优的不相交集合的数据结构

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_disjointsetforest_AdvDataStructures01.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_disjointsetforest_AdvDataStructures02.PNG)

### 3.伪代码:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160915_disjointsetforest_pcode.PNG)

### 4.代码片段:
```
class disjointset:
    def __init__(self):
        self.p = self
        self.rank = 0

    @staticmethod
    def union(x, y):
        disjointset.link(x, y)

    @staticmethod
    def link(x, y):
        if x.rank > y.rank:
            y.p = x
        else:
            x.p = y
            if x.rank == y.rank:
                y.rank += 1

    def findset(self, x):
        if x != x.p:
            x.p = self.findset(x.p)
        return  x.p


if __name__ == '__main__':
    d1 = disjointset()
    d2 = disjointset()

    disjointset.union(d1, d2)

    d3 = d1.findset(d2)
    if d2 == d3:
        print  'd2 == d3'
    else:
        print 'd2 != d3'



```
