---
layout: post
title: 算法设计-贪心算法之活动选择
keywords:
  - 贪心算法

description: 学习贪心算法的设计
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
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160911_Greedy_Activitysel_DataStructures01.PNG)


### 3.伪代码:
```
GREEDY-ACTIVITY-SELECTOR(s, f)
n = s.length
A = {a1}
k = 1
for m = 2 to n
    if s[m] >= f[k]
        A = A U {am}
        k = m
return A
``` 

### 4.代码片段:
```
a = [[5,7],[1,4],[3,5],[0,6],[3,9],[5,9],[6,10],[8,11],[8,12],[2,14],[12,16]]
a = sorted(a, key=lambda e:e[1])

def greedy_activity_selector(s,f):
    n = len(s)
    A = [a[0]]
    k = 0
    for m in xrange(1,n):
        if s[m] >= f[k]:
            A.append(a[m])
            k = m
    return  A

if __name__ == '__main__':
    s, f = [e[0] for e in a], [e[1] for e in a]
    r = greedy_activity_selector(s, f)
    print r
```
