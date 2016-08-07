---
layout: post
title: 算法设计-排序算法之基数排序
keywords:
  - 计数排序
  - 排序
description: 学习基数排序算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}


快速排序:这是一个对大量整数元素进行排序的有效算法。

<!--more-->
### 1.原理:
按最低有效位有效位到最高位***按位***依次进行排序

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160808_RadixSort.PNG)

### 3.伪代码:
```
// 	  RADIX-SORT(A, B, k)
//        for i=1 to d
//              use a stable sort to sort array A on digit i

//	  example
//		input: (170,45,75,90,802,2,24,66)
//		output:(2,24,45,66,75,90,170,802)
``` 

### 4.代码片段:
```
#include <iostream>
#include <memory>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

void SortArray(vector<int> *b, int num)
{
    for (int i = 0; i != num; ++i)
    {
        std::sort(b[i].begin(), b[i].end());
    }
}

int GetBitValue(int value, int bit)
{
    int cnt = 0;
    do
    {
        ++cnt;
        int result = value % 10;
        if (cnt == bit)
        {
            return result;
        }
    } while (value = value / 10);

    return 0;
}

void ConcatenateArray(int *arr, vector<int> *b, int num)
{
    int index = 0;
    for (int i = 0; i != num; ++i)
    {
        for (int j = 0; j != b[i].size(); ++j)
        {
            arr[index++] = b[i][j];
        }
    }
}

void Print(int *arr, int num)
{
    cout << "print array: ";
    for (int i = 0; i != num; ++i)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void ClearArray(vector<int> *b, int num)
{
    for (int i = 0; i != num; ++i)
    {
        b[i].clear();
    }
}

void RadixSort(int* arr, int n, int digit)
{
    const int NUM = 10;
    vector<int> b[NUM];
 
    
    for (int i = 0; i != digit; ++i)
    {
        for (int j = 0; j != n; ++j)
        {
       
            int index = GetBitValue(arr[j], i+1);
            b[index].push_back(arr[j]);
        }
        SortArray(b, NUM);
        ConcatenateArray(arr, b, NUM);
        ClearArray(b, NUM);
        Print(arr, n);
    }
}

int main()
{

    int arr[] = { 170,45,75,90,802,2,24,66 };
    int len = sizeof(arr) / sizeof(arr[0]);
    RadixSort(arr, len, 3);
    for (int i = 0; i != len; ++i)
    {
        cout << arr[i] << " ";
    }
    return 0;
}


```

计数排序的平均性能相当好，最差运行时间为```n``` ,当输入规模较大时，适宜采用。
