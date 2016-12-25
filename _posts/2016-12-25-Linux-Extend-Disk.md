---
layout: post
title: VMware中扩展Linux的硬盘空间
keywords:
  - Linux
  - 硬盘
description: VMware中扩展Linux的硬盘空间
category: Linux
tags:
  - Linux
published: true
---
{% include JB/setup %}

### VMware中扩展Linux的硬盘空间
最近使用VMware过程中需要扩展CentOS7的硬盘空间,在此记录下操作过程

## 操作步骤
* 1.关闭虚机，使用VMware扩展硬盘容量
![cmd-markdown-logo]({{ IMAGE_PATH }}/20161225_Extend-Disk-01.PNG)
* 2.硬盘分区及格式化
```
fdisk /dev/sda　

p　　　　　　　查看已分区数量（/dev/sda1 /dev/sda2 /dev/sda5） 
n　　　　　　　新增加一个分区 
p　　　　　　　分区类型我们选择为主分区 
　　　　　　   分区号选3（因为1,2已经用过了，见上） 
回车　　　　　 默认（起始扇区） 
回车　　　　　 默认（结束扇区） 
t　　　　　　　修改分区类型 
　　　　　　   选分区3 
8e　　　　　　 修改为LVM（8e就是LVM） 
w　　　　　　  写分区表 
q　　　　　　  完成，退出fdisk命令

```
* 3.添加硬盘分区
```
partprobe 
```
* 4.格式化分区
```
mkfs.ext3 /dev/sda3
```
* 5.添加进LVM组
```
lvm　　　　　　　　　　　　　　　　　　    进入lvm管理
lvm>pvcreate /dev/sda3　　　这是初始化刚才的分区，必须的
lvm>vgextend centos /dev/sda3  将初始化过的分区加入到虚拟卷组centos (卷和卷组的命令可以通过  vgdisplay )
lvm>vgdisplay -v
lvm>lvextend -l+21513 /dev/mapper/centos-root　　扩展已有卷的容量（21513 是通过vgdisplay查看的free的大小）
lvm>pvdisplay   查看卷容量，这时你会看到一个很大的卷了
lvm>quit    　退出
```
* 6.扩容
```
xfs_growfs /dev/mapper/centos-root
```
* 7.查看硬盘空间
```
df -h
```









