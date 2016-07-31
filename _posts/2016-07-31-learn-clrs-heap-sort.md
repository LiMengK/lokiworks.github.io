---
published: false
---
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
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160729_MergeSort.JPG)

### 3.伪代码: