---
layout: post
title: 算法设计-链表
keywords:
  - 数据结构
  - 链表

description: 学习数据结构链表算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
各对象按线性顺序排列，对象的顺序由对象里的指针决定的

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160901_LinkedListDataStructures.PNG)
### 3.伪代码:
```
LIST-SEARCH(L, k)
x = L.head
while x!=NIL and x.key!= k
	x = x.next
return x

LIST-INSERT(L, x)
x.next = L.head
if L.head != NIL
	L.head.prev = x
L.head = x
x.prev = NIL

LIST-DELETE(L, x)
if x.prev != NIL
	x.prev.next = x.next
else
	L.head = x.next
if x.next != NIL
	x.next.prev = x.prev


``` 

### 4.代码片段:
```

#include <stdio.h>
#include <stdlib.h>

struct Node {
	Node(int key) {
		this->key = key;
	}
	int key;
	Node* prev;
	Node* next;
};

struct LinkList {
	LinkList()
	{
		head = NULL;
	}
	Node* head;

};

void PrintList(LinkList* l) {
	Node* tmp = l->head;
	while (tmp != NULL) {
		printf("%d, ", tmp->key);
		tmp = tmp->next;
	}
	printf("\n");
}

void FreeList(LinkList* l) {
	Node* tmp = l->head;
	while (tmp != NULL) {
		Node* delNode = tmp;
		tmp = tmp->next;
		delete delNode;

	}
}

Node* ListSearch(LinkList* l, int k) {
	Node* x = l->head;
	while ((x != NULL) && (x->key) != k)
		x = x->next;
	return x;
}

void ListInsert(LinkList* l, Node* x) {
	x->next = l->head;
	if (l->head != NULL)
		l->head->prev = x;
	l->head = x;
	x->prev = NULL;
}

void ListDelete(LinkList* l, Node* x) {
	if (x->prev != NULL)
		x->prev->next = x->next;
	else
		l->head = x->next;
	if (x->next != NULL)
		x->next->prev = x->prev;

	delete x;
}

int main(void) {

	LinkList l;
	for (int i = 0; i != 5; ++i) {
		ListInsert(&l, new Node(i + 1));
	}
	PrintList(&l);
	Node* node2 = ListSearch(&l, 2);
	printf("key of node2 is [%d]", node2->key);
	FreeList(&l);
	return 0;

}

```
