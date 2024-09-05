---
title: Go学习概览
date: 2020-03-22 12:40:12
tags: 
categories:
---

💠

- 1. [Golang](#golang)
    - 1.1. [社区](#社区)
    - 1.2. [教程](#教程)
    - 1.3. [书籍](#书籍)
    - 1.4. [实践项目](#实践项目)
- 2. [安装](#安装)
    - 2.1. [Linux 下安装](#linux-下安装)
        - 2.1.1. [Hello World](#hello-world)
    - 2.2. [Docker](#docker)
- 3. [环境变量解释](#环境变量解释)
- 4. [开发环境搭建 基于 VSCode](#开发环境搭建-基于-vscode)
- 5. [生态](#生态)

💠 2024-03-20 17:27:12
****************************************

# Golang

> [go dev](https://learn.go.dev/) | [awesome-go](https://github.com/avelino/awesome-go) | [awesome-go-cn](https://github.com/yinggaozhen/awesome-go-cn)

- [学习Go的知乎话题](https://www.zhihu.com/question/23486344)
- [Java 20年：转角遇到Go](http://www.infoq.com/cn/news/2015/05/java20-from-language-to-platform)

> [Golang vs Rust vs Dlang 哪个更有前途](https://www.zhihu.com/question/27226962) `大致就是go偏向Java Python, Rust 偏向 C++ 的领域`
> [从 0 到 1 学习 Go 语言 ](https://mp.weixin.qq.com/s?__biz=MjM5NzM0MjcyMQ==&mid=2650087380&idx=1&sn=56c77443ae171e1091e146704798647a)

- [go-gtk alternatives](https://go.libhunt.com/go-gtk-alternatives) `gui框架对比`


> 负面

- [Go1.0的吐槽](http://blog.csdn.net/liigo/article/details/23699459)
- [参考: 我为什么放弃Go语言](https://blog.csdn.net/liigo/article/details/23699459)
- [对 Go 语言的综合评价](http://www.yinwang.org/blog-cn/2014/04/18/golang) `设计角度：泛型，接口和排序的问题！！`

工程角度： 包管理，错误处理

## 社区

- [GoCN Forum](https://gocn.vip/)
- [Go语言中文网](https://studygolang.com)

## 教程

- [Go Programming &amp; Concurrency in Practice](https://github.com/hyper0x/goc2p)
- [golang教程](http://c.biancheng.net/golang/)
- [build web application with golang](https://www.gitbook.com/book/astaxie/build-web-application-with-golang)
- [Go 语言学习资料与社区索引](https://github.com/Unknwon/go-study-index)
- [Go语言资料收集](https://github.com/wonderfo/wonderfogo/wiki)
- [go](http://www.runoob.com/go/go-tutorial.html)
- [在线编译执行 学习go](http://www.vaikan.com/go/a-tour-of-go/#1) `在线编辑运行`
- [go101](https://github.com/go101/go101)
- [build-web-application-with-golang](https://github.com/astaxie/build-web-application-with-golang)
- [golang-design-pattern](https://github.com/senghoo/golang-design-pattern)

## 书籍

> [Go相关书籍的知乎话题](https://www.zhihu.com/question/30461290)
> [Go语言高级编程(Advanced Go Programming)](https://chai2010.cn/advanced-go-programming-book/index.html)

- [The Go Programming Language](http://www.gopl.io/)
- [Go 语言设计与实现](https://draveness.me/golang/docs)
- [Go 语言原本](https://golang.design/under-the-hood/)

## 实践项目
- [PolarDB-ClusterManager](https://github.com/ApsaraDB/PolarDB-ClusterManager)
- Docker
- Kubernetes
- [Vitess](https://github.com/vitessio/vitess)`horizontal scaling of MySQL`

************************

# 安装

## Linux 下安装

> [Official Download](https://golang.google.cn/dl/) | [Official Doc](https://golang.google.cn/doc/install)

1. `sudo tar -C /usr/local -xzf go1.10.3.linux-amd64.tar.gz` 安装和升级都是如此
   - 注意: 升级前必须 `rm -rf /usr/local/go` 以免造成文件的混乱
2. `*shrc` 或者 `/etc/profile` 中添加
   ```sh
       export GOROOT=/usr/local/go
       export GOPATH=$HOME/Code/go # workspace
       export GOBIN=$GOPATH/bin # 'go install' command install dir
       export PATH=$PATH:$GOBIN:$GOPATH:$GOROOT/bin
   ```
3. **查看版本** `go version`正常输出go的版本则是配置成功

### Hello World

1. 在 `$HOME/Code/go` 下 新建 test.go
   ```go
       package main
       import "fmt"
       func main() {
           fmt.Println("hello, world")
       }
   ```
2. go run test.go 或者 go build 然后执行可执行文件

## Docker

> [Docker image](https://hub.docker.com/_/golang/)
> [go 的 Docker镜像的讨论](https://gocn.vip/question/153)

1. 部署运行的时候, 如果不需要调用外部Linux命令 就直接使用空镜像 `from scratch` 但是缺点是排查问题时无工具可用
2. 需要外部命令则 `from alpine` 更精简一点 更好是使用 `frolvlad/alpine-glibc`



# 环境变量解释

> [
>     关于GOROOT、GOPATH、GOBIN、project目录](https://blog.csdn.net/Alsmile/article/details/48290223)
> [GOPATH 深度解析 ](https://studygolang.com/articles/3493)

- Go 开发环境依赖于一些 `操作系统环境变量`，最好在安装 Go 之间就已经设置好他们。如果是 Windows系统 Go 将被默认安装在目录 c:/go 下。这里列举几个最为重要的环境变量：
  - `$GOROOT` 表示 Go 在你的电脑上的安装位置，它的值一般都是 $HOME/go，当然，你也可以安装在别的地方。
  - `$GOARCH` 表示目标机器的处理器架构，它的值可以是 386、amd64 或 arm。
  - `$GOOS` 表示目标机器的操作系统，它的值可以是 darwin、freebsd、linux 或 windows。
  - `$GOBIN` 表示编译器和链接器的安装位置，默认是 `$GOROOT/bin`，如果你使用的是 Go 1.0.3 及以后的版本，一般情况下你可以将它的值设置为空，Go 将会使用前面提到的默认值。
    - 为了区分本地机器和目标机器，你可以使用 `$GOHOSTOS` 和 `$GOHOSTARCH` 设置目标机器的参数，这两个变量只有在进行交叉编译的时候才会用到，
    - 如果你不进行显示设置，他们的值会和本地机器（`$GOOS` 和 `$GOARCH`）一样。
  - `$GOPATH` 默认采用和 `$GOROOT` 一样的值，但从 Go 1.1 版本开始，你必须修改为其它路径。它可以包含多个包含 Go 语言源码文件、包文件和可执行文件的路径，
    - 而这些路径下又必须分别包含三个规定的目录：src、pkg 和 bin，这三个目录分别用于存放源码文件、包文件和可执行文件。
  - `$GOARM` 专门针对基于 arm 架构的处理器，它的值可以是 5 或 6，默认为 6。
  - `$GOMAXPROCS` 用于设置应用程序可使用的处理器个数与核数，详见第 14.1.3 节。
  - `$GOPROXY` 设置 mod 的代理. 例如： **GOPROXY=https://mirrors.aliyun.com/goproxy/**



# 开发环境搭建 基于 VSCode

> [Github:Golang](https://github.com/golang) | [基础学习项目](https://github.com/Kuangcp/GoBase)

入门时使用 VSCode 是比较方便的, VSCode 会推荐我们安装如下工具

1. tools _工具集_
   1. guru `golang.org/x/tools/cmd/guru`
   2. gorename `golang.org/x/tools/cmd/gorename`
2. lint `golang.org/x/lint`
   1. golint `golang.org/x/lint/golint`
3. go-outline `github.com/ramya-rao-a/go-outline`
4. go-symbols `github.com/acroca/go-symbols`
5. goreturns `github.com/sqs/goreturns`
6. dep `github.com/golang/dep`

由于 golang.org 用的是Google的服务器, 所以..., 这几个工具不能直接安装：guru gorename imports(goreturns要用到) lint golint
但是本质上都是获取源码进行安装, 所以也可以从github获取并安装

**汇总一下命令**

```sh
    # 必须在 GOPATH 下执行
    cd $GOPATH
    mkdir -p src/golang.org/x/tools
    git clone --depth 1 https://github.com/golang/tools src/golang.org/x/tools

    mkdir -p src/golang.org/x/lint
    git clone --depth 1 https://github.com/golang/lint  src/golang.org/x/lint

    go get golang.org/x/tools/cmd/guru 
    go get golang.org/x/tools/cmd/gorename 
    go get golang.org/x/tools/cmd/goimports

    go get golang.org/x/lint
    go get golang.org/x/lint/golint
```

```sh
    # 可在任意目录执行
    go get github.com/ramya-rao-a/go-outline
    go get github.com/acroca/go-symbols
  
    ## 仅为了提速
    mkdir -p src/github.com/golang/dep
    git clone --depth 1 https://github.com/golang/dep src/github.com/golang/dep
    go get github.com/golang/dep

    go get github.com/sqs/goreturns
    go get github.com/rogpeppe/godef
    go get github.com/uudashr/gopkgs/cmd/gopkgs
    go get github.com/go-delve/delve/cmd/dlv
    go get github.com/mdempsky/gocode
```

************************

# 生态

[cron](https://github.com/robfig/cron)
gorm xorm
