---
title: ShellLearn.md
date: 
tags: 
catagroies: 
---

**目录 start**
 
1. [学习Shell](#学习shell)
    1. [shell类别](#shell类别)
    1. [Shell内建命令](#shell内建命令)
    1. [Tips](#tips)
    1. [执行](#执行)
    1. [输入输出](#输入输出)
        1. [输入](#输入)
        1. [输出](#输出)
            1. [彩色输出](#彩色输出)
    1. [变量](#变量)
        1. [变量作用域](#变量作用域)
        1. [嵌套](#嵌套)
    1. [数据类型](#数据类型)
        1. [整型](#整型)
        1. [字符串](#字符串)
        1. [数组](#数组)
    1. [结构](#结构)
        1. [传递参数](#传递参数)
        1. [判断](#判断)
            1. [if](#if)
            1. [case](#case)
        1. [循环](#循环)
    1. [函数](#函数)
    1. [配置文件](#配置文件)
    1. [脚本的参数自动补全](#脚本的参数自动补全)
        1. [Bash](#bash)
        1. [Zsh](#zsh)
    1. [常用模块](#常用模块)
        1. [时间](#时间)
    1. [工具](#工具)
        1. [shyaml](#shyaml)

**目录 end**|_2018-12-13 12:06_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 学习Shell
> 首先语法不像别的语言可读性好，比如Python，然后方言众多，学习比Python2，3还恶心  
> [Shell 编程之语法基础](https://linuxtoy.org/archives/shell-programming-basic.html) | [Shell 编程之执行过程](https://linuxtoy.org/archives/shell-programming-execute.html)  
> [Shell 教程](http://www.runoob.com/linux/linux-shell.html)

## shell类别

- sh
  - 大多Linux都支持的shell类别
- bash
- zsh
  - 十分现代化 [配置oh my zsh](https://segmentfault.com/a/1190000004695131)
- dash
  - 它主要是为了执行脚本而出现，而不是交互，它速度更快，但功能相比bash要少很多，语法严格遵守POSIX标准
  - 速度确实要快,输入上的交互确实交互不了
- fish

> [linux shell dash&bash](http://blog.csdn.net/zengqiang1/article/details/61916697)
> [参考博客: 常见shell类型](http://www.cnblogs.com/happycxz/p/7840077.html)

> [Github: zsh guide](https://github.com/goreliu/zshguide)  
*****************
## Shell内建命令
- [ ] 学习内建命令的使用

****************
## Tips
> 常用代码片段 

1. 获取当前shell脚本的绝对路径 ```basepath=$(cd `dirname $0`; pwd)```
1. 命令嵌套 只要在 命令中用 两个反引号 `` 将子命令包住即可
1. 检查当前用户为Root用户
    ```sh
        if [ $(id -u) != "0" ]; then
            printf $red"Please use root to run this script\n"$end
            exit 1
        fi
    ```
1. kill 脚本进程
    ```sh
        id=`ps -ef | grep "WithRedis.py" | grep -v "grep" | grep -v "\-d" | awk '{print $2}'`
        if [ "${id}1" = "1" ];then
            printf $red"not exist background running script\n"$end
        else
            kill -9 $id
        fi
    ```
1. 得到脚本绝对路径; 如果只是执行 pwd 只是得到执行脚本时的当前绝对路径而已
    ```sh
        basepath=$(cd \`dirname $0\`; pwd) 
    ```

*******************
## 执行
- [source命令](http://blog.csdn.net/xiaolang85/article/details/7861441) | [点和source命令](http://www.cnblogs.com/my_life/articles/4323528.html)

- 文件头部 `#!/bin/sh`表示要使用sh解释器来执行, 可以替换成bash dash
  -  只要该文件具有执行权限就可以直接运行了 `./a.sh` 或者绝对路径

**********************
## 输入输出
### 输入
- `read answer`

并且在处理管道的输入也是一样的使用 read
```sh
while read line; do
  echo $line
done
```
### 输出
echo  printf 

#### 彩色输出
> [参考博客,比较详细](http://blog.csdn.net/magiclyj/article/details/72637666)

```sh
  red='\033[0;31m'
  green='\033[0;32m'
  yellow='\033[0;33m'
  blue='\033[0;34m'
  purple='\033[0;35m'
  cyan='\033[0;36m'
  white='\033[0;37m'
  default='\033[0m'
```

******************
## 变量

### 变量作用域
> 比Python的作用域更加恶心

### 嵌套
```sh
  # 实现了读取 A_host变量的值
  perfix='A_'
  name=${perfix}host
  host=${!name}
```

> [shell将变量当命令执行问题](http://www.bitscn.com/os/linux/201505/506409.html)

1. `${command}`
2. `echo ${command}|awk '{run=$0;system(run)}'` 最好

*****************
## 数据类型
### 整型

- 自增：
    - i=$(( $i + 1 )) _dash sh 都有效_
    - ((a++))
    - ``` i=`expr $i + 1`;```
    - let i+=1;
    - i=$[$i+1];
- 取余
    - i=$(( $i % 3))

> [取随机数](http://www.cnblogs.com/chengmo/archive/2010/10/23/1858879.html)

- 四则运算 [参考博客 ](https://blog.csdn.net/taijianyu/article/details/6907288)
  - ((i=$j+$k))     等价于   i=`expr $j + $k`
  - ((i=$j-$k))     等价于   i=`expr $j -$k`
  - ((i=$j*$k))     等价于   i=`expr $j \*$k`
  - ((i=$j/$k))     等价于   i=`expr $j /$k`

_判断变量是否为数值_
> [博客 判断是否为数值](http://www.jb51.net/article/67468.htm)
```sh
  if [ "$1" -gt 0 ] 2>/dev/null ;then 
    echo "$1 is number." 
  else 
    echo 'no.' 
  fi 
```
************
### 字符串
- [字符串截取](https://www.2cto.com/os/201305/208219.html) | [Blog:变量字符串截取](http://www.jb51.net/article/56563.htm) | [Shell正则](http://man.linuxde.net/docs/shell_regex.html)

- [ ] 重新整理
```sh
  ${varible##*string} 从左向右截取最后一个string后的字符串
  ${varible#*string}  从左向右截取第一个string后的字符串
  ${varible%%string*} 从右向左截取最后一个string后的字符串
  ${varible%string*}  从右向左截取第一个string后的字符串

  vars=${vars%%#*} # 截取#左边
  vars=${vars#*cd} # 截取最左的cd的右边
  vars=${vars%\'*} # 截取 右边引号 之左
```

`获取命令的输出`
- 使用  保存结果的变量名=`需要执行的linux命令` 这种方式来获取命令的输出时，注意的情况总结如下：
- 1）保证反单引号内的命令执行时成功的，也就是所命令执行后$?的输出必须是0，否则获取不到命令的输出
- 2）即便是命令的返回值是0，也需要保证结果是通过标准输出来输出的，而不是标准错误输出，否则需要重定向
- 因此我们推荐使用  保存结果的变量名=`需要执行的linux命令 2>&1 `的方式来获取命令的执行结果。

- 输出变量时: `$var`会丢失换行和空格 `"$var"`不会

`字符串的包含问题`
```sh
  isGithub=`expr match "$line" ".*"$2`
  # 简单的就是使用grep
  isGithub=`echo $line | grep "github" `
  # return 0 is $1 is substring of $2, otherwise 1
  strIsSubstring(){
      local x=1
      case "$2" in
          *$1*) x=0;;
      esac
      echo $x
  }
```
_求长_ ```${#var}```

_字符串拆分成数组_
> [修改分隔符](http://www.cnblogs.com/FlyFive/p/3640243.html) | [三种方法概述](https://blog.csdn.net/bitcarmanlee/article/details/50973454)

1. 如果是空格分割的字符串
    - 直接 `for element in $target`

************************
### 数组

*********************
## 结构

### 传递参数
> [参考博客](http://www.cnblogs.com/FrankTan/archive/2010/03/01/1634516.html) `命令行选项 参数处理`

| 参数 | 说明 |
|:----:|:----|
| `$#` | 传递到脚本的参数个数
| `$*` | 以一个单字符串显示所有向脚本传递的参数。以"$1 $2 … $n"的形式输出所有参数。
| `$$` | 脚本运行的当前进程ID号
| `$!` | 后台运行的最后一个进程的ID号
| `$@` | 与$*相同，但是使用时加引号 以"$1" "$2" … "$n" 的形式输出所有参数。
| `$-` | 显示Shell使用的当前选项，与set命令功能相同。
| `$?` | 显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。

> 读取脚本参数 
```sh
  # 1. 简单的方式
  case $1 in 
    -h | h)
      echo "help"
    ;;
    *)
      echo "default"
    ;;
  esac

  # 2. 规范化的参数
  while getopts "hup:" opt; do
    case "$opt" in
      h)
        usage
        exit 0
        ;;
      u)
        UPCASE=true
        ;;
      d)
        DATE=$OPTARG
        ;;
    esac
  done
```
### 判断
#### if
- [参考博客](http://www.cnblogs.com/276815076/archive/2011/10/30/2229286.html)

_判断文件_
- 文件 `if [ -f path ]`
- 链接 `if [ -L path ]`
- 目录 `if [ -d path ]`

- 整数比较
    - `-eq` 等于,如:if [ "$a" -eq "$b" ]
    - `-ne` 不等于,如:if [ "$a" -ne "$b" ]
    - `-gt` 大于,如:if [ "$a" -gt "$b" ]
    - `-ge` 大于等于,如:if [ "$a" -ge "$b" ]
    - `-lt` 小于,如:if [ "$a" -lt "$b" ]
    - `-le` 小于等于,如:if [ "$a" -le "$b" ]
    - `大于` (需要双括号),如:(("$a" > "$b"))
    - `>= `大于等于(需要双括号),如:(("$a" >= "$b"))
#### case

```sh
  case $content in 
    -h|h)
      echo "help"
    ;;
    *)
      echo "前面全部不匹配才会执行"
    ;;
  esac
```
### 循环
- [参考博客](http://www.cnblogs.com/fhefh/archive/2011/04/15/2017233.html)

`简易循环`
```sh
  for i in $(seq 1 5); do
    echo $i
  done
```
```sh
    i=1
    while [ "$i" -le 10 ];do
        echo $i
        i=$(($i+1))
    done
```
*****************
## 函数
> Shell的函数只能返回整型数据类型

```sh
  simple(){
    echo "simple"
  }
```
**********************
## 配置文件
> [参考博客](http://blog.csdn.net/xinfuqizao/article/details/21812003)

********************
## 脚本的参数自动补全
> [参考博客: 命令行自动补全原理 ](http://www.cnblogs.com/wang_yb/p/5969451.html)

### Bash

### Zsh
> 更为直观, 简单

学习怎么使用的话, 可以看上面的博客(虽然有点简陋), 但是如果是 oh-my-zsh 的用户, 可以直接看别人的插件, 模仿就行了, 例如 redis-cli 插件的自动补全, 就很简单直接
1. `#compdef redis-cli rec` 这第一行很重要, 定义了是对哪个命令或脚本的自动补全

*****************
## 常用模块
### 时间
> [shell处理时间格式](http://blog.csdn.net/superbfly/article/details/52453334)

*********************************
## 工具
> [更多工具](/Skills/Soft_Manual.md#终端工具)

### shyaml
> [参考](https://linuxtoy.org/archives/shyaml.html)

