---
layout: post
title: Windows下通过端口号杀死进程
keywords:
  - Process

description: Windows下通过端口号杀死进程
category: Share
tags:
  - Cmd
published: true
---
{% include JB/setup %}



<!--more-->
# Windows下通过端口号杀死进程
* 输入命令**netstat -a -o -n**查找端口所对应的进程号
* 输入命令**taskkill /F /PID 28344**杀死进程(28344,表示进程号)



