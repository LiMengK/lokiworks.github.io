---
layout: post
title: XShell无法连接ubuntu问题
keywords:
  - XShell

description: XShell无法连接ubuntu问题
category: Linux常见操作
tags:
  - Linux
published: true
---
{% include JB/setup %}



<!--more-->
## XShell无法连接ubuntu问题
* 检测是否安装SSH服务,如果没有则安装服务**sudo apt-get install openssh-server**
* 检测是否启用SSH服务,如果没有则启用服务**sudo /etc/init.d/ssh restart**
