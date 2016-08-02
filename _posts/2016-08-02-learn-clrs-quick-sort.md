---
published: false
---
## A New Post

快速排序:这是一个对大量元素进行排序的有效算法。

<!--more-->
### 1.原理:
类似于归并排序，也是基于分治模式(divide-and-conquer),不同的是快速排序每次迭代时就已对数组重排，因此不需要合并操作。

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160802_QuickSort.PNG)

### 3.伪代码:
```
// 	  merge-sort(A, p, r)
// 	  if p < r
// 	  	q = [(p+r)/2]
// 	  	merge-sort(A, p, q)
// 	  	merge-sort(A, q+1, r)
// 	  	merge(A, p, q, r)
//
// 	  merge(A, p, q, r)
// 	  	n1 = p-q+1
// 	  	n2 = r-q
// 	  	let L[1..n1+1] and R[1..n2+1] be new arrays
// 	  	for i = 1 to n1
// 	  		L[i] = A[p+i-1]
// 	  	for j = 1 to n2
// 	  		R[j] = A[q+j]
// 	  	L[n1+1] = ~
// 	  	R[n2+1] = ~
// 	  	i = 1
// 	  	j = 1
// 	  	for k = p to r
// 	  	if L[i] <= R[j]
// 	  		A[k] = L[i]
// 	  		i = i + 1
// 	  	else
// 	  		A[k] = R[j]
// 	  		j = j + 1
//	  example
//		input: (5, 2, 4, 6, 1, 3)
//		output:(1, 2, 3, 4, 5, 6)
``` 
