---
layout: post
title: linux c下协程的实现
keywords:
  - coroutine
description: 
category: linux
tags:
  - coroutine
published: true
---
{% include JB/setup %}

linux c 下提供了一组API用于用户层的context切换。
API分别为:
```c
1. int getcontext(ucontext_t *ucp); 用于获取当前活动context
2. void makecontext(ucontext_t *ucp, void(*func)(), int argc, ...); 修改context
3. int swapcontext(ucontext_t * oucp, const ucontext_t *ucp); 将当前的context保存在oucp中，并设置ucp为当前活动的context
```

其中,ucontext_t的结构定义如下:
```c
typedef struct ucontext{
struct ucontext_t *uc_link; 指向下一个需要resumend的context
sigset_t uc_sigmask; 
stack_t uc_stack; context使用的stack
mcontext_t uc_mcontext;保存context使用的机器指令
......
}ucontext_t;
```

通过上述API，可以实现一个简单的协程库。详细实现参见云风的coroutine库:[linked phrase(https://github.com/cloudwu/coroutine)
