---
layout: post
title: keepalived的主备切换
keywords:
  - HA
description: 
category: HA
tags:
  - keepalived
published: true
---
{% include JB/setup %}

# keepalived的主备切换
互联网行业一般不允许有单点的系统，至少得是主备的。通常会用keepalived来做ip漂移的工作。下面讲讲如何配置keepalived的主备模式。

## 实验环境
```

        192.168.17.219
              |
      +-------+------+
      |              |
  +---+---+      +---+---+         
  | master|      |salve  |
  +---+---+      +-------+
192.168.17.216  192.168.17.215

```
## 安装配置过程
* 首先下载keepalived，使用的是1.2.9版本,编译并安装keepalived
```
cd /home/test01
wget http://www.keepalived.org/software/keepalived-1.2.9.tar.gz
tar zxf keepalived-1.2.9.tar.gz 
cd keepalived-1.2.9
./configure --prefix=/usr/local/keepalived 
make
make install
```
* 添加到服务启动脚本
```
cp /usr/local/keepalived/etc/rc.d/init.d/keepalived /etc/init.d/keepalived
chmod +x /etc/init.d/keepalived
```
* 修改/etc/init.d/keepalived中的配置内容
```
". /etc/sysconfig/keepalived"替换成". /usr/local/keepalived/etc/sysconfig/keepalived"
```
* 将keepalived主程序添加到环境变量中
```
PATH="$PATH:/usr/local/keepalived/sbin"
export PATH
```
* 修改/usr/local/keepalived/etc/sysconfig/keepalived中的启动参数
```
KEEPALIVED_OPTIONS="-D -f /usr/local/keepalived/etc/keepalived/keepalived.conf"
```
* 设置为开机启动
```
chkconfig keepalived on 
```
至此，keepalived程序的基本安装完成。

## 主备模式的配置
### Master(192.168.17.216)中的配置设置
* 编辑文件
```
vim /usr/local/keepalived/etc/keepalived/keepalived.conf
```

* 配置参数如下
```

! Configuration File for keepalived

global_defs {
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.200.1
   smtp_connect_timeout 30
   router_id VI_1
}
vrrp_script chk_http_port {
        script "</dev/tcp/127.0.0.1/80" #检测本机的80端口
        inerval 1 #单位为秒
        weight -30
 #       fall 2   #不能与weight同时出现,当达到fall次时ko
 #       rise 1   #当达到rise次时ok
}

vrrp_instance VI_1 {
    state MASTER
    interface ens33 #网卡
    virtual_router_id 51 #路由id要一致
    priority 100 #优先级要高于备的
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        192.168.17.219 #虚拟IP
    }

   track_script {
        chk_http_port
    }
}

```
### Salve(192.168.17.215)中的配置设置
* 编辑文件
```
vim /usr/local/keepalived/etc/keepalived/keepalived.conf
```

* 配置参数如下
```

! Configuration File for keepalived

global_defs {
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.200.1
   smtp_connect_timeout 30
   router_id VI_1
}

vrrp_instance VI_1 {
    state BACKUP
    interface ens33 #网卡
    virtual_router_id 51 #路由id要一致
    priority 80
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        192.168.17.219 #虚拟IP
    }
}


```

至此，主备模式就搭建好了，下面来验证是否配置成功。

### 主备模式的验证
* 使用nc模拟web server,在216上启80服务
```
nc -l -k -p 80
```
* 验证80服务是否正常开启，此时应该如下图所示
```
netstat -ntl | awk '{print $4}' | grep ":80$"
```
![cmd-markdown-logo]({{ IMAGE_PATH }}/20170624_ha_1.JPG)

* 分别启动215、216中的keepalived，此时应该如下图所示
```
service keepalived start
```
![cmd-markdown-logo]({{ IMAGE_PATH }}/20170624_ha_2.JPG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20170624_ha_6.JPG)
* 停止80服务
```
ctrl+c
```
![cmd-markdown-logo]({{ IMAGE_PATH }}/20170624_ha_3.JPG)
* 此时应该如下图所示
![cmd-markdown-logo]({{ IMAGE_PATH }}/20170624_ha_4.JPG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20170624_ha_5.JPG)
至此,keepalived的主备模式验证ok。

### 安装配置过程的一些问题
#### 启动时，主备上同时存在vip
需要允许arp转发,因为个人机器的原因，我直接关闭了防火墙
```
systemctl stop firewalld.service #停止firewall

systemctl disable firewalld.service #禁止firewall开机启动
```
#### keepalived启动失败
keepalived程序没有成功添加到path中,修改/etc/init.d/keepalived中的内容，使用绝对路径/etc/init.d/keepalived替代keepalived