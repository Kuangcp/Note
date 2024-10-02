---
title: IDEA
date: 2018-11-14 21:29:09
tags: 
    - IDEA
categories: 
    - Java
    - IDE
---

💠

- 1. [IDEA 使用笔记](#idea-使用笔记)
    - 1.1. [常用技巧](#常用技巧)
        - 1.1.1. [Tomcat的使用](#tomcat的使用)
        - 1.1.2. [导出为可运行JAR](#导出为可运行jar)
        - 1.1.3. [Springboot热加载](#springboot热加载)
        - 1.1.4. [Debug](#debug)
    - 1.2. [常用配置](#常用配置)
    - 1.3. [IDEA快捷键](#idea快捷键)
        - 1.3.1. [默认快捷键](#默认快捷键)
        - 1.3.2. [个人习惯](#个人习惯)
            - 1.3.2.1. [File](#file)
            - 1.3.2.2. [Coding](#coding)
            - 1.3.2.3. [Extract](#extract)
            - 1.3.2.4. [Jump](#jump)
            - 1.3.2.5. [Search](#search)
            - 1.3.2.6. [View](#view)
            - 1.3.2.7. [Setting](#setting)
    - 1.4. [常用插件](#常用插件)
        - 1.4.1. [HTTP Client](#http-client)
- 2. [运行优化](#运行优化)
- 3. [Tips](#tips)
    - 3.1. [使用项目外配置文件](#使用项目外配置文件)
    - 3.2. [Error:Cannot compile Groovy files](#errorcannot-compile-groovy-files)
    - 3.3. [无法启动fcitx输入中文](#无法启动fcitx输入中文)
- 4. [Datagrip](#datagrip)
    - 4.1. [Datagrip时区问题](#datagrip时区问题)

💠 2024-10-02 22:33:00
****************************************

# IDEA 使用笔记
> [Doc](https://www.jetbrains.com/help/idea/getting-started.html)  

> [学生授权申请方式](https://sales.jetbrains.com/hc/zh-cn/articles/207154369)

> [IDEA Tutorial](https://github.com/judasn/IntelliJ-IDEA-Tutorial)
> [W3C idea 教程](https://www.w3cschool.cn/intellij_idea_doc/intellij_idea_doc-q3ke2coy.html)

## 常用技巧
1. 鼠标方法上悬停显示javadoc  勾选 General -> show quick documentation on mouse move 
1. 自定义 TODO 等标签 Editor -> TODO, 照已有的 TODO FIXME 新建一个即可 

### Tomcat的使用
> 直接配置解压的即可, 然后Idea会在 用户目录下的Idea主目录中配置一个专门放Tomcat的配置和日志等文件, 和原Tomcat进行了隔离, 这样就不会影响到该Tomcat.

### 导出为可运行JAR
- File -> project structure ->artifact 里面设置好 引入的库，设置Main类，引用的jar包的相对classpath
- Build artifact -> Build
- Maven或者Gradle的话直接就能得到，不过也要配置一下main

### Springboot热加载
> 每个project都是一个新的工作区，所以要重新配置 | [howto-hotswapping](https://docs.spring.io/spring-boot/docs/current/reference/html/howto-hotswapping.html)

- Ctrl Shift A 快捷搜索 automatically 在Build下的 Compiler，勾选 `Build project automatically` 自动构建
    -  (如果旁边有提示说不会在运行和debug执行, 那么就要勾选并行)  `Compile independent modules in parallel`
- **Ctrl Shift A** 快捷搜索 Registry 进入后找到 compiler.automake.allow.when.app.running 勾选
- 加入devtools依赖 | [DevTools的官方文档](https://docs.spring.io/spring-boot/docs/current/reference/html/using-boot-devtools.html#using-boot-devtools)

************************

### Debug
> debug还是比较强大的, 会在行末显示这一行的变量值

- [在Intellij IDEA中使用Debug](http://www.cnblogs.com/chiangchou/p/idea-debug.html)

_横排的八个按钮_
| 操作 | 备注 |
|:----|:----|
|`Show Execution Point (Alt + F10)`|       如果你的光标在其它行或其它页面，点击这个按钮可跳转到当前代码执行的行。
|`Step Over (F8)`                  |       步过，一行一行地往下走，如果这一行上有方法不会进入方法。
|`Step Into (F7)`                  |       步入，如果当前行有方法，可以进入方法内部，一般用于进入自定义方法内，不会进入官方类库的方法，如第25行的put方法。
|`Force Step Into (Alt + Shift + F7)`|     强制步入，能进入任何方法，查看底层源码的时候可以用这个进入官方类库的方法。
|`Step Out (Shift + F8)`           |       步出，从步入的方法内退出到方法调用处，此时方法已执行完毕，只是还没有完成赋值。
|`Drop Frame (默认无)`              |       回退断点，后面章节详细说明。
|`Run to Cursor (Alt + F9)`        |       运行到光标处，你可以将光标定位到你需要查看的那一行，点击按钮,代码会运行至光标行，而不需要打断点。
|`Evaluate Expression (Alt + F8)`  |       计算表达式，后面章节详细说明。  

_竖向的七个按钮_

| 操作 | 备注 |
|:----|:----|
|`Rerun 'xxxx'`                         |重新运行程序，会关闭服务后重新启动程序。  |
|`Update 'tech' application (Ctrl + F5)`|更新程序，一般在你的代码有改动后可执行这个功能。而这个功能对应的操作则是在服务配置里，如图2.3。  |
|`Resume Program (F9)`                  |恢复程序，比如，你在第20行和25行有两个断点，当前运行至第20行，按F9，则运行到下一个断点(即第25行)，再按F9，则运行完整个流程，因为后面已经没有断点了。  |
|`Pause Program`                        |暂停程序，挂起所有线程 |
|`Stop 'xxx' (Ctrl + F2)`               |连续按两下，关闭程序。有时候你会发现关闭服务再启动时，报端口被占用，这是因为没完全关闭服务的原因，你就需要查杀所有JVM进程了。  |
|`View Breakpoints (Ctrl + Shift + F8)` |查看所有断点，后面章节会涉及到。  |
|`Mute Breakpoints`                     |哑的断点，选择这个后，所有断点变为灰色，断点失效，按F9则可以直接运行完程序。再次点击，断点变为红色，有效。如果只想使某一个断点失效，可以在断点上右键取消Enabled  |

**个人思考**
1. 当断点 F8 步过 到一行代码后, 这个方法没有抛出异常结束, idea的面板上的属性, 断点状态都没了, 只有一个 app is running 。
    - 那很有可能是线程陷入死循环或者长久的锁/IO等待，后面的代码也不会执行了, 所以代码才会没按预期的调用链执行，可通过间隔一段时间的两次jstack 查看目标线程的栈，确认该问题

*************************

## 常用配置
**自定义类文件头**
- 依次找到配置项: `File->settings->Editor->File and Code Templates->`
    - 如果自己要每个文件都单独设置头部, 就依次点击Class Interface Enum ...进行设置
        - [参考博客](https://segmentfault.com/q/1010000005997550)
    - 如果要统一设置 就点击Includes标签, 选择File Header
_例如修改为如下_
```java
/**
 * Created by https://github.com/kuangcp
 * @author kuangcp
 * @date ${DATE}  ${TIME}
 */
```

**自定义模板**
在 `Setting -> Editor -> Live Templates` 设置项下可以看到已有的配置

1. `$SELECTION$` surrounding with 功能标记
1. `$END$` 光标结束位置

************************

- 关闭特定文件的自动格式化 Code Style -> Formatter 中设置 *.md *.sql

************************

> 个人IDEA配置
- 代码字体 
    1. Fira Code Retina 14 0.9
    1. IBM Plex Mono SemiBold 15 0.9 
- 设置字体
    1. Robot Mono Medium for Powershell 14 
    1. Cascadia Code

[IDEA 自定义配置](https://github.com/Kuangcp/Configs/tree/master/IDEA)
- colors 代码配色方案
- keymaps 快捷键映射
- temlates 代码模板

************************
## IDEA快捷键
> [参考: Intellij IDEA神器居然还有这些小技巧](https://my.oschina.net/samgege/blog/1808622)  
> 如果一时不习惯idea, 可以在 设置中 的keymap 选择eclipse系列即可

### 默认快捷键
> 可以在 Help -> Keymap Reference 看到内置PDF文档   
> `个人觉得最简单就是打开 Setting -> keymap -> Find Action by shortcut, 任意的按键, 然后查看对应的内容` 

| Ctrl  | Shift | Alt | Key | Action |
|:----: |:----:|:----:|:----:|:----|
|C| | | `E` |可以显示最近编辑的文件列表 |
| |S| | `鼠标左击` | 可以关闭文件|
|C|S| | `Backspace` | 可以跳转到上次编辑的地方|
|C| | | `F12` |可以弹窗显示当前文件中类的结构(快速跳转方法和属性)|
|C| | | `F7` | 可以查询当前元素在当前文件中的引用，然后按F3可以选择|
|C| | | `N` | 可以快速打开类|
|C|S| | `N` | 可以快速打开文件|
| | |A| `Q` | 可以看到光标处的元素的Javadoc|
|C| | | `W` | 可以选择单词继而语句继而行继而函数|
| | |A| `F1` | 可以将正在编辑的元素在各个面板中定位|
|C| | | `P` | 可以显示参数信息|
|C|S| | `Insert` | 可以选择剪贴板内容并插入|
| | |A| `Insert` | 可以生成构造器/Getter/Setter等|
| |S|A| `Insert` | 进入/退出 列编辑模式 |
|C| |A| `V` | 重构代码, 将选中的代码抽离出称为一个变量 Variable |
|C| |A| `T` | 可以把代码包在一块内，例如try/catch|
| | |A| `Up/Down` | 可在方法间快速移动|
| |S| | `Escape` | 不仅可以把焦点移到编辑器上而且还可以隐藏当前（或最后活动的）工具窗口。|
|C|S| | `左/右` | 调节以上窗口分隔线|
|C|S| | `Enter` | 就能自动补全代码的分号,括号|
|C| | | `Space` | 代码提示|
|C| |A| `Space` | 代码提示 包括类,变量,方法等内容|
|C|S| | `Space` | 智能提示|
|C| | | `P` | 方法参数提示|
| | |A| `F1` | 查找当前文件所在位置(项目,结构,maven等等)|
|C|S| | `F7` | 要先选中文本然后按键 高亮显示所有该文本，按Esc高亮消失。|
| | |A| `F3` | 要先选中文本然后按键，然后 F3逐个往下查找相同文本，并高亮显示。|
|C| | | `B` | 快速打开光标处的类或方法的 _声明或调用_|
|C| |A| `B` | 查看抽象类或接口的实现方法 等价的,B键 可以换成鼠标左键单击|
|C|S|A| `N` | 可以快速打开符号(方法名, 变量名等等,全局搜索)|
|C| | | `O` | 可以选择父类的方法进行重写|
| |S| | `Shift` | 也就是双击, 就可以快速搜索类了|
|C|S| | `F` |全局搜索, 不含Shift 就是简单当前文件搜索- 快速打开类/文件/符号时，可以使用通配符，也可以使用缩写|
|C| | | `J` | Live Templates!  例如 fori 等快速模板代码|
|C|S| | `F7` | 可以高亮当前元素在当前文件中的使用|
|C| |A| `Up/Down` | 可以快速跳转搜索结果|
|C|S| | `J` | 可以整合两行|
| | |A| `F8` | 是计算变量值|

******
1. `Ctrl Enter`, 如果光标在一行的中间, 可以迅速让光标跳转到下一行
1. 在调试程序时查看任何表达式值的一个容易的方法就是在编辑器中选择文本（可以按几次 `Ctrl-W` 组合键更有效地执行这个操作）然后按 `Alt-F8` 。
1. 要打开编辑器脱字符处使用的类或者方法 Java 文档的浏览器，就按 `Shift-F1` （右键菜单的 External JavaDoc ）。
1. 要使用这个功能须要把加入浏览器的路径，在“ General ”选项中设置（ Options | IDE Settings ），另外还要把创建的 Java 文档加入到工程中（ File | Project Properties ）。

**************************************************************************

### 个人习惯
> 从eclipse风格继承而来和原生Idea快捷键结合, 自己修改的风格, 如果需要, 则在[个人配置文件夹](https://github.com/Kuangcp/Configs/tree/master/Idea)下找到对应的jar导入即可  
> 个人的习惯特点是左手完成大部分快捷键的任务, 因为还没习惯脱离鼠标工作  

| Ctrl | Shift | Alt | Key | Action |
|:----:|:----:|:----:|:----:|:----|
| | |A| `Enter` | 自动修复|
|C| | | `Q`  | 显示javadoc|
|C| | | `B` | 显示定义或者调用|
|C| |A| `B` | 显示其实现|
| | |A| `U` | 面板显示调用处 |
|C|S| | `T` | 自动创建或跳转 Test|
|C|S| | `F7` | 高亮显示光标所在元素所有出现过的地方(就是搜索)|
|C| |A| `L` | 快速格式化代码 |
|C| |A| `O` | 优化导入的类和包|
|C| | | `Esc` | 格式化并优化导入|
| | |A| `Esc` | 停止正在运行的运行项|
| | |A| `1` | 运行上次的运行项|
| |S|A| `1` | 显示运行项面板|
| | |A| `2` | Debug上次的运行项|
| |S|A| `2` | 显示Debug运行项面板|
| | | | `F10` | 运行光标所在处的运行项|
| |S|A| `F10` | 运行选择的运行项|
| |S|A| `F9` | Debug选择的运行项|

#### File 
| Ctrl | Shift | Alt | Key | Action |
|:----:|:----:|:----:|:----:|:----|
|C| | | `W` | 选中代码 |
|C| | | `E` | 显示最近打开的文件 |
| | |A| `E` | 显示最近打开的文件 |
| |A|S| `C` | 最近更改的文件|
|C| | | `N` | 快速搜索类 |
|C|S| | `N` | 搜索所有文件|
|C|S|A| `N` | 按文件内容字符的搜索,也能按类名首字母搜索|
| | |A| `左/右` | 左右切换打开的文件|
|C| | | `鼠标左键` | 在文件标签页上单击, 即可在文件管理器中打开该文件 |
||S|A| `S` |保存当前窗口的context|
||S|A| `L` |加载保存过的context|
||S|A| `X` |清除当前所有窗口的context|

#### Coding
> [Doc: 2018.2](https://www.jetbrains.com/help/idea/2018.2/using-code-editor.html?utm_content=2018.2&utm_medium=link&utm_source=product&utm_campaign=IU)

| Ctrl | Shift | Alt | Key | Action |
|:----:|:----:|:----:|:----:|:----|
| | |A| `C` | build 项目|
|C|S| | `V` | 显示最近的粘贴板记录|
|C| | | `O` | 选择要重写的方法|
|C| | | `I` | 选择要实现的方法 |
|C| |A| `Insert` |  生成代码(如get,set方法,构造函数等)|
| |S|A| `K` |  重命名|
|C| | | `X` |  剪切一行|
|C| | | `D` |  删除一行|
|C| | | `Y` |  复制一行到下一行|
|C| | | `Q` |  显示注释文档 或者 Alt+鼠标中键|
|C|S| | `Space` |  智能提示代码的补全|
| |S|A| `上/下` |  `代码行`上/下移动|
|C|S| | `上/下` |  `代码块`上/下移动 |
|C| | | `J` |  提示代码片段 也就是 `Live Templates` |
| | |A| `J` |  选中字符 Add Selection for Next Occurence|
|C| | | `J` |  提示 Live Templates |
|C| |A| `J` |  提示 Surround Live Templates |
|C| | | `Space` |  智能补全|
|C|S| | `Space` |  结合上下文补全|
|C| | | `W` |  选中代码，连续按会有其他效果|
|C|S| | `U` | 选中字符大小写转换 |
| |S|A| `3` | 查看方法完整调用链 |


#### Extract
| Ctrl | Shift | Alt | Key | Action |
|:----:|:----:|:----:|:----:|:----|
|C| |A| `T` | 根据选中代码(或者光标前的代码片段)**包裹 在块中** 例如try/catch if for ...|
|C| |A| `J` | 根据选中代码(或者光标前的代码片段)**包裹在自定义的模板中**|
|C| |A| `M` | 根据选中代码(或者光标前的代码片段)抽离成 **函数** |
|C| |A| `V` | 根据选中代码(或者光标前的代码片段)抽离成 **变量** 自定义为 `C A S J`|
|C| |A| `C` | 根据选中代码(或者光标前的代码片段)抽离成 **常量**|
|C| |A| `F` | 根据选中代码(或者光标前的代码片段)抽离成 **属性**|
|C| |A| `P` | 根据选中代码(或者光标前的代码片段)抽离成 **方法参数**|
|C|S|A| `P` | 根据选中代码(或者光标前的代码片段)抽离成 **函数式方法参数**|

#### Jump
| Ctrl | Shift | Alt | Key | Action |
|:----:|:----:|:----:|:----:|:----|
| | |A| `上/下` | 在方法间快速移动定位|
|C| |A| `左/右` | 后退/前进 至光标的上一个位置|
|C| | | `,` | 高亮错误或警告快速定位 组合 Shift 前进, 原为F2|
|C| | | `[ ]` | 可以跳到大括号的开头结尾|
| | |A| `S` | 跳转类的方法或属性|

#### Search
| Ctrl | Shift | Alt | Key | Action |
|:----:|:----:|:----:|:----:|:----|
|C| | | `N` | 查找类(所有类范围,包括引用的包)|
| | |A| `L` | 查找类 `原默认是 Ctrl N`|
| | |A| `I` | 查找文件名|
|C| | | `R` | 替换文本|
|C| | | `F` | 查找文本|
|C|S| | `F` | 全局搜索字符串|
| | |A| `K` | 查找任意文件`原默认是双击Shift` |

#### View 
| Ctrl | Shift | Alt | Key | Action |
|:----:|:----:|:----:|:----:|:----|
|C|S| | **左/右** | 调节以上工具窗口与编辑器窗口的分隔线位置|
| |S|A| `H` | 显示/隐藏 所有工具窗口|
|C| |A| **;** | 关闭活跃中的Tab|
|C| | | `H` | 生成类结构图并显示|
| | |A| `H` | 类结构图窗口|
| | |A| `A` | 目录结构窗口|
| | |A| `X` | Run窗口|
| | |A| `D` | Debug窗口|
| | |A| `T` | TODO的窗口 `Ctrl +/-` 显示和折叠TODO|
| | |A| `G` | Gradle窗口|
| | |A| `M` | Maven窗口|
| | |A| `Z` | Spring窗口|
| | |A| `V` | VCS窗口|
| | |A| `N` | 导航至文件所在目录等...|
| | |A| `3` | 数据库工具窗口|
| | |A| `.` | 终端窗口|
| |S|A| `V` | 数据库 Console 窗口|

> 在任一工具窗口, 按`ESC`都会让焦点回到编辑器 `Shift ESC` 就能关闭工具窗口并让焦点回到编辑器
> 以上的窗口都是默认显示小bar的, 我为了窗口更大就设置为了默认隐藏, 如果想显示, 可以双击Alt, 在第二下按住不动, 鼠标就能进行点击了  

#### Setting
| Ctrl | Shift | Alt | Key | Action |
|:-:|:-:|:-:|:-:|:--|
|C|S| | `A` | 搜索设置项的位置|
|C|S|A| `?` | 进行一些关键设置 |

**Tips**
- 代码模板 Live Template (**fori** **notnull**...) 输入完成后，按Tab或者Enter，生成代码。

*********************
## 常用插件
1. Atom Material Icons
1. rainbow brackets 将括号变成彩色, 更方便查看
1. Alibaba Java Code Guideline
    - 阿里巴巴的代码规范插件
    - [《阿里巴巴Java开发规约》IDEA插件与Eclipse插件使用指南](https://zhuanlan.zhihu.com/p/30191998)
1. TestMe 快速创建测试类
1. TestNG 测试框架的集成
1. Junit4 Parallel Runner 并行执行单元测试
1. lombok
    - 插件商店中搜索 lombok 安装重启idea即可
    - 配置 Build,Execution > Compiler > Annotation Processors 勾选上即可使用lombok的注解
1. Jrebel 热部署插件, 需要付费
1. GoogleTranslation **Ctrl Alt 1** 快速翻译选中的单词和语句
1. FindBugs
1. Docker
1. Kubernates
1. Maven helper
1. Maven Project Version 快速修改整个项目所有模块的版本号
1. Grep console 控制台搜索工具
1. Code with me 远程协作插件
1. jclasslib Bytecode Viewer 字节码查看插件
1. JarEditor Jar包编辑，无需解压
1. GsonFormatPlus ： json转Class定义
1. POJO to JSON ： Class定义转JSON
1. Sequence Diagram 查看代码时序图

**************************
> 内置插件
- 为了节省内存, 禁用无关插件, 把插件列表中所有插件全看一遍

1. haml haml语言, HTML的抽象化语言
1. Gherkin Gherkin是Cucumber用于定义测试用例的语言。
    1. cucumber java
    1. cucumber groovy

### HTTP Client
[Jetbrain Help](https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html)

1. 登录设置 cookie
    ```sh
    POST http://localhost/coolsoftware/rest/authentication?login=username&password=1234
    > {% client.global.set("yourVariable", response.headers.valueOf('Set-Cookie')); %}
    
    按实际情况来设置，例如 提取接口返回(JSON类型)中的 data 字段：
    > {% client.global.set("token", response.body.data); %}
    ```

**********************

# 运行优化
> [官网文档](https://www.jetbrains.com/help/idea/increasing-memory-heap.html)
> [IntelliJ IDEA 内存优化最佳实践](http://blog.oneapm.com/apm-tech/426.html)

> [参考: 记一次idea性能调优](http://www.cnblogs.com/nevermorewang/p/10061377.html)  

- 如果有 node_modules 等大量文件的目录， 可以右键该目录设置忽略这个目录的文件索引

************************

# Tips

## 使用项目外配置文件
IDEA中Java项目启动时Console里灰色被折叠的第一行是完整的Java命令，可以复制出classpath参数，在头部追加自定义目录，然后把这一长串填回到VM Options中
就能实现自定义目录下的文件对IDEA中classpath下的同名文件替换

## Error:Cannot compile Groovy files
> Error:Cannot compile Groovy files: no Groovy library is defined for module "XXX"

1. Project Structure -> 找到 XXX 项目 右击 -> Add -> 选择 Groovy

## 无法启动fcitx输入中文
1. 启动脚本 idea.sh 头部追加 `source ~/.xpfrofile`

`~/.xpfrofile`
```sh
export XMODIFIERS=@im=fcitx
export QT_IM_MODULE=fcitx
```

# Datagrip
> 执行SQL时底部的耗时拆分为 execution fetching。 
- execution: JDBC提交Statement执行，到返回ResultSet的耗时
- fetching： 读取ResultSet全部数据的耗时

> 大批量执行DDL语句时，卡顿
- 由于特性设计是DDL执行后Datagrip会自动去拉库的元数据更新到本地，当有大批量的DDL要执行时（例如删除一批表），每一条DDL的执行都会有一个执行结果tab加上元数据的更新，Datagrip就会越来越卡直到卡死

## Datagrip时区问题
> [DataGrip设置时区](https://blog.csdn.net/qiaominghe/article/details/82757206)

`-Duser.timezone=Asia/Shanghai`
