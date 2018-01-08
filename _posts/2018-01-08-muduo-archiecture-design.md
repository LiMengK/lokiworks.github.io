---
layout: post
title: Muduo的软件架构设计
keywords:
  - 笔记
description: 
category: 读书笔记
tags:
  - Muduo的软件架构设计
published: true
---
{% include JB/setup %}

# Muduo软件架构设计
## Muduo是什么?
Muduo是陈硕先生设计的一款基于Linux平台下的TCP网络库，基于Reactor 模式，采用基于对象的设计风格，其接口多以function+bind的方式表达
## 类图
![itemContent.gif]({{ IMAGE_PATH }}/20180108_Muduo_arch.gif)
- Channel 是 selectable IO channel，负责注册与响应 IO 事件，它不拥有 file descriptor。它是 Acceptor、Connector、EventLoop、TimerQueue、TcpConnection 的成员，生命期由后者控制。
- Socket 封装一个 file descriptor，并在析构时关闭 fd。它是 Acceptor、TcpConnection 的成员，生命期由后者控制。EventLoop、TimerQueue 也拥有 fd，但是不封装为 Socket。
- SocketsOps 封装各种 sockets 系统调用。
- EventLoop 封装事件循环，也是事件分派的中心。它用 eventfd(2) 来异步唤醒，这有别于传统的用一对 pipe(2) 的办法。它用 TimerQueue 作为计时器管理，用 Poller 作为 IO Multiplexing。
- Poller 是 PollPoller 和 EPollPoller 的基类，采用“电平触发”的语意。它是 EventLoop 的成员，生命期由后者控制。
- PollPoller 和 EPollPoller 封装 poll(2) 和 epoll(4) 两种 IO Multiplexing 后端。Poll 的存在价值是便于调试，因为 poll(2) 调用是上下文无关的，用 strace 很容易知道库的行为是否正确。
- Connector 用于发起 TCP 连接，它是 TcpClient 的成员，生命期由后者控制。
- Acceptor 用于接受 TCP 连接，它是 TcpServer 的成员，生命期由后者控制。
- TimerQueue 用 timerfd 实现定时，这有别于传统的设置 poll/epoll_wait 的等待时长的办法。为了简单起见，目前用链表来管理 Timer，如果有必要可改为优先队列，这样复杂度可从 O(n) 降为O(ln n) （某些操作甚至是 O(1)）。它是 EventLoop 的成员，生命期由后者控制。
- EventLoopThreadPool 用于创建 IO 线程池，也就是说把 TcpConnection 分派到一组运行 EventLoop 的线程上。它是 TcpServer 的成员，生命期由后者控制。

## 线程模型
Muduo 的线程模型符合我主张的 one loop per thread + thread pool 模型。每个线程最多有一个 EventLoop。每个 TcpConnection 必须归某个 EventLoop 管理，所有的 IO 会转移到这个线程，换句话说一个 file descriptor 只能由一个线程读写。TcpConnection 所在的线程由其所属的 EventLoop 决定，这样我们可以很方便地把不同的 TCP 连接放到不同的线程去，也可以把一些 TCP 连接放到一个线程里。TcpConnection 和 EventLoop 是线程安全的，可以跨线程调用。TcpServer 直接支持多线程，它有两种模式：

1. 单线程，accept 与 TcpConnection 用同一个线程做 IO。
1. 多线程，accept 与 EventLoop 在同一个线程，另外创建一个 EventLoopThreadPool，新到的连接会按 round-robin 方式分配到线程池中。
