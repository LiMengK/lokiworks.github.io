---
layout: post
title: 算法设计-队列
keywords:
  - 数据结构
  - 队列

description: 学习数据结构队列算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
实现的是一种先进先出(**FIFO**)的策略

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160821_QueueDataStructures.PNG)
### 3.伪代码:
```
ENQUEUE(Q,x)
Q[Q.tail] = x
if Q.tail = Q.length
	Q.tail = 1
else
	Q.tail = Q.tail + 1

DEQUEUE(Q)
x = Q[Q.head]
if Q.head == Q.length
	Q.head = 1
else
	Q.head = Q.head + 1
return x
``` 

### 4.代码片段:
```
#include <stdio.h>
#include <assert.h>


#define QUEUE_MAX 100

struct Queue {
	int data[QUEUE_MAX];
	int length;
	int head;
	int tail;
};

typedef struct Queue Queue;

void InitQueue(Queue * q){
assert(q != NULL);
 q->head = q->tail = 0;
 q->length = QUEUE_MAX;

}

void Enqueue(Queue *q, int x)
{
	assert(q != NULL);
	q->data[q->tail] = x;
	if(q->tail == q->length-1)
		q->tail = 0;
	else
		q->tail += 1;
}


int Dequeue(Queue *q)
{
	assert(q != NULL);
	int x = q->data[q->head];
	if (q->head == q->length-1) {
		q->head = 0;

	}else
		q->head +=1;
	return x;
}


int main() {
	Queue q;
	InitQueue(&q);
	for (int i = 0; i < 5; ++i) {
		Enqueue(&q, i+1);
	}

	for (int i = 0; i < 5; ++i) {
		printf("%d, ", Dequeue(&q));
	}

	return 0;
}

```
