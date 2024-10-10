---
title: 浏览器
date: 2018-12-15 12:11:56
tags: 
categories: 
    - 工具
---

💠

- 1. [浏览器](#浏览器)
    - 1.1. [FireFox](#firefox)
        - 1.1.1. [开发版本](#开发版本)
        - 1.1.2. [必备插件](#必备插件)
        - 1.1.3. [配置](#配置)
        - 1.1.4. [使用](#使用)
        - 1.1.5. [Tips](#tips)
    - 1.2. [Seamonkey](#seamonkey)
    - 1.3. [Chrome](#chrome)
        - 1.3.1. [主题](#主题)
        - 1.3.2. [插件](#插件)
    - 1.4. [Vivaldi](#vivaldi)

💠 2024-10-10 20:43:07
****************************************
# 浏览器
[neko](https://github.com/m1k1o/neko)`runs in docker and uses WebRTC`

## FireFox
> [所有桌面版](https://www.mozilla.org/zh-CN/firefox/channel/desktop/) | [所有正式版](https://www.mozilla.org/en-US/firefox/releases/)
> [正式版本和夜更新版FTP下载地址](http://ftp.mozilla.org/pub/firefox/) | [所有开发者版本](http://ftp.mozilla.org/pub/devedition/releases/)

`57为全新的Quantum版本， 因为插件标准的缘故和之前的56版本插件不兼容`

- 分为 正式版， beta， Nightly 开发版 
- 如果要配置多个火狐在电脑上 终端中 `./firefox -P` 就会进入配置文件的编辑（关闭所有火狐的情况下）
    - 新建一个就好了，之后就用新建的打开该火狐`./firefox -P name`
    - 如果要同时运行多种版本的火狐 加上`--no-remote`参数，但是我这个deepin不要诶，只要配置不同即可，但是Ubuntu mint加上也没有用

- 火狐和Chrome都支持在控制台的网络中直接右击一个请求然后复制, 就可以出来复制成cURL命令的选项, 比较好用

> [火狐性能优化贴](https://www.xzcblog.com/post-47.html)  
> [Firefox uses too much memory or CPU resources - How to fix](https://support.mozilla.org/en-US/kb/firefox-uses-too-much-memory-or-cpu-resources)

> [Floorp](https://github.com/floorp-Projects/floorp/)`FF衍生品，支持工作区，多行tab，单窗口多tab` 但是没有循环tab切换  

### 开发版本
> [开发者版本链接](https://www.mozilla.org/zh-CN/firefox/developer/) | [开发工具](https://firefox-dev.tools/)  
> [使用说明文档](https://developer.mozilla.org/zh-CN/docs/Tools?utm_source=devtools&utm_medium=tabbar-menu)

### 必备插件
> [开发自己的插件](https://github.com/Kuangcp/LearnWebExtension)

1. 附加组件管理器: 只有正式版会内置该插件, 别的版本都没有, 插件的功能是 地址栏二维码,拖拽链接,
    - 如果想在开发版以及Nightly上用上该插件, 只需要去 ~/.mozilla/ 下找到正式版的配置文件里的 extension 目录就能找到 cpmanager.xpi 了, 拖入浏览器就可以了
    - 但是这个组件只保证正式版是正常的, 其他版本则要看运气

- `Vimium C - All by Keyboard`
    - Vim风格操作浏览器日常操作
1. `Dark Reader` 设置网页黑夜模式
1. `Greasemonkey` Tampermonkey 传说中的油猴, 可以自己写脚本 [wiki](https://wiki.greasespot.net/User_Script_Hosting)
1. `New Tab Tools` 新建标签页的自定义工具 
1. `cliget` 能将下载中的任务转化为 curl wget命令 牛
1. `eolinker` 接口测试工具
1. `Simple Tab Groups` 懒加载式隔离标签组
1. `RESTer` rest客户端工具
1. `Download all Images`下载图片
1. `octotree` github 目录查看
1. `Web Developer` 各种Web调试开发工具
1. `Remove Cookies Button`
1. `滴答清单` 全平台可使用
1. `Auto Reload Tab` 定时自动刷新标签页
1. `ReloadMatic` 定时自动刷新
1. `轻灵划译` 即刻翻译, 多种平台
1. `Tab Counter` Tab计数 开发者 WaldiPL
1. `Elasticvue` Elasticsearch 插件
1. `HeaderEditor` 修改请求响应的Header和Body
1. [TechStack](https://github.com/Get-Tech-Stack/TechStack)

### 配置
> 大多是通过 about:config 页面配置

1. 配置火狐访问80以外的端口
    1. 打开 `about:config?filter=network.security.ports.banned.override` 新建字符串类型
    1. 输入值 81,88,98, 也可以是 6000-6005, 省事就 0-65535(不建议)

1. 对于自己喜欢多开火狐的习惯, 整理如下习惯
    - 安装开发版本, 使用默认的配置
    - 使用开发版本的可执行文件, 通过 -P 参数配置一个新的配置目录
    1. 前者是重度使用(往往很多标签20+), 常用的标签页全部固定, 一些TODO的tab也放在这里, 用于开发和娱乐(1000M-2000M)
    1. 后者是轻度使用(开10个以下标签), 仅在内存不够时, 只用于内存不足时开发必需 (一般400M左右)

1. 当前标签页右边打开新标签页: `about:config?filter=browser.tabs.insertAfterCurrent` 新建Bool类型, 设置为true

1. 网页重定向次数限制 默认 20 `network.http.redirection-limit` 设置为0就禁止了网页的重定向

1. 内存资源占用大
    1. `about:memory` 查看内存情况
    1. `dom.ipc.processCount` 降低进程数
    1. `browser.tabs.remote.autostart` 设置 false
    1. `about:unloads` 手动触发tab卸载
    1. `about:processes` 查看tab进程 **Shift + Esc**
    1. [Auto Tab Discard 插件](https://addons.mozilla.org/en-US/firefox/addon/auto-tab-discard/)

### 使用
1. 地址栏 `@bing @baidu...` 即可使用指定的搜索引擎进行搜索
1. 地址栏 `* Java` 即可在所有书签中搜索 Java
1. 地址栏 `% Java` 就可以在已打开的标签页中搜索Java

### Tips
> 在B站看视频 看久了就会发现内存爆炸, 曾经全屏看LOL直播连续6个小时, 然后结束的时候发现出不去了, 要等好久  
> 等了半天打开htop一看firefox 占用内存 6g, 负载 297, 怪不得风扇转这么大声...  
> 原以为是Firefox 的问题, 用 Chrome 看B站一样的场景, 看了没多久就是CPU负载高 内存泄露严重, 所以是操作系统问题还是B站问题....

************************
> firefox 突然crash并且无法重新打开 124.07 版本，删Profiles重置也不生效，降级到122.0b3后可正常使用

论坛里提到可能和滚动升级的共享库版本不一致有关，但是近一个月没更新底层库和软件了（因为另一个安全验证的问题），感觉可能是打开了阿里云盘和百度云盘两个站点导致的

*********************

## Seamonkey
> Mozilla基金会另一个项目 [seamonkey](https://www.seamonkey-project.org/) 亮点在于内置IRC

****************************************

## Chrome
- 的确快,几乎没有各种兼容和诡异问题，就是内存占用高, 还有就是主题被墙,fq才能配置好

1. `Removing keychain login from Chormium` 启动命令添加如下参数 chromium --password-store=basic
1. `设置代理` chrome追加启动参数 --proxy-server=192.168.7.77:8888 --ignore-certificate-errors 
    - PAC设置 `--proxy-pac-url=http://localhost:1235/pac`

- 切换最近标签 CTRL+PgUp 和 CTRL+PgDn

使用Profiles实现多账户共存，但是保存的帐号密码都会跟随其他Profile，还是没有Firefox的Multiple Accounts丝滑。

### 主题
1. Aero Trans Brushed Metal Theme
1. Material Dark
1. Morpheon Dark
1. 炭黑+銀色金屬
1. Modern Flat

### 插件 
- [插件网](https://extfans.com/)
- [chromefor](https://www.chromefor.com/)
- [Chrome插件英雄榜](https://github.com/zhaoolee/ChromeAppHeroes)

1. Vimium C - All by Keyboard 
1. crxMouse 
1. TabsFolder
1. Cluster Window & Tab Manager
1. Chrome Download Manager
1. Fatkun 图片批量保存
1. Stylized Scrollbar 滚动条美化
1. Tab Position Options 当前tab右侧打开新tab
1. Auto Tab Discard 冻结最少使用的tab
1. Open Last Tab 按最近使用标签切换

************************

## Vivaldi
- 采用的是chrome内核 内置了很多常用插件(但是安装插件的入口关闭了) 相比于chrome更符合国内使用

vivaldi://settings
