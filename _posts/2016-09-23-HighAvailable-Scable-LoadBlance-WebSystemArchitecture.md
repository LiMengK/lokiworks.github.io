---
layout: post
title: Linux下高可用及负载均衡的系统架构
keywords:
  - 高可用
  - 负载均衡
description: 描述Linux下高可用及负载均衡的系统架构
category: Linux
tags:
  - Architecture
published: true
---
{% include JB/setup %}

# Linux下高可用及负载均衡的系统架构
## 常用的软件配置
* LVS 全称为Linux Virtual Server,工作在七层网络架构的第4层(网络层 TCP/UDP协议)，用于服务器的负载均衡，挑选最合适的一台服务器，将客户端的请求转发给它处理，实现客户端到真实服务端的透明转发。本身不做任何业务的处理。对外提供的是一个虚拟IP(VIP,并不是真实物理机的IP)，一般需要配合keepAlived一起使用。
* KeepAlived 类似于心跳检测(heartBeat),检测真实主机的健康状况
* Nginex(Tengine) 工作在七层网络架构的第7层(应用层 HTTP协议), 高性能的HTTP服务器，提供反向代理及负载均衡
* ATS 全称为Apache traffic server, 高性能的缓存服务器,提供反向代理及负载均衡
* Bind9 Linux下的一款DNS服务器(下图中省略),一般会在其配置中绑定N个IP(这里的IP就是LVS中的VIP),对外提供的接口就是域名

### 示例图
![cmd-markdown-logo]({{ IMAGE_PATH }}/高可用的软件架构.jpg)







