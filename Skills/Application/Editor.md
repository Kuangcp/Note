---
title: 编辑器
date: 2018-12-15 12:11:10
tags: 
    - 编辑器
categories: 
    - 工具
---

💠

- 1. [文本编辑器](#文本编辑器)
    - 1.1. [Kate](#kate)
    - 1.2. [Geany](#geany)
    - 1.3. [scite](#scite)
    - 1.4. [textadept](#textadept)
        - 1.4.1. [快捷键](#快捷键)
    - 1.5. [Sublime](#sublime)
        - 1.5.1. [快捷键](#快捷键)
        - 1.5.2. [crack](#crack)
    - 1.6. [VSCode](#vscode)
        - 1.6.1. [快捷键](#快捷键)
        - 1.6.2. [代码片段](#代码片段)
        - 1.6.3. [插件](#插件)
        - 1.6.4. [实践](#实践)
        - 1.6.5. [vscode server](#vscode-server)
    - 1.7. [Atom](#atom)
    - 1.8. [Gedit](#gedit)
    - 1.9. [notepadqq](#notepadqq)
    - 1.10. [MousePad](#mousepad)
    - 1.11. [Xed](#xed)
    - 1.12. [小书匠](#小书匠)
    - 1.13. [Moeditor/Typora/CuteMarkEd](#moeditortyporacutemarked)
- 2. [终端中的文本编辑器](#终端中的文本编辑器)
    - 2.1. [Vi/Vim](#vivim)
    - 2.2. [helix](#helix)
    - 2.3. [Nano](#nano)
    - 2.4. [Micro](#micro)
    - 2.5. [BS在线编辑器](#bs在线编辑器)
- 3. [十六进制 Hex](#十六进制-hex)

💠 2024-09-06 11:36:43
****************************************
# 文本编辑器

## Kate
> [Official site](https://kate-editor.org/) 相关: KWrite(Kate的轻量版)
 
- [安装markdown预览插件](https://github.com/antonizoon/kate-markdown)
- 码Python也挺方便，也有常用快捷键，自动提示，终端整合，而且是自动切目录


************************

## Geany
- 码C 编译方便 有Ctag辅助

************************

## scite
> 简洁的编辑器，可配置挺多，打开速度快

## textadept
> 基于前者进行开发，十分简洁，有着和sublime的外观和速度，没有他的功能强大但也没有他的烦心bug！ 但是自己定制时难度有点大
> [官方手册](https://foicica.com/textadept/manual.html)

- Github 地址[textadept](https://github.com/rgieseke/textadept/)
- 主题仓库 [textadept-themes](https://github.com/rgieseke/textadept-themes) 
_个人配置_
```lua
    if not CURSES then ui.set_theme('base16-solarized-light') end
    ui.set_theme('light', {font = 'Monospace', fontsize = 13})
    -- print(ui.size)
    -- for k,v in ipairs(ui.size) do
    -- print(k,v)
    -- end
    ui.size = {[1] = 800, [2] = 650}
```

### 快捷键
> Alt Shift 列编辑  

## Sublime 
> [常用配置](https://segmentfault.com/a/1190000002596724)

- 直接下载压缩包 `wget https://download.sublimetext.com/sublime_text_3_build_3211_x64.tar.bz2`

- 如果出现小bug，就直接删除 ～/.config 下的 sublime文件夹注意注册证书拷出来
- 中文不兼容解决方法： 3143版本号下：
    - 搜索安装插件 ChineseLocalizations 就能汉化 
    - 修改配置文件 添加`"font_face": "DeJaVu Sans Mono",` 就解决了字体错位的问题
    - 保存为项目来切换管理更为方便
- 主题安装 Boxy Theme 以及  A File Icon 就能切换多种主题了 [参考博客](https://www.zhihu.com/question/46266742)
- [配置C/C++开发环境](http://www.cnblogs.com/flipped/p/5836002.html)

**关闭自动检查升级**
- setting 中 "update_check":false

### 快捷键
> [参考: Sublime Text 3 快捷键](http://www.cnblogs.com/roadone/p/7745641.html)
> [sublime的常用快捷键](http://www.cnblogs.com/kristen-zou/p/7641158.html)

### crack
> [3143码](https://gitee.com/gin9/codes/89xfugn5dwoyr23vchikb54)

- [参考博客](http://www.cnblogs.com/hollow/p/6496469.html)
- [3143 1](https://fatesinger.com/100121) | [3143 2](https://fatesinger.com/100227) | [3176](https://fatesinger.com/100237) 

************************************

## VSCode

> [Official Site](https://code.visualstudio.com/) | [中文手册](https://jeasonstudio.gitbooks.io/vscode-cn-doc/) | [code-server](https://github.com/cdr/code-server) 
> 用户自定义配置目录 `~/.config/Code/User/`

1. vscode 书写 markdown [官方文档](https://code.visualstudio.com/Docs/languages/markdown)
1. 禁用GPU加速 ctrp+shift+p 中的 Preferences: Configure Runtime Arguments 命令
    - 加上 "disable-hardware-acceleration": true
1. 设置tab多行展示 `workbench.editor.wrapTabs`

### 快捷键
> [快捷键官方PDF说明](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)

- `Ctrl P` 快速命令
    - 直接输入文件名就是搜文件
    - `>` 作为前缀则等同 `Ctrl Shift P`
    - `#` 作为前缀则等同 `Ctrl T`
    - `@` 当前文件内标题 版本1.71.1+
- `Ctrl T ` 搜索打开所有Markdown文件的所有标题 1.25+
- `Ctrl Shift P ` 执行命令
- `Ctrl+K Ctrl+S` 设置用户快捷键  Keyboard Shortcuts
- `Ctrl Shift C `在当前打开的文件夹下打开系统默认终端
- `Ctrl Space` 智能提示 变量,代码片段... **需要注意这个快捷键和Windows以及Linux上切换输入法快捷键有冲突,修改即可**
- `Alt Shift` 列编辑
- `C S .` 显示面包屑 版本:1.26+
- `workbench.editor.wrapTabs` 启用多tab同时展示

> [参考: 快捷键大全](https://blog.csdn.net/crper/article/details/54099319)
> [参考: VS Code 使用小技巧](https://zhuanlan.zhihu.com/p/22880087)

### 代码片段
> 配置地点 文件-首选项-用户代码片段 可以新建一个代码片段  
> 默认是放在用户的配置目录下 `~/.config/Code/User/snippets/`

- [参考: VS Code 折腾记 - (6) 基本配置/快捷键定义/代码片段的录入（snippet）](https://juejin.im/post/58aeeca22f301e006cf65c8b)
- [巧用VScode“用户代码片段”来提高效率](https://www.dogxu.cn/2017/06/10/vscode-snippet/)
    - 然后自定义一下insert snippet的快捷键,就很方便使用了 个人配置为`Ctrl L`, **其实 直接 Ctrl Space 直接提示就行了**
    - 注意,每次修改片段配置文件,都需要重启Vscode才会生效最新修改...emm

### 插件
**美化**
>1. Material Icon Theme
>1. Snazzy Operator

1. vscode-icons
1. One Dark Pro
1. Gruvbox Theme

**工具**
1. Beautify
1. Prettier
1. Auto Rename Tag
1. Todo Tree 
1. GitLens 
1. LeetCode
1. vscode-proto3 
1. PlantUML
1. Markdown PDF
1. Draw.io Integration
1. vscode-mindmap
1. rainbow csv 
1. Office Viewer 类似 Typora
1. Docker 微软推出
    - 可直接修改容器内文件

### 实践
> [参考: 用Git在Visual Studio Code内进行版本控制[指导]](https://sdk.cn/news/4041)
> [参考: 使用vscocd进行python开发 ](http://www.cnblogs.com/bloglkl/archive/2016/08/23/5797805.html)

### vscode server
> [vscode-server](https://code.visualstudio.com/docs/remote/vscode-server)

[Docker: vscode-server](https://hub.docker.com/r/ahmadnassri/vscode-server)

***********************************
## Atom
> Github 推出的编辑器 [淘宝Mirror](https://npm.taobao.org/mirrors/atom)

1. 配置apm命令镜像 
`~/.atom/.atomrc`
```
registry=https://registry.npm.taobao.org/
strict-ssl=false
```
1. 或者直接clone 进行安装 在`~/.atom/packages`下clone仓库, 然后 apm install 

************************************
## Gedit
> [Github地址](https://github.com/GNOME/gedit)

- 安装markdown预览插件 `该插件早已经停止维护了，还是只用来简单的查看修改文件就好了`

## notepadqq

## MousePad

## Xed 
> [Github](https://github.com/linuxmint/xed)  

******************************

## 小书匠
> [在线使用](https://markdown.xiaoshujiang.com/) | [github地址](https://github.com/suziwen/markdownxiaoshujiang)

- 本来是很合适的，但是对文件操作不干净（引入自定义的文本和格式），文件偶尔闪退出错,终端不方便，资源占用大
    - 不适合编程适合写作,所支持的md的格式非常方便
- 快捷键
    - 加粗    `Ctrl + B` 
    - 斜体    `Ctrl + I` 
    - 引用    `Ctrl + Q`
    - 插入链接    `Ctrl + L`
    - 插入代码    `Ctrl + K`
    - 插入图片    `Ctrl + G`
    - 提升标题    `Ctrl + H`
    - 有序列表    `Ctrl + O`
    - 无序列表    `Ctrl + U`
    - 横线    `Ctrl + R`
    - 撤销    `Ctrl + Z`
    - 重做    `Ctrl + Y`

************

## Moeditor/Typora/CuteMarkEd 
> [Github:Moeditor](https://github.com/Moeditor/Moeditor)

- 书写单个md文件方便，美观，没有目录树侧栏是硬伤, 但是typora 导出很强大


**************************

# 终端中的文本编辑器
## Vi/Vim
> [Github: Vim](https://github.com/vim/vim)  
> [Vim 学习笔记](/Linux/Tool/Vim.md)

## helix
[Github: helix](https://github.com/helix-editor/helix)

************
## Nano
- 使用简单，安装占用小 类似 emacs 的快捷键操作方式

## Micro
> [Github: micro](https://github.com/zyedidia/micro)

*****************
## BS在线编辑器
- _[stackedit.io](https://stackedit.io/)_
- [Github地址](https://github.com/benweet/stackedit/)
- [小书匠](https://markdown.xiaoshujiang.com/)
- CMD编辑器

************************

# 十六进制 Hex
> 十六进制方式查看和修改二进制文件 

> [What's the best hex editor in 2023? ](https://www.reddit.com/r/hacking/comments/105mzw5/whats_the_best_hex_editor_in_2023/)  

**终端**
- 查看 hexdump xxd od hexyl
- 编辑 hexedit vim

**GUI**
Ghex
[HexWalk](https://github.com/gcarmix/HexWalk)
[010Editor](https://www.sweetscape.com/)
[ImHex](https://github.com/WerWolv/ImHex)

