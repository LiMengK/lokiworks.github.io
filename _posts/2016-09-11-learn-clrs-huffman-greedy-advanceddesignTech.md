---
layout: post
title: 算法设计-贪心算法之哈夫曼编码
keywords:
  - 数据结构
  - 贪心算法

description: 学习数据结构贪心算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
只考虑当前状态下的最优解，只做局部最优的选择

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160911_Greedy_Huffman_DataStructures01.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160911_Greedy_Huffman_DataStructures02.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160911_Greedy_Huffman_DataStructures03.PNG)

### 3.伪代码:
```
HUFFMAN(C)
n = |C|
Q = C
for i = 1 to n-1
    allocate a new node z
    z.left = x = EXTRACT-MIN(Q)
    z.right = y = EXTRACT-MIN(Q)
    z.freq = x.freq + y.freq
    INSERT(Q.z)
return EXTRACT-MIN(Q) // return the root of the tree
``` 

### 4.代码片段:
```
import heapq


def huffman(C):
    Q = C[:]
    heapq.heapify(Q)
    n = len(C)
    for i in range(1,n):
        x, y = heapq.heappop(Q), heapq.heappop(Q)
        z = (x[0]+y[0], x, y)
        heapq.heappush(Q, z)

    return Q[0]

def printhuffTree(huffTree, prefix=''):
    if len(huffTree) == 2:
        print(huffTree[1], prefix)
    else:
        printhuffTree(huffTree[1], prefix+'0')
        printhuffTree(huffTree[2], prefix+'1')

if __name__ == '__main__':
    C = [
        (5, 'f'),
        (9, 'e'),
        (12, 'c'),
        (13, 'b'),
        (16, 'd'),
        (45, 'a'),
    ]

r =   huffman(C)

printhuffTree(r)


```
