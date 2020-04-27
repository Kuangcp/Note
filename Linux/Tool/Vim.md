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
        1. [GVim](#gvim)
    1. [基础操作](#基础操作)
        1. [跳转](#跳转)
            1. [高级跳转](#高级跳转)
        1. [搜索和替换](#搜索和替换)
        1. [复制粘贴](#复制粘贴)
        1. [插入模式](#插入模式)
        1. [命令模式](#命令模式)
    1. [插件管理](#插件管理)
1. [定制化](#定制化)
    1. [vim-init](#vim-init)
    1. [spf13](#spf13)
    1. [SpaceVim](#spacevim)
    1. [space-vim](#space-vim)

**目录 end**|_2020-04-27 23:42_|
****************************************
# Vim 
> 学习曲线很高，但是学会熟练使用后就效率很高 `官方教程程序 vimtutor`

- [vim galore](https://github.com/mhinz/vim-galore)
- [Vim galore 中文翻译](https://github.com/wsdjeg/vim-galore-zh_cn)

> [bytefluent.com/vivify](http://bytefluent.com/vivify/) `方便的自制主题`

> [vim教程网](https://vimjc.com/)

## Tips
1. 误按 `Ctrl S` 终止屏幕输出（即停止回显）你敲的依然有效，只是看不见 `Ctrl Q` 即可恢复

1. `/usr/share/vim/vim80/macros/less.sh` vim 版 less 
    - 具备语法高亮 路径中间是依据vim版本来的, 按实际情况改动

1. 设置默认编辑器 `export EDITOR=/usr/bin/vim`

1. vim 会导致文件 inode 变更 [why inode value changes when we edit in “vi” editor?](https://unix.stackexchange.com/questions/36467/why-inode-value-changes-when-we-edit-in-vi-editor)

************************

`配置文件优先级`
- 系统 vimrc 文件: `$VIM/vimrc`
- 用户 vimrc 文件: `$HOME/.vimrc`
- 第二用户 vimrc 文件: `~/.vim/vimrc`
- 用户 exrc 文件: `$HOME/.exrc`
- defaults file: `$VIMRUNTIME/defaults.vim`
- $VIM 预设值: `/usr/share/vim`

## 基本配置
1. 全局修改 ：`/etc/vim/vimrc`
1. 或者配置放在 `/etc/vim/vimrc.local`
    - 然后在 `/etc/vim/vimrc` 中添加:
    ```sh
    if filereadable("/etc/vim/vimrc.local")
        source /etc/vim/vimrc.local
    endif
    ```
1. 或者当前用户：`~/.vimrc` [个人vim配置](https://github.com/Kuangcp/Configs/blob/master/Linux/vimrc.local)

************************

### GVim
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

> [参考: vim中执行shell命令小结](https://blog.csdn.net/topgun_chenlingyun/article/details/8013115)

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

#### 高级跳转
- fg 如果光标所在处是一个完整的路径,就跳转到该文件 
    - `Ctrl Shift 6` 或者 `:e#` 跳回来 | [参考 stackoverflow](https://stackoverflow.com/questions/133626/how-do-you-return-from-gf-in-vim) 

### 搜索和替换
- `/name`  正向搜索字符串 name
	- `n` 搜索后跳下一个 
	- `N` 搜索后跳上一个
- `?name` 反向搜索字符串

> 替换  `:[range]s/pattern/string/[c,e,g,i]`

| 参数 | 含义 |
|:----|:----|
| range    | 指的是范围 1,5 指的是1-5行; `1,$`或是`1,%` 则是第一行到最后一行; `.,5`当期行到第5行
| pattern  | 就是要被替换掉的字串，可以用 regexp 來表示。
| string   | 匹配到 pattern 的字符串替换为 string
| c        | confirm，每次替换前先询问
| e        | 不显示error
| g        | global 全局
| i        | ignore 不分大小写。

> % 是目前編輯的文章，# 是前一次編輯的文章, . 表示当前行

### 复制粘贴
> `:reg` 查看寄存器

- `yy` 复制当前行 `nyy` 是复制该行开始的共n行(是vim内的剪贴板)
    - `yn` 加换行 等效
- `"+nyy` 同理复制n行，操作系统级的剪贴板
    - `"+yn` 等效

1. vim 中粘贴内容时被自动缩进, 导致大量空格
    1. 先执行 `:set paste` 命令,然后粘贴
    1. 关闭 paste 模式 `:set nopaste`

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

> 先 q 再 : 就会显示最近的命令


************************

## 插件管理
> [vim-plug](https://github.com/junegunn/vim-plug)  

> [参考: VIM插件推荐](https://zhuanlan.zhihu.com/p/58816186)  

> 语言插件
- vim-python   
- vim-go 

************************

# 定制化
## vim-init
> [Github:](https://github.com/skywind3000/vim-init)

## spf13
- [official site](http://vim.spf13.com/)

## SpaceVim
> [参考: SpaceVim 中文手册](https://ruby-china.org/topics/32020)`主要看评论, 两个作者理念不同`
> [参考: 如何评价Vim配置文件SpaceVim?](https://www.zhihu.com/question/54270182)

- [Space Vim](https://github.com/topics/spacevim)
    - [GitBook : Space Vim Guide](https://legacy.gitbook.com/book/everettjf/spacevimtutorial/details)
    - [quick start](https://spacevim.org/quick-start-guide/)
    - [中文 文档](https://spacevim.org/cn/documentation/)

## space-vim 
> [Github:](https://github.com/liuchengxu/space-vim)
