---
title: Tmux
date: 2019-02-28 17:43:53
tags: 
categories: 
    - 工具
---

**目录 start**
 
1. [Tmux](#tmux)
    1. [键绑定](#键绑定)
        1. [切换](#切换)
    1. [插件](#插件)
        1. [tmux-resurrect](#tmux-resurrect)

**目录 end**|_2019-04-19 15:38_|
****************************************
# Tmux
> [Arch wiki: tmux](https://wiki.archlinux.org/index.php/Tmux_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

> [tmux 入门](http://blog.jobbole.com/87278/) | [tmux简洁教程及config关键配置](https://www.jianshu.com/p/fd3bbdba9dc9)

> [参考博客: 文本三巨头：zsh、tmux 和 vim](http://blog.jobbole.com/86571/)

- 新建会话 `tmux new -s myth`  
- 连接会话 `tmux a -t test`
- 显示所有 `tmux ls` 
- 重新加载配置文件 `tmux source ~/.tmux.conf`

> [自定义配置文件](https://gitee.com/gin9/Configs/blob/master/Linux/tmux/tmux.conf)
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


## 插件
- [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) `查看Readme下载安装`

> [参考博客: 保存和恢复 Tmux 会话 ](https://liam.page/2016/09/10/tmux-plugin-resurrect/)

### tmux-resurrect

> [tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect)

prefix c-s 保存
prefix c-r 加载

