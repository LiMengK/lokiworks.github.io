---
published: false
---
## Linux下安装Nginx
描述Linux下使用Nginx源码，编译、安装Nginx

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




