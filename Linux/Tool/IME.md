---
title: 输入法
date: 2018-12-15 12:04:24
tags: 
categories: 
    - 工具
---

💠

- 1. [IME](#ime)
- 2. [fcitx](#fcitx)
    - 2.1. [Tips](#tips)
- 3. [ibus](#ibus)
- 4. [常用输入法](#常用输入法)
    - 4.1. [Rime](#rime)
    - 4.2. [搜狗](#搜狗)
    - 4.3. [Google拼音](#google拼音)
            - 4.3.0.1. [小小输入法](#小小输入法)

💠 2024-10-13 17:59:27
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

## Tips 
> fcitx + sogou 输入法经常出现 `单CPU 100%满载`
- 在搜狗输入法 中打开 fcitx 设置, 插件中 关闭 搜狗云 插件, 即可解决问题

> 特定软件 无法输入中文，无法使用剪切板， 意味着fcitx未激活
需要看软件是否支持进程内加脚本执行，例如 IDEA的 idea.sh WPS的 /usr/bin/et , 都可以通过在脚本首行添加 source ~/.xprofile 解决问题

************************

# ibus

# 常用输入法
## Rime
> [rime](https://rime.im/)  中州韵 

响应速度快，配置方式均为配置文件方式，扩展性高

Ctrl ` 进入设置

> [Rime 输入法安装和使用指北](https://blog.mikelyou.com/2020/07/31/rime-input/)  

> 双拼方案
- yay rime-double-pinyin 
[rime 输入法小鹤双拼配置](https://blog.moe233.net/posts/3c46778c/)
[自然码双拼](https://jingyan.baidu.com/article/64d05a027cac09de55f73b18.html)

> 自定义词库
- [导入词库](https://gist.github.com/lotem/5443073)  
- [rime 词库](https://github.com/mutoe/rime)`emoji,计算机等生活词库`  
- [Rime 擴充詞庫](https://github.com/rime-aca/dictionaries)  
- [Dict.yml](https://github.com/LEOYoon-Tsaw/Rime_collections/blob/master/Rime_description.md#dictyaml-%E8%A9%B3%E8%A7%A3)
- [RimeConfig](https://github.com/SaboZhang/RimeConfig)  

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

