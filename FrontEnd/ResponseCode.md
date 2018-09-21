`目录 start`
 
- [HTTP状态码大全](#http状态码大全)
    - [标准扩展码](#标准扩展码)
        - [1xx Informational 信息化](#1xx-informational-信息化)
        - [2xx Success 成功](#2xx-success-成功)
        - [3xx Redirection 重定向](#3xx-redirection-重定向)
        - [4xx Client Error 客户端错误](#4xx-client-error-客户端错误)
        - [5xx Server Error 服务器错误](#5xx-server-error-服务器错误)
    - [非官方扩展码](#非官方扩展码)
    - [互联网信息服务扩展状态码](#互联网信息服务扩展状态码)
    - [NGINX 扩展状态码](#nginx-扩展状态码)
    - [七牛扩展状态码](#七牛扩展状态码)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# HTTP状态码大全
> [HTTP状态码](http://www.runoob.com/http/http-status-codes.html)
> [HTTP状态码百度百科](https://baike.baidu.com/item/HTTP%E7%8A%B6%E6%80%81%E7%A0%81)
## 标准扩展码

### 1xx Informational 信息化
```
100 Continue 继续
101 Switching Protocols 交换协议
102 Processing 继续处理
```
### 2xx Success 成功
```
200 OK
201 Created 创建
202 Accepted 已接受
203 Non-Authoritative Information 非授权信息
204 No Content 无内容
205 Reset Content 重置内容
206 Partial Content 部分内容
207 Multi-Status 多状态
208 Already Reported 已报告
226 IMIM Used 使用的
```
### 3xx Redirection 重定向
> [HTTP返回码中301与302的区别  ](http://blog.163.com/darkness@yeah/blog/static/131774484201221495129735/)

```
300 Multiple Choices 多种选择
301 Moved Permanently 永久移动
302 Found 发现 代表暂时性转移(Temporarily Moved )。
303 See Other 查看其它
304 Not Modified 未修改,使用缓存
305 Use Proxy 使用代理
306 Switch Proxy 开关代理
307 Temporary Redirect 临时重定向
308 Permanent Redirect 永久重定向
```
### 4xx Client Error 客户端错误
```
400 Bad Request 错误的请求
401 Unauthorized 未授权
402 Payment Required 需要付费
403Forbidden 拒绝访问
404 Not Found 未找到
405 Method Not Allowed 不允许的方法
406 Not Acceptable 不可接受
407 Proxy Authentication Required 代理服务器需要身份验证
408 Request Timeout 请求超时
409 Conflict 冲突
410 Gone 完成
411 Length Required 需要长度
412 Precondition Failed 前提条件失败
413 Payload Too Large 负载过大
414 URI Too Long 太长
415 Unsupported Media Type 不支持的媒体类型
416 Range Not Satisfiable 的范围不合适
417 Expectation Failed 预期失败
418 I'm a teapot 我是一个茶壶
421 Misdirected Request 误导请求
422 Unprocessable Entity 无法处理的实体
423 Locked 锁定
424 Failed Dependency 失败的依赖
426 Upgrade Required 升级所需
428 Precondition Required 所需的先决条件
429 Too Many Requests 太多的请求
431 Request Header Fields Too Large 请求头字段太大
451 Unavailable For Legal Reasons 不可出于法律原因
```

### 5xx Server Error 服务器错误
```
500 Internal Server Error 内部服务器错误
501 Not Implemented 未执行
502 Bad Gateway 错误的网关
503 Service Unavailable 服务不可用
504 Gateway Timeout 网关超时
505 HTTP Version Not Supported 不支持HTTP版本
506 Variant Also Negotiates 变体也进行协商
507 Insufficient Storage 存储空间不足
508 Loop Detected 检测到循环
510 Not Extended 不延长
511 Network Authentication Required 网络需要身份验证
```

## 非官方扩展码
```
103 Checkpoint 检查点
420 Method Failure (Spring Framework) 故障的方法（Spring框架）
420 Enhance Your Calm (Twitter) 增强您的平静（微博）
450 Blocked by Windows Parental Controls (Microsoft) 被Windows阻止家长控制（微软）
498 Invalid Token (Esri) 无效的令牌（ESRI的）
499 Token Required (Esri) 令牌必需（ESRI的）
499 Request has been forbidden by antivirus 请求已被禁止反病毒
509 Bandwidth Limit Exceeded (Apache Web Server/cPanel) 超出带宽限制（Apache的Web服务器/的cPanel）
530 Site is frozen 网站被冻结
```
## 互联网信息服务扩展状态码
```
440 Login Timeout 登录超时
449 Retry With 重新发送带
451 Redirect 重定向
```

## NGINX 扩展状态码
```
444 No Response 没有响应
495 SSL Certificate Error 证书错误
496 SSL Certificate Required证书要求
497 HTTP Request Sent to HTTPS Port 发送到HTTPS端口请求
499 Client Closed Request 客户端请求关闭
```

## 七牛扩展状态码
```
298 部分操作执行成功。
419 用户账号被冻结。
478 镜像回源失败。 主要指镜像源服务器出现异常。
573 单个资源访问频率过高
579 上传成功但是回调失败。 包括业务服务器异常；七牛服务器异常；服务器间网络异常。
599 服务端操作失败。
608 资源内容被修改。
612 指定资源不存在或已被删除。
614 目标资源已存在。
630 已创建的空间数量达到上限，无法创建新空间。
631 指定空间不存在。
640 调用列举资源 (list) 接口时，指定非法的marker参数。
701 在断点续上传过程中，后续上传接收地址不正确或ctx信息已过期。
```
