---
layout: post
title: 算法设计-动态规划之最长公共子序列
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
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160911_DP_Cls_DataStructures01.PNG)


### 3.伪代码:
```
LCS-LENGTH(X, Y )
m = X.length
n = Y.length
let b[1..m, 1..n] and c[0..m,0..n] be new tables
for i = 1 to m
    c[i, 0] = 0
for j = 0 to n
    c[0, j] = 0
for i = 1 to m
    for j = 1 to n
        if xi == yj
            c[i,j]  = c[i-1,j-1] + 1
            b[i,j]  = “\”
        elseif c[i-1, j] >= c[i,j-1]
            c[i,j]  = c[i-1, j] 
            b[i,j]  = “|”
        else c[i,j]  = c[i,j-1]
            b[i,j]  = “-”
return c and b


PRINT-LCS(b,X, i, j)
if i == 0 or j == 0
    return
if b[i,j]  == “\”
    PRINT-LCS(b,X, i-1,j-1)
    print xi
6 elseif b[i,j]  == “|”
7   PRINT-LCS(b,X,i-1,j)
8 else PRINT-LCS(b,X, i, j-1)

``` 

### 4.代码片段:
```
def lcs_lenght(X, Y):
    m = len(X)
    n = len(Y)
    b = [[0 for i in range( n + 1)] for j in range(m + 1)]
    c = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                c[i+1][j+1] = c[i][j] + 1
                b[i+1][j+1] = '\\'
            elif c[i+1][j] > c[i][j+1]:
                c[i+1][j+1] = c[i+1][j]
                b[i+1][j+1] = '-'
            else:
                c[i+1][j+1] = c[i][j+1]
                b[i+1][j+1] = '|'

    return  c, b



def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == '\\':
        print_lcs(b, X, i - 1, j - 1)
        print(X[i-1])
    elif b[i][j] =='|':
        print_lcs(b, X, i, j-1)
    else:
        print_lcs(b, X, i-1, j)


if __name__ == '__main__':

    X = 'ABCBDAB'
    Y = 'BDCABA'
    c, b = lcs_lenght(X, Y)

    for i in c:
        print i
    print('')
    for j in b:
        print j
    print ('')

    print_lcs(b, X, len(X), len(Y))


```
