---
layout: post
title: 算法设计-动态规划之矩阵链
keywords:
  - 数据结构
  - 动态规划

description: 学习数据结构动态规划算法的设计
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
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160911_DP_MatricChaining_DataStructures01.PNG)


### 3.伪代码:
```
MATRIX-CHAIN-ORDER(p)
n = p.length - 1
let m[1..n, 1..n] and s[1..n-1, 2..n] be new tables
for i = 1 to n
    m[i,i] = 0
for l = 2 to n // l is the chain length
    for i = 1 to n-l+1
        j = i + l - 1
        m[i,j]  = max
        for k = i to j - 1
            q = m[i,k] + m[k+1, j]  + pi-1pkpj
            if q < m[i,j]
                m[i,j] = q
                s[i,j] = k
return m and s

PRINT-OPTIMAL-PARENS(s, i, j)
if i == j
    print “A”i
else print “(”
    PRINT-OPTIMAL-PARENS(s, i, s[i,j])
    PRINT-OPTIMAL-PARENS(s, s[i,j]+1, j)
    print “)”

``` 

### 4.代码片段:
```
import sys

def gk(i,j):
    return  str(i) + ',' + str(j)

def matrix_chain_order(p):
    n = len(p)-1
    m, s = {}, {}
    for i in xrange(1, n+1):
        m[gk(i, i)] = 0
    for l in xrange(2, n+1):
        for i in xrange(1, n-l+2):
            j = i+l-1
            m[gk(i, j)] = sys.maxint
            for k in xrange(i, j):
                q = m[gk(i, k)]+m[gk(k+1, j)]+p[i-1]*p[k]*p[j]
                if q<m[gk(i, j)]:
                    m[gk(i, j)] = q
                    s[gk(i, j)] = k
    return m, s

def get_optimal_parens(s, i, j):
    res = ''
    if i == j:
        return "A"+str(j)
    else:
        res += "("
        res += get_optimal_parens(s, i, s[gk(i, j)])
        res += get_optimal_parens(s, s[gk(i, j)]+1, j)
        res +=  ")"
        return res





if __name__ == '__main__':
    p = [30, 35,15, 5, 10, 20, 25]
    m, s = matrix_chain_order(p)
    print 'total number is ', m[gk(1, 6)]
    print 'the solution is ', get_optimal_parens(s, 1, 6)


```
