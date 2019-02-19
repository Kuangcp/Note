---
title: LinuxUI.md
date: 2018-12-15 11:18:48
tags: 
    - 工具使用经验
    - 美化
categories: 
    - Linux
---

**目录 start**
 
1. [UI](#ui)
    1. [Font](#font)
        1. [字体渲染](#字体渲染)
    1. [Theme](#theme)
    1. [Icon](#icon)

**目录 end**|_2019-02-19 10:36_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************

# UI
> themes icons fonts 

- 所有用户通用, 安装新的后需要重启 `/usr/share/themes`
- 当前用户, 直接复制进来立即生效:  `~/.local/share/themes` 或者 ~/.themes

## Font
> [笔记: 字体](/FrontEnd/Font.md)  

### 字体渲染
> [Debian8安装Infinality改善字体渲染，安装Ubuntu字体](https://www.linuxdashen.com/debian8%E5%AE%89%E8%A3%85infinality%E6%94%B9%E5%96%84%E5%AD%97%E4%BD%93%E6%B8%B2%E6%9F%93%EF%BC%8C%E5%AE%89%E8%A3%85ubuntu%E5%AD%97%E4%BD%93)
> [一条命令搞定Linux字体渲染](https://www.lulinux.com/archives/278)

- 刷新字体缓存 `fc-cache -fv`

*******************

## Theme


> [参考博客: 10 Great Linux GTK Themes For 2018 ](https://www.maketecheasier.com/gtk-themes-for-linux/)

- [mac theme](https://www.gnome-look.org/p/1239453/)
- [Github:vimix](https://github.com/vinceliuice/vimix-gtk-themes)`material design theme`
- [GTK3主题：OSX-Arc](https://www.linuxidc.com/Linux/2017-01/139053.htm) `解压到 /usr/share/themes/ 下即可,或者 ~/.themes/ `

***********************

## Icon
> sudo apt search icon-theme  也能看到很多icon

1. Halo-icon-theme
