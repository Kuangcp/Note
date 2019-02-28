---
title: Tmux.md
date: 2019-02-28 17:43:53
tags: 
categories: 
---

**目录 start**
 
1. [Tmux](#tmux)
    1. [键绑定](#键绑定)
        1. [切换](#切换)

**目录 end**|_2019-02-28 17:43_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Tmux
> 好用的管理会话的软件 [arch wiki: tmux](https://wiki.archlinux.org/index.php/Tmux_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

> [tmux 入门](http://blog.jobbole.com/87278/) | [tmux简洁教程及config关键配置](https://www.jianshu.com/p/fd3bbdba9dc9)

> [自定义配置文件](https://gitee.com/gin9/Configs/blob/master/Linux/tmux/tmux.conf)

- 新建会话 `tmux new -s myth`  
- 连接会话 `tmux a -t test`
- 显示所有 `tmux ls` 

*************

> 开启鼠标选择与复制
```conf
    set -g mouse on
```
按住Shift即可照常使用鼠标选中文本
*************

## 键绑定
> prefix 默认是 C-b 也就是 Ctrl b

### 切换
- prefix w 切换 panel 或者 window


