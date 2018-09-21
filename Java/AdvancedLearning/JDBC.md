`目录 start`
 
- [JDBC](#jdbc)
    - [Java内置数据库Derby](#java内置数据库derby)

`目录 end` |_2018-08-09_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# JDBC
> [码农翻身:JDBC的诞生](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513438&idx=1&sn=2967d595bb7d4ffdd2dacd3ab7501bbd&chksm=80d6799db7a1f08b27dc97650434fb2fc0e2570628945db99d9300a99e52828fd05c42fdb441&scene=21#wechat_redirect)

- 基础的批量操作SQL ` pstmt.executeBatch(); //批量执行`

注册driver
创建 connection
创建 statement
执行获取 Resultset
处理返回结果 resultst

Statement 和 PrepareStatement 的区别， 掌握PrepareStatement的主要用法(推荐使用)

## Java内置数据库Derby

> [Derby](http://db.apache.org/derby/derby_comm.html)

