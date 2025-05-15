---
title: Docker进阶
date: 2018-12-15 11:25:27
tags: 
categories: 
    - Docker
---

💠

- 1. [Docker Advance](#docker-advance)
    - 1.1. [文件系统](#文件系统)
        - 1.1.1. [AUFS](#aufs)
        - 1.1.2. [OverlayFS](#overlayfs)
    - 1.2. [配置](#配置)
        - 1.2.1. [更改数据的存放目录](#更改数据的存放目录)
        - 1.2.2. [提供底层接口访问](#提供底层接口访问)
            - 1.2.2.1. [暴露守护进程端口](#暴露守护进程端口)
            - 1.2.2.2. [持有套接字文件](#持有套接字文件)
- 2. [Tips](#tips)
    - 2.1. [孤儿进程以及僵死进程](#孤儿进程以及僵死进程)

💠 2025-05-15 15:33:14
****************************************
# Docker Advance

## 文件系统
> Docker支持 AUFS、Btrfs、Device mapper、OverlayFS、Overlay2FS、ZFS 

### AUFS
> Docker旧版本 采用的是 AUFS 文件系统

> [参考: 剖析Docker文件系统：Aufs与Devicemapper](http://www.infoq.com/cn/articles/analysis-of-docker-file-system-aufs-and-devicemapper)
> [参考: 理解Docker（7）：Docker 存储 - AUFS](http://www.cnblogs.com/sammyliu/p/5931383.html)

> [参考: Docker: Just Stop Using AUFS](https://sthbrx.github.io/blog/2015/10/30/docker-just-stop-using-aufs/)

### OverlayFS
> 最新的Docker都是采用这种文件系统, 并具有 overlay overlay2 两代驱动

> [参考: docker 存储驱动之overlay](https://blog.csdn.net/u010278923/article/details/79215828)

> 查看占用大小 docker system df 

强行修改和复制文件：

- 所有容器和创建出来的volumes 都在 /var/lib/docker 下的 volumes 或 overlay2 下
- 例如复制一个Redis的容器（未挂载出volumes）
    - find . -iname dump.rdb 找到文件所在，按创建时间和大小找到想要的数据，复制出来即可，或者替换成自己想要的
    - 因为如果是Redis容器运行时替换dump.rdb文件，那么在容器停止时内存的数据会覆盖磁盘的 dump.rdb 文件。

****************

## 配置
> [官方检查配置的脚本](https://github.com/moby/moby/blob/master/contrib/check-config.sh)

### 更改数据的存放目录

> docker 默认是将数据放在了 `/var/lib/docker` 下, 包括所有的镜像, 容器, 卷...

1. `挂载新的目录到 /var/lib/docker 上`
> [参考: Docker数据将跟分区磁盘占满了 ](http://dockone.io/question/531)
> [参考: Docker 常见问题 (FAQ)](https://www.lsproc.com/post/docker-faq/#toc_1)
```sh
service docker stop
cp -prf /var/lib/docker /data/
rm -rf /var/lib/docker

vi /etc/fstab # 追加一下内容：
/data/docker /var/lib/docker none bind 0 0
mount -a
service docker start
```
2. 还尝试过将文件复制出去, 然后用软链接的方式, 但是失败了 报的错也没怎么看懂
3. 修改配置文件
```
-g, --graph=""
  Path to use as the root of the Docker runtime. Default is /var/lib/docker.

如 docker -d --graph=/opt/docker
docker daemon 的启动参数修改方法

rhel/centos 下, 默认启动参数在 /etc/sysconfig/docker, 如:

6.x:
other_args="--graph=/opt/docker "

7.x: (update: 2015-01-21)
OPTIONS="--graph=/opt/docker "

debian/ubuntu 下, 默认启动参数在 /etc/default/docker, 如:
DOCKER_OPTS="--graph=/opt/docker "

```

### 提供底层接口访问
#### 暴露守护进程端口

1. systemctl edit docker.service
```ini
    [Service]
    ExecStart=
    ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock 
```
> 以上所处文件为: /etc/systemd/system/docker.service.d/override.conf 
>> 注意: `-H unix:///var/run/docker.sock` 如果少了这个配置, Docker客户端就失效了, 什么都干不了

2. systemctl restart docker 

> 而那些不是使用systemd管理服务的才要在 /etc/docker/ 下配置 daemon.json [official doc](https://docs.docker.com/engine/reference/commandline/dockerd/)

#### 持有套接字文件
> 将 `/var/run/docker.sock` 的访问权限 提供给使用方即可

# Tips
> WARNING: No swap limit support

1. Edit the /etc/default/grub file.
  - Set the GRUB_CMDLINE_LINUX value as follows:
  - GRUB_CMDLINE_LINUX="cgroup_enable=memory swapaccount=1"
1. sudo update-grub
1. Reboot your system.

## 孤儿进程以及僵死进程
> [进程相关知识](/Linux/Base/LinuxBase.md#进程)  
> 当父进程结束后,原来的僵死子进程, 会成为孤儿进程且是僵死进程, 此时会被1号进程收养  

> [参考: Docker和孤儿进程、僵死进程 ](https://yq.aliyun.com/articles/61894)  
> 在 Docker 中, 由于没有 init 这个1号进程(往往是应用进程作为1号进程) 很有可能子进程称为僵死进程且一直存在  
> Docker1.11之前的版本，孤儿进程是否有可能成为僵死进程取决于容器内pid为1的进程是否在子进程退出时调用wait/waitpid  
> Docker1.11版本之后孤儿进程不会成为僵死进程

**解决策略**
> [tini](https://github.com/krallin/tini#using-tini)  `tini 轻量级init进程 更好的管理进程等资源`
