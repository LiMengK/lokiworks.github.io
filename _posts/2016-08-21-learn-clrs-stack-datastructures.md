---
layout: post
title: 算法设计-栈
keywords:
  - 数据结构
  - 栈

description: 学习数据结构栈算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
实现的是一种后进先出(**LIFO**)的策略

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160821_StackDataStructures.PNG)
### 3.伪代码:
```
STACK-EMPTY(S)
if S.top == 0
    return TRUE
else return FALSE

PUSH(S,x)
S.top = S.top + 1
S[S.top] = x

POP(S)
if STACK-EMPTY(S)
    error "underflow"
else S.top = S.top -1
    return S[S.top+1]
``` 

### 4.代码片段:
```
#include <stdio.h>
#include <assert.h>

#define STACK_MAX 100

struct Stack {
	int data[STACK_MAX];
	int top;
};

typedef struct Stack Stack;

void InitStack(Stack *s){
	assert(s != NULL);
	s->top = 0;
}

bool StackEmpty(Stack *s) {
	assert(s != NULL);

	if (s->top == 0) {
		return true;
	}
	return false;
}

void Push(Stack *s, int x) {
	assert(s != NULL);
	s->data[s->top] = x;
	s->top = s->top + 1;
}

int Pop(Stack * s) {
	assert(s != NULL);
	if (StackEmpty(s)) {
		printf("underflow\n");
		return -1;
	}
	s->top = s->top - 1;
	return 	s->data[s->top];
}

int main() {

	Stack s;
	InitStack(&s);
	for (int i = 0; i < 5; ++i) {
		Push(&s, i+1);
	}

	while(!StackEmpty(&s))
	{
		printf("%d, ",Pop(&s));
	}


	return 0;
}

```
