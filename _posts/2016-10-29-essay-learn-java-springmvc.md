---
layout: post
title: 随笔-学习Java中Web开发框架SpringMVC
keywords:
  - JavaWeb

description: 随笔-学习Java中Web开发框架SpringMVC
category: Essay
tags:
  - Web
published: true
---
{% include JB/setup %}



<!--more-->
&emsp;&emsp;学习Web开发的缘由，部门内部使用的一款Portal需要整合进公司的云商城里，需要在原来的基础上做一些开发。
组内暂时没有做Web开发的人，领导安排了我来接手。来着任务及学习Web开发的目的，在网上找一了简易的javaweb
的项目，这个项目使用了**SpringMVC**+**Mybatis**+**redis**+**mysql**,使用Maven做项目管理。之所以选
这个项目，是因为该项目与我手上的Portal架构基本吻合。然后就是要跑通这个项目了。对我而言，学习另一门语言
或技术，首先需要克服工具关，需要知道哪些事是可以由工具完成的，平台下都有哪些工具,工具能胜任的事，就尽量
使用工具。刚开始使用的是eclipse,然后在同事的建议下换成了**STS**(集成了JavaWeb开发中多数的插件)，配置
了一些模板及代码检测工具(**CheckStyle**、**FindBugs**、**PMD**、**TestNG**)使用工具的过程中遇到了些
奇葩的问题，还好问题一一解决。项目跑通后，就照着写了一遍，准备跑自己写的程序的时候，一个又一个问题出现了。
修改Maven的POM文件，是需要**Update Project**的。需要了解项目中使用的JVM及Server版本，使用不同的版本可
能出错。需要正确的使用Spring的注解,不能漏写，信息也不能填错。我写的程序中有一处少加了Controller注解，
结果排查了一天。掌握一门语言或技术不仅仅是会它的语法或用法，还要能诊断由它引起的一系列问题。前者不难，后
者是需要时间与项目的积累及知识的沉淀。

----

## 项目地址
<https://github.com/lokiworks/javaweb/tree/master/project/springmvc/springmvc_Demo01/>






