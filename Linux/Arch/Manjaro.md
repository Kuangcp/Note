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

**目录 end**|_2019-04-19 13:04_| [Kuangcp](https://github.com/Kuangcp/Note) | [yi-yun](https://github.com/yi-yun/Memo)
****************************************
# Manjaro
> [Gitlab source code](https://gitlab.manjaro.org/explore/groups)

> pacman 文档 https://wiki.archlinux.org/index.php/Pacman_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)

> [Manjaro 安装配置简要](https://blog.csdn.net/ouening/article/details/79633966)
> [参考博客: Manjaro Deepin安装使用分享](https://zhuanlan.zhihu.com/p/43442012)

由于是基于arch的, 滚动更新的特性, 所以需要在每次在安装软件前 `pacman -Syu` 更新整个系统
- 这次下载解压运行 VSCode 就是这样, 报错为 
   - error while loading shared libraries: libgconf-2.so.4: cannot open shared object file: No such file or directory
   - 尝试安装 libgconf libgconf2 ...
   - 其实真正的包是 gconf , 而这个也是尝试过的,  但是还是说找不到package, 更新了下系统,才找到了这个包

安装时候 默认用户名和密码是 manjaro

