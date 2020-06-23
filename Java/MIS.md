---
title: MIS
date: 2018-12-20 10:42:29
tags: 
    - MIS
categories: 
    - Java
---

**目录 start**

1. [完整的MIS构建经验](#完整的mis构建经验)
    1. [MVC](#mvc)
        1. [持久化层](#持久化层)
            1. [数据库设计](#数据库设计)
            1. [Domain对象设计](#domain对象设计)
        1. [控制层](#控制层)
            1. [权限控制](#权限控制)
                1. [Session和Token的对比](#session和token的对比)
                1. [统一授权](#统一授权)
        1. [视图层](#视图层)

**目录 end**|_2020-06-24 02:06_|
****************************************
# 完整的MIS构建经验
> MIS: Management information system

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
> [码农翻身:从密码到token，一个授权的故事](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513744&idx=1&sn=93d0db97cfd67422bcd21c8afd00f495&chksm=80d67b53b7a1f24537fdc7c10eb2783357c1f8c65ad55601a722216d2293ae3fb7b1c16e5449&scene=21#wechat_redirect) 

### 视图层

*一种比较安全的iframe思路*
- 在主页面上写form iframe页面用来展示,这样的话,截图截不了长图,也不能保存文件,也不能打印出来(试了好多种方式去修改教务系统得到的结论)
