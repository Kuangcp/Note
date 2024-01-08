---
title: 输入法
date: 2018-12-15 12:04:24
tags: 
categories: 
    - 工具
---

**目录 start**

1. [IME](#ime)
1. [fcitx](#fcitx)
1. [ibus](#ibus)
1. [常用输入法](#常用输入法)
    1. [Rime](#rime)
    1. [搜狗](#搜狗)
    1. [Google拼音](#google拼音)
            1. [小小输入法](#小小输入法)
1. [Tips](#tips)

**目录 end**|_2021-02-03 17:25_|
****************************************
# IME
> 输入法

主要的输入法框架分为 fcitx ibus

# fcitx 
> fcitx  fcitx-im  fcitx-configtool

> [wiki: fcitx](https://wiki.archlinux.org/index.php/Fcitx_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

`~/.xprofile`
```sh
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
```

- 设置里面 Global config -> Program -> Active 

************************

# ibus

# 常用输入法
## Rime
> [rime](https://rime.im/)  中州韵 

响应速度快，配置方式均为配置文件方式，扩展性高

Ctrl ` 进入设置

> 双拼方案
- yay rime-double-pinyin 

[rime 输入法小鹤双拼配置](https://blog.moe233.net/posts/3c46778c/)

[自然码双拼](https://jingyan.baidu.com/article/64d05a027cac09de55f73b18.html)

## 搜狗
> [Official Site](https://pinyin.sogou.com/linux/)  

> [参考: Linux安装搜狗拼音和谷歌拼音输入法](https://www.jianshu.com/p/429b8f75af2c)

比较良心， 一直希望百度输入法能出Linux版， 最后还是没有， 优点就是能同步账号， 云词库什么的， 但是bug比较多， 容易奔溃（可能和Deepin有关）
- Ctrl Alt B 显示/关闭 特殊字符面板


## Google拼音
> fcitx-googlepinyin

速度比较快， 但是不够聪明， 打字舒适度上没有rime好用

#### 小小输入法
[小小输入法在Deepin上的使用](https://bbs.deepin.org/forum.php?mod=viewthread&tid=138500&highlight=%E5%B0%8F%E5%B0%8F%E8%BE%93%E5%85%A5%E6%B3%95)


# Tips 
> fcitx + sogou 输入法经常出现 `单CPU 100%满载`
- 在搜狗输入法 中打开 fcitx 设置, 插件中 关闭 搜狗云 插件, 即可解决问题
