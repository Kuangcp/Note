---
title: Go基础
date: 2018-12-14 09:25:49
tags: 
    - 函数式编程
categories: 
    - Go
---

**目录 start**

1. [Go](#go)
    1. [Modules](#modules)
        1. [配置](#配置)
    1. [数据类型](#数据类型)
        1. [string](#string)
        1. [int](#int)
        1. [Array](#array)
        1. [Slice](#slice)
        1. [Map](#map)
        1. [Set](#set)
    1. [基本语法](#基本语法)
        1. [标准输入输出](#标准输入输出)
        1. [时间处理](#时间处理)
    1. [函数](#函数)
        1. [参数](#参数)
        1. [返回值](#返回值)
        1. [defer](#defer)
    1. [接口](#接口)
    1. [Channel](#channel)
    1. [文件操作](#文件操作)
    1. [Test](#test)
    1. [JSON](#json)
1. [Tips](#tips)
    1. [通过字符串调用指定函数](#通过字符串调用指定函数)

**目录 end**|_2020-10-28 20:53_|
****************************************
# Go
> [官网](https://golang.org) | [镜像官网](https://golang.google.cn/) | [Github Repo](https://github.com/golang/go) | [Go Doc](https://godoc.org/)

> [Rethinking Visual Programming with Go](https://divan.dev/posts/visual_programming_go/)

> [Goplus](https://github.com/qiniu/goplus)

> [project-layout](https://github.com/golang-standards/project-layout)`项目结构规范`

## Modules
> 1.11 开始支持 [Wiki](https://github.com/golang/go/wiki/Modules)  

### 配置
- `go env -w GOSUMDB=off` 关闭官方 sum 校验服务

> 配置国内源
```sh
export GO111MODULE=on
export GOPROXY=https://mirrors.aliyun.com/goproxy/
export GOSUMDB=sum.golang.google.cn
```

> [wiki Modules](https://github.com/golang/go/wiki/Modules)  
> [参考: Go模块简明教程](https://github.com/wuyumin/tutorial/blob/master/zh-cn/Modules/README.md)  

************************

1. `go mod init moduleName` 按名初始化模块
1. `go mod edit -replace github.com/kuangcp/gobase/cuibase=./../cuibase`
    - 多模块开发时，使用本地开发的模块取代发布的版本
    - 效果: `replace github.com/kuangcp/gobase/cuibase => ./../cuibase`

************************

## 数据类型
_类型后置的设计相关文章_

> [螺旋形（C/C++）和顺序（Go）的声明语法](https://cxwangyi.wordpress.com/2011/03/14/%E8%9E%BA%E6%97%8B%E5%BD%A2%EF%BC%88cc%EF%BC%89%E5%92%8C%E9%A1%BA%E5%BA%8F%EF%BC%88go%EF%BC%89%E7%9A%84%E5%A3%B0%E6%98%8E%E8%AF%AD%E6%B3%95/)  
> [Why do a lot of programming languages put the type *after* the variable name?](https://stackoverflow.com/questions/1712274/why-do-a-lot-of-programming-languages-put-the-type-after-the-variable-name)

### string
strings 包 提供了常用字符串API

### int
> int8 int16 int32 int64 int(位数按操作系统字长而定 32/64)
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
```go
    // 判断 key 存在
    _, ok := dataMap["key"]
```

### Set

******************

## 基本语法

### 标准输入输出
> [参考: golang中的格式化输入输出](https://blog.csdn.net/xiaoyida11/article/details/51554022)

- 打印结构体 `fmt.Printf("%v\n", object)`

### 时间处理
> [Go: Format a time or date](https://programming.guide/go/format-parse-string-time-date-example.html)

记住这个神奇的时间 `2006-01-02 03:04:05` Go 中不是寻常的 YYYY-mm-dd 这种格式

**************************

## 函数
基本结构
```go
// 函数名 (参数 ) 返回值{函数体}
func functionName (param int) int {

}
```

### 参数
> 使用函数作为参数 `func doAny(functionName func(string, string)){}`

### 返回值
> 可以多返回值 元组

### defer
> 类似于 Java 中的 finally 语句 例如 `defer openFile.Close()`

一个函数中可以定义多个 defer 语句, 执行顺序按定义顺序的逆序, 也就是栈的概念

*************************

## 接口
> [参考:接口的定义和使用](http://www.cnblogs.com/yjf512/archive/2012/06/09/2543628.html)

************************

## Channel 
> [参考 如何优雅地关闭Go channel](https://www.jianshu.com/p/d24dfbb33781)
> [Go Channel 详解 ](https://colobu.com/2016/04/14/Golang-Channels/)  

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

************************

> [statik](github.com/rakyll/statik) `将文件打包入二进制执行文件中去`

************************

## Test
> [Github: assert](https://godoc.org/github.com/stretchr/testify/assert)

***********************

## JSON
> `结构体必须是大写字母开头的成员才会被处理(大写字母开头才有对外权限)`

> [参考: Go操作JSON](https://blog.csdn.net/u011304970/article/details/70769949)
> [参考: go and json](https://eager.io/blog/go-and-json/)
> [参考: 在Go语言中使用JSON](https://blog.csdn.net/tiaotiaoyly/article/details/38942311) 

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

> 忽略空字段

1. 字段是指针类型 且注明 omitempty
```go
Msg struct{
 Text     *Content `json:"text,omitempty"`
}
```

************************

# Tips
> [lorca](https://github.com/zserge/lorca.git) `H5 + chromium + Golang`桌面端

## 通过字符串调用指定函数
> [参考: Go 根据字符串调用指定函数](https://blog.csdn.net/HOOKTTG/article/details/52184500)
> [参考: WebAssembly 和 Go语言：对未来的观望](http://www.techug.com/post/webassembly-and-go-a-look-to-the-future.html)
