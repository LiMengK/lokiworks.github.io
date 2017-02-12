---
layout: post
title: 多线程环境下的Sleep
keywords:
  - Sleep
description: 多线程环境下的Sleep
category: Program
tags:
  - Sleep
published: true
---
{% include JB/setup %}

多线程环境下Sleep的使用

```
void thread_sleep(int second)
{
    // time wait
    timespec outtime;
    pthread_cond_t  cont;
    pthread_mutex_t mutex;

    // timer init
    pthread_mutex_init(&mutex, nullptr);
    pthread_cond_init(&cont, nullptr);

    pthread_mutex_lock(&mutex);
    outtime.tv_sec = time(nullptr) + second;
    outtime.tv_nsec = 0;
    pthread_cond_timedwait(&cont, &mutex, &outtime);
    pthread_mutex_unlock(&mutex);
    
}
```














