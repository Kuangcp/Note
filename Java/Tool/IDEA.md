`目录 start`
 
- [IDEA 使用笔记](#idea-使用笔记)
    - [常识](#常识)
    - [常用技巧](#常用技巧)
        - [Tomcat的使用](#tomcat的使用)
        - [导出为可运行的JAR包 普通Java项目](#导出为可运行的jar包-普通java项目)
        - [Springboot热加载](#springboot热加载)
        - [Debug](#debug)
    - [常用配置](#常用配置)
        - [个人IDEA配置](#个人idea配置)
    - [IDEA快捷键](#idea快捷键)
        - [默认快捷键](#默认快捷键)
        - [个人习惯](#个人习惯)
            - [File](#file)
            - [Coding](#coding)
            - [Extract](#extract)
            - [Jump](#jump)
            - [Search](#search)
            - [View](#view)
            - [Setting](#setting)
    - [常用插件](#常用插件)
    - [启动配置](#启动配置)
    - [Tips](#tips)
        - [Error:Cannot compile Groovy files: no Groovy library is defined for module "XXX"](#errorcannot-compile-groovy-files-no-groovy-library-is-defined-for-module-"xxx")

`目录 end` |_2018-08-29_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************

# IDEA 使用笔记
> [学生授权申请方式](https://sales.jetbrains.com/hc/zh-cn/articles/207154369) | [click](http://idea.lanyus.com/)
> [rover12421博客](http://ju.outofmemory.cn/feed/2608/?page=1) | [IDEA主题](http://www.riaway.com/index.php)

## 常识
-  project 就是一个工作空间，一个Module就是一个项目
- 新建一个empty项目可以作为一个工作空间，放很多module,新建的时候不要选中任何目录，*光标选中JRE库*，再菜单栏点击File然后new，
    - 不然项目结构很乱, 会在光标停留的文件夹下新建module
- 一个项目一个空间也是可以的，就是跨项目查看代码会有点麻烦，而且每个项目的IDEA的配置都是不一样的，同样的配置可能要配置很多遍

- 在新版中提供的load unload 模块功能,必须要重启idea, 才能让maven生效 emmm


## 常用技巧
1. 鼠标方法上悬停显示javadoc  勾选 General -> show quick documentation on mouse move 
1. 自定义 TODO 等标签 Editor -> TODO, 照已有的 TODO FIXME 新建一个即可 

### Tomcat的使用
> 直接配置解压的即可, 然后Idea会在 用户目录下的Idea主目录中配置一个专门放Tomcat的配置和日志等文件, 和原Tomcat进行了隔离, 这样就不会影响到该Tomcat.

### 导出为可运行的JAR包 普通Java项目
- File -> project structure ->artifact 里面设置好 引入的库，设置Main类，引用的jar包的相对classpath
- Build artifact -> Build
- Maven或者Gradle的话直接就能得到，不过也要配置一下main

### Springboot热加载
> 每个project都是一个新的工作区，所以要重新配置 | [howto-hotswapping](https://docs.spring.io/spring-boot/docs/current/reference/html/howto-hotswapping.html)

- Ctrl Shift A 快捷搜索 automatically 在Build下的 Compiler，勾选 `Build project automatically` 自动构建
    -  (如果旁边有提示说不会在运行和debug执行, 那么就要勾选并行)  `Compile independent modules in parallel`
- **Ctrl Shift A 快捷搜索 Registry 进入后找到 compiler.automake.allow.when.app.running 勾选
- 加入devtools依赖 | [DevTools的官方文档](https://docs.spring.io/spring-boot/docs/current/reference/html/using-boot-devtools.html#using-boot-devtools)

*********************************
### Debug
> debug还是比较强大的, 会在行末显示这一行的变量值

- [在Intellij IDEA中使用Debug](http://www.cnblogs.com/chiangchou/p/idea-debug.html)

_横排的八个按钮_
> `Show Execution Point (Alt + F10)`：如果你的光标在其它行或其它页面，点击这个按钮可跳转到当前代码执行的行。  
> `Step Over (F8)`：步过，一行一行地往下走，如果这一行上有方法不会进入方法。  
> `Step Into (F7)`：步入，如果当前行有方法，可以进入方法内部，一般用于进入自定义方法内，不会进入官方类库的方法，如第25行的put方法。  
> `Force Step Into (Alt + Shift + F7)`：强制步入，能进入任何方法，查看底层源码的时候可以用这个进入官方类库的方法。  
> `Step Out (Shift + F8)`：步出，从步入的方法内退出到方法调用处，此时方法已执行完毕，只是还没有完成赋值。  
> `Drop Frame (默认无)`：回退断点，后面章节详细说明。  
> `Run to Cursor (Alt + F9)`：运行到光标处，你可以将光标定位到你需要查看的那一行，点击按钮,代码会运行至光标行，而不需要打断点。  
> `Evaluate Expression (Alt + F8)`：计算表达式，后面章节详细说明。  

_竖向的七个按钮_
> Rerun 'xxxx'：重新运行程序，会关闭服务后重新启动程序。  
> Update 'tech' application (Ctrl + F5)：更新程序，一般在你的代码有改动后可执行这个功能。而这个功能对应的操作则是在服务配置里，如图2.3。  
> Resume Program (F9)：恢复程序，比如，你在第20行和25行有两个断点，当前运行至第20行，按F9，则运行到下一个断点(即第25行)，再按F9，则运行完整个流程，因为后面已经没有断点了。  
> Pause Program：暂停程序，启用Debug。目前没发现具体用法。  
> Stop 'xxx' (Ctrl + F2)：连续按两下，关闭程序。有时候你会发现关闭服务再启动时，报端口被占用，这是因为没完全关闭服务的原因，你就需要查杀所有JVM进程了。  
> View Breakpoints (Ctrl + Shift + F8)：查看所有断点，后面章节会涉及到。  
> Mute Breakpoints：哑的断点，选择这个后，所有断点变为灰色，断点失效，按F9则可以直接运行完程序。再次点击，断点变为红色，有效。如果只想使某一个断点失效，可以在断点上右键取消Enabled  

**个人思考**
1. 当断点 F8 步过 到一行代码后, 这个方法没有抛出异常什么的, idea的面板上的那些属性, 断点什么的都没了, 只有一个 app is running , 这个意思就是这行代码还在执行中, 很有可能就是死循环...
    - 没有断点的时候, 也就是说这个死循环一直挂在这边, 不会被回收, 后面的代码也被阻塞了, 所以代码才诡异的不符合自己构想的调用链执行

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

**自定义缩写模板**
在 `Setting -> Editor -> Live Templates` 设置项下可以看到已有的配置, 新建一个即可


### 个人IDEA配置
- 字体Fira Code Retina 14 0.9

************************
## IDEA快捷键
> [参考博客: Intellij IDEA神器居然还有这些小技巧](https://my.oschina.net/samgege/blog/1808622)  
> 如果一时不习惯idea, 可以在 设置中 的keymap 选择eclipse系列即可

### 默认快捷键
> 可以在 Help -> Keymap Reference 看到内置PDF文档   
> `个人觉得最简单就是打开 Setting -> keymap -> Find Action by shortcut, 任意的按键, 然后查看对应的内容`

| Ctrl | Shift | Alt | Key | Action |
|:----:|:----:|:----:|:----:|:----|
|C| | | **E** |可以显示最近编辑的文件列表
| |S| | **鼠标左击** | 可以关闭文件
|C|S| | **Backspace** | 可以跳转到上次编辑的地方
|C| | | **F12** |可以弹窗显示当前文件中类的结构(快速跳转方法和属性)
|C| | | **F7** | 可以查询当前元素在当前文件中的引用，然后按F3可以选择
|C| | | **N** | 可以快速打开类
|C|S| | **N** | 可以快速打开文件
| | |A| **Q** | 可以看到光标处的元素的Javadoc
|C| | | **W** | 可以选择单词继而语句继而行继而函数
| | |A| **F1** | 可以将正在编辑的元素在各个面板中定位
|C| | | **P** | 可以显示参数信息
|C|S| | **Insert** | 可以选择剪贴板内容并插入
| | |A| **Insert** | 可以生成构造器/Getter/Setter等
|C| |A| **V** | 重构代码, 将选中的代码抽离出称为一个变量 Variable 
|C| |A| **T** | 可以把代码包在一块内，例如try/catch
| | |A| **Up/Down** | 可在方法间快速移动
| |S| | **Escape** | 不仅可以把焦点移到编辑器上而且还可以隐藏当前（或最后活动的）工具窗口。
|C|S| | **左/右** | 调节以上窗口分隔线
|C|S| | **Enter** | 就能自动补全代码的分号,括号
|C| | | **Space** | 代码提示
|C| |A| **Space** | 代码提示 包括类,变量,方法等内容
|C|S| | **Space** | 智能提示
|C| | | **P** | 方法参数提示
| | |A| **F1** | 查找当前文件所在位置(项目,结构,maven等等)
|C|S| | **F7** | 要先选中文本然后按键 高亮显示所有该文本，按Esc高亮消失。
| | |A| **F3** | 要先选中文本然后按键，然后 F3逐个往下查找相同文本，并高亮显示。
|C| | | **B** | 快速打开光标处的类或方法的 _声明或调用_
|C| |A| **B** | 查看抽象类或接口的实现方法 等价的,B键 可以换成鼠标左键单击
|C|S|A| **N** | 可以快速打开符号(方法名, 变量名等等,全局搜索)
|C| | | **O** | 可以选择父类的方法进行重写
| |S| | **Shift** | 也就是双击, 就可以快速搜索类了
|C|S| | **F** |全局搜索, 不含Shift 就是简单当前文件搜索- 快速打开类/文件/符号时，可以使用通配符，也可以使用缩写
|C| | | **J** | Live Templates!  例如 fori 等快速模板代码
|C|S| | **F7** | 可以高亮当前元素在当前文件中的使用
|C| |A| **Up/Down** | 可以快速跳转搜索结果
|C|S| | **J** | 可以整合两行
| | |A| **F8** | 是计算变量值

******
1. 在调试程序时查看任何表达式值的一个容易的方法就是在编辑器中选择文本（可以按几次 **Ctrl-W 组合键更有效地执行这个操作）然后按 Alt-F8 。
1. 要打开编辑器脱字符处使用的类或者方法 Java 文档的浏览器，就按 Shift-F1 （右键菜单的 External JavaDoc ）。
1. 要使用这个功能须要把加入浏览器的路径，在“ General ”选项中设置（ Options | IDE Settings ），另外还要把创建的 Java 文档加入到工程中（ File | Project Properties ）。

**************************************************************************

### 个人习惯
> 从eclipse风格继承而来和原生Idea快捷键结合, 自己修改的风格, 如果需要, 则在[个人配置文件夹](https://github.com/Kuangcp/Configs/tree/master/Idea)下找到对应的jar导入即可
> 个人的习惯特点是左手完成大部分快捷键的任务, 因为还没习惯脱离鼠标工作  

| Ctrl | Shift | Alt | Key | Action |
|:----:|:----:|:----:|:----:|:----|
| | |A| **Enter** | 自动修复
|C| | | **Q**  | 显示javadoc
|C| | | **B** | 显示定义处或者调用处
|C|S| | **T** | 自动创建或跳转 Test
|C|S| | **F7** | 高亮显示光标所在元素所有出现过的地方(就是搜索)
|C| |A| **L** | 快速格式化代码 
|C| |A| **O** | 优化导入的类和包
|C| | | **Esc** | 格式化并优化导入
| | |A| **Esc** | 停止正在运行的运行项
| | |A| **1** | 运行上次的运行项
| | |A| **2** | Debug上次的运行项
| | | | **F10** | 运行光标所在处的运行项
| |S|A| **F10** | 运行选择的运行项
| |S|A| **F9** | Debug选择的运行项

#### File 
| Ctrl | Shift | Alt | Key | Action |
|:----:|:----:|:----:|:----:|:----|
|C| | | **W** | 选中代码 |
|C| | | **E** | 显示最近打开的文件 |
| | |A| **E** | 显示最近打开的文件 |
| |A|S| **C** | 最近更改的文件|
|C| | | **N** | 快速搜索类 |
|C|S| | **N** | 搜索所有文件|
|C|S|A| **N** | 按文件内容字符的搜索,也能按类名首字母搜索|
| | |A| **左/右** | 左右切换打开的文件|
|C| | | **鼠标左键** | 在文件标签页上单击, 即可在文件管理器中打开该文件 |

#### Coding
> [Doc: 2018.2](https://www.jetbrains.com/help/idea/2018.2/using-code-editor.html?utm_content=2018.2&utm_medium=link&utm_source=product&utm_campaign=IU)

| Ctrl | Shift | Alt | Key | Action |
|:----:|:----:|:----:|:----:|:----|
| | |A| **C** | build 项目
|C|S| | **V** | 显示最近的粘贴板记录
|C| | | **O** | 选择要重写的方法
|C| | | **I** | 选择要实现的方法 
|C| |A| **Insert** |  生成代码(如get,set方法,构造函数等)
| |S|A| **K** |  重命名
|C| | | **X** |  剪切一行
|C| | | **D** |  删除一行
|C| | | **Y** |  复制一行到下一行
|C| | | **Q** |  显示注释文档 或者 Alt+鼠标中键
|C|S| | **Space** |  智能提示代码的补全
| |S|A| **上/下** |  代码上/下移动
|C|S| | **上/下** |  代码上/下移动 | `光标在一行上就是移动一行, 光标在代码块的首行就是移动整个代码块`
|C| | | **J** |  提示代码片段 也就是 Live Template
| | |A| **J** |  选中字符
|C| | | **Space** |  智能补全
|C|S| | **Space** |  结合上下文补全
|C| | | **W** |  选中代码，连续按会有其他效果
|C|S| | **U** | 选中字符大小写转换


#### Extract
| Ctrl | Shift | Alt | Key | Action |
|:----:|:----:|:----:|:----:|:----|
|C| |A| **T** | 根据选中代码(或者光标前的代码片段)**包裹 在块中** 例如try/catch if for ...
|C| |A| **J** | 根据选中代码(或者光标前的代码片段)**包裹在自定义的模板中**
|C| |A| **M** | 根据选中代码(或者光标前的代码片段)抽离成 **函数** 
|C| |A| **V** | 根据选中代码(或者光标前的代码片段)抽离成 **变量** 自定义为 `C A S J`
|C| |A| **C** | 根据选中代码(或者光标前的代码片段)抽离成 **常量**
|C| |A| **F** | 根据选中代码(或者光标前的代码片段)抽离成 **属性**
|C| |A| **P** | 根据选中代码(或者光标前的代码片段)抽离成 **方法参数**
|C|S|A| **P** | 根据选中代码(或者光标前的代码片段)抽离成 **函数式方法参数**

#### Jump
| Ctrl | Shift | Alt | Key | Action |
|:----:|:----:|:----:|:----:|:----|
| | |A| **上/下** | 在方法间快速移动定位
|C| |A| **左/右** | 后退/前进 至光标的上一个位置
| | | | **F2** | 高亮错误或警告快速定位 组合 Shift 前进
|C| | | [ ] | 可以跳到大括号的开头结尾
| | |A| **S** | 跳转类的方法或属性

#### Search
| Ctrl | Shift | Alt | Key | Action |
|:----:|:----:|:----:|:----:|:----|
|C| | | **N** | 查找类(所有类范围,包括引用的包)
| | |A| **L** | 查找类 `原默认是 Ctrl N`
|C|S| | **N** | 查找文件名
|C|S|A| **N** | 符号查找: 类中的方法或变量
|C| | | **R** | 替换文本
|C| | | **F** | 查找文本
| | |A| **K** | 查找任意文件`原默认是双击Shift` 

#### View 
| Ctrl | Shift | Alt | Key | Action |
|:----:|:----:|:----:|:----:|:----|
|C| | | **H** | 生成类结构图并显示
| | |A| **H** | 类结构图窗口
| | |A| **A** | 目录结构窗口
| | |A| **X** | Run窗口
| | |A| **D** | Debug窗口
| | |A| **T** | TODO的窗口 `Ctrl +/-` 显示和折叠TODO
| | |A| **G** | Gradle窗口
| | |A| **M** | Maven窗口
| | |A| **Z** | Spring窗口
| | |A| **V** | VCS窗口
| | |A| **N** | 定位当前文件在目录结构的位置
| | |A| **3** | 数据库工具窗口
| | |A| **.** | 终端窗口
| |S|A| **V** | 数据库 Console 窗口
|C|S| | **左/右** | 调节以上工具窗口与编辑器窗口的分隔线位置

> 在任一工具窗口, 按`ESC`都会让焦点回到编辑器 `Shift ESC` 就能关闭工具窗口并让焦点回到编辑器
> 以上的窗口都是默认显示小bar的, 我为了窗口更大就设置为了默认隐藏, 如果想显示, 可以双击Alt, 在第二下按住不动, 鼠标就能进行点击了  

#### Setting
| Ctrl | Shift | Alt | Key | Action |
|:-:|:-:|:-:|:-:|:--|
|C|S| | **A** | 搜索设置项的位置
|C|S|A| **?** | 进行一些关键设置 

**Tips**
- 代码模板 Live Template (**fori** **notnull**...) 输入完成后，按Tab或者Enter，生成代码。

*********************
## 常用插件
1. Alibaba Java Code Guidelineshuo
    - 阿里巴巴的代码规范插件
    - [《阿里巴巴Java开发规约》IDEA插件与Eclipse插件使用指南](https://zhuanlan.zhihu.com/p/30191998)

1. TestMe
    - 快速创建测试类

1. TestNG
    - TestNG 测试框架的集成

1. lombok
    - 插件商店中搜索 lombok 安装重启idea即可
    - 配置 Build,Execution > Compiler > Annotation Processors 勾选上即可使用lombok的注解

1. Jrebel
    - 热部署插件, 需要付费
    
1. GoogleTranslation
    - **Ctrl Alt 1** 快速翻译选中的单词和语句

1. http-client
    - https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html

1. Docker
1. Kubernates
1. Maven helper
1. rainbow brackets 将括号变成彩色, 更方便查看

**************************

> 内置插件
- 为了节省内存, 禁用无关插件, 把插件列表中所有插件全看一遍

1. haml haml语言, HTML的抽象化语言
1. Gherkin Gherkin是Cucumber用于定义测试用例的语言。
    1. cucumber java
    1. cucumber groovy

**********************
## 启动配置
> [官网文档](https://www.jetbrains.com/help/idea/increasing-memory-heap.html)
> [IntelliJ IDEA 内存优化最佳实践](http://blog.oneapm.com/apm-tech/426.html)


## Tips

### Error:Cannot compile Groovy files: no Groovy library is defined for module "XXX"
1. Project Structure -> 找到 XXX 项目 右击 -> Add -> 选择 Groovy

