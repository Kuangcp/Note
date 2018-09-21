`目录 start`
 
- [Docker Advance](#docker-advance)
    - [AUFS](#aufs)
    - [配置](#配置)
        - [更改数据的存放目录](#更改数据的存放目录)
        - [暴露出tcp端口](#暴露出tcp端口)
        - [Tips](#tips)

`目录 end` |_2018-09-18_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Docker Advance

## AUFS
> Docker 采用的是 AUFS 文件系统, go语言编写的程序

> [参考博客: 剖析Docker文件系统：Aufs与Devicemapper](http://www.infoq.com/cn/articles/analysis-of-docker-file-system-aufs-and-devicemapper)
> [参考博客: 理解Docker（7）：Docker 存储 - AUFS](http://www.cnblogs.com/sammyliu/p/5931383.html)

## 配置

### 更改数据的存放目录

> docker 默认是将数据放在了 `/var/lib/docker` 下, 包括所有的镜像, 容器, 卷...

1. `挂载新的目录到 /var/lib/docker 上`
> [参考博客: Docker数据将跟分区磁盘占满了 ](http://dockone.io/question/531)
> [参考博客: Docker 常见问题 (FAQ)](https://www.lsproc.com/post/docker-faq/#toc_1)
```sh
service docker stop
cp -prf /var/lib/docker /data/
rm -rf /var/lib/docker

vi /etc/fstab # 追加一下内容：
/data/docker /var/lib/docker none bind 0 0
mount -a
service docker start
```
2. 还尝试过将文件复制出去, 然后用软链接的方式, 但是失败了 报的错也没怎么看懂
3. 修改配置文件
```
-g, --graph=""
  Path to use as the root of the Docker runtime. Default is /var/lib/docker.

如 docker -d --graph=/opt/docker
docker daemon 的启动参数修改方法

rhel/centos 下, 默认启动参数在 /etc/sysconfig/docker, 如:

6.x:
other_args="--graph=/opt/docker "

7.x: (update: 2015-01-21)
OPTIONS="--graph=/opt/docker "

debian/ubuntu 下, 默认启动参数在 /etc/default/docker, 如:
DOCKER_OPTS="--graph=/opt/docker "

```

### 暴露出tcp端口

1. systemctl edit docker.service
```ini
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock 
```
> 以上所处文件为: /etc/systemd/system/docker.service.d/override.conf 
>> 注意: `-H unix:///var/run/docker.sock` 如果少了这个配置, Docker客户端就失效了, 什么都干不了

2. systemctl restart docker 

> 而那些不是使用systemd管理服务的才要在 /etc/docker/ 下配置 daemon.json [official doc](https://docs.docker.com/engine/reference/commandline/dockerd/)

### Tips
> WARNING: No swap limit support

1. Edit the /etc/default/grub file.
  - Set the GRUB_CMDLINE_LINUX value as follows:
  - GRUB_CMDLINE_LINUX="cgroup_enable=memory swapaccount=1"
1. sudo update-grub
1. Reboot your system.

