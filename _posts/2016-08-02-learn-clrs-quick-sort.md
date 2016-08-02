---
layout: post
title: 算法设计-排序算法之快速排序
keywords:
  - 快速排序
  - 排序
description: 学习快速排序算法的设计
category: 算法设计
tags:
  - CLRS
  - 排序
published: true
---
{% include JB/setup %}


快速排序:这是一个对大量元素进行排序的有效算法。

<!--more-->
### 1.原理:
类似于归并排序，也是基于分治模式(divide-and-conquer),不同的是快速排序每次迭代时就已对数组重排，因此不需要合并操作。

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160802_QuickSort.PNG)

### 3.伪代码:
```
// 	  QUICKSORT(A, p, r)
// 	  if p < r
// 	  	q = PARTITION(a, p, r)
//		QUICKSORT(A, p, q-1)
//		QUICKSORT(A, q+1, r)
//
//    PARTITION(a, p, r)
//      x = A[r]
//		i = p-1
//    for(j=p to r-1)
//		if A[j] <= x
//			i = i+1
//			exchange A[i] with A[j]
//	  exchange A[i+1] with A[r]
//	  return i+1
//
//	  example
//		input: (5, 2, 4, 6, 1, 3)
//		output:(1, 2, 3, 4, 5, 6)
``` 

### 4.代码片段:
```
#include <iostream>
using namespace std;

int Partition(int* arr, int p, int r) {
	int x = arr[r];
	int i = p - 1;
	for (int j = p; j <= r-1; ++j) {
		if (arr[j] <= x) {
			++i;
			std::swap(arr[i], arr[j]);
		}

	}
	std::swap(arr[i+1], arr[r]);
	return i+1;
}

void QuickSort(int* arr, int p, int r) {
	if (p < r) {
int q = Partition(arr, p, r);
QuickSort(arr, p, q-1);
QuickSort(arr, q+1, r);
	}
}

void PrintArray(int* arr, int size)
{
	for(int i = 0; i != size-1; ++i){
		cout << arr[i] << ", ";
	}
	cout << arr[size-1] << endl;
}

// test code.
int main() {
int arr[] = {2, 8, 7, 1, 3, 5, 6, 4};
int size = sizeof(arr)/sizeof(arr[0]);

cout << "sort array before is: " << endl;
PrintArray(arr, size);
QuickSort(arr, 0, size-1);
cout << "sort array after is: " << endl;
PrintArray(arr, size);
	return 0;
}
```

快速排序的平均性能相当好，期望运行时间为```nlgn``` ,当输入规模较大时，适宜采用。
