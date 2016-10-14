---
layout: post
title: DOS2Unix编码问题
keywords:
  - Process

description: DOS2Unix编码问题
category: Share
tags:
  - Encode
published: true
---
{% include JB/setup %}



<!--more-->
# DOS2Unix编码问题
在windows下文本工具编写的脚本，在Linux报错**/bin/sh^M: bad interpreter: No such file or directory**,需要
在linux下使用vim打开文件，设置文件风格为unix,**:set fileformat=unix**最后保存文件。再重新执行脚本，就ok了。






