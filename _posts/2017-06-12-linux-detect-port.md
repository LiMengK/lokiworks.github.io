---
layout: post
title: Linux下端口检测
keywords:
  - 端口
description: 
category: Linux
tags:
  - 端口
published: true
---
{% include JB/setup %}

# Linux下检测端口的几种方式

## 使用telnet命令检测
```
telnet baidu.com 80
```
## 使用nmap命令检测
```
nmap baidu.com -p 80
```
## 使用nc命令检测
```
nc -w 5  baidu.com 80 && echo ok
```