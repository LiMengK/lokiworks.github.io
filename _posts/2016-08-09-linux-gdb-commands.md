---
layout: post
title: GDB-常用命令集
keywords:
  - GDB
  - 调试
description: 记录GDB常用调试命令
category: Linux
tags:
  - GDB
published: true
---
{% include JB/setup %}

# GDB-常用调试命令

* 调试带参执行文件
```
gdb --args executablename arg1 arg2 arg3
```
或者
```
set args arg1 arg2 arg3
```

* 进入到函数体
```
s
```
* 可视化调试
```
gdb -tui -q
```

