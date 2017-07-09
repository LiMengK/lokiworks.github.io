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


## 测试命令

### centos_1发送10GB数据
```
dd if=/dev/zero bs=1MB count=10000 | nc 192.168.17.215 9002
```
### centos_2接受数据并显示带宽
```
nc -l 9002|pv -W >/dev/null
```

## 测试结果
```
10000+0 records in
10000+0 records out
10000000000 bytes (10 GB) copied, 39.5666 s, 253 MB/s

```
