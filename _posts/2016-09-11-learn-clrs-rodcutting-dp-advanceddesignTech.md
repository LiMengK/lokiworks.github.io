---
layout: post
title: 算法设计-动态规划之切割钢条
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
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160911_DP_RodCutting_DataStructures01.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160911_DP_RodCutting_DataStructures02.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160911_DP_RodCutting_DataStructures03.PNG)

### 3.伪代码:
```
BOTTOM-UP-CUT-ROD(p, n)
let r[0..n] be a new array
r[0] = 0
for j = 1 to n
    q = -max
    for i = 1 to j
        q = max(q,p[i] + r[j - i] )
    r[j]  = q
return r[n]

``` 

### 4.代码片段:
```
import time

import sys


def bottom_up_cut_rod(p, n):
    r = [0]*(n+1)
    for j in range(1, n+1):
        q = -sys.maxint-1
        for i in range(j):
            q = max(q, p[i]+r[j-i-1])
        r[j] = q

    return  r[n]



if __name__ == '__main__':
    begin = time.time()
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    print  bottom_up_cut_rod(p, 3)

    print 'total run time', time.time() - begin

```
