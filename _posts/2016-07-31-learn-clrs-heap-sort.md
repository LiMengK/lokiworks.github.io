---
layout: post
title: 算法设计-排序算法之堆排序
keywords:
  - 堆排序
  - 排序
description: 学习堆排序算法的设计
category: 算法设计
tags:
  - CLRS
  - 排序
published: true
---
{% include JB/setup %}

堆排序:这是一个对大量元素进行排序的有效算法。

<!--more-->
### 1.原理:
将数组对象视为一颗完全二叉树。树中的每个结点与数组中的元素对应。对数组元素的排序就是调整树中结点的位置，任意时刻树的根结点的值都是当前堆的最大值。每迭代一次将当前根节点的值按照从后往前的顺序依次放入数值元素中。

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160731_HeapSort.PNG)

### 3.伪代码:
```
// PARENT(i) return [i/2]
// LEFT(i) return 2*i
// Right(i) return 2*i+1
// MAX_HEAPIFY(A,i)
// l = LEFT(i)
// r = RIGHT(i)
// if l<= A.heapsize() and A[l] > A[i]
//      largest = l
// else largest = i
// if r <= A.heapsize and A[r] > A[largest]
//      largest = r
// if largest != i
//      exchange A[i] with A[largest]
//      MAX_HEAPIFY(A, largest)
//
// BUILD_MAX_HEAP(A)
// A.heapsize = A.length
// for i=[A.length/2] downto 1
//      MAX_HEAPIFY(A, i)
//
// HEAPSORT(A)
// BUILD_MAX_HEAP(A)
// for i = A.length downto 2
// exchange A[1] with A[i]
// A.heapsize = A.heapsize-1
// Max_Heapify(A,1)
``` 
### 4.代码片段:
```
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define  LEFT(i) 2*i + 1
#define  RIGHT(i) 2*i + 2

class IntArray
{
public:
    IntArray();
    ~IntArray();

    void push_back(int val)
    {
        m_array.push_back(val);
    }

    int& operator[](int index)
    {
        return m_array[index];
    }

    int size()
    {
        return m_array.size();
    }

    int heapsize()
    {
        return m_heapsize;
    }

    void heapsize(int heapsize)
    {
        m_heapsize = heapsize;
    }

private:
    std::vector<int> m_array;
    int m_heapsize;
};

IntArray::IntArray()
{
}

IntArray::~IntArray()
{
}


void Max_Heapify(IntArray & intarray, int index)
{
    int left_index = LEFT(index);
    int right_index = RIGHT(index);
    int size = intarray.heapsize();
    // check whether out of array.
    int large_index;
    if (left_index < size && intarray[left_index] > intarray[index])
    {
        large_index = left_index;
    }
    else
    {
        large_index = index;
    }
    if (right_index < size && intarray[right_index] > intarray[large_index])
    {
        large_index = right_index;
    }

    if (large_index != index)
    {
        std::swap(intarray[index], intarray[large_index]);
        Max_Heapify(intarray, large_index);
    }
}

void Build_Max_Heap(IntArray & intarray)
{
    int index = intarray.size()/2-1;
       intarray.heapsize(intarray.size());
    for (int i = index; i >= 0; --i)
    {
        Max_Heapify(intarray, i);

    }
}


void HeapSort(IntArray & intarray)
{

    Build_Max_Heap(intarray);

    for (int i = intarray.size() - 1; i >= 0; --i)
    {
        std::swap(intarray[0], intarray[i]);
        intarray.heapsize(intarray.heapsize() - 1);
        Max_Heapify(intarray, 0);
    }
}

int main(int argc, char *argv[])
{
    IntArray arr;
    arr.push_back(16);
    arr.push_back(4);
    arr.push_back(1);
    arr.push_back(8);
    arr.push_back(7);
    arr.push_back(9);
    arr.push_back(3);
    arr.push_back(2);
    arr.push_back(14);
    arr.push_back(10);
    cout << "size is " << arr.size() << endl;

    HeapSort(arr);
    for (int i = 0; i != arr.size(); ++i) {
        cout << arr[i] << endl;
    }
	return 0;
}
```

堆排序的最坏情况时间代价为```nlgn``` ,当输入规模较大时，适宜采用。

