`目录 start`
 
1. [问题解决方案](#问题解决方案)
    1. [Linux](#linux)
    1. [JDK](#jdk)
    1. [IDE](#ide)
        1. [IDEA](#idea)
    1. [Docker](#docker)
        1. [内存高占用](#内存高占用)

`目录 end` |_2018-11-25_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************

# 问题解决方案
## Linux 
> [详细](/Linux/Base/LinuxProblem.md)

## JDK
> `Picked up _JAVA_OPTIONS: ` 例如这样的提示, 由于设置了 _JAVA_OPTIONS 或者 JAVA_OPTIONS 就一定会输出这个提示

- [参考博客: Disabling Java_Options On Java Console Apps in Linux](https://nixmash.com/post/disabling-java_options-on-java-console-apps-in-linux)
- [参考博客: Suppressing the “Picked up _JAVA_OPTIONS” message](https://superuser.com/questions/585695/suppressing-the-picked-up-java-options-message)
- [参考博客: 理解环境变量 JAVA_TOOL_OPTIONS](https://segmentfault.com/a/1190000008545160)

但是又不能直接 unset, 这个变量似乎是用来解决字体锯齿问题的, 所以需要如下配置
```sh
_SILENT_JAVA_OPTIONS="$_JAVA_OPTIONS"
unset _JAVA_OPTIONS
alias java='java "$_SILENT_JAVA_OPTIONS"'
```
- 只需将该配置加到  `/etc/profile` 文件尾部, 这样的话, 终端不会有如上提示
- 但是IDEA中输出控制台仍带有该提示, 在 `bin/idea.sh` 中也添加如上配置即可(在最后一段之前)

*******************************
> Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=gasp
- 原因是linux自带的OpenJDK影响了安装的java, 同样的也是可以采用如上的方法, 或者:
    - `sudo mv /etc/profile.d/java-awt-font-gasp.sh /etc/profile.d/java-awt-font-gasp.sh.bak`

*************************
## IDE
### IDEA
- [调整参数，解决CPU满载](https://intellij-support.jetbrains.com/hc/en-us/articles/206544869)
    - [同样的](https://intellij-support.jetbrains.com/hc/en-us/articles/207241235)

## Docker
### 内存高占用
- 明明是一样的docker配置，构建出来的镜像按道理也应该是一样的，所以运行出来的容器也应该是一样的才对，但是结果却是两倍的差别
    - 优化jvm？
- 修改基础镜像？

- [ ] docker ps hanging on docker 1.13.2
