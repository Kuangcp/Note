---
title: DockerFile
date: 2018-12-15 11:27:03
tags: 
    - 基础
categories: 
    - Docker
---

💠

- 1. [Dockerfile](#dockerfile)
    - 1.1. [使用入门案例](#使用入门案例)
    - 1.2. [docker build](#docker-build)
        - 1.2.1. [docker buildx](#docker-buildx)
    - 1.3. [Dockerfile命令](#dockerfile命令)
        - 1.3.1. [FROM](#from)
        - 1.3.2. [MAINTAINER](#maintainer)
        - 1.3.3. [RUN](#run)
            - 1.3.3.1. [修改容器时区设置](#修改容器时区设置)
            - 1.3.3.2. [修改 hosts](#修改-hosts)
            - 1.3.3.3. [软件安装后缓存文件的清理](#软件安装后缓存文件的清理)
        - 1.3.4. [CMD](#cmd)
        - 1.3.5. [ENTRYPOINT](#entrypoint)
        - 1.3.6. [USER](#user)
        - 1.3.7. [EXPOSE](#expose)
        - 1.3.8. [ENV](#env)
        - 1.3.9. [LABEL](#label)
        - 1.3.10. [ARG](#arg)
        - 1.3.11. [COPY](#copy)
        - 1.3.12. [ADD](#add)
        - 1.3.13. [VOLUME](#volume)
        - 1.3.14. [WORKDIR](#workdir)
        - 1.3.15. [STOPSIGNAL](#stopsignal)
        - 1.3.16. [HEALTHCHECK](#healthcheck)
        - 1.3.17. [ONBUILD](#onbuild)
        - 1.3.18. [中间镜像](#中间镜像)
- 2. [Practice](#practice)
    - 2.1. [dockerignore文件的使用](#dockerignore文件的使用)
    - 2.2. [Exercises](#exercises)
        - 2.2.1. [打包最新版git](#打包最新版git)
        - 2.2.2. [Dockerfile中新建用户](#dockerfile中新建用户)

💠 2026-09-10 17:32:27
****************************************
# Dockerfile

## 使用入门案例
- `mkdir test && cd test && touch Dockerfile ` 输入如下文本
```Dockerfile
    #随意写的
    FROM alpine
    MAINTAINER Mythos
    ENV DIRPATH /path
    WORKDIR $DIRPATH/$DIRNAME
    RUN pwd
```
- `docker build .` 如果成功则会得到一个没有名字的镜像 `none:none`
    - `docker build -t image:tag .` 给镜像指定名字, 注意标签不设置就是默认的latest
- 创建镜像成功后 `docker run --name ContainerName -d image:tag` 新建容器来运行镜像

************************
## docker build 

- 如果文件名是默认的 `Dockerfile` 就使用 `.`。 自定义文件名可以：
    - `docker build -t image:tag- < 文件名`
    - `-f` 指向任意位置的文件进行配置 `docker build -f /path/to/a/Dockerfile .`
- `-t`如果构建成功 可以指定保存新镜像的image和tag (多个的话就多个 -t就行了，例如 `docker build -t shykes/myapp:1.0.2 -t shykes/myapp:latest .`)

> [moby/buildkit: concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit](https://github.com/moby/buildkit)  

### docker buildx
- [docker buildx](https://github.com/docker/buildx)

************************

## Dockerfile命令
- Dockerfile是一个`镜像`的表示，可以通过Dockerfile来描述构建镜像的步骤，且可以自动构建一个容器
- 所有的 Dockerfile 命令格式都是: `INSTRUCTION arguments` 

> 注意
- 在运行配置文件时，dockerfile所在目录应尽量减少无关文件，因为当前dockerfile所在目录递归传入Docker构建进程中
    - 或者使用`.dockerignore`文件来忽略不要上传的文件
- 执行命令时，不常变的命令应放在前面，利用Docker的 build cache，因为每个命令会生成一层文件layer，如果layer一致就会复用
    - 例如 npm 对应的 package.json 配置，先COPY文件 然后 npm install, 如果 package.json 没有变动 npm install 也会复用旧 layer

### FROM
> 基于某镜像构建,这是整个文件的第一条指令，一定是基于某镜像构建的，如果是空镜像就使用特殊的 `FROM scratch`  
> 允许多个FROM命令，其后的命令就是基于该FROM的镜像构建的，但是一个dockerfile只能得到一个有名字的镜像(最后一个FROM构建的镜像)，之前的FROM就是none:none

- `FROM image`
- `FROM image:tag`
- `FROM image@digest`

- 如果FROM使用中，找不到对应的版本的镜像，整个Dockerfile就会报错退出

************************

> 在 17.05 版本开始, 支持分步构建, Multiple stage

例如基于一个编译环境镜像, 编译得到结果文件, 然后基于运行环境, 将结果文件复制过来, 构建成新的镜像, 最终镜像将不包含编译环境
```dockerfile
FROM maven:3.5.0-jdk-8-alpine AS builder
RUN mvn clean package

From openjdk:8-jre-alpine
COPY --from=builder target/demo.jar demo.jar
CMD ["java", "-jar", "demo.jar"]
```

### MAINTAINER
- 留开发者名字 例如 `MAINTAINER kuangcp myth.kuang@gmail.com`
- 可以放多个信息，但是建议只有开发者信息，其他的放在Labels里 

### RUN
> 每条RUN命令在当前镜像的基础上执行指定命令，并提交为新的镜像层，所以尽量将所有命令放在一个RUN里, 便于后续构建时复用缓存和减少层数

- `RUN command` 
    - 这种写法中的command是shell `/bin/sh -C`负责执行，所以就会有限制，必须要有 `/bin/sh`

- `RUN ["executable", "param1", "param2" ... ]`  一定要双引号（`JSON字符串的格式`来解析的）
    - 这种写法适用任意一个二进制程序 
        - 例如bash执行 `RUN ["/bin/bash", "-C", "echo hello"]`
        - 例如 ui-docker 就是基于空镜像的直接二进制文件执行的。
    - 环境变量的问题： `RUN ["echo","$HOME"]` 是不会正常输出的，因为此时不会加载环境变量中的数据
        - `RUN ["sh", "-c", "echo", "$HOME"]` 就可以正常输出了
- 当RUN命令执行完毕后，就会生成一个新的文件层。这个文件层会保存在缓存中作为下一个指令的基础镜像存在，如果不需要缓存就加上 `--no-cache`

> 注意 apt update 会被Docker缓存,因为缓存的判定是依据命令字符，而不是文件的内容，会有这种[奇怪的问题](https://github.com/moby/moby/issues/3313)
- 但是遇到了一种奇怪的场景，有时候会使用到缓存，但是有时候会重新执行update命令和安装软件的命令就会很费时甚至超时失败。

#### 修改容器时区设置
> [参考: Docker修改默认时区](https://www.jianshu.com/p/004ddf941aac) 

```sh
    # Alpine 
    RUN apk --no-cache add tzdata  && \
        ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
        echo "Asia/Shanghai" > /etc/timezone

    # Ubuntu 可能需要安装tzdata
    RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
        echo "Asia/Shanghai" > /etc/timezone && \
        dpkg-reconfigure -f noninteractive tzdata

    # Centos
    RUN echo "Asia/shanghai" > /etc/timezone;
```
> 对于 alpine 以及 Ubuntu ln -s 建立到时间文件的软链接就已经够了, 但是确保没问题就最好还是修改下 时区文件

#### 修改 hosts
由于Docker动态分配pod的虚拟ip，所以hosts会动态生成，单纯使用RUN命令在Dockerfile中修改hosts文件是**不生效的**。  
正确方式为:
- Docker  `docker run –add-host host:ip`
- K8S 
    ```yml
        hostAliases:
        - hostnames:
            - api.xxxxx.com
            ip: 192.168.1.5
        - hostnames:
            - user.xxxx.cn
            ip: 192.168.1.9
    ```

#### 软件安装后缓存文件的清理
```sh
    # Ubuntu 
    apt update && apt install tzdata && apt autoclean && rm -rf /var/lib/apt/lists/

    # Alpine 
    apk update && apk add bash && 
```


**************

> 关于Java的时区问题
1. `docker run ... -e JAVA_OPTS=-Duser.timezone=Asia/Shanghai `
1. java读取的是 /etc/timezone 文件 所以修改为 Asia/Shanghai 就可以了

### CMD
> 指定 容器启动时默认执行的命令

- `三种格式`
    - `CMD ["executable","param1","param2"]` (like an exec, preferred form) `推荐`
    - `CMD ["param1","param2"]` (as default parameters to ENTRYPOINT) 作为默认参数提供给ENTRYPOINT
    - `CMD command param1 param2` (as a shell) 作为shell命令 依靠`bin/sh -C`执行

- 一个Dockerfile里只能有一个CMD，如果有多个，只有最后一个生效。
- 如果用户在`docker run` 中带了运行的命令，就会覆盖CMD命令
- 与RUN命令一样如果要环境变量就要使用 `sh -C` : `CMD ["sh", "-C", "echo $HOME"]`

### ENTRYPOINT
> `容器入口点` 命令设置在容器启动时执行命令 一般用来做初始化容器，或者运行持久软件  

一个 Dockerfile 内可以有 多个 ENTRYPOINT， 但是最后的才会生效

- `ENTRYPOINT java param1 param2 ...` 注意这种写法会使用系统默认shell（ash,bash,dash,sh 等等）去解释执行这个命令。sh是1号进程，java是sh的子进程
- `ENTRYPOINT ["java", "param1", "param2"...]` 非最佳实践，java是1号进程

- [Java 应用最佳实践](/Java/Basic/JavaDeploy.md#容器中jvm信号及参数接收问题)

### USER
USER 指令会设置后续所有 RUN、CMD、ENTRYPOINT（以及运行时容器主进程）的默认用户（和可选的组）。如果没有指定，默认就是 root（UID 0）

- 切换用户，其后的命令都将以该用户执行
    - 如果在这个镜像上的容器需要安装软件就会需要提权，就要至少创建额外的两个层，(层限制是42, 所有其他的操作在root用户执行 减少层数, 但是overlay2之后不限制了)
    - 更好的方法是在基础镜像中创建用户和用户组，然后在完成构建时再设置默认的用户

最佳实践

```dockerfile
FROM some-base
# 创建用户和组（建议固定 UID/GID，避免不确定性）
# 统一约定
ARG APP_UID=1001
ARG APP_GID=1001
ARG SHARED_GID=2000        # 公共共享组（可选，用于读写挂载卷）
RUN groupadd -r -g ${APP_GID} appgroup && \
    useradd --no-log-init -r -u ${APP_UID} -g appgroup -G ${SHARED_GID}  -m -s /usr/sbin/nologin appuser

# 所有安装、复制、权限设置都用 root 做
RUN apt-get update && apt-get install -y ... && rm -rf /var/lib/apt/lists/*
COPY --chown=appuser:appgroup . /app
# 或单独 chown

# 最后才切换（推荐放在靠后位置）
USER ${APP_UID}:${APP_GID} 
WORKDIR /app
ENTRYPOINT ["your-app"]
```

>- 永远不要让最终运行进程是 root（除非绝对必要）。这是安全红线之一，K8S可以 加约束 runAsNonRoot: true 避免团队不一致
    - 容器逃逸，提权到宿主机root
>- 所有需要 root 的操作（安装包、创建用户、改权限）在 USER 之前完成。
>- 尽量避免在 Dockerfile 里来回切换 USER（增加复杂度和层）。
>- 用数字 UID:GID 比用户名更稳妥。
>- 配合 multi-stage build：构建阶段可以随便用 root，最终运行阶段只复制必要文件并切到非 root。
>- 对于需要写挂载卷的场景，注意权限匹配（可在 entrypoint 里临时处理，或用 fixed UID）。
    - 最佳实践是声明存储卷时限定 公共 GID 
>- 运行时还可用 docker run -u 或 Kubernetes securityContext.runAsNonRoot / runAsUser 强制覆盖。


### EXPOSE
- 对外开放端口 例如 EXPOSE 22
- 但是还不能被外部访问到，只能被容器内或主机的其他容器访问，加上-p 开放端口才可以

### ENV
> 设置环境变量 

- `ENV <key> <value>`
    - 这种方式会将第一个字符串看作key，后面所有的字符串看成value
    - 所以只能设置一个变量 `ENV name kuang cheng ping`
- `ENV <key>=<value>`
    - 可以设置多个，但是空格要转义 `ENV name=myth\ kuang`
    - 例如：设置时区 `ENV TZ=Asia/Shanghai`

- ENV命令之后的RUN命令都可以使用这里配置的环境变量
- 如果`docker run --env <key>=<value>`则会覆盖dockerfile中同名key的值
    - `docker run -e` 重设环境变量
- 一个ENV命令一个新层，所以也是尽量使用一个ENV命令

- `ENV TIME_ZONE Asiz/Shanghai`

### LABEL
> 用来定义键值对， 相当于是一个内置的配置文件

- `LABEL key=value`
    - 两种方式 前者更好，可以使用空格`LABEL version="java 1.8"` `LABEL test=other`
- 同样的 一个LABEL命令就会构建一个新的层，所以建议一个LABEL
- 旧镜像中LABEL设置的key会被新镜像中的相同的key的值进行覆盖

### ARG
> 用来指定一些镜像中使用的参数，例如版本信息 

- 定义 `ARG <name> [=<default value>]`
- 使用 `$name`
- 传入 `docker build --build-arg<name>=<value>`

ARG 指令有生效范围，如果在 FROM 指令之前指定，那么只能用于 声明到 FROM 指令中间的命令上。所以多阶段构建使用FROM分离变量

### COPY
> 当复制本地目录时，推荐使用copy

> [参考博客](http://www.simapple.com/364.html)
- `copy <src> <dest>`
    - src是当前Dockerfile的相对路径的文件或目录,也可以是远程URL
    - dest 是目标容器中的绝对路径。
- 例如: `copy ["./log", "${APPROOT}"]`

### ADD
- 相当于copy命令
- `ADD <src> <dest>` 
    - src 和 dest 和上面COPY命令使用是一样的

### VOLUME
- `VOLUME ["<mountpoint>"]` `VOLUME ["/data"]` 创建挂载点 用于共享目录

### WORKDIR
- `WORKDIR /path/to/workdir`
- 配置RUN, CMD, ENTRYPOINT 命令设置当前工作路径，如果目录不存在就新建
- 可以设置多次，如果是相对路径，则相对前一个 WORKDIR 命令
    - 例如：`WORKDIR /a WORKDIR b WORKDIR c RUN pwd` 其实是在 /a/b/c 下执行 pwd

### STOPSIGNAL

### HEALTHCHECK
健康检查

### ONBUILD
- 注入下游镜像。如果生成的镜像是作为另一个镜像的基础镜像，则该指令定义了需要被执行的那些指令


### 中间镜像

```dockerfile
    FROM imageA AS builder
    RUN ...

    FROM imageB AS final
    RUN ...

    # 可以引用builder镜像中的文件
    COPY --from=builder /path/to/a /app
    ENTRYPOINT ["/app"]
```
******************************************

# Practice
> [docker: best-practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

- [官方文档 dockerfile](https://www.docker.io/learn/dockerfile/)
- [官方文档 builder](http://docs.docker.io/reference/builder/)

> [Reducing Your Docker Image Size](https://blog.codeship.com/reduce-docker-image-size/)

## dockerignore文件的使用
- .dockerignore文件是依据 Go 的 PathMatch 规范来的，使用和.gitignore类似

## Exercises
- [alpine构建ssh](/Linux/Docker/alpine/Dockerfile)
- [docker-wordpress-nginx](https://github.com/eugeneware/docker-wordpress-nginx)
- [rails-meets-docker](https://github.com/gemnasium/rails-meets-docker)

### 打包最新版git
- 注意其运行环境是容器内，不是宿主机，入口点的命令运行完了就退出了，不能当成宿主机上的git使用，只能说是学习一些操作
    - 所以不可能说在容器中安装软件然后在宿主机上交互运行

```Dockerfile
    FROM ubuntu
    MAINTAINER "your email"
    RUN apt-get update \
        && apt-get install -ysoftware-properties-common \
        && add-apt-repository ppa:git-core/ppa \
        && apt-get update && apt-get install -y git
    ENTRYPOINT ["git"]
```

- 构建镜像`docker build -t git:new .`
- 将镜像容器化执行命令后自动删除容器`docker run --rm git:new`

### Dockerfile中新建用户
```Dockerfile
    RUN useradd -ms /bin/bash mythos;\
        echo "mythos:jiushi" | chpasswd;
    USER mythos
    WORKDIR /home/mythos
```
**************************
> [参考: 在 Docker 上开发应用 - 编写 Dockerfile 的最佳实践](https://blog.csdn.net/kikajack/article/details/79366043) | [英文原文](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)


