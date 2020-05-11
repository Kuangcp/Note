---
title: Manjaro
date: 2018-12-21 10:55:08
tags: 
   - Arch
   - Manjaro
categories: 
   - Linux
---

**目录 start**

1. [Manjaro](#manjaro)
    1. [Tips](#tips)

**目录 end**|_2020-05-12 01:07_|
****************************************
# Manjaro
> [Gitlab source code](https://gitlab.manjaro.org/explore/groups)  

> [Manjaro Controversies](https://rentry.co/manjaro-controversies)

> [Manjaro 安装体验小结 ](https://michael728.github.io/2019/08/03/linux-manjaro-install/)  
> [Manjaro 安装配置简要](https://blog.csdn.net/ouening/article/details/79633966)  
> [Manjaro安装后你需要这样做](https://www.cnblogs.com/haohao77/p/9034499.html)  
> [参考: Manjaro Deepin安装使用分享](https://zhuanlan.zhihu.com/p/43442012)  
> [参考: Manjaro Deepin 配置备忘](https://yifeitao.com/2019/06/xiaomi-pro-manjaro-deepin)  

> [参考: Manjaro 配置](https://blog.triplez.cn/manjaro-quick-start)  

由于是基于arch的, 滚动更新的特性, 所以需要在每次在安装软件前 `pacman -Syu` 更新整个系统

## Tips
> U盘启动盘运行Live系统时, 默认用户名和密码都为 manjaro

- 这次下载解压运行 VSCode 就是这样, 报错为 
   - `error while loading shared libraries: libgconf-2.so.4: cannot open shared object file: No such file or directory`
   - 尝试安装 libgconf libgconf2 ...
   - 其实真正的包是 gconf , 而这个也是尝试过的,  但是还是说找不到package, 更新了下系统,才找到了这个包

- Linux5 内核和 VirtualBox 有兼容问题，需要版本匹配，如果内核从4升级到5 VirtualBox要相应更新

************************

> Manjaro 安装 deb 包 

1. 安装工具 yaourt -S debtap  或者  yay debtap
1. 升级 sudo debtap -u
1. 转换deb包 sudo debtap  xxxx.deb
1. 安装转换后的安装包 sudo pacman -U x.tar.xz

************************

> 使用国内镜像源 
1. `sudo pacman-mirrors -i -c China -m rank` | [ustc.edu.cn](http://mirrors.ustc.edu.cn/help/manjaro.html)

foxit GitKraken deepin-screenshot