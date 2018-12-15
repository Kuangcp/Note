---
title: 应用容器化
date: 2018-12-15 11:27:31
tags: 
    - 工具使用经验
categories: 
    - Docker
---

**目录 start**
 
1. [Docker 安装应用](#docker-安装应用)
    1. [个人镜像](#个人镜像)
    1. [Linux发行版](#linux发行版)
        1. [Ubuntu-ssh](#ubuntu-ssh)
        1. [Alpine-ssh](#alpine-ssh)
        1. [Centos-ssh](#centos-ssh)
    1. [编程语言](#编程语言)
        1. [Java](#java)
            1. [Jib](#jib)
        1. [Node](#node)
        1. [Go](#go)
    1. [数据库](#数据库)
        1. [PostgreSQL](#postgresql)
        1. [Oracle](#oracle)
        1. [MySQL](#mysql)
        1. [MongoDB](#mongodb)
        1. [Redis](#redis)
    1. [持续集成](#持续集成)
        1. [flow.ci](#flowci)
        1. [Jenkins](#jenkins)
    1. [Protobuf](#protobuf)
    1. [git服务器](#git服务器)
        1. [简易git-daemon](#简易git-daemon)
        1. [Gogs](#gogs)
        1. [Gitea](#gitea)
            1. [配置](#配置)
    1. [在线IDE](#在线ide)
        1. [Coding平台的WebIDE](#coding平台的webide)
    1. [图形化管理工具](#图形化管理工具)

**目录 end**|_2018-12-13 12:06_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Docker 安装应用
> [如何创建尽可能小的Docker容器教程](http://www.open-open.com/lib/view/open1419760974078.html)

- [Docker Hub: explore](https://hub.docker.com/explore/)

- [Official: Docker in docker](https://hub.docker.com/_/docker/)
- [Official: registry](https://hub.docker.com/_/registry/)

## 个人镜像
`百度云`
- 配置好SSH服务器的 alpine 3.6 | [docker hub地址](https://hub.docker.com/r/mythkuang/alpine-ssh/) | 百度镜像源: `hub.baidubce.com/mythos/alpine-ssh:1.0` 
    1. `docker run --name sshd -p 8989:22 hub.baidubce.com/mythos/alpine-ssh:1.0`
    1. 设置root用户密码 `docker exec -it sshd passwd`
    1. 登录 `ssh -p 8989 root@localhost`

- Jenkins 镜像 `hub.baidubce.com/mythos/jenkins:2.138.1`

- protobuf的编译环境以及2.5的源码在内 `hub.baidubce.com/mythos/protoc-alpine-src:2.5` 
    - protobuf 的 Alpine 的 2.5版本 `hub.baidubce.com/mythos/protoc-alpine:2.5` 
    - protobuf 的 Ubuntu 的 2.5版本 `hub.baidubce.com/mythos/protoc:2.5`
    - protobuf 的 Alpine 的 3.5.1版本 `hub.baidubce.com/mythos/protoc-alpine:3.5.1`

***********************************
## Linux发行版
> 只适合自己折腾, 不应该用于应用的镜像, 应用不该开放ssh

### Ubuntu-ssh
- 最为简单的是：`docker run  -i -t --name ubuntu17 -p 34433:22 ubuntu /bin/bash`
    - 为这些软件预留端口 `ssh tomcat mysql postgresql mysql oracle nginx reids`
    - 直接跑一个Ubuntu出来,预留出要用的端口，容器运行不会退出
    - 进终端之后就 `apt update` 才能安装软件，现在才知道这个命令的重要性
- 现在的问题是：能不能在已经运行的容器中添加端口映射？？要是用到途中发现端口少了就麻烦了，解决方法可以是commit成镜像再跑出一个容器出来，
- 最好是一个服务（应用）一个容器

**********
- [ ] 日后更新, Dockerfile现在还有bug

- 自己写构建文件，安装相应的软件 
```Dockerfile
    FROM ubuntu
    MAINTAINER kuangcp myth.kuang@gmail.com
    ENTRYPOINT echo "Welcome login server by ssh"
    ENV DEBIAN_FRONTEND noninteractive

    ADD id_rsa.pub /root/.ssh/authorized_keys

    RUN apt-get update; \
        apt-get install -y apt-utils debconf-utils iputils-ping wget curl mc htop ssh; \ 
        chmod 700 /root/.ssh; \
        chmod 600 /root/.ssh/authorized_keys; \
        service ssh start; \ 
    EXPOSE 22
```
- `docker build . -t myth:ssh`
- `docker run -d -t --name myth -p 8989:22 myth:ssh`
- `docker start myth`

### Alpine-ssh
- [alpine-ssh](/Linux/Docker/alpine/alpine-ssh) 
    - 也可以使用百度云镜像 `docker pull hub.baidubce.com/mythos/alpine-ssh:1.0`

### Centos-ssh
- [centos-ssh](https://github.com/jingniao/centos-ssh)

****************************************************************

## 编程语言
### Java
- [Official:Java](https://hub.docker.com/_/java/) `Oracle`
- [openJDK](https://hub.docker.com/_/openjdk/) 
- [oracle-jdk8](https://hub.docker.com/r/frolvlad/alpine-oraclejdk8/)`非常精简`
    - [Github:](https://github.com/frol/docker-alpine-oraclejdk8)`可以学习一波Dockerfile`

- [jdk-alpine-cst](https://hub.docker.com/r/mythkuang/jdk-alpine-cst/)`设置好CST时区的JDK基础镜像`

> [参考博客: Java和Docker限制的那些事儿](http://www.techug.com/post/java-and-docker-memory-limits.html)`描述了一个天坑`

#### Jib
> [参考博客: GOOGLE JIB](https://my.oschina.net/u/3666671/blog/1845065) | [Github:jib](https://github.com/GoogleContainerTools/jib)

### Node
- [Official](https://hub.docker.com/_/node/)

### Go
- [Official](https://hub.docker.com/_/golang/)

**********************************

## 数据库
### PostgreSQL
- [Docker 安装 PostgreSQL](/Database/Postgresql.md)

### Oracle
- [社区文档](https://hub.docker.com/r/wnameless/oracle-xe-11g/)`简单粗暴`

### MySQL
- [官方文档](https://hub.docker.com/_/mysql/)
- `docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag`
- 挂载自定义配置文件 主要是配置编码 以及设定时区
    - `docker run --name mysql-5.6 -v 配置文件目录:/etc/mysql/conf.d  -e MYSQL_ROOT_PASSWORD=mythos1104 -e TZ=Asia/Shanghai -p 3360:3306 -d mysql:5.6`
- 连接`mysql -h 127.0.0.1 -P 3360 -uroot -pmythos1104`

### MongoDB
> [Official](https://hub.docker.com/_/mongo/)

### Redis
> [Official](https://hub.docker.com/_/redis/)

- 获取镜像：`docker pull redis ` 如果使用`redis:alpine`镜像可以更小，但是稳定就。。
- 运行默认配置的容器：`docker run --name test-redis -d redis`
- 使用本地配置文件启动redis容器
- `sudo docker run -v /myredis/conf/redis.conf:/usr/local/etc/redis/redis.conf --name myredis redis redis-server /usr/local/etc/redis/redis.conf`
- port-redis容器的端口映射：`sudo docker run -d -p 6379:6379 --name port-redis redis` 左本机右容器

*****************************************
## 持续集成

> [参考博客: 如何Docker化端到端验收测试](https://www.tuicool.com/articles/YZJzAzF)
### flow.ci
- [flow.ci](https://github.com/flowci/docker) 可以学习compose

******************
### Jenkins
> [详情](/Skills/DevOps/Jenkins.md#docker)

****************************
## Protobuf
1. 创建一个Ubuntu/alpine 容器运行起来
1. 下载 https://github.com/google/protobuf/releases
2. 安装 g++ make 
4. 编译安装下载的源码 进入目录 `./configure --prefix=/usr && make && make check && make install` 

## git服务器
### 简易git-daemon
> 基于git-daemon构建一个Docker镜像, 跑起来直接做git服务器 | [学习使用git-daemon命令](/Linux/Git_Action.md)

```sh
    # 创建一个挂载了本地文件夹的git仓库，并关联到nginx，目录结构和上文一致
    docker run --name git-repos -it -v /home/kuang/Repository/:/root/Repository/ --link mynginx:mynginx alpine
    # 进入容器
    docker exec -it git-repos ash
    # 安装git
    apk update
    apk add git git-daemon
    #　启动服务
    git daemon --export-all --base-path="/root/Repository" --port=55443
```
### Gogs

### Gitea
- [docker 安装 gitea](https://docs.gitea.io/en-us/install-with-docker/) `gitea是一个自助git服务，基于git`
    - [中文版](https://docs.gitea.io/zh-cn/install-with-docker/)
- [gitea配置文件说明](https://docs.gitea.io/zh-cn/config-cheat-sheet/)

#### 配置
> 配置SSH
只要没有禁用掉SSH, 就能和Github一样使用SSH操作仓库, 但是,由于使用的Docker, 所以端口不是默认的22  
所以在本机需要配置下 例如我的就是 6002映射到了22上
`~/.ssh/config`
```conf
    Host git.kuangcp.com
    HostName 111.111.111.111
    User git
    Port 6002
    IdentityFile /home/kcp/.ssh/id_rsa
```
然后就能正常使用了

## 在线IDE
### Coding平台的WebIDE

## 图形化管理工具
DockerUI
- [Portainer](https://github.com/portainer/portainer)

