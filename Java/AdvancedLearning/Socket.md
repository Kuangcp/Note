`目录 start`
 
- [Socket](#socket)
    - [基础](#基础)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Socket

## 基础
> 其实就是Socket [码农翻身:张大胖的socket ](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513387&idx=1&sn=99665948d0b968cf15c5e7a01ffe166c&chksm=80d679e8b7a1f0febad077b57e8ad73bfb4b08de74814c45e1b1bd61ab4017b5041942403afb&scene=21#wechat_redirect)

- 得到URL文件的输入流
    - `new URL(url).openStream()`

- 使用Linux编程开启web容器时`java.net.SocketException: 权限不够`
    - [参考博客](http://www.xuebuyuan.com/1432737.html)
    - 快速解决，不使用小于1024的端口即可，或者提权
   
