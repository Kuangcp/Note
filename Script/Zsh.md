---
title: Zsh
date: 2018-12-15 12:06:10
tags: 
    - Shell
categories: 
    - Linux
---

💠

- 1. [Zsh](#zsh)
    - 1.1. [为什么要使用](#为什么要使用)
    - 1.2. [Tips](#tips)
- 2. [基础结构](#基础结构)
- 3. [oh-my-zsh](#oh-my-zsh)
    - 3.1. [插件](#插件)
    - 3.2. [主题](#主题)
        - 3.2.1. [自己定制](#自己定制)

💠 2024-09-14 11:51:16
****************************************
# Zsh
> [arch zsh wiki](https://wiki.archlinux.org/index.php/Zsh)

## 为什么要使用
> [mac 装了 oh my zsh 后比用 bash 具体好在哪儿？](https://www.zhihu.com/question/29977255)  
> [终极 Shell——ZSH](https://zhuanlan.zhihu.com/mactalk/19556676)

> [某人的配置](https://github.com/lilydjwg/dotzsh)

- [Zsh 开发指南](https://www.zhihu.com/column/zshguide)

- 提供较为强大的历史命令match功能
- 较为丰富的扩展实现
- 更现代化的支持 更多语言，unicode字符

## Tips 

- 数组使用 `list=(a b c); for i in $list; do echo $i; done`

# 基础结构
************************

# oh-my-zsh
> [Github](https://github.com/robbyrussell/oh-my-zsh)  
> [关于PS1环境变量的折腾](https://gitee.com/kcp1104/codes/gca14wtqvm67l9j5r0deb56#Zsh.md) `因为含特殊字符GitBook构建通不过,只能放出去了`

1. 安装好 zsh wget git
2. `sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"`
3. `vi ~/.zshrc` 进行配置

```
    plugins=(
        git mvn docker
    )
```

## 插件
> [wiki: plugins](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins)  
> [zsh oh-my-zsh 插件推荐 ](https://hufangyun.com/2017/zsh-plugin/)

- 个人常用 git gitfast mvn gradle golang docker kubectl sudo colored-man-pages 

**********************

## 主题
> [官网主题列表](https://github.com/robbyrussell/oh-my-zsh/wiki/Themes) 

- 自带主题: amuse clean wedisagree, muse也还好,就是没时间

> [额外主题列表](https://github.com/robbyrussell/oh-my-zsh/wiki/External-themes)

- `推荐` powerlevel10k **性能强劲，交互式配置**
    - [Github](https://github.com/romkatv/powerlevel10k)
    - install nerd-fonts-meslo-lg 

- powerlevel9k
    - [Github Doc](https://github.com/bhilburn/powerlevel9k/wiki/Install-Instructions#option-2-install-for-oh-my-zsh)
    - `git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k`
    - `powerlevel9k/powerlevel9k`

- Bullet Train `桌面在用 bullet-train` 
    - [Github repo](https://github.com/caiogondim/bullet-train.zsh) |  [必需的符号字体](https://github.com/powerline/powerline)
    - Source Code Pro for Powerline + Powerline + Awesonme 的 Bold 字体搭配最合适

```sh
    wget https://raw.githubusercontent.com/caiogondim/bullet-train.zsh/master/bullet-train.zsh-theme -O /home/kcp/.oh-my-zsh/custom/themes

    wget https://github.com/powerline/powerline/raw/develop/font/PowerlineSymbols.otf
    wget https://github.com/powerline/powerline/raw/develop/font/10-powerline-symbols.conf
    mv PowerlineSymbols.otf ~/.local/share/fonts/
    fc-cache -vf ~/.local/share/fonts/
    mv 10-powerline-symbols.conf ~/.config/fontconfig/conf.d/
```

- Maglev `Tmux 主题 和上面的Zsh主题搭配使用`
    - [Github地址](https://github.com/caiogondim/maglev)

- spaceship
    - [地址](https://www.ctolib.com/denysdovhan-spaceship-zsh-theme.html)

> [安装步骤](https://github.com/caiogondim/bullet-train.zsh#for-oh-my-zsh-users)
1. mkdir $ZSH_CUSTOM/themes/
2. wget http://raw.github.com/caiogondim/bullet-train-oh-my-zsh-theme/master/bullet-train.zsh-theme
3. config .zshrc to `ZSH_THEME="bullet-train" `

### 自己定制
> [Github doc](https://github.com/robbyrussell/oh-my-zsh/wiki/Customization)

`基于muse的主题` 用在服务器上挺好
> ~/.oh-my-zsh/custom/themes/muse-myth.zsh-theme [源码](https://github.com/Kuangcp/Script/blob/master/zsh/themes/muse-mythos.zsh-theme) 

