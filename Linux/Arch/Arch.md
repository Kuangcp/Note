---
title: Arch
date: 2018-12-21 10:55:04
tags: 
    - Arch
    - 基础
categories: 
    - Linux
---

**目录 start**
 
1. [Arch](#arch)
    1. [包管理](#包管理)
        1. [Pacman](#pacman)
        1. [snap](#snap)
        1. [Yaourt](#yaourt)
        1. [Yay](#yay)
1. [Tips](#tips)

**目录 end**|_2019-11-28 16:36_|
****************************************

# Arch
> [参考博客: 为什么 Archlinux 不适合服务器使用](https://www.tuicool.com/articles/byAFZr)
> [参考博客: Arch Linux的用户都有理想主义倾向吗？](https://www.zhihu.com/question/49439472)
> [参考博客: ArchLinux你可能需要知道的操作与软件包推荐](https://www.viseator.com/2017/07/02/arch_more/)
> [参考博客: 长期使用Arch，Gentoo等滚动更新的发行版是怎样的一种体验？](https://www.zhihu.com/question/37720991?sort=created)

- [什么Linux发行版软件最多？](https://www.lulinux.com/archives/2787)
- [Arch Linux 安装、配置、美化和优化](http://www.cnblogs.com/bluestorm/p/5929172.html)

## 包管理
### Pacman 

> Arch User Repository （常被称作 AUR），是一个为 Arch 用户而生的社区驱动软件仓库。Debian/Ubuntu 用户的对应类比是 PPA。

1. `pacman-mirrors` generate pacman mirrorlist for Manjaro Linux 

1. -S 安装
1. -R 卸载
    - -Rs 卸载以及没有被其他软件依赖的软件包

### snap
> 安装 
1. sudo pacman -S snapd
1. sudo systemctl enable --now snapd.socket
1. sudo ln -s /var/lib/snapd/snap /snap

> 使用 sudo snap install redis-desktop-manager

### Yaourt
> [Arch User Repository](https://wiki.archlinux.org/index.php/Arch_User_Repository)`但是已经暂停开发了`

1. `/etc/pacman.conf` 追加
    ```conf
    [archlinuxcn]
    #The Chinese Arch Linux communities packages.
    SigLevel = Optional TrustAll
    Server   = http://repo.archlinuxcn.org/$arch
    ```
1. `sudo pacman -Syu yaourt` 同步

> 若遇到 签名错误  signature from ... is unknown trust

```sh
sudo rm -R /etc/pacman.d/gnupg/
sudo rm -R /root/.gnupg/ 
sudo gpg --refresh-keys
sudo pacman-key --init && pacman-key --populate archlinux manjaro
sudo pacman-key --refresh-keys
sudo pacman -Syyu
```

### Yay

- `pacman -S yay` 下一代aur管理

************************

# Tips

- deepin-wine
- [企业微信](https://aur.archlinux.org/packages/deepin-wxwork/)
- [go-for-it](https://aur.archlinux.org/packages/go-for-it/)
