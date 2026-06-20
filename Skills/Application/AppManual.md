---
title: 常用工具手册
date: 2018-11-21 10:56:52
tags: 
categories: 
    - WIKI
---

💠

- 1. [软件使用记事](#软件使用记事)
    - 1.1. [包管理](#包管理)
        - 1.1.1. [sdkman](#sdkman)
    - 1.2. [服务管理](#服务管理)
        - 1.2.1. [oneinstack](#oneinstack)
    - 1.3. [日常工具](#日常工具)
        - 1.3.1. [Termux](#termux)
        - 1.3.2. [iSH](#ish)
        - 1.3.3. [kite](#kite)
    - 1.4. [开发调试工具&技巧](#开发调试工具&技巧)
        - 1.4.1. [网络](#网络)
        - 1.4.2. [Debug](#debug)
    - 1.5. [IDE](#ide)
        - 1.5.1. [Idea](#idea)
        - 1.5.2. [Eclipse](#eclipse)
    - 1.6. [绘图工具](#绘图工具)
        - 1.6.1. [思维导图](#思维导图)

💠 2026-06-15 21:18:09
****************************************
# 软件使用记事
## 包管理
### sdkman

`安装`
- 安装sdkman `curl -s "https://get.sdkman.io?rcupdate=false" | bash` 依赖 zip unzip curl sed
- 依据提示配置 sdkman-init.sh 或者重启终端就可以使用了
- 查看sdkman版本 `sdk version`
- 如果是Windows 可以安装 Git，就会有git-bash 了，也可以用，但是注意会报错找不到zip命令，实际上git-bash里有unzip，他也只是用到这个来解压，所以可以欺骗他 cp /usr/bin/unzip /usr/bin/zip 如果没权限就提权下。

`使用`
- [官网文档](http://sdkman.io/usage.html)
- 查看所有 `sdk list`
    - 查看某sdk的版本 `sdk list java ` 
- 安装最新稳定版 `sdk install java` 安装指定版本 `sdk default java 8u131-zulu`
- 使用指定版本 `sdk use scala 2.12.1`
- 查看当前版本 `sdk current java`
- 验证是否成功 `java -version`
- 移除 `sdk uninstall scala 2.11.6`

******************
## 服务管理
### oneinstack
> 一键配置环境 [官方文档](https://oneinstack.com/install/)

![配图](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Linux/install_oneinstack.png)
- `apt -y install wget screen curl python`
- 下载源码：
    - `wget http://aliyun-oss.linuxeye.com/oneinstack-full.tar.gz` #阿里云经典网络下载
    - `wget http://mirrors.linuxeye.com/oneinstack-full.tar.gz` #包含源码，国内外均可下载
    - `wget http://mirrors.linuxeye.com/oneinstack.tar.gz` #不包含源码，建议仅国外主机下载
- `tar xzf oneinstack-full.tar.gz`
- `cd oneinstack` #如果需要修改目录(安装、数据存储、Nginx日志)，请修改options.conf文件
- `screen -S oneinstack` #如果网路出现中断，可以执行命令`screen -R oneinstack`重新连接安装窗口
- `sudo ./install.sh` #注：请勿sh install.sh或者bash install.sh这样执行

******************
## 日常工具
> iOS 相关

[a shell](https://holzschu.github.io/a-Shell_iOS/) `iOS13`

### Termux
> 安卓上安装的Linux模拟器, 几乎完整的运行时，只有Docker等虚拟化不支持，常见命令和开发环境均支持（前提是技术组件支持arm架构指令）  
> 只建议 Google Play中安装，通过换机软件导入的运行时，文件及环境变量会有缺失和损坏

> [wiki FAQ](https://wiki.termux.com/wiki/FAQ)

> [参考: Hello，Termux](https://tonybai.com/2017/11/09/hello-termux/)
> [参考: Termux：让Android手机摇身一变成为高级Linux终端](https://www.asmodeus.cn/archives/769)

- 开启ssh服务 pkg install openssh 对应端口默认 8022
- 执行 termux-setup-storage 命令，建立常用目录软链接

### iSH
> iOS体系内终端模拟器。耗电发热大，且必须前台运行才能保持软件内开启的各种服务线程(ssh,http,tcp等)，因为iOS会冻结后台

- apk add openssh 
- ssh root@ip 方式登录iOS设备
    - 但是 ip只能通过设置中的wifi信息看机子的局域网ip `ifconfig命令在iSH内执行无效`

### kite
> [Official Site](https://www.kite.com/)  
> Free AI Coding Assistant and Code Auto-Complete  

支持 VS Code IDEA Vim 等等

************************
## 开发调试工具&技巧
### 网络
- **xswtich** `Chrome插件`
    - 浏览器层面通过劫持ajax请求，修改请求的实际地址从而达到访问某网站时指定替换加载的静态资源（js css）,或者是替换请求的服务端地址
    - 场景：访问前后端分离的某应用服务，浏览器打开测试环境时，修改配置使前端对测试环境后端发起请求实际被替换请求到本地，方便调试
    - 由于Firefox不兼容，自己基于go开发的替代品 [dev-proxy](https://github.com/Kuangcp/GoBase/tree/master/toolbox/dev-proxy)

- **Multi-Account-Container** `Firefox 插件`
    - 同一网站同时登录多个账号，账号之间cookie等信息会隔离

- **potatso** iOS体系内代理软件 iOS 15兼容有问题

### Debug

************************


## IDE
### Idea
> [详细内容](/Java/Tool/IDEA.md)

### Eclipse
> [详细内容](/Java/Tool/Eclipse.md)

************************

## 绘图工具
### 思维导图
> [参考: 这 7 款开源思维导图工具真的很神奇](https://blog.csdn.net/zuochao_2013/article/details/68928381)

1. [processon](https://www.processon.com/)`免费额度比较小, 但是使用很方便`

1. [百度脑图在线版](https://github.com/fex-team/kityminder)
    - [百度脑图客户端](https://github.com/NaoTu/DesktopNaotu)
    - vscode-mindmap 百度脑图VSCode插件版

1. [my-mind](https://github.com/ondras/my-mind)`简单轻巧`
1. FreeMind 
1. [freeplane](https://github.com/freeplane/freeplane)`Java编写的, FreeMind衍生`
1. XMind 收费,占用资源大, 文件是二进制,不方便做版本控制
