---
title: 高效的Linux
date: 2019-04-18 22:04:15
tags: 
    - Effective
categories: 
    - Linux
    - WIKI
---

💠

- 1. [高效的Linux](#高效的linux)
    - 1.1. [效率工具](#效率工具)
        - 1.1.1. [协作工具](#协作工具)
        - 1.1.2. [目录跳转](#目录跳转)
        - 1.1.3. [xdotool](#xdotool)
        - 1.1.4. [rofi](#rofi)
        - 1.1.5. [远程工具](#远程工具)
    - 1.2. [零散工具集合](#零散工具集合)
        - 1.2.1. [剪贴板管理](#剪贴板管理)
    - 1.3. [硬件检测工具](#硬件检测工具)
    - 1.4. [文本处理](#文本处理)
    - 1.5. [文件操作](#文件操作)
    - 1.6. [安全工具](#安全工具)
        - 1.6.1. [gpg](#gpg)
        - 1.6.2. [JumpServer](#jumpserver)
- 2. [多媒体](#多媒体)
    - 2.1. [ffmpeg](#ffmpeg)
    - 2.2. [图片处理](#图片处理)
        - 2.2.1. [ImageMagick](#imagemagick)
            - 2.2.1.1. [convert](#convert)
            - 2.2.1.2. [多图操作](#多图操作)
        - 2.2.2. [asciinema](#asciinema)
        - 2.2.3. [图片浏览器](#图片浏览器)
        - 2.2.4. [截图](#截图)
        - 2.2.5. [录屏](#录屏)
    - 2.3. [视频](#视频)
    - 2.4. [音频](#音频)
    - 2.5. [PDF](#pdf)
- 3. [运行 Windows 应用](#运行-windows-应用)
- 4. [日常应用](#日常应用)
    - 4.1. [Office](#office)
        - 4.1.1. [QQ](#qq)
        - 4.1.2. [wechat](#wechat)
        - 4.1.3. [wework](#wework)
- 5. [外设](#外设)
    - 5.1. [鼠标](#鼠标)
- 6. [Tips](#tips)

💠 2025-05-13 14:25:46
****************************************
# 高效的Linux

> [Awesome Linux Software](https://github.com/luong-komorebi/Awesome-Linux-Software)  

> [trimstray/the-book-of-secret-knowledge: A collection of inspiring lists, manuals, cheatsheets, blogs, hacks, one-liners, cli/web tools and more.](https://github.com/trimstray/the-book-of-secret-knowledge)`很完备的软件列表`  

## 效率工具

> 提高工作和开发效率

`通知提醒`
> [Desktop notifications](https://wiki.archlinux.org/index.php/Desktop_notifications) | [xfce notify-send ](https://docs.xfce.org/apps/notifyd/preferences)
> [Desktop Notifications Specification](https://developer.gnome.org/notification-spec/#protocol)
> [Notification Development Guidelines](https://wiki.ubuntu.com/NotificationDevelopmentGuidelines)

> [Github notify-send.sh](https://github.com/vlevit/notify-send.sh)

### 协作工具

**synergy**

> 多系统间共享键鼠

**scrpy**

> PC远程操作安卓

[scrcpy](https://github.com/Genymobile/scrcpy)
- [操作流程](http://blog.lujun9972.win/blog/2019/03/20/%E4%BD%BF%E7%94%A8scrcpy%E6%8E%A7%E5%88%B6%E4%BD%A0%E7%9A%84%E6%89%8B%E6%9C%BA/)

> USB 连接方式  

推荐使用USB连接，这样操作起来比较流畅。手机通过USB连接到PC上,在弹出的USB用途中选择 传输文件(MTP)

> WIFI 方式连接

- 确保PC和手机在同一Wifi中
- 手机先通过USB与PC相连
- 在PC上运行 `adb tcpip 端口`, 令手机开启端口
- 断开手机和PC的USB连接
- 在PC上运行 `adb connect 手机IP:端口`
- 运行scrcpy

> 使用技巧

- 鼠标左键: 模拟点击
- 鼠标右键/Ctrl+b: 返回上一页
- Ctrl+s: 切换app
- 手机录屏: scrcpy --record file.mp4
- 帮助信息: scrcpy --help
- 远程成功并关闭设备屏幕: scrcpy --turn-screen-off

### 目录跳转

**`Autojump`**

> 统计cd 目录，方便目录跳转  *shrc 中要有 : `. /usr/share/autojump/autojump.sh`

- `apt install autojump` 设置为自动运行 `echo '. /usr/share/autojump/autojump.sh' >> ~/.bashrc`
  - `j -v` 查看安装版本
  - `j --stat` 查看统计信息
  - `j --help`
  - `jo code` 打开code文件夹
  - `jco c` 打开子目录
- `ls -l ~/.local/share/autojump/` 统计信息的目录，清除就相当于卸载重装了

**`z.lua`**

> [Github](https://github.com/skywind3000/z.lua)   与 Autojump 类似, 性能更好

- `pip install qrcode`
  - *qr --help* 终端内生成二维码

`fd`

Simple, fast and user-friendly alternative to find

`skim`

Fuzzy Finder in Rust!

`alias cds='cd $(fd ".*" -t d | sk)'` 模糊搜索跳转进目录

### xdotool 
command-line X11 automation tool `可以控制指定窗口激活关闭，最大最小化，输入快捷键等`

> 将该脚本配置为快捷键后，实现效果：激活已有终端的窗口，或者启动终端
```sh 
  #!/bin/bash

  tmd=xfce4-terminal

  PID=$(pgrep -x $tmd)
  if [[ $PID -ne "" ]]
  then
      xdotool windowactivate `xdotool search --pid $PID | tail -1`
  else
      $tmd
  fi
```

### rofi
[Github rofi](https://github.com/davatorium/rofi) 窗口切换

设置 `rofi -show window` 快捷键为 右Alt

### 远程工具
[rdesktop and xfreerdp](https://www.joxrays.com/linux-rdp-windows/)

rdesktop xfreerdp

************************

## 零散工具集合
> 通常会安装到 /usr/bin/*  目录下

- sudo 是需要安装的
    1. `alias sudo='sudo'` 能够在别名上使用 sudo *神奇*
- md5sum 报文摘要算法 Message-Digest Algorithm 5 的实现
    - `printf 'Who?123' | md5sum`
    - `md5sum file` 计算出md5值
    - `md5sum -c file.md5` file 和 file.md5 在同一目录下, 执行这个命令就是检查md5是否匹配, 确保文件的完整性和正确性
- sha1sum sha256sum *用法和 md5sum 一致*
- last _查看Linux登录信息_
    - last -n 5 最近五次登录
- w | uptime _查看启动情况_
- colrm
    - ps | clorm 20 30 `colrm` _删除输出的20 到30 列_

- figlet 字符转ascii图
- logkeys 记录键盘输入 [Github](https://github.com/kernc/logkeys)
- expect [用于自动输入密码](http://www.cnblogs.com/iloveyoucc/archive/2012/05/11/2496433.html)
- [WTF](https://wtfutil.com) | [Github Repo](https://github.com/senorprogrammer/wtf)
    - 丰富的功能, 一个方便的终端控制面板
- when-changed 监控文件变化 执行命令 pip install when-changed
- dircolors [Linux dircolors命令](http://www.runoob.com/linux/linux-comm-dircolors.html) `用于设置 ls 命令输出时的色彩`
- gtypist 用于练习打字
- watch 周期执行命令并输出

- `uniq` 统计出现次数 `cat log.log | grep WARN | awk '{print $5}' | sort | uniq -c`
- `starDict` 终端内字典
- [upx](https://github.com/upx/upx) 压缩可执行文件

https://kbumsik.io/using-ipad-as-a-2nd-monitor-on-linux
https://snapdensing.com/2020/04/07/ipad-as-an-extended-screen-in-linux/

**进程管理**

gnome-system-monitor  
Supervisor 进程监控管理  

### 剪贴板管理
> [参考: 面向 Linux 的 10 款最佳剪贴板管理器](https://linux.cn/article-7329-1.html)
- CopyQ，Manjaro 的 clipman

- xclip
    - `cat README.md | xclip -sel clip` 将文件复制到剪贴板
- xsel
    - `cat a.md | xsel -b` _将文件所有内容复制到剪贴板_ 但是处理大文件时会失效 xclip 更有效
- [Clipboard](https://github.com/Slackadays/Clipboard)`终端操作剪贴板复制粘贴`

************************

## 硬件检测工具
> [Linux系统硬件信息检测工具hwinfo — Cloud Atlas beta 文档](https://cloud-atlas.readthedocs.io/zh-cn/latest/linux/server/hardware/hwinfo.html)  

> 硬盘

- CrystalDiskMark
- [KDiskMark](https://github.com/JonMagon/KDiskMark)

> smartmontools 
- 检测健康状况 `smartctl -Hc /dev/sda9`
- 查看全部信息 `smartctl -a /dev/sda`

************************

## 文本处理

- `wc` 单词 行数 统计
- `ccze` 日志高亮
- `lolcat` 给输出包装上彩虹颜色 有 c python ruby 版
- choose _方便的cut_

> `在当前目录下, 快速全文内容搜索`

- ag _The Silver Searcher_
  - ubuntu:silversearcher-ag  alpine:the_silver_searcher
  - [The Silver Searcher](https://github.com/ggreer/the_silver_searcher)
- rg _ripgrep_
- glow markdown renderer

************************

## 文件操作

`iconv`

> 可以将一种已知的字符集文件转换成另一种已知的字符集文件

例如 将git仓库内所有Java文件 GBK 转 UTF8 `git ls-files | grep "\.java" | tee  | xargs -I {}  iconv -f GBK -t UTF-8 {} -o {}`

`zssh`
> [参考 zssh, rz, sz互相传输](http://blog.csdn.net/ygm_linux/article/details/32321729)

## 安全工具

### gpg
> [参考博客](http://www.ruanyifeng.com/blog/2013/07/gpg.html)

- 生成的过程, 输入相关的提示信息, 最后输完密码后需要输入随机字符, 就也是按照提示, 但是1.4是正常的, 其他的直接假死,不是很理解这种操作

### JumpServer
> [Github](https://github.com/jumpserver/jumpserver)

************************

# 多媒体

## ffmpeg

> [Official Site](http://ffmpeg.org/ffmpeg.html)

- 查看属性 `ffprobe -pretty target.mp4`

> m3u8 URL 转换为mp4

- `ffmpeg -i http://xxx.m3u8 -c copy -bsf:a aac_adtstoasc output.mp4`
- 获取视频中的音频 `ffmpeg -i input.mp4 -vn -y -acodec copy output.m4a`
- 去掉视频中的音频 `ffmpeg -i input.mp4 -an output.mp4`
- 合并视频 `ffmpeg -f concat -safe 0 -i file.cfg  -c copy result.mp4`
  - file.cfg 内容为多行文件 : `file '/path/to/file'`
- 截取视频 `ffmpeg -ss 00:00:00 -t 00:00:30 -i input.mp4 -vcodec copy -acodec copy output.mp4`
  - `-ss` 开始时间 `-t` 截取时长  `-q 0` 无损 `-c copy`表示不必重新编码

## 图片处理

- byzanz 录制屏幕为gif

### ImageMagick
> ImageMagick® is a free, open-source software suite, used for editing and manipulating digital images  
> [Github: ImageMagick](https://github.com/ImageMagick/ImageMagick)  

1. display

#### convert
> convert between image formats as well as resize an image, blur, crop, despeckle, dither, draw on, flip, join, re-sample, and much more

`convert 源文件 [参数] 目标文件`
- 格式转换： convert a.png a.jpg 

- 将图片转换成指定大小 这是保持比例的 `convert -resize 600X600 src.jpg dst.jpg` 中间是字母X
    - 如果不保持比例，就在宽高后加上感叹号
    - 可以只指定高度，那么宽度会等比例缩放 `convert -resize 400 src.jpg dst.jpg`
    - 还可以按百分比缩放 `convert page200.png -resize 50% page100.png`

> svg to ico 两种方式
- `magick convert -background none icon.svg -define icon:auto-resize icon.ico`
- `convert -background none icon.svg -define icon:auto-resize icon.ico`

#### 多图操作
- 若干图片合并并转PDF `convert origin1.jpg origin2.jpg target.pdf`
- [imagemagick 图片合并_convert 多图拼接-CSDN博客](https://blog.csdn.net/qq_24127015/article/details/86525305)  
  - 水平方向拼接,纵向则是 -append `magick convert +append  2024* aa.jpg`
  - composite 方式
    - 生成空白图片 `magick -size 1920x1200 xc:none dest0.jpg`
    - 按坐标放入两张图片 `magick composite -geometry +0+0 u-0.jpg dest0.jpg dest0.jpg`  `magick composite -geometry +1000+0 u-1.jpg dest0.jpg dest0.jpg`

> 批量修改 
如果没有 -path 语句，新生成的 png 文件将会覆盖原始文件 [参考博客](http://www.cnblogs.com/jkmiao/p/6756929.html)
- `mogrify -path newdir -resize 40X40 *.png` 把png图片全部转成40X40大小并放在新文件夹下
- `mogrify -path newdir -format png  *.gif` 将所有gif转成png放在新目录下

### asciinema

- [asciinema](https://asciinema.org) `终端屏幕录制和分享网`
- 执行 `asciinema`或 `asciinema rec` 即可开始录制
- 要注册就运行 `asciinema auth` 进入输出的网址，填邮箱和名字即可（每次登录都要这样。或者使用邮件来确认，麻烦ing）

### 图片浏览器

1. Nomacs 快
2. gThumb
3. Eye of GNOME Image Viewer 功能比上面多了一点

### 截图

Flameshot 截图工具  类似于 snipaste
- Ctrl 鼠标滚动 调整线条粗细
- Ctrl Alt S： 截图 (注意某些交互性场景，截图会导致失去焦点从而无法截到，例如网页的下拉选项，此时可以不使用快捷键而是鼠标点托盘的图标触发截图，可绕过这个问题)
- Alt Q ：pin
- 截图并OCR识别中文 `flameshot gui --raw | tesseract -l chi_sim stdin stdout | xclip -in -selection clipboard`
    - 可以绑定快捷键到这个命令上，如果不生效可以将命令创建为sh文件，快捷键绑定到这个sh文件上。
    - [OCR to clipboard hook for selections · Issue #702 · flameshot-org/flameshot](https://github.com/flameshot-org/flameshot/issues/702)  

deepin-screenshot

### 录屏

- `kazam` 支持选进程窗口，输出mp4
- `peek` 顶层窗口选择录屏区域，输出 gif 有较高压缩比

************************

## 视频

> [参考: Top 10 Best Linux Video Players](https://www.ubuntupit.com/top-10-best-linux-video-players-enjoy-ultimate-movie-music/)

- [百度网盘命令客户端](https://github.com/iikira/BaiduPCS-Go) `Go语言实现`
- [you-get](https://github.com/soimort/you-get)

## 音频

- [netease-cloud-music-gtk](https://github.com/gmg137/netease-cloud-music-gtk)
- audacious 音频播放
- lollypop GNOME 环境简单应用
- Audacity 音频剪辑

************************

## PDF
`evince` GNOME PDF阅读器应用

`ghostscript`

> [ghostscript.com](https://ghostscript.com/)
> [参考: Ubuntu上压缩PDF文件的方法](https://blog.csdn.net/lx_ros/article/details/79887562)

`gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dBATCH -dQUIET -sOutputFile=output.pdf input.pdf`

************************

`pdftk`

> [pdflabs](https://www.pdflabs.com/) | [Docs](https://www.pdflabs.com/docs/pdftk-cli-examples/)

************************

`pdfunite`

> Portable Document Format (PDF) page merger

- pdfunite 1.pdf 2.pdf merged.pdf

************************

> [smallpdf.com](https://smallpdf.com) 在线处理


************************
# 运行 Windows 应用

- [Bottles](https://github.com/bottlesdevs/Bottles)
- [wine](https://github.com/wine-mirror/wine)
- [deepin-wine](https://github.com/zq1997/deepin-wine)

************************

# 日常应用
## Office
### QQ
> [QQ Linux](https://im.qq.com/linuxqq/index.shtml)

### wechat
[wechat-universal-bwrap](https://aur.archlinux.org/packages/wechat-universal-bwrap)  
> [微信 Linux 测试版](https://linux.weixin.qq.com/)  

### wework
- [企业微信](https://aur.archlinux.org/packages/deepin-wxwork/)

************************

# 外设
> [键鼠共享](https://github.com/debauchee/barrier)  
> [xdotool](https://github.com/jordansissel/xdotool)`模拟键盘和鼠标操作的命令行工具`  

## 鼠标
- solaar Logitech鼠标Options修改

************************

# Tips

- 问题： `sudo echo "Text I want to write" > /path/to/file` 失败

> [参考: &#34;sudo echo&#34; does not work together in Ubuntu ](https://blogs.oracle.com/joshis/sudo-echo-does-not-work-together-in-ubuntu-another-waste-of-time-issue)
> [stack over flow](https://stackoverflow.com/questions/84882/sudo-echo-something-etc-privilegedfile-doesnt-work-is-there-an-alterna)

- `sudo sh -c 'echo "Text I want to write" >> /path/to/file'`
- `echo "Text I want to write" | sudo tee -a /path/to/file > /dev/null`

