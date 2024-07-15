# 生态

> [参考: 除了Guava，Java开发者还值得了解的5个谷歌类库](http://www.techug.com/post/forget-guava-5-google-libraries-java-developers.html)
`Guice ErrorProne Truth Kythe Protobuf`

- [ ] canal


- [Hibernate](/Java/Ecosystem/Hibernate.md) | [Mybatis](/Java/Ecosystem/Mybatis.md) 对比
    - 有些设计思想是一致的，一二级缓存， Mybatis可以灵活自定义SQL，Hibernate也是可以的，相较现在这种分布式的环境下，单表操作两者没什么区别
    - 在Hibernate基础之上的[JPA](/Java/Ecosystem/JPA.md)能更简化开发, 在需要写复杂SQL的时候也是可以自定义的
    - 而且很多功能实际上用处不大了，一二级缓存，一对一一对多这样的映射 等等功能。缓存通常会交给分布式缓存实现，不会给表配置外键(为了性能以及避免频繁的死锁) 
    - 参考：数据库的诸多设计，账号，权限，约束，触发器，都是为 C/S 结构设计的，是以 C 端不可信做为假设前提的。B/S 模式安全边界前移到 web 服务层，应用与数据库之间是可信的，应用自行完成这些功能更加灵活。所以能不用就不用 [大家设计数据库时使用外键吗？](https://www.zhihu.com/question/19600081)

