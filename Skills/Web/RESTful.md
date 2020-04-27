---
title: RESTful
date: 2018-12-20 10:43:20
tags: 
    - Restful
categories: 
    - Web
---

**目录 start**

1. [RESTful风格](#restful风格)
    1. [Rest](#rest)
        1. [资源 Resources](#资源-resources)
        1. [表现层 Representation](#表现层-representation)
        1. [状态转化 State Transfer](#状态转化-state-transfer)

**目录 end**|_2020-04-27 23:42_|
****************************************
# RESTful风格
> 要理解RESTful架构，最好的方法就是去理解Representational State Transfer这个词组到底是什么意思，它的每一个词代表了什么涵义。

> [知乎: 使用通俗的语言解释RESTful](https://www.zhihu.com/question/28557115)

> [参考:  RPC vs REST vs GraphQL ](https://segmentfault.com/a/1190000013961872)  

## Rest
> Representational State Transfer  表现层状态转化  
> 如果一个架构符合REST原则，就称它为RESTful架构。

> [参考自 使用 Python 和 Flask 设计 RESTful API](http://www.pythondoc.com/flask-restful/first.html)
- 六条设计规范定义了一个 REST 系统的特点:
    - 客户端-服务器: 客户端和服务器之间隔离，服务器提供服务，客户端进行消费。
    - 无状态: 从客户端到服务器的每个请求都必须包含理解请求所必需的信息。换句话说， 服务器不会存储客户端上一次请求的信息用来给下一次使用。
    - 可缓存: 服务器必须明示客户端请求能否缓存。
    - 分层系统: 客户端和服务器之间的通信应该以一种标准的方式，就是中间层代替服务器做出响应的时候，客户端不需要做任何变动。
    - 统一的接口: 服务器和客户端的通信方法必须是统一的。
    - 按需编码: 服务器可以提供可执行代码或脚本，为客户端在它们的环境中执行。这个约束是唯一一个是可选的。


> [参考: 理解RESTful架构](http://www.ruanyifeng.com/blog/2011/09/restful.html)

> [RESTful Best Practices](https://segmentfault.com/a/1190000002949234)
> [理解本真的REST架构风格](http://www.infoq.com/cn/articles/understanding-restful-style)
> [RESTful风格的springMVC](https://blog.csdn.net/wy5612087/article/details/52149249)

### 资源 Resources
REST的名称"表现层状态转化"中，省略了主语。"表现层"其实指的是"资源"（Resources）的"表现层"。
所谓"资源"，就是网络上的一个实体，或者说是网络上的一个具体信息。它可以是一段文本、一张图片、一首歌曲、一种服务，总之就是一个具体的实在。
你可以用一个URI（统一资源定位符）指向它，每种资源对应一个特定的URI。要获取这个资源，访问它的URI就可以，因此URI就成了每一个资源的地址或独一无二的识别符。
所谓"上网"，就是与互联网上一系列的"资源"互动，调用它的URI。

### 表现层 Representation

"资源"是一种信息实体，它可以有多种外在表现形式。我们把"资源"具体呈现出来的形式，叫做它的"表现层"（Representation）。
比如，文本可以用txt格式表现，也可以用HTML格式、XML格式、JSON格式表现，甚至可以采用二进制格式；图片可以用JPG格式表现，也可以用PNG格式表现。
URI只代表资源的实体，不代表它的形式。严格地说，有些网址最后的".html"后缀名是不必要的，因为这个后缀名表示格式，属于"表现层"范畴，而URI应该只代表"资源"的位置。
它的具体表现形式，应该在HTTP请求的头信息中用Accept和Content-Type字段指定，这两个字段才是对"表现层"的描述。

### 状态转化 State Transfer
访问一个网站，就代表了客户端和服务器的一个互动过程。在这个过程中，势必涉及到数据和状态的变化。
互联网通信协议HTTP协议，是一个无状态协议。这意味着，所有的状态都保存在服务器端。因此，如果客户端想要操作服务器，必须通过某种手段，让服务器端发生"状态转化"（State Transfer）。
而这种转化是建立在表现层之上的，所以就是"表现层状态转化"。客户端用到的手段，只能是HTTP协议。具体来说，就是HTTP协议里面，四个表示操作方式的动词：GET、POST、PUT、DELETE。
它们分别对应四种基本操作：GET用来获取资源，POST用来新建资源（也可以用于更新资源），PUT用来更新资源，DELETE用来删除资源。

*****************

> [阮一峰 RESTful API 设计指南](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)`很细致的说明该规范`


- [ ]  需要整理和计划如何规范化实现这个接口
