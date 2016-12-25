---
layout: post
title: Linux下配置LVS-DR模式
keywords:
  - LVS
description: Linux下配置LVS-DR模式
category: LVS
tags:
  - LVS
published: true
---
{% include JB/setup %}

### 安装环境
* 系统:ubuntu 16.04

* 实验环境:

```
      |
------+--------------------------------------------------------------------
	  |
	  +--------------------------+--------------------------+
	  | 192.168.17.253(VIP)      |                          |
ens33 | 192.168.17.159     ens33 | 192.168.17.157     ens33 | 192.168.17.158
+-----+-----+              +-----+-----+              +-----+-----+ 
| LVS server|              | Backend#1 |              | Backend#2 |   
|           |              | Web Server|              | Web Server|
+-----+-----+              +-----+-----+              +-----+-----+
```

### 安装步骤

* 安装ipvsadm

```
sudo apt-get -y install ipvsadm
```

* 配置VIP

```
ifconfig ens33:0 192.168.17.253 broadcast 192.168.17.253 netmask 255.255.255.255 up
```

* 开启IP转发

```
echo "1" >/proc/sys/net/ipv4/ip_forward
```

* 清除IPVS Table

```
ipvsadm -C
```

* 配置Backend Server IP

```
ipvsadm -A -t 192.168.17.253:80 -s rr -p 600
ipvsadm -a -t 192.168.17.253:80 -r 192.168.17.157:80 -g
ipvsadm -a -t 192.168.17.253:80 -r 192.168.17.158:80 -g
```

#### Backend Server

* 配置VIP

```
ifconfig lo:0 192.168.17.253 netmask 255.255.255.255 broadcast 192.168.17.253
```

* 配置路由

```
route add -host 192.168.17.253 dev lo:0
```

* 屏蔽ARP

```
echo "1" >/proc/sys/net/ipv4/conf/lo/arp_ignore
echo "2" >/proc/sys/net/ipv4/conf/lo/arp_announce
echo "1" >/proc/sys/net/ipv4/conf/all/arp_ignore
echo "2" >/proc/sys/net/ipv4/conf/all/arp_announce
```


### 参考
https://www.server-world.info/en/note?os=Ubuntu_14.04&p=lvs

---

### 配置过程中可能出现问题的解决方法

* 检查IPVS配置是否正确

* 检查IP表配置是否正确

* 检查路由表配置是否正确















