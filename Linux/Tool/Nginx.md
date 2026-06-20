---
title: Nginx
date: 2018-12-15 12:05:09
tags: 
    - Nginx
categories: 
    - 工具
---

💠

- 1. [Nginx](#nginx)
    - 1.1. [Nginx的安装](#nginx的安装)
        - 1.1.1. [命令安装](#命令安装)
        - 1.1.2. [编译安装](#编译安装)
        - 1.1.3. [Docker安装](#docker安装)
    - 1.2. [命令参数](#命令参数)
- 2. [可视化管理工具](#可视化管理工具)
- 3. [内置变量](#内置变量)
- 4. [配置使用](#配置使用)
    - 4.1. [静态资源Web服务器](#静态资源web服务器)
    - 4.2. [4层转发 TCP/UDP](#4层转发-tcpudp)
    - 4.3. [反向代理多个服务](#反向代理多个服务)
        - 4.3.1. [静态资源+反代理后端](#静态资源反代理后端)
        - 4.3.2. [前后端分离时避免跨域](#前后端分离时避免跨域)
    - 4.4. [配置https](#配置https)
        - 4.4.1. [自签发证书](#自签发证书)
        - 4.4.2. [通过 certbot 配置 HTTPS](#通过-certbot-配置-https)
    - 4.5. [配置Websocket反向代理](#配置websocket反向代理)
    - 4.6. [代理-HTTP转发](#代理-http转发)
    - 4.7. [防盗链](#防盗链)
    - 4.8. [gzip](#gzip)
    - 4.9. [负载均衡](#负载均衡)
        - 4.9.1. [负载均衡策略](#负载均衡策略)
    - 4.10. [SSE](#sse)
- 5. [Nginx Plus](#nginx-plus)
- 6. [Keepalived](#keepalived)
- 7. [同类应用](#同类应用)
    - 7.1. [Caddy](#caddy)
    - 7.2. [Squid](#squid)
    - 7.3. [Varnish](#varnish)
    - 7.4. [HAProxy](#haproxy)
    - 7.5. [nuster](#nuster)
- 8. [Tips](#tips)

💠 2026-06-14 01:06:31
****************************************
# Nginx

> [Official Site](https://www.nginx.com/) | [Official Doc](https://docs.nginx.com)  
> [Tengine](http://tengine.taobao.org/)  

> [nginx-tutorial](https://github.com/dunwu/nginx-tutorial)

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
# 可视化管理工具
> [nginxWebUI](https://github.com/cym1102/nginxWebUI)  
> [nginx-proxy-manager ](https://github.com/NginxProxyManager/nginx-proxy-manager)  
> [0xJacky/nginx-ui: Yet another WebUI for Nginx](https://github.com/0xJacky/nginx-ui)`go+js`
  
************************
# 内置变量
> [Official Doc](https://nginx.org/en/docs/varindex.html) | [Nginx 内置变量](https://www.jianshu.com/p/deccac3a4fd0)

- `$remote_addr` 客户端地址
- `$remote_port` 客户端端口

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

> [Nginx反向代理，当后端为Https时的一些细节和原理](https://blog.dianduidian.com/post/nginx%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%BD%93%E5%90%8E%E7%AB%AF%E4%B8%BAhttps%E6%97%B6%E7%9A%84%E4%B8%80%E4%BA%9B%E7%BB%86%E8%8A%82%E5%92%8C%E5%8E%9F%E7%90%86/)  

nginx提供Http服务，但是反向代理了HTTPS地址时 需要注意证书的一致性问题

************************

## 静态资源Web服务器
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

## 4层转发 TCP/UDP

```ini
# 和 http 同级 
stream {
    upstream backend {
        server 192.168.1.100:3306 weight=1;
        server 192.168.1.101:3306 weight=1;
    }

    server {
        listen 3306;                 # 对外暴露的 TCP 端口
        proxy_pass backend;          # 4 层转发
        proxy_timeout 60s;           # 下游连接超时
        proxy_connect_timeout 10s;   # 上游建连超时
        so_keepalive on;             # TCP 保活
    }
}
```

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

### 静态资源+反代理后端
> [Nginx反向代理解决跨域问题](https://segmentfault.com/a/1190000012859206) | [nginx简易使用教程,使用nginx解决跨域问题](https://www.jianshu.com/p/05415981e5e5)

_配置统一出口_
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
            proxy_pass http://127.0.0.1:8889/; # 去除请求的 api 路径，并访问后端
            # proxy_pass http://127.0.0.1:8889; 这种方式不会去除 /api/
        }

        location /api/a-service {
          proxy_pass http://127.0.0.1:8889/a-service; # 移除 /api/ 路径，保留a-service （api路径下多个服务时使用此类型配置）
        }
    }
```
1. 将静态文件交由Nginx进行处理， 后台的服务统一用一个前缀和前台进行区分， 然后将服务端的真实host和ip或者域名配置进来
2. 这样在于前端看来就是访问 static.me/api 而已， 实际上访问的是 127.0.0.1:8889/api 
> 注意，原先使用nginx反向代理tomcat，尝试配置后端为一个本地dns解析的域名。然后发现这是无法生效的，所以应该使用真实IP或公网域名

### 前后端分离时避免跨域
在需要被跨域访问的服务端，添加如下配置
```ini
    add_header Access-Control-Allow-Origin *;
    add_header Access-Control-Allow-Headers X-Requested-With;
    add_header Access-Control-Allow-Methods GET,POST,OPTIONS; 
```

************************

## 配置https
> [nginx搭建https服务](http://www.cnblogs.com/tintin1926/archive/2012/07/12/2587311.html) | [nginx http/2](http://letus.club/2016/04/08/nginx-http2-letsencrypt/)

如果使用caddy就会很简单，它会自动续签 lets crypt

### 自签发证书
- [Linux: 自签发证书](/Linux/Base/LinuxNetwork.md#自签发证书)

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
            proxy_pass http://one; # 注意Nginx已经配置了SSL，后端只需支持http协议即可
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

      proxy_pass http://back_end; # 末尾不能加任何uri
      # 不设置的话 默认是 1.0 就会不支持 keepAlive
      proxy_http_version 1.1; 
      proxy_redirect off;
      proxy_read_timeout 300s; # 大于心跳时间即可
      proxy_buffering off;     # 关闭缓冲，实时帧，否则会出现ws消息业务意义上的粘包
      proxy_cache off;         # 禁用缓存
    }
  }
```

- 如果没有按这里的配置，单纯做proxy_pass配置 会出现只有101状态码 只代表“握手”成功，但是没有建立 WS 帧隧道
- 可以通过在服务端执行 sudo tcpdump -i any -nn port 8888 来看是否有完整的握手和后续消息的tcp包

> 绕过Grafana，免密登录，需要预先生成key
```ini
map $http_upgrade $connection_upgrade{
    default upgrade;
    ''  close;
}

  # http://grafana-user.test/d/spring_boot_21/shang-shu-tai-jian-kong-mian-ban?orgId=1
server {
    listen 80;
    server_name  grafana-user.test;

    location / {
        proxy_pass http://192.168.1.1:9091/;
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Connection "";
        proxy_set_header Authorization "Bearer xxxxx";
        # add_header X-Frame-Options SAMEORIGIN;
        proxy_hide_header X-Frame-Options;
    }
    location /api/live/ws {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_set_header X-Nginx-Proxt true;
        
        proxy_set_header Authorization "Bearer cccc";
        
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
        
        proxy_http_version 1.1; 
        proxy_redirect off;
        proxy_read_timeout 300s;

        proxy_pass http://192.168.1.1:9091;
    }
}
```

## 代理-HTTP转发
> 例如 aaa.com 需要VPN等方式才能访问，Nginx所在的主机能访问，就可以这么配置，然后配置DNS将 aaa.com 解析到Nginx的主机上，就可以实现其他客户机不安装VPN 直接访问 aaa.com

```ini
  server {
    server_name aaa.com;
    listen 80;
    location / {
      proxy_pass http://aaa.com;
      proxy_set_header Host $host:$server_port;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
    }
  }
```

## 防盗链

## gzip
> [nginx 启用 gzip压缩](https://www.jianshu.com/p/c5d1fc829855)

```conf
  gzip  on;
  gzip_comp_level 4; # 缺省值
  gzip_buffers 4 16k;
  gzip_http_version 1.1; # 缺省值
  gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
```

当前Nginx代理上游开启了gzip的服务，并解压其gzip响应

```conf
server {
	server_name xxxx.cn;
	location / {
    proxy_set_header Accept-Encoding ""; # 禁用代理请求开启gzip
    gzip off; # 禁用gzip
		proxy_pass http://x.x.x.x:8080/;
	}
}
```

> 遇到一个奇怪的问题：Nginx层开启gzip http的response的header里也有标识开启了gzip，但是body并没有被压缩，导致浏览器报错 ERR_CONTENT_DECODING_FAILED 无法解析response引发业务故障

## 负载均衡
> [Nginx 反向代理 负载均衡 虚拟主机配置](https://segmentfault.com/a/1190000012479902)

分为四层和七层： 
- 在四层只依据ip的报文转发（修改进入时目的ip`从nginx改成upstream的IP`，修改返回时发送ip）
- 在七层依据数据内容做转发，例如按http请求后缀做转发 *.jpg 到A服务器 *.jsp 到B服务器

### 负载均衡策略
> [Doc: Http Load Balancer](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/)

1. Round Robin：
    - 默认方式，对所有backend无差别按序轮询, 如果backend宕机会自动移除掉
1. Weight：
    - 对所有backend按权重进行轮询，权重越高分发到的请求就越多，默认值为1。适合硬件差别比较大的多个节点
    ```ini
        #动态服务器组
        upstream dynamic_server {
            server localhost:8080 weight=2;
            server localhost:8081;
            server localhost:8082 backup;
            server localhost:8083 max_fails=3 fail_timeout=20s;
        }
    ```
1. Least Connections(least_conn): 
    - 依据每个backend当前活跃连接数，将请求分发到连接数最少的backend上，此时会考虑backend的weight权重比例
    - upstream配置块中在首行添加 `least_conn;`即可
1. IP Hash(ip_hash): 对请求来源IP地址计算hash值，通过某种映射（例如取余，详细可查看ip_hash相关源码）分发至对应backend
    - upstream配置块中在首行添加 `ip_hash;`即可
1. Generic Hash(hash): 用户自定义资源（例如URL）计算hash完成分发，可选consistent关键字支持`一致性hash`特性

************************

> Q & A
1. 如果负载均衡了A B两个节点，请求进入了A节点后，立马移除了对A节点的负载均衡，该请求是否能正常执行
    - 能正常执行，假如此时请求A失败，例如A节点宕机, 请求还会转移至B节点（failover）
1. 如果负载均衡了A B两个节点, A节点宕机了，后续请求是否还会分发到A节点
    - 不会，原理： TODO


## SSE
由于http开启缓冲能提高内存使用率，但是这个设置和sse 消息流推送是违背的 否则会出现粘包拆包问题，需要关闭 

```
proxy_set_header Connection '';
proxy_http_version 1.1;
chunked_transfer_encoding off;

proxy_buffering off;
proxy_cache off;
```

```ini
# 关闭代理缓冲。当设置为off时，Nginx会立即将客户端请求发送到后端服务器，并立即将从后端服务器接收到的响应发送回客户端。
proxy_buffering off;
# 启用分块传输编码。分块传输编码允许服务器为动态生成的内容分块发送数据，而不需要预先知道内容的大小。
chunked_transfer_encoding on;
# 开启TCP_NOPUSH，这告诉Nginx在数据包发送到客户端之前，尽可能地发送数据。这通常在sendfile使用时配合使用，可以提高网络效率。
tcp_nopush on;
# 开启TCP_NODELAY，这告诉Nginx不延迟发送数据，立即发送小数据包。在某些情况下，这可以减少网络的延迟。
tcp_nodelay on;
# 设置保持连接的超时时间，这里设置为120秒。如果在这段时间内，客户端和服务器之间没有进一步的通信，连接将被关闭。
keepalive_timeout 120;
```

以及如果开了 HTTP2 

```ini
server {
    listen 443 ssl http2; # 👈 1. 确保外部访问支持 HTTP/2
    server_name ://yourcompany.com;

    location / {
        proxy_pass http://llm_backend_cluster;
        
        # 👈 2. 核心：Nginx 1.25+ 已经支持 proxy_http_version 2; 
        # 如果是老版本 Nginx，默认 proxy 只走 1.1，多路复用会失效。
        proxy_http_version 1.1; 
        
        # 👈 3. 针对 SSE 流式特性的必备优化，防止 Nginx 缓存 Token
        proxy_set_header Connection "";
        proxy_buffering off;
        proxy_cache off;
    }
}

```

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
- request_time 比实际时间长 [Nginx的延迟关闭](http://shibing.github.io/2016/11/18/nginx%E7%9A%84%E5%BB%B6%E8%BF%9F%E5%85%B3%E9%97%AD-lingering-close/)`lingering_timeout`


************************
access 日志中 upstream 408状态码 本身返回的502 实际上upstream没收到请求

> [Random HTTP 408 on POST requests and no body is transferred](https://stackoverflow.com/questions/70856800/random-http-408-on-post-requests-and-no-body-is-transferred)  


