`目录 start`
 
- [Go](#go)
    - [社区](#社区)
    - [书籍](#书籍)
    - [安装](#安装)
        - [Docker](#docker)
    - [环境变量解释](#环境变量解释)
    - [基本开发环境搭建](#基本开发环境搭建)
    - [数据类型](#数据类型)
        - [基本类型](#基本类型)
        - [Array](#array)
        - [Slice](#slice)
        - [Map](#map)
        - [Set](#set)
    - [基本语法](#基本语法)
        - [标准输入输出](#标准输入输出)
    - [文件操作](#文件操作)
    - [JSON](#json)
- [Tips](#tips)
    - [通过字符串调用指定函数](#通过字符串调用指定函数)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Go
> [官网](https://golang.org) | [镜像网](https://golang.google.cn/) | [Github Repo](https://github.com/golang/go) | [Go Doc](https://godoc.org/)

Go 语言被设计成一门应用于搭载 Web 服务器，存储集群或类似用途的巨型中央服务器的系统编程语言。对于高性能分布式系统领域而言，Go 语言无疑比大多数其它语言有着更高的开发效率。它提供了海量并行的支持，这对于游戏服务端的开发而言是再好不过了。

- [Go语言资料收集](https://github.com/wonderfo/wonderfogo/wiki)
- [学习Go的知乎话题](https://www.zhihu.com/question/23486344)
- [Go相关书籍的知乎话题](https://www.zhihu.com/question/30461290)
- [Go1.0的吐槽](http://blog.csdn.net/liigo/article/details/23699459)
- [Java 20年：转角遇到Go](http://www.infoq.com/cn/news/2015/05/java20-from-language-to-platform)

> [参考博客: Golang官网被墙解决办法](https://golangtc.com/t/504072ca320b5276e2000004)
## 社区
- [GoCN Forum](https://gocn.vip/)
- [Go语言中文网](https://studygolang.com)

- [Go Programming & Concurrency in Practice](https://github.com/hyper0x/goc2p)

## 书籍

> [Go语言高级编程(Advanced Go Programming)](https://books.studygolang.com/advanced-go-programming-book/index.html)


## 安装
> [下载](https://golang.google.cn/dl/)|[官方教程](https://golang.google.cn/doc/install) | [参考 教程](http://www.runoob.com/go/go-environment.html) | [_](http://cloud.kuangcp.top/go-1.10.3.tar.gz)


1. sudo tar -C /usr/local -xzf go1.10.3.linux-amd64.tar.gz
2. *shrc或者 /etc/profile 中添加
```sh
export GOROOT=/usr/local/go
export GOPATH=$HOME/Code/go # workspace
export GOBIN=$GOPATH/bin # 'go install' command install dir
export PATH=$PATH:$GOBIN:$GOPATH:$GOROOT/bin
```
> **查看版本** `go version`正常输出go的版本则是配置成功  
3. 在 /home/kcp/code/go 下 新建 test.go
```go
package main
import "fmt"
func main() {
    fmt.Printf("hello, world\n")
}
```
4. go run test.go 或者 go build

### Docker
> 使用Docker安装和部署

> [Docker image](https://hub.docker.com/_/golang/) `这里的镜像都是用于 从源码编译构建成可执行文件的 环境`   
> [go 的 Docker镜像的讨论](https://gocn.vip/question/153)

1. 实际运行的时候, 如果不需要调用外部Linux命令 就直接 `from scratch`
1. 需要则 `from alpine` 更精简一点 更好是使用 `frolvlad/alpine-glibc`

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

## 基本开发环境搭建
> [Github:Golang](https://github.com/golang)

入门时使用VSCode是比较方便的, VSCode 会推荐我们安装如下工具
1. tools _工具集_
    1. guru `golang.org/x/tools/cmd/guru`
    1. gorename `golang.org/x/tools/cmd/gorename`
1. lint `golang.org/x/lint`
    1. golint `golang.org/x/lint/golint`
1. go-outline `github.com/ramya-rao-a/go-outline`
1. go-symbols `github.com/acroca/go-symbols`
1. goreturns `github.com/sqs/goreturns`

- [ ] godep 同样的方式

- 安装完后就会在GOPATH中能找到这些工具对应的命令了, 由于 golang.org 被墙 
    - 所以 只有这几个工具不能直接 go get : guru gorename imports(goreturns要用到) lint golint 

https://github.com/golang/tools 是 tools 的Github地址,  
https://github.com/golang/lint 是 lint 和 golint 的Github地址, 


1. `mkdir -p src/golang.org/x/tools`
1. `mkdir -p src/golang.org/x/lint`
1. 将 https://github.com/golang/tools clone所有内容 放到 src/golang.org/x/tools 下
1. 将 https://github.com/golang/lint  clone所有内容 放到 src/golang.org/x/lint 下
1. 此时再执行 go get 那五个工具即可全部安装成功

问题又来了, Github 由于飘忽不定的被墙, 网速特别慢, 就可以利用码云来加速下载
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

## JSON
> [参考博客: Go操作JSON](https://blog.csdn.net/u011304970/article/details/70769949)
> [参考博客: go and json](https://eager.io/blog/go-and-json/)
> [参考博客: 在Go语言中使用JSON](https://blog.csdn.net/tiaotiaoyly/article/details/38942311) `结构体必须是大写字母开头的成员才会被JSON处理到，小写字母开头的成员不会有影响。`

> [website: json to go struct](https://mholt.github.io/json-to-go/)

# Tips
## 通过字符串调用指定函数
> [参考博客: Go 根据字符串调用指定函数](https://blog.csdn.net/HOOKTTG/article/details/52184500)
> [参考博客: WebAssembly 和 Go语言：对未来的观望](http://www.techug.com/post/webassembly-and-go-a-look-to-the-future.html)
