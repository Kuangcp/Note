`目录 start`
 
- [软件使用记事](#软件使用记事)
    - [【包管理】](#包管理)
        - [使用sdkman](#使用sdkman)
    - [【服务管理】](#服务管理)
        - [oneinstack](#oneinstack)
- [【常用工具】](#常用工具)
    - [网络工具](#网络工具)
        - [nmap](#nmap)
        - [apache benchmark](#apache-benchmark)
    - [日常工具](#日常工具)
        - [百度网盘](#百度网盘)
        - [输入法](#输入法)
            - [搜狗输入法](#搜狗输入法)
            - [rime](#rime)
            - [小小输入法](#小小输入法)
        - [qgit](#qgit)
        - [convert](#convert)
        - [todo.txt](#todotxt)
            - [todo.txt-cli](#todotxt-cli)
    - [【IDE】](#ide)
        - [Idea](#idea)
        - [eclipse](#eclipse)
    - [绘图工具](#绘图工具)
        - [在线版](#在线版)
        - [安装版](#安装版)
    - [安全工具](#安全工具)
        - [gpg](#gpg)

`目录 end` |_2018-09-01_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 软件使用记事
## 【包管理】
### 使用sdkman
> 但是总会莫名其妙的冒出问题，sdk命令掉线始终连不上网，终端打开巨慢

`安装`
- 安装sdkman `curl -s "https://get.sdkman.io" | bash` 遇到提示zip 就是需要安装zip `sudo apt install zip` 然后重新执行命令
- 执行脚本：`source "/home/kuang/.sdkman/bin/sdkman-init.sh"` 或者重启终端就可以使用了，查看sdkman 版本:`sdk version`
`使用`
- [官网文档](http://sdkman.io/usage.html)
- 查看所有 `sdk list`
    - 查看某sdk的版本 `sdk list java ` 
- 不指定版本则默认安装最新版 `sdk install java` 安装指定版本 `sdk default java 8u131-zulu`
- 开始使用指定版本(for the current shell only) `sdk use scala 2.12.1`
- 查看当前版本 `sdk current java`
- 验证是否成功：`java -version`
- 移除 `sdk uninstall scala 2.11.6`

******************
## 【服务管理】
### oneinstack
> 一键配置环境 [官方文档](https://oneinstack.com/install/)

![配图](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Linux/install_oneinstack.png)
- `apt -y install wget screen curl python`
- 下载源码：
    - `wget http://aliyun-oss.linuxeye.com/oneinstack-full.tar.gz` #阿里云经典网络下载
    - `wget http://mirrors.linuxeye.com/oneinstack-full.tar.gz` #包含源码，国内外均可下载
    - `wget http://mirrors.linuxeye.com/oneinstack.tar.gz` #不包含源码，建议仅国外主机下载
- `tar xzf oneinstack-full.tar.gz`
- `cd oneinstack` #如果需要修改目录(安装、数据存储、Nginx日志)，请修改options.conf文件
- `screen -S oneinstack` #如果网路出现中断，可以执行命令`screen -R oneinstack`重新连接安装窗口
- `sudo ./install.sh` #注：请勿sh install.sh或者bash install.sh这样执行

******************
# 【常用工具】
> 基本是Linux工具，因为主力是用Linux

## 网络工具
### nmap
> 端口扫描 [参考博客](http://aaaxiang000.blog.163.com/blog/static/2063491220113284325531/)

- 扫描`nmap <param> IP`
    - -sP
    - -sT
    - -sR
    - -n `最简单直接的参数`

### apache benchmark
> 压力测试工具

- 测试本机超过100连接报错 104: 
    - [Blog:解决问题](http://www.cnblogs.com/archoncap/p/5883723.html)

************************************
## 日常工具
### 百度网盘
- [百度网盘命令客户端](https://github.com/iikira/BaiduPCS-Go) `Go语言实现`

### 输入法
#### 搜狗输入法
> 唯一一个大厂支持Linux 

- Ctrl Alt B 显示/关闭 特殊字符面板

#### rime
- [rime](http://rime.im/) `用过一下子有莫名其妙的bug就卸载了`

#### 小小输入法
[小小输入法在Deepin上的使用](https://bbs.deepin.org/forum.php?mod=viewthread&tid=138500&highlight=%E5%B0%8F%E5%B0%8F%E8%BE%93%E5%85%A5%E6%B3%95)

### qgit
- git查看仓库的图形化界面

***********************************
### convert
- [参考博客](http://blog.csdn.net/mybelief321/article/details/9969949)
- 将图片转换成指定大小 这是保持比例的 `convert -resize 600X600 src.jpg dst.jpg` 中间是字母X
- 如果不保持比例，就在宽高后加上感叹号 
- 可以只指定高度，那么宽度会等比例缩放 `convert -resize 400 src.jpg dst.jpg`
- 还可以按百分比缩放

_批量修改_
> 如果没有 -path 语句，新生成的 png 文件将会覆盖原始文件 [参考博客](http://www.cnblogs.com/jkmiao/p/6756929.html)

- `mogrify -path newdir -resize 40X40 *.png` 把png图片全部转成40X40大小并放在新文件夹下
- `mogrify -path newdir -format png  *.gif` 将所有gif转成png放在新目录下

### todo.txt
> [官网](http://todotxt.org/) 一个简约的 TODO 软件

#### todo.txt-cli
> 终端中的TODO 

- [todo.txt-cli](https://github.com/todotxt/todo.txt-cli)

******************************
## 【IDE】
### Idea
> [更多](/Java/Tool/IDEA.md)

### eclipse

【eclipse EE Mars】
* 这里的Tomcat是使用了你所导入的必要执行文件，但是运行的必要配置文件在eclipse Server项目里另有一份
* 而且运行时也是使用这份配置文件，这样的结果是可以使用一份Tomcat目录，在eclipse配置运行多个Tomcat
* 但是奇怪的是 访问不了Tomcat主页即：localhost:8080 所以也就不能管理Tomcat 查看运行状态

资源下载 archive.eclipse.org/eclipse/downloads/ 

***********************************************
## 绘图工具
### 在线版
- [processon](https://www.processon.com/)

### 安装版
*****************
## 安全工具
### gpg
> [参考博客](http://www.ruanyifeng.com/blog/2013/07/gpg.html)

常用参数
```
gpg --list-key
    --gen-key
```
- 生成的过程, 输入相关的提示信息, 最后输完密码后需要输入随机字符, 就也是按照提示, 但是1.4是正常的, 其他的直接假死,不是很理解这种操作


