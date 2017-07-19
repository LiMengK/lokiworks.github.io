---
layout: post
title: makefile中常用命令
keywords:
  - makefile
description: 
category: linux
tags:
  - linux
published: true
---
{% include JB/setup %}

# makefile中常用命令

## 自动变量
```
all: library.cpp main.cpp
```
**In this case**:

* $@ evaluates to all
* $< evaluates to library.cpp
* $^ evaluates to library.cpp main.cpp



## 参考
[GNU Make manual](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html#Automatic-Variables)
