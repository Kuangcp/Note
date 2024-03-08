---
title: Tmux
date: 2019-02-28 17:43:53
tags: 
categories: 
    - 工具
---

💠

- 1. [Tmux](#tmux)
- 2. [基本操作](#基本操作)
- 3. [配置](#配置)
    - 3.1. [个人配置](#个人配置)
    - 3.2. [键绑定](#键绑定)
    - 3.3. [切换](#切换)
- 4. [编译安装](#编译安装)
- 5. [TPM插件管理](#tpm插件管理)
    - 5.1. [tmux-resurrect](#tmux-resurrect)
    - 5.2. [maglev](#maglev)
    - 5.3. [copycat](#copycat)
- 6. [Tips](#tips)

💠 2024-03-08 18:19:25
****************************************
# Tmux
> [Arch wiki: tmux](https://wiki.archlinux.org/index.php/Tmux_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

> [tmux简洁教程及config关键配置](https://www.jianshu.com/p/fd3bbdba9dc9)
> [参考: 程序员高效技巧系列](http://cenalulu.github.io/linux/professional-tmux-skills/)  

************************
# 基本操作

- 新建会话 `tmux new -s myth`
- 连接会话 `tmux a -t test`
- 显示所有 `tmux ls`
- 重新加载配置文件 `tmux source ~/.tmux.conf`

> 快捷键
- prefix
    - ? 帮助
    - s 选择 session
    - w 选择 window
    - d deattach 脱离
    - j 下 panel
    - k 上 panel
    - ; 最近的 panel
    - $ 重命名 session
    - , 重命名 panel
    - Alt+方向键 往指定方向扩展当前 panel 大小
- Alt+方向键 跳转到对应方向的panel上

*************

# 配置
> [Oh My Tmux!](https://github.com/gpakosz/.tmux)

## 个人配置
> [Tmux配置文件](https://gitee.com/gin9/Configs/blob/master/Linux/tmux/tmux.conf)  

步骤  
1. `ln -s $(pwd)/tmux.conf ~/.tmux.conf` 
1. `git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm`
1. `tmux source ~/.tmux.conf`
1. `Ctrl A, I` 等待插件安装完成

*******************

> 开启鼠标选择与复制
```conf
    set -g mouse on
```

1. 按住Shift即可照常使用鼠标选中文本
1. 在tab区域用滚轮可快速切换tab

*************
## 键绑定
> Prefix 默认是 C-b 也就是 Ctrl b

## 切换
- prefix w 切换 window 或者 Session
- Prefix () 切换 Session

************************

# 编译安装
> 场景： 目标机器Linux内核版本较低，或者是Debian Centos等发行版，源中没有高版本的Tmux，甚至没有Tmux，这个时候通过静态编译安装，能在影响最小的情况下使用上新版本的Tmux

因为低版本Tmux不支持鼠标，导致无法使用滚轮上翻命令输出记录。

> [CentOS 静态编译](https://zhengzexin.com/archives/Tmux_static_compilation/)`但是在Centos6上没成功 内核3.10 gcc 4.6.8`

************************

# TPM插件管理
- [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) `查看Readme下载安装`
> `git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm`

- [tmux-plugins list 插件列表](https://github.com/tmux-plugins/list)

> [参考: 保存和恢复 Tmux 会话 ](https://liam.page/2016/09/10/tmux-plugin-resurrect/)

https://github.com/whame/tmux-modal 快速操作切换和创建 window panel

- `Prefix I` 安装新增的插件 

## tmux-resurrect

> [tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect)  
> [tmux-continuum](https://github.com/tmux-plugins/tmux-continuum)  

prefix c-s 保存会话
prefix c-r 加载历史会话

## maglev
> [Github](https://github.com/caiogondim/maglev)

## copycat
> [Github](https://github.com/tmux-plugins/tmux-copycat)  

使用: `Prefix /` 可用 less 一样的方式搜索


# Tips 
> [bash: append_path: command not found when open tmux](https://superuser.com/questions/1590651/bash-append-path-command-not-found-when-open-tmux)

`set-option -g default-command '/bin/bash'` 追加到 tmux.conf 即可解决，如果使用 zsh 则是 /usr/bin/zsh
