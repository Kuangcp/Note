`目录 start`
 
- [SQLServer](#sqlserver)
    - [安装配置](#安装配置)
        - [Docker安装2017硬是不成功](#docker安装2017硬是不成功)
            - [2000版本](#2000版本)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# SQLServer

## 安装配置
### Docker安装2017硬是不成功
- [dockerhub网址](https://hub.docker.com/r/exoplatform/sqlserver/)

```sh
    docker run -d -e SA_PASSWORD=<passord> -e SQLSERVER_DATABASE=<db name> -e SQLSERVER_USER=<user> -e 
    SQLSERVER_PASSWORD=<password> -p <local port>:1433 exoplatform/sqlserver:ctp2-1-1

    docker run -d -e SA_PASSWORD=ad -e SQLSERVER_DATABASE=mythos -e SQLSERVER_USER=myth -e SQLSERVER_PASSWORD=jiushi -p 1433:1433 mssql


    docker run --name mssql -e ACCEPT_EULA=Y -e SA_PASSWORD=docker888 -e SQLSERVER_USER=myth -e SQLSERVER_PASSWORD=jiushi -p 1433:1433 -d microsoft/mssql-server-linux:latest

    docker run -e 'SA_PASSWORD=docker888' -p 1433:1433 -it --rm microsoft/mssql-server-linux:latest /opt/mssql/bin/sqlservr --accept-eula


    # 查看控制台输出
    docker run --name mssql -e ACCEPT_EULA=Y -e SA_PASSWORD=docker888 -e SQLSERVER_USER=myth -e SQLSERVER_PASSWORD=jiushi -p 1433:1433 -it microsoft/mssql-server-linux:2017-GA


    docker run -d -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=ad'  -e 'SQLSERVER_PASSWORD=jiushi' -p 1433:1433 microsoft/mssql-server-linux:2017-GA 

```
#### 2000版本
- [docker别人做的镜像](https://hub.docker.com/r/rsmoorthy/mssql/)