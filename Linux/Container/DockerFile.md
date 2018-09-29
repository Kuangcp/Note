`目录 start`
 
1. [Dockerfile](#dockerfile)
    1. [使用入门案例](#使用入门案例)
    1. [Tips](#tips)
    1. [Dockerfile命令](#dockerfile命令)
        1. [FROM](#from)
        1. [MAINTAINER](#maintainer)
        1. [RUN](#run)
        1. [CMD](#cmd)
        1. [ENTRYPOINT](#entrypoint)
        1. [USER](#user)
        1. [EXPOSE](#expose)
        1. [ENV](#env)
        1. [LABEL](#label)
        1. [ARG](#arg)
        1. [COPY](#copy)
        1. [ADD](#add)
        1. [VOLUME](#volume)
        1. [WORKDIR](#workdir)
        1. [STOPSIGNAL](#stopsignal)
        1. [ONBUILD](#onbuild)
    1. [Dockerfile案例](#dockerfile案例)
        1. [打包最新版git](#打包最新版git)
        1. [Dockerfile中新建用户](#dockerfile中新建用户)

`目录 end` |_2018-09-28_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
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

## Tips
> [Reducing Your Docker Image Size](https://blog.codeship.com/reduce-docker-image-size/)
*******************************************************************
## Dockerfile命令
- Dockerfile是一个`镜像`的表示，可以通过Dockerfile来描述构建镜像的步骤，且可以自动构建一个容器
- 所有的 Dockerfile 命令格式都是: `INSTRUCTION arguments` 
- 最好在运行这个配置文件的时候新建一个空目录目录下放dockerfile，不要使用根目录，不然全部的东西都传到守护进程里去了
    - 因为生成过程的第一件事是将整个上下文 (递归) 发送到守护进程。
- 同样的可以使用`.dockerignore`文件来忽略不要上传的文件

_docker build_
- 如果文件名是默认的`Dockerfile` 就使用 `.` 
    - 否则就是 `docker build -t image:tag- < 文件名` 或者使用-f参数:
    - `-f` 指向任意位置的文件进行配置 `docker build -f /path/to/a/Dockerfile .`
- `-t`如果构建成功 可以指定保存新镜像的image和tag (多个的话就多个 -t就行了，例如 `docker build -t shykes/myapp:1.0.2 -t shykes/myapp:latest .`)

### FROM
> 基于某镜像构建,这是整个文件的第一条指令，一定是基于某镜像构建的，如果是空镜像就使用特殊的 `FROM scratch`  
> 允许多个FROM命令，其后的命令就是基于该FROM的镜像构建的，但是一个dockerfile只能得到一个有名字的镜像(最后一个FROM构建的镜像)，之前的FROM就是none:none

- `FROM image`
- `FROM image:tag`
- `FROM image@digest`

- 如果FROM使用中，找不到对应的版本的镜像，整个Dockerfile就会报错返回

> 在 17.05 版本开始, 支持分步构建, Multiple stage
>1. 例如基于一个编译环境镜像, 编译得到结果文件, 然后基于运行环境, 将结果文件复制过来, 构建成新的镜像
>1. 构建出来的镜像是不包含编译环境的

### MAINTAINER
- 留开发者名字 例如 `MAINTAINER kuangcp myth.kuang@gmail.com`
- 可以放多个信息，但是建议只有开发者信息，其他的放在Labels里 

### RUN
> 每条RUN命令在当前镜像的基础上执行指定命令，并提交为新的镜像层，所以尽量将所有命令放在一个RUN里

- `RUN command` 
    - 这种写法中的command是shell `/bin/sh -C`负责执行，所以就会有限制，必须要有 `/bin/sh`

- `RUN ["executable", "param1", "param2" ... ]`  一定要双引号（`JSON字符串的格式`来解析的）
    - 这种写法适用任意一个二进制程序 
        - 例如bash执行 `RUN ["/bin/bash", "-C", "echo hello"]`
        - 例如 ui-docker 就是基于空镜像的直接二进制文件执行的。
    - 环境变量的问题： `RUN ["echo","$HOME"]` 是不会正常输出的，因为此时不会加载环境变量中的数据
        - `RUN ["sh", "-c", "echo", "$HOME"]` 就可以正常输出了
- 当RUN命令执行完毕后，就会生成一个新的文件层。这个文件层会保存在缓存中作为下一个指令的基础镜像存在，如果不需要缓存就加上 `--no-cache`
    - 所以就尽量是将所有的命令 放在一个RUN命令里减少镜像层数。


### CMD
> 指定 容器启动时默认执行的命令

- `三种格式`
    - `CMD ["executable","param1","param2"]` (like an exec, preferred form) `推荐`
    - `CMD ["param1","param2"]` (as default parameters to ENTRYPOINT) 作为默认参数提供给ENTRYPOINT
    - `CMD command param1 param2` (as a shell) 作为shell命令 依靠`bin/sh -C`执行
- 一个Dockerfile里只能有一个CMD，如果有多个，只有最后一个生效。
- 如果用户在`docker run` 中带了运行的命令，就会覆盖CMD命令
- 与RUN命令一样如果要环境变量就要使用 `sh -C`

### ENTRYPOINT
- `容器入口点` 命令设置在容器启动时执行命令 一般用来做初始化容器，或者运行持久软件
- `ENTRYPOINT echo "Welcome!"` 那么每次启动容器都有这个输出
- `ENTRYPOINT cmd param1 param2 ...`
- `ENTRYPOINT ["cmd", "param1", "param2"...]`

### USER
- 切换用户，其后的命令都将以该用户执行
    - 如果在这个镜像上的容器需要安装软件就会需要提权，就要至少创建额外的两个层，层限制是42,
        - 所以，所有其他的操作在root用户执行 减少层数
    - 更好的方法是在基础镜像中创建用户和用户组，然后在完成构建时再设置默认的用户
- 指定 mysql 的运行用户 `ENTRYPOINT ["mysql", "-u", "daemon"]`
- 更好的方式是：
```
    ENTRYPOINT ["memcached"]
    USER daemon
```

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

-  `ARG <name> [=<default value>]`
- 使用`docker build --build=-arg<name>=<value>` 来传入值

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


### ONBUILD
- 注入下游镜像。如果生成的镜像是作为另一个镜像的基础镜像，则该指令定义了需要被执行的那些指令

******************************************
## Dockerfile案例
- [alpine构建ssh](/Linux/Docker/alpine/Dockerfile)
- [docker-wordpress-nginx](https://github.com/eugeneware/docker-wordpress-nginx)
- [rails-meets-docker](https://github.com/gemnasium/rails-meets-docker)

- [官方文档 dockerfile](https://www.docker.io/learn/dockerfile/)
- [官方文档 builder](http://docs.docker.io/reference/builder/)

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
