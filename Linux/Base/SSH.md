---
title: SSH使用总结
date: 2018-12-15 11:20:07
tags: 
    - 工具使用经验
categories: 
    - Linux
---

**目录 start**

1. [SSH](#ssh)
    1. [安装](#安装)
    1. [复制粘贴建立密钥对](#复制粘贴建立密钥对)
    1. [使用脚本更简单](#使用脚本更简单)
    1. [SSH配置文件](#ssh配置文件)
    1. [多密钥对](#多密钥对)
    1. [访问图形化](#访问图形化)
    1. [SSH登录并执行一系列命令](#ssh登录并执行一系列命令)
        1. [通过SSH执行命令时的环境变量问题](#通过ssh执行命令时的环境变量问题)
1. [Tips](#tips)
1. [Mosh](#mosh)

**目录 end**|_2020-04-27 23:42_|
****************************************
# SSH
> Secure Shell 

> [Linux启动或禁止SSH用户及IP的登录](https://blog.csdn.net/linghe301/article/details/8211305)
> [ssh和ssh2之间的免密码登陆详解](http://blog.chinaunix.net/uid-26517277-id-4055228.html)
> [SSH原理与运用（一）：远程登录](http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)
> [SSH原理与运用（二）：远程操作与端口转发](http://www.ruanyifeng.com/blog/2011/12/ssh_port_forwarding.html)

- 默认22端口登录系统`ssh user@host` | 指定端口登录 `ssh -p port user@host`   
- 测试能否登录上 `ssh -T user@host`     

> `ssh -i 私钥绝对路径 user@host` 采用指定私钥登录(一般默认是`.ssh/id_rsa`)  
>> 私钥一定要是 600 权限  
>> 去除私钥的口令 `openssl rsa -in ~/.ssh/id_rsa -out ~/.ssh/id_rsa_new` _在GitForWindows里面虽然有openssl,但是这个命令却执行不了_

使用密码方式免去密码登录
>1. 安装sshpass [完整教程](https://linux.cn/article-8086-1.html)
>2. sshpass -p '密码' 后接正常的ssh命令 ssh user@host

> ssh登录然后执行一系列命令, sudo会执行不了 需要加 -t 参数才行 

******************

## 安装
_客户端_
- `sudo apt-get install openssh-client`
- 生成密钥对 `ssh-keygen` 可以设置密码，为了方便也可以全部采用默认(不安全)

_服务端_
- 安装：`sudo apt-get install openssh-server`
- 启动：`sudo /etc/init.d/ssh start` 或者 `service ssh start` 
- 更改配置文件修改默认端口 `/etc/ssh/sshd_config`
- 查看对否启动sshd`ps -e |grep ssh`
- 关闭服务 `/etc/init.d/ssh stop`

## 复制粘贴建立密钥对
_客户端_
- 进入.ssh文件夹下 `gedit id_rsa.pub` 然后复制该公钥内容
    - 或者 `cat ~/.ssh/id_rsa.pub | xclip -sel clip` 将文件复制到剪贴板 
    - 或者 `cat ~/.ssh/id_rsa.pub | xsel -b` 也是文件复制到剪贴板
- 在各种平台服务上添加这个公钥即可免密登录

_服务器端_
- 进入.ssh文件夹下 `sudo vim authorized_keys` 粘贴客户端公钥内容
- 更改文件权限 `sudo chmod 600 authorized_keys` 确保 其 group和other位没有 w 权限

## 使用脚本更简单
- 两方安装好软件 客户端生成好了秘钥对之后
- 默认端口:`ssh-copy-id "username@host"` 输密码就可以了
- 指定端口 `ssh-copy-id ”-p port username@host“` 
    - 或者:`ssh-copy-id " username@host" -p port`
    
- 成功后 客户端登录 `ssh -p 22 username@ip`
    - root用户一般需要修改:
    - `/etc/ssh/sshd_confg` 文件中PermitRootLogin  no 改为yes 重新启动ssh服务。

- 注意:
    - 一个端口和IP如果之前记录过相关信息,然后服务器重装了系统或者别的原因, 修改了服务器秘钥 
    - 再次连接新的系统按着提示来运行一条命令即可
    - 例如 `ssh-keygen -f "/home/kcp/.ssh/known_hosts" -R 120.78.154.52`

## SSH配置文件
`vim ~/.ssh/config`
```
    Host aliyun
        HostName www.ttlsa.com
        Port 22
        User root
        IdentityFile  ~/.ssh/id_rsa.pub
        IdentitiesOnly yes
```

_参数解释_
```
    HostName 指定登录的主机名或IP地址
    Port 指定登录的端口号
    User 登录用户名
    IdentityFile 登录的公/私钥文件 奇怪的是有时候用公有时候用私??
    IdentitiesOnly 只接受SSH key 登录
    PubkeyAuthentication
```
- `ssh aliyun` 即可登录 但是要输入生成公钥时的密码， _方便多公钥的情况_
    - 如果生成公钥时_没有_设置密码就要错三次，然后输入用户密码，
    - 不觉得有多方便，还不如 alias进行配置

> 修改欢迎信息 /etc/motd

## 多密钥对
> [参考博客](http://blog.csdn.net/black_ox/article/details/17753943)   

1. `ssh-keygen` 生成SSH密钥对 在询问中输入新的文件名
2. `ssh-add 私钥文件绝对路径`
    - 若执行ssh-add时出现Could not open a connection to your authentication agent
    - 就先执行 `ssh-agent bash` 对应自己的解释器环境
3. 如上 创建配置文件 config
    - 在git项目中使用别名:正常的项目，我们clone下来之后，origin对应的URL假设为: `git@git.:Rusher/helloworld`
    - 现在需要做个改动，将git, 要换成rusher_gitlab:
        - `git remote set-url origin git@rusher_gitlab:Rusher/helloworld`
    - 如果是root用户的项目:
        - `git remote set-url origin git@root_gitlab:root/helloworld`

_config_
```
    Host default
    HostName github.com
    User git
    IdentityFile ~/.ssh/default_id_rsa.pub
```
- 测试配置是否正确: `ssh -T git@default`

## 访问图形化

在`/etc/ssh/sshd_config`添加以下信息，然后重启ssh服务
```
    X11Forwarding yes
    X11DisplayOffset 10
```
- `ssh -X -p port user@host` 登录即可
    - 使用过一次,发现了严重的内存泄露,也不知道是什么原因

## SSH登录并执行一系列命令
```sh
    ssh user@host 'cmd \
        && cmd \'
```

### 通过SSH执行命令时的环境变量问题
详细在于不同的shell中 Linux 环境变量加载的不同

- 简单方式: 手动加载环境变量 `ssh name@host "source ~/.bashrc && java -version"`

************************

# Tips
> 终端抛出`ssh_exchange_identification: Connection closed by remote host` 错误:
```sh
    echo "PermitRootLogin without-password" >> /etc/ssh/sshd_config ;\
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config ;\
```
- 或者尝试 `echo "sshd: ALL" >> /etc/hosts.allow && service sshd restart`

************************

> 连接时提示错误信息 前提：配置好了公钥，即使有这个信息，但是却已经连上了
```sh
$ ssh -p 8888 git@184.170.220.117
    The authenticity of host '[184.170.220.117]:8888 ([184.170.220.117]:8888)' can't be established.
    ECDSA key fingerprint is SHA256:Ha9k9dsMxtTaDgN4maUy1VoNzzsm+uMb84zcib6U5jU.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added '[184.170.220.117]:8888' (ECDSA) to the list of known hosts.
    PTY allocation request failed on channel 0
    Welcome to GitLab, Carlsiry Chen!
    Connection to 184.170.220.117 closed.
```

************************

> SSH: Could not load host key: /etc/ssh/ssh_host_rsa_key
- `/usr/bin/ssh-keygen -A` 生成所有方式的密钥对

************************

# Mosh
> [Official Site](https://mosh.org/)  

采用UDP协议实现, 对带宽需求更小, 但是设计上有很明显的优点和缺点...

- 优点: 占用带宽小, 速度快, 无连接的 
    - 会话的中断不会导致当前正在前端执行的命令中断，相当于你所有的操作都是在screen命令中一样在后台执行。
    - 会话在中断过后，不会立刻退出，而是启用一个计时器，当网络恢复后会自动重新连接，同时会延续之前的会话，不会重新开启一个。
- 缺点: 连接是一次性的, 往往需要额外配置UDP端口

简易使用
1. 服务端使用指定端口启动, `mosh-server -p 6005` 默认是随机在 60001-61000 
    - 复制好启动输出的秘钥
1. 客户端 `MOSH_KEY=秘钥 mosh-client ip port`


