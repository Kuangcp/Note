---
title: 浏览器
date: 2018-12-15 12:11:56
tags: 
categories: 
    - 工具
---

**目录 start**

1. [浏览器](#浏览器)
    1. [FireFox](#firefox)
        1. [开发版本](#开发版本)
        1. [必备插件](#必备插件)
        1. [配置](#配置)
        1. [使用](#使用)
        1. [Tips](#tips)
    1. [Seamonkey](#seamonkey)
    1. [Chrome](#chrome)
        1. [主题](#主题)
        1. [插件](#插件)
    1. [Vivaldi](#vivaldi)
    1. [Opera](#opera)

**目录 end**|_2020-11-02 23:23_|
****************************************
# 浏览器
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

### 开发版本
> [开发者版本链接](https://www.mozilla.org/zh-CN/firefox/developer/) | [开发工具](https://firefox-dev.tools/)  
> [使用说明文档](https://developer.mozilla.org/zh-CN/docs/Tools?utm_source=devtools&utm_medium=tabbar-menu)

### 必备插件
> [开发自己的插件](https://github.com/Kuangcp/LearnWebExtension)

1. 附加组件管理器: 只有正式版会内置该插件, 别的版本都没有, 插件的功能是 地址栏二维码,拖拽链接,
    - 如果想在开发版以及Nightly上用上该插件, 只需要去 ~/.mozilla/ 下找到正式版的配置文件里的 extension 目录就能找到 cpmanager.xpi 了, 拖入浏览器就可以了
    - 但是这个组件只保证正式版是正常的, 其他版本则要看运气

- `Saka Key` 快捷键神器 大幅度脱离鼠标 [官方文档](https://key.saka.io/)
    1. 浏览器默认: 脱离输入框焦点 _Esc_ | 切换标签 _ctrl-Tab_  _shift-ctrl-Tab_ | 关闭标签 _ctrl-w_
    1. 滑动: 
        - 下滑 `d/j` 上滑 `s/k `
        - 上下滑半屏幕 `Shift d/s` | 上下滑全屏 `Shift j/k` 
        - 滑到底/顶 `Shift-g` / `gg`
        - 滑左/右 `alt-s or alt-k` / `alt-d or alt-j`
    1. 缩放: 
        - 放大/缩小 `z/shift-z` | 重置大小 `shift-alt-z`
    1. 前进/后退: 
        - `cc/vv` | 跳上级URL `uu` | 跳URL域名 `u shift-u`
    1. 标签页: 
        - 新建 `t` | 恢复关闭 `shift t` | 复制 `b`
        - 关闭 `xx` | 关闭其他 `x shift x` | 关闭左边 `x [` | 关闭右边 `x ]`
        - 刷新 `rr` | 刷新全部标签 `r shift r` | 深度刷新 `shift r shift r `
        - 切换: 左右 `q/w` 或者 `[/]` | 第一个/最后一个 `1/0`或者`shift-q`/`shift-w or 0 `
        - 移动: 左右 `i/o` 或者 `shift-[` / `shift-]` 第一个/最后一个 `shift-i/shift-o` 或者 `alt-[/alt-]`
        - 静音: `m` 静音所有标签 `shift-m`
    1. 窗口: 
        - 新建 `n` | 新建隐私 `shift n`
    1. 页面上所有页面链接 `ff` _神操作_ [文档](https://key.saka.io/tutorial/clicking_and_link_hints)
    1. 传递快捷键即绕过插件的事件监听 `;` [文档](https://key.saka.io/tutorial/pass_keys)
        - 比如要在网页上敲英文的时候,就需要每次都要输入分号,才能绕过监听, 真是麻烦
    1. [剪贴板](https://key.saka.io/tutorial/clipboard): 复制当前页面的URL:`yy`
        - 当前标签页打开链接 `yf`| 后台打开 `yb` | 新窗口打开 `yn` | 隐私窗口 `y shift-n`

- `Vimium`
    - Vim风格操作浏览器日常操作，命令简单，基本功能一致
    - 可以按域名配置启用禁用规则
    - FF113版本不能正常工作了
- `Vimium C - All by Keyboard`
    - Vim风格操作浏览器日常操作
1. `Dark Reader` 设置网页黑夜模式
1. `Greasemonkey` 传说中的油猴, 可以自己写脚本 [wiki](https://wiki.greasespot.net/User_Script_Hosting)
1. `New Tab Tools` 新建标签页的自定义工具 
1. `cliget` 能将下载中的任务转化为 curl wget命令 牛
1. `eolinker` 接口测试工具
1. `Simple Tab Groups` 懒加载式隔离标签组
1. `RESTer` rest客户端工具
1. `Download all Images`下载图片
1. `octotree` github 目录查看
1. `Web Developer` 各种Web调试开发工具
1. `One Tab` tab归组,十分好用
1. `Remove Cookies Button`
1. `滴答清单` 全平台可使用
1. `Auto Reload Tab` 定时自动刷新标签页
1. `ReloadMatic` 定时自动刷新
1. `轻灵划译` 即刻翻译, 多种平台
1. `Tab Counter` Tab计数 开发者 WaldiPL
1. `Elasticvue` Elasticsearch 插件

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

1. 当前标签页右边打开新标签页: 
    - 打开 `about:config?filter=browser.tabs.insertAfterCurrent` 新建Bool类型, 设置为true

1. 网页重定向次数限制 默认 20 `network.http.redirection-limit` 设置为0就禁止了网页的重定向

1. 内存资源占用大
    1. `about:memory` 查看内存情况
    1. `dom.ipc.processCount` 降低进程数
    1. `browser.tabs.remote.autostart` 设置 false

### 使用
1. 地址栏 `@bing @baidu...` 即可使用指定的搜索引擎进行搜索
1. 地址栏 `* Java` 即可在所有书签中搜索 Java
1. 地址栏 `% Java` 就可以在已打开的标签页中搜索Java

### Tips
> 在B站看视频 看久了就会发现内存爆炸, 曾经全屏看LOL直播连续6个小时, 然后结束的时候发现出不去了, 要等好久  
> 等了半天打开htop一看firefox 占用内存 6g, 负载 297, 怪不得风扇转这么大声...  
> 原以为是Firefox 的问题, 用 Chrome 看B站一样的场景, 看了没多久就是CPU负载高 内存泄露严重, 所以是操作系统问题还是B站问题....

*********************

## Seamonkey
> Mozilla基金会另一个项目 [seamonkey](https://www.seamonkey-project.org/) 亮点在于内置IRC

****************************************

## Chrome
- 的确快,几乎没有各种兼容和诡异问题，就是内存占用高, 还有就是主题被墙,fq才能配置好

1. `Removing keychain login from Chormium` 启动命令添加如下参数 chromium --password-store=basic
1. `设置代理` chrome追加启动参数 --proxy-server=192.168.7.77:8888 --ignore-certificate-errors 

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

1. Saka key
1. cVim [Github](https://github.com/1995eaton/chromium-vim)
1. crxMouse 
1. TabsFolder
1. Cluster Window & Tab Manager
1. Chrome Download Manager
1. Fatkun 图片批量保存

************************

## Vivaldi
- 采用的是chrome内核 内置了很多常用插件 相比于chrome更符合国内使用

- vivaldi://settings

## Opera
- 定制化比较多，但是设置不开放
