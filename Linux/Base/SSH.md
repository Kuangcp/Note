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
        - 1.2.1. [客户端参数说明](#客户端参数说明)
        - 1.2.2. [复制粘贴建立密钥对](#复制粘贴建立密钥对)
        - 1.2.3. [使用 ssh-copy-id 脚本](#使用-ssh-copy-id-脚本)
    - 1.3. [SSH客户端配置](#ssh客户端配置)
        - 1.3.1. [跳板](#跳板)
        - 1.3.2. [多密钥对](#多密钥对)
    - 1.4. [服务端配置](#服务端配置)
        - 1.4.1. [访问图形化](#访问图形化)
    - 1.5. [SSH Tunnel](#ssh-tunnel)
        - 1.5.1. [ZModem](#zmodem)
- 2. [Tips](#tips)
    - 2.1. [传输文件](#传输文件)
    - 2.2. [保持SSH连接稳定](#保持ssh连接稳定)
    - 2.3. [登录并执行批量命令](#登录并执行批量命令)
- 3. [Mosh](#mosh)

💠 2026-06-28 20:33:17
****************************************
# SSH
> Secure Shell 

> [Linux启动或禁止SSH用户及IP的登录](https://blog.csdn.net/linghe301/article/details/8211305)
> [ssh和ssh2之间的免密码登陆详解](http://blog.chinaunix.net/uid-26517277-id-4055228.html)
> [SSH原理与运用（一）：远程登录](http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)
> [SSH原理与运用（二）：远程操作与端口转发](http://www.ruanyifeng.com/blog/2011/12/ssh_port_forwarding.html)

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
### 客户端参数说明
- 默认22端口登录系统`ssh user@host` | 指定端口登录 `ssh -p port user@host`   
- 测试能否登录上 `ssh -T user@host`     

> `ssh -i 私钥绝对路径 user@host` 采用指定私钥登录(一般默认是`.ssh/id_rsa`)  
- 私钥文件必须是 600 权限  
- 去除私钥的口令 `openssl rsa -in ~/.ssh/id_rsa -out ~/.ssh/id_rsa_new` _在GitForWindows里面虽然有openssl,但是这个命令却执行不了_  
- `ssh-add 私钥` 添加私钥到OpenSSH的认证代理  

> 非交互式密码登录
1. 安装sshpass [完整教程](https://linux.cn/article-8086-1.html)
2. sshpass -p '密码' 后接正常的ssh命令 ssh user@host `占用了ssh指定端口的参数，指定端口就需要改成 -P`

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
    IdentityFile  ~/.ssh/id_rsa
    IdentitiesOnly yes
```

_参数解释_
- HostName 指定登录的主机名或IP地址
- Port 指定登录的端口号
- User 登录用户名
- IdentityFile 登录的私钥文件
- IdentitiesOnly 指定只使用当前 `config` 文件中由 `IdentityFile` 明确列出的密钥，或者由 `ssh-agent` 注入的密钥进行认证。
    - **作用**：防止客户端盲目地把本地 `~/.ssh/` 目录下所有的密钥挨个发给服务器去试（如果试的错误密钥超过服务器上限，服务器会直接拒绝连接并报 `Too many authentication failures` 错误）。
- PubkeyAuthentication yes ：显式开启公钥认证模式。
- PasswordAuthentication no ：（可选补充）如果想**彻底禁用密码登录**，只接受 SSH Key 登录，应该使用这个参数。

`ssh aliyun` 即可登录

### 跳板

```conf
# 1. 配置跳板机 A
Host serverA
    HostName 1.1.1.1          # A 的公网 IP
    User root                 # A 的用户名

# 2. 配置目标机 B（核心）
Host serverB
    HostName 10.0.0.2         # B 的内网 IP（在 A 看来能连通的 IP）
    User root                 # B 的用户名
    ProxyJump serverA         # 告诉 SSH：连 B 之前，自动通过 A 进行流量转发 

```

> 注意 ProxyJump 这里的配置支持逗号分隔多个，也就是支持任意多层级跳转 例如  ProxyJump A,B,C 就意为依次跳入ABC，最终进入当前服务端

### 多密钥对
> [参考博客](http://blog.csdn.net/black_ox/article/details/17753943)   

1. `ssh-keygen` 生成SSH密钥对 在询问中输入新的文件名
1. `ssh-add 私钥文件绝对路径`
    - 若执行ssh-add时出现 Could not open a connection to your authentication agent
    - 就先执行 `ssh-agent bash` 对应自己的解释器环境切换 bash zsh
1. 实现不同域名的不同私钥分流

_~/.ssh/config_
```conf
# 只要连接的域名匹配 ://company.com，就自动应用此配置
Host ://company.com
    HostName ://company.com
    User git                          # Git 托管平台的 SSH 用户名一律是 git
    IdentityFile ~/.ssh/id_ed25519_company
    IdentitiesOnly yes                # 关键：绝对不让个人的密钥去撞公司服务器的门

# 只要连接的域名匹配 github.com，就自动应用此配置
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes                # 关键：绝对不让公司的密钥去撞 GitHub 的门
```

1. 同一个域名的不同私钥分流

```conf
# 账户一：个人主力号（别名设为 github.com，克隆时直接用原 URL）
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes

# 账户二：博客自动化部署号（使用别名 github-blog）
Host github-blog
    HostName github.com               # 真实的域名依然是 github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_blog_robot
    IdentitiesOnly yes
```

当你想用“机器人账号”克隆代码时，你需要**手动将 URL 中的真实域名修改为你在 config 中定义的 `Host` 别名**：
*   *原始 URL*：`git@github.com:blog-owner/my-blog.git`
*   *修改后的命令*：git clone git@github-blog:blog-owner/my-blog.git
（效果：SSH 看到 `github-blog` 别名后，会自动把真实地址解析成 `github.com`，并强制带上 `id_ed25519_blog_robot` 这把机器人私钥去登录。）

************************

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

### 访问图形化

在`/etc/ssh/sshd_config`添加以下信息，然后重启ssh服务
```
    X11Forwarding yes
    X11DisplayOffset 10
```
- `ssh -X -p port user@host` 登录即可
    - 使用过一次,发现了严重的内存泄露,也不知道是什么原因


## SSH Tunnel 
>  [Wiki: Tunneling protocol](https://en.wikipedia.org/wiki/Tunneling_protocol#Secure_Shell_tunneling)

简单来说就是可以建立一个双工通道，实现内网穿透，反向代理

> [Is it normal to use an SSH tunnel to access a production database? ](https://www.reddit.com/r/learnrust/comments/11poo5h/is_it_normal_to_use_an_ssh_tunnel_to_access_a/)  
> [How does reverse SSH tunneling work?](https://unix.stackexchange.com/questions/46235/how-does-reverse-ssh-tunneling-work/118650#118650)  

- 创建独立的代理用户 localUser 并生成ssh公私钥，公钥注册到自身ssh的authorized_keys中去
- 本地转发 `ssh localUser@localHost -L  localHost:localPort:remoteHost:remotePort`
    - 在localHost上启动localPort, 当其他客户端连到localPort时，tcp流量会转发到remotePort上去
- 关闭隧道时 exit 退出交互式命令行 注意`不能Ctrl D` 无法正常关闭

### ZModem
ZModem（包括它的前身 XModem、YModem）诞生于 20 世纪 80 年代（1980s），那个时候还没有互联网（Internet），人们上网是通过电话线拨号连接到 BBS（电子公告牌系统）。

快速记忆： send zmodem file `sz` 与之对应的就是 receive `rz`

- 服务器端： 你敲下 sz run.log，服务器上的 sz 程序开始往这个 TTY 隧道里发送 ZModem 的控制字符和二进制文本流。
- 网络传输： 这些数据被 SSH 协议打包、加密，安全的传输到你本地的电脑。
- 本地接收端： 
    - 如果是 Xshell / SecureCRT / MobaXterm：这些商用终端内置了“听音辨位”的功能。它们解密出 SSH 数据后，发现里面夹带了 ZModem 的控制特征码，立马拦截这部分数据，在本地弹出保存框，帮你把文件存下来。
    - 如果是 Xfce-terminal / Gnome-terminal：这些 Linux 现代终端极其纯粹，它们只负责把解密后的字符原封不动地打印在屏幕上。因为它们没有内置“ZModem 听音机”，所以它看不懂那些特征码，最终结果就是你的屏幕被 sz 喷出的二进制乱码疯狂刷屏，或者直接卡死。

> Xfce Terminal、Gnome Terminal、Alacritty 这种 Linux 下的标准现代终端，出于安全和架构精简的考虑，都没有原生内置 ZModem 模块.
- 协议漏洞（会断流卡死）：ZModem 强行把文件数据伪装成文本传输。如果你的日志文件 b.log 里面刚好包含了一些特殊的控制字符（比如 Ctrl+C 的 ASCII 码、或者换行符符集），有时候会误触发终端的控制快捷键，导致传输直接断开或者会话卡死。
- 安全隐患：ZModem 允许服务器端主动向本地终端发起文件写入。如果黑客攻陷了你的服务器，他在服务器反向执行一个恶意的 sz 脚本，如果你的本地终端不够安全，它可能会利用漏洞直接在你的本地电脑上写入恶意文件。
- 现代有更好的亲儿子协议：SFTP / SCP 或者 SSHFS 将服务器目录挂载到本地

************************

# Tips
> 终端抛出`ssh_exchange_identification: Connection closed by remote host` 错误:

```sh
    echo "PermitRootLogin without-password" >> /etc/ssh/sshd_config ;\
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config ;\
```
- 或者尝试 `echo "sshd: ALL" >> /etc/hosts.allow && service sshd restart`

************************

> SSH: Could not load host key: /etc/ssh/ssh_host_rsa_key
- `/usr/bin/ssh-keygen -A` 生成所有方式的密钥对

## 传输文件
> 传统思路 用scp命令，或者 用支持ZModem协议的终端软件跑sz命令

> [libfuse/sshfs: A network filesystem client to connect to SSH servers](https://github.com/libfuse/sshfs)  

可以通过sshfs将服务端的文件系统挂载到本地，用文件管理器或者 cp mv 命令就可以实现快速文件操作了

建立映射很简单，先建个空目录，然后挂载到本地： `sshfs -p 8118 root@192.168.2.7:/root /mnt/fs1`  
卸载挂载  fusermount3 -u /mnt/fs1  

sshfs -f 前台执行 -o debug 显示日志信息 

> 特殊情况

如果没法直接连接到目标服务需要跳转，就参考 [跳板](#跳板) 配置好，例如通过ABC跳转入D，那最终sshfs挂载命令是 `sshfs D:/root /mnt/fs1`
但是，如果跳转的路径上存在需要交互输入密码的情况，sshfs就会卡住了，因为sshfs没法像普通ssh那样会弹出tty输入密码，还可以通过sshpass自动输入然后自动进入。

```
Host D
    ...
    ProxyJump A,B,C
    # 加这三个配置
    ControlMaster auto
    ControlPath ~/.ssh/sockets/%r@%h:%p
    ControlPersist 10m              # 保持通道在后台空闲存活10分钟
```

先执行 sshpass -p 'xxx' ssh D 建立连接后，再执行  sshfs D:/root /mnt/fs1 就能成功挂载了，这个时候sshfs会复用已有的隧道，就能绕开上述没法交互式输入密码的问题了

## 保持SSH连接稳定
> man ssh_config

服务端和客户端配置
```conf
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

## 登录并执行批量命令
```sh
    ssh user@host 'cmd \
        && cmd \'
```

ssh登录然后执行一系列命令, 命令里如果有sudo会执行不了 需要加 -t 参数才行 

> 这些命令执行时的环境变量问题

详细在于不同的shell中 Linux 环境变量加载的不同

- 简单方式: 手动加载环境变量 `ssh name@host "source ~/.bashrc && java -version"`

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


