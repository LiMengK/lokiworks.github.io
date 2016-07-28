---
layout: post
title: 算法设计-排序算法之插入排序
keywords:
  - 插入
  - 排序
description: 学习插入排序算法的设计
category: 算法设计
tags:
  - CLRS
  - 排序
published: true
---
{% include JB/setup %}

插入排序:这是一个对少量元素进行排序的有效算法。

<!--more-->
### 1.原理:
工作原理与很多人打牌时，整理手中牌时的做法差不多。在开始摸牌时，我们的左手是空的，牌面朝下放在桌上。接着，一次从桌上摸起一张牌，并将它插入到左手一把牌的正确位置上。为了找到这张牌的正确位置，要将它与手中已有的每一张从右到左地进行比较，无论在什么时候，左手中的牌都是排好序的，而这些牌原先都是桌上那副牌里最顶上的一些牌。

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160724_InsertSort.JPG)

### 3.伪代码:
```
// for j = 2 to A.length
// 		key = A[j]
// 		// Insert A[j] into the sorted sequence A[1..j-1]
// 		i = j - 1
// 		while i > 0 and A[i] > key
// 		A[i+1] = A[i]
// 		i = i - 1
// 		A[i+1] = key
//
// 		example 
// 		input: (5, 2, 4, 6, 1, 3)
//		output:(1, 2, 3, 4, 5, 6)
``` 
### 4.代码片段:
```
#include <stdio.h>
#include <assert.h>

#define COUNT_OF(x) (sizeof(x) / sizeof(0[x])) / ((size_t)(!(sizeof(x) % sizeof(0[x]))))
 

int*  insert_sort(int* arr, int length)
{
	assert(arr != NULL);
	assert(length > 0);
	
	for (int j = 1; j != length; ++j)
	{
		int key = arr[j];
		int i = j - 1;
		while(i >= 0 && arr[i] > key)
		{
			arr[i+1] = arr[i];
			i = i - 1;
		}
		arr[i + 1] = key;
		
	}	

	return arr;
}

// test code.
int main()
{
	int input_arr[] = {5, 2, 4, 6, 1, 3};
	int length = COUNT_OF(input_arr);
	int* output_arr = insert_sort(input_arr, length);
	
	// input info.
	printf("input array is {5,2,4,6,1,3} .\n");	

	// output result.
	printf("output array is {");
	for(int i = 0; i != length-1; ++i)
	{
		printf("%d,", output_arr[i]);
	}
	printf("%d", output_arr[length-1]);
	printf("} .\n");

	return 0;
}
```


插入排序的最坏情况时间代价为```n^2``` ,当输入规模较大时，不宜采用。
