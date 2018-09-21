`目录 start`
 
- [TestNG](#testng)
    - [使用](#使用)
        - [基本注解](#基本注解)

`目录 end` |_2018-08-23_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# TestNG
> [Official Doc](http://testng.org/doc/documentation-main.html) 

> [易百: TestNG教程](https://www.yiibai.com/testng/)  
> [TestNG 入门教程](http://www.cnblogs.com/TankXiao/p/3888070.html) 
> [testNG官方文档](http://testng.org/doc/index.html) | [Github:TestNG](https://github.com/cbeust/testng)  
> [tools](http://toolsqa.com/selenium-webdriver/testng-introduction/)

## 使用
> 基本使用
**Gradle使用**
```groovy
testCompile group: 'org.testng', name: 'testng', version: '6.14.3'
```
然后和Junit使用是一致的, 在方法上打上 @Test 注解即可运行`注意Test注解的包为 import org.testng.annotations.Test;`


### 基本注解
1. @Test

