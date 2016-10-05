---
layout: post
title: MySQL开启远程连接
keywords:
  - XShell

description: MySQL开启远程连接
category: Linux
tags:
  - Linux
published: true
---
{% include JB/setup %}



<!--more-->
## MySQL开启远程连接
### 1.修改配置 
* vim /etc/mysql/my.cnf
* 添加注释
  * #bind-address           = 127.0.0.1
  * #skip-networking
### 2.重启服务
* service mysql restart
### 3.修改表
* mysql> GRANT ALL PRIVILEGES ON *.* TO 'USERNAME'@'%' IDENTIFIED BY 'PASSWORD' WITH GRANT OPTION;
### 4.刷新表
* mysql> FLUSH PRIVILEGES;

