`目录 start`
 
- [Zsh](#zsh)
    - [为什么要使用](#为什么要使用)
    - [安装](#安装)
    - [配置](#配置)
        - [oh-my-zsh](#oh-my-zsh)
            - [插件](#插件)
            - [主题](#主题)
                - [自己定制](#自己定制)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Zsh
> [arch zsh wiki](https://wiki.archlinux.org/index.php/Zsh)

## 为什么要使用
> 知乎:[mac 装了 oh my zsh 后比用 bash 具体好在哪儿？](https://www.zhihu.com/question/29977255)
> [终极 Shell——ZSH](https://zhuanlan.zhihu.com/mactalk/19556676)

## 安装
> debian系 `apt install zsh`  

## 配置
> [某人的配置](https://github.com/lilydjwg/dotzsh)


### oh-my-zsh
> [Github](https://github.com/robbyrussell/oh-my-zsh) | [参考博客进行安装](https://segmentfault.com/a/1190000004695131)

> [关于PS1环境变量的折腾](https://gitee.com/kcp1104/codes/gca14wtqvm67l9j5r0deb56#Zsh.md) `因为含特殊字符GitBook构建通不过,只能放出去了`

1. 安装好 zsh wget git
2. `sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"`
3. `vi ~/.zshrc` 进行配置

```
    plugins=(
        git mvn gradle autojump
    )
```
#### 插件
> [wiki: plugins](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins)  
> [zsh oh-my-zsh 插件推荐 ](https://hufangyun.com/2017/zsh-plugin/)

#### 主题
> [官网主题列表](https://github.com/robbyrussell/oh-my-zsh/wiki/Themes) 
- 自带主题:
    - 个人偏好 amuse clean wedisagree, muse也还好,就是没时间

_额外安装_
> [额外主题列表](https://github.com/robbyrussell/oh-my-zsh/wiki/External-themes)

- powerlevel9k
    - [官方文档](https://github.com/bhilburn/powerlevel9k/wiki/Install-Instructions#option-2-install-for-oh-my-zsh)
    - `git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k`
    - `powerlevel9k/powerlevel9k`

- Bullet Train (桌面在用) | [Github repo](https://github.com/caiogondim/bullet-train.zsh)
    - Source Code Pro for Powerline + Powerline + Awesonme 的 Bold 字体搭配最合适

- spaceship
    - [地址](https://www.ctolib.com/denysdovhan-spaceship-zsh-theme.html)

> [安装步骤](https://github.com/caiogondim/bullet-train.zsh#for-oh-my-zsh-users)
1. mkdir $ZSH_CUSTOM/themes/
2. wget http://raw.github.com/caiogondim/bullet-train-oh-my-zsh-theme/master/bullet-train.zsh-theme
3. config .zshrc to `ZSH_THEME="bullet-train" `

- Maglev
    - [Github地址](https://github.com/caiogondim/maglev)

##### 自己定制
> [Github doc](https://github.com/robbyrussell/oh-my-zsh/wiki/Customization)

