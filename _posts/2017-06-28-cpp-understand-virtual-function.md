---
layout: post
title: 理解c++中虚函数的两个例子
keywords:
  - cpp
description: 
category: c/c++
tags:
  - 虚函数
published: true
---
{% include JB/setup %}

# 理解c++中虚函数的两个例子

## 例1
```
#include<iostream>
using namespace std;
class Base {
public:
	virtual void f() { cout << "Base::f" << endl; }
};

class Base2
{
public:
	virtual void g() { cout << "Base2::g" << endl; }
};


class Derived2 :public Base, Base2
{
public:
	virtual void g() { cout << "Derived2::g" << endl; }
};



int main()
{
	Base2*b2 = (Base2*)new Derived2();
	Base *d2 = (Base *)b2;
	d2->f();
	return 0;
}
``` 
## 例2
```
#include<iostream>
#include  <stdint.h>
using namespace std;
class Base {
public:
	virtual void f() { cout << "Base::f" << endl; }
	virtual void g() { cout << "Base::g" << endl; }
	virtual void h() { cout << "Base::h" << endl; }
};


int main()
{
	typedef void(*Fun)();

	Base b;
	Base *bp2 = &b;
	Fun pFun = NULL;

	for (int i = 0; i < 3; i++)
	{
		pFun = (Fun)*((intptr_t*)*(intptr_t*)&b + i);
		pFun();
	}
	return 0;
}

```

以上两个例子，在vc14.0和gcc 4.4.6下编译通过。如果能理解上面的两个例子，基本算是理解了c++中的虚函数。

