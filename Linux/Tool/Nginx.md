---
title: Nginx
date: 2018-12-15 12:05:09
tags: 
    - Nginx
categories: 
    - 工具
---

**目录 start**

1. [Nginx](#nginx)
    1. [Nginx的安装](#nginx的安装)
        1. [命令安装](#命令安装)
        1. [编译安装](#编译安装)
        1. [Docker安装](#docker安装)
    1. [命令参数](#命令参数)
1. [配置使用](#配置使用)
    1. [Location配置](#location配置)
    1. [本地静态文件Web服务器](#本地静态文件web服务器)
    1. [反向代理多个服务](#反向代理多个服务)
    1. [配置https](#配置https)
        1. [通过 certbot 配置 HTTPS](#通过-certbot-配置-https)
    1. [配置Websocket反向代理](#配置websocket反向代理)
    1. [防盗链](#防盗链)
    1. [gzip](#gzip)
    1. [负载均衡](#负载均衡)
    1. [跨域问题的配置](#跨域问题的配置)
        1. [静态服务器反代理后台接口](#静态服务器反代理后台接口)
1. [Nginx Plus](#nginx-plus)
1. [Keepalived](#keepalived)
1. [同类应用](#同类应用)
    1. [Caddy](#caddy)
    1. [Squid](#squid)
    1. [Varnish](#varnish)
    1. [HAProxy](#haproxy)
    1. [nuster](#nuster)
1. [Tips](#tips)

**目录 end**|_2020-12-29 22:15_|
****************************************
# Nginx

> [Official Site](https://www.nginx.com/)  
> [Tengine](http://tengine.taobao.org/)  

## Nginx的安装
### 命令安装

- 安装 `sudo apt install nginx`
- 启动服务 `sudo nginx`
  - 或者`sudo /etc/init.d/nginx start`
  - 或者  systemd 方式 `systemctl start nginx`
- 关闭 `sudo nginx -s quit`
  - 或者 `sudo /etc/init.d/nginx stop`
  - 或者 systemd 方式`systemctl stop nginx`

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

### Docker安装
> [nginx hub 官方镜像](https://hub.docker.com/r/library/nginx/)

## 命令参数
- `-s signal`
  - stop 停止
  - quit 退出
  - reopen 重新打开
  - reload 重载配置（修改配置文件常使用）
- `-t` 测试配置文件

************************

# 配置使用
> [Official Doc](https://www.nginx.com/resources/wiki/start/#pre-canned-configurations)  

> [知乎专栏](https://zhuanlan.zhihu.com/p/24524057)  
> [nginx基本配置](https://segmentfault.com/a/1190000002797601) | [ngrok nginx docker本地搭建服务器](https://fengqi.me/unix/409.html)
- [实验楼课程](https://www.shiyanlou.com/courses/95)

nginx 配置文件的语法是自己独有的语法, 比较像 shell, 里面有用到正则, 变量等概念

- 读取自定义目录配置: 
    - nginx.conf 中 http 块内添加 `include /etc/nginx/conf.d/*.conf;`
- 错误页面重定向 `error_page   404  /404.html;` 也可以填完整URL

## Location配置


************************

## 本地静态文件Web服务器
> [参考 nginx配置静态文件服务器 ](http://blog.yuansc.com/2015/04/29/nginx%E9%85%8D%E7%BD%AE%E9%9D%99%E6%80%81%E6%96%87%E4%BB%B6%E6%9C%8D%E5%8A%A1%E5%99%A8/)

```ini
  server {
    client_max_body_size 4G;
    listen  80; 
    # server_name static.me; # 如果需要使用域名 则需要在hosts文件配置
    root /home/mini/Sync;
    location / {
        autoindex on; # 显示索引
        autoindex_exact_size on; # 显示大小
	      autoindex_localtime on;  # 显示时间
    }
  }
```

1. 若出现403错误, 将 /etc/nginx/nginx.conf 中第一行的 `user nginx;` 改成可访问静态文件目录的用户即可
1. `配置为文本文件类型` 即 text/plain; 类型。例: 浏览器直接查看 code 目录下所有源代码
  ```ini
      location /code/ {
          # All files in it
          location ~* {
              add_header Content-Type text/plain;
          }
      }
  ```
如果有编码问题可配置成 `add_header Content-Type 'text/plain;charset=UTF-8';`
`location ~* /.*\.(py|md|sql)${}`

## 反向代理多个服务
`配置反向代理`
1. nginx 的 80 端口下：`/` 路径的请求转发到9991端口 `/myth` 转发到7898端口 

```ini
  upstream one {
    server 127.0.0.1:9991;
  }
  upstream two {
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

      proxy_pass http://one;
      proxy_redirect off;
    }
    
    location /myth{
      proxy_pass http://two;
      proxy_redirect off;
    }
  }
```

## 配置https
> [nginx搭建https服务](http://www.cnblogs.com/tintin1926/archive/2012/07/12/2587311.html) | [nginx http/2](http://letus.club/2016/04/08/nginx-http2-letsencrypt/)

> 自签发证书 `命令运行`
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

`配置HTTPS`

```ini
    upstream one {
        server 127.0.0.1:8888;
    }
    server {
        listen 443;
        server_name web.me;

        # 主要就是添加了这一块
        ssl on;
        ssl_certificate  /data/https/server.crt;
        ssl_certificate_key  /data/https/server.key;
        
        # http 转向 https
        return 302  https://$host$request_uri;

        location / {
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $http_host;
            proxy_set_header X-Nginx-Proxt true;
            proxy_pass https://one;
            proxy_redirect off;
        }
    }
```

### 通过 certbot 配置 HTTPS
> 免费的网站, 并且现在支持泛域名了[参考博客](http://www.cnblogs.com/lidong94/p/7156839.html) | [参考博客](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04)  
> [Nginx反向代理https](http://linux.it.net.cn/e/server/nginx/2015/0131/12745.html)

```sh
  wget https://dl.eff.org/certbot-auto
  chmod a+x certbot-auto
  ./certbot-auto #进行安装 但是过程中会有一些设置，
  ./certbot-auto certonly --email xxx@xxx --nginx -d xxx.domain # 生成 xxx.domain 证书
```
_SSL 接收到一个超出最大准许长度的记录 要在端口后加上SSL nginx_
```ini
  upstream one {
    server 127.0.0.1:8080;
  }

  server{
    listen 443 ssl;
    server_name xxx.domain
    access_log /data/log/https.log;
    
    # ssl配置
    ssl on;
    ssl_certificate  /etc/letsencrypt/live/xxx.domain/fullchain.pem;
    ssl_certificate_key  /etc/letsencrypt/live/xxx.domain/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/xxx.domain/chain.pem;
    ssl_dhparam /etc/nginx/ssl/dhparam.pem;

    location / {
        proxy_pass https://one;
    }
  }
```

## 配置Websocket反向代理
```ini
  # 配置连接的配置信息
  map $http_upgrade $connection_upgrade{
    default upgrade;
    ''  close;
  }
  upstream back_end {
    server 127.0.0.1:8888;
  }
  server {
    listen 80;
    server_name 127.0.0.1;
    location / {
      # 设置转发真实ip
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
      proxy_set_header Host $host;
      proxy_set_header X-Nginx-Proxt true;

      # 设置接收到的请求类型
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection $connection_upgrade;

      proxy_pass http://back_end;
      # 默认是 1.0 不支持 keepAlive
      proxy_http_version 1.1; 
      proxy_redirect off;
      proxy_read_timeout 300s;
    }
  }
```

## 防盗链

## gzip
> [nginx 启用 gzip压缩](https://www.jianshu.com/p/c5d1fc829855)

```conf
  gzip  on;
  gzip_comp_level 4;
  gzip_buffers 4 16k;
  gzip_http_version 1.1;
  gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
```

## 负载均衡
> [Nginx 反向代理 负载均衡 虚拟主机配置](https://segmentfault.com/a/1190000012479902)

## 跨域问题的配置
在需要被跨域访问的服务端，添加如下配置
```
    add_header Access-Control-Allow-Origin *;
    add_header Access-Control-Allow-Headers X-Requested-With;
    add_header Access-Control-Allow-Methods GET,POST,OPTIONS; 
```

### 静态服务器反代理后台接口
> [Nginx反向代理解决跨域问题](https://segmentfault.com/a/1190000012859206) | [nginx简易使用教程,使用nginx解决跨域问题](https://www.jianshu.com/p/05415981e5e5)

_配置静态端_
```ini
    server {
        client_max_body_size 4G;
        listen  80;  # listen for ipv4; this line is default and implied
        server_name static.me;
        
        location / {
            root /data/static;
            # proxy_pass http://127.0.0.1:8889/; 如果静态资源在别的端口上，这样配置也可以
        }

        location /api/ {
            # add_header 'Access-Control-Allow-Origin' '*';
            proxy_pass http://127.0.0.1:8889/; # 去除 api 路径，并访问后端
            # proxy_pass http://127.0.0.1:8889; 这种方式不会去除 /api/
        }
    }
```
1. 将静态文件交由Nginx进行处理， 后台的服务统一用一个前缀和前台进行区分， 然后将服务端的真实host和ip或者域名配置进来
2. 这样在于前端看来就是访问 static.me/api 而已， 实际上访问的是 127.0.0.1:8889/api 
> 注意，原先使用nginx反向代理tomcat，尝试配置后端为一个本地dns解析的域名。然后发现这是无法生效的，所以应该使用真实IP或公网域名

************************

# Nginx Plus
> 对标 F5 BIG-IP

> [5-reasons-switch-f5-big-ip-to-nginx-plus](https://www.nginx.com/blog/5-reasons-switch-f5-big-ip-to-nginx-plus/)

************************

# Keepalived
Keepalived软件起初是专为LVS负载均衡软件设计的，用来管理并监控LVS集群系统中各个服务节点的状态，后来又加入了可以实现高可用的VRRP功能。因此，Keepalived除了能够管理LVS软件外，还可以作为其他服务（例如：Nginx、Haproxy、MySQL等）的高可用解决方案软件。

> [参考: keepalived实现服务高可用](https://www.cnblogs.com/clsn/p/8052649.html)  

************************

# 同类应用
## Caddy
> [official website](https://caddyserver.com/)

具有丰富的插件支持, 配置简洁, 自动配置 HTTPS证书，相较于nginx资源消耗更多 吞吐量低一些

> [参考: 使用 Caddy 替代 Nginx，全站升级 https，配置更加简单](https://my.oschina.net/diamondfsd/blog/897301)

## Squid
> [Official](http://www.squid-cache.org)

## Varnish

## HAProxy
> [Official](https://www.haproxy.org/) 企业级工具

## nuster
> [Github](https://github.com/jiangwenyuan/nuster)`基于 HAProxy`


************************

# Tips
- 文件上传报错 413 
  - http{} 中添加 `client_max_body_size 80M;`
