`目录 start`
 
- [完整的MIS构建经验](#完整的mis构建经验)
    - [MVC](#mvc)
        - [持久化层](#持久化层)
            - [数据库设计](#数据库设计)
            - [Domain对象设计](#domain对象设计)
        - [控制层](#控制层)
            - [权限控制](#权限控制)
                - [Session和Token的对比](#session和token的对比)
                - [统一授权](#统一授权)
        - [视图层](#视图层)
    - [分布式](#分布式)
        - [CAP定理](#cap定理)

`目录 end` |_2018-08-26_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 完整的MIS构建经验

- [OAuth 2.0授权框架](https://github.com/jeansfish/RFC6749.zh-cn/blob/master/index.md)


## MVC
### 持久化层
#### 数据库设计
> 一种极端是将业务也放在了数据库里, 使用大量的存储过程和函数  
> 一种是将约束都放在了业务层, 数据库没有外键约束

#### Domain对象设计
1. 首先名称不能使用Java或者数据库中的的关键字 class group table from 等等
    - 班级就用ClassGroup吧
1. 实体间的关系映射注意死循环

### 控制层
> 只是映射好URL, 调用对应的Service

#### 权限控制

##### Session和Token的对比
> [码农翻身:干掉状态：从session到token ](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513566&idx=1&sn=a2688cadbe9c8042ff1abbdf04a8bd5e&chksm=80d67a1db7a1f30b28b93ed2ab29edfbf982b780433e4bfd178e3cc52cb1f9100cc8f923db4f&scene=21#wechat_redirect)

- token优势是前后端分离做起来比较简单,session在于实现快,但是容易有CSRF问题,其实token也是会有的
    - 如果登录和页面的跳转路由还是由后端控制的，那么Token的实现就有点没有那么必要了。（不过为了安全性能够防范CSRF）

##### 统一授权
> [码农翻身:从密码到token，一个授权的故事](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513744&idx=1&sn=93d0db97cfd67422bcd21c8afd00f495&chksm=80d67b53b7a1f24537fdc7c10eb2783357c1f8c65ad55601a722216d2293ae3fb7b1c16e5449&scene=21#wechat_redirect) | [自己收集到的相关文档](/API_DOC.md#登录授权)

### 视图层

*一种比较安全的iframe思路*
- 在主页面上写form iframe页面用来展示,这样的话,截图截不了长图,也不能保存文件,也不能打印出来(试了好多种方式去修改教务系统得到的结论)

## 分布式
### CAP定理
> [码农翻身:张大胖和CAP定理](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513560&idx=1&sn=ba861726537c57bd34253cbce010b5fe&chksm=80d67a1bb7a1f30df37905ce979504aa132dcaef59075577ff52f45f057734825a59f6de75c9&scene=21#wechat_redirect)
