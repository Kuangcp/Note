---
title: Go基础
date: 2018-12-14 09:25:49
tags: 
    - 基础
    - 函数式编程
categories: 
    - Go
---

**目录 start**
 
1. [Go](#go)
    1. [社区](#社区)
        1. [教程](#教程)
    1. [书籍](#书籍)
    1. [安装](#安装)
        1. [Docker](#docker)
    1. [环境变量解释](#环境变量解释)
    1. [基本开发环境搭建](#基本开发环境搭建)
    1. [数据类型](#数据类型)
        1. [基本类型](#基本类型)
            1. [int](#int)
            1. [int64](#int64)
        1. [Array](#array)
        1. [Slice](#slice)
        1. [Map](#map)
        1. [Set](#set)
    1. [基本语法](#基本语法)
        1. [标准输入输出](#标准输入输出)
    1. [函数](#函数)
        1. [参数](#参数)
        1. [返回值](#返回值)
    1. [接口](#接口)
    1. [文件操作](#文件操作)
    1. [Test](#test)
    1. [JSON](#json)
1. [Tips](#tips)
    1. [通过字符串调用指定函数](#通过字符串调用指定函数)

**目录 end**|_2019-05-26 21:38_|
****************************************
# Go
> [官网](https://golang.org) | [镜像官网](https://golang.google.cn/) | [Github Repo](https://github.com/golang/go) | [Go Doc](https://godoc.org/)

Go 语言被设计成一门应用于搭载 Web 服务器，存储集群或类似用途的巨型中央服务器的系统编程语言。对于高性能分布式系统领域而言，Go 语言无疑比大多数其它语言有着更高的开发效率。它提供了海量并行的支持，这对于游戏服务端的开发而言是再好不过了。

- [Go语言资料收集](https://github.com/wonderfo/wonderfogo/wiki)
- [学习Go的知乎话题](https://www.zhihu.com/question/23486344)
- [Go相关书籍的知乎话题](https://www.zhihu.com/question/30461290)
- [Go1.0的吐槽](http://blog.csdn.net/liigo/article/details/23699459)
- [Java 20年：转角遇到Go](http://www.infoq.com/cn/news/2015/05/java20-from-language-to-platform)

> [参考博客: Golang官网被墙解决办法](https://golangtc.com/t/504072ca320b5276e2000004)
> [参考博客: why is go popular in china](http://herman.asia/why-is-go-popular-in-china)
> [参考博客: 我为什么放弃Go语言](https://blog.csdn.net/liigo/article/details/23699459)
> [参考博客: 使用Go语言工作400天后的感受](https://blog.csdn.net/erlib/article/details/50998026)
> [Golang vs Rust vs Dlang 哪个更有前途](https://www.zhihu.com/question/27226962)`大致就是go偏向Java Python Rust 偏向 C++ 的领域`

- [从 0 到 1 学习 Go 语言 ](https://mp.weixin.qq.com/s?__biz=MjM5NzM0MjcyMQ==&mid=2650087380&idx=1&sn=56c77443ae171e1091e146704798647a&chksm=bedac4ba89ad4dac6dab9bd21355a13a692f3411d4242e02ce2be91534570167ee3b7afb5d82&mpshare=1&scene=1&srcid=0127jfIvpS2r7ItNbpOnjnr8#rd)

> go相关应用 
docker golang lantern kubernetes awesome-go gogs synching hugo grafana etcd hub influxdb caddy beego martini cayley nsq codis delve cobra shadowsocks-go phcolus 
**************************************

## 社区
- [GoCN Forum](https://gocn.vip/)
- [Go语言中文网](https://studygolang.com)

### 教程

- [Go Programming & Concurrency in Practice](https://github.com/hyper0x/goc2p)
- [golang教程](http://c.biancheng.net/golang/)

**************************************

## 书籍

> [Go语言高级编程(Advanced Go Programming)](https://books.studygolang.com/advanced-go-programming-book/index.html)
> [Go 语言学习资料与社区索引](https://github.com/Unknwon/go-study-index)
***********************************

## 安装
> [Official Download](https://golang.google.cn/dl/) | [Official Doc](https://golang.google.cn/doc/install) | [参考 教程](http://www.runoob.com/go/go-environment.html) [.](http://cloud.kuangcp.top/go-1.10.3.tar.gz) 

1. `sudo tar -C /usr/local -xzf go1.10.3.linux-amd64.tar.gz` 安装和升级都是如此
    - 注意: 升级前必须 `rm -rf /usr/local/go` 以免造成文件的混乱
1. `*shrc` 或者 `/etc/profile` 中添加
	```sh
        export GOROOT=/usr/local/go
        export GOPATH=$HOME/Code/go # workspace
        export GOBIN=$GOPATH/bin # 'go install' command install dir
        export PATH=$PATH:$GOBIN:$GOPATH:$GOROOT/bin
	```
1. **查看版本** `go version`正常输出go的版本则是配置成功  

************************

1. 在 `/home/kcp/code/go` 下 新建 test.go
    ```go
        package main
        import "fmt"
        func main() {
            fmt.Printf("hello, world\n")
        }
    ```
1. go run test.go 或者 go build

### Docker
> 使用Docker安装和部署

> [Docker image](https://hub.docker.com/_/golang/) `这里的镜像都是用于 从源码编译构建成可执行文件的 环境`   
> [go 的 Docker镜像的讨论](https://gocn.vip/question/153)

1. 实际运行的时候, 如果不需要调用外部Linux命令 就直接使用空镜像 `from scratch`
1. 需要外部命令则 `from alpine` 更精简一点 更好是使用 `frolvlad/alpine-glibc`

*****************************************

## 环境变量解释
> [	关于GOROOT、GOPATH、GOBIN、project目录](https://blog.csdn.net/Alsmile/article/details/48290223)
> [GOPATH 深度解析 ](https://studygolang.com/articles/3493)

- Go 开发环境依赖于一些操作系统环境变量，你最好在安装 Go 之间就已经设置好他们。如果你使用的是 Windows 的话，你完全不用进行手动设置，Go 将被默认安装在目录 c:/go 下。这里列举几个最为重要的环境变量：
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

********************************

## 基本开发环境搭建
> [Github:Golang](https://github.com/golang)

入门时使用 VSCode 是比较方便的, VSCode 会推荐我们安装如下工具
1. tools _工具集_
    1. guru `golang.org/x/tools/cmd/guru`
    1. gorename `golang.org/x/tools/cmd/gorename`
1. lint `golang.org/x/lint`
    1. golint `golang.org/x/lint/golint`
1. go-outline `github.com/ramya-rao-a/go-outline`
1. go-symbols `github.com/acroca/go-symbols`
1. goreturns `github.com/sqs/goreturns`
1. dep `github.com/golang/dep`

由于 golang.org 用的是Google的服务器, 所以..., 这几个工具不能直接安装  guru gorename imports(goreturns要用到) lint golint 
但是本质上都是获取源码而已, 所以可以从github获取

**汇总一下命令**
```sh
    cd $GOPATH
    mkdir -p src/golang.org/x/tools
    git clone --deepth 1 https://github.com/golang/tools src/golang.org/x/tools

    mkdir -p src/golang.org/x/lint
    git clone --deepth 1 https://github.com/golang/lint  src/golang.org/x/lint

    mkdir -p src/github.com/golang/dep
    git clone --deepth 1 https://github.com/golang/dep src/github.com/golang/dep

    go get golang.org/x/tools/cmd/guru 
    go get golang.org/x/tools/cmd/gorename 
    go get golang.org/x/lint
    go get golang.org/x/lint/golint
    go get github.com/ramya-rao-a/go-outline
    go get github.com/acroca/go-symbols
    go get github.com/sqs/goreturns
    go get github.com/golang/dep
```

> 可以利用码云来加速下载
1. lint https://gitee.com/gin9/golang-lint.git
1. tools https://gitee.com/gin9/golang-tools.git 

*********************************

## 数据类型
_有关类型后置_
> [螺旋形（C/C++）和顺序（Go）的声明语法](https://cxwangyi.wordpress.com/2011/03/14/%E8%9E%BA%E6%97%8B%E5%BD%A2%EF%BC%88cc%EF%BC%89%E5%92%8C%E9%A1%BA%E5%BA%8F%EF%BC%88go%EF%BC%89%E7%9A%84%E5%A3%B0%E6%98%8E%E8%AF%AD%E6%B3%95/)
> [Why do a lot of programming languages put the type *after* the variable name?](https://stackoverflow.com/questions/1712274/why-do-a-lot-of-programming-languages-put-the-type-after-the-variable-name)

### 基本类型
#### int 
#### int64

```go
    // string到int
    int,err:=strconv.Atoi(string)
    // string到int64
    int64, err := strconv.ParseInt(string, 10, 64)
    // int到string
    string:=strconv.Itoa(int)
    // int64到string
    string:=strconv.FormatInt(int64,10)
```

### Array
### Slice
### Map
### Set

******************

## 基本语法

### 标准输入输出
> [参考博客: golang中的格式化输入输出](https://blog.csdn.net/xiaoyida11/article/details/51554022)

**************************

## 函数
基本结构
```go
// 函数名 (参数 ) 返回值{函数体}
func functionName (param1 int) int {

}
```
> 函数作为参数 `functionName func(string, string)`


### 参数
### 返回值

*************************

## 接口
> [参考:接口的定义和使用](http://www.cnblogs.com/yjf512/archive/2012/06/09/2543628.html)

***************

## 文件操作

**递归读取当前目录的文件**
```go
package main
import (
    "fmt"
    "os"
    "path/filepath"
)
func main() {
    filepath.Walk("./", walkfunc)
}
func walkfunc(path string, info os.FileInfo, err error) error {
	if(!info.IsDir()){
		fmt.Println(path)
	}
    return nil
}
```

*************************************

## Test
> [Github: assert](https://godoc.org/github.com/stretchr/testify/assert)

***********************

## JSON
> `结构体必须是大写字母开头的成员才会被处理(大写字母开头才有对外权限)`

> [参考博客: Go操作JSON](https://blog.csdn.net/u011304970/article/details/70769949)
> [参考博客: go and json](https://eager.io/blog/go-and-json/)
> [参考博客: 在Go语言中使用JSON](https://blog.csdn.net/tiaotiaoyly/article/details/38942311) 

> [website: json to go struct](https://mholt.github.io/json-to-go/)

```go
	type GridConfig struct {
        ID   int   `json:"id"`
        Row  int   `json:"row"`
        Col  int   `json:"col"`
        Data []int `json:"data"`
    }

// 第一种
func (*GenerateGrid) ReadConfig() []GridConfig {
	var datas []GridConfig
	fp, _ := os.Open("grid.json")
	dec := json.NewDecoder(fp)
	for {
		err := dec.Decode(&datas)
		if err != nil {
			fmt.Println(err)
			break
		}
		//use v
		// fmt.Printf("%+v", datas)
		for _, line := range datas {
			fmt.Println(" ", line)
		}
	}

    // 第二种方式
	var datas []GridConfig
	raw, err := ioutil.ReadFile("./grid.json")
	// fmt.Println(raw)
	if err != nil {
		fmt.Println(err.Error())
		os.Exit(1)
	}
	err = json.Unmarshal(raw, &datas)
	if err != nil {
		fmt.Println("error:", err)

	}
	for _, line := range datas {
		fmt.Println(" ", line)
	}

	return datas
}

```
# Tips
## 通过字符串调用指定函数
> [参考博客: Go 根据字符串调用指定函数](https://blog.csdn.net/HOOKTTG/article/details/52184500)
> [参考博客: WebAssembly 和 Go语言：对未来的观望](http://www.techug.com/post/webassembly-and-go-a-look-to-the-future.html)
