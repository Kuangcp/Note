---
title: Arch
date: 2018-12-21 10:55:04
tags: 
    - Arch
    - 基础
categories: 
    - Linux
---

💠

- 1. [Arch](#arch)
    - 1.1. [社区](#社区)
    - 1.2. [包管理](#包管理)
        - 1.2.1. [Pacman](#pacman)
        - 1.2.2. [Yay](#yay)
        - 1.2.3. [Snap](#snap)
- 2. [Tips](#tips)

💠 2024-10-02 22:33:00
****************************************

# Arch

> [参考: Arch Linux的用户都有理想主义倾向吗？](https://www.zhihu.com/question/49439472)
> [参考: ArchLinux你可能需要知道的操作与软件包推荐](https://www.viseator.com/2017/07/02/arch_more/)
> [参考: 长期使用Arch，Gentoo等滚动更新的发行版是怎样的一种体验？](https://www.zhihu.com/question/37720991?sort=created)
> [Arch Linux 安装、配置、美化和优化](http://www.cnblogs.com/bluestorm/p/5929172.html)

************************

衍生版： 
- [EndeavourOS](https://endeavouros.com/)
- Manjaro


## 社区

- [arch cn bbs](https://bbs.archlinuxcn.org/viewforum.php?id=19)
- [archlinux 简明指南](https://arch.icekylin.online/)

## 包管理

> [Creating Arch Linux Packages](https://www.theurbanpenguin.com/creating-arch-linux-packages/)  
> [Arch archive packages](https://archive.archlinux.org/packages/)`软件包镜像站`

### Pacman

> [Arch wiki: pacman ](https://wiki.archlinux.org/index.php/Pacman_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)#%E5%88%A0%E9%99%A4%E8%BD%AF%E4%BB%B6%E5%8C%85)
> Arch User Repository （常被称作 AUR），是一个为 Arch 用户而生的社区驱动软件仓库。Debian/Ubuntu 用户的对应类比是 PPA。

/etc/pacman.conf 追加

```conf
    [archlinuxcn]
    #The Chinese Arch Linux communities packages.
    SigLevel = Optional TrustAll
    #Server   = http://repo.archlinuxcn.org/$arch
    Server   = https://mirrors.ustc.edu.cn/archlinuxcn/$arch
```

- `pacman-mirrors` generate pacman mirrorlist for Manjaro Linux
- -S 安装
- -R 卸载
   - -Rs 卸载以及没有被其他软件依赖的软件包
- -Q 查询
   - -Qdt 查询未被依赖的软件包
- -U 升级或添加软件包 [archive](https://archive.archlinux.org/packages/)
    - 例如 `pacman -U https://archive.archlinux.org/packages/c/curl/curl-8.4.0-1-x86_64.pkg.tar.zst` 安装curl历史版本

> 注意
- pacman yay 升级某些包时需要留意是否需要全系统升级，单独升级某个包容易造成**依赖库版本不匹配**
    - 比如 当前手动curl 8.4.0-2 升级到 8.6.0-3，发现安装失败, 报错 `pacman: /usr/lib/libssl.so.3: version 'OPENSSL_3.2.0' not found (required by /usr/lib/libcurl.so.4)`
    - 由于yay pacman也是依赖的curl，这里就有点死锁了，没法降级了
    - 从curl官网下载源码编译安装，安装路径默认 `/usr/local/bin/curl` 不是pacman默认的`/bin/curl`，只好手动复制lib过去 `sudo cp /usr/local/lib/libcurl.so.4.8.0 /usr/lib/libcurl.so.4.8.0` 新的报错 `curl: /usr/lib/libcurl.so.4: no version information available (required by curl)`
    - 搜索后添加参数 重新编译 `./configure --enable-versioned-symbols  --with-openssl` 重新复制lib过去 还是一样报错信息
    - 但是发现这个报错好像是警告级别不影响实际功能，然后用上述的 pacman -U 安装指定的版本，才恢复了正常使用

> 安装deb包 [How to Install a .deb Package on Arch Linux](https://www.baeldung.com/linux/arch-install-deb-package)

### Yay
缓存目录 ~/.cache/yay

- `pacman -S yay` 下一代aur管理
- `alias yay='/usr/bin/yay --color=always'` 默认开启颜色高亮

### Snap

> 使用 pacman 安装
1. sudo pacman -S snapd
2. sudo systemctl enable --now snapd.socket
3. sudo ln -s /var/lib/snapd/snap /snap

- 例如安装 sudo snap install redis-desktop-manager
    - 可执行文件 /snap/bin/redis-desktop-manager.rdm

- 但是国内会很慢，此时可以手动下载安装 [参考: snapInstall](https://kuricat.com/gist/snap-install-too-slow-zmbjy)
    - curl -H 'Snap-Device-Series: 16' http://api.snapcraft.io/v2/snaps/info/{{packageName}} 例如 `redis-desktop-manager`
    - sudo snap install xxx.snap --dangerous

************************

# Tips

> 无法识别 USB设备（键盘 鼠标 移动硬盘） 可能原因

1. 查看是usb模块 `sudo modprobe usb-storage`
    1. 若报错 `modprobe: FATAL: Module usb-storage not found in directory /lib/modules/4.19**`
    2. 查看 `ls /lib/modules`
2. Linux内核滚动升级了 但是grub 没有更新, `update-grub`即可
3. 滚动升级了，没有重启电脑

- sudo pacman -S net-tools dnsutils inetutils iproute2
    - ifconfig,route 在net-tools
    - nslookup,dig 在dnsutils
    - ftp,telnet等 在inetutils
    - ip 在 iproute2

************************

> 键盘 F区 按键映射错误

- [Arch Wiki](https://wiki.archlinux.org/index.php/Apple_Keyboard#Function_keys_do_not_work)
- `echo 2 > /sys/module/hid_apple/parameters/fnmode` 注意重启会失效
  - `echo 2 | sudo tee /sys/module/hid_apple/parameters/fnmode`

- 向 /sys/module/hid_apple/parameters/fnmode 文件中写入不同的值，可切换不同的模式：
    ```
        0  禁用功能键，按 ‘Fn’ + ‘F8’ 等同于 F8
        1  默认功能键，按 ‘F8’ 触发功能键 (play/pause)，按 ‘Fn’ + ‘F8’ 触发 F8 键
        2  默认非功能键，按 ‘F8’ 触发 F8 键，按 ‘Fn’ + ‘F8’ 触发功能键 (play/pause)
    ```
- 以上方法重启后失效，如果要让配置永久生效： `Manjaro中没有这个文件`
    ```
        # vi /etc/modprobe.d/hid_apple.conf
        options hid_apple fnmode=2
    ```
- 或者将命令写入登录shell /etc/profile

************************

> keyring 错误

`yay -Sy archlinux-keyring`

