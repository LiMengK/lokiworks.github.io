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
