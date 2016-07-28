---
layout: post
title: 算法设计-排序算法之归并排序
keywords:
  - 归并
  - 排序
description: 学习归并排序算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}

归并排序:这是一个对大量元素进行排序的有效算法。

<!--more-->
### 1.原理:
* **分解**:将原问题分解成一系列子问题
* **解决**:递归地解决子问题。若子问题足够小，则直接求解
* **合并**:将子问题的结果合并成原问题的解
### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160729_MergeSort.JPG)

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
### 4.代码片段:
```
#include <iostream>
#include <limits>  
#include <memory>


#define COUNT_OF(x) (sizeof(x) / sizeof(0[x])) / ((size_t)(!(sizeof(x) % sizeof(0[x]))))


int * merge(int * arr, int p, int q, int r);

void print_array(int * arr)
{
    std::cout << "after sort, array is : ";
    for (int i = 0; i != 5; ++i)
    {
        std::cout << arr[i] << ',';
    }
    std::cout << arr[5] << std::endl;
}

int * merge_sort(int * arr, int p, int r)
{
#if _DEBUG
    print_array(arr);
#endif


    if (p < r) // at least two numbers in arrays. 
    {
        int q = (p + r) / 2;
        merge_sort(arr, p, q);
        merge_sort(arr, q + 1, r);
        merge(arr, p, q, r);
    }

    return arr;
}

int * merge(int * arr, int p, int q, int r)
{
    int * A = arr;

    int n1 = q - p + 1;
    int n2 = r - q;
    
    std::unique_ptr<int[]> L(new int[n1 + 1]);
    std::unique_ptr<int[]> R(new int[n2 + 1]);

    for (int i = 0; i != n1; ++i)
    {
        L[i] = A[p + i];
    }

    for (int i = 0; i != n2; ++i)
    {
        R[i] = A[q + i + 1];
    }

    L[n1] = std::numeric_limits<int>::max();
    R[n2] = std::numeric_limits<int>::max();

    int i = 0;
    int j = 0;
    for (int k = p; k <= r; ++k)
    {
        std::cout << "R[1] = " << R[1] << std::endl;
        if (L[i] <= R[j])
        {
            A[k] = L[i];
            ++i;
        }
        else
        {
            A[k] = R[j];
            ++j;
        }
    }
    return A;
}

// test code.
int main()
{
    int input_arr[] = { 5, 2, 4, 6, 1, 3 };
    int length = COUNT_OF(input_arr);
    int* output_arr = merge_sort(input_arr, 0, length - 1);

    // input info.
    printf("input array is {5,2,4,6,1,3} .\n");

    // output result.
    printf("output array is {");
    for (int i = 0; i != length - 1; ++i)
    {
        printf("%d,", output_arr[i]);
    }
    printf("%d", output_arr[length - 1]);
    printf("} .\n");

    return 0;
}

```


插入排序的最坏情况时间代价为```nlgn``` ,当输入规模较大时，适宜采用。
