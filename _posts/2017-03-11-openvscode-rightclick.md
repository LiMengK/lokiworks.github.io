---
layout: post
title: 右键打开Visual Code
keywords:
  - VS
description: 
category: Misc
tags:
  - Misc
published: true
---

# 右键打开VS Code
路径使用的是VS Code默认安装路径，如果改过路径，需要更换路径

```
Windows Registry Editor Version 5.00 
 
; Open files 
[HKEY_CLASSES_ROOT\*\shell\Open with VS Code] 
@="Edit with VS Code" 
"Icon"="C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe,0" 
 
[HKEY_CLASSES_ROOT\*\shell\Open with VS Code\command] 
@="\"C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe\" \"%1\"" 
 
; This will make it appear when you right click ON a folder 
; The "Icon" line can be removed if you don't want the icon to appear 
 
[HKEY_CLASSES_ROOT\Directory\shell\vscode] 
@="Open Folder as VS Code Project" 
"Icon"="\"C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe\",0" 
 
[HKEY_CLASSES_ROOT\Directory\shell\vscode\command] 
@="\"C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe\" \"%1\"" 
 
 
; This will make it appear when you right click INSIDE a folder 
; The "Icon" line can be removed if you don't want the icon to appear 
 
[HKEY_CLASSES_ROOT\Directory\Background\shell\vscode] 
@="Open Folder as VS Code Project" 
"Icon"="\"C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe\",0" 
 
[HKEY_CLASSES_ROOT\Directory\Background\shell\vscode\command] 
@="\"C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe\" \"%V\""
```












