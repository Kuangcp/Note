---
title: Docker的应用
date: 2018-12-15 11:27:31
tags: 
    - 工具使用经验
categories: 
    - Docker
---

**目录 start**

1. [Docker容器化应用](#docker容器化应用)
    1. [个人镜像](#个人镜像)
    1. [Linux发行版](#linux发行版)
        1. [Ubuntu-ssh](#ubuntu-ssh)
        1. [Alpine-ssh](#alpine-ssh)
        1. [Centos-ssh](#centos-ssh)
    1. [编程语言开发环境](#编程语言开发环境)
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
    1. [博客](#博客)
    1. [在线IDE](#在线ide)
    1. [图形化管理工具](#图形化管理工具)
1. [运行图形化应用](#运行图形化应用)

**目录 end**|_2020-04-27 23:42_|
****************************************
# Docker容器化应用
> [https://docs.docker.com/samples/](https://docs.docker.com/samples/)  
> [Docker Hub: explore](https://hub.docker.com/explore/)

- [Official: Docker in docker](https://hub.docker.com/_/docker/)
- [Official: registry](https://hub.docker.com/_/registry/)

> [如何创建尽可能小的Docker容器教程](http://www.open-open.com/lib/view/open1419760974078.html)
> [参考: 一次 Docker 容器内大量僵死进程排查分析](https://juejin.im/post/5e0002adf265da33dc7a3a1f?from=singlemessage)  

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

1. `docker build . -t myth:ssh`
1. `docker run -d -t --name myth -p 8989:22 myth:ssh`
1. `docker start myth`

### Alpine-ssh
- [dockerfile: alpine-ssh](https://github.com/Kuangcp/DockerfileList/blob/master/alpine/alpine-ssh.dockerfile) 
    - 也可以使用百度云镜像 `docker pull hub.baidubce.com/mythos/alpine-ssh:1.0`

### Centos-ssh
- [centos-ssh](https://github.com/jingniao/centos-ssh)

****************************************************************

## 编程语言开发环境
### Java
- [Official:Java](https://hub.docker.com/_/java/) `Oracle` | [Official: OpenJDK](https://hub.docker.com/_/openjdk/)`从7开始` 

- [frolvlad alpine-java](https://hub.docker.com/r/frolvlad/alpine-java)`非常精简`
    - `个人基于以上镜像 设置好CST中国时区`[jdk-alpine-cst](https://hub.docker.com/r/mythkuang/jdk-alpine-cst/)
    - `可以学习一波Dockerfile` [Github: Dockerfile](https://github.com/frol/docker-alpine-java)

> 个人习惯
- Java7 `docker pull java:7u121-jdk-alpine`
- Java8 `docker pull frolvlad/alpine-java:jdk8.202.08-slim`

> [参考: Java和Docker限制的那些事儿](http://www.techug.com/post/java-and-docker-memory-limits.html)`描述了一个天坑`

#### Jib
> [参考: GOOGLE JIB](https://my.oschina.net/u/3666671/blog/1845065) | [Github:jib](https://github.com/GoogleContainerTools/jib)

### Node
- [Official](https://hub.docker.com/_/node/)
- [Dockerizing a Node.js web app](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/)

### Go
- [Official](https://hub.docker.com/_/golang/)

**********************************

## 数据库
### PostgreSQL
- [Docker 安装 PostgreSQL](/Database/Postgresql.md)

### Oracle
- [社区文档](https://hub.docker.com/r/wnameless/oracle-xe-11g/)`简单粗暴`

### MySQL
- [Docker hub: Mysql](https://hub.docker.com/_/mysql/)

- 简单启动 `docker run --name some-mysql -p 3360:3306 -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag`
    - 容器中默认配置文件为 `/etc/mysql/conf.d/docker.cnf`

- 或者挂载自定义配置文件 主要是配置编码 以及设定时区
    - `docker run --name mysql-5.7 -v 配置文件目录:/etc/mysql/conf.d  -e MYSQL_ROOT_PASSWORD=mythos1104 -e TZ=Asia/Shanghai -p 3360:3306 -d mysql:5.7`

- 连接 `mysql -h 127.0.0.1 -P 3360 -uroot -pmythos1104`

> 最简单方式, 前提是已经安装好 docker-compose

1. [Github](https://github.com/Kuangcp/DockerfileList/tree/master/docker-compose/mysql)`克隆项目,在该目录下执行命令`
    - `docker-compose up -d` 既可创建 正确时区, utf8编码的数据库 

### MongoDB
> [Official](https://hub.docker.com/_/mongo/)

### Redis
> [Official](https://hub.docker.com/_/redis/)

- 获取镜像：`docker pull redis ` 如果使用`redis:alpine`镜像可以更小
- 运行默认配置的容器：`docker run --name test-redis -d redis`
- 使用本地配置文件启动redis容器
- `sudo docker run -v /myredis/conf/redis.conf:/usr/local/etc/redis/redis.conf --name myredis redis redis-server /usr/local/etc/redis/redis.conf`
- port-redis容器的端口映射：`sudo docker run -d -p 6379:6379 --name port-redis redis` 左本机右容器

*****************************************
## 持续集成

> [参考: 如何Docker化端到端验收测试](https://www.tuicool.com/articles/YZJzAzF)
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

> 直接下载二进制最简单...

************************

## git服务器
### 简易git-daemon
> 基于git-daemon构建一个Docker镜像, 跑起来直接做git服务器 | [学习使用git-daemon命令](/Skills/Vcs/GitAction.md#使用-git-daemon-搭建简易-server)

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
> 通过 daemon 能下拉提交代码, nginx 能在线浏览文件

### Gogs

### Gitea
- [docker 安装 gitea](https://docs.gitea.io/en-us/install-with-docker/) `gitea是一个自助git服务，基于git`
    - [中文版](https://docs.gitea.io/zh-cn/install-with-docker/)
- [gitea配置文件说明](https://docs.gitea.io/zh-cn/config-cheat-sheet/)

#### 配置
> 配置SSH

只要没有禁用掉SSH, 就能和Github一样使用SSH操作仓库, 为了避免其他进程的端口冲突, 单独设置端口 例如: 6002映射到了22上  
`~/.ssh/config`
```conf
    Host git.kuangcp.com
    HostName 111.111.111.111
    User git
    Port 6002
    IdentityFile /home/kcp/.ssh/id_rsa
```
然后就能正常使用了

************************

## 博客

> [参考: 使用Docker 实现微服务并搭建博客，一文全掌握。 ](https://mp.weixin.qq.com/s?__biz=MzI3NzE0NjcwMg==&mid=2650121506&idx=1&sn=39e3ba8c5d9698bbfb8acfc6b7e772bf&chksm=f36bb803c41c3115371b69cbd1e626fcaf5a85c7034f96fe495cfbf6dc1630a42dfdd6e342da&mpshare=1&scene=1&srcid=06219wgtCPJNvZP66ccQXRCj#rd)

************************

## 在线IDE
- Coding平台的WebIDE
- eclipse che

- [coder-sever](https://github.com/codercom/code-server)`BS模式的VSCode`

************************

## 图形化管理工具
- DockerUI
- [Portainer](https://github.com/portainer/portainer)

# 运行图形化应用
> [Github Topic](https://github.com/search?p=4&q=docker+desktop&type=Repositories&utf8=%E2%9C%93)
> [Running GUI apps with Docker](https://www.tuicool.com/articles/ayIzI3)
https://www.cnblogs.com/larva-zhh/p/10531824.html
