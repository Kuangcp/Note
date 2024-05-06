---
title: 正则表达式
date: 2018-11-21 10:56:52
tags: 
categories: 
    - 基础知识
---

💠

- 1. [正则表达式](#正则表达式)
    - 1.1. [基本字符](#基本字符)
    - 1.2. [特殊字符](#特殊字符)
    - 1.3. [变量](#变量)
    - 1.4. [零宽断言](#零宽断言)
- 2. [正则表达式引擎](#正则表达式引擎)
    - 2.1. [匹配模式](#匹配模式)
    - 2.2. [性能陷阱](#性能陷阱)
- 3. [语言实现](#语言实现)
    - 3.1. [Java](#java)
    - 3.2. [Python](#python)
    - 3.3. [Shell](#shell)
- 4. [Tips](#tips)

💠 2024-05-06 19:59:21
****************************************
# 正则表达式
> [Regular Expression Language - Quick Reference](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference)  


## 基本字符 

| 模式 | 作用 |
|:----|:----|
| `^`     | 匹配输入字符串的开始位置，除非在方括号表达式中使用，此时它表示不接受该字符集合。
| `$`     | 匹配输入字符串的结尾位置。如果设置了 RegExp 对象的 Multiline 属性，则 $ 也匹配 '\n' 或 '\r'。
| `( )`   | 标记一个子表达式的开始和结束位置。子表达式可以获取供以后使用：`([0-9]{3})?` 匹配出现三个数字连着的字符串
| `{N}`   | 匹配前面出现的子表达式 N 次
| `{N,M}` | 匹配前面的子表达式 N-M 次
| `[...]` | 匹配字符集的任一单个字符 ： `[abcdejk]`就是匹配里面任一单个字符 
| `[^...]`| 不匹配此集合中任一字符，包括某一范围的字符：`[^0-9]` 字符串中不含数字
| `[x-y]` | 匹配x-y范围内单一字符 ： `[0-9] [a-z]`
| `*`     | 匹配前面的子表达式 0或多次。 
| `+`     | 匹配前面的子表达式 1或多次。
| `?`     | 匹配前面的子表达式 0或1次，或指明一个非贪婪限定符。
| `.`     | 匹配除换行符 `\r` `\n` 之外的任何 单个字符。
| `\`     | 将下一个字符标记为或转义字符、或原义字符、或向后引用、或八进制转义符。'\n' 匹配换行符。 
| `|`     | 指明两项之间的一个选择。

`以上字符都需转义`

************************

## 特殊字符
| 模式 | 作用 |
|:----|:----|
| `\d`    | 匹配任何十进制数字 与 `[0-9]` 相同 `\D`与之相反 |
| `\w`    | 匹配任何字母数字字符 与 `[a-zA-Z0-9_]` 相同， `\W`与之相反 |
| `\s`    | 匹配任何空字符(空格 tab 回车) 与 `[\n\t\r\v\f]` 相同，`\S`与之相反 |
| `\b`    | 匹配任何单词的边界 `\B`与之相反 |
| `\N`    | 匹配已保存的子组N次 `name\100` |
| `\c`    | 逐字匹配任何特殊字符 `c` 就是转义字符的使用 |
| `\A \Z` | 匹配字符串的开始或结束 |

> 构造正则表达式的方法和创建数学表达式的方法一样。也就是用多种元字符与操作符将小的表达式结合在一起来创建更大的表达式。
> 正则表达式的组件可以是单个的字符、字符集合、字符范围、字符间的选择或者所有这些组件的任意组合。 

************************

## 变量

常用于正则替换
1. `(\w*)_(\w*)_(\w*)` => `\l$1\u$2\u$3` 
    - user_name_flag => userNameFlag
1. `(.*)/\d+\.\d+\.\d+\.\d+(.*)` => `$1/1.1.1.1/$2` 
    - http://1.2.3.4/path/url => http://1.1.1.1/path/url

## 零宽断言
> 用于查找在某些内容(但并不包括这些内容)之前或之后的东西，也就是说它们像 \b, ^, $, <, >, 那样用于指定一个位置  
> 这个位置应该满足一定的条件(即断言)，因此它们也被称为零宽断言

> [参考: 零宽断言](https://www.cnblogs.com/shangdawei/p/4673117.html)
> [正则表达式的先行断言(lookahead)和后行断言(lookbehind)](https://www.runoob.com/w3cnote/reg-lookahead-lookbehind.html)

- `(?=exp)`  零宽正向先行断言(zero-width positive lookahead assertion) 
- `(?!exp)`  零宽负向先行断言(zero-width negative lookahead assertion)
- `(?<=exp)` 零宽正向后行断言(zero-width positive lookbehind assertion)
- `(?<!exp)` 零宽负向后行断言(zero-width negative lookbehind assertion)

> eg：
- `(?<=a).*(?=b)` 提取ab字符之间的值

***************************
# 正则表达式引擎
正则表达式是一个用正则符号写出的公式，程序对这个公式进行语法分析，建立一个语法分析树，再根据这个分析树结合正则表达式的引擎生成执行程序（这个执行程序我们把它称作状态机，也叫状态自动机），用于字符匹配。

而这里的正则表达式引擎就是一套核心算法，用于建立状态机。

目前实现正则表达式引擎的方式有两种：DFA [确定有限状态自动机](https://en.wikipedia.org/wiki/Deterministic_finite_automaton) 和 NFA [非确定有限状态自动机](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton)。

对比来看，构造 DFA 自动机的代价远大于 NFA 自动机，但 DFA 自动机的执行效率高于 NFA 自动机。

假设一个字符串的长度是 n，如果用 DFA 自动机作为正则表达式引擎，则匹配的时间复杂度为 O(n)；如果用 NFA 自动机作为正则表达式引擎，由于 NFA 自动机在匹配过程中存在大量的分支和回溯，假设 NFA 的状态数为 s，则该匹配算法的时间复杂度为 O(ns)。

NFA 自动机的优势是支持更多功能。例如：捕获 group、环视、占有优先量词等高级功能。这些功能都是基于子表达式独立进行匹配，因此在编程语言里，使用的正则表达式库**都是基于 NFA 实现的**。

## 匹配模式
贪婪模式（Greedy）
懒惰模式（Reluctant）
独占模式（Possessive）

## 性能陷阱
> [如何优化正则表达式性能？](https://segmentfault.com/a/1190000039941785)

************************

# 语言实现
## Java

```java
    Pattern pt = Pattern.compile("\\d+");
    pt.matcher("12,3");
```

注意：
- Pattern对象尽可能复用，compile很耗CPU资源

## Python
- ![re.jpg](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/python/re.jpg)

## Shell
- [Shell正则表达式](http://man.linuxde.net/docs/shell_regex.html)

************************

# Tips
- 连续重复字符的匹配 `(.)\1+` [正则表达式匹配重复的字符串](http://www.aijquery.cn/Html/jqueryjiqiao/181.html)
