---
title: Git实践
date: 2018-11-21 10:56:52
tags: 
categories: 
    - Git
---

**目录 start**
 
1. [GitInAction](#gitinaction)
    1. [Tips](#tips)
    1. [配置记住密码](#配置记住密码)
    1. [【安装】](#安装)
        1. [Linux(debian系)](#linuxdebian系)
        1. [windows](#windows)
        1. [GUI](#gui)
    1. [【简单使用】](#简单使用)
        1. [配置GPG](#配置gpg)
        1. [实验楼上使用Github](#实验楼上使用github)
        1. [码云](#码云)
    1. [【git初始化配置】](#git初始化配置)
        1. [【VI编辑器的使用】](#vi编辑器的使用)
    1. [【配置SSH连接上Github】](#配置ssh连接上github)
        1. [Github上fork别人项目的操作](#github上fork别人项目的操作)
        1. [Github上PR](#github上pr)
        1. [.gitingnore文件](#gitingnore文件)
        1. [终端中显示当前分支](#终端中显示当前分支)
        1. [命令的自动补全](#命令的自动补全)
    1. [搭建Git服务器](#搭建git服务器)
        1. [使用git daemon搭建简易 Server](#使用git-daemon搭建简易-server)
        1. [【HTTP访问Git服务器】](#http访问git服务器)
            1. [【配置HTTPS】](#配置https)
            1. [【使用SSH登录GitServer】](#使用ssh登录gitserver)
    1. [基础命令概述](#基础命令概述)

**目录 end**|_2018-12-29 21:14_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# GitInAction
> [try git](https://try.github.io/)

> [Github: lazygit](https://github.com/jesseduffield/lazygit)`命令行的简易图形化`

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
7. git的输出中文乱码 执行 `git config --global core.quotepath false`即可

## 配置记住密码
-  `Windows下记住密码` ： 
    * 新建环境变量 HOME 值：`%USERPROFILE%`
    * 在C盘User下你的当前用户目录下新建` _netrc `文本文件： 
        * `machine https://github.com/Kuangcp/`
        * `login ***`
        * `password ***` 
    * 成功配置，测试便知

- `Linux下记住密码`：(如果使用了多个github账号，设置这个后只能使用一个账号的自动登录，另一个账号将完全连不上github，ssh也只能一个账号配一个，不能多个账号用一个ssh)
    * `touch .git-credentials`
    * `vim .git-credentials`
    * 输入： ` http://{username}:{password}@github.com` 或者是https开头
    * `git config --global credential.helper store`
    * `~/.gitconfig` 文件中多了以下内容即可
        * [credential]
        * helper = store

- `ssh 方法：（推荐）`
    - `ssh-keygen` 不设置密码
    - `cat ~/.ssh/id_rsa.pub | xclip -sel clip`  添加即可

*********
- 关于许可证 [Github许可证网](https://choosealicense.com/licenses/)
    - 新建项目的时候可以选择 添加.gitignore和许可证类别 许可证大致分为 MIT Apache2.0 GPL 
    - `MIT` 简单宽松的许可证，任何人可以拿代码做任何事与我无关` eg: jQuery、Rails` 
    - `Apache` 关注于专利，这类似于MIT许可证，但它同时还包含了贡献者向用户提供专利授权相关的条款。 `Apache、SVN和NuGet`
    - `GPL` 关注于共享改进，这是一种copyleft许可证，要求修改项目代码的用户再次分发源码或二进制代码时，必须公布他的相关修改。 `Linux、Git`

**********
## 【安装】 
### Linux(debian系)
- `sudo apt-get install git`

`安装最新版本Git`
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
    - sudo find /usr/local -depth -iname 'git*' -exec rm -fr {} \;

### windows
- 直接搜索git-for-windows 建议使用360搜索,会有360的下载链接,无意间发现 毕竟官网的下载速度不敢恭维

### GUI
> [官方列表](https://git-scm.com/downloads/guis)

**************
## 【简单使用】 

*Github下拉到eclipse*
- 1.在GitHub上新建一个项目，不勾选初始化，复制下URL
- 2.在eclipse新建项目然后在eclipse里添加git remote
- 3.commit -》push 完成
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

*********************
### 实验楼上使用Github
> 方便学习使用 

- `git clone URL` 复制下来，默认是master
- `git branch 新分支名` 新建一个分支，切换过去，使用的就是这个新分支放代码
- `git push origin 新分支名` add commit 之后就push
- `git fetch origin 已有分支` 下拉别的分支代码

### 码云
> [帮助文档](http://git.mydoc.io/) 

- [如何进行减少提交历史数量以及修改自己的commit中的邮箱](http://git.mydoc.io/?t=83152)
- [改写历史，永久删除git库的物理文件 ](https://my.oschina.net/jfinal/blog/215624?fromerr=ZTZ6c38X)
********************************
## 【git初始化配置】 
```sh
	git config --global user.name " "
	git config --global user.email " "
	git config --global color.ui  auto 
```
> 如果是多个账号使用同一台电脑就不要配置这个，单独配置每个仓库下的用户名，邮箱即可<br/>
> `git config user.name ""`

### 【VI编辑器的使用】
> [详情](/Linux/Tool/Vim.md)

- 在pull或者合并分支的时候有时会遇到打开 VI编辑器 的状态  可以不输入(直接下面3,4步)
`如果要输入解释的话就需要:`
```
    1.按键盘字母 i 进入insert模式
    2.修改最上面那行黄色合并信息,可以不修改
    3.按键盘左上角"Esc"
    4.输入`:wq`,按回车键即可 或者 :x
```

## 【配置SSH连接上Github】 
> 其他平台类似

- 【Markdown语法】: 
    - @用户名， @组织名 ；#编号 会连接到该仓库对应的Issue编号 。
    - 通过 用户名/仓库名 #编号 来指定仓库的指定Issue
- 【将Bash和GitHub绑定起来】：
    - 1.在GItHub上设置SSH key， 有一个即可
    - 2.$ssh-keygen -t rsa -C "xxx@outlook.com" 生成一个具有指定邮箱的rsa密钥对,然后复制到平台上
    - 3.设置密钥对密码. 当然为了偷懒就不设置,不然每次提交都要输入....
    - 4.测试SSH连接  $ssh -T git@github.com 输入 密钥对 密码
        - 询问将github的ip加入已知列表中 选择yes

### Github上fork别人项目的操作

**合并对方最新代码**
> 1. 首先fork一个项目, 然后clone自己所属的该项目下来,假设 原作者为A 自己为B  
> 1. 添加原作者项目的URL 到该项目的远程分支列表中 `git add remote A A_URL`  
> 1. fetch作者的代码到本地 `git fetch A`  
> 1. 新建本地分支, 并与A的远程分支绑定 `git branch A A/master` 
> 1. 合并两个分支代码 `git merge --no-ff A/master`  
> 1. push即可  

### Github上PR
> [Using git to prepare your PR to have a clean history](https://github.com/mockito/mockito/wiki/Using-git-to-prepare-your-PR-to-have-a-clean-history)

********************
### .gitingnore文件
> [Github: gitignore](https://github.com/github/gitignore) | 一行是一个配置, 是独占一行的

- 使用 `#` 注释一行
- `test.txt`  忽略该文件
- `*.html`  忽略所有HTML后缀文件
- `*[o/a]`  忽略所有o和a后缀的文件
- `!foo.html`  不忽略该文件

`示例文件`
```conf
    # maven #
    target/
    # IDEA #
    .idea/
    *.iml
    out/
    # eclipse #
    bin/
    .settings/
    .metadata/
    .classpath
    .project
```
********************
### 终端中显示当前分支
> 使用 .git-prompt.sh 在Bash下显示当前分支   Windows环境不用看,安装的Git-for-windows软件已经会显示分支名了

- `wget https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh -O ~/.git-prompt.sh` 下载脚本
- `chmod +x ~/.git-prompt.sh` 赋予可执行权限
- 在 .bash_alases文件中添加
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
********************
### 命令的自动补全
> [git自动补全脚本GitHub地址](https://github.com/git/git/tree/master/contrib/completion)

- 下载脚本 `wget https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -o ~/.git-completion.bash`
    -  在 .bashrc 或者 .bash_aliases 中添加 source ~/.git-completion.bash
    - 重启终端或者 `source .bashrc`即可
- 双击tab可以得到命令建议

***************************************************
## 搭建Git服务器
### 使用git daemon搭建简易 Server

*`目录结构`*
```
    ├── a
    │   └── .git
    └── b
        └── .git
```
> 也就是说在仓库目录的父级目录 作为基础目录 (base-path)

- `git daemon --export-all --base-path='BASE_PATH' --port=8080` 在 BASE_PATH 启动一个Git守护进程
    - `--export-all` 开放当前目录下所有项目
    - `--enable=receive-pack` 为了安全，默认是仓库不能被修改，添加这个参数就可以push了
    - `--base-path=''` 指定开放的基本目录（指定开放别的路径）
    - `--port=8080` 指定开放的端口
    - `--verbose` 启动看到的日志信息更多

- 克隆: `git clone git://localhost:8080/a` 

### 【HTTP访问Git服务器】
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

#### 【配置HTTPS】
- 切换到Apache主目录下 `bin\openssl genrsa -des3 -out server.key 2048 -config conf\openssl.cnf` 输入密码
- `bin\openssl req -new -key server.key -out server.csr -config conf\openssl.cnf` 输入之前密码
- `bin\openssl x509 -req -days 3650 -in server.csr -signkey server.key -out server.crt` 输入之前密码
- 把server.key 更名为server.key.old :`bin\openssl rsa -in server.key.old -out server.key`
- 将server.key server.crt 移动到conf
- 修改 httpd.conf 去掉如下三行的注释 # 字符
```
    LoadModule socache_shmcb_module..
    LoadModule ssl_module..
    Include conf/extra...
```
- 因为是自己建立的SSL证书 所以要去掉SSL验证 `git -c http.sslVerify=false clone URL `
- 或者直接改配置文件，省的每次输这么多 `git config http.sslVerify false`

#### 【使用SSH登录GitServer】
- [ ] 实践一下

*********************
## 基础命令概述
- `git touch file1 file2 ` 新建三个文件
- `echo "  ">>file1 ` 修改文件file1
- `git rm 文件名 ` ： 删除文件至缓存区
- `git commit -am " " `从缓存提交（切记要先 commit 才能 push）
- `git diff`  ： 查看当前工作树和暂存区的差别
- `git diff --cached `：查看缓存中文件修改的痕迹和对比 输入q 退出
- `git log --graph `：查看（图形化）提交日志 输入q退出
- `git banrch `分支名 ：创建新的分支
- `git branch -a`查看当前分支信息
- `git checkout -b`：创建一个分支，并立即切换
- `git checkout -b feature-D origin/feature-D` 新建一个分支来接收同步后面那个远程仓库的分支
- `git pull `：获取最新的远程仓库分支
- `git pull origin feature-D `：只把本地的feature-D分支更新到最新
- `git reset --hard 哈希值`：数据库的回滚操作似的
- `git reflog `  查看仓库的操作日志
- `git mv -k oldName  newName` :更改文件名字

```sh
	usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
```
