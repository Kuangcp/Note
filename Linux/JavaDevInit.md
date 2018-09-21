`目录 start`
 
- [配置Deepin的Java开发环境](#配置deepin的java开发环境)
    - [新增用户](#新增用户)
    - [安装Docker](#安装docker)
- [在Linux上配置Java环境](#在linux上配置java环境)
    - [配置JDK](#配置jdk)
        - [解压配置](#解压配置)
        - [sdkman方式](#sdkman方式)
        - [mythsdk](#mythsdk)
    - [配置MySQL](#配置mysql)
    - [配置Redis](#配置redis)
        - [从源码编译运行并测试](#从源码编译运行并测试)
    - [问题以及解决方案：](#问题以及解决方案)
    - [双硬盘的折腾记录](#双硬盘的折腾记录)

`目录 end` |_2018-08-21_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 配置Deepin的Java开发环境

修改Hostname需要重启, 设置java默认需要重启, docker添加用户组需要重启
## 新增用户
> [详细](/Linux/Base/LinuxBase.md#用户管理)

## 安装Docker
> [详细文档](/Linux/Container/Docker.md)

# 在Linux上配置Java环境
## 配置JDK
### 解压配置
- [下载地址](http://www.oracle.com/technetwork/java/javase/downloads/index.html)
- 在文件 `/etc/profile` 中添加

```sh
    export JAVA_HOME= 绝对路径例如： /home/kcp/Application/sdk/jdk1.8.0_131
    export JRE_HOME=${JAVA_HOME}/jre
    export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
    export PATH=${JAVA_HOME}/bin:$PATH
```
> 让修改立即生效`source /etc/profile` 或者修改 `.bashrc` 文件, 就会在当前用户的终端生效

**root用户的环境**
- 指定默认的jdk，因为系统预装了openJdk ,为了稳妥建议先进入JDK的bin目录,然后执行
```sh
    sudo update-alternatives --install /usr/bin/java java `pwd`/java 300
    sudo update-alternatives --install /usr/bin/javac javac `pwd`/javac 300
```
- 或者不执行命令, 直接修改链接文件即可完成同样的目的
> 后期更新JDK版本, 普通用户的话, 就只是需要更改 `.bashrc` 文件, root用户就执行以上命令, 或者直接重建软链接文件
>> root 用户下 `which java` 然后 `ls -l 显示的路径` 一直往下找, 找到 `/etc/alternatives/java` 和 `/etc/alternatives/javac` 重建这两个软链接.

### sdkman方式 
> jdk不推荐使用sdkman安装，这里的jdk是开源版估计，会少javafx等一些闭源包 Oracle版本才是完整的
> 但是最近SDKMAN出了一个oracle的版本貌似是完整的，因为有个同意协议的过程 `sdk install java 8u144-oracle`

- 安装sdkman `curl -s "https://get.sdkman.io" | bash`

```
    Looking for a previous installation of SDKMAN...
    Looking for unzip...
    Not found.
    Please install unzip on your system using your favourite package manager.
    Restart after installing unzip.
```
- 遇到这种提示就是需要安装zip `sudo apt install zip unzip` 然后重新执行命令
- 执行脚本：`source "/home/kuang/.sdkman/bin/sdkman-init.sh"` 或者重启终端就可以使用 `sdk`命令了
- 查看sdkman 版本 ：`sdk version`
- 查看可用版本 `sdk list java` 
- 不指定版本就是安装最新版 `sdk install java` 
- 指定默认版本 `sdk default java 8u131-zulu`
- 验证是否成功：`java -version`

### mythsdk
> 个人用py开发的脚本， 实现了和sdkman一致的内容， 并且很简单 | [使用文档](https://github.com/Kuangcp/Script/tree/master/python/mythsdk)

********************************
## 配置MySQL
> [安装MySQL](/Database/MySQL.md)

**************************************
## 配置Redis
> [安装Redis](/Database/Redis.md)

### 从源码编译运行并测试
> 新建文件夹将源码下拉下来运行，然后就可以将该目录删除

```sh
    wget http://downloads.sourceforge.net/tcl/tcl8.6.1-src.tar.gz
    sudo tar xzvf tcl8.6.1-src.tar.gz  -C /usr/local/
    cd  /usr/local/tcl8.6.1/unix/
    sudo ./configure
    sudo make
    sudo make install
```
**************
## 问题以及解决方案：
> QQ
- `sudo apt-get install deepin-crossover deepinwine-qq`
- [安装QQ](https://www.findhao.net/easycoding/1748)

> 显卡问题
- 联想G4070 安装 deepin 15.4.1 显卡兼容失败（15.4还能正常用）, 15.5 15.6 是正常使用的 15.7 有点缺陷
- 因为合上盖子休眠就会导致打开电脑直接死机， 找了半天原因是驱动问题
    - 安装 `nvidia-driver`, `nvidia-setting`, `bumblebee-nvidia` 即可解决

手残，按到关闭窗口特效后，就无法打开了，各种用着不爽， 然后重装了最新版系统，然后就装驱动，重启就不能开特效了。。。。。
虽然各种小bug, 也花费了很多时间来解决这些问题(因为自己有强迫症), 但是还是学到了很多东西

********************
## 双硬盘的折腾记录
> [记录](/MyBlog/2018-3-15-install-deepin.md)
