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




