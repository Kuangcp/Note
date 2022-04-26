---
title: ELK.md
date: 2019-03-19 17:59:18
tags: 
categories: 
---

**目录 start**

1. [ELK](#elk)
    1. [ElasticSearch](#elasticsearch)
    1. [Logstash](#logstash)

**目录 end**|_2020-08-18 17:49_|
****************************************
# ELK

> [5 Good Reasons to Use a Log Server ](https://reflectoring.io/log-server/)

- 整体架构为Logstash采集日志输出文件，制定解析格式，存入ES，Kibana用于展示
- 此时可以优化日志输出，区分不同的字段（时间，线程，方法），方便解析为不同字段，索引优化

************************

## ElasticSearch
> [ElasticSearch](/Skills/Search/Elasticsearch.md)

> UI
1. [appbaseio/dejavu](https://github.com/appbaseio/dejavu)
1. [cars10/elasticvue](https://github.com/cars10/elasticvue)
1. cerebro

************************

## Logstash
> [Official Doc](https://www.elastic.co/guide/en/logstash/current/index.html)  
> [Logstash 最佳实践](https://doc.yonyoucloud.com/doc/logstash-best-practice-cn/index.html)  

常用于 数据的采集 过滤，配置文件使用 Ruby 编写

1. input  数据源 通过 input plugin 可支持 JDBC Kafka 文件流 HTTP 等等
1. filter 数据源做处理 类似于 Java8 中 Stream 表达式 中的map filter等函数，对数据进行处理
1. ouput 输出数据源 对应 output plugin 

> 解析嵌套[JSON](https://www.elastic.co/guide/en/logstash/current/plugins-filters-json.html) message内content
```ruby
filter{
    json {
        source => "message"
        target => "parsed"
        add_field => {"content" => "%{[parsed][content]}"}
        remove_field => ["parsed"]
    }
}
```

> 增减字段
```ruby
filter {
    mutate {
        add_field => { "[@metadata][program]" => "%{program}" }
        remove_field => "[program]"
    }
}
```

- 使用指定配置文件且自动重载 bin/logstash -f app.conf --config.reload.automatic 
