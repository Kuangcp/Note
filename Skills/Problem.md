`目录 start`
 
- [问题解决方案](#问题解决方案)
    - [终端](#终端)
    - [JDK](#jdk)
    - [IDE](#ide)
        - [IDEA](#idea)
    - [Docker](#docker)
        - [内存高占用](#内存高占用)
    - [Linux](#linux)
        - [Deepin](#deepin)
            - [输入法](#输入法)
                - [fcitx](#fcitx)
            - [Flash](#flash)

`目录 end` |_2018-08-21_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************

# 问题解决方案
## 终端

## JDK
> `Picked up _JAVA_OPTIONS: ` 例如这样的提示, 由于设置了 _JAVA_OPTIONS 或者 JAVA_OPTIONS 就一定会输出这个提示

- [参考博客: Disabling Java_Options On Java Console Apps in Linux](https://nixmash.com/post/disabling-java_options-on-java-console-apps-in-linux)
- [参考博客: Suppressing the “Picked up _JAVA_OPTIONS” message](https://superuser.com/questions/585695/suppressing-the-picked-up-java-options-message)
- [参考博客: 理解环境变量 JAVA_TOOL_OPTIONS](https://segmentfault.com/a/1190000008545160)

但是又不能直接 unset 这个变量似乎是用来解决字体锯齿问题的, 所以需要如下配置
```sh
_SILENT_JAVA_OPTIONS="$_JAVA_OPTIONS"
unset _JAVA_OPTIONS
alias java='java "$_SILENT_JAVA_OPTIONS"'
```
只需将该配置加到  `/etc/profile` 文件尾部, 这样的话, 终端不会有如上提示, 但是IDEA中输出控制台仍带有该提示, 这时候可以在IDEA的启动脚本 `bin/idea.sh` 中也添加如上配置即可(在最后一段之前)

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

## Linux 
### Deepin

- [FAQ](https://bbs.deepin.org/forum.php?mod=viewthread&tid=146921&extra=page%3D1)


#### 输入法
##### fcitx
- fcitx单核满载:三种（搜狗拼音导致）
    - 杀掉，fcitx -r
    - 先把进程杀掉再fcitx-autostart &
    - fcitx再fcitx-qimpanel 
`相关网页：`
- [某引擎搜索结果页](https://ausdn.com/s/ubuntu+cpu+fcitx)| [几种方式](https://www.findhao.net/res/786)| [卸载搜狗安装拼音](http://tieba.baidu.com/p/3863217434)
- [知乎问题](https://www.zhihu.com/question/19839748) | [ubuntu论坛](http://forum.ubuntu.com.cn/viewtopic.php?f=122&t=173730&p=1299087) | [ubuntu论坛](http://forum.ubuntu.com.cn/viewtopic.php?f=8&t=194486&start=0)

- 输入法没有显示打字窗口
    - 直接杀掉 sogou-qimpanel 然后点击图标进行启动

#### Flash
- 点击[官网下载地址](https://get.adobe.com/cn/flashplayer/)下载,然后解压,
- 将文件复制进火狐插件目录:`sudo cp libflashplayer.so  /usr/lib64/mozilla/plugins`
- 添加其他用户可执行权限`chmod 755 /usr/lib64/mozilla/plugins/libflashplayer.so`

