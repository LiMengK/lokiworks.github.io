---
layout: post
title: java面试题:用队列实现栈
keywords:
  - java
description: 
category: java
tags:
  - java
published: true
---
{% include JB/setup %}

# 题目:用队列实现栈


## 队列实现栈的方式
主要考察出栈的处理，由于队列与栈执行的是相反的操作，所以出栈时首先将队列n-1个元素poll到临时的队列中，使用中间变量保存队列中最后一个元素的值，再将临时队列中的数据交还于原队列。最后返回中间变量。

## 代码示例
**IntStack.java**
```java
package queueStack;

import java.util.PriorityQueue;
import java.util.Queue;

public class IntStack {
	
	public IntStack(){}

	public int pop() {
		int size = queues1.size();
		Queue<Integer> queues2=new PriorityQueue<Integer> ();
		while (size-- > 1) {
			queues2.add(queues1.poll());
		}
		int result = queues1.poll();

		while (!queues2.isEmpty()) {
			queues1.add(queues2.poll());

		}
		return result;
	}

	public void push(int num) {
		queues1.add(num);
	}

	private Queue<Integer> queues1 = new PriorityQueue<Integer> ();

}

```

**Operator.java**
```java
package queueStack;



/*
 * 用队列实现栈
 */

public class QueueStack {
	
public static void main(String[] args) {
	IntStack intStack  = new IntStack();
	
	for(int i = 0; i < 6; i++)
	{
		intStack.push(i);
	}
	int i = 6;
	while (i-->0) {
	
		System.out.println(intStack.pop());
		
	}
}

}

```
