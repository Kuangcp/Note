---
title: Git实践技巧
date: 2018-11-21 10:56:52
tags: 
categories: 
    - 版本控制
---

💠

- 1. [GitInAction](#gitinaction)
    - 1.1. [安装](#安装)
        - 1.1.1. [Linux(debian系)](#linuxdebian系)
        - 1.1.2. [Windows](#windows)
    - 1.2. [配置记住密码](#配置记住密码)
    - 1.3. [配置GPG签名](#配置gpg签名)
    - 1.4. [简单使用](#简单使用)
        - 1.4.1. [配置GPG](#配置gpg)
        - 1.4.2. [码云](#码云)
    - 1.5. [git初始化配置](#git初始化配置)
        - 1.5.1. [终端中显示当前分支](#终端中显示当前分支)
        - 1.5.2. [命令的自动补全](#命令的自动补全)
    - 1.6. [Git服务器](#git服务器)
        - 1.6.1. [使用 git daemon 搭建简易 Server](#使用-git-daemon-搭建简易-server)
        - 1.6.2. [HTTP 方式的 Git 服务器](#http-方式的-git-服务器)
            - 1.6.2.1. [配置HTTPS](#配置https)
            - 1.6.2.2. [使用SSH登录GitServer](#使用ssh登录gitserver)
    - 1.7. [Tips](#tips)
        - 1.7.1. [清理仓库大文件](#清理仓库大文件)
        - 1.7.2. [CRLF与LF](#crlf与lf)
        - 1.7.3. [仓库统计](#仓库统计)

💠 2024-01-23 19:08:38
****************************************
# GitInAction
> [try git](https://try.github.io/)

> [Github: lazygit](https://github.com/jesseduffield/lazygit)`命令行的简易图形化`
> [Github: Git History](https://githistory.xyz/)  

## 安装
### Linux(debian系)
- `sudo apt-get install git`

> 安装最新版本Git
- `sudo add-apt-repository ppa:git-core/ppa` 
    - 如果命令找不到就先安装这个 `sudo apt-get install software-properties-common`
- `sudo apt update`
- `sudo apt install git`

- 从源码安装 [Github:git](https://github.com/git/git)
    - make prefix=/usr/local all 
    - sudo makeprefix=/usr/local install 

- 安装文档(可选):
    - sudo apt-get installasciidoc
    - make prefix=/usr/local docinfo
    - sudo makeprefix=/usr/local install

- 卸载
    - sudo find /usr/local -depth -iname 'git*' -exec rm -rf {} \;

### Windows
- [git-for-windows 淘宝镜像源](https://npm.taobao.org/mirrors/git-for-windows/)

*******************

## 配置记住密码
-  `Windows下记住密码` ： 
    * 新建环境变量 HOME 值：`%USERPROFILE%`
    * 在C盘User下你的当前用户目录下新建` _netrc `文本文件： 
        * `machine https://github.com/Kuangcp/`
        * `login ***`
        * `password ***` 
    * 成功配置，测试便知

- `Linux下记住密码` 
    - 这种情况下一个域名只能使用一个账号
    - `git config --global credential.helper store`
    - 那么下一次输入账号和密码就会被持久化保存， 后续无需输入

- `ssh 方法：（推荐）`
    - `ssh-keygen` 不设置密码
    - `cat ~/.ssh/id_rsa.pub | xclip -sel clip`  添加即可

## 配置GPG签名
> [Github Doc](https://docs.github.com/en/github/authenticating-to-github/managing-commit-signature-verification)

- [Git error - gpg failed to sign data](https://stackoverflow.com/questions/41052538/git-error-gpg-failed-to-sign-data)
    - `git config --global user.signingkey 指纹`

因为Github等代码托管网站通常是使用 commit 信息里的邮箱来标记提交者的，但是这个信息是可以任意填的，这个时候就需要GPG签名来对该次提交签名，确认是本人提交

************************

## 简单使用

*Github下拉到eclipse*
- 1.在GitHub上新建一个项目，不勾选初始化，复制下URL
- 2.在eclipse新建项目然后在eclipse里添加git remote
- 3.commit -> push 完成
- 4.打开Git Bash 使用命令行再查看一下

*本地已有代码关联远程空仓库*
- 先在远程建立空仓库 一般各大平台也都有命令提示 
    - 传送门: [Gitee](https://gitee.com) | [Github](https://github.com/) | [Bitbucket](https://bitbucket.org/)  | [GitLab](https://gitlab.com/) ...
```sh
   	git remote add origin  https://github.com/Kuangcp/StudentManager.git
   	git push -u origin master 
```
- 说明下上面的命令 第一条是设置了一个远程仓库 仓库名为origin URL是后面那个,一般默认的远程仓库名都叫origin
    - 名字可以随便取 但是提交就要标明仓库名了,而且分支也是一样的默认是master可以自己加别的分支. `git push -u 随便 随意`

*建立本地空仓库并关联到远程仓库*
- 1.先在GitHub上创建一个仓库，不勾选README（不然添加远程仓库还得pull一下README文件才能push）
- 如果本地没有则 `mkdir 库名 `创建一个文件夹，最好和远程的库同名
- 2.在某本地项目根目录下运行 `Git Bash`
    - 2.1 `git init` 初始化（建立 `.git` 目录）
    - 2.2 `touch README.md`
    - 2.3 `git remote add origin master URL` 连上远程仓库
    - 2.4 `git push -u origin master` 输入用户名，密码 （若因为没有上游节点就按提示输入命令建立初始节点即可 git push --setupstream origin master）
    - 原因是没有指定本地dev分支与远程origin/dev分支的链接，根据提示，设置dev和origin/dev的链接：`git branch --set-upstream dev origin/dev` master同理

### 配置GPG
> [阮一峰:GPG入门教程](http://www.ruanyifeng.com/blog/2013/07/gpg.html)

- 能够提高安全性,但是麻烦,不过向来这两者就是不可兼得的.

### 码云
> [帮助文档](http://git.mydoc.io/) 

- [如何进行减少提交历史数量以及修改自己的commit中的邮箱](http://git.mydoc.io/?t=83152)
- [改写历史，永久删除git库的物理文件 ](https://my.oschina.net/jfinal/blog/215624?fromerr=ZTZ6c38X)
********************************
## git初始化配置
```sh
	git config --global user.name " "
	git config --global user.email " "
	git config --global color.ui  auto 
```
> 如果是多个账号使用同一台电脑就不要配置这个，单独配置每个仓库下的用户名，邮箱即可  
> `git config user.name ""`

********************
### 终端中显示当前分支
> 使用 .git-prompt.sh 在Bash下显示当前分支   Windows环境不用看,安装的Git-for-windows软件已经会显示分支名了

- `wget https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh -O ~/.git-prompt.sh` 下载脚本
- `chmod +x ~/.git-prompt.sh` 赋予可执行权限
> 在 .bash_alases文件中添加
```conf
    lightgreen='\[\033[1;32m\]'
    lightcyan='\[\033[1;36m\]'
    lightpurple='\[\033[1;35m\]'
    yellow='\[\033[1;33m\]'
    nocolor='\[\033[0m\]'
    source ~/.git-prompt.sh
    set_bash_prompt(){
        #PS1="[e[32m]u[e[m]@[e[33m]W[e[36m]$(__git_ps1 ' (%s)')[e[31m]$[e[m]"
        PS1="${lightcyan}\t${lightgreen}\w${lightpurple}$(__git_ps1 ' (%s)')${yellow} → \[\e[m\]"
    }
    PROMPT_COMMAND="set_bash_prompt; $PROMPT_COMMAND"
```

如果使用 zsh 加上 oh-my-zsh 这就是换个主题的事 下面的自动补全也是默认就有

********************
### 命令的自动补全
> [git自动补全脚本GitHub地址](https://github.com/git/git/tree/master/contrib/completion)

- 下载脚本 `wget https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -o ~/.git-completion.bash`
    -  在 .bashrc 或者 .bash_aliases 中添加 source ~/.git-completion.bash
    - 重启终端或者 `source .bashrc`即可
- 双击tab可以得到命令建议

***************************************************
## Git服务器
### 使用 git daemon 搭建简易 Server

*`目录结构`*
```
    root
    ├── a
    │   └── .git
    └── b
        └── .git
```
> 也就是说在仓库目录的父级目录 root 作为基础目录 (base-path)

- `git daemon --export-all --base-path=$(pwd) --port=8080` 在 当前目录 启动一个Git守护进程
    - `--enable=receive-pack` 为了安全，默认是仓库不能被修改， 添加这个参数就可以push了
    - `--export-all` 开放当前目录下所有项目
    - `--base-path=''` 指定开放的基本目录（指定开放别的路径）
    - `--port=8080` 指定开放的端口
    - `--verbose` 启动看到的日志信息更多

- 直接克隆 `git clone git://localhost:8080/a` 
- 或者作为已有代码的远程 `git remote add hub git://localhost:8080/a`
    - 然后 git fetch 对应的分支就可以达到将某个分支直接给对方的目的

### HTTP 方式的 Git 服务器
- 安装Apache： Web服务器
- 配置Apache服务器的开放的目录以及Git的路径 
```xml
    <Location /git>
        AuthType Basic 
        AuthName "GIT Repository" 
        AuthUserFile "/home/mythos/GitRemoteRepo/htpassed"
        Require valid-user
    </Location>
```
- 切换到Apache的bin目录下：`htpasswd -cmb /home/mythos/GitRemoteRepo/htpsswd 账号名 密码`
- 到仓库目录下 `git init --bare 程序项目名称`
- `git clone http://localhost/git/程序项目名称` 输入用户名密码即可

#### 配置HTTPS
- 切换到Apache主目录下执行
    1. `bin\openssl genrsa -des3 -out server.key 2048 -config conf\openssl.cnf` 输入密码
    1. `bin\openssl req -new -key server.key -out server.csr -config conf\openssl.cnf` 输入之前密码
    1. `bin\openssl x509 -req -days 3650 -in server.csr -signkey server.key -out server.crt` 输入之前密码

- 把server.key 更名为server.key.old :`bin\openssl rsa -in server.key.old -out server.key`
- 将server.key server.crt 移动到conf
- 修改 httpd.conf 去掉如下三行的注释 # 字符

```
    LoadModule socache_shmcb_module..
    LoadModule ssl_module..
    Include conf/extra...
```
- 因为是自己建立的SSL证书 所以要去掉SSL验证 `git -c http.sslVerify=false clone URL `
- 或者写入配置文件 `git config http.sslVerify false`

#### 使用SSH登录GitServer

******************

## Tips
1. 虽然在物理上本地仓库中所有文件是放在一起的，但是分支之间是互不能访问以及操作的
2. 在本地的每次commit都是有index的，上传到github可以不用那么频繁，反正都是有记录的
3. 出现了冲突，从而无法自动merge：
```
    git pull 对方的分支
    git checkout 自己的分支
    git merge --no-ff 对方的分支
    git push （自己的源+分支）origin master
```
4. 切记：避免隐私的配置文件上传github时，将配置分离出来配置.gitignore中忽略掉配置文件，然后建立模板文件夹放待配置的文件即可
    -  `大意的后果`：[程序员复仇记 | 这些年，GitHub 上泄露了些什么？](https://zhuanlan.zhihu.com/p/33424997)
    - [不小心把密码上传到 GitHub 了，怎么办](https://www.bennythink.com/git-password.html)
5. `cat ~/.ssh/id_rsa.pub | xclip -sel clip` 复制公钥
6. Linux下当大量文件出现mode的变化（因为你的目录移动，文件权限变化等影响的）可以设置忽略掉 `git config core.fileMode false`
    * 当将目录备份出去，然后重装系统粘贴回来，权限就变了，mode也变了，可以设置忽略掉改变
7. git status 中文文件名乱码, 执行 `git config --global core.quotepath false`即可

- `git ls-files` 列出文件列表
    - `git ls-files | xargs wc -l` 计算文件中程序代码行数 通过工具：`xargs` `wc` (中文命名的文件编码问题无法计算行数)
    - `git ls-files | xargs cat | wc -l` 计算行数总和

- [API: github开发接口](https://developer.github.com/v3/)
- [Github: Search 技巧](https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github)

### 清理仓库大文件
- [official:7.6 Git 工具 - 重写历史](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%87%8D%E5%86%99%E5%8E%86%E5%8F%B2)

> [Tool: bfg-cleaner](https://rtyley.github.io/bfg-repo-cleaner/)

> [参考博客 从git中永久删除文件以节省空间](http://blog.csdn.net/meteor1113/article/details/4407209) | 
> [参考博客4 减小磁盘占用](http://zhongmingmao.me/2017/04/19/git-reduce/)  
> [删除仓库的某个时间点之前的历史记录，减少.git 目录大小](https://www.v2ex.com/t/297802)  
> [如何清洗 Git Repo 代码仓库](http://www.open-open.com/lib/view/open1414632626075.html)  

> [参考: 寻找并删除Git记录中的大文件](https://www.tuicool.com/articles/vAVVZrA)
1. 找出大文件 `git rev-list --objects --all | grep "$(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -10 | awk '{print$1}')"`
1. 删除文件, 重写提交 `git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch 文件的路径' --prune-empty --tag-name-filter cat -- --all`
1. 强制推送 `git push origin --force --all`
    - `git push origin --force --tags`
1. 使用`git pull rebase`来更新分支，而不是 `git merge` 不然大文件又从别的分支回来了

> 要注意, 所有的分支都必须 pull rebase , 只要还有一个人留有对大文件的引用, 大文件就一直在仓库

### CRLF与LF
> 由于系统的不同 Windows是 CRLF *nix 是 LF Mac 是 CR | [wiki: CRLF](https://en.wikipedia.org/wiki/Newline)  

Git提供了一个“换行符自动转换”功能。这个功能默认处于“自动模式”，当你在签出文件时，它试图将 UNIX 换行符（LF）替换为 Windows 的换行符（CRLF）；  
当你在提交文件时，它又试图将 CRLF 替换为 LF。Git 的“换行符自动转换”功能听起来似乎很智能、很贴心，因为它试图一方面保持仓库内文件的一致性（UNIX 风格），一方面又保证本地文件的兼容性（Windows 风格）。但遗憾的是，这个功能是有 bug 的

```sh
    git config --global core.autocrlf false 
    git config --global core.safecrlf true
```

> [参考: CRLF和LF](https://www.tuicool.com/articles/IJjQVb)
> [参考: git 换行符LF与CRLF转换问题](https://www.cnblogs.com/sdgf/p/6237847.html)

>1. CRLF -> LF `sed -i 's/\r//g' file` 配合git 就是 `git ls-files| sed -i 's/\r//g' `

### 仓库统计
> [https://github.com/hoxu/gitstats](https://github.com/hoxu/gitstats)  
> gogitstats  