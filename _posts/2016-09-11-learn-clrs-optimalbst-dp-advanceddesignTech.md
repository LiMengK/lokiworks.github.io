---
layout: post
title: 算法设计-动态规划之最优二叉搜索树
keywords:
  - 动态规划

description: 学习动态规划算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
利用空间代价换取了时间代价，将结果集保存在内存中，避免了相同问题的重复计算

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160911_DP_optimalbst_DataStructures01.PNG)


### 3.伪代码:
```
OPTIMAL-BST(p,q,n)
let e[1..n+1, 0..n], w[1..n+1,0..n],
        and root[1..n,1..n] be new tables
for i = 1 to n + 1
    e[i, i-1] = qi-1
    w[i, i-1] = qi-1
for l = 1 to n
    for i = 1 to n-l + 1
        j = i + l - 1
        e[i, j]  = max
        w[i, j]  = w[i,j-1 + pj + qj
        for r = i to j
            t = e[i, r-1] + e[r+1, j]  + w[i,j] 
            if t < e[i,j]
                e[i,j]  = t
                root[i,j]  = r
return e and root

``` 

### 4.代码片段:
```
def optimal_bst(p, q, n):
    e = dict()
    w = dict()
    root = dict()
    for i in range(1, n+2):
        e[(i,i-1)] = q[i-1]
        w[(i, i-1)] = q[i-1]
    for l in range(1, n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            e[(i,j)] = float("inf")
            w[(i,j)] = w[(i,j-1)] + p[j-1] + q[j]
            for r in range(i,j+1):
                t = round(e[(i,r-1)] + e[(r+1,j)] + w[(i,j)], 2)
                if t < e[(i,j)]:
                    e[(i,j)] = t
                    root[(i,j)] = r

    return  e, root

if __name__ == '__main__':
    p = [0.15, 0.1, 0.05, 0.1, 0.2]
    q = [0.05, 0.1, 0.05, 0.05, 0.05, 0.1]
    e, root = optimal_bst(p, q, len(p))
    print e[(1,5)]

```
