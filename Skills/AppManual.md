---
title: 常用工具手册
date: 2018-11-21 10:56:52
tags: 
categories: 
---

**目录 start**
 
1. [软件使用记事](#软件使用记事)
    1. [包管理](#包管理)
        1. [使用sdkman](#使用sdkman)
    1. [服务管理](#服务管理)
        1. [oneinstack](#oneinstack)
1. [常用工具](#常用工具)
    1. [网络工具](#网络工具)
        1. [nmap](#nmap)
        1. [whatportis](#whatportis)
    1. [日常工具](#日常工具)
        1. [图片查看工具](#图片查看工具)
        1. [BaiduPCS](#baidupcs)
        1. [you-get](#you-get)
        1. [输入法](#输入法)
            1. [输入引擎](#输入引擎)
            1. [搜狗输入法](#搜狗输入法)
            1. [rime](#rime)
            1. [小小输入法](#小小输入法)
        1. [qgit](#qgit)
        1. [convert](#convert)
        1. [todo.txt](#todotxt)
            1. [todo.txt-cli](#todotxt-cli)
        1. [termux](#termux)
    1. [IDE](#ide)
        1. [Idea](#idea)
        1. [Eclipse](#eclipse)
    1. [绘图工具](#绘图工具)
        1. [思维导图](#思维导图)
    1. [安全工具](#安全工具)
        1. [gpg](#gpg)

**目录 end**|_2019-11-20 20:21_|
****************************************
# 软件使用记事
## 包管理
### 使用sdkman
> 但是总会莫名其妙的冒出问题，sdk命令掉线始终连不上网，终端打开巨慢

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
# 常用工具
> 基本是Linux工具，因为主力是用Linux

## 网络工具
### nmap
> 端口扫描 [参考博客](http://aaaxiang000.blog.163.com/blog/static/2063491220113284325531/)

- 扫描`nmap <param> IP`
    - -sP
    - -sT
    - -sR
    - -n `最简单直接的参数`

### whatportis
> whatportis 是一款可以通过服务查询默认端口，或者是通过端口查询默认服务的工具

************************************
## 日常工具
### 图片查看工具
1. Viewnior  轻量简洁
1. Eye of GNOME Image Viewer 功能比上面多了一点

### BaiduPCS
- [百度网盘命令客户端](https://github.com/iikira/BaiduPCS-Go) `Go语言实现`

### you-get
是一款命令行工具，用来下载网页中的视频、音频、图片，支持众多网站，包含 41 家国内主流视频、音乐网站，  
如 网易云音乐、AB站、
百度贴吧、斗鱼、熊猫、爱奇艺、凤凰视频、酷狗音乐、乐视、荔枝 FM、秒拍、腾讯视频、优酷土豆、央视网、芒果 TV
等等，只需一个命令就能直接下载视频、音频以及图片回来，并且可以自动合并视频。

而对于有弹幕的网站，比如 B 站，还可以将弹幕下载回来

### 输入法
#### 输入引擎
> fcitx ibus ...

> [wiki: fcitx](https://wiki.archlinux.org/index.php/Fcitx_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

#### 搜狗输入法

- Ctrl Alt B 显示/关闭 特殊字符面板

#### rime
- [rime](http://rime.im/) 

#### 小小输入法
[小小输入法在Deepin上的使用](https://bbs.deepin.org/forum.php?mod=viewthread&tid=138500&highlight=%E5%B0%8F%E5%B0%8F%E8%BE%93%E5%85%A5%E6%B3%95)

### qgit
- git查看仓库的命令行式图形化界面

***********************************
### convert
> convert between image formats as well as resize an image, blur, crop, despeckle, dither, draw on, flip, join, re-sample, and much more

- 将图片转换成指定大小 这是保持比例的 `convert -resize 600X600 src.jpg dst.jpg` 中间是字母X
    - 如果不保持比例，就在宽高后加上感叹号 
    - 可以只指定高度，那么宽度会等比例缩放 `convert -resize 400 src.jpg dst.jpg`
    - 还可以按百分比缩放

_批量修改_
> 如果没有 -path 语句，新生成的 png 文件将会覆盖原始文件 [参考博客](http://www.cnblogs.com/jkmiao/p/6756929.html)

- `mogrify -path newdir -resize 40X40 *.png` 把png图片全部转成40X40大小并放在新文件夹下
- `mogrify -path newdir -format png  *.gif` 将所有gif转成png放在新目录下

> 将原有大小图片转换成其他指定大小的图片(保持比例)  
1. 原图片 a * b -> x * y 
1. x/y 得到比例 在 原图中裁剪出同样比例的图片 (Viewnior就很好用)
1. 将裁剪出来的图片转换指定大小 `convert -resize xXy src.jpg dst.jpg`

-  convert origin.jpg target.pdf

***********************************************

### todo.txt
> [官网](http://todotxt.org/) 一个简约的 TODO 软件

#### todo.txt-cli
> 终端中的TODO 

- [todo.txt-cli](https://github.com/todotxt/todo.txt-cli)

### termux
> [wiki FAQ](https://wiki.termux.com/wiki/FAQ)

> [参考博客: Hello，Termux](https://tonybai.com/2017/11/09/hello-termux/)
> [参考博客: Termux：让Android手机摇身一变成为高级Linux终端](https://www.asmodeus.cn/archives/769)
******************************
## IDE
### Idea
> [详细内容](/Java/Tool/IDEA.md)

### Eclipse
> [详细内容](/Java/Tool/Eclipse.md)

***********************************************
## 绘图工具
### 思维导图
> [参考博客: 这 7 款开源思维导图工具真的很神奇](https://blog.csdn.net/zuochao_2013/article/details/68928381)

1. [processon](https://www.processon.com/)`免费额度比较小, 但是使用很方便`

1. [百度脑图在线版](https://github.com/fex-team/kityminder)
    - [百度脑图客户端](https://github.com/NaoTu/DesktopNaotu)

1. [my-mind](https://github.com/ondras/my-mind)`简单轻巧`
1. FreeMind 
1. [freeplane](https://github.com/freeplane/freeplane)`Java编写的, FreeMind衍生`
1. XMind 收费,占用资源大, 文件是二进制,不方便做版本控制

*****************
## 安全工具
### gpg
> [参考博客](http://www.ruanyifeng.com/blog/2013/07/gpg.html)

常用参数
```
gpg --list-key
    --gen-key
```
- 生成的过程, 输入相关的提示信息, 最后输完密码后需要输入随机字符, 就也是按照提示, 但是1.4是正常的, 其他的直接假死,不是很理解这种操作


