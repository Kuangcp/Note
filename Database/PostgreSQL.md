`目录 start`
 
- [Postgresql](#postgresql)
    - [概述](#概述)
    - [和MySQL对比](#和mysql对比)
    - [安装](#安装)
        - [安装客户端](#安装客户端)
        - [安装服务端](#安装服务端)
        - [Docker方式安装服务端](#docker方式安装服务端)
            - [pull完整版](#pull完整版)
            - [pull精简版](#pull精简版)
            - [Dockerfile构建](#dockerfile构建)
            - [解释Dockerfile文件](#解释dockerfile文件)
    - [使用](#使用)
        - [Postgresql终端命令行使用](#postgresql终端命令行使用)
        - [用户和角色权限](#用户和角色权限)
            - [创建用户](#创建用户)
            - [修改权限](#修改权限)
        - [Java使用](#java使用)
    - [基础数据](#基础数据)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Postgresql
- [ ] [该公司对于PostgreSQL的缺点陈列是否属实](http://www.onexsoft.com/onesql.html)

## 概述
> [PostgreSQL](http://www.cnblogs.com/fcode/articles/PostgreSQL.html) | [wiki](https://wiki.postgresql.org/wiki/Main_Page)

- 严格SQL标准
- Schemas 和表，用户的关系：
    - Schemas相当于是一个数据库进行分类的文件夹

## 和MySQL对比
> [PostgreSQL 与 MySQL 相比，优势何在？](https://www.zhihu.com/question/20010554)
> [Converting MySQL to PostgreSQL](https://en.wikibooks.org/wiki/Converting_MySQL_to_PostgreSQL)

## 安装
### 安装客户端
> `sudo apt-get install postgresql-client`

### 安装服务端
> `sudo apt install postgresql`

### Docker方式安装服务端
> [官方镜像](https://hub.docker.com/_/postgres/)

#### pull完整版
- 或者： `docker pull postgres` [官方镜像](https://hub.docker.com/_/postgres/)
    - 运行容器 `docker run --name mypostgre -i -t -p 5432:5432 postgres`
    - 客户端连接 `psql -h localhost -p 5432 -U postgres`

#### pull精简版
- 下拉镜像：`docker pull postgres:alpine` | 因为个人系统客户端是9.6, 所以用`9.6-alpine`镜像
- 构建容器：
```sh
    docker run -d --name postgre \
    -e POSTGRES_PASSWORD=jiushi \
    -v gitea-db-data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:9.6-alpine
```
- 容器中连接 进入postgresql终端 `docker exec -it postgre psql -U postgres`
    - 客户端连接 `psql -h localhost -U postgres`
- 连接后 输入`\l` 列出所有数据库 即可查看连接成功与否

#### Dockerfile构建
`Dockerfile`
```dockerfile
    FROM ubuntu:16.04
    RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
    RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list
    RUN apt-get update && apt-get -y -q install python-software-properties software-properties-common \
        && apt-get -y -q install postgresql-9.4 postgresql-client-9.4 postgresql-contrib-9.4
    USER postgres
    RUN /etc/init.d/postgresql start \
        && psql --command "CREATE USER pger WITH SUPERUSER PASSWORD 'pger';" \
        && createdb -O pger pgerdb
    USER root
    RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.4/main/pg_hba.conf
    RUN echo "listen_addresses='*'" >> /etc/postgresql/9.4/main/postgresql.conf
    EXPOSE 5432
    RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql
    VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
    USER postgres
    CMD ["/usr/lib/postgresql/9.4/bin/postgres", "-D", "/var/lib/postgresql/9.4/main", "-c", "config_file=/etc/postgresql/9.4/main/postgresql.conf"]
```
- 构建容器 `docker build -t mypostgresql:9.4 .`
    - 运行容器 `docker run --name mypostgre -i -t -p 5432:5432 mypostgresql:9.4`
    - 使用客户端连接`psql -h localhost -p 5432 -U pger -W pgerdb` 口令：`pger`

#### 解释Dockerfile文件
> 待学习解释

************************************
## 使用
> [PostgreSQL 9.6.0 手册](http://postgres.cn/docs/9.6/index.html)

### Postgresql终端命令行使用
> [PostgreSQL新手入门](http://www.ruanyifeng.com/blog/2013/12/getting_started_with_postgresql.html)
`用熟悉的MySQL命令来解释`
- `\l` show databases
- `\c dbname [user]` 切换数据库
- `\dt` show tables
- `\d tablename` desc tablename
- `\di` 查看索引
- `\du` 查看所有用户
- `\dn` 查看模式列表
- `\copyright` 显示版权信息
- `\encoding` 显示编码信息
- `\h` SQL命令语法上的说明，用*显示全部命令 
- `\prompt [文本]名称` 提示用户设定内部变数
- `\password [username]` 改密码
- `\q` exit
- 可以使用pg_dump和pg_dumpall来完成。比如备份sales数据库： 
    - pg_dump drupal>/opt/Postgresql/backup/1.bak 

### 用户和角色权限

#### 创建用户
- `createuser -P -D -R -e playboy`  //创建一个用户,-P要设置密码，-R,不参创建其他用户，-D不能创建数据库
- `create user myth` 不带login属性
- `create role myth` 具有login属性
- `psql -U playboy -d playboy` 登录用户，一般默认是有用户同名数据库才能登录

- [修改默认登录不需要密码的配置](http://www.linuxidc.com/Linux/2013-04/83564p2.htm)

#### 修改权限
> [参考博客](http://blog.csdn.net/beiigang/article/details/8604578)
> [参考博客_角色](http://www.cnblogs.com/stephen-liu74/archive/2012/05/18/2302639.html)
> [配置](http://www.linuxidc.com/Linux/2013-04/83564p2.htm)

- `ALTER ROLE rolename LOGIN;`  设置登录权限
- `ALTER ROLE david WITH PASSWORD 'ufo456';` 设置密码登录权限
    - 但是，默认是不需要密码 查看pg_hba.conf 文件，发现local 的METHOD 为trust，所以不需要输入密码
    - 将local 的METHOD 更改为password，然后保存重启postgresql。
    - [博客](http://www.linuxidc.com/Linux/2014-02/96886.htm)
- ` ALTER ROLE sandy VALID UNTIL '2014-04-24';` 设置角色有效期
- `SELECT * from pg_roles ;` 查看所有角色

- `CREATE ROLE father login nosuperuser nocreatedb nocreaterole noinherit encrypted password 'abc123';` 
    - 在PostgreSQL中，首先需要创建一个代表组的角色，之后再将该角色的membership 权限赋给独立的角色即可。
- `GRANT CONNECT ON DATABASE test to father;` 角色赋予数据库test 连接权限和相关表的查询权限。


### Java使用
> [Postgresql JDBC Driver](https://github.com/pgjdbc/pgjdbc)

- [官方：springboot使用](https://springframework.guru/configuring-spring-boot-for-postgresql/)
    - [参考博客](https://www.netkiller.cn/java/spring/boot/postgresql.html)

## 基础数据
> [ PostgreSQL中的数据类型](https://blog.csdn.net/jpzhu16/article/details/52140048)
