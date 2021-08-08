# CDN
例如自己注册了域名 xxx.com, 此时需要CDN服务商帮你对网站静态资源做CDN加速, 通常会提供一个域名X，让 xxx.com CNAME到 X 域名上。
使用CNAME而不是A解析 好处是，X域名的A解析掌控权在CDN服务商，其可以依据地域，时间做动态调整，而不需要去 xxx.com 的控制台改解析。

