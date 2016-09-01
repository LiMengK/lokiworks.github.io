---
layout: post
title: 算法设计-哈希表
keywords:
  - 数据结构
  - 哈希表

description: 学习数据结构哈希表算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
利用哈希函数计算出元素所在槽的位置,映射的过程中可能会产生冲突(多个元素映射到同一个槽中),通常用链表法(**chaining**)或开放寻址法(**open addressing**)来解决冲突

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160901_HashtablesDataStructures01.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160901_HashtablesDataStructures02.PNG)
### 3.伪代码:
```
//Open addressing
//@{{
HASH-INSERT(T, k)
i = 0
repeat
	j = h(k, i)
	if T[j] == NIL
		T[j] = k
	    return j
	else
		i = i + 1
until i == m
error "hash table overflow"

HASH-SEARCH(T, k)
i = 0
repeat
	j = h(k, i)
	if T[j] == k
		return j
	i = i + 1
until T[j] == NIL or i == m
return NIL

//@}}


``` 

### 4.代码片段:
* 链表法
```
// LinkedList.h
#include <iostream>
#include <string>
using namespace std;

struct Item
{
string key;
Item * next;
};


class LinkedList {
public:
	LinkedList();
	virtual ~LinkedList();

	void InsertItem(Item* newItem);

	bool RemoveItem(string itemKey);

	Item* GetItem(string itemKey);

	void PrintList();

	int GetLength(){return length;}


private:
	Item* head;
	int length;

};

// LinkedList.cpp
#include "LinkedList.h"

LinkedList::LinkedList() {
	// TODO Auto-generated constructor stub
	head = new Item;
	head->next = NULL;
	length = 0;

}

LinkedList::~LinkedList() {
	// TODO Auto-generated destructor stub
	Item * p = head;
	Item * q = head;

	while(q)
	{
		p = q;
		q = p->next;
		if(p)
		{
			delete p;
		}
	}
}

void LinkedList::InsertItem(Item* newItem) {
	if (!head->next) {
		head->next = newItem;
		++length;
		return;
	}

	Item * p = head;
	Item * q = head;

	while (q) {
		p = q;
		q = p->next;
	}
	p->next = newItem;
	newItem->next = NULL;
	++length;
}

bool LinkedList::RemoveItem(string itemKey) {
	if (!head->next)
		return false;

	Item* p = head;
	Item * q = head;
	while (q) {
		if (q->key == itemKey) {
			p->next = q->next;
			delete q;
			--length;
			return true;
		}

		p = q;
		q = p->next;
	}

	return false;
}

Item* LinkedList::GetItem(string itemKey) {

	Item * p = head;
	Item * q = head;
	while(q)
	{
		p = q;
		if((p != head) && (p->key == itemKey))
			return p;
		q = p->next;

	}

	return NULL;

}

void LinkedList::PrintList() {
	if(length == 0)
	{
		cout << "\n{ }\n";
		return ;
	}
	Item * p = head;
	Item * q = head;

	cout << "\n{ ";
	while(q)
	{
		p = q;
		if(p != head)
		{
			cout << p->key;
			if(p->next) cout << ", ";
			else cout << " ";
		}
		q = p->next;
	}
	cout << "}\n";
}

// HashTable.h

#include "LinkedList.h"

class HashTable {
public:

	~HashTable();

	HashTable(int tablelength = 20);

	void InsertItem(Item* newItem);

	bool RemoveItem(string itemKey);

	Item* GetItemByKey(string itemKey);

	void PrintTable();

	void PrintHistogram();

	int GetLength();

	int GetNumberOfItems();

private:
	LinkedList * array;
	int length;
	int hash(string itemKey);
};

// HashTable.cpp

#include "HashTable.h"



HashTable::~HashTable() {
	// TODO Auto-generated destructor stub
	delete[] array;
}

HashTable::HashTable(int tablelength) {
	if (tablelength <= 0)
		tablelength = 20;
	array = new LinkedList[tablelength];

	length = tablelength;
}

void HashTable::InsertItem(Item* newItem) {
	int index = hash(newItem->key);
	array[index].InsertItem(newItem);
}

bool HashTable::RemoveItem(string itemKey) {
	int index = hash(itemKey);
	return array[index].RemoveItem(itemKey);
}

Item* HashTable::GetItemByKey(string itemKey) {
	int index = hash(itemKey);
	return array[index].GetItem(itemKey);
}

void HashTable::PrintTable() {
	cout << "\n\nHash Table:\n";
	for (int i = 0; i < length; ++i) {
		cout << "Bucket " << i + 1 << ": ";
		array[i].PrintList();
	}
}

void HashTable::PrintHistogram() {
	cout << "\n\nHash Table Contains ";
	cout << GetNumberOfItems() << " Items total\n";

	for (int i = 0; i < length; ++i) {
		cout << i + 1 << ":\t";
		for (int j = 0; j < array[i].GetLength(); ++j) {
			cout << "X";
		}
		cout << "\n";
	}
}

int HashTable::GetLength() {
	return length;
}

int HashTable::GetNumberOfItems() {
	int itemCount = 0;
	for (int i = 0; i < length; ++i) {
		itemCount += array[i].GetLength();
	}
	return itemCount;
}

int HashTable::hash(string itemKey) {
	int value = 0;
	for (int i = 0; i < itemKey.length(); ++i) {
		value += itemKey[i];
	}

	return (value * itemKey.length()) % length;
}

// main.cpp

#include "HashTable.h"

int main(void) {
	Item * A = new Item { "Apple", NULL };
	Item * B = new Item { "Banana", NULL };
	Item * C = new Item { "Caterpillar", NULL };
	Item * D = new Item { "Dog", NULL };
	Item * E = new Item { "Elephant", NULL };
	Item * F = new Item { "Fedora", NULL };
	Item * G = new Item { "Goosebumps", NULL };
	Item * H = new Item { "House", NULL };
	Item * I = new Item { "Insects", NULL };
	Item * J = new Item { "Jam", NULL };
	Item * K = new Item { "Kite", NULL };
	Item * L = new Item { "Limestone", NULL };
	Item * M = new Item { "Mountaineering", NULL };
	Item * N = new Item { "Night", NULL };
	Item * O = new Item { "Open Sesame", NULL };
	Item * P = new Item { "Potatoes", NULL };
	Item * Q = new Item { "Quantum Mechanics", NULL };
	Item * R = new Item { "Rrrrrrrrrrawr", NULL };
	Item * S = new Item { "Snakes", NULL };
	Item * T = new Item { "Tizzy Tube", NULL };
	Item * U = new Item { "Underworld", NULL };
	Item * V = new Item { "Volcanic Ash", NULL };
	Item * W = new Item { "Who When What Why", NULL };
	Item * X = new Item { "XXX", NULL };
	Item * Y = new Item { "Yellow", NULL };
	Item * Z = new Item { "Zest of Lemon", NULL };

	HashTable table;

	table.InsertItem(A);
	table.InsertItem(B);
	table.InsertItem(C);
	table.PrintTable();
	table.PrintHistogram();

	table.RemoveItem("Apple");
	table.PrintTable();
	table.PrintHistogram();

	table.InsertItem(D);
	table.InsertItem(E);
	table.InsertItem(F);
	table.InsertItem(G);
	table.InsertItem(H);
	table.InsertItem(I);
	table.InsertItem(J);
	table.InsertItem(K);
	table.InsertItem(L);
	table.InsertItem(M);
	table.InsertItem(N);
	table.InsertItem(O);
	table.InsertItem(P);
	table.InsertItem(Q);
	table.InsertItem(R);
	table.InsertItem(S);
	table.InsertItem(T);
	table.InsertItem(U);
	table.InsertItem(V);
	table.InsertItem(W);
	table.InsertItem(X);
	table.InsertItem(Y);
	table.InsertItem(Z);
	table.PrintTable();
	table.PrintHistogram();

    Item * result = table.GetItemByKey("Snakes");
    cout << result-> key << endl;

}

```

* 开放寻址法
```
#include <iostream>
#include <string>
using namespace std;

struct Entry {
	bool isUsed;
	string value;
};

unsigned int hashString(const string & s) {
	unsigned int h = 0;
	for (size_t i = 0; i < s.length(); ++i) {
		h += s[i];
	}
	return h;
}

const int TABLE_SIZE = 256;

class HashSet {
public:
	HashSet() {
		for (int i = 0; i < TABLE_SIZE; ++i) {
			entries[i].isUsed = false;
		}
	}

	Entry* Lookup(const string & value) {
		unsigned int hash = hashString(value);
		unsigned int offset = hash % TABLE_SIZE;
		unsigned int step = (hash / TABLE_SIZE) % TABLE_SIZE;

		step |= 1;

		for(int i = 0; i < TABLE_SIZE; ++i)
		{
			Entry * e = &entries[offset];
			if(!e->isUsed)
				return e;
			if(e->value == value)
				return e;
			offset = (offset + (i+1)*step) %TABLE_SIZE;
		}

		return NULL;
	}

	bool Contains(const string & value)
	{
		Entry * entry = Lookup(value);
		return entry!=NULL && entry->isUsed;

	}

	void Add(const string & value)
	{
		Entry * entry = Lookup(value);
		if(entry != NULL && !entry->isUsed)
		{
			entry->isUsed = true;
			entry->value = value;
		}
	}

private:
	Entry entries[TABLE_SIZE];
};

int main() {
	HashSet hashset;
	hashset.Add("Apple");
	hashset.Add("Banana");
	hashset.Add("Caterpillar");
	hashset.Add("Dog");
	hashset.Add("goD");

	Entry* goD = hashset.Lookup("goD");
	cout << "the value of goD is " << goD->value << endl;

	Entry* Dog = hashset.Lookup("Dog");
	cout << "the value of Dog is " << Dog->value << endl;


	return 0;
}

```

### 5.构建**Makefile**
```

INC_DIR = ./include
vpath %.cpp ./src

CXXFLAGS =	-O2 -g -Wall -fmessage-length=0 -I$(INC_DIR)

CXX = g++

OBJS =		HashTable.o LinkedList.o main.o 

LIBS =

TARGET =	hashtable

$(TARGET):	$(OBJS)
	$(CXX) -o $(TARGET) $(OBJS) $(LIBS)

all:	$(TARGET)

clean:
	rm -f $(OBJS) $(TARGET)

```


