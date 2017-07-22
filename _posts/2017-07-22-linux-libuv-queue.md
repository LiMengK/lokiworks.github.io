---
layout: post
title: libuv中队列的实现
keywords:
  - queue
description: 
category: c/c++
tags:
  - queue
published: true
---
{% include JB/setup %}

# libuv中队列的实现
libuv中实现双向链表的代码只有七十多行，非常的简洁。下面主要通过分析源码来学习libuv中队列的实现。

## queue.h的源码
```
/* Copyright (c) 2013, Ben Noordhuis <info@bnoordhuis.nl>
 *
 * Permission to use, copy, modify, and/or distribute this software for any
 * purpose with or without fee is hereby granted, provided that the above
 * copyright notice and this permission notice appear in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 * ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 * ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 * OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */

#ifndef QUEUE_H_
#define QUEUE_H_

#include <stddef.h>

typedef void *QUEUE[2];

/* Private macros. */
#define QUEUE_NEXT(q) (*(QUEUE **)&((*(q))[0]))
#define QUEUE_PREV(q) (*(QUEUE **)&((*(q))[1]))
#define QUEUE_PREV_NEXT(q) (QUEUE_NEXT(QUEUE_PREV(q)))
#define QUEUE_NEXT_PREV(q) (QUEUE_PREV(QUEUE_NEXT(q)))

/* Public macros. */
#define QUEUE_DATA(ptr, type, field)                                           \
  ((type *)((char *)(ptr)-offsetof(type, field)))

/* Important note: mutating the list while QUEUE_FOREACH is
 * iterating over its elements results in undefined behavior.
 */
#define QUEUE_FOREACH(q, h)                                                    \
  for ((q) = QUEUE_NEXT(h); (q) != (h); (q) = QUEUE_NEXT(q))

#define QUEUE_EMPTY(q) ((const QUEUE *)(q) == (const QUEUE *)QUEUE_NEXT(q))

#define QUEUE_HEAD(q) (QUEUE_NEXT(q))

#define QUEUE_INIT(q)                                                          \
  do {                                                                         \
    QUEUE_NEXT(q) = (q);                                                       \
    QUEUE_PREV(q) = (q);                                                       \
  } while (0)

#define QUEUE_ADD(h, n)                                                        \
  do {                                                                         \
    QUEUE_PREV_NEXT(h) = QUEUE_NEXT(n);                                        \
    QUEUE_NEXT_PREV(n) = QUEUE_PREV(h);                                        \
    QUEUE_PREV(h) = QUEUE_PREV(n);                                             \
    QUEUE_PREV_NEXT(h) = (h);                                                  \
  } while (0)

#define QUEUE_SPLIT(h, q, n)                                                   \
  do {                                                                         \
    QUEUE_PREV(n) = QUEUE_PREV(h);                                             \
    QUEUE_PREV_NEXT(n) = (n);                                                  \
    QUEUE_NEXT(n) = (q);                                                       \
    QUEUE_PREV(h) = QUEUE_PREV(q);                                             \
    QUEUE_PREV_NEXT(h) = (h);                                                  \
    QUEUE_PREV(q) = (n);                                                       \
  } while (0)

#define QUEUE_MOVE(h, n)                                                       \
  do {                                                                         \
    if (QUEUE_EMPTY(h))                                                        \
      QUEUE_INIT(n);                                                           \
    else {                                                                     \
      QUEUE *q = QUEUE_HEAD(h);                                                \
      QUEUE_SPLIT(h, q, n);                                                    \
    }                                                                          \
  } while (0)

#define QUEUE_INSERT_HEAD(h, q)                                                \
  do {                                                                         \
    QUEUE_NEXT(q) = QUEUE_NEXT(h);                                             \
    QUEUE_PREV(q) = (h);                                                       \
    QUEUE_NEXT_PREV(q) = (q);                                                  \
    QUEUE_NEXT(h) = (q);                                                       \
  } while (0)

#define QUEUE_INSERT_TAIL(h, q)                                                \
  do {                                                                         \
    QUEUE_NEXT(q) = (h);                                                       \
    QUEUE_PREV(q) = QUEUE_PREV(h);                                             \
    QUEUE_PREV_NEXT(q) = (q);                                                  \
    QUEUE_PREV(h) = (q);                                                       \
  } while (0)

#define QUEUE_REMOVE(q)                                                        \
  do {                                                                         \
    QUEUE_PREV_NEXT(q) = QUEUE_NEXT(q);                                        \
    QUEUE_NEXT_PREV(q) = QUEUE_PREV(q);                                        \
  } while (0)

#endif /* QUEUE_H_ */
#pragma once

```

## 调用示例
```
#include "queue.h"
#include <iostream>

using namespace std;

struct User {
  int age;
  char *name;
  QUEUE node;

  User() : age(0), name(NULL) { QUEUE_INIT(&node); }
};

QUEUE queue;

int main() {

  User user1;
  user1.age = 1;
  user1.name = "ab";

  User user2;
  user2.age = 2;
  user2.name = "cd";

  QUEUE_INIT(&queue);

  QUEUE_INSERT_TAIL(&queue, &user1.node);
  QUEUE_INSERT_TAIL(&queue, &user2.node);

  QUEUE *q = NULL;

  QUEUE_FOREACH(q, &queue) {
    User *pUser = QUEUE_DATA(q, User, node);

    printf("Received rest inserted users: %s who is %d.\n", pUser->name,
           pUser->age);
  }

  return 0;
}


```

## 源码分析
分析源码前先介绍下offsetof及container_of

### offsetof
offset的实现如下
```
#ifdef __cplusplus
    #define offsetof(s,m) ((size_t)&reinterpret_cast<char const volatile&>((((s*)0)->m)))
#else
    #define offset(s,m) ((size_t)&(((s*)0)->m))
```
实现逻辑:在内存起始处(0x00000000)映射一个结构体，结构体成员变量在结构体中的偏移大小，对应该成员变量的内存地址。
![cmd-markdown-logo]({{ IMAGE_PATH }}/offsetof.PNG)

### container_of
```
#define container_of(ptr, type, member) ({                         \
      ((type *)((char *)(ptr)-offsetof(type, member)))
```
实现逻辑:通过成员变量的地址及其在结构体的偏移量计算出结构体的首地址
### queue.h

```
/* Copyright (c) 2013, Ben Noordhuis <info@bnoordhuis.nl>
 *
 * Permission to use, copy, modify, and/or distribute this software for any
 * purpose with or without fee is hereby granted, provided that the above
 * copyright notice and this permission notice appear in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 * ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 * ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 * OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */

#ifndef QUEUE_H_
#define QUEUE_H_

#include <stddef.h>

// 含有两个元素的数组
// 数组中的第一位元素表示双向链表中的next
// 数组中的第二位元素表示双向链表中的prev
typedef void *QUEUE[2];

/*
 双向队列实现的逻辑:
QUEUE queue; //queue的第一位元素用来表示header，永远指向队列中的第一位元素;queue的第二位元素用来表示tailer,永远指向队列中的最后一位元素
队列中的第一位元素的prev指向queue,队列中的最后一位元素的next指向queue
*/


/*
假设节点为q,以下api分表表示:
q->next
q->prev
q->prev->next
q->next->prev

宏对应的函数版本
inline QUEUE **queue_next(QUEUE *q) { return ((QUEUE **)&(*q)[0]); }
inline QUEUE **queue_prev(QUEUE *q) { return ((QUEUE **)&(*q)[1]); }
inline QUEUE **queue_prev_next(QUEUE *q) { return queue_next(*queue_prev(q)); }
inline QUEUE **queue_next_prev(QUEUE *q) { return queue_prev(*queue_next(q)); }

下面对queue_next函数做下动作的分解,以便理解代码
QUEUE **queue_next(QUEUE *q)
{
   void * next = (*q)[0]; // 表示取数组中的第一个元素
   return (QUEUE **)&next; // 将void**类型强转成QUEUE**类型
}

*/
#define QUEUE_NEXT(q) (*(QUEUE **)&((*(q))[0]))
#define QUEUE_PREV(q) (*(QUEUE **)&((*(q))[1]))
#define QUEUE_PREV_NEXT(q) (QUEUE_NEXT(QUEUE_PREV(q)))
#define QUEUE_NEXT_PREV(q) (QUEUE_PREV(QUEUE_NEXT(q)))

// 等同于container_of，用于获取结构体的首地址
#define QUEUE_DATA(ptr, type, field)                                           \
  ((type *)((char *)(ptr)-offsetof(type, field)))

/* Important note: mutating the list while QUEUE_FOREACH is
 * iterating over its elements results in undefined behavior.
 */
// 遍历队列，直到最后一位元素的next指向queue
#define QUEUE_FOREACH(q, h)                                                    \
  for ((q) = QUEUE_NEXT(h); (q) != (h); (q) = QUEUE_NEXT(q))
// q == q->next,只有哨兵本身
#define QUEUE_EMPTY(q) ((const QUEUE *)(q) == (const QUEUE *)QUEUE_NEXT(q))
// 队列的第一个元素
#define QUEUE_HEAD(q) (QUEUE_NEXT(q))
// next和prev指向元素本身
#define QUEUE_INIT(q)                                                          \
  do {                                                                         \
    QUEUE_NEXT(q) = (q);                                                       \
    QUEUE_PREV(q) = (q);                                                       \
  } while (0)

#define QUEUE_ADD(h, n)                                                        \
  do {                                                                         \
    QUEUE_PREV_NEXT(h) = QUEUE_NEXT(n);                                        \
    QUEUE_NEXT_PREV(n) = QUEUE_PREV(h);                                        \
    QUEUE_PREV(h) = QUEUE_PREV(n);                                             \
    QUEUE_PREV_NEXT(h) = (h);                                                  \
  } while (0)

#define QUEUE_SPLIT(h, q, n)                                                   \
  do {                                                                         \
    QUEUE_PREV(n) = QUEUE_PREV(h);                                             \
    QUEUE_PREV_NEXT(n) = (n);                                                  \
    QUEUE_NEXT(n) = (q);                                                       \
    QUEUE_PREV(h) = QUEUE_PREV(q);                                             \
    QUEUE_PREV_NEXT(h) = (h);                                                  \
    QUEUE_PREV(q) = (n);                                                       \
  } while (0)

#define QUEUE_MOVE(h, n)                                                       \
  do {                                                                         \
    if (QUEUE_EMPTY(h))                                                        \
      QUEUE_INIT(n);                                                           \
    else {                                                                     \
      QUEUE *q = QUEUE_HEAD(h);                                                \
      QUEUE_SPLIT(h, q, n);                                                    \
    }                                                                          \
  } while (0)
// 在队列中的第一个元素之前插入元素
#define QUEUE_INSERT_HEAD(h, q)                                                \
  do {                                                                         \
    QUEUE_NEXT(q) = QUEUE_NEXT(h);                                             \
    QUEUE_PREV(q) = (h);                                                       \
    QUEUE_NEXT_PREV(q) = (q);                                                  \
    QUEUE_NEXT(h) = (q);                                                       \
  } while (0)
// 在队列中的最后一个元素之后插入元素
#define QUEUE_INSERT_TAIL(h, q)                                                \
  do {                                                                         \
    QUEUE_NEXT(q) = (h);                                                       \
    QUEUE_PREV(q) = QUEUE_PREV(h);                                             \
    QUEUE_PREV_NEXT(q) = (q);                                                  \
    QUEUE_PREV(h) = (q);                                                       \
  } while (0)

#define QUEUE_REMOVE(q)                                                        \
  do {                                                                         \
    QUEUE_PREV_NEXT(q) = QUEUE_NEXT(q);                                        \
    QUEUE_NEXT_PREV(q) = QUEUE_PREV(q);                                        \
  } while (0)

#endif /* QUEUE_H_ */
#pragma once

```

* 头部插入
![cmd-markdown-logo]({{ IMAGE_PATH }}/insert_head.PNG)
* 尾部插入
![cmd-markdown-logo]({{ IMAGE_PATH }}/insert_tail.PNG)