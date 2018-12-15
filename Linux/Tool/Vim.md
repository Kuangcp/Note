---
title: Vim
date: 2018-12-15 12:05:58
tags: 
    - Vim
categories: 
    - 工具
---

**目录 start**
 
1. [Vim](#vim)
    1. [Tips](#tips)
    1. [基本配置](#基本配置)
    1. [基础操作](#基础操作)
        1. [跳转](#跳转)
        1. [搜索匹配](#搜索匹配)
        1. [复制粘贴](#复制粘贴)
        1. [插入模式](#插入模式)
        1. [命令模式](#命令模式)
    1. [vim-init](#vim-init)
    1. [spf13](#spf13)
    1. [SpaceVim](#spacevim)
    1. [space-vim](#space-vim)

**目录 end**|_2018-12-13 12:06_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Vim 
> 学习曲线很高，但是学会熟练使用后就效率很高

- [vim galore](https://github.com/mhinz/vim-galore)
- [Vim galore 中文翻译](https://github.com/wsdjeg/vim-galore-zh_cn)

> [bytefluent.com/vivify](http://bytefluent.com/vivify/)方便的自制主题

## Tips
1. 误按 `Ctrl S` 终止屏幕输出（即停止回显）你敲的依然有效，只是看不见 `Ctrl Q` 即可恢复

1. /usr/share/vim/vim80/macros/less.sh vim版less 具备语法高亮 路径中间是依据vim版本来的,按实际情况改动
**************
`vim输出的信息`
```
    系统 vimrc 文件: "$VIM/vimrc"
    用户 vimrc 文件: "$HOME/.vimrc"
    第二用户 vimrc 文件: "~/.vim/vimrc"
    用户 exrc 文件: "$HOME/.exrc"
    defaults file: "$VIMRUNTIME/defaults.vim"
    $VIM 预设值: "/usr/share/vim"
```
## 基本配置
- 在文件 全局：`/etc/vim/vimrc` 先备份一下 `sudo cp /etc/vim/vimrc /etc/vim/vimrc.bak`
	- 或者当前用户：`~/.vimrc` 中添加如下内容
```
set showcmd		" Show (partial) command in status line.
set autowrite		" Automatically save before commands like :next and :make
set nocompatible
set number
filetype on 
syntax on
set history=1000
set autoindent
set smartindent
set tabstop=4
set expandtab
set shiftwidth=4
set showmatch
set guioptions=T
set ruler
set hls
set backspace=2
imap jk <Esc> 

set relativenumber " 设置相对行号
" 逗号后追加空格
inoremap , ,<space>  
```
**~/.gvimrc**
```
:set guifont=IBM\ Plex\ Mono\ 12
colorscheme desert
syntax enable
syntax on
```
## 基础操作
> [参考博客](http://www.jianshu.com/p/bcbe916f97e1)  
> [高效率编辑器 Vim——操作篇，非常适合 Vim 新手](https://linuxtoy.org/archives/efficient-editing-with-vim.html)

- v 可视化操作
> [参考博客: vim中执行shell命令小结](https://blog.csdn.net/topgun_chenlingyun/article/details/8013115)
### 跳转
- K J H L 上下左右
- Ctrl+F  上翻一页
- Ctrl+B  下翻一页
- H M L   跳转到屏幕 顶 中 尾
	- 2H  第二行 3L 倒数第三行

- `*` 当光标在某单词上 会进行搜索跳转到下一个
- `#` 与`*` 一样，不过是跳转到上一个
- `/)`和`/(` 跳转到 后和前 语句的位置 为了() 跳转方便
- `/}`和`/{` 跳转到 后和前 段落的位置  
- `g_` 跳转到最后一个不是空格的字符的位置
- `gg` 跳转到文件第一行的起始位置
- `G` 跳转到文件最后一行起始位置

- `5gg`或`5G` `:5` 跳转到 5 行的起始位置
- `number` 正数则是往下，负数则是往上 (相对)

`行内移动`
- `w` 右移到下一个字的开头
- `e` 右移到下一个字的末尾
- `b` 左移到前一个字的开头
- `0` 左移光标到本行的开始
- `$` 右移光标到行末尾
- `^` 移动到本行第一个非空字符

`fg` 在光标所在处(如果是有效的目录或者文件,就能直接跳转过去)

### 搜索匹配
- `/name`  正向搜索字符串 name
	- `n` 搜索后跳下一个 
	- `N` 搜索后跳上一个
- `?name` 反向搜索字符串

### 复制粘贴
> `:reg` 查看寄存器

- `yy` 复制当前行 `nyy` 是复制该行开始的共n行(是vim内的剪贴板)
    - `yn` 加换行 等效
- `"+nyy` 同理复制n行，操作系统级的剪贴板
    - `"+yn` 等效

*********

- `P`/`p`  将剪贴板的内容粘贴在 前/后
    - `"+p` 将系统的剪贴板内容粘贴进来
- `u` 撤销上一条命令的效果
- `.` 重复最后一条修改正文的命令

### 插入模式
- i  在光标左侧插入
- a  在光标右侧插入
- o  在光标该行下一行新增一行
- O  在光标该行上一行新增一行
- I  在光标该行开头插入
- A  在光标该行末尾插入

### 命令模式
- `:e path` 打开指定路径下文件
- `:w` 保存当前编辑的文件 后接文件名就是另存为
- `ZZ` 退出Vim 并将所做修改覆盖原始文件
- `:q` 未修改的情况下退出
- `:q!` 放弃所有修改，退出
- `wq` `x` 先保存后退出

## vim-init
> [Github:](https://github.com/skywind3000/vim-init)

## spf13
- [official site](http://vim.spf13.com/)

## SpaceVim
> [参考博客: SpaceVim 中文手册](https://ruby-china.org/topics/32020)`主要看评论, 两个作者理念不同`
> [参考博客: 如何评价Vim配置文件SpaceVim?](https://www.zhihu.com/question/54270182)

- [Space Vim](https://github.com/topics/spacevim)`把Vim玩上天了`
    - [GitBook : Space Vim Guide](https://legacy.gitbook.com/book/everettjf/spacevimtutorial/details)
    - [quick start](https://spacevim.org/quick-start-guide/)
    - [中文 文档](https://spacevim.org/cn/documentation/)

## space-vim 
> [Github:](https://github.com/liuchengxu/space-vim)
