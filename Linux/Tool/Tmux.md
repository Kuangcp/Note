---
title: Tmux
date: 2019-02-28 17:43:53
tags: 
categories: 
    - 工具
---

**目录 start**
 
1. [Tmux](#tmux)
    1. [配置](#配置)
    1. [键绑定](#键绑定)
        1. [切换](#切换)
    1. [TPM插件管理](#tpm插件管理)
        1. [tmux-resurrect](#tmux-resurrect)
        1. [maglev](#maglev)
        1. [copycat](#copycat)

**目录 end**|_2019-08-25 12:31_|
****************************************
# Tmux
> [Arch wiki: tmux](https://wiki.archlinux.org/index.php/Tmux_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

> [tmux 入门](http://blog.jobbole.com/87278/) | [tmux简洁教程及config关键配置](https://www.jianshu.com/p/fd3bbdba9dc9)

> [参考博客: 文本三巨头：zsh、tmux 和 vim](http://blog.jobbole.com/86571/)
> [参考博客: 程序员高效技巧系列](http://cenalulu.github.io/linux/professional-tmux-skills/)  

************************
> 基本操作

- 新建会话 `tmux new -s myth`  
- 连接会话 `tmux a -t test`
- 显示所有 `tmux ls` 
- 重新加载配置文件 `tmux source ~/.tmux.conf`

*************

## 配置
> [个人Tmux配置文件](https://gitee.com/gin9/Configs/blob/master/Linux/tmux/tmux.conf) 

1. `ln -s $(pwd)/tmux.conf ~/.tmux.conf` 
1. `git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm`
1. `tmux source ~/.tmux.conf`
1. `Ctrl A, I` 等待插件安装完成

*******************

> 开启鼠标选择与复制
```conf
    set -g mouse on
```
按住Shift即可照常使用鼠标选中文本

*************
## 键绑定
> Prefix 默认是 C-b 也就是 Ctrl b

### 切换
- prefix w 切换 panel 或者 window
- Prefix () 切换Session

************************

## TPM插件管理
- [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) `查看Readme下载安装`
> `git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm`

> [参考博客: 保存和恢复 Tmux 会话 ](https://liam.page/2016/09/10/tmux-plugin-resurrect/)

- `Prefix I` 安装新增的插件 

### tmux-resurrect

> [tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect)  
> [tmux-continuum](https://github.com/tmux-plugins/tmux-continuum)  

prefix c-s 保存会话
prefix c-r 加载历史会话

### maglev
> [Github](https://github.com/caiogondim/maglev)

### copycat
> [Github](https://github.com/tmux-plugins/tmux-copycat)  

使用: `Prefix /` 可用 less 一样的方式搜索
