`目录 start`
 
- [Python](#python)
    - [简介](#简介)
        - [关于Python2.x与3.x的使用](#关于python2x与3x的使用)
    - [安装配置](#安装配置)
        - [Docker](#docker)
    - [基础](#基础)
        - [代码风格](#代码风格)
        - [基础语法](#基础语法)
        - [基础数据类型](#基础数据类型)
        - [virtualenv](#virtualenv)
        - [pip](#pip)
            - [Requirements files](#requirements-files)
            - [发布包到 pypi](#发布包到-pypi)
    - [变量](#变量)
    - [基本运行结构](#基本运行结构)
        - [序列](#序列)
            - [列表](#列表)
            - [元组](#元组)
            - [字符串](#字符串)
            - [字符串编码问题(python2问题)](#字符串编码问题python2问题)
            - [字典（键值对）](#字典（键值对）)
        - [运算符](#运算符)
        - [模块](#模块)
    - [输入输出](#输入输出)
        - [输入](#输入)
        - [输出](#输出)
        - [读取命令行参数](#读取命令行参数)
            - [docopt](#docopt)
            - [Python Fire](#python-fire)
    - [函数](#函数)
    - [类](#类)
            - [继承](#继承)
    - [异常](#异常)
    - [文件操作](#文件操作)
        - [JSON](#json)
        - [conf或者ini](#conf或者ini)
    - [测试](#测试)
    - [数据库](#数据库)
        - [MySQL](#mysql)
        - [Redis](#redis)
    - [部署](#部署)
        - [Docker部署](#docker部署)
    - [绘图](#绘图)
        - [matplotlib](#matplotlib)
    - [常见函数](#常见函数)
    - [常见库](#常见库)
        - [内置库](#内置库)
            - [时间处理](#时间处理)
        - [三方库](#三方库)
    - [QT](#qt)

`目录 end` |_2018-09-12_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Python
> [官网](https://www.python.org/)

> [Python初学者（零基础学习Python、Python入门）书籍、视频、资料、社区推荐](https://github.com/Yixiaohan/codeparkshare)
> [参考博客: Python3的主要应用](http://www.techug.com/post/what-can-you-do-with-python-the-3-main-applications.html)
- [Python中的多态](http://blog.csdn.net/shangzhihaohao/article/details/7065675)
- [python输出带颜色的字体](http://www.cnblogs.com/oleli/p/5228880.html)

> [Anaconda](https://docs.anaconda.com/anaconda/install/linux)`一站式集成环境`

- [Python2](https://docs.python.org/2/) | [Python3](https://docs.python.org/3/)
- [python-gtk3](https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html) `python-gtk3的开发`
- [httpie](http://python.ctolib.com/httpie.html) `好用的类curl工具 文档` 
- [一译](http://python.usyiyi.cn/)`翻译了大量Python文档`

## 简介

### 关于Python2.x与3.x的使用
> 摘自 Python核心编程 第三版 Wesley Chun著

- print 变为 print()
- 默认字符的编码是 Unicode
- 增加单类 类型
- 更新异常的语法
- 更新了整数
- 迭代无处不在

> 列出所有已安装模块 pydoc pydoc3

## 安装配置

**Debian系安装3.6**
1. sudo add-apt-repository ppa:jonathonf/python-3.6
1. sudo apt update 
1. sudo apt install python3.6

### Docker
> [docker hub](https://hub.docker.com/_/python/)


## 基础
### 代码风格
- 一行只写一句
- 表达式尽量不要省略括号，有助于理解
- 函数的行数不要超过100行
- 尽量使用系统函数
- 尽量使用局部变量，不要使用全局
- 循环，分支，最好不要超过5层
- 尽量减少否定的条件语句
- 对输入的数据进行合法性检查

`巨坑: tab和空格不能混用,如果你复制别人的代码是tab,自己敲空格,就会缩进错误!!!!, 天灭tab空格保平安, 要不是kate编辑器显示了tab字符,找半天都不知道错在哪`

- [Google 开源项目风格指南 (中文版)](http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/background/) 
    - `import this` 就会输出Zen Of Python | [官方文档](https://www.python.org/dev/peps/pep-0020/)
```
    优美胜于丑陋（Python 以编写优美的代码为目标）
    明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）
    简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）
    复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
    扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）
    间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
    可读性很重要（优美的代码是可读的）
    即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）
    
    不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）
    
    当存在多种可能，不要尝试去猜测
    而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）
    虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido ）
    
    做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
    
    如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）
    
    命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
```
### 基础语法
- 缩进来表示代码块的嵌套关系
- 单行注释：`#` 多行注释： `""" """`
- 空行的重要性，代码段之间有空行，Python之禅

### 基础数据类型
- 数值类型
    - 整数 各种进制 `0 八` `0x 十六` `0b 二`
    - 浮点数 `1.2e2` `13.34e-2`
    - 复数  `3+4j` `0.1-0.5j`
- 布尔型
    - 0或0.0 :看成false
    - `""` `''` :false
    - () [] {} :false
- 字符串
    - 单引号 双引号: 单行字符串
    - 三引号 多行字符串
- 空值 None

### virtualenv
> [廖雪峰 virtualenv](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000)

`sudo apt install python3-venv`

- 创建环境 `python3 -m venv web` 或者 `virtualenv --no-site-packages web` 不将系统中安装的包带入该环境
- 启动环境 `source web/bin/activate`
    - 在环境中使用的pip python 都是环境中的, 其实就是修改了系统的环境变量指向
- 停用环境 `deactivate`

### pip
> [pip](https://pip.readthedocs.io/en/stable/) | Python的包管理器

> [doc](https://pip.pypa.io/en/stable/reference/pip_install/)
#### Requirements files
> [pip官方文档 Requirements files](https://pip.readthedocs.io/en/1.1/requirements.html)

1. 导出 `pip freeze > requirements.txt` _这个命令会将当前环境安装的包全部列出来, 适合env环境下使用_
    - 如果没有使用虚拟环境, 然后只想导出某项目的依赖 [Github pipreqs](https://github.com/bndr/pipreqs)
    - 安装 : `pip install pipreqs` 然后 `pipreqs /path/to/project`
2. 使用 `pip install -r requirements.txt`

#### 发布包到 pypi
> [Official : about package](https://packaging.python.org/guides/distributing-packages-using-setuptools/?highlight=pypirc#id78)

`$HOME/.pypirc`
```
[pypi]
username = <username>
password = <password>
```

pip3 install wheel twine 

rm -rf dist build *.egg-info

python3 setup.py bdist_wheel
twine upload dist/*

*******************************
## 变量
- 局部变量：
- 全局变量：定义在函数外的变量，也称公用变量，函数中 `global x` 声明引用全局变量x
## 基本运行结构
- 输入输出：
    - input("") 默认当成字符串输入 数值：int() 强转一下
    - print("")
        - 输出不带换行  print('', '', end='')
- 选择：
    - if elif else
- for循环：
    - `for in ` `while ` 例如：`for i in range(1,10,2):`  范围 [1,10) 增量为2
    - pass 语句，当某个子句没有任何操作，，用pass保持程序结构完整性 不影响下一句 不像continue
- while 循环;
    - `while True:`` while ‘2’ in nums:`` while num<2:`  
    - `while 列表: ` 直到列表为空退出循环

```python
    if (b==0) and (a==1) :
        pass
        print("pass")
    else:
        print("Hi")
```

### 序列
`序列通用操作（包含：字符串，列表，元组）`
- `​索引`，从左至右：`0,1,2...n` 从右至左：`-1,-2...-n`
- `切片`（截取序列的部分） `temp[:]` 返回一个副本
    - `temp[2:4]`就是`[2,4)` 
    - `temp[1:]`1到最后 `temp[-3:]` *[-3,-1]*
    - `temp[:4]` *[0,4)* `temp[:-3]` *[0,-3]*
- `加 `：lista+listb 直接连接
- `乘`：lista*4
- `判断是否存在`：`in` `not int`
- len() 
- min() max() sum() 要求元素全是数值

*****
#### 列表
- 元素可包含 字符串，浮点，整型，列表，布尔
- 操作：
    - 增加 + ，`append()/extend()`尾部加入元素/列表  `insert(index, "")` 元素插入到任意位置,其后元素后移
    - 检索 count() in 
    - 删除 ：`del list[2] `/ `remove("apple")` /`pop(index) index为空指最后一个`
    - 永久性排序：sort() a-z ` sort(reverse=True) z-a` 列表全是字符串才可
    - 临时性排序：sorted() 也可以使用上面的参数   列表全是字符串才可
    - 永久性的逆序列表:reverse() 
- 类似数组的操作，例如声明数组：[参考博客](http://blog.csdn.net/minsenwu/article/details/7872679)
    - 原始的定义就是 lists = [1, 2, 4]
    - 若要定义连续列表 lists = range(0, 100) 得到的是range对象不是列表对象
    - 若要定义大小1000全为0列表 lists = [0 for x in range(0, 1000)]
- 二维数组的定义：
    - 原始： lists = [[1, 2], [3, 4]]
    - 仿造一维的定义： lists = [[0 for x in range(10)] for y in range(10)] 10*10 初始为0的列表
    - 简便但是不可行的方法： lists = [[0]*10]*10 这是个坑， 只是声明了一维数组，然后多次引用， 虽然看起来是二维， 引用数据就会发现是一维  

#### 元组
- 元组和列表类似但是元组是创建不可更改的 
    - 和列表相比，相同点：按定义的顺序排序，负索引一致，可以使用分片
    - 不同点：元组使用的是()，不能增加删除元素，没有index方法但是有in，可以在字典中作为键,列表不可以
    - 由于具有写保护，代码安全，操作速度略快列表
- 操作：
    - 访问： 和列表一样的索引和分片，
    - 连接：+ 连接得到新的元组
    - 删除：del 删除整个元组

*****
#### 字符串
- str() 将对象转化成字符串 （注：Python中不能像Java一样字符串和数值直接+）
- repr() 注意和str()的区别
- `r"d:\python27\"` r前缀表示转义字符看成普通字符
- 因为Python字符串实现是类似字符数组，`temp = "python" temp[0]` 结果：p `temp.index("p")` 结果是：0
- 操作：
    - `index('s')` 找到s字符的下标
    - `find('s',[start,end])` 找s的下标，只有一个整数参数则是start
    - `replace('s','v')` 替换
    - `count('sd')` 计数
    - `split('')` 正则切分 空参数默认是空格
    - `join('')` 列表转化成字符串的方法
    - `cmp(str1,str2)` 比较两个字符串是否相等
    - `+`  进行拼接 可以拼接字符串 列表
    - `a in b` 判断a是否在b里存在
    - `*` 重复序列  例如 `print "-"*20` 就会输出20个 - 
    - `b = "www.github.com" `  `c = b.split(".")` `"#".join(c)` 实现了将字符串的 . 换成了#
    - `"i am %s %d" % ("python",67)  `%s %d %f 和C语言一样占位符
        - 新的方式 `"i am {0} {1} ..".format(23,"ret")`  
        - 或者`"i am {name} {age} ..".format(age=23,name="ret")`
        - 字典方式 
    - `title()` 首字母大写 

****
`字符串，列表，元组相互转换：`
- 字符串-列表 ： list("python")
- 字符串-元组 ： tuple("python")
- 列表或元组-字符串 join(obj) 参数是列表或元组类型，其元素只能是字符串类型


***************************************
#### 字符串编码问题(python2问题)
> [ Python 3的bytes/str之别 ](http://www.ituring.com.cn/article/1116)

![str和bytes的关系](https://raw.githubusercontent.com/Kuangcp/ImageRepos/masters/Tech/python/str_bytes.jpeg)

- 解码 `encode("utf-8")`： str -> bytes
- 编码 `decode()`： bytes -> str

```python
    # coding:utf-8
    unicode_str = unicode('使用',encoding='utf-8')
    print unicode_str.encode('utf-8')
```

```python
    import codecs
    codecs.open('filename',encoding='utf-8')
```
- 因为文件不是UTF8：`UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb9 in position 2: invalid start byte `

*************************************
#### 字典（键值对）
- 通过用空间来换取时间，与列表相比，键的增加不影响查找插入速度，需要占用大量内存 
- 特性：
    - 值是可以是任意的，甚至是字典嵌套
    - 键必须不可变，只能由 数值，字符串，元组，不能用列表
- 操作：
    - 定义字典 dict={}
    - 添加 ： `dict['a'] = 2323 `
    - 返回所有key：keys() 
    - 查询是否有这个键 ：has_key() 
    - get() keys() values() 
    - 转化元组并返回 ：items() 
    - 删除指定键：del() `del dict['name']` 
    - 删除所有：clear() 
    - 删除指定键并返回值 ：pop() 
    - 合并另一个字典：update() 
    - in 

- 嵌套：
    - 字典套列表 `{'d':['we','e']}` 
    - 列表套字典，当成普通类型包含即可
    - 字典套字典
    
- [ ] 字典的排序问题

### 运算符
- 算术运算符
    - 加减一样，`*` 乘,不仅可以用于数字，还可以用于字符串 ，`/` 除，和Java不一样，整数相除也会得到浮点数
    - `//` 取整除，得到商的整数部分 ，`%` 取余数 ，`**` 幂运算 可以用来开根
- 关系运算符
    - 都是和Java一致
- 逻辑运算符
    - and or not 
- 身份运算符 
    - is : `a is b` 就是比较 id(a) id(b) 相同则是返回1
    - is not 比较id 不相同返回1

- 位运算符
    - `<< >>` 左右移 
    - ` & | `按位与或
    - `^  ~` 按位异或 按位翻转 
- 算术运算符优先级 `** / // % +`
    - // 取整数部分除法
    - ** 幂运算
- 转义字符：
    - \a 响铃
    - \b  退格 backspace
    - \000  空
    - \f   换页
    - \  续行符（行尾）


### 模块
> [参考博客](http://blog.csdn.net/hansel/article/details/8975663)

- 关于同级，子级目录是比较方便的，涉及到上级目录的就麻烦点了

************
## 输入输出
### 输入
### 输出
- python3 `print('Hi')`
    - 格式化输出 `print("%10s - %-10s"%(name, addr))`
    - print会默认追加换行符, 取消需要参数 `end=''`
```python
def show_help():
    start='\033[0;32m'
    end='\033[0m'
    print("%-26s %-20s"%(start+"-h"+end, "帮助"))
```

- python2 `print 'Hi'`

### 读取命令行参数
> [参考博客](http://www.sharejs.com/codes/python/6121)

`只有输入参数，没有选项`
```python
    import sys
    print("脚本名：", sys.argv[0])
    for i in range(1, len(sys.argv)):
        print("参数", i, sys.argv[i])
```
`python tree.py hi op ` 顺序是python，第一个参数是文件，之后才是别的参数
 结果>> `脚本名 tree.py 参数1 hi 参数2 op`

`有选项`
`getopt.getopt(args, options[, long_options])`
```python
    import sys, getopt
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
    for op, value in opts:
    
```
- `sys.argv[1:]`为要处理的参数列表，`sys.argv[0]`为脚本名，所以用`sys.argv[1:]`过滤掉脚本名。
- `"hi:o:"`: 当一个选项只是表示开关状态时，即后面不带附加参数时，在分析串中写入选项字符。当选项后面是带一个附加参数时，在分析串中写入选项字符同时后面加一个":"号。
    - 所以"hi:o:"就表示"h"是一个开关选项(单单的-h)；"i:"和"o:"则表示后面应该带一个参数。
- 调用getopt函数。函数返回两个列表：`opts和args`。opts为分析出的格式信息。args为不属于格式信息的剩余的命令行参数。
    - opts是一个两元组的列表。每个元素为：(选项串,附加参数)。如果没有附加参数则为空串''。
    - getopt函数的第三个参数[, long_options]为可选的长选项参数，上面例子中的都为短选项(如-i -o)
- 长选项格式举例:
    - `--version`
    - `--file=error.txt`
- 让一个脚本同时支持短选项和长选项 `getopt.getopt(sys.argv[1:], "hi:o:", ["version", "file="]) `

#### docopt
> [Github地址](https://github.com/docopt/docopt) | 在脚本头部添加文档来实现读取参数的便捷
会读取输入返回字典对象,可以很方便的读取输入的参数,但是需要书写大量文档, 适合参数比较多的时候,一眼过去简洁明了

#### Python Fire
> [Github地址](https://github.com/google/python-fire)快速的简洁的生成CLI
> 不过要自己书写帮助文档输出,小量参数的话,开发十分的便利 可以和类一起,也可以和方法一起

```python
import fire
def main(action=None):
    print(action)
    if action == '-h':
        show_help()
       
fire.Fire(main)
// 使用时 py filename.py -h  
```
*****************************************
## 函数

- 形参赋值传递方式
    - 按位置 `就是直接用看起来和Java一样，但不是按类型和位置，只是位置`
    - 按指定名称 调用的时候 `create(name='df')`
    - 缺省默认值（参数缺省之后，调用可以不传这个参数，否则必须要传） `def create(name='df')`
    - 列表类型，不想形参改变实参 传递副本过去即可 `list[:]`
    
- `以下两种情况（* 和 **），都必须放在形参列表的最后 (两者同时使用时：* 只能在 ** 前 )`
    - 多个实参 `create(age, *name)` `create(12, 's','d')`
        - 所以这是名为name的`元组` 不能指定没有的名称 错误：create(12，d=2, 2,3,4)
    - 多个指定名称实参 `create(age, **name)` `create(12, name='d', lo=23)` 
        - 必须要指定名称 这是名为name的键值对`字典`
        - 错误：create(12,d=23,3,3,3)
    - 注意：
        - `def hi(name, age=0, *names, **s)` `hi('d', 23,34, d=6) ` age会被赋值23
        - `def hi(name, *names, age=0, **s)` `hi('d', 23,34, d=6)` 这样写age就不会赋值，除非指定名称 age=23

- 返回值
    - 返不返回 看需求 没有像Java一样的强制性约束类型

- 将函数写在一个py文件里，然后导入 `import 文件名`，名曰导入模块
    -  还可以加别名 `import creat as fun` 给模块加别名
    -  导入指定的函数 `from create import create_aliens, type_button` 多个就，分隔 同理 as给函数加别名 * 通配所有
- 注意：递归深度，Python中递归默认深度是 989， 要么更改实现，要么就 `sys.setrecursionlimit(10000000)`


*******************
## 类
`Python 不存在多态，存在鸭子类型` [博客介绍](http://blog.csdn.net/shangzhihaohao/article/details/7065675)
- 写在一个py文件里，默认构造器，可以加参数 `def __init__(self):`

- 属性：
    - 实例属性 形如`self.name`，在任何方法中声明过即可
    - 类属性 不加self前缀，`__name`私有的类属性， 类不能访问对象属性
    - 类属性可以修改，但是实际上只能修改实例属性（这个修改只是声明了同名的实例属性，引用的时候就会覆盖类属性，看起来就是修改了
        - 可以删除实例属性，然后就能看到原有的类属性了 

```python
    class People:
        name = 'md'
    p = People()
    p.name = 'gh' # 声明了实例属性覆盖了类属性
    del p.name # 删除实例属性，恢复类属性引用
```
- 方法：
    - 对象方法，类方法，静态方法
    - 对象方法，同样的 `__`开头是私有的，只能在对象的公有方法中`self.__`引用
    - 静态方法，之中只能引用类成员，不能访问对象成员

- 构造函数和析构函数：
    - `def __init__(self)`
    - `def __del__(self)`

```python
    class Person:
        # 对象方法， 将对象作为参数self传进去
        def say(self):
            print('hi')
        # 静态方法
        @staticmethod
        def drink():
            print('static method')
        # 类方法，将类作为参数cls传进去
        @classmethod
        def eat(cls):
            print('class method')
```

- self 代表了自身引用 类似Java的this
- 特别不舒服 __init__ 这种命名 不像Java的构造函数重载，这个就是后面覆盖前面定义的__init__ 不管形参列表
    - 因为不存在重载，就是说不能多个构造函数的书写了。。。

- 导入和函数一样 注意继承中类的依赖

#### 继承
- Python是支持多重继承的

- 同文件 父类定义要在子类之前
- 父类的构造器不会自动调用，需要显式使用父类构造器：
    - 2.×版本： `super(子类名, self).__init__(参数)`
    - 3.×版本： `super().__init__(参数)`
    - 或者 `父类名.__init__()`

- 重写父类方法：只需要定义一个和父类方法同名的方法即可，因为没有多态，覆盖时形参不作考虑    

- 多态：
    - 方法重载： 子类覆盖父类的方法
    - 运算符重载： 加`__add__(self, x)` 减`__sub__(self, x)`

******************************************
## 异常
```python
    try:
        print(5/0)
    except ZeroDivisionError as err:
        print("0 不能做除数", err)
    else:
        print("成功")
    finally:
        print('finally')
```
- 基本语法 `try except else finally`
    - else是无异常执行
    - 有异常就执行 except， except 超类Exception，也可以多个except （和Java一致）
    - 最终执行finally 和 Java的结构是一致的

| except 分句使用形式 |  说明 |
| :--- | :---|
|except | 捕获所有类型|
|except name| 只捕获指定类型|
|except name, value|捕获指定类型，并获得抛出的异常对象|
|except (name1, name2)|捕获列出的异常|
|except (name1, name2), value |捕获列出的异常，获得抛出的异常对象|

- raise 语句 和Java的throw关键字 一致 ， 不过raise只是抛出一个通用异常类型 Exception
- dir(exceptions) 查看所有异常类型
    - raise name 手动引发异常
    - raise name,data 传递一个附加的数据
- 同样的也是可以自定义异常类型的，`class MyExcetion(Exception):`
- with 语句 在异常处理中，将 try except finally 关键字以及与资源分配释放相关的代码省略掉。
    - 文件打开 `with open('a.py') as files:`

| 常见异常类 | 描述 |
|:---|:---|
|NameError/UnboundLocalError | 引用不存在的变量/或者引用在声明之前|
|ZeroDivisionError|除数为0|
|SyntaxError|语法错误|
|IndexError|索引错误|
|KeyError|使用不存在的字典关键字|
|IOError|输入输出错误|
|ValueError|搜索列表中不存在的值|
|AtrributeError|调用不存在的方法|
|TypeError|未强制转换就混用数据类型|
|EOPError|文件结束标识错误|

*****************
## 文件操作
- 注意路径，Windows系统中要使用反斜杠 \ 
- 最简单：`file = open('')` 只读打开
- `使用with来操作 好处是Python自动关闭文件`
```python
    with open('filename') as name: 
        name.read()
```
- 为写打开新文本文件只读 `file = open('a.txt','w+'[,coding='utf-8'])` 打开删空
- `file.write('')`
- `os模块`
    - `os.rename('filename1','filename2') ` mv 
    - `os.remove('filename.py')` rm
    - `os.listdir(path)` ls 
    - `os.getcwd()` pwd
    - `os.makedirs(r'path')` mkdir
    - `os.chdir('')` 改变一个目录
    - `os.rmdir('')` 删除该目录，前提是空目录

- `os.path模块`
    - abspath('') 获取绝对路径
    - exists('') 是否存在
    - isdir('') 是否是一个目录
    - isfile('')  是否是文件
    - islink('') 是否是软链接硬链接文件
    - getsize() 获取文件尺寸

- shutil模块
    - dir() 复制单个文件
    - shultil.copytree(r'',r'') 复制目录树 

`b 表示字节流（二进制文件） 不加表示字符流（文本文件）`

|方式   |意义   |当存在   |当不存在   |
|:-----:|:-----:|:------:|:-----:|
|r   |只读打开   |打开   |返回空指针 |
|w   |只写打开新  |打开删空 |新建打开  |
|a   |追加打开   |打开   |新建打开  |
|r+  |读打开可写  |打开   |返回空指针  |
|w+  |写打开新可读 |打开删空 |新建打开  |
|a+  |追加打开可读 |打开   |新建打开  |
|rb  |只读打开   |打开   |返回空指针 |
|wb  |只写打开新  |打开删空 |新建打开  |
|ab  |追加打开   |打开   |新建打开  |
|rb+ |读打开可写  |打开   |返回空指针 |
|wb+ |写打开新可读 |打开删空 |新建打开  |
|ab+ |追加打开可读 |打开   |新建打开  |

### JSON
```python
    alien = {'color': 'green', 'age': '23'}
    files = 'a.json'
    with open(files, 'w') as o:
        json.dump(alien, o)
    data = json.load(files)
    # 引用
    data['root']['name']
```
- json.dump()持久化 和 load() 装载

### conf或者ini
> [参考博客: python操作ini文件](https://www.oschina.net/code/snippet_782578_14344)

```python
    import os
    from configparser import ConfigParser

    path = os.path.split(os.path.realpath(__file__))[0]
    mainConf = path + '/main.conf'
    cf = ConfigParser()
    cf.read(mainConf)
    host = cf.get('redis', 'host')

    # 写 但是要有write节点
    cf.set('write', 'add', '12')
    cf.write(open(mainConf, 'r+'))
    ```
    _对应的conf_
    ```conf
        [redis]
        host=127.0.0.1
```
******************************
## 测试
- 文件名test开头就当做是测试类，不会直接运行
- 类继承 unittest.TestCase, 所有test_开头的方法都将自动运行
- 断言 self.assertEqual assertNotEquals assertIn(item, list)
- 直接运行 unittest.main()
- 输出结果，`. 测试通过` `E 测试运行错误` `F 测试断言不通过`

************
## 数据库
### MySQL
- python3环境下： `sudo apt install python3-mysqldb`
- `sudo apt install libmysqlclient-dev`
- `sudo pip install mysql-python`


### Redis
_安装模块_
- python2 `sudo pip install redis`
- python3 `sudo pip3 install redis`

_使用_
- 使用的接口方法是和redis一样的
    - [Redis笔记传送门](/Database/Redis.md)

## 部署
### Docker部署
> [参考官方文档](https://hub.docker.com/_/python/)
Create a Dockerfile in your Python app project
```dockerfile
    FROM python:3
    WORKDIR /usr/src/app
    COPY requirements.txt ./
    RUN pip install --no-cache-dir -r requirements.txt
    COPY . .
    CMD [ "python", "./your-daemon-or-script.py" ]
```
_or (if you need to use Python 2)_
```dockerfile
    FROM python:2
    WORKDIR /usr/src/app
    COPY requirements.txt ./
    RUN pip install --no-cache-dir -r requirements.txt
    COPY . .
    CMD [ "python", "./your-daemon-or-script.py" ]
```
- You can then build and run the Docker image:
    - $ docker build -t my-python-app .
    - $ docker run -it --rm --name my-running-app my-python-app

********************
## 绘图 
### matplotlib
`python 3.5 安装`
```sh
    sudo apt install python3-matplotlib 
    sudo apt install python3.5-dev python3.5-tk tk-dev
    sudo apt install libfreetype6-dev g++
```

********
## 常见函数

- `id()` 查看内存地址
- `help(方法名)` 展示方法的说明文档
- `dir(对象)` 展示对象的方法API

******************************
## 常见库
### 内置库
- `codecs` 编码

- `os` 操作系统相关API
    - 获取脚本绝对路径  `os.path.split(os.path.realpath(__file__))[0]`
    - 获取用户目录 `os.environ['HOME']` | `os.path.expandvars('$HOME')` | `os.path.expanduser('~')`

- `subprocess` [代码](https://gitee.com/kcp1104/codes/9ytejo7fl2xmqsr5zwkv380)

#### 时间处理

_time_
> [参考博客: Python 日期和时间](http://www.runoob.com/python/python-date-time.html)
### 三方库
- `redis` 和Redis命令完美融合
- `httpie` HTTP方便的交互 [doc](https://httpie.org/doc)
    - POST时 特别注意:`参数==值`
- [python-excel](http://www.python-excel.org/)
- `python-docx` [文档](https://python-docx.readthedocs.io/en/latest/)
- `chef` [文档](https://docs.chef.io/resource_python.html) `Use the python resource to execute scripts using the Python interpreter`

********************
## QT
- 在Terminal中输入:sudo apt-get install qt4-dev-tools qt4-doc qt4-qtconfig qt4-demos qt4-designer
```
    qt4-dev-tools 中包括了Qt Assistant,Qt Linguist,Qt Creator
    qt4-doc 这个是帮助文档
    qt4-qtconfig Qt的配置工具,这个装好默认好
    qt4-demos 官方的一些Demo
    qt4-designer 可视化窗体设置工具
```
