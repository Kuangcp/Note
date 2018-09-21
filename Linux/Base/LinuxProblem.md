`目录 start`
 
- [遇到的常见问题](#遇到的常见问题)
    - [命令找不到](#命令找不到)
    - [其他](#其他)
        - [终端响铃](#终端响铃)
        - [Ubuntu与Windows10时间相差8小时的解决](#ubuntu与windows10时间相差8小时的解决)
        - [终端开启慢](#终端开启慢)
        - [Deepin的NVIDIA驱动问题](#deepin的nvidia驱动问题)
        - [笔记本突然断电导致开机报错](#笔记本突然断电导致开机报错)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 遇到的常见问题

## 命令找不到
- `sudo找不到` 就安装 sudo
- locale-gen 安装locales 使用`locale-gen --purge`命令进行更新编码

> Linux上的报错, 提示说找不到共享库 | [参考解决方式 ](http://www.cnblogs.com/Anker/p/3209876.html)

## 其他
### 终端响铃
> [参考博客: Linux中关闭响铃](https://blog.csdn.net/u010691256/article/details/9048729)

1. 临时关闭：`rmmod pcspkr` 临时开启：`modprobe pcspkr`
1. 编辑 `/etc/inputrc`，找到`#set bell-style none`这一行，去掉前面的注释符号
1. xset -b

`下面的方法不敢试`
- 对于Debian/Ubuntu系统，使用root身份执行：
    - `sudo echo "blacklist pcspkr" >> /etc/modprobe.d/blacklist`
- 对于CentOS/Redhat/RHEL/Fedora系统，使用root身份执行：
    - `echo "alias pcspkr off" >> /etc/modprobe.conf `

### Ubuntu与Windows10时间相差8小时的解决
- `timedatectl set-local-rtc true `

### 终端开启慢 
- 检查 .bashrc 文件 看是否有可疑脚本,
    -  这次就是因为sdkman的原因导致巨慢,那上次搞得我新建用户,重装系统是什么原因呢?

### Deepin的NVIDIA驱动问题
- [论坛博客](https://bbs.deepin.org/forum.php?mod=viewthread&tid=132312)
    - `sudo apt-get install bumblebee-nvidia nvidia-driver nvidia-settings`

### 笔记本突然断电导致开机报错
> 报错信息: fsck exited with status code 4

1. 根据报错提示的分区, 进行修复, 由于我的Linux是ext3文件系统
1. `fsck.ext3 -y /dev/sda9` **分区根据实际情况**
1. 完成后重启即可
