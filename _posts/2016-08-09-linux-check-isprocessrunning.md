---
layout: post
title: Linux下检测进程是否已运行
keywords:
	- Programming
description: 检测当前只有一个进程在运行
category: Linux
tags:
  - Programming
published: true
---
{% include JB/setup %}

# Linux下检测当前只有一进程实例在运行
## 基本原理
Linux下/proc目录记录了当前所有正在运行的进程实例的PID, 使用cmdline查找出当前进程的完整命令,给定的进程名称与查找出的命令进行一一比对，如果找到则认为进程已运行，否则认为该进程尚未启动
## 代码示例
```
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <dirent.h>
#include <sys/types.h>

pid_t proc_find(const char* name) 
{
    DIR* dir;
    struct dirent* ent;
    char* endptr;
    char buf[512];

    if (!(dir = opendir("/proc"))) {
        perror("can't open /proc");
        return -1;
    }

    while((ent = readdir(dir)) != NULL) {
        /* if endptr is not a null character, the directory is not
         * entirely numeric, so ignore it */
        long lpid = strtol(ent->d_name, &endptr, 10);
        if (*endptr != '\0') {
            continue;
        }

        /* try to open the cmdline file */
        snprintf(buf, sizeof(buf), "/proc/%ld/cmdline", lpid);
        FILE* fp = fopen(buf, "r");

        if (fp) {
            if (fgets(buf, sizeof(buf), fp) != NULL) {
                /* check the first token in the file, the program name */
                char* first = strtok(buf, " ");
                if (!strcmp(first, name)) {
                    fclose(fp);
                    closedir(dir);
                    return (pid_t)lpid;
                }
            }
            fclose(fp);
        }

    }

    closedir(dir);
    return -1;
}


int main(int argc, char* argv[]) 
{
    if (argc == 1) {
        fprintf("usage: %s name1 name2 ...\n", argv[0]);
        return 1;
    }

    int i;
    for(int i = 1; i < argc; ++i) {
        pid_t pid = proc_find(argv[i]);
        if (pid == -1) {
            printf("%s: not found\n", argv[i]);
        } else {
            printf("%s: %d\n", argv[i], pid);
        }
    }

    return 0;
}
```





