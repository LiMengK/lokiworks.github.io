---
layout: post
title: 算法设计-排序算法之计数排序
keywords:
  - 计数排序
  - 排序
description: 学习计数排序算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}


计数排序:这是一个对大量整数元素进行排序的有效算法。

<!--more-->
### 1.原理:
对于每一输入元素x，确定出小于x的元素个数。就可将x放入到数组中的正确位置。

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160808_CountSort.PNG)

### 3.伪代码:
```
// 	  COUNTING-SORT(A, B, k)
// 	  let C[0..k] be a new array
// 	  	for i=0 to k
//			C[i] = 0
//		for j=1 to A.length
//			C[A[j]] = C[A[j]] + 1
//    // C[i] now contains the number of elements equal to i.
//    	for i=1 to k
//	  		C[i] = C[i] + C[i-1]
//    // C[i] now contains the number of elements less than or equal to i.
//		for j=A.length downto 1
//			B[C[A[j]]] = A[j]
//			C[A[j]] = C[A[j]] - 1
//
//	  example
//		input: (1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1)
//		output:(1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 7)
``` 

### 4.代码片段:
```
import copy
#arraycopy = []
def countingsort(array, maxval):
        arraycopy = copy.deepcopy(array)
        
        m = maxval + 1
        count = [0] * m

        for a in array:
                count[a] += 1

        for a in range(1,m):

                count[a] =  count[a] + count[a-1]

        for a in range(len(array)-1, -1, -1):
                arraycopy[count[array[a]]-1] = array[a]
                count[array[a]] = count[array[a]] - 1
        return (arraycopy, count)

print countingsort([1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1], 7)

```

计数排序的平均性能相当好，最差运行时间为```n``` ,当输入规模较大时，适宜采用。
