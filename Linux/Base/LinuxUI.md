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
    1. [Terminal](#terminal)
        1. [彩色输出](#彩色输出)

**目录 end**|_2020-05-06 21:24_|
****************************************

# UI
> themes icons fonts 

- [www.gnome-look.org](https://www.gnome-look.org/)

- 所有用户通用, 安装新的后需要重启 `/usr/share/themes`
- 当前用户, 直接复制进来立即生效:  `~/.themes` 或者 `~/.local/share/themes`

- 问题: Deepin上 全放 ~/.local/share/themes 会有bug, 只能全放 ~/.themes

## Font
> [字体](/FrontEnd/Font.md)  

### 字体渲染
> [Debian8安装Infinality改善字体渲染，安装Ubuntu字体](https://www.linuxdashen.com/debian8%E5%AE%89%E8%A3%85infinality%E6%94%B9%E5%96%84%E5%AD%97%E4%BD%93%E6%B8%B2%E6%9F%93%EF%BC%8C%E5%AE%89%E8%A3%85ubuntu%E5%AD%97%E4%BD%93)  
> [一条命令搞定Linux字体渲染](https://www.lulinux.com/archives/278)  
> [Font Configuration/Chinese (简体中文)](https://wiki.archlinux.org/index.php/Font_Configuration/Chinese_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))  
> [参考: Fcitx (简体中文)](https://wiki.archlinux.org/index.php/Fcitx_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))  

- 刷新字体缓存 `fc-cache -fv` 
    - 对应于目录 `~/.local/share/fonts`

*******************

## Theme
- [Github:vimix](https://github.com/vinceliuice/vimix-gtk-themes)`material design theme`

> [参考: 10 Great Linux GTK Themes For 2018 ](https://www.maketecheasier.com/gtk-themes-for-linux/)

- [pingguo](https://www.gnome-look.org/p/1239453/)

- [Sierra](https://www.gnome-look.org/p/1013714/)
- [GTK3主题：OSX-Arc](https://www.linuxidc.com/Linux/2017-01/139053.htm) `解压到 /usr/share/themes/ 下即可,或者 ~/.themes/ `

***********************

## Icon
> sudo apt search icon-theme  也能看到很多icon

1. Halo-icon-theme

## Terminal

### 彩色输出
> [参考博客,比较详细](http://blog.csdn.net/magiclyj/article/details/72637666)  
> [Linux Terminal Color](https://blog.csdn.net/y2701310012/article/details/40142809)  

```sh
  red='\033[0;31m'
  green='\033[0;32m'
  yellow='\033[0;33m'
  blue='\033[0;34m'
  purple='\033[0;35m'
  cyan='\033[0;36m'
  white='\033[0;37m'
  default='\033[0m'
```

> 256 color
```sh
    # 测试 terminal 是否支持 256
    for i in {0..255} ; do
        printf "\x1b[48;5;%sm%3d\e[0m " "$i" "$i"
        if (( i == 15 )) || (( i > 15 )) && (( (i-15) % 6 == 0 )); then
            printf "\n";
        fi
    done
```

[Gihub: LS_COLORS](https://github.com/trapd00r/LS_COLORS)  
[customize bash prompt](https://www.howtogeek.com/307701/how-to-customize-and-colorize-your-bash-prompt/)  

1. `curl https://raw.githubusercontent.com/trapd00r/LS_COLORS/master/LS_COLORS -o /etc/lscolor-256color`
1. add to *sh.rc
    ```sh
    if [[ ("$TERM" = *256color || "$TERM" = screen* || "$TERM" = xterm* ) && -f /etc/lscolor-256color ]]; then
            eval $(dircolors -b /etc/lscolor-256color)
        else
                eval $(dircolors)
    fi
    ```
