---
title: 常用工具手册
date: 2018-11-21 10:56:52
tags: 
categories: 
---

**目录 start**

1. [软件使用记事](#软件使用记事)
    1. [包管理](#包管理)
        1. [sdkman](#sdkman)
    1. [服务管理](#服务管理)
        1. [oneinstack](#oneinstack)
    1. [日常工具](#日常工具)
        1. [termux](#termux)
        1. [kite](#kite)
    1. [IDE](#ide)
        1. [Idea](#idea)
        1. [Eclipse](#eclipse)
    1. [绘图工具](#绘图工具)
        1. [思维导图](#思维导图)

**目录 end**|_2021-03-05 17:53_|
****************************************
# 软件使用记事
## 包管理
### sdkman

`安装`
- 安装sdkman `curl -s "https://get.sdkman.io" | bash` 遇到提示zip 就是需要安装zip `sudo apt install zip` 然后重新执行命令
- 执行脚本：`source "/home/kuang/.sdkman/bin/sdkman-init.sh"` 或者重启终端就可以使用了，查看sdkman 版本:`sdk version`
`使用`
- [官网文档](http://sdkman.io/usage.html)
- 查看所有 `sdk list`
    - 查看某sdk的版本 `sdk list java ` 
- 不指定版本则默认安装最新版 `sdk install java` 安装指定版本 `sdk default java 8u131-zulu`
- 开始使用指定版本(for the current shell only) `sdk use scala 2.12.1`
- 查看当前版本 `sdk current java`
- 验证是否成功：`java -version`
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
> 安卓上安装的Linux模拟器, 几乎完整的运行时，只有Docker等虚拟化不支持，其他命令和环境均支持

> [wiki FAQ](https://wiki.termux.com/wiki/FAQ)

> [参考: Hello，Termux](https://tonybai.com/2017/11/09/hello-termux/)
> [参考: Termux：让Android手机摇身一变成为高级Linux终端](https://www.asmodeus.cn/archives/769)

- 开启ssh服务 pkg install openssh 对应端口默认 8022
- 执行 termux-setup-storage 命令，建立常用目录软链接


### iSH
> 耗电发热大，必须前台运行，
- apk add openssh 
- ssh root@ip ip只能通过wifi看局域网ip ifconfig无效

### kite
> [Official Site](https://www.kite.com/)  
> Free AI Coding Assistant and Code Auto-Complete  

支持 VS Code IDEA Vim 等等

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
