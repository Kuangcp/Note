`目录 start`
 
- [Nginx](#nginx)
    - [Nginx的安装](#nginx的安装)
        - [命令安装](#命令安装)
        - [编译安装](#编译安装)
        - [Docker安装并做反向代理](#docker安装并做反向代理)
    - [命令使用](#命令使用)
    - [配置使用](#配置使用)
        - [本地静态文件Web服务器](#本地静态文件web服务器)
            - [反向代理多个服务](#反向代理多个服务)
            - [配置https](#配置https)
                - [certbot来配置Https](#certbot来配置https)
            - [配置Websocket反向代理](#配置websocket反向代理)
        - [防盗链](#防盗链)
        - [负载均衡](#负载均衡)
        - [跨域问题的配置](#跨域问题的配置)
            - [静态服务器将后台反代理](#静态服务器将后台反代理)
    - [问题](#问题)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Nginx

## Nginx的安装
### 命令安装

- 安装`sudo apt install nginx`
- 启动服务 `sudo nginx`或者`sudo /etc/init.d/nginx start`
- 关闭 `sudo nginx -s quit` 或者 `sudo /etc/init.d/nginx stop`

### 编译安装
> 不建议使用这种方式进行安装，很容易出现兼容问题


- 下载 nginx，pcre，zlib，openssl 的压缩包
- 进入解压根目录（按实际情况配置） 
`配置各个包`
```sh
    ./configure --sbin-path=/usr/local/nginx/nginx \
    --conf-path=/usr/local/nginx/nginx.conf \
    --pid-path=/usr/local/nginx/nginx.pid \
    --with-http_stub_status_module \
    --with-http_ssl_module \
    --with-pcre=/home/kuang/pcre-8.20 \
    --with-openssl=/home/kuang/openssl \
    --with-zlib=/home/kuang/zlib-1.2.11
```

### Docker安装并做反向代理
> [nginx hub 官方镜像](https://hub.docker.com/r/library/nginx/)
- 运行命令创建容器运行 `docker run --name youhuigo -d -p 80:80 -v /home/kuang/nginx/conf/:/etc/nginx/conf.d/:ro --link you:web nginx`

`conf 基础配置文件`
```
upstream gitea {
  server 127.0.0.1:6001;
}
server {
  listen 80;
  server_name git.kuangcp.top;
  location / {
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $http_host;
    proxy_set_header X-Nginx-Proxt true;

    proxy_pass http://gitea;
    proxy_redirect off;
  }
}
```
> [配置多域名反向代理](http://www.ttlsa.com/nginx/use-nginx-proxy/) `其实也就是多了 俩 upstream 监听80的server`

## 命令使用
`nginx -h 输出`
```
  nginx version: nginx/1.13.3
  Usage: nginx [-?hvVtTq] [-s signal] [-c filename] [-p prefix] [-g directives]
  Options:
    -?,-h         : this help
    -v            : show version and exit
    -V            : show version and configure options then exit
    -t            : test configuration and exit
    -T            : test configuration, dump it and exit
    -q            : suppress non-error messages during configuration testing
    -s signal     : send signal to a master process: stop, quit, reopen, reload
    -p prefix     : set prefix path (default: /usr/share/nginx/)
    -c filename   : set configuration file (default: /etc/nginx/nginx.conf)
    -g directives : set global directives out of configuration file
```
- `-s signal`
  - stop 停止
  - quit 退出
  - reopen 重新打开
  - reload 重载（修改配置文件常使用）
- `-t` 测试配置
  - 使用 指定配置文件，或者默认配置文件 进行测试

***************
## 配置使用
> [知乎专栏](https://zhuanlan.zhihu.com/p/24524057)  
> [nginx基本配置](https://segmentfault.com/a/1190000002797601) | [ngrok nginx docker本地搭建服务器](https://fengqi.me/unix/409.html)
- [实验楼课程](https://www.shiyanlou.com/courses/95)

- 个人理解
  1. server_name 是一个域名或者ip, 如果是ip和公网的域名就没什么好解释的,
    - 但是如果只是局域网的修改host文件生成的域名, 自己使用该域名访问是没有问题的, 别人访问不了,但是如果也同样的修改host文件后, 也能正确使用域名访问
  2. server是一个门路, 不会冲突, 所以才能有很多个监听80端口的配置而互不影响.

### 本地静态文件Web服务器
> 最简单的使用 [参考博客](http://blog.yuansc.com/2015/04/29/nginx%E9%85%8D%E7%BD%AE%E9%9D%99%E6%80%81%E6%96%87%E4%BB%B6%E6%9C%8D%E5%8A%A1%E5%99%A8/)

```conf
  server {
    # listen 6050;
    client_max_body_size 4G;
    listen  80;  ## listen for ipv4; this line is default and implied
    server_name static.me.com;
    root /home/mini/Sync;
    location / {
    }
  }
```
再在 `/etc/hosts`文件中配置下域名即可访问

> 在服务器中配置， 出现403错误， 将 /etc/nginx/nginx.conf 中第一行的 user 改成 root
#### 反向代理多个服务
- 修改默认配置文件 `/etc/nginx/nginx.conf`
  - 或者更好的就是在 `/etc/nginx/conf.d/`下新建 *.conf 文件，文件名任意

`该配置文件配置了服务器反向代理，80端口上：/路径的请求转发到9991端口 /myth转发到7898端口 `
```conf
upstream xxxuthus {
  server 127.0.0.1:9991;
}
upstream youhui {
  server 127.0.0.1:7898;
}

server {
  listen 80;
  server_name 1.1.1.1;

  location / {
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $http_host;
    proxy_set_header X-Nginx-Proxt true;

    proxy_pass http://xxxuthus;
    proxy_redirect off;
  }
 location /myth{
  proxy_pass http://youhui;
  proxy_redirect off;
 }
}
```
- 测试配置文件 再 重启nginx `nginx -s reload`

#### 配置https
> 参考博客 [nginx搭建https服务](http://www.cnblogs.com/tintin1926/archive/2012/07/12/2587311.html) | [nginx http/2](http://letus.club/2016/04/08/nginx-http2-letsencrypt/)

- 先签发证书 `命令运行`
```sh
  ############ 证书颁发机构
  # CA机构私钥
  openssl genrsa -out ca.key 2048
  # CA证书
  openssl req -x509 -new -key ca.key -out ca.crt
  ############ 服务端
  # 生成服务端私钥
  openssl genrsa -out server.key 2048
  # 生成服务端证书请求文件
  openssl req -new -key server.key -out server.csr
  # 使用CA证书生成服务端证书  关于sha256，默认使用的是sha1，在新版本的chrome中会被认为是不安全的，因为使用了过时的加密算法。
  openssl x509 -req -sha256 -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -days 3650 -out server.crt    
  # 打包服务端的资料为pkcs12格式(非必要，只是换一种格式存储上一步生成的证书) 生成过程中，需要创建访问密码，请记录下来。
  openssl pkcs12 -export -in server.crt -inkey server.key -out server.pkcs12
```
`*.conf配置文件 配置HTTPS`
```
upstream youhui {
  server 127.0.0.1:8888;
}
server {
  listen 443;
  server_name wx.jjyouhuigo.com;
  # 主要就是添加了这一块
  ssl on;
  ssl_certificate  /home/youhuigo/https/server.crt;
  ssl_certificate_key  /home/youhuigo/https/server.key;

  location / {
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $http_host;
    proxy_set_header X-Nginx-Proxt true;
    proxy_pass https://youhui;
    proxy_redirect off;
  }
}

```
##### certbot来配置Https
> 免费的网站, 并且现在支持泛域名了! [参考博客](http://www.cnblogs.com/lidong94/p/7156839.html) | [参考博客](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04)  
> [Nginx反向代理https](http://linux.it.net.cn/e/server/nginx/2015/0131/12745.html)
```sh
  wget https://dl.eff.org/certbot-auto
  chmod a+x certbot-auto
  ./certbot-auto 进行安装 但是过程中会有一些设置，
  ./certbot-auto certonly --email kuangcp@aliyun.com --nginx -d wx.kuangcp.top 生成证书
```
_SSL 接收到一个超出最大准许长度的记录 要在端口后加上SSL nginx_
```conf
  upstream youhui {
    server 127.0.0.1:8080;
  }
  upstream git{
    server 127.0.0.1:55443;
  }
  server {
    listen 80;
    server_name git.kuangcp.top;
  location / {
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
      proxy_set_header Host $http_host;
      proxy_set_header X-Nginx-Proxt true;
      proxy_pass http://git;
      proxy_redirect off;
    }
    access_log /home/kuang/log/youhui.log;
  }
  server{
    listen 443 ssl;
    server_name wx.kuangcp.top
      ssl on;
      ssl_certificate  /etc/letsencrypt/live/wx.kuangcp.top/fullchain.pem;
      ssl_certificate_key  /etc/letsencrypt/live/wx.kuangcp.top/privkey.pem;
      ssl_trusted_certificate /etc/letsencrypt/live/wx.kuangcp.top/chain.pem;
      ssl_dhparam /etc/nginx/ssl/dhparam.pem;
      location / {
        proxy_pass https://youhui;
    }
    access_log /home/kuang/log/https.log;
  }
```

#### 配置Websocket反向代理
```
  # 配置连接的配置信息
  map $http_upgrade $connection_upgrade{
    default upgrade;
    ''  close;
  }
  upstream youhui {
    server 127.0.0.1:8888;
  }
  server {
    listen 80;
    server_name 127.0.0.1;
    location / {
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
      proxy_set_header Host $host;
      proxy_set_header X-Nginx-Proxt true;

      # 设置接收到的请求类型
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection $connection_upgrade;

      proxy_pass http://youhui;
      proxy_redirect off;
    proxy_read_timeout 300s;
    }
  }
```

### 防盗链


### 负载均衡
> [Nginx 反向代理 负载均衡 虚拟主机配置](https://segmentfault.com/a/1190000012479902)

### 跨域问题的配置
需要被跨域访问的一端， 添加如下配置
```
add_header Access-Control-Allow-Origin *;
add_header Access-Control-Allow-Headers X-Requested-With;
add_header Access-Control-Allow-Methods GET,POST,OPTIONS; 
```

#### 静态服务器将后台反代理
> 极大地省去了后台的配置！！
> [Nginx反向代理解决跨域问题](https://segmentfault.com/a/1190000012859206) | [nginx简易使用教程,使用nginx解决跨域问题](https://www.jianshu.com/p/05415981e5e5)
_配置静态端_
```
server {
    client_max_body_size 4G;
    listen  80;  ## listen for ipv4; this line is default and implied
    server_name view.kcp;
    location /api/ {
            # add_header 'Access-Control-Allow-Origin' '*';
            proxy_pass http://127.0.0.1:8889;
    }
    location / {
        root /home/kcp/IdeaProjects/Base/graduate/static;
    }
}
```
1. 将静态文件交由Nginx进行处理， 后台的服务统一用一个前缀和前台进行区分， 然后将服务端的真实host和ip或者域名配置进来
2. 这样在于前端看来就是访问 view.kcp/api 而已， 实际上访问的是 127.0.0.1:8889/api 
> 由于我原先用了nginx反向代理tomcat， 配置一个修改本地host得到的域名， 然后填在这里就没用了， 所以最好使用真实IP或者外网可访问的域名

****************************
## 问题
- 文件上传报错 413 
  - http{}中添加 `client_max_body_size 80M;`
