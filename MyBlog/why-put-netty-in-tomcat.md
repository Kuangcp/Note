`目录 start`
 
- [为何要将Netty放在Tomcat下](#为何要将netty放在tomcat下)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 为何要将Netty放在Tomcat下
> 2018-03-19 17:41:28

> [stackoverflow上的相关问题](https://stackoverflow.com/questions/3194508/is-hosting-a-netty-server-inside-tomcat-feasible-desirable/3200624#3200624)  
[知乎相关提问](https://www.zhihu.com/question/21472041)  
[Tomcat中如何使用netty的功能？](https://bbs.csdn.net/topics/390763179)  
[netty导致tomcat假死](http://blog.csdn.net/aishangyutian12/article/details/52251357)  
[tomcat为什么没有用netty作为底层通信框架？](https://www.zhihu.com/question/58796648)  
[请教，netty如何跟运行在tomcat中的web应用交互呢？ ](http://www.oschina.net/question/2762305_2191710)

- 然后我们老大就说 是因为Tomcat的环境具有一致性, 例如日志的方式以及日志文件的位置等等,
    - 因为是部署到甲方那边去, 所以不能由着自己性子来, 就不能用Docker来做环境的统一化部署了
    - 日志的一些配置什么的,能够在部署的时候进行修改和切换
- 例如运行环境
    - 感觉这个是最大的一个原因了, 因为甲方的电脑环境, 肯定都是乱七八糟什么玩意都有的, 对于我这个war来说的话, 只要有能正常运行的tomcat, 我就没有什么问题了
    - 但是如果抛开Tomcat, 弄成jar运行, 就比较麻烦了(主要还是为了日志和启动脚本,emmm)
- 还有就是为了使用丰富的协议, 例如Websocket Hybrid 等等, 就还是不能脱离Tomcat


>　2018-06-23 21:01:11
- 其实是可以直接将 Tomcat有关的依赖全部去除 Maven打包成jar, 配置下Main方法就能直接启动了, 而且资源消耗还少

