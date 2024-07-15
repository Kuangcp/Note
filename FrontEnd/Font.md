---
title: 字体
date: 2018-12-14 09:21:37
tags: 
    - 字体
categories: 
    - 基础知识
---

💠

- 1. [字体](#字体)
    - 1.1. [基础知识](#基础知识)
    - 1.2. [资源](#资源)
    - 1.3. [Tips](#tips)
        - 1.3.1. [使用字体保护网页敏感信息](#使用字体保护网页敏感信息)
- 2. [符号](#符号)
    - 2.1. [制表符](#制表符)
- 3. [个人习惯](#个人习惯)
    - 3.1. [操作系统默认字体](#操作系统默认字体)
    - 3.2. [编辑器](#编辑器)
    - 3.3. [IDEA](#idea)
    - 3.4. [终端](#终端)

💠 2024-05-09 14:32:49
****************************************
# 字体
> [Deepin wiki 字体](https://wiki.deepin.org/wiki/%E5%AD%97%E4%BD%93)  
> [有哪些适合用于写代码的西文字体？](https://www.zhihu.com/question/20299865)  
> [What are the best programming fonts?](https://www.slant.co/topics/67/~best-programming-fonts)  
> [大家都用什么字体写代码的？](https://segmentfault.com/q/1010000000193004)

## 基础知识 
> ttf otf eot woff woff2 

> [参考: Web 字体简介: TTF, OTF, WOFF, EOT & SVG](https://zhuanlan.zhihu.com/p/28179203)  

1. TTF (TrueType Font) 字体格式是由苹果和微软为 PostScript 而开发的字体格式。
1. OTF (OpenType Font) 由 TTF 演化而来，是 Adobe 和微软共同努力的结果。
1. EOT (Embedded Open Type) 字体是微软设计用来在 Web 上使用的字体。
1. WOFF (Web Open Font Format) 本质上是 metadata + 基于 SFNT 的字体（如 TTF、OTF 或其他开放字体格式）。
1. WOFF2 是 WOFF 的下一代。 WOFF2 格式在原有的基础上提升了 30% 的压缩率。
1. SVG (Scalable Vector Graphics font) 字体格式使用 SVG 的字体元素定义。

********************************
## 资源
> Github
- [IBM字体](https://github.com/IBM/plex)`2017年发布的新字体`
- [cascadia-code](https://github.com/microsoft/cascadia-code)

- [nerd-fonts](https://github.com/ryanoasis/nerd-fonts)`系列字体图标`
- [Font-Awesome](https://github.com/FortAwesome/Font-Awesome)`一大堆字体图标`

> website
- [https://www.fontsquirrel.com/](https://www.fontsquirrel.com/)
- [https://www.urbanfonts.com/](https://www.urbanfonts.com/)
- [https://www.1001fonts.com/](https://www.1001fonts.com/)
- [https://www.ffonts.net/](https://www.ffonts.net/)

- ttf-ms-fonts
- ttf-wps-fonts

************************
## Tips
### 使用字体保护网页敏感信息
场景：网页上需要公开展示一些敏感信息（例如手机号）避免被爬虫爬取（其实只能增加一点点难度）

> 实现思路：
1. 网页直接静态化，不通过后端请求
2. 展示的值是特殊字体（例如 LeeTreeshadow）渲染后的值，而不是普通的字符串，即无法直接通过复制粘贴，读取网页HTML得到真实值
3. 字体文件还能再通过js用base64加载进来，规避F12直接看到字体ttf文件
4. 每个网页使用不同的unicode和数字映射规则，加大数据字典构造复杂度
4. 再对整体静态结果资源进行混淆

> 爬虫破解思路
1. 得到字体实际unicode字符串值
1. 数据字典构造
    1. 人工去寻找unicode值和肉眼看到的数字组成数据字典（才10个数字），但是遇到多规则就无法人工完成了
    1. 终极：通过unicode值的规律来推算出数据字典 0-9 是有序依次递增的unicode值，而手机号通常首位为1

************************

# 符号
> [符号](http://www.bangnishouji.com/fuhao/)

## 制表符
```
    ┌ 	┬ 	┐ 	  	┏ 	┳ 	┓ 	  	╒ 	╤ 	╕ 	  	╭ 	─ 	╮
    ├ 	┼ 	┤ 	  	┣ 	╋ 	┫ 	  	╞ 	╪ 	╡ 	  	│ 	╳ 	│
    └ 	┴ 	┘ 	  	┗ 	┻ 	┛ 	  	╘ 	╧ 	╛ 	  	╰ 	─ 	╯
    ┏ 	┳ 	┓ 	  	┏ 	━ 	┓ 	  	┎ 	┰ 	┒ 	  	┍ 	┯ 	┑
    ┣ 	╋ 	┫ 	  	┃ 	  	┃ 	  	┠ 	╂ 	┨ 	  	┝ 	┿ 	┥
    ┗ 	┻ 	┛ 	  	┗ 	━ 	┛ 	  	┖ 	┸ 	┚ 	  	┕ 	┷ 	┙
    ┏ 	┱ 	┐ 	  	┌ 	┲ 	┓ 	  	┌ 	┬ 	┐ 	  	┏ 	┳ 	┓
    ┡ 	╃ 	┤ 	  	├ 	╄ 	┩ 	  	┟ 	╁ 	┧ 	  	┞ 	┴ 	┦
    └ 	┴ 	┘ 	  	└ 	┴ 	┘ 	  	┗ 	╁ 	┛ 	  	└ 	┴ 	┘
    ─ 	━ 	┄ 	┅ 	┈ 	┈ 	╲ 	  	  	  	  	  	  	  	 
    │ 	┃ 	┆ 	┇ 	┊ 	┋ 	╱ 	  	  	  	  	  	  	  	 
```

************************

# 个人习惯
## 操作系统默认字体
- 微软雅黑
- Adobe 楷体 Std

## 编辑器
- Fira Code Retina
- IBM Plex Mono SemiBold [Github](https://fontmeme.com/fonts/ibm-plex-mono-font/)
- Cascadia-Code [Github](https://github.com/microsoft/cascadia-code)

## IDEA
- Roboto Mono Medium `Appearance custom font`
- IBM Plex Mono SemiBold `Editor`
    - JetBrainsMono 开启连字符

## 终端
- Cascadia Mono PL 
- Source Code Pro for Powerline
    - 并且 + [Powerline](https://github.com/powerline/powerline) + Awesonme 的 Bold 最适合ZSH的 Bullet Train 主题
- Droid Sans Mono for Powerline
- Roboto Mono for Powerline Bold
- JetBrainsMono Nerd Font Mono Regular

************************

- [fonts](https://github.com/powerline/fonts)`终端中常用字体`
- [FiraCode](https://github.com/tonsky/FiraCode)
