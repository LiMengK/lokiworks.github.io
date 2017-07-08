---
layout: post
title: TCP测速实验
keywords:
  - TCP
description: 
category: TCP
tags:
  - TCP
published: true
---
{% include JB/setup %}

# TCP测速实验
两台测试机器,分别为centos_1(192.168.17.216)、centos_2(192.168.17.215)。centos_1作为客户端向centos_2发送1GB的数据

##测试命令
### centos_1发送数据
```
dd if=/dev/zero bs=1MB count=1000 | nc 192.168.17.215 9002
```
## centos_2接受数据
```
nc -l 9002 > /dev/null
```

##测试结果
```
1000+0 records in
1000+0 records out
1000000000 bytes (1.0 GB) copied, 3.80853 s, 263 MB/s
```
