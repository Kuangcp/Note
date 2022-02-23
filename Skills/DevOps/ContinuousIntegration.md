---
title: ContinuousIntegration
date: 2018-11-21 10:56:52
tags: 
categories: 
---

**目录 start**

1. [持续集成](#持续集成)
    1. [Jenkins](#jenkins)
    1. [GoCD](#gocd)
    1. [Drone](#drone)
    1. [flow.ci](#flowci)
    1. [三方平台](#三方平台)
1. [代码质量管理](#代码质量管理)
    1. [Bug跟踪](#bug跟踪)
    1. [sonarqube](#sonarqube)
1. [测试平台](#测试平台)

**目录 end**|_2021-04-14 14:37_|
****************************************
# 持续集成
> 参考: [持续集成](http://www.ruanyifeng.com/blog/2015/09/continuous-integration.html) | [持续集成服务 Travis CI 教程](http://www.ruanyifeng.com/blog/2017/12/travis_ci_tutorial.html)  
> [廖雪峰 使用Travis进行持续集成](https://www.liaoxuefeng.com/article/0014631488240837e3633d3d180476cb684ba7c10fda6f6000)  
> 目前个人理解: 使用jenkins 结合gradle docker ，一键上传代码之后自动构建得到镜像

> [利用Travis CI更新github page](https://github.com/steveklabnik/automatically_update_github_pages_with_travis_example)
- 使用bitbucket配置私有仓库，在hub上配置docker文件的目录，进行构建，这样就会得到一个可用的镜像

**************************
## Jenkins
> [详细](Jenkins.md)

## GoCD
> [Github:GoCD](https://github.com/GoCD) 

> [参考: GoCD的正确打开方式](https://insights.thoughtworks.cn/the-right-interpretation-of-gocd/)

> [参考: GoCD概念篇](http://www.cnblogs.com/elisun/p/7071536.html)
************************
## Drone 
> [官网](https://drone.io/)

go语言实现，一个原生支持 docker 的 CI

> [参考: Drone 一个原生支持 docker 的 CI](https://aisensiy.github.io/2017/08/04/drone-best-ci/)  
> [参考: Drone CI + GitLab持续集成的基础设施搭建](https://zmcdbp.com/drone-ci-gitlab-base-build/) | [参考: Drone CI的持续集成的基本使用](https://zmcdbp.com/drone-ci-basic-use/)

*******************
## flow.ci
> [官网](https://flow.ci/) | [文档](https://github.com/FlowCI/docs/blob/master/intro_base.md)

************************
- [gopub](https://gitee.com/dev-ops/gopub)
- [gokins](https://gitee.com/gokins/gokins)  

## 三方平台
- [appveyor](https://ci.appveyor.com/projects)

> [Gradle + Travis CI 学习笔记](https://upupming.site/2018/04/03/gradle-travis/#travis-ci)  

****************************
# 代码质量管理

## Bug跟踪
- [bugzilla](https://bugzilla.readthedocs.io/en/latest/installing/quick-start.html)
- redmine 

## sonarqube
> [官网](https://www.sonarqube.org/) | [Docker Hub](https://hub.docker.com/_/sonarqube/)

> 快速使用
1. `docker run -d --name sonarqube -p 9000:9000  sonarqube:8-community`

1. [sonarscanner](https://docs.sonarqube.org/latest/analysis/scan/sonarscanner-for-maven/)
    1. Maven会输出当前分析项目的结果URL
1. sonar-scanner 命令行工具安装
    1. 配置工具 `/etc/sonar-scanner/sonar-scanner.properties`
        - ```ini
            sonar.host.url=http://localhost:9000
            sonar.sourceEncoding=UTF-8
            sonar.login=admin
            sonar.password=admin
            ```
    1. 配置项目根路径 `sonar-project.properties`
        - ```ini
            sonar.projectKey=com.github.kuangcp.gobase
            sonar.projectName=GoBase
            ```

> [参考: 有赞 GO 项目单测、集成、增量覆盖率统计与分析](https://cloud.tencent.com/developer/article/1684515)  
> [支持 Go](https://docs.sonarqube.org/latest/analysis/languages/go/)

************************

# 测试平台
> [metersphere.io](https://metersphere.io/)