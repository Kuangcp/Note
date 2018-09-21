`目录 start`
 
- [日志系统](#日志系统)
    - [slf4j 体系](#slf4j-体系)
        - [Log4j](#log4j)
            - [问题](#问题)
        - [Log4j2](#log4j2)
        - [LogBack](#logback)
            - [Gradle中使用](#gradle中使用)
            - [配置理解](#配置理解)
                - [根节点 <configuration> 属性](#根节点-<configuration>-属性)
                - [子节点](#子节点)
                    - [设置上下文名称：<contextName>](#设置上下文名称<contextname>)
                    - [设置变量： <property>](#设置变量-<property>)
                    - [获取时间戳字符串：<timestamp>](#获取时间戳字符串<timestamp>)
                - [设置loger：](#设置loger)
                - [详解<appender>](#详解<appender>)
    - [实践经验](#实践经验)
    - [apache 体系](#apache-体系)
- [分析日志](#分析日志)
    - [Linux上查看日志](#linux上查看日志)
    - [lnav](#lnav)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 日志系统
> [码农翻身: 一个著名的日志系统是怎么设计出来的？ ](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513967&idx=1&sn=5586ce841a7e8b39adc2569f0eb5bb45&chksm=80d67bacb7a1f2ba38aa37620d273dfd7d7227667df556d36c84d125cafd73fef16464288cf9&scene=21#wechat_redirect)`深刻的理解了日志系统的来源以及相关关系`  

## slf4j 体系
> SLF4J是一套简单的日志`外观模式`的Java API，帮助在项目部署时对接各种日志实现。 只是接口设计, 以下是具体实现库

> [lombok+slf4j+logback SLF4J和Logback日志框架详解](http://www.cnblogs.com/diegodu/p/6098084.html)

> 目前来说, LogBack要好于Log4j [参考博客: 从Log4j迁移到LogBack的理由](https://blog.csdn.net/gaojian881/article/details/53957961)

- 个人体验:  logback 1.1.3 log4j 1.7.25
    - 在Java中
        - 
    - 在Groovy中
        - Log4j不能在Groovy中获取到正确的 类,方法,方法所在行 直接输出?
        - LogBack可以拿到正确的值, 但是在闭包中, 方法是混乱的
        
****************************
### Log4j
> [Log4J使用笔记](http://www.cnblogs.com/eflylab/archive/2007/01/11/618001.html)
> [log4j.properties配置详解](http://www.cnblogs.com/ITEagle/archive/2010/04/23/1718365.html)

#### 问题
> `log4j:WARN No appenders could be found for logger` 这是路径下没有对应的配置文件, 那么这时就有了神奇的事情, maven项目按道理是resources下就行了, 
> 但如果你项目配置文件自己新建目录然后再复制过去什么的, 这么瞎搞的话,虽然在ide是能运行的, 但是一大包就没用了, 那么直接把log的配置单独放在 src/main/java 下就行了

### Log4j2
> [官方文档, 配置详解](https://logging.apache.org/log4j/2.x/manual/configuration.html)
> 听说是为了解决Log4j无法在多环境使用的问题 , 也就是类似于 SpringBoot 多profile的功能

**************************
### LogBack

- [logback简单示例](https://github.com/Kuangcp/Notes/blob/master/ConfigFiles/Log/logback.xml)

> [xml to groovy config](https://logback.qos.ch/translator/asGroovy.html)


#### Gradle中使用
1. 添加依赖 `  testCompile 'ch.qos.logback:logback-classic:1.2.3'`
    - `compile 'org.projectlombok:lombok:1.16.16'`
2. 类上加注解 `@Slf4j` 然后 就能用了


#### 配置理解
> [参考博客](http://www.cnblogs.com/lixuwu/p/5811273.html)

##### 根节点 <configuration> 属性
- _scan_ : 当此属性设置为true时，配置文件如果发生改变，将会被重新加载，默认值为true。
- _scanPeriod_ : 设置监测配置文件是否有修改的时间间隔，如果没有给出时间单位，默认单位是毫秒。当scan为true时，此属性生效。默认的时间间隔为1分钟。
- _debug_ : 当此属性设置为true时，将打印出logback内部日志信息，实时查看logback运行状态。默认值为false。

```xml
    <configuration scan="true" scanPeriod="60 seconds" debug="false"> 
        <!-- 其他配置省略--> 
    </configuration> 
```
##### 子节点
###### 设置上下文名称：<contextName>
每个logger都关联到logger上下文，默认上下文名称为“default”。但可以使用`<contextName>`设置成其他名字，用于区分不同应用程序的记录。一旦设置，不能修改。
```xml
    <configuration scan="true" scanPeriod="60 seconds" debug="false">
      <contextName>myAppName</contextName>
      <!-- 其他配置省略-->
    </configuration> 
```
###### 设置变量： <property>
用来定义变量值的标签，`<property>` 有两个属性，name和value；其中name的值是变量的名称，value的值时变量定义的值。通过`<property>`定义的值会被插入到logger上下文中。
定义变量后，可以通过`${}`来使用变量。例如使用`<property>`定义上下文名称，然后在`<contentName>`设置logger上下文时使用。
```xml
    <configuration scan="true" scanPeriod="60 seconds" debug="false">
      <property name="APP_Name" value="myAppName" /> 
      <contextName>${APP_Name}</contextName>
      <!-- 其他配置省略-->
    </configuration>
```
###### 获取时间戳字符串：<timestamp>
两个属性 key:标识此`<timestamp>` 的名字；datePattern：设置将当前时间（解析配置文件的时间）转换为字符串的模式，遵循`java.txt.SimpleDateFormat`的格式。
例如将解析配置文件的时间作为上下文名称：
```xml
    <configuration scan="true" scanPeriod="60 seconds" debug="false"> 
      <timestamp key="bySecond" datePattern="yyyyMMdd'T'HHmmss"/> 
      <contextName>${bySecond}</contextName> 
      <!-- 其他配置省略--> 
    </configuration>
```
************
##### 设置loger：
- `<loger>`
    - 用来设置某一个包或者具体的某一个类的日志打印级别、以及指定`<appender>`。`<loger>`仅有一个name属性，一个可选的level和一个可选的addtivity属性。
    - `name:`
        - 用来指定受此loger约束的某一个包或者具体的某一个类。
    - `level:`
        - 用来设置打印级别，大小写无关：TRACE, DEBUG, INFO, WARN, ERROR, ALL 和 OFF，还有一个特俗值INHERITED或者同义词NULL，代表强制执行上级的级别。
        - 如果未设置此属性，那么当前loger将会继承上级的级别。
    - `addtivity:`
        - 是否向上级loger传递打印信息。默认是true。
- `<loger>`可以包含零个或多个`<appender-ref>`元素，标识这个appender将会添加到这个loger。

********
- `<root>`
    - 也是`<loger>`元素，但是它是根loger。只有一个level属性，应为已经被命名为"root".
    - `level:`
        - 用来设置打印级别，大小写无关：TRACE, DEBUG, INFO, WARN, ERROR, ALL 和 OFF，不能设置为INHERITED或者同义词NULL。
        - 默认是DEBUG。
- `<root>`可以包含零个或多个`<appender-ref>`元素，标识这个appender将会添加到这个loger。
**********
`测试类：`
```java
    public class LogbackDemo { 
        private static Logger log = LoggerFactory.getLogger(LogbackDemo.class);  
        public static void main(String[] args) {  
            log.trace("======trace");  
            log.debug("======debug");  
            log.info("======info");  
            log.warn("======warn");  
            log.error("======error");  
        }  
    } 
```
_第1种：只配置root_
```xml
    <configuration> 
        <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">   
            <!-- encoder 默认配置为PatternLayoutEncoder -->   
            <encoder>   
                <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>   
            </encoder>   
        </appender>   
        <root level="INFO">             
            <appender-ref ref="STDOUT" />   
        </root>     
    </configuration>
```
其中appender的配置表示打印到控制台(稍后详细讲解appender )；
`<root level="INFO">`将root的打印级别设置为“INFO”，指定了名字为“STDOUT”的appender。
当执行logback.LogbackDemo类的main方法时，root将级别为“INFO”及大于“INFO”的日志信息交给已经配置好的名为“STDOUT”的appender处理，“STDOUT”appender将信息打印到控制台；

_第2种：带有loger的配置，不指定级别，不指定appender_
```xml
    <configuration> 
      <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender"> 
        <!-- encoder 默认配置为PatternLayoutEncoder -->   
        <encoder>   
          <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>   
        </encoder>   
      </appender> 
      <!-- logback为java中的包 --> 
      <logger name="logback"/> 
      <root level="DEBUG"> 
        <appender-ref ref="STDOUT" />   
      </root> 
     </configuration> 
```
其中appender的配置表示打印到控制台(稍后详细讲解appender )；
`<logger name="logback" />`将控制logback包下的所有类的日志的打印，但是并没用设置打印级别，所以继承他的上级`<root>`的日志级别“DEBUG”；
没有设置addtivity，默认为true，将此loger的打印信息向上级传递；
没有设置appender，此loger本身不打印任何信息。
`<root level="DEBUG">`将root的打印级别设置为“DEBUG”，指定了名字为“STDOUT”的appender。
 
当执行logback.LogbackDemo类的main方法时，因为LogbackDemo 在包logback中，所以首先执行`<logger name="logback" />`，将级别为“DEBUG”及大于“DEBUG”的日志信息传递给root，本身并不打印；
root接到下级传递的信息，交给已经配置好的名为“STDOUT”的appender处理，“STDOUT”appender将信息打印到控制台；

_第3种：带有多个loger的配置，指定级别，指定appender_
```xml
    <configuration> 
       <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender"> 
        <!-- encoder 默认配置为PatternLayoutEncoder -->   
        <encoder>   
          <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>   
        </encoder>   
      </appender> 
      <!-- logback为java中的包 --> 
      <logger name="logback"/> 
      <!--logback.LogbackDemo：类的全路径 --> 
      <logger name="logback.LogbackDemo" level="INFO" additivity="false"> 
        <appender-ref ref="STDOUT"/>  
      </logger> 
      <root level="ERROR">
        <appender-ref ref="STDOUT" />   
      </root>
    </configuration> 
```
其中appender的配置表示打印到控制台(稍后详细讲解appender )；
 
`<logger name="logback" />`将控制logback包下的所有类的日志的打印，但是并没用设置打印级别，所以继承他的上级`<root>`的日志级别“DEBUG”；
没有设置addtivity，默认为true，将此loger的打印信息向上级传递；
没有设置appender，此loger本身不打印任何信息。
` <logger name="logback.LogbackDemo" level="INFO" additivity="false">`控制logback.LogbackDemo类的日志打印，打印级别为“INFO”；
additivity属性为false，表示此loger的打印信息不再向上级传递，
指定了名字为“STDOUT”的appender。
`<root level="DEBUG">`将root的打印级别设置为“ERROR”，指定了名字为“STDOUT”的appender。
 
 当执行logback.LogbackDemo类的main方法时，先执行`<logger name="logback.LogbackDemo" level="INFO" additivity="false">`，将级别为“INFO”及大于“INFO”的日志信息交给此loger指定的名为“STDOUT”的appender处理，在控制台中打出日志，不再向次loger的上级 `<logger name="logback"/>` 传递打印信息；
`<logger name="logback"/>`未接到任何打印信息，当然也不会给它的上级root传递任何打印信息；
*********
如果将`<logger name="logback.LogbackDemo" level="INFO" additivity="false">` 修改为 `<logger name="logback.LogbackDemo" level="INFO" additivity="true">`那打印结果将是什么呢？
没错，日志打印了两次，想必大家都知道原因了，因为打印信息向上级传递，logger本身打印一次，root接到后又打印一次

##### 详解<appender>
> <appender>是<configuration>的子节点，是负责写日志的组件。
> <appender>有两个必要属性name和class。name指定appender名称，class指定appender的全限定名。

_1.ConsoleAppender:_
把日志添加到控制台，有以下子节点：
`<encoder>`：对日志进行格式化。（具体参数稍后讲解 ）
`<target>`：字符串 System.out 或者 System.err ，默认 System.out ；
```xml
    <configuration>
      <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>  
          <pattern>%-4relative [%thread] %-5level %logger{35} - %msg %n</pattern>  
        </encoder>  
      </appender>
      <root level="DEBUG">
        <appender-ref ref="STDOUT" />  
      </root>
    </configuration> 
```
_2.FileAppender:_
- 把日志添加到文件，有以下子节点：
    - `<file>`：被写入的文件名，可以是相对目录，也可以是绝对目录，如果上级目录不存在会自动创建，没有默认值。
    - `<append>`：如果是 true，日志被追加到文件结尾，如果是 false，清空现存文件，默认是true。
    - `<encoder>`：对记录事件进行格式化。（具体参数稍后讲解 ）
    - `<prudent>`：如果是 true，日志会被安全的写入文件，即使其他的FileAppender也在向此文件做写入操作，效率低，默认是 false。
```xml
    <configuration>
      <appender name="FILE" class="ch.qos.logback.core.FileAppender"> 
        <file>testFile.log</file>  
        <append>true</append>  
        <encoder>  
          <pattern>%-4relative [%thread] %-5level %logger{35} - %msg%n</pattern>  
        </encoder>  
      </appender> 
      <root level="DEBUG"> 
        <appender-ref ref="FILE" />  
      </root> 
    </configuration> 
```
- _3.RollingFileAppender:_
    - 滚动记录文件，先将日志记录到指定文件，当符合某个条件时，将日志记录到其他文件。有以下子节点：
        - `<file>：`被写入的文件名，可以是相对目录，也可以是绝对目录，如果上级目录不存在会自动创建，没有默认值。
        - `<append>：`如果是 true，日志被追加到文件结尾，如果是 false，清空现存文件，默认是true。
        - `<encoder>：`对记录事件进行格式化。（具体参数稍后讲解 ）
        - `<rollingPolicy>:`当发生滚动时，决定 RollingFileAppender 的行为，涉及文件移动和重命名。
        - `<triggeringPolicy >:` 告知 RollingFileAppender 合适激活滚动。
        - `<prudent>：`当为true时，不支持FixedWindowRollingPolicy。支持TimeBasedRollingPolicy，但是有两个限制，1不支持也不允许文件压缩，2不能设置file属性，必须留空。
 
_rollingPolicy_
 
TimeBasedRollingPolicy： 最常用的滚动策略，它根据时间来制定滚动策略，既负责滚动也负责出发滚动。有以下子节点：
`<fileNamePattern>:`
必要节点，包含文件名及“%d”转换符， “%d”可以包含一个java.text.SimpleDateFormat指定的时间格式，如：%d{yyyy-MM}。如果直接使用 %d，默认格式是 yyyy-MM-dd。RollingFileAppender 的file字节点可有可无，通过设置file，可以为活动文件和归档文件指定不同位置，当前日志总是记录到file指定的文件（活动文件），活动文件的名字不会改变；如果没设置file，活动文件的名字会根据fileNamePattern 的值，每隔一段时间改变一次。“/”或者“\”会被当做目录分隔符。
 
`<maxHistory>:`
可选节点，控制保留的归档文件的最大数量，超出数量就删除旧文件。假设设置每个月滚动，且`<maxHistory>`是6，则只保存最近6个月的文件，删除之前的旧文件。注意，删除旧文件是，那些为了归档而创建的目录也会被删除。
 
FixedWindowRollingPolicy： 根据固定窗口算法重命名文件的滚动策略。有以下子节点：
`<minIndex>`:窗口索引最小值
`<maxIndex>`:窗口索引最大值，当用户指定的窗口过大时，会自动将窗口设置为12。
`<fileNamePattern >:`
必须包含“%i”例如，假设最小值和最大值分别为1和2，命名模式为 mylog%i.log,会产生归档文件mylog1.log和mylog2.log。还可以指定文件压缩选项，例如，mylog%i.log.gz 或者 没有log%i.log.zip
 
`triggeringPolicy:`
 
SizeBasedTriggeringPolicy： 查看当前活动文件的大小，如果超过指定大小会告知RollingFileAppender 触发当前活动文件滚动。只有一个节点:
`<maxFileSize>:`这是活动文件的大小，默认值是10MB。

_例如：每天生成一个日志文件，保存30天的日志文件。_
```xml
    <configuration> 
      <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender"> 
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">   
          <fileNamePattern>logFile.%d{yyyy-MM-dd}.log</fileNamePattern>   
          <maxHistory>30</maxHistory>    
        </rollingPolicy>   
        <encoder>   
          <pattern>%-4relative [%thread] %-5level %logger{35} - %msg%n</pattern>   
        </encoder>   
      </appender>
      <root level="DEBUG"> 
        <appender-ref ref="FILE" />   
      </root> 
    </configuration>
```
_例如：按照固定窗口模式生成日志文件，当文件大于20MB时，生成新的日志文件。窗口大小是1到3，当保存了3个归档文件后，将覆盖最早的日志。_
```xml
    <configuration> 
      <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>test.log</file>   
       
        <rollingPolicy class="ch.qos.logback.core.rolling.FixedWindowRollingPolicy">   
          <fileNamePattern>tests.%i.log.zip</fileNamePattern>   
          <minIndex>1</minIndex>   
          <maxIndex>3</maxIndex>   
        </rollingPolicy>   
       
        <triggeringPolicy class="ch.qos.logback.core.rolling.SizeBasedTriggeringPolicy">   
          <maxFileSize>5MB</maxFileSize>   
        </triggeringPolicy>   
        <encoder>   
          <pattern>%-4relative [%thread] %-5level %logger{35} - %msg%n</pattern>   
        </encoder>   
      </appender>
               
      <root level="DEBUG"> 
        <appender-ref ref="FILE" />   
      </root>
    </configuration> 
```
_4.另外还有SocketAppender、SMTPAppender、DBAppender、SyslogAppender、SiftingAppender，并不常用，这些就不在这里讲解了，大家可以参考官方文档。当然大家可以编写自己的Appender。_
 
`<encoder>：`
负责两件事，一是把日志信息转换成字节数组，二是把字节数组写入到输出流。
目前PatternLayoutEncoder 是唯一有用的且默认的encoder ，有一个`<pattern>`节点，用来设置日志的输入格式。使用“%”加“转换符”方式，如果要输出“%”，则必须用“\”对“\%”进行转义。
```xml
    <encoder>
        <pattern>%-4relative [%thread] %-5level %logger{35} - %msg%n</pattern>   
    </encoder>
```

![模式图](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/pattern_type.jpg)

## 实践经验
> [Java 调整格式日志输出](https://www.jb51.net/article/88937.htm)

1. 日志记录方式, 注意格式的正确, 否则, 错误会被隐藏
    - [Github: CorrectLog.java](https://github.com/kuangcp/JavaBase/blob/master/java-classfile/src/main/java/log/CorrectLog.java)

1. 在Springboot中还能指定包的日志等级 `logging.level.com.github.kuangcp.service = DEBUG`
************
## apache 体系
- [apache的简单示例](https://github.com/Kuangcp/Notes/blob/master/ConfigFiles/Log/log4j.xml)

# 分析日志
## Linux上查看日志
> [Linux常用的日志分析命令与工具 ](https://yq.aliyun.com/articles/388039) `其中就是使用简单的cat less awk sed`

## lnav
> 一个专门用于浏览日志文件的软件  | [官网](http://lnav.org/) | [文档](http://lnav.readthedocs.io/en/latest/)
> [博客: LNAV：基于 Ncurses 的日志文件阅读器 ](https://linux.cn/article-6677-1.html)

