---
title: Shell学习
date: 2018-12-15 12:10:46
tags: 
    - Shell
categories: 
    - Linux
---

💠

- 1. [学习Shell](#学习shell)
    - 1.1. [shell类别](#shell类别)
    - 1.2. [执行方式](#执行方式)
- 2. [基础结构](#基础结构)
    - 2.1. [输入输出](#输入输出)
        - 2.1.1. [输入](#输入)
        - 2.1.2. [输出](#输出)
    - 2.2. [变量](#变量)
        - 2.2.1. [变量作用域](#变量作用域)
        - 2.2.2. [嵌套](#嵌套)
    - 2.3. [数据类型](#数据类型)
        - 2.3.1. [整型](#整型)
        - 2.3.2. [字符串](#字符串)
        - 2.3.3. [数组](#数组)
    - 2.4. [结构](#结构)
        - 2.4.1. [传递参数](#传递参数)
        - 2.4.2. [判断](#判断)
            - 2.4.2.1. [if](#if)
            - 2.4.2.2. [case](#case)
        - 2.4.3. [循环](#循环)
    - 2.5. [函数](#函数)
    - 2.6. [多线程](#多线程)
    - 2.7. [定时执行](#定时执行)
        - 2.7.1. [watch](#watch)
        - 2.7.2. [sleep](#sleep)
- 3. [集成](#集成)
    - 3.1. [文件处理](#文件处理)
        - 3.1.1. [配置文件](#配置文件)
            - 3.1.1.1. [ini和conf](#ini和conf)
        - 3.1.2. [shyaml](#shyaml)
    - 3.2. [脚本的参数自动补全](#脚本的参数自动补全)
        - 3.2.1. [Bash](#bash)
        - 3.2.2. [Zsh](#zsh)
- 4. [Tips](#tips)
    - 4.1. [常用代码片段](#常用代码片段)

💠 2024-09-20 11:10:09
****************************************
# 学习Shell
> [Shell 编程之语法基础](https://linuxtoy.org/archives/shell-programming-basic.html) | [Shell 编程之执行过程](https://linuxtoy.org/archives/shell-programming-execute.html)  

> [菜鸟教程: Shell 教程](http://www.runoob.com/linux/linux-shell.html)  
> [C语言中文网: Shell教程](http://c.biancheng.net/shell/)  

> [参考: 编写 Bash Shell 脚本的最佳实践](https://blog.mythsman.com/post/5d2ab67ff678ba2eb3bd346f/)  

************************

> [shellcheck](https://github.com/koalaman/shellcheck)`Shell语法检测`  
> [cmd-wrapped](https://github.com/YiNNx/cmd-wrapped)`统计命令执行历史`  

## shell类别
> 切换默认shell `chsh -s /bin/zsh`

- sh
    - 大多Linux都支持的shell类别
- bash
- zsh
  - 高扩展性 [配置oh my zsh](https://segmentfault.com/a/1190000004695131)
- dash
    - 它主要是为了执行脚本而出现，而不是交互，它速度更快，但功能相比bash要少很多，语法严格遵守POSIX标准
    - 速度确实要快,输入上的交互确实交互不了
- fish
    - 交互式的, 补全功能比较好 

> [参考: 常见shell类型](http://www.cnblogs.com/happycxz/p/7840077.html)  
> [Github: zsh guide](https://github.com/goreliu/zshguide)  

*******************

## 执行方式
- [source命令](http://blog.csdn.net/xiaolang85/article/details/7861441) | [点和source命令](http://www.cnblogs.com/my_life/articles/4323528.html)

- 文件头部 `#!/bin/sh`表示要使用sh解释器来执行, 可以替换成bash dash
    -  只要该文件具有执行权限就可以直接运行了 `./a.sh` 或者绝对路径

- [pueue](https://github.com/Nukesor/pueue)`shell后台执行队列`

**********************
# 基础结构
## 输入输出
### 输入
- `read answer`

处理管道的输入也是使用 read
```sh
while read line; do
  echo $line
done
```

- `select`

```sh
  echo "What is your favourite OS?"
  select var in "Linux" "Gnu Hurd" "Free BSD" "Other"; do
    break;
  done
  echo "You have selected $var"
```
### 输出
echo  printf 

> printf
1. 原样输出字符串:
    - printf("%s", str);
2. 输出指定长度的字符串, 超长时不截断, 不足时右对齐:
    - printf("%Ns", str);  N 为指定长度的10进制数值
3. 输出指定长度的字符串, 超长时不截断, 不足时左对齐:
    - printf("%-Ns", str); N 为指定长度的10进制数值
4. 输出指定长度的字符串, 超长时截断, 不足时右对齐: 
    - printf("%N.Ms", str);  N 为最终的字符串输出长度  M 为从参数字符串中取出的子串长度
5. 输出指定长度的字符串, 超长时截断, 不足时左对齐是:
    - printf("%-N.Ms", str);  N 为最终的字符串输出长度  M 为从参数字符串中取出的子串长度
6. 上述N,M是可以动态指定的，方法是用*代替M或者N，然后在参数列表里加上一个数字参数。
    - `printf("%-*.*s", 5, 2, "123");`  等价于 `printf("%-5.2s", "123");`
    - `printf("%*s", 5, "123");` `printf("%5s", "123");`

******************
## 变量

- 获取命令输出作为变量
    - `$(ls)`
    - ``` `ls` ```

### 变量作用域
> 比Python的作用域更加宽泛和不可控，引用一个变量时需要注意值的来源。

### 嵌套
```sh
    # 实现了读取 A_host变量的值
    perfix='A_'
    name=${perfix}host
    host=${!name}
```

> [shell将变量当命令执行问题](http://www.bitscn.com/os/linux/201505/506409.html)

1. `${command}` 执行 command变量 内容
    - `echo ${command} |awk '{run=$0;system(run)}'` 推荐方式

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

************************

### 字符串
- [字符串截取](https://www.2cto.com/os/201305/208219.html) | [Blog:变量字符串截取](http://www.jb51.net/article/56563.htm) | [Shell正则](http://man.linuxde.net/docs/shell_regex.html)
> [字符串操作](https://www.cnblogs.com/gaochsh/p/6901809.html)

| Pattern | 描述 ||
|:----|:----|:---|
| `${varible#*str}`  | 截取 `首个` |str `右` 的字符串 |
| `${varible##*str}` | 截取 `最末` |str `右` 的字符串 |
| `${varible%%str*}` | 截取 `首个` |str `左` 的字符串 |
| `${varible%str*}`  | 截取 `最末` |str `左` 的字符串 |

1. `${varible:start:end}` 定长截取
  - `${varible:4}` 第四个字符到结束
1. `ls -al | cut -d "." -f 2` 取常规文件后缀名

************************

**`获取命令的输出`**
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

> [shell处理时间格式](http://blog.csdn.net/superbfly/article/details/52453334)
************************

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

注意方括号格式时，内部要留一个空格，否则会报 语法错误 

_判断文件_
- 文件存在 `if [ -e path ]`
    - -r 可读
    - -f 存在，而且是普通文件
    - -s 存在且文件大小大于0字节
- 链接存在 `if [ -L path ]`
- 目录存在 `if [ -d path ]`

- 整数比较
    - `-eq` 等于,如:if [ "$a" -eq "$b" ]
    - `-ne` 不等于,如:if [ "$a" -ne "$b" ]
    - `-gt` 大于,如:if [ "$a" -gt "$b" ]
    - `-ge` 大于等于,如:if [ "$a" -ge "$b" ]
    - `-lt` 小于,如:if [ "$a" -lt "$b" ]
    - `-le` 小于等于,如:if [ "$a" -le "$b" ]
    - `大于` (需要双括号),如:(("$a" > "$b"))
    - `>= `大于等于(需要双括号),如:(("$a" >= "$b"))

- 字符串比较
    - `if [ "$root"x = 'x' ]` 判断是否为空
        - `if test -z "$repo_path";`
    - `if [ $(echo $str | grep -e '$str1') ]` 判断包含
    - `if [[ $a == z* ]]` 模式匹配，但是不是严格正则表达式格式

- 判断数组包含 `if [[ "${ary[@]}" =~ "$a" ]]`
    - 其中 ary=(1 2 3); a=2; 

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

> for
```sh
  for i in $(seq 1 5); do
    echo $i
  done

  for (( a=0; a<10; a++)) do
    echo $a;
  done
```

> while
```sh
    i=1
    while [ "$i" -le 10 ];do
        echo $i
        i=$(($i+1))
    done
```

> 逐行遍历命令的输出
```sh
  while read -r proc; do
      #do work
  done <<< "$(ps -ewo pid,cmd,etime | grep python | grep -v grep | grep -v sh)"
```

> Tips 
1. break continue: break能跳出多层循环，只需带上数字 `break num`，也可以理解为无参的break默认带了1参数
1. done 后面可以重定向，将循环的输出转到文件而不是终端: `for do done > loop.log`

*****************

## 函数
> Shell的函数只能返回整型数据类型

- 定义函数
    - `function a {}`
    - `a(){}`
    - 注意：
        - Shell是解释执行，必须先定义，然后调用，而且函数没有重载，只覆盖
        - 命令行内定义函数: `function hi { echo hi;};` 注意左括号和命令的空格，以及命令;结尾

```sh
    simple(){
        echo "simple"
    }

    zero(){
        return 0
    }
    # 函数退出状态码（0-255）
    echo "return "$?
    
    # 使用输出返回值
    result=$(simple)
```
- 引用 shell 文件 `source shell文件相对路径` source可以简写为 `.`

## 多线程
> [参考: shell如何实现多线程](https://www.cnblogs.com/signjing/p/7074778.html)  

************************

## 定时执行
### watch
> execute a program periodically, showing output fullscreen

- -d 高亮差异数据

watch 等待命令对应进程执行完成后才进入计时到下一个周期执行，可以利用这个特性来执行异步shell

> demo.sh 
```sh 
for i in $(seq 1 100); do
  doSomething &
done
```

watch demo.sh 达到的效果为：等到sh中的100个子进程执行结束后，主进程退出，才会等2s再执行一次demo.sh 

### sleep

**********************
# 集成
## 文件处理
> 读取当前目录文件

```bash
    for file in ./*
    do
        if test -f "$file"
        then
            echo "$file 是文件"
        fi
        if test -d "$file"
        then
            echo "$file 是目录"
        fi
    done
```

> 读取文件行
```bash
    # 1
    while IFS= read -r -u3 line; do
        echo "$line"
    done 3< "$2"

    # 2
    cat a.log | while read line; do
        echo "line: "$line;
    done
```

1. 当前目录创建临时文件，并输出创建的文件名 `mktmp data.XXXXXX`
  - `-t` 在 /tmp/目录下创建，并返回全路径
  - `-d` 创建目录

1. 输出到终端并写入文件 `echo "test" | tee a.log`
1. 基于模板快速创建多份配置文件 
    ```sh
        REPLICA=01 SHARD=01 envsubst < config.xml > clickhouse01/config.xml
        REPLICA=02 SHARD=01 envsubst < config.xml > clickhouse02/config.xml
    ```
    - config.xml 中使用`${}`做占位符 例如： `<interserver_http_host>clickhouse${REPLICA}</interserver_http_host>`

### 配置文件

#### ini和conf
```conf
  [block]
  name=myth
```
- 如果没有 `[block]` 这样的声明就可以当sh用, 直接 source file 就加载了配置内容

### shyaml
> [参考](https://linuxtoy.org/archives/shyaml.html)

********************

## 脚本的参数自动补全
> [参考: 命令行自动补全原理 ](http://www.cnblogs.com/wang_yb/p/5969451.html)

### Bash

### Zsh
> 更为直观, 简单

学习怎么使用的话, 可以看上面的博客(虽然有点简陋), 但是如果是 oh-my-zsh 的用户, 可以直接看别人的插件, 模仿就行了, 例如 redis-cli 插件的自动补全, 就很简单直接
1. `#compdef redis-cli rec` 这第一行很重要, 定义了是对哪个命令或脚本的自动补全

************************

# Tips
> [hyperfine](https://github.com/sharkdp/hyperfine)命令压测工具

- set -x 开启调试 每条实际执行的命令都会输出到控制台
  - set +x 关闭调试

## 常用代码片段 

1. 获取命名或函数标准输出: 反引号 **\`cmd\`**  或者 **$(cmd)**
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
1. 得到脚本绝对路径; `如果脚本内执行 pwd 只会得到执行脚本时会话的绝对路径，而不是脚本的路径`
    ```sh
        basepath=$(cd \`dirname $0\`; pwd) 
    ```
