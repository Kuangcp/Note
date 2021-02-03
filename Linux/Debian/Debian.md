---
title: Debian基础
date: 2018-12-15 11:29:14
tags: 
    - Debian
categories: 
    - Linux
---

**目录 start**

1. [Debian](#debian)
    1. [配置](#配置)
        1. [配置语言环境](#配置语言环境)
    1. [软件管理](#软件管理)
        1. [软件源列表](#软件源列表)
        1. [包管理器](#包管理器)
        1. [源码编译安装](#源码编译安装)

**目录 end**|_2021-02-03 17:25_|
****************************************
# Debian 
> 很古老但是很好用的系统 [官网](https://www.debian.org/index.zh-cn.html)

> [参考: Debian8最小安装](https://www.howtoforge.com/tutorial/debian-8-jessie-minimal-server/)
- 奇怪的是我在虚拟机里装了好几个好几次装不上, 装完一登录就只有壁纸

_服务器_
- 2018-04-01 17:19:50 作为服务器系统安装完Debian8.2 85M内存占用 docker 是1.6
- 2018-04-10 10:35:54 服务器安装Ubuntu16.04 71M内存 docker是1.13

## 配置
### 配置语言环境
1. apt install locales
2. dpkg-reconfigure locales
3. 进入选择界面 `zh_CN.UTF-8 UTF-8` 空格选择, 换行 继续


## 软件管理
### 软件源列表
- apt 的默认配置文件是 `/etc/apt/source.list`
    - 以及 sources.list.d/ 目录下的 *.list 文件 (最好将list文件都进行备份 备份文件为 *.save)

- [参考博客 阿里云的软件源](https://hacpai.com/article/1482807364546?p=1&m=0)
- [wiki-源列表说明](http://wiki.ubuntu.com.cn/%E6%BA%90%E5%88%97%E8%A1%A8)

1. 源 URL 后的单词: 
    1. main: 完全的自由软件。
    1. restricted: 不完全的自由软件。
    1. universe: Ubuntu官方不提供支持与补丁，全靠社区支持。
    1. multiverse: 非自由软件，完全不提供支持和补丁。

1. 添加私有源ppa
    - 若不能添加私有源ppa：
        - debain：`sudo apt install software-properties-common python-software-properties`
        - Ubuntu `sudo apt install python-software-properties`
    - 添加：`sudo add-apt-repository ppa:dotcloud/lxc-docker `
	- 删除ppa : `cd  /etc/apt/sources.list.d/` 打开该目录下文件把对应的ppa的一行注释掉或删掉就行了


1. 添加一个源列表
    - 例如添加 nginx: 新建文件 `/etc/apt/sources.list.d/nginx.list` 
    ```
        deb http://nginx.org/packages/mainline/debian/ jessie nginx
        deb-src http://nginx.org/packages/mainline/debian/ jessie nginx
    ```
    - `curl http://nginx.org/keys/nginx_signing.key | apt-key add -`
        - 把签名添加进来才能正常 apt update

### 包管理器
**`dpkg`**
1. 查看已安装的应用 `dpkg --list`
1. 显示已安装包的详情 `dpkg -s package`
1. 安装deb包
	- ` sudo  dpkg  -i  *.deb`

**`apt-get / apt`**
1. `install 包名`  安装指定包的最新版
    - `-y` 参数可以省去确认
    - `-s` 模拟安装
    - `package=version` 安装指定版本的包

1. list 列出所有可安装的包
    - --installed 已安装的包
    - package 列出已安装的 该package 的信息 `加上 -a`: 所有版本

1. 只卸载程序，保留配置文件 `sudo apt remove 包名`
    - 彻底卸载应用 `sudo apt--purge remove 包名`
    - 若已经卸载, 清理配置: `apt purge 包名` (不会清理home/.config里的内容)

- apt-cache showpkg/policy/madison/show package
    - showpkg (特别详细) 列出所有版本以及来源, MD5 ...
    - policy (基本信息) 列出所有版本以及来源
    - madison (简略显示) 内容同上
    - show 查询指定包的详情(已安装的版本信息)
    - search 搜索包

**`snap`**
- [official doc: snap](https://snapcraft.io/docs/core/usage) `提供一个类似容器的环境,将所有依赖打包，隔离运行`

### 源码编译安装
1. make install 源代码安装
    - 1.解压缩 `tar -zxf nagios-4.0.2.tar.gz ` 
    - 2.进入目录 `cd nagios-4.0.2`
    - 3.配置 `./configure --prefix=/usr/local/nagios  ` 
    - 4.编译 `make all`
    - 5.安装 `make install && make install-init && make install-commandmode && make install-config`
