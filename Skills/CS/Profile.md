`目录 start`
 
- [配置文件](#配置文件)
    - [conf或者ini](#conf或者ini)
    - [properties](#properties)
    - [XML](#xml)
    - [YAML](#yaml)
        - [Java使用](#java使用)
    - [JSON](#json)
        - [Jackson](#jackson)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 配置文件

## conf或者ini
```
[main]
debug=true
[client]
timeOut=10
```

## properties

## XML
> 可阅读性强, 结构清晰, 但是太繁杂, 信息承载比重小

## YAML
> yaml is ain't markup language

- [入门博客](http://blog.csdn.net/liukuan73/article/details/78031693)
- [Python使用YML](http://www.cnblogs.com/c9com/archive/2013/01/05/2845539.html)

### Java使用
- Springboot将这种配置文件引入了我的视野，使用这个用来自定义配置文件要特别注意采用小写（不然影响反射中set方法）

- [Jackson操作yaml](https://dzone.com/articles/read-yaml-in-java-with-jackson)

## JSON
> [Google 规范](https://github.com/darcyliu/google-styleguide/blob/master/JSONStyleGuide.md)

### Jackson
- [Jackcon 注解的讲解](http://blog.csdn.net/sdyy321/article/details/40298081)
