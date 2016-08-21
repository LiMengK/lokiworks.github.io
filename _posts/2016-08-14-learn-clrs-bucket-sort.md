---
layout: post
title: 算法设计-桶排序
keywords:
  - 排序

description: 学习桶排序算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
划分n个大小相同的子区间(**桶**)，然后将n个数放入各个桶中

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160821_BucketSort.PNG)
### 3.伪代码:
```
BUCKET-SORT(A)
	let B[0..n-1] be a new array
n = A.length
for i=0 to n-1
	make B[i] an empty list
for i=1 to n
	insert A[i] insert B[nA[i]]
for i = 0 to n-1
	sort list B[i] with insert sort
concatenate the lists B[0],B[1]......B[n-1] together in order
``` 

### 4.代码片段:
```
#include <iostream>
#include <algorithm>
#include <vector>
#include <memory>
using namespace std;

void bucketsort(float * arr, int n)
{
    std::unique_ptr<vector<float>[]> b(new vector<float>[n]);
    for (int i = 0; i != n; ++i)
    {
        int bi = n * arr[i];
        b[bi].push_back(arr[i]);
    }

    for (int i = 0; i != n; ++i)
    {
        std::sort(b[i].begin(), b[i].end());
    }

    int index = 0;
    for (int i = 0; i != n; ++i)
    {
        for (int j = 0; j != b[i].size(); ++j)
        {
            arr[index++] = b[i][j];
        }
    }


}
int main()
{
    float arr[] = { 0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434 };
    int n = sizeof(arr) / sizeof(arr[0]);
    bucketsort(arr, n);

    cout << "sorted array is \n";
    for (int i = 0; i != n; ++i)
    {
        cout << arr[i] << " ";
    }

    return 0;
}

```
