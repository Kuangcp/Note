---
title: SSH使用总结
date: 2018-12-15 11:20:07
tags: 
    - 工具使用经验
categories: 
    - Linux
---

💠

- 1. [SSH](#ssh)
    - 1.1. [安装](#安装)
    - 1.2. [建立连接](#建立连接)
        - 1.2.1. [复制粘贴建立密钥对](#复制粘贴建立密钥对)
        - 1.2.2. [使用 ssh-copy-id 脚本](#使用-ssh-copy-id-脚本)
    - 1.3. [SSH客户端配置](#ssh客户端配置)
        - 1.3.1. [多密钥对](#多密钥对)
    - 1.4. [服务端配置](#服务端配置)
    - 1.5. [访问图形化](#访问图形化)
    - 1.6. [SSH登录并执行一系列命令](#ssh登录并执行一系列命令)
        - 1.6.1. [通过SSH执行命令时的环境变量问题](#通过ssh执行命令时的环境变量问题)
    - 1.7. [SSH Tunnel](#ssh-tunnel)
- 2. [Tips](#tips)
    - 2.1. [保持SSH连接稳定](#保持ssh连接稳定)
- 3. [Mosh](#mosh)

💠 2024-09-11 14:55:54
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
>> 私钥文件必须是 600 权限  
>> 去除私钥的口令 `openssl rsa -in ~/.ssh/id_rsa -out ~/.ssh/id_rsa_new` _在GitForWindows里面虽然有openssl,但是这个命令却执行不了_  
>> `ssh-add 私钥` 添加私钥到OpenSSH的认证代理  

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

当新增用户testA并开启ssh登录时

- /etc/ssh/sshd_config  新增 AllowUsers testA
- chmod 700 /home/testA/.ssh 
- chmod 600 /home/testA/.ssh/authorized_keys

## 建立连接
### 复制粘贴建立密钥对
_客户端_
- 进入.ssh文件夹下 `gedit id_rsa.pub` 然后复制该公钥内容
    - 或者 `cat ~/.ssh/id_rsa.pub | xclip -sel clip` 将文件复制到剪贴板 
    - 或者 `cat ~/.ssh/id_rsa.pub | xsel -b` 也是文件复制到剪贴板
- 在各种平台服务上添加这个公钥即可免密登录

_服务器端_
- 进入.ssh文件夹下 `sudo vim authorized_keys` 粘贴客户端公钥内容
- 更改文件权限 `sudo chmod 600 authorized_keys`
    - 注意 该文件 group 和 other 位不能有 w 权限

### 使用 ssh-copy-id 脚本
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

## SSH客户端配置
`~/.ssh/config`
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


### 多密钥对
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

## 服务端配置
> 修改登录后的欢迎信息 /etc/motd

一般需要重启ssh服务才生效`/etc/ssh/sshd_config`
```conf
    #禁用密码验证 
    PasswordAuthentication no
    #启用密钥验证
    RSAAuthentication yes
    PubkeyAuthentication yes
```

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

## SSH Tunnel 
>  [Wiki: Tunneling protocol](https://en.wikipedia.org/wiki/Tunneling_protocol#Secure_Shell_tunneling)

简单来说就是可以建立一个双工通道，实现内网穿透，正向代理

> [Is it normal to use an SSH tunnel to access a production database? ](https://www.reddit.com/r/learnrust/comments/11poo5h/is_it_normal_to_use_an_ssh_tunnel_to_access_a/)  
> [How does reverse SSH tunneling work?](https://unix.stackexchange.com/questions/46235/how-does-reverse-ssh-tunneling-work/118650#118650)  

- 创建独立的代理用户 localUser 并生成ssh公私钥，公钥注册到自身ssh的authorized_keys中去
- 本地转发 `ssh localUser@localHost -L  localHost:localPort:remoteHost:remotePort`
    - 在localHost上启动localPort, 当其他客户端连到localPort时，tcp流量会转发到remotePort上去
- 关闭隧道时 exit 退出交互式命令行 注意`不能Ctrl D` 无法正常关闭

************************

# Tips
> 终端抛出`ssh_exchange_identification: Connection closed by remote host` 错误:
```sh
    echo "PermitRootLogin without-password" >> /etc/ssh/sshd_config ;\
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config ;\
```
- 或者尝试 `echo "sshd: ALL" >> /etc/hosts.allow && service sshd restart`

## 保持SSH连接稳定
> man ssh_config

服务端和客户端配置
```conf
    ServerAliveInterval 60
    ServerAliveCountMax 3
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


