`目录 start`
 
- [浏览器](#浏览器)
    - [FireFox](#firefox)
        - [开发版本](#开发版本)
        - [必备插件](#必备插件)
        - [配置](#配置)
        - [使用](#使用)
    - [seamonkey](#seamonkey)
    - [Chrome](#chrome)
        - [主题](#主题)
    - [Vivaldi](#vivaldi)
    - [Opera](#opera)

`目录 end` |_2018-09-09_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 浏览器
## FireFox
> [所有桌面版](https://www.mozilla.org/zh-CN/firefox/channel/desktop/) | [所有正式版](https://www.mozilla.org/en-US/firefox/releases/)
> [正式版本和夜更新版FTP下载地址](http://ftp.mozilla.org/pub/firefox) | [所有开发者版本](http://ftp.mozilla.org/pub/devedition/releases/)

`57为全新的Quantum版本， 因为插件标准的缘故和之前的56版本插件不兼容`

- 分为 正式版， beta， Nightly 开发版 
- 如果要配置多个火狐在电脑上 终端中 `./firefox -P` 就会进入配置文件的编辑（关闭所有火狐的情况下）
    - 新建一个就好了，之后就用新建的打开该火狐`./firefox -P name`
    - 如果要同时运行多种版本的火狐 加上`--no-remote`参数，但是我这个deepin不要诶，只要配置不同即可，但是Ubuntu mint加上也没有用

- 火狐和Chrome都支持在控制台的网络中直接右击一个请求然后复制, 就可以出来复制成cURL命令的选项, 比较好用

> [火狐性能优化贴](https://www.xzcblog.com/post-47.html)

### 开发版本
> [开发者版本链接](https://www.mozilla.org/zh-CN/firefox/developer/) | [开发工具](https://firefox-dev.tools/)  
> [使用说明文档](https://developer.mozilla.org/zh-CN/docs/Tools?utm_source=devtools&utm_medium=tabbar-menu)

### 必备插件
> [开发自己的插件](https://github.com/Kuangcp/LearnWebExtension)

- `Saka Key` 快捷键神器 大幅度脱离鼠标 [官方文档](https://key.saka.io/)
    1. 浏览器默认: 脱离输入框焦点 _Esc_ | 切换标签 _ctrl-Tab_  _shift-ctrl-Tab_ | 关闭标签 _ctrl-w_
    1. 滑动: 下滑 `d/j` 上滑 `s/k `
        - 上下滑半屏幕 `Shift d/s` | 上下滑全屏 `Shift j/k` 
        - 滑到底/顶 `Shift-g` / `gg`
        - 滑左/右 `alt-s or alt-k` / `alt-d or alt-j`
    1. 缩放: 放大/缩小 `z/shift-z` | 重置大小 `shift-alt-z`
    1. 前进/后退: `cc/vv` | 跳上级URL `uu` | 跳URL域名 `u shift-u`
    1. 标签页: 新建 `t` | 恢复关闭 `shift t` | 复制 `b`
        - 关闭 `xx` | 关闭其他 `x shift x` | 关闭左边 `x [` | 关闭右边 `x ]`
        - 刷新 `rr` | 刷新全部标签 `r shift r` | 深度刷新 `shift r shift r `
        - 切换: 左右 `q/w` 或者 `[/]` | 第一个/最后一个 `1/0`或者`shift-q`/`shift-w or 0 `
        - 移动: 左右 `i/o` 或者 `shift-[` / `shift-]` 第一个/最后一个 `shift-i/shift-o` 或者 `alt-[/alt-]`
        - 静音: `m` 静音所有标签 `shift-m`
    1. 窗口: 新建 `n` | 新建隐私 `shift n`
    1. 页面上所有页面链接 `ff` _神操作_ [文档](https://key.saka.io/tutorial/clicking_and_link_hints)
    1. 传递快捷键即绕过插件的事件监听 `;` [文档](https://key.saka.io/tutorial/pass_keys)
        - 比如要在网页上敲英文的时候,就需要每次都要输入分号,才能绕过监听, 真是麻烦
    1. [剪贴板](https://key.saka.io/tutorial/clipboard): 复制当前页面的URL:`yy`
        - 当前标签页打开链接 `yf`| 后台打开 `yb` | 新窗口打开 `yn` | 隐私窗口 `y shift-n`

1. `Greasemonkey` 传说中的油猴, 可以自己写脚本 [wiki](https://wiki.greasespot.net/User_Script_Hosting)
1. `New Tab Tools` 新建标签页的自定义工具 有一定bug
1. `cliget` 能将下载中的任务转化为 curl wget命令 牛
1. `eolinker` 接口测试工具
1. `Simple Tab Groups` 58版本有bug
1. `rester` rest客户端工具
1. `Download all Images`下载图片
1. `octotree` github 目录查看
1. `Web Developer` 各种Web调试开发工具
1. `One Tab` tab归组,十分好用
1. `Remove Cookies Button`
1. `围脖是个好图床哟` 方便的图床,但是要登录微博
1. `滴答清单` 全平台可使用
1. `Auto Reload Tab` 定时自动刷新标签页
1. `轻灵划译` 即刻翻译, 多种平台

### 配置
> 主要是 about:config 

1. 配置火狐访问80以外的端口
    1. 地址栏 : `about:config` 
    1. 右键新建字符串 `network.security.ports.banned.override` 
    1. 输入值 81,88,98 也可以是 6000-6005, 省事就 0-65535(不建议)

1. 对于自己喜欢多开火狐的习惯, 整理如下习惯
    - 安装开发版本, 使用一个默认的配置
    - 使用开发版本的可执行文件, 配置一个新的配置目录, 也就是一个新的火狐
1. 前者是重度使用(往往很多标签20+), 常用的标签页全部固定, 一些TODO的tab也放在这里, 用于开发和娱乐(1000M-2000M)
1. 后者是轻度使用(开10个以下标签), 仅在内存不够时, 只用于内存不足时开发必需 (一般400M左右)

### 使用
1. 地址栏 `@bing` @baidu... 即可使用指定的搜索引擎进行搜索
1. 地址栏 `* Java` 即可在所有书签中搜索 Java
*********************
## seamonkey
> Mozilla基金会另一个项目 [seamonkey](https://www.seamonkey-project.org/) 亮点在于内置IRC

****************************************
## Chrome
- 的确快,几乎没有各种兼容和诡异问题，就是内存占用高, 还有就是主题被墙,fq才能配置好

### 主题
1. Aero Trans Brushed Metal Theme
1. Material Dark
1. Morpheon Dark
1. 炭黑+銀色金屬
1. Modern Flat
************

## Vivaldi
- 感觉采用的是chrome内核，做的更漂亮了，而且是内置了很多常用插件，的确很方便，相比于chrome更符合国内使用

## Opera


