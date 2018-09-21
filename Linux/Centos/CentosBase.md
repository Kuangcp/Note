`目录 start`
 
- [Centos](#centos)
    - [安装](#安装)
        - [docker安装](#docker安装)
    - [基础命令](#基础命令)
    - [用户管理](#用户管理)
        - [新增](#新增)
    - [BUG](#bug)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Centos
> 主流服务器

## 安装
### docker安装
> [hub的官方镜像](hub.docker.com/_/centos/)

- `docker pull centos` 得到镜像，然后跑起来即可
    - `cat /etc/redhat-release` 查看当前centos版本（适用于redhat centos） [参考博客](www.cnblogs.com/hitwtx/archive/2012/02/13/2349742.html)

- docker 中 centos7systemctl命令失效的解决方案：
	- `docker run --name centos2 --privileged  -ti -e "container=docker"  -v /sys/fs/cgroup:/sys/fs/cgroup  centos  /usr/sbin/init`

## 基础命令
> 采用的是yum rpm 管理包

## 用户管理

### 新增
> 和Ubuntu类似, 但是adduser会新建用户并且建立home目录,而且没有废话的交互, ubuntu就有

`adduser kuang` 新增用户和对应目录
`passwd kuang` 修改密码 , 奇怪的是使用gpasswd就更改成功了用不了


## BUG
> 2018-04-01 16:34:17 稳定?呵呵
```
已安装:
  nginx.x86_64 1:1.12.2-2.el7                                                                                                                                                                  

作为依赖被安装:
  fontconfig.x86_64 0:2.10.95-11.el7                 fontpackages-filesystem.noarch 0:1.44-8.el7  gd.x86_64 0:2.0.35-26.el7                         gperftools-libs.x86_64 0:2.4-8.el7         
  libX11.x86_64 0:1.6.5-1.el7                        libX11-common.noarch 0:1.6.5-1.el7           libXau.x86_64 0:1.0.8-2.1.el7                     libXpm.x86_64 0:3.5.12-1.el7               
  libjpeg-turbo.x86_64 0:1.2.90-5.el7                libpng.x86_64 2:1.5.13-7.el7_2               libunwind.x86_64 2:1.2-2.el7                      libxcb.x86_64 0:1.12-1.el7                 
  libxslt.x86_64 0:1.1.28-5.el7                      lyx-fonts.noarch 0:2.2.3-1.el7               nginx-all-modules.noarch 1:1.12.2-2.el7           nginx-mod-http-geoip.x86_64 1:1.12.2-2.el7 
  nginx-mod-http-image-filter.x86_64 1:1.12.2-2.el7  nginx-mod-http-perl.x86_64 1:1.12.2-2.el7    nginx-mod-http-xslt-filter.x86_64 1:1.12.2-2.el7  nginx-mod-mail.x86_64 1:1.12.2-2.el7       
  nginx-mod-stream.x86_64 1:1.12.2-2.el7            

失败:
  nginx-filesystem.noarch 1:1.12.2-2.el7                                                                                                                                                       

完毕！
16:28:02 ~/frp/frp_0.16.1_linux_amd64 → nginx
nginx: relocation error: /lib64/libc.so.6: symbol _dl_starting_up, version GLIBC_PRIVATE not defined in file ld-linux-x86-64.so.2 with link time reference
16:28:06 ~/frp/frp_0.16.1_linux_amd64 → sudo yum install nginx
sudo: relocation error: /lib64/libc.so.6: symbol _dl_starting_up, version GLIBC_PRIVATE not defined in file ld-linux-x86-64.so.2 with link time reference
16:28:14 ~/frp/frp_0.16.1_linux_amd64 → sudo yum install git
sudo: relocation error: /lib64/libc.so.6: symbol _dl_starting_up, version GLIBC_PRIVATE not defined in file ld-linux-x86-64.so.2 with link time reference
16:28:30 ~/frp/frp_0.16.1_linux_amd64 → su root
su: relocation error: /lib64/libc.so.6: symbol _dl_starting_up, version GLIBC_PRIVATE not defined in file ld-linux-x86-64.so.2 with link time reference
```