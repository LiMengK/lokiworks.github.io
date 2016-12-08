---
layout: post
title: Linux下安装Nginx
keywords:
  - Nginx
description: Linux下使用Nginx源码，编译、安装Nginx
category: Nginx
tags:
  - Nginx
published: true
---
{% include JB/setup %}

### 安装环境
  系统:ubuntu 16.04
  编译器:GCC 5.4.0

### 安装Nginx依赖库
* PCRE库 -为Nginx的Core和Rewrite模块提供正则支持

```
$ wget ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.39.tar.gz
$ tar -zxf pcre-8.39.tar.gz
$ cd pcre-8.39
$ ./configure
$ make
$ sudo make install
```

* zlib库-为Nginx的Gzip模块提供头压缩的支持

```
$ wget http://zlib.net/zlib-1.2.8.tar.gz
$ tar -zxf zlib-1.2.8.tar.gz
$ cd zlib-1.2.8
$ ./configure
$ make
$ sudo make install
```

* OpenSSL库-为Nginx的SSL模块提供HTTPS协议的支持

```
$ wget http://www.openssl.org/source/openssl-1.0.2f.tar.gz
$ tar -zxf openssl-1.0.2f.tar.gz
$ cd openssl-1.0.2f
$ ./configure darwin64-x86_64-cc --prefix=/usr
$ make
$ sudo make install
```

### 下载Nginx源码
这里使用的是nginx-0.1.13的版本

```
$ wget http://nginx.org/download/nginx-0.1.13.tar.gz
$ tar -zxf nginx-1.11.6.tar.gz
$ cd nginx-1.11.6
```

### 配置Build选项
使用 ./configure脚本生成Makefile文件

```
$ ./configure  --with-ld-opt="-lm -ldl" --sbin-path=/usr/local/nginx/nginx --conf-path=/usr/local/nginx/nginx.conf --pid-path=/usr/local/nginx/nginx.pid --with-pcre=../pcre-8.39 --with-zlib=../zlib-1.2.8 --with-http_ssl_module --with-debug --with-cc-opt='-O0 -g' --with-md5=../openssl-1.0.2f --with-openssl=../openssl-1.0.2f 
```

### 编译安装
* 编译

```
$ make
$ sudo make install
```
* 安装

```
$ sudo nginx
```

### 参考
https://www.nginx.com/resources/admin-guide/installing-nginx-open-source/

---


### 编译安装过程中可能会出现的一些问题

* 编译
	1. 报IOV_MAX的错误
    解决:在src/core/ngx_config.h文件中添加如下指令
    
    ```
    	#ifndef IOV_MAX
		#define IOV_MAX   1024
		#endif
    ```
    	2. 报[-Werror=XXX]的错误
    解决:修改objs下的Makefile文件,修改如下
    
    ```
    CFLAGS =  -pipe   -W -Wall -O0 -g

    ```
* 链接
	1.报/openssl-1.0.2f/libcrypto.a(dso_dlfcn.o): In function `dlfcn_globallookup':dso_dlfcn.c文件中的相关函数的未定义的引用
    解决:修改objs下的Makefile文件,在$(LINK) -o 处将 -lm -ldl从开头处放到尾部,修改如下
    
    ```
	../pcre-8.39/.libs/libpcre.a ../openssl-1.0.2f/libssl.a ../openssl-1.0.2f/libcrypto.a ../zlib-1.2.8/libz.a -lm -ldl
	

    ```
* 安装
	1.报open() "/usr/local/nginx/conf/mime.types"的错误
    解决:在/usr/local/nginx/创建conf文件夹，并将mime.types拷贝到该文件夹下,命令如下
    
    ```
    sudo cp mime.types ./conf/

    ```


















