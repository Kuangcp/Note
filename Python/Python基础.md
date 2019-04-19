# 1， 运行

## 1, 直接运行源程序

- 指定使用python执行 `python test.py`

- 在源代码中指定Python的程序 `#!/usr/bin/python` 并赋予可执行权限， 然后执行 `test.py`

## 2， 字节代码（源代码编译后生成的后缀为pyc文件）

```
# 编译方法
import py_compile
py_compile.compile("test.py")
```

## 3， 优化代码（经过优化的源文件，后缀名为'.pyo'）

- 方法 `python -O -m py_compile test.py`

# 2, 数据类型

## 1, 数字

- 整型 （范围`-2^31 ~ 2^31-1`）

- 长整型 (范围非常大， 几乎可以说任意大的整数均可存储，指定定义为长整型 `123L`)

- 浮点型 （小数）

- 复数型 （表示复数类型 `3.14j`）

## 2， 字符串 （不可变）

- 定义

  - 单引号 `‘hello’`

  - 双引号 `“hello”`

  - 三重引号 `”“”hello“”“` （也可做注释）

- 取值 （`c = 'hello' ， (index为索引)`）

  - 其中的单个值 `c[index]`

  - 取一定范围的值 `c[index0 : index1]` , 从索引1到索引2的值

  - 间隔性的取值 `c[::n]` , 表示从第一个每间隔n个取值

## 3， 列表

- 定义

  - 空列表 `l = []`

  - 含值的列表 `l = ['dragonhht', 21, 'male']`

- 取值 （可通过与字符串类似的切片取值）

- 修改 `l[1] = 18`

- 添加 `l.append("hello")`

- 删除 `del(l[3])` 或 `l.remove(l[2])`

- 查找 `'dragonhht' in l`

## 4， 元组 （不可变）

- 定义

  - 空元组 `t = ()`

  - 单个元素的元组 `t = ("dragonhht", )` , 未加逗号则为该单一元素的类型， 不是元组类型

  - 一般元组 `t = ("dragonhht", 21, "male")`

- 取值 (可通过与字符串类似的切片取值)

  - 用单个变量分别接受元组中的值 `name,age,sex = t`

## 5， 字典 （键值对）

- 定义 （还有其他方式， 具体查看API）

  - 空字典 `d = {}`

  - 含元素 `d = {'name' : "dragonhht", 'age' : 21}`

- 取值 `d['name']` ， 通过键获取值， 也可通过遍历获取

- 修改 `d['age'] = 18`

- 删除

  - 删除制定键的元素 `d.pop('age')`

  - 删除字典所有元素 `d.clear()`

  - 删除整个字典 `del d`

- 添加 `d['age'] = 21`， 直接通过新键添加元素

# 3, 流程控制

## 1， 分支结构

- 结构 (注意缩进)

```
if 表达式:
  执行语句
else:
  执行语句
```

## 2, 逻辑运算符 `and` 、`or` 和 `not`

## 3, 循环

### 1, for循环

- 语法结构

```
for var in sequence:
  执行语句
else：
  执行语句 # 循环结束后执行
```

- 循环指定次数

```
for i in range(first, last, [进步值]):
  执行语句
```

### 2, 循环控制 `break`、 `continue` 和 `pass`

### 3， while循环

- 结构

```
while 表达式:
  执行语句
```

# 4, 函数

- 结构

```
def 函数名(参数列表):
  函数体
```

# 5, 错误和异常

- 异常捕获

```
try:
    f2 = open("file/test2.txt", "w")
    f2.write("这是一个创建文件的测试")
except Exception, e:
    print "写入错误",  e
finally:
    f2.close()
```

- 使用with打开文件

```
with open("file/test2.txt", "r") as f5:
    print f5.read()
```

# 6, 文件操作

- 打开文件

```
f = open("file/test2.txt")
for line in f:
    print line,  # 后面加一个逗号，去掉原来默认增加的\n
f.close()
```

- 创建文件 （以写方式打开文件）(异常的处理)

```
try:
    f2 = open("file/test2.txt", "w")
    f2.write("这是一个创建文件的测试")
except Exception, e:
    print "写入错误",  e
finally:
    f2.close()
```

- 以只读的方式打开文件

```
f3 = open("file/test2.txt", "r")
for line in f3:
    print "\n" + line
f3.close()
```

- 以追加模式打开文件

```
f4 = open("file/test2.txt", "a")
f4.write("\n你好呀")
f4.close()
```

- 使用with打开文件

```
with open("file/test2.txt", "r") as f5:
    print f5.read()
```

- 查看文件的状态

```
file_stat = os.stat("file/test2.txt")
print file_stat
```

- 读取大文件时

```
for line in fileinput.input("file/test2.txt"):
    print line,
```

- 复制图片(以二进制模式读取文件)

```
f5 = open("file/3c28af542f2d49f7-da1566425074a021-9c373de8439e52c5d885c8459d285946.jpg", "rb")
f6 = open("file/pic.jpg", "w")
r = f5.read(1)
while r:
    f6.write(r)
    r = f5.read(1)
f5.close()
f6.close()
```

# 7， [数据库操作](https://github.com/dragonhht/PythonStudy/blob/master/mysql/__init__.py)
