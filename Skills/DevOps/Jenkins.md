---
title: Jenkins
date: 2018-11-21 10:56:52
tags: 
categories: 
    - DevOps
---

**目录 start**

1. [Jenkins](#jenkins)
    1. [安装](#安装)
        1. [直接运行jar](#直接运行jar)
        1. [Docker](#docker)
    1. [配置](#配置)
        1. [配置Gradle](#配置gradle)
        1. [配置Docker插件](#配置docker插件)
    1. [使用](#使用)
        1. [Pipeline](#pipeline)
        1. [个人经验](#个人经验)

**目录 end**|_2020-04-27 23:42_|
****************************************
# Jenkins
> [官网](https://jenkins.io/)

> [参考: 用 Docker, maven, jenkins 完成 CI](http://www.open-open.com/lib/view/open1436922756240.html)

## 安装
> [官方下载地址](https://jenkins.io/download/) | 由于是一个Java的Web服务, 所以也有war版本, 资源消耗都挺大的

### 直接运行jar
直接下载最新LTS版本, java -jar XXX.war 就可以运行了

### Docker
> [Dockerhub: official](https://hub.docker.com/_/jenkins/) `已废弃? 版本太老了` 

> [Dockerhub: LTS](https://hub.docker.com/r/jenkins/jenkins/) | [长期支持版文档](https://github.com/jenkinsci/docker/blob/master/README.md)  

- `docker pull jenkins/jenkins` 下拉镜像(600M+)
    - Alpine版: `jenkins/jenkins:alpine` 更小点(200M+)
- 构建容器 `sudo docker run --name myjenkins -p 8080:8080 -p 50000:50000 -v /home/kcp/docker/jenkins:/var/jenkins_home jenkins`
- 确保 `/home/kcp/docker/jenkins` 目录是开放了权限的, `chmod 777 jenkins` 最简单直接
- 容器启动后, 第一次访问需要配置管理员账号, 插件等等, 配置完成之后就可以任意重启容器了

********************************

**`手动构建镜像`**
> 但是以上镜像都太大,更新不一定及时, 所以完全可以手动构建镜像

1. 去 [下载](https://jenkins.io/download/) 对应版本的war, 然后在一个空目录下 新建一个文件 `jenkins.dockerfile`
```Dockerfile
    FROM frolvlad/alpine-oraclejdk8:slim
    COPY . . 
    EXPOSE 8080
    EXPOSE 5000
    CMD ["java", "-jar", "jenkins.war"]
```
1. 构建镜像 `docker build -t jenkins:xxx -f jenkins.dockerfile .`

********************************

- [h1kkan/jenkins-docker](https://hub.docker.com/r/h1kkan/jenkins-docker/) `依据LTS的war包加上一些常用插件的镜像版本`

## 配置

`配置时区`

[Official Wiki](https://wiki.jenkins.io/display/JENKINS/Change+time+zone) | [参考: Jenkins修改时区（Docker）](https://blog.csdn.net/k_zombie/article/details/50754253)  
或者在 Script Console 中 运行 `System.setProperty('org.apache.commons.jelly.tags.fmt.timeZone', 'Asia/Shanghai');`

### 配置Gradle
> 系统管理 -> Global Tool Configuration 下 配置gradle, 然后新建项目的时候选择新建的gradle配置, 执行构建的时候才会去下载Gradle

### 配置Docker插件

***********************
## 使用

### Pipeline
Jenkins 通过配置好的 slave 镜像启动对应容器, 在slave 容器中完成构建过程, 然后更换应用容器 销毁slave容器

```groovy
pipeline {
    agent {
		label 'docker-slave'
	}
    stages {
        stage('init') {
            steps {
                echo 'init..'
				script {
					echo "PATH = ${PATH}"
					echo "env.version = ${env.version}"
				}
            }
        }
        stage('package') {
                steps {
                echo "start to build"
                checkout changelog: false, poll: false, scm: [$class: 'SubversionSCM', additionalCredentials: [], excludedCommitMessages: '', excludedRegions: '', excludedRevprop: '', excludedUsers: '', filterChangelog: false, ignoreDirPropChanges: false, includedRegions: '', locations: [[cancelProcessOnExternalsFail: true, credentialsId: '22f6f4c9-f19e-4120-af4b-7946ea7cc2ef', depthOption: 'infinity', ignoreExternalsOption: true, local: '.', remote: 'http://192.168.10.200/svn/hecheng/dev/server/trunk']], quietOperation: true, workspaceUpdater: [$class: 'UpdateUpdater']]
                 sh "mvn -B -V -U clean package -DskipTest=true"
                }
        }
        stage('test') {
            steps {
                echo 'Testing..'
                sh "mvn -B test"
            }
        }
        stage('build docker image and publish into local registry') {
            steps {
                echo "starting to build docker image..."
                script {		
                /* This builds the actual image; synonymous to
                * docker build on the command line */
                sh "pwd && ls . && docker info"
                withDockerRegistry(url: 'http://192.168.10.6:5000/') {
                    def app = docker.build "192.168.10.6:5000/synthesizer-dev:${env.BUILD_ID}"
                    app.push()
                    echo "pushed into local registry"
                    }
                }
            }
        }
        stage('deploy') {
            steps {
                echo 'killing old server and start new server....'
                script {
                    sh "docker container rm -f synthesizer-dev  &&  docker run -d -p 3070:3070 -p 16888:16888 --name synthesizer-dev 192.168.10.6:5000/synthesizer-dev:${env.BUILD_ID}"
                }
            }
        }
        stage('clean local images') {
            steps {
                echo "cleaning dangling images..."
                script {
                    sh "docker images --filter \"dangling=true\" -q |xargs --no-run-if-empty docker rmi"
                }
            }
        }	
    }
}
```

slave 配置
```
    /home/ai/rs/jenkins-slave/m2:/home/jenkins/.m2
    /var/run/docker.sock:/var/run/docker.sock
    /usr/bin/docker:/usr/bin/docker
```
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
