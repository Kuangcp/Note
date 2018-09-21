`目录 start`
 
- [文本编辑器](#文本编辑器)
    - [Ghex](#ghex)
    - [Kate/KWrite(Kate的轻量版)](#katekwritekate的轻量版)
    - [Geany](#geany)
    - [scite](#scite)
    - [textadept](#textadept)
        - [快捷键](#快捷键)
    - [Sublime](#sublime)
        - [快捷键](#快捷键)
        - [crack](#crack)
    - [VSCode](#vscode)
        - [快捷键](#快捷键)
        - [代码片段](#代码片段)
        - [插件](#插件)
        - [实践](#实践)
    - [Atom](#atom)
    - [Gedit](#gedit)
    - [小书匠](#小书匠)
    - [Moeditor|Typora|CuteMarkEd](#moeditor|typora|cutemarked)
    - [Cmd](#cmd)
- [终端中的文本编辑器](#终端中的文本编辑器)
    - [Vi/Vim](#vivim)
    - [Nano](#nano)
    - [fte-terminal](#fte-terminal)
    - [在线编辑器](#在线编辑器)

`目录 end` |_2018-09-01_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 文本编辑器
## Ghex
- 十六进制文件编辑器

************************************
## Kate/KWrite(Kate的轻量版)
- [安装markdown预览插件](https://github.com/antonizoon/kate-markdown)
- 码Python也挺方便，也有常用快捷键，自动提示，终端整合，而且是自动切目录

*********************************
## Geany
- 码C 编译方便 有Ctag辅助

*********************************
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

- 如果出现小bug，就直接删除 ～.config 下的 sublime文件夹注意注册证书拷出来
- 中文不兼容解决方法： 3143版本号下：
    - 搜索安装插件 ChineseLocalizations 就能汉化 
    - 修改配置文件 添加`"font_face": "DeJaVu Sans Mono",` 就解决了字体错位的问题
    - 保存为项目来切换管理更为方便
- 主题安装 Boxy Theme 以及  A File Icon 就能切换多种主题了 [参考博客](https://www.zhihu.com/question/46266742)
- [配置C/C++开发环境](http://www.cnblogs.com/flipped/p/5836002.html)

**关闭自动检查升级**
- setting 中 "update_check":false
### 快捷键
> [参考博客: Sublime Text 3 快捷键](http://www.cnblogs.com/roadone/p/7745641.html)
> [sublime的常用快捷键](http://www.cnblogs.com/kristen-zou/p/7641158.html)

### crack
> [3143码](https://gitee.com/kcp1104/codes/89xfugn5dwoyr23vchikb54#sublime-3143-Key)

- [参考博客](http://www.cnblogs.com/hollow/p/6496469.html)
- [3143 1](https://fatesinger.com/100121) | [3143 2](https://fatesinger.com/100227) | [3176](https://fatesinger.com/100237) 

************************************

## VSCode

> [官网](https://code.visualstudio.com/) 码笔记，码Python 比较方便，目录树，预览，整合终端  | [中文手册](https://jeasonstudio.gitbooks.io/vscode-cn-doc/)

1. 其所有用户自定义配置都缓存在此目录 `~/.config/Code/User/`
1. vscode 书写 markdown [官方文档](https://code.visualstudio.com/Docs/languages/markdown)


### 快捷键
> [快捷键官方PDF说明](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)

- `Ctrl P` 快速命令
    - 直接输入文件名就是搜文件
    - `>` 作为前缀则等同 `Ctrl Shift P`
    - `#` 作为前缀则等同 `Ctrl T`
- `Ctrl T ` 搜索打开所有Markdown文件的所有标题 1.25+
- `Ctrl Shift P ` 执行命令
- `Ctrl+K Ctrl+S` 设置用户快捷键  Keyboard Shortcuts
- `Ctrl Shift C `在当前打开的文件夹下打开系统默认终端
- `Ctrl Space` 智能提示 变量,代码片段... **需要注意这个快捷键和Windows以及Linux上切换输入法快捷键有冲突,修改即可**
- `Alt Shift` 列编辑
- `C S .` 显示面包屑 版本:1.26+

> [参考博客: 快捷键大全](https://blog.csdn.net/crper/article/details/54099319)
> [参考博客: VS Code 使用小技巧](https://zhuanlan.zhihu.com/p/22880087)

### 代码片段
> 配置地点 文件-首选项-用户代码片段 可以新建一个代码片段  
> 默认是放在用户的配置目录下 `~/.config/Code/User/snippets/`

- [参考博客: VS Code 折腾记 - (6) 基本配置/快捷键定义/代码片段的录入（snippet）](https://juejin.im/post/58aeeca22f301e006cf65c8b)
- [巧用VScode“用户代码片段”来提高效率](https://www.dogxu.cn/2017/06/10/vscode-snippet/)
    - 然后自定义一下insert snippet的快捷键,就很方便使用了 个人配置为`Ctrl L`, **其实 直接 Ctrl Space 直接提示就行了**
    - 注意,每次修改片段配置文件,都需要重启Vscode才会生效最新修改...emm

### 插件
**美化**
1. vscode-icons
1. Material Icon Theme
1. One Dark Pro
1. snazzy operator

**工具**
1. Beautify
1. Auto Rename Tag
1. Todo Tree 
1. GitLens `方便查看更改`

### 实践
> [参考博客: 用Git在Visual Studio Code内进行版本控制[指导]](https://sdk.cn/news/4041)
> [参考博客: 使用vscocd进行python开发 ](http://www.cnblogs.com/bloglkl/archive/2016/08/23/5797805.html)

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

******************************

## 小书匠
- [在线使用](http://markdown.xiaoshujiang.com/) | [github地址](https://github.com/suziwen/markdownxiaoshujiang)
- 本来是很合适的，但是对文件操作不干净，总有些bug不好用,文件闪退出错,终端不方便
    - 不适合编程适合写作,所支持的md的格式非常强大
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

## Moeditor|Typora|CuteMarkEd 
> [Moeditor](https://github.com/Moeditor/Moeditor)

- 书写单个md文件方便，美观，没有目录树侧栏是硬伤, 但是typora 导出很强大

*****************************

## Cmd
> [官网](https://www.zybuluo.com/cmd/)

**************************

# 终端中的文本编辑器
## Vi/Vim
> [Github地址](https://github.com/vim/vim)  
> [Vim 学习笔记](/Linux/vim.md)

************
## Nano
- 模式没有vi系列复杂，使用简单，安装占用小

************
## fte-terminal
- 文件树浏览，快速打开文件进行修改是比较方便的

*****************
## 在线编辑器
_[stackedit.io](https://stackedit.io/)_
- [Github地址](https://github.com/benweet/stackedit/)

CMD编辑器