`目录 start`
 
- [Lombok](#lombok)
    - [何为Lombok](#何为lombok)
    - [为什么要用](#为什么要用)
    - [为什么不要用](#为什么不要用)
    - [个人见解](#个人见解)
- [配置](#配置)
    - [Maven](#maven)
        - [普通Java项目](#普通java项目)
        - [Groovy和Java项目使用Lombok](#groovy和java项目使用lombok)
- [使用](#使用)
    - [注解使用](#注解使用)
        - [POJO常用](#pojo常用)
        - [日志相关](#日志相关)
        - [异常相关](#异常相关)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Lombok

## 何为Lombok
> [Lombok Project 官网](https://projectlombok.org/) | [Github : ](https://github.com/rzwitserloot/lombok)

## 为什么要用
> 简化JavaBean 更为直观 省去了Setter Getter toString hashCode 构造器等方法  
> 一定有人就会跳出来说 在IDE中几个快捷键的事情,何必这么复杂, 
>> 那他们一定是没有遇到修改的时候吧, 改个属性的名字,类型, 对应的方法你需要改吧, 但是使用lombok就不用担心了

## 为什么不要用
> 暂时还没有想到

## 个人见解
> Lombok在IDE中安装插件是为了编译和构建中能够动态的添加Getter Setter 等方法, 而在Maven或者Gradle中添加是为了注解能够引用得到??

# 配置
## Maven
> [官方文档](https://projectlombok.org/setup/maven)
### 普通Java项目
```xml
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>2.3.2</version>
        <configuration>
          <source>1.8</source>
          <target>1.8</target>
          <encoding>UTF-8</encoding>
        </configuration>
      </plugin>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <configuration>
          <skip>true</skip>
        </configuration>
      </plugin>
      <plugin>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok-maven-plugin</artifactId>
        <version>1.16.8.0</version>
        <executions>
          <execution>
            <phase>generate-sources</phase>
            <goals>
              <goal>delombok</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
```
```xml
    <dependency>
      <groupId>org.projectlombok</groupId>
      <artifactId>lombok</artifactId>
      <version>1.16.10</version>
    </dependency>
```
而static有还是有可能被new出多个实例的
### Groovy和Java项目使用Lombok

_配置编译插件_
```xml
<!--lombok-->
<plugin>
<artifactId>maven-compiler-plugin</artifactId>
<version>3.7.0</version>
<configuration>
    <target>1.8</target>
    <source>1.8</source>
    <encoding>UTF-8</encoding>
    <compilerId>groovy-eclipse-compiler</compilerId>
    <verbose>true</verbose>
    <fork>true</fork>
    <compilerArguments>
    <javaAgentClass>lombok.launch.Agent</javaAgentClass>
    </compilerArguments>
</configuration>
<dependencies>
    <dependency>
    <groupId>org.codehaus.groovy</groupId>
    <artifactId>groovy-eclipse-compiler</artifactId>
    <version>2.9.3-01</version>
    </dependency>
    <dependency>
    <groupId>org.codehaus.groovy</groupId>
    <artifactId>groovy-eclipse-batch</artifactId>
    <version>2.5.0-01</version>
    </dependency>
    <dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.16.10</version>
    </dependency>
</dependencies>
</plugin>
```
_添加依赖_
```xml
    <dependency>
      <groupId>org.projectlombok</groupId>
      <artifactId>lombok</artifactId>
      <version>1.16.10</version>
    </dependency>
```

# 使用
- Lombok 注解在线帮助文档：http://projectlombok.org/features/index.

## 注解使用
### POJO常用
- `@Data` ：注解在类上；提供类所有属性的 getter 和 setter 方法，此外还提供了equals、canEqual、hashCode、toString 方法
- `@Setter`：注解在属性上；为属性提供 setter 方法
- `@Getter`：注解在属性上；为属性提供 getter 方法
- `@NoArgsConstructor`：注解在类上；为类提供一个无参的构造方法
- `@AllArgsConstructor`：注解在类上；为类提供一个全参的构造方法

### 日志相关
1. @Log4j
1. @Log4j2
1. @Slf4j `用上logback, 但是这个不是一个接口规范么` TODO 

### 异常相关
1. [@SneakyThrows](https://projectlombok.org/features/SneakyThrows)


