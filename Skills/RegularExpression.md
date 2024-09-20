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
    - 1.3. [分组捕获](#分组捕获)
    - 1.4. [变量](#变量)
    - 1.5. [零宽断言](#零宽断言)
- 2. [正则表达式引擎](#正则表达式引擎)
    - 2.1. [NFA匹配模式](#nfa匹配模式)
    - 2.2. [性能陷阱](#性能陷阱)
- 3. [语言实现](#语言实现)
    - 3.1. [Java](#java)
    - 3.2. [Python](#python)
    - 3.3. [Shell](#shell)
- 4. [Tips](#tips)

💠 2024-09-20 11:10:09
****************************************
# 正则表达式
> [Regular Expression Language - Quick Reference](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference)  

> [Grex](https://github.com/pemistahl/grex)  
> [Regex-Vis](https://github.com/Bowen7/regex-vis)  

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

`以上字符需要匹配字面值时都需转义`

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

> Pattern
- (?i) 开启忽略大小写 (?-i) 关闭忽略大小写
    - 但是i只处理 ASCII 字符，如果需要处理Unicode字符需要加上u或U 例如 `(?iu)`, `(?iU)`

```
i - Ignore case
m - Treat a newline as a character matched by .
x - Ignore whitespace and comments in the pattern
o -> Perform #{} interpolation only once
```

************************
## 分组捕获
> [Grouping Constructs](https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference#grouping-constructs)

正则中的()都是一个分组捕获，库通常使用下标来定位匹配到的分组

同时可以使用命名分组  Named groups。

```java
    Pattern idxGroup = Pattern.compile("(\\d{4})-(\\d{2})");
    Matcher matcher = idxGroup.matcher("2012-12");
    System.out.println(matcher.matches());
    assertThat(matcher.group(1), equalTo("2012"));
    assertThat(matcher.group(2), equalTo("12"));

    Pattern nameGroup = Pattern.compile("(?<year>\\d{4})-(?<month>\\d{2})");
    matcher = nameGroup.matcher("2012-12");
    System.out.println(matcher.matches());
    assertThat(matcher.group("year"), equalTo("2012"));
    assertThat(matcher.group("month"), equalTo("12"));
```

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

NFA 自动机的优势是支持更多功能。例如：捕获group、环视、占有优先量词等高级功能。这些都是基于子表达式独立进行匹配，因此在编程语言里，正则表达式库**都是基于 NFA 实现的**。

## NFA匹配模式
> [what are possessive quantifiers in Java regular expression used for?](https://stackoverflow.com/questions/26006653/what-are-possessive-quantifiers-in-java-regular-expression-used-for)

**贪婪模式（Greedy）**

如果单独使用 +、？、*或{min,max}等量词，正则表达式会匹配尽可能多的内容。

例如 文本 abbc 模式 `ab{1,3}c`， NFA会先读取最大匹配范围3，匹配失败后回溯到2匹配成功，如果文本是 abbbc 就不会回溯直接匹配成功了
当有多个匹配组时，性能下降会更明显 例如 `^([A-Za-z0-9]+)([A-Z0-9][A-Z0-9])(.*)` 可以看到有三个匹配分组第一个可能将匹配失败的字符给到第二个第三个组匹配，分支数会大量膨胀

**懒惰模式（Reluctant）**

尽可能少地重复匹配字符，如果匹配成功，它会继续匹配剩余的字符串。

例如 文本 abbc 模式 `ab{1,3}?c`, NFA自动机会先读取最小匹配范围1再继续匹配，*避免了回溯问题*。
当多匹配组时 改进前文中表达式 `^([A-Za-z0-9]+?)([A-Z0-9][A-Z0-9])(.*)` 降低了分支数。

**独占模式（Possessive）**

和贪婪模式一样，独占模式一样会最大限度地匹配更多内容；不同的是，在独占模式下，匹配失败就会结束匹配，不会发生回溯问题。多组匹配时一个组的匹配失败的字符不会给到另一个组

例如 文本 abbc，模式为`ab{1,3}+c`。 
- JavaScript中匹配会报错 **Invalid regular expression Nothing to repeat**。 
- Java中能匹配成功，但没有发生所谓的独占模式引发匹配失败的场景, 奇怪？
- Golang中会报错 **invalid nested repetition operator**
当多匹配组时 例如 `^([A-Z]++)([H-Zw])(.*)` 

> 注意：JavaScript，Python和Go 的标准库*不支持*独占模式

## 性能陷阱
> [如何优化正则表达式性能？](https://segmentfault.com/a/1190000039941785)

1. 少用贪婪模式
1. 减少分支选择带来的组合情况笛卡尔积
1. 减少捕获`()`嵌套
1. 
************************

# 语言实现
## Java

```java
    Pattern pt = Pattern.compile("\\d+");
    pt.matcher("12,3");
```

注意：
- 因为compile很耗CPU资源，所以Pattern对象需要尽可能复用，最好成为静态属性（它是不可变实例，是并发安全的）

## Python
- ![re.jpg](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/python/re.jpg)

## Shell
- [Shell正则表达式](http://man.linuxde.net/docs/shell_regex.html)

************************

# Tips
- 连续重复字符的匹配 `(.)\1+` [正则表达式匹配重复的字符串](http://www.aijquery.cn/Html/jqueryjiqiao/181.html)
