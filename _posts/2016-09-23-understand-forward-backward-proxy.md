---
layout: post
title: 前向代理与反向代理
keywords:
  - 前向代理
  - 反向代理
description: 什么是前向代理与反向代理
category: Linux
tags:
  - Architecture
published: true
---
{% include JB/setup %}

## 理解前向代理与反向代理

# 正向代理
* proxy和client同属一个LAN，对server透明

# 反向代理
* proxy和server同属一个LAN，对client透明。

# 图示
![cmd-markdown-logo]({{ IMAGE_PATH }}/正向代理与反向代理.png)

```
实际上proxy在两种代理中做的事都是代为收发请求和响应，不过从结构上来看正好左右互换了下，所以把后出现的那种代理方式叫成了反向代理。
```





