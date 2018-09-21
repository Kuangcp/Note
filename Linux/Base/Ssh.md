`目录 start`
 
- [SSH](#ssh)
    - [1.安装软件](#1安装软件)
    - [2.复制粘贴建立密钥对](#2复制粘贴建立密钥对)
    - [2.使用脚本更简单](#2使用脚本更简单)
    - [3.遇到的问题](#3遇到的问题)
    - [4.SSH配置文件](#4ssh配置文件)
    - [5.多密钥对](#5多密钥对)
    - [6.访问图形化](#6访问图形化)
    - [7.ssh登录并执行一系列命令](#7ssh登录并执行一系列命令)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# SSH
> [Linux启动或禁止SSH用户及IP的登录](https://blog.csdn.net/linghe301/article/details/8211305)
> [ssh和ssh2之间的免密码登陆详解](http://blog.chinaunix.net/uid-26517277-id-4055228.html)
> [SSH原理与运用（一）：远程登录](http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)
> [SSH原理与运用（二）：远程操作与端口转发](http://www.ruanyifeng.com/blog/2011/12/ssh_port_forwarding.html)

- `ssh user@host` 默认22端口登录系统  
- `ssh -p port user@host` 指定端口登录  
- `ssh -T user@host` 测试能否登录上    

> `ssh -i 私钥绝对路径 user@host` 采用指定私钥登录(一般默认是`.ssh/id_rsa`)  
>> 私钥一定要是 600 权限
>> 去除私钥的口令 `openssl rsa -in ~/.ssh/id_rsa -out ~/.ssh/id_rsa_new` _在GitForWindows里面虽然有openssl,但是这个命令却执行不了_

> 使用密码方式免去密码登录(因为一些奇怪的需求, 又想省事)
>> 1. 安装sshpass [完整教程](https://linux.cn/article-8086-1.html)
>> 2. sshpass -p '密码' 后接正常的ssh命令 ssh user@host

> ssh登录然后执行一系列命令, sudo会执行不了 需要加 -t 参数才行 


## 1.安装软件
_客户端安装软件_
- `sudo spt-get install openssh-client`
- 生成密钥对 `ssh-keygen` 可以设置密码，为了方便也可以全部采用默认

_服务端安装软件_
- 安装：`sudo apt-get install openssh-server`
- 启动：`sudo /etc/init.d/ssh start` 或者 `service ssh start` 
- 更改配置文件修改默认端口 `/etc/ssh/sshd_config`
- 查看对否启动sshd`ps -e |grep ssh`
- 关闭服务 `/etc/init.d/ssh stop`

## 2.复制粘贴建立密钥对
_客户端_
- 进入.ssh文件夹下 `gedit id_rsa.pub` 然后复制该公钥内容
    - 或者 `cat ~/.ssh/id_rsa.pub | xclip -sel clip` 将文件复制到剪贴板 
    - 或者 `cat ~/.ssh/id_rsa.pub | xsel -b` 也是文件复制到剪贴板
- 在各种平台服务上添加这个公钥即可免密登录

_服务器端_
- 进入.ssh文件夹下 `sudo vim authorized_keys` 粘贴客户端公钥内容
- 更改文件权限 `sudo chmod 600 authorized_keys` 确保 其 group和other位没有 w 权限

## 2.使用脚本更简单
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

## 3.遇到的问题
- 终端抛出`ssh_exchange_identification: Connection closed by remote host` 错误:
```sh
    echo "PermitRootLogin without-password" >> /etc/ssh/sshd_config ;\
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config ;\
```
- 或者尝试 `echo "sshd: ALL" >> /etc/hosts.allow && service sshd restart`
********
_这是什么问题,这么6的么, 配置好了公钥_
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
_emmm.出现这样的输出竟然是连接上了,,,_

## 4.SSH配置文件
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
## 5.多密钥对
> [参考博客](http://blog.csdn.net/black_ox/article/details/17753943)   

1. `ssh-keygen` 生成SSH密钥对
    - 然后在询问中输入新的文件名
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

## 6.访问图形化

在`/etc/ssh/sshd_config`添加以下信息，然后重启ssh服务
```
    X11Forwarding yes
    X11DisplayOffset 10
```
- `ssh -X -p port user@host` 登录即可
    - 使用过一次,发现了严重的内存泄露,也不知道是什么原因

## 7.ssh登录并执行一系列命令
```sh
    ssh user@host 'cmd \
        && cmd \'
```