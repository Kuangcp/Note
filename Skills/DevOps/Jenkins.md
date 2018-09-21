`目录 start`
 
- [Jenkins](#jenkins)
    - [安装](#安装)
        - [直接运行jar](#直接运行jar)
        - [Docker](#docker)
    - [配置](#配置)
        - [配置Gradle](#配置gradle)
        - [配置Docker插件](#配置docker插件)
    - [使用](#使用)
        - [个人经验](#个人经验)

`目录 end` |_2018-09-18_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Jenkins
> [官网](https://jenkins.io/)

> [参考博客: 用 Docker, maven, jenkins 完成 CI](http://www.open-open.com/lib/view/open1436922756240.html)

## 安装
> [官方下载地址](https://jenkins.io/download/) | 由于是一个Java的Web服务, 所以也有war版本, 资源消耗都挺大的

### 直接运行jar
直接下载最新LTS版本, java -jar XXX.war 就可以运行了

### Docker
> [DockerHub : official ](https://hub.docker.com/_/jenkins/) | [长期支持版](https://hub.docker.com/r/jenkins/jenkins/)[长期支持版文档](https://github.com/jenkinsci/docker/blob/master/README.md)

- `sudo docker pull jenkins` 下拉镜像(600M+) `jenkins:alpine` 更小点(200M+)
- `sudo docker run --name myjenkins -p 8080:8080 -p 50000:50000 -v /home/kcp/docker/jenkins:/var/jenkins_home jenkins` 构建容器
- 确保目录是开放了权限的, `chmod 777 jenkins` 最简单直接
- 容器启动后, 第一次访问需要初始化, 之后就是正常的容器的启动关闭了

- [h1kkan/jenkins-docker](https://hub.docker.com/r/h1kkan/jenkins-docker/) `由于官方镜像更新太慢,这个镜像有最新的版本`

> 但是以上镜像都太大,更新不一定及时, 所以完全可以自动手动构建镜像
1. 现取[下载](https://jenkins.io/download/)好想要的版本的jar, 然后在一个空目录下 新建一个文件 jenkins.dockerfile
```Dockerfile
    FROM frolvlad/alpine-oraclejdk8:slim
    COPY . . 
    EXPOSE 8080
    EXPOSE 5000
    CMD ["java", "-jar", "jenkins.war"]
```
1. `docker build -t jenkins:xxx -f jenkins.dockerfile .` 注意最后有一个点, 是表明当前目录

********************************
## 配置

### 配置Gradle
> 系统管理 -> Global Tool Configuration 下 配置gradle, 然后新建项目的时候选择新建的gradle配置, 执行构建的时候才会去下载Gradle

### 配置Docker插件


***********************
## 使用


### 个人经验
> 从Gitlab私有库(Maven SpringBooot项目)建好一个任务, 并构建好镜像和容器, 更新容器
> 做法是在运行Docker的服务器上建立一个目录专门用来更新该项目, 然后在Jenkins构建完成后将 jar 包传过去, 执行该目录下的脚本完成容器和镜像的更迭

1. 复制项目URL, Credentials 中添加一个 username/password 类型的授权即可(就是gitlab上的用户名密码)
    - 可以选择指定的 分支 进行构建
1. 添加一个构建, 选择Maven的版本, Goal 中添加 命令 clean package 
1. 在Build 这里添加一个Post-build step 这里 选择添加一个 Shell, 写入要执行的脚本即可
```sh
echo "...构建完成, 开始建立镜像..."
jarFile=$WORKSPACE/target/app.jar
if [ -f $jarFile ];then
	scp $WORKSPACE/target/app.jar xx@xxx:/home/xxx/
    ssh xx@xxx "cd /home/xx/ && sh deploy.sh dev"
fi
```

`deploy.sh`
```sh
version=`date +%Y-%m-%d-%H-%M`
num=`docker ps | grep app | wc -l`
if [ $num = 1 ];then
    docker logs app >> /home/ai/xx/log/$version.log
    docker rm -f app
fi
if [ "$1" = "dev" ];then
    docker build -t app:$version -f /home/xx/build-dev.dockerfile .
else
    docker build -t app:$version -f /home/xx/build-prod.dockerfile . 
fi
echo "版本:"$version"镜像构建完成"
docker run --name app -d -p 16888:16888 -p 3070:3070 app:$version
echo "容器启动成功"
```

`build-dev.dockerfile`
```dockerfile
FROM frolvlad/alpine-oraclejdk8:slim
COPY . .
EXPOSE 16888
EXPOSE 3070
CMD ["java", "-jar", "app.jar", "--spring.profiles.active=jenkins"]
```

`build-prod.dockerfile`
```dockerfile
FROM frolvlad/alpine-oraclejdk8:slim
COPY upload/* .
EXPOSE 16888
EXPOSE 3070
CMD ["java", "-jar", "app.jar", "--spring.profiles.active=production", ">>/var/log/game.log"]
```
