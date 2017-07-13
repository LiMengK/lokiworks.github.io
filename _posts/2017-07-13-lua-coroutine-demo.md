---
layout: post
title: 理解LUA中协程的一些例子
keywords:
  - coroutine
description: 
category: LUA
tags:
  - LUA
published: true
---
{% include JB/setup %}

# 理解LUA中协程的一些例子

## 例1
```
co = coroutine.create(function(value1, value2)
    local tempval3 = 10
    print("coroutine section 1", value1, value2, tempval3)
    local tempvar1, tempvar2 = coroutine.yield(value1+1, value2+1)
    print("coroutine section 2", tempvar1, tempvar2)
    return "end"
  end)

print("main", coroutine.resume(co, 3,2))
print("main", coroutine.resume(co, 12,14))
print("main", coroutine.resume(co, 13,7))

```
