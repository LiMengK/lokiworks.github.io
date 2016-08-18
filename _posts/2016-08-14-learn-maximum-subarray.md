---
layout: post
title: 算法设计-查找最大的子数组
keywords:
  - 分治
  - 查找
  - 子数组
description: 学习分治算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}


使用***分治***的思想解决查找最大的子数组的问题

<!--more-->
### 1.原理:
* **分解**:将原问题分解成一系列子问题
* **解决**:递归地解决子问题。若子问题足够小，则直接求解
* **比较**:比较子问题的结果，找出最优的解

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160814_MaxSubarray01.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160814_MaxSubarray02.PNG)
### 3.伪代码:
```
//FIND-MAX-CROSSING-SUBARRAY(A; low; mid; high)
//1 left-sum = min
//2 sum = 0
//3 for i = mid downto low
//4 sum = sum + A[i]
//5 if sum > left-sum
//6 left-sum = sum
//7 max-left = i
//8 right-sum = min
//9 sum = 0
//10 for j = mid + 1 to high
//11 sum = sum + A[j]
//12 if sum > right-sum
//13 right-sum = sum
//14 max-right = j
//15 return (max-left; max-right; left-sum + right-sum)

//FIND-MAXIMUM-SUBARRAY(A; low; high)
//1 if high == low
//2 return (low; high;A[low]) // base case: only one element
//3 else mid = [(low + high)=2]
//4 (left-low; left-high; left-sum) =
//FIND-MAXIMUM-SUBARRAY(A; low; mid)
//5 (right-low; right-high; right-sum) =
//FIND-MAXIMUM-SUBARRAY(A; mid + 1; high)
//6 (cross-low; cross-high; cross-sum) =
//FIND-MAX-CROSSING-SUBARRAY(A; low; mid; high)
//7 if left-sum >= right-sum and left-sum >= cross-sum
//8 return (left-low; left-high; left-sum)
//9 elseif right-sum >= left-sum and right-sum >= cross-sum
//10 return (right-low; right-high; right-sum)
//11 else return (cross-low; cross-high; cross-sum)

// example:
//        input:{13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, -7}
//        output:{18,20,-7,12}
``` 

### 4.代码片段:
```
#include <iostream>
#include <limits>
#include <assert.h>

using namespace std;

std::tuple<int, int, int> find_max_crossing_subarray(int *arr, int low,
		int mid, int high)
{
	int left_sum = std::numeric_limits<int>::min();
	int sum = 0;
	int max_left;
	for (int i = mid; i >= low; --i)
	{
		sum = sum + arr[i];
		if (sum > left_sum)
		{
			left_sum = sum;
			max_left = i;
		}
	}

	int right_sum = std::numeric_limits<int>::min();
	sum = 0; // reset it to 0

	int max_right;
	for (int i = mid + 1; i <= high; ++i)
	{
		sum = sum + arr[i];
		if (sum > right_sum)
		{
			right_sum = sum;
			max_right = i;
		}
	}

	return std::make_tuple(max_left, max_right, left_sum + right_sum);
}

std::tuple<int, int, int> find_maximum_subarray(int *arr, int low, int high)
{
	if (high == low)
	{
		return std::make_tuple(low, high, arr[low]);
	}
	else
	{
		int mid = (high + low) / 2;
		std::tuple<int, int, int> left_result = find_maximum_subarray(arr, low,
				mid);
		std::tuple<int, int, int> right_result = find_maximum_subarray(arr,
				mid + 1, high);
		std::tuple<int, int, int> cross_result = find_max_crossing_subarray(
				arr, low, mid, high);
		if (std::get<2>(left_result) >= std::get<2>(right_result)
				&& std::get<2>(left_result) >= std::get<2>(cross_result))
		{
			return left_result;
		}
		else if (std::get<2>(right_result) >= std::get<2>(left_result)
				&& std::get<2>(right_result) >= std::get<2>(cross_result))
		{
			return right_result;
		}
		else
		{
			return cross_result;
		}
	}

}

int main()
{
	int arr[] = {13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, -7};
	int arr_length = sizeof(arr) / sizeof(arr[0]);
	cout << "input array is :{ ";

	for (int i = 0; i < arr_length-1; ++i) {
		cout << arr[i] << ",";
	}
	cout << arr[arr_length-1] << " }." << endl;

	std::tuple<int, int, int> result = find_maximum_subarray(arr, 0, arr_length-1);

	cout << "index of left side is : " << std::get<0>(result) << endl;
	cout << "index of right side is : " << std::get<1>(result) << endl;
	cout << "sum of numbers is : " << std::get<2>(result) << endl;

	return 0;
}

```
