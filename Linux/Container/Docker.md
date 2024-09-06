---
title: Docker
date: 2018-12-15 11:24:44
tags: 
    - 基础
categories: 
    - Docker
---

💠

- 1. [Docker](#docker)
    - 1.1. [简介](#简介)
    - 1.2. [学习资源](#学习资源)
- 2. [安装与卸载](#安装与卸载)
    - 2.1. [Linux](#linux)
        - 2.1.1. [安装包安装](#安装包安装)
        - 2.1.2. [不加sudo执行docker命令](#不加sudo执行docker命令)
        - 2.1.3. [Ubuntu](#ubuntu)
        - 2.1.4. [Debian](#debian)
        - 2.1.5. [Centos](#centos)
        - 2.1.6. [Arch](#arch)
    - 2.2. [Windows](#windows)
    - 2.3. [图形化管理工具](#图形化管理工具)
        - 2.3.1. [Portainer](#portainer)
- 3. [基础管理](#基础管理)
    - 3.1. [配置代理](#配置代理)
    - 3.2. [配置镜像源](#配置镜像源)
    - 3.3. [搭建本地镜像仓库](#搭建本地镜像仓库)
        - 3.3.1. [Push over HTTP](#push-over-http)
    - 3.4. [基础命令](#基础命令)
    - 3.5. [镜像](#镜像)
    - 3.6. [容器](#容器)
        - 3.6.1. [ps](#ps)
        - 3.6.2. [create](#create)
        - 3.6.3. [run](#run)
            - 3.6.3.1. [资源限制](#资源限制)
        - 3.6.4. [exec](#exec)
        - 3.6.5. [port](#port)
    - 3.7. [端口映射](#端口映射)
- 4. [数据存储](#数据存储)
    - 4.1. [文件系统](#文件系统)
    - 4.2. [数据卷](#数据卷)
    - 4.3. [数据卷容器](#数据卷容器)
- 5. [容器编排](#容器编排)
    - 5.1. [Docker-Compose](#docker-compose)
        - 5.1.1. [配置文件](#配置文件)
        - 5.1.2. [使用命令](#使用命令)
        - 5.1.3. [Tips](#tips)
    - 5.2. [Docker-Machine](#docker-machine)
    - 5.3. [Docker-Swarm](#docker-swarm)
- 6. [网络](#网络)
    - 6.1. [None](#none)
    - 6.2. [Host](#host)
    - 6.3. [Bridge](#bridge)
    - 6.4. [User-defined](#user-defined)
    - 6.5. [跨主机容器通信](#跨主机容器通信)
        - 6.5.1. [overlay](#overlay)
- 7. [Dockerfile](#dockerfile)

💠 2024-09-06 11:36:43
****************************************
# Docker
> [Official Doc](https://docs.docker.com/) | [docker-cn](www.docker-cn.com)`Docker中国`

- [docker中文](http://www.docker.org.cn/)`社区`

- [Gitbook: docker 从入门到实践](https://yeasy.gitbooks.io/docker_practice/content/)

- [docker-android](https://github.com/budtmo/docker-android)

## 简介
> `Docker 是一个开源的应用容器引擎` 理解为轻量版虚拟机(不模拟硬件层)

## 学习资源
- [PMD: player with docker](https://labs.play-with-docker.com/)`线上练习Docker环境`
- [docker-slim](https://github.com/docker-slim/docker-slim)`镜像瘦身`
- [ ] todo [Use multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/) `17.05+`

- [dockerlabs](https://github.com/collabnix/dockerlabs)

************************

> [码云上Docke相关资源](https://gitee.com/explore/starred?lang=Docker)
- [docker-training 开源项目](https://gitee.com/dockerf/docker-training)
    - [第二课](https://gitee.com/dockerf/second)
- [Dockerfile集锦](https://gitee.com/kennylee/docker)
- [Oracle的Dockerfile仓库](https://github.com/oracle/docker-images)

- [ 具有中国特色的docker折腾记（上）](http://blog.csdn.net/Raptor/article/details/18305299)
    - [ 具有中国特色的docker折腾记（下）](http://blog.csdn.net/raptor/article/details/18405569)

> [docker资源汇总 ](http://www.open-open.com/lib/view/open1443075440623.html)
> [简述 Docker](http://www.importnew.com/24658.html)


***************************************
# 安装与卸载
> [daocloud安装帮助](http://get.daocloud.io/#install-docker) | [Docker 加速器](http://guide.daocloud.io/dcs/daocloud-9153151.html)

> [中科大Docker仓库镜像源](https://lug.ustc.edu.cn/wiki/mirrors/help/docker)

## Linux
> [Official doc](https://docs.docker.com/install/linux/docker-ce/) `所有的发行版`

> docker.io 是旧版本 现在新的Docker分为 docker-ce  docker-ee  
> 注意 Deepin上 如果通过 apt 去安装 docker-compose 它会把 docker-ce 卸掉, 装旧的 docker.io 

### 安装包安装
> [官方文件地址](https://download.docker.com/linux/)

- _Debian系_
    - [deb包选择](https://download.docker.com/linux/debian/dists/)
    - 进去后选择debain的版本，deepin15.4 的版本是stretch 然后pool/stable/amd64/选版本即可 
    - 例如：[Deepin 15.4直接点这里](https://download.docker.com/linux/debian/dists/stretch/pool/stable/amd64/)
    - `这两种方式装的是同一个版本号` 
    - 双击或者`sudo dpkg -i deb文件`
    - 测试安装成功 `sudo docker run hello-world`

### 不加sudo执行docker命令
> [官方文档](https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user)

- 如果没有docker组，添加组 `sudo groupadd docker `
- 将当前用户加入用户组 `sudo gpasswd -a $USER docker`
- 然后重新注销登录，或者退出会话重新登录即可

### Ubuntu
- [Official: Ubuntu安装最新版](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1)
- `sudo apt install docker-ce`
    - 关闭服务则是标准服务操作, service docker stop 

`snap`
- 安装snap `sudo apt install snapd`
- 查看适用于当前系统的包：`snap install find`
- 安装： `snap install docker`

### Debian
> [参考](http://www.docker.org.cn/book/install/install-docker-on-debian-8.0-jessie-34.html)
- `sudo echo "deb http://http.debian.net/debian jessie-backports main" >> /etc/apt/sources.list`
- `sudo apt-get install docker-ce`

1. `前置软件` sudo apt-get install \
     apt-transport-https \
     ca-certificates \
     curl \
     gnupg2 \
     lsb-release \
     software-properties-common

> [使用清华大学镜像源安装](https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/)

### Centos
- `sudo yum install docker`
    - Ubuntu的话,Docker没有启动, 只要一执行Docker相关命令就会自动启动, 但是Centos要手动启动
    - `service docker start`  设置开机启动: `chkconfig docker on`

### Arch
- `pacman -S docker`

************************

## Windows
> Windows上本质是用了VirtualBox创建虚拟机来跑Docker, 屎一般的体验, 然而Win10的WSL因为不能模拟aufs 以及 cgroup 所以能装不能用  
> 只能装上docker for windows 然后把Docker守护进程的套接字文件配置给wsl用。。。。。

- [参考博客](http://www.cnblogs.com/linjj/p/5606687.html)
- [官方toolbox 下载](https://www.docker.com/products/docker-toolbox)
- 然后双击安装，勾选上virtualbox 记住cpu要开虚拟化
- 安装完成后就会有三个图标在桌面上，然后进入Docker Quickstart Terminal后 `docker run hello-world` 有正常输出即可
**************************************

## 图形化管理工具
> [lazydocker](https://github.com/jesseduffield/lazydocker)  

### Portainer
> [Official Site](https://www.portainer.io/)  | [installation](https://www.portainer.io/installation/)

1. `docker volume create portainer_data`
1. `docker run --name portainer -d -p 8000:8000 -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce`


# 基础管理
> docker 所有的数据默认存储在 `/var/lib/docker`

> [ctop](https://github.com/bcicen/ctop)`Top-like interface for container metrics`  

- [bitnami](https://bitnami.com/)`非官方，但是维护了很多常用软件的镜像`  

## 配置代理
2024-06-06 开始封禁Dockerhub及国内源，所以最稳妥的还是用代理

> 设置代理方式
- mkdir -p /etc/systemd/system/docker.service.d
- vim /etc/systemd/system/docker.service.d/http-proxy.conf
    ```conf
    [Service]
    Environment="HTTP_PROXY=http://localhost:7890"
    Environment="HTTPS_PROXY=http://localhost:7890"
    # 可选项，配置不走代理的仓库
    Environment="NO_PROXY=your-registry.com,10.10.10.10,*.example.com"
    ```
- systemctl daemon-reload
- systemctl restart docker
- 检查环境变量 systemctl show --property=Environment docker
- 查看代理 docker info

## 配置镜像源
> 默认的DockerHub因为在国外所以网络不太稳定，需要使用国内镜像源

- [Official doc](https://docs.docker.com/registry/recipes/mirror/)

`三种使用的方式`
1. 使用指定的URL `docker pull registry.docker-cn.com/myname/myrepo:mytag`
2. 仅仅配置当前守护进程, 重启就失效了`docker --registry-mirror=https://registry.docker-cn.com daemon`
3. 修改 `/etc/docker/daemon.json`文件, 永久性更改
```json
    {"registry-mirrors": ["https://registry.docker-cn.com"]}
```

> 时速云
- `sudo docker pull index.tenxcloud.com/<namespace>/<repository>:<tag>`
- 下载后可以用别名 `docker tag index.tenxcloud.com/docker_library/node:lastest node:lastest`

********************************
## 搭建本地镜像仓库
> [Official doc](https://docs.docker.com/registry/#requirements)

> [参考：Docker Registry V1 与 V2 的区别解析以及灵雀云的实时同步迁移实践](https://www.csdn.net/article/2015-09-09/2825651)

> [Github:v1](https://github.com/docker/docker-registry) | [Github:v2](https://github.com/docker/distribution)

> v1
- 服务器上运行 并映射到本地目录 `docker run -d -p 5000:5000 -v /opt/data/registry:/tmp/registry registry`
- 对服务器中docker已经有的镜像 设置别名 `docker tag 镜像 ip:port/镜像名`
- docker push ip:port/镜像名
- 查看服务器上仓库的镜像 `curl http://IP:5000/v1/search `

> v2
- 启动镜像 `docker run -d -p 5000:5000 --name registry registry:2` 
- 一样的设置好别名， 然后push上去
- 查看仓库中的镜像 `curl IP:5000/v2/_catalog`

### Push over HTTP
> **注意** 由于 docker client 默认是用的 HTTPS 方式通信， 但是这个本地的 registry 默认是 HTTP 的， 所以有几种解决方案

1. 直接将本地仓库的IP和端口 设置为本地Docker的白名单
    - 给dockerd 添加参数 `DOCKER_OPTS="--insecure-registry ip:port"`
    - 或者配置 `/etc/docker/daemon.json` 增加白名单  `{ "insecure-registries":["IP:PORT"] }`
    - **重启**Docker服务
1. 将 registry 配置为 HTTPS， 那么就需要配置SSL证书， 使用本地证书或者公网证书

********************************
## 基础命令
> 直接运行 docker, 就会有命令的使用提示 例如查看docker版本 `docker version`

_登录镜像仓库_
- 登录hub.docker ：`docker login ` 或者 `docker login -u username -p password`
- 登录时速云：`sudo docker login index.tenxcloud.com`

- 清理全部未使用的资源 docker system prune -a

## 镜像
> Docker 的镜像是采用分层文件系统， Dockerfile中每个RUN命令造成的修改或新增都是新的一层layer，旧文件不变

> [dive](https://github.com/wagoodman/dive)`查看镜像内各layer文件`

- 查看所有 ： `docker images`
    - docker images -a 查看所有镜像(包括中间镜像)
- 搜索 ： `docker search 镜像名`
- 安装 ： `docker pull 镜像名`
- 删除 ： `docker rmi 镜像名`
- 查看详细： `docker inspect [-f {{".Architesture"}}]`  -f 查看JSON格式的具体节点的数据值
- 查看Layer历史：`docker history imagename` 每一层的Layer id 和 执行的操作
- 添加标签（别名）： `docker tag originname newname`
- 导出镜像文件：`docker save -o ubuntu.tar  ubuntu:14.04`
    - 导入镜像文件： `docker load --input ubuntu.tar` 或 `docker load < ubuntu.tar`
- 上传镜像： `docker push mythos/test:lastest`
- 删除所有未使用的image `docker image prune --all`

************************

## 容器
- 查看所有容器的状态：`docker stats` 能看到正在运行的容器内存 cpu io net等信息
    - `-a` 所有容器
    - `--no-stream` 不阻塞标准输出流，只输出一次信息

- 停止容器：`docker stop 容器name`
- 重启容器：`docker restart 容器name`
- 启动容器：`docker start 容器name`
    - -i 交互模式，也可以进入终端

- 删除容器：`docker rm 容器name`
    - `-f` 强行停止正在运行的容器并删除 
    - `-l` 删除容器的连接，但是保留容器
    - `-v` 删除容器挂载的数据卷
    - 删除所有容器：`docker rm ${docker -a -q}`
    - 删除所有容器和挂载的目录：`docker system prune --volumes -f`
- 容器日志(终端所有输入输出)：`docker logs 容器name或id`
- 重命名 ： `docker rename origin new`

- 导入导出 （容器快照）： **注意此方式不会保留layer历史，无法回滚**
    - 导出： `docker export -o test.tar 容器名` `docker export 容器name > test.tar`
    - 导入： `docker import [-c |--change=[]] [-m | --message=[]] file|URL - [repository]:[tag]`
    - -c | --change=[] 选项在导入的同时执行对容器就行修改的Dockerfile指令。
- 将容器导出为镜像： `docker commit container_name image:tag`

> [Attach a volume to a container while it is running](http://jpetazzo.github.io/2015/01/13/docker-mount-dynamic-volumes/)

> 修改端口映射

- 停止容器和Docker服务
- cd /var/lib/docker/containers/{id} 
- 修改 hostconfig.json 
    - `PortBindings` 节点 新增或修改
    ```json
    "PortBindings":{"3306/tcp":[{"HostIp":"","HostPort":"3360"}]}
    ```
- config.v2.json
    - `NetworkSettings.Ports` 节点下 新增或修改
    ```json
    "Ports":{"8080/tcp":[{"HostIp":"0.0.0.0","HostPort":"8888"}],"8081/tcp":[{"HostIp":"0.0.0.0","HostPort":"8881"}]}
    ```

************************

### ps
- 查看当前运行的容器：`docker ps `
    - 查看所有容器 ：`docker ps -a`
    - 查看占用 :`docker ps -s`
    - [ps formatting](https://docs.docker.com/engine/reference/commandline/ps/#formatting)

```
    .ID 	    Container ID
    .Image 	    Image ID
    .Command 	Quoted command
    .CreatedAt 	Time when the container was created.
    .RunningFor Elapsed time since the container was started.
    .Ports 	    Exposed ports.
    .Status 	Container status.
    .Size 	    Container disk size.
    .Names 	    Container names.
    .Labels 	All labels assigned to the container.
    .Label 	    Value of a specific label for this container. For example '{{.Label "com.docker.swarm.cpu"}}'
    .Mounts 	Names of the volumes mounted in this container.
    .Networks 	Names of the networks attached to this container.
```

### create
> [官方文档](https://docs.docker.com/engine/reference/commandline/create)

### run 
> [Docker run 命令的使用方法](http://www.open-open.com/lib/view/open1422492851548.html)
> 等价于 docker create 再 docker start

- `docker run -d --name conrainer-name image-name touch a.md` ，如果镜像本地没有会自动pull
    - `--name` 配置容器名字
    - `-d` 后台启动程序
    - `-i` 交互模式运行容器(标准输入和标准输出) `docker run  -it ubuntu /bin/bash`
    - `-t` 容器启动后进入其命令行
    - `-v` 将本地文件夹建立映射到容器内 `-v 本机:容器`
    - `-p` 端口映射左本机右容器：`-p 44:22`, 主机容器端口相同：`-p 22`
        - 将所有EXPOSE的端口映射到宿主机上的随机端口`-P`
        - 绑定udp端口 `-p 44:22/udp`
    - `--env name="tanky"` 设置环境变量
    - `--cpu-shares` 设置CPU的相对权重，只在link之间容器的权重比例
    - `--cpuset-cpus` 限制只能运行在某标号的CPU上
    - `--user` -u 限制用户
    - `--cap-drop` 去除能力
    - `--link` 链接其他容器
    - `--rm` 容器运行结束退出就自动删除该容器 注意和`-d`不能共存
    - `--restart=always` 设置该容器随dokcer 服务自启动
    - `--hostname hostname` 指定容器的 hostname
    - `--init` 能增加 docker-init 进程作为1号进程 entrypoint 或 cmd 中的命令成为docker-init 子进程

`-e TZ="Asia/Shanghai" -v /etc/localtime:/etc/localtime:ro`

#### 资源限制
> [Docker CPU 内存 资源限制](https://www.cnblogs.com/zhuochong/p/9728383.html)

> **`内存限制`**
- 限制最大内存100M `--memory 100M` 或者 `-m 100M`
- 配置交换内存不受限制 `--memory-swap -1`
    - 不配置该项 或者 该项小于 --memory 则都是采用默认值, --memory 的两倍

> [参考: Docker 资源限制之内存](https://blog.opskumu.com/docker-memory-limit.html)

### exec
- 登录容器：
    - `docker exec -it 容器name或id bash `
    - `docker attach 容器id` 这个命令虽然简单，但是退出会话就自动关闭了容器
- 这些选项不加就是默认值，加上短参数形式就是设为另一个值 如 -t
    - `-i `，`--interactive=ture|false` 打开标准输入接受用户输入命令
    - `--privileged=true|false` 是否给以最高权限
    - `-t`，`--tty=true|false` 是否分配伪终端
    - `-u`，`--user=""` 执行命令的用户或ID

- 使用 nsenter 连接到容器:
    - PID=${docker-pid 容器id}
    - nsenter --target $PID --mount --uts --ipc --net --pid

### port
> 查看容器的端口映射情况， 输出是左容器右本机， 和使用相反

************************

## 端口映射
- 当不指定对应的参数容器默认不开放任何端口给外部，可以使用 `-P` 或 `-p` 参数来开放
    - -P 随机映射一个 49000-49900 的端口到容器开放的端口
    - -p  `IP:HostPort:ContainerPort | IP::ContainerPort | HostPort:ContainerPort`
        - 映射到指定IP的指定端口`IP:HostPort:ContainerPort` 
        - 映射到指定IP的任意端口`IP::ContainerPort`
        - 映射到所有接口的地址的指定端口`HostPort:ContainerPort`
    - 还可以使用 udp来标记为udp类型 `docker run -d -p 127.0.0.1::5000/udp ubuntu apt update`
- 查看端口
    - 查看容器内5000对应的外端口 `docker port ubuntu17 5000`
    - 查看容器的具体信息 `docker inspect 容器id` 

*********************

# 数据存储
## 文件系统
- AUFS (AnotherUnionFS)  `Ubuntu/Debian默认`
- Device Mapper：`CentOS/RedHat默认`

## 数据卷
> [Docker 中管理数据](http://www.open-open.com/lib/view/open1403571027233.html)
> [参考: 给一个正在运行的Docker容器动态添加Volume](http://www.open-open.com/lib/view/open1421996521062.html)

- 数据卷是一个可供容器使用的特殊目录，它将宿主机操作系统目录映射进容器 类似于 mount操作
    - 数据卷可以在容器之间共享重用
    - 数据卷内数据的修改会立马生效，无论是容器内操作还是本地操作
    - 对数据卷的更新不会影响镜像，解耦了应用和数据
    - 卷会一直存在，直到没有容器使用，才可以安全的卸载

- `docker run -v dir:dir[:ro]` 一般是创建容器时使用，和-p类似可以多个，左本机右容器 默认rw权限可以指定 ro只读
    - 可以将一个文件挂载为数据卷，但是文件夹更好，文件可能会有问题出现

- 挂载宿主机时区及时间 `/etc/localtime:/etc/localtime`

## 数据卷容器
- `docker run -it -v /test --name data ubuntu ` 运行一个挂载了数据卷的容器
- 引用数据卷容器 来挂载数据卷：`docker run -it --volumes-from data --name db1 ubuntu`
- 从已经挂载了数据卷容器的容器 来挂载数据卷：`docker run -it --volumes-from db1 --name db2 ubuntu`
- 使用 `--volumes-from` 参数所挂载数据卷的容器并不需要保持在运行状态
- 如果删除了挂载的容器，数据卷并不会自动删除，而是要在删除最后一个容器时 使用 `docker rm -v` 来声明删除容器并删除关联的数据卷

`利用数据卷容器来迁移数据`
- 备份：
    - `docker run --volumes-from data -v $(pwd):/backup --name worker ubuntu tar cvf /backup/backup.tar /data`
    - 先基于Ubuntu创建一个worker容器并引用了数据卷容器data，然后将当前目录作为数据卷挂载进去，并执行tar命令，打包到数据卷容器的目录下
    - 实现了将当前目录归档到数据卷容器下
- 恢复：
    - 创建一个带有数据卷的容器（目标容器）`docker run -v /data --name reuse ubuntu /bin/bash`
    - 解压当前目录的tar文件到数据卷容器中 `docker run --volumes-from reuse -v $(pwd):/backup busybox tar xvf /backup/backup.tar`
    - 这个就是实现了将本地的归档数据放到指定的容器内，如果要从数据卷容器中恢复到别的容器就只要挂载对应的数据卷容器然后进目录直接解压即可

******************************************************

# 容器编排
## Docker-Compose
> [Official](https://docs.docker.com/compose/)

声明式环境，管理多容器， 并处理好相关资源的关系

> [Demo: 开源电商平台](https://github.com/fecshop/yii2_fecshop_docker/blob/master/docker-compose.yml)
> [Demo: 安装 Kafka](http://www.cnblogs.com/xuxinkun/p/5473952.html)

- [安装](https://docs.docker.com/compose/install/)
    - 最简单: `sudo pip install docker-compose`

### 配置文件
> 一个配置文件就表示了一组容器, 以及相关的网络,文件等配置, docker-compose 都是基于该配置文件进行基本命令操作  
> 语法上和 docker run 基本一致, 只不过以 yml 形式配置而已

> 声明一个 xxx 网络 供 service 使用
```yml
networks:
  xxx:
    external: false
    driver: bridge
    ipam:
      driver: default
      config:
      - subnet: 10.12.0.0/16
```

```yml
version: "2.1"
services:
  zookeeper:
    image: ${IMAGE_NAME:-defaultImage}
    expose:
      - "6666"
    ports:
      - "6666:6666"
    volumes:
      - /etc/localtime:/etc/localtime
    networks: # 可不配置，Docker会默认分配一个ip 172.xx 开头
      - xxx 
    command: ./bin/start.sh
    links:
        - "mysql:mysql"
    environment:
      - NAME=who
```

### 使用命令
> 必须要在 docker-compose.yml 文件目录下执行

- help
- up          # 自动完成构建镜像，`创建`服务，启动服务，并关联服务等操作, `-d` 后台执行
- down        # 停止并`删除`该服务的所有容器, 移除网络, `-v` 移除挂载的volume
- start       # 启动存在的服务 
- stop        # 停止
- restart     # 重启项目中服务
- exec        # 进入指定容器
- image       # 列出 Compose 文件中包含的镜像
- kill [SERVICE...]
- pause [SERVICE...]
- unpause [SERVICE...]
- ps          # 列出项目中所有容器

### Tips
> yml所在的目录名会作为容器名的前缀


************************

## Docker-Machine
> 创建一个docker集群环境 [官方文档安装](https://docs.docker.com/machine/install-machine)

Error with pre-create check: "VBoxManage not found. Make sure VirtualBox is installed and VBoxManage is in the path
Error with pre-create check: "This computer doesn't have VT-X/AMD-v enabled. Enabling it in the BIOS is mandatory"

## Docker-Swarm

***********************************

# 网络
> [Official Doc](https://docs.docker.com/network/) 分为 none host brige(缺省) user-defined 几种类型

> Connection reset by peer
1. 可能是 docker0 和本身网段冲突了 `docker network inspect bridge` 对比 `netstat -nr` 查看
    - [Docker: connection reset by peer](https://serverfault.com/questions/848075/docker-connection-reset-by-peer)
1. 重置网桥 [Connection reset by peer](https://blog.csdn.net/Alphr/article/details/107969190) `原因待寻找`

[规避网段冲突](https://www.jb51.net/article/208255.htm)

/etc/docker/daemon.json 顶级元素加入如下配置网段
```json
  "default-address-pools":[
     {"scope":"local","base":"172.80.0.0/16","size":24},
     {"scope":"global","base":"172.90.0.0/16","size":24}
```
## None
> docker run -it --network none  busybox

- 不联网的容器, ifconfig 可以看到只有 lo 

## Host
> docker run -it --network host busybox

- 采用宿主机的网络, 也就是说和宿主机使用同一个网络环境, hostname都是host的
    1. 特点是性能, 但是不够灵活, 要考虑和host上的端口冲突问题
    1. 直接配置host的网络: 例如配置防火墙容器

## Bridge
> 安装 Docker 的时候, 都会创建一个 docker0 的网桥 Linux bridge

- 如果没有指定 `--network` 或者使用 `--network default` 创建容器 都会默认挂载到 docker0 上
- 通过 `docker network inspect bridge` 命令可以看到子网掩码是 `172.17.0.0/16` 网关是 172.17.0.1 
    - 也就是说能容纳 2的16次幂 -2 个容器 (65534), 容器创建时会依次分配ip

> 注意: 此方式下容器之间是互通的, 通常使用的 `--link containerName:aliasName` 也只不过是在 /etc/hosts 文件中添加了容器的 dns 而已

> 特别容易出现锁，一个没有启动，其他的都启动不了 尝试？ `sudo service docker restart`

- 例如: `创建一个MySQL容器供一个Ubuntu容器使用`
1. 创建MySQL容器 `docker run --name mysql2 -e MYSQL_ROOT_PASSWORD=ad -d mysql`
2. 创建Ubuntu容器 `docker run -d --name test --link mysql2:db ubuntu`
    - link参数说明 ：`--link name:alias` 在父容器中会将该映射加入host文件，所以无需找ip，直接使用别名
3. docker会连接两个容器，而不用通过暴露端口来实现，web容器的host文件以及环境变量都会追加上mysql2的配置
4. 所以在Ubuntu容器中连接MySQL容器， `mysql -h db -u root -pad` 即可连接上mysql
    - 如需看IP就 `cat /etc/hosts` 中myslq容器别名为db值的IP地址 
    - 或者直接 `ping db` `apt install  inetutils-ping` `ifconfig就要安装net-tools`

- 例如：`创建一个Nginx和一个Springboot搭建的web服务`
    - 构建Springboot应用镜像，构建应用容器 开放8888端口
    - 新建nginx容器：`docker run --name test-nginx -d -p 80:80 -v /home/kuang/nginx/conf/:/etc/nginx/conf.d/:ro --link you:web nginx`
- 配置文件：`一样的cat /etc/hosts 查看容器的IP`， 其实最简单就是用link配置时的别名即可，因为Docker已经帮我们配置好了host。。。
```
    upstream backend {
        server 172.17.0.4:8888;
    }

    server {
        listen 80;
        server_name backend;

        location / {
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $http_host;
            proxy_set_header X-Nginx-Proxt true;

            proxy_pass http://backend;
            proxy_redirect off;
        }
    }
```

> [weave](https://www.weave.works/) `能解决跨宿主机的容器互联问题`

## User-defined 
> Docker 提供三种 网络驱动 bridge overlay macvlan, 后两者可用于跨主机的容器通信

> 容器分配独立ip

1. 宿主机新建网络 `docker network create --subnet=172.13.0.0/24 test-standby`
1. 宿主机新建容器并分配ip `docker run -it --net test-standby --ip 172.13.0.8 -p 6379 --name redis-stand redis:5.0.9-alpine`
1. 宿主机 配置为虚拟路由器 完成转发
    - `sysctl -w net.ipv4.ip_forward=1`
    - ip route 查看路由表，并 ping 172.13.0.8 查看路由表是否正确
1. 其他主机上加上这个路由，就可以访问 容器了  
    - Windows: `route add 172.13.0.0 mask 255.255.255.0 192.168.7.110`
    - Linux: `ip route add 172.13.0.0/24 via 192.168.7.110`

## 跨主机容器通信

### overlay
> [参考: DOCKER的内置OVERLAY网络](http://dockone.io/article/2717)

***********************
# Dockerfile
>[Dockerfile文件学习](/Linux/Container/DockerFiles.md)
