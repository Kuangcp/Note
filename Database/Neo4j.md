---
title: Neo4j
date: 2024-10-13 17:59:27
tags: 
categories: 
---

💠

- 1. [Neo4j](#neo4j)
    - 1.1. [安装](#安装)
        - 1.1.1. [驱动](#驱动)
- 2. [使用](#使用)
    - 2.1. [结构](#结构)
    - 2.2. [Schema](#schema)
        - 2.2.1. [索引](#索引)
        - 2.2.2. [约束](#约束)
        - 2.2.3. [统计信息](#统计信息)
    - 2.3. [Pattern](#pattern)
- 3. [应用](#应用)

💠 2024-10-14 19:26:20
****************************************
# Neo4j
> [Neo4j Graph Database & Analytics | Graph Database Management System](https://neo4j.com/)  

## 安装

- `docker run  --publish=7474:7474 --publish=7687:7687 neo4j:5.24`
- [Neo4j: Can't log in: Neo.ClientError.Security.Unauthorized: The client is unauthorized due to authentication failure - Stack Overflow](https://stackoverflow.com/questions/53687901/neo4j-cant-log-in-neo-clienterror-security-unauthorized-the-client-is-unauth)  
`neo4j-admin dbms set-initial-password pwdtest123` 然后重启
    - 或者运行时添加环境变量 `--env NEO4J_AUTH=neo4j/neo4jpassword` 
- http://localhost:7474/browser/  bolt协议，用户名 neo4j 
- 登录后 Favorites 菜单下的 Sample Scripts 可以快速了解常用查询语句

> 注意
- 社区版本不支持命令 create database xxx 只能使用默认的 neo4j

### 驱动

Python

> [Neo4j Python Driver 5.25 — Neo4j Python Driver 5.25](https://neo4j.com/docs/api/python-driver/current/)  

************************

# 使用
> [快速入门 Neo4J教程](https://juejin.cn/post/7146016720388358181)  
> [Neo4j图数据库及Cypher语法基础 | Quantum Bit](https://www.eula.club/blogs/Neo4j%E5%9B%BE%E6%95%B0%E6%8D%AE%E5%BA%93%E5%8F%8ACypher%E8%AF%AD%E6%B3%95%E5%9F%BA%E7%A1%80.html)  


> [Neo4j - 悦光阴 - 博客园](https://www.cnblogs.com/ljhdo/tag/Neo4j/)  
> [Neo4j 第二篇：图形数据库 - 悦光阴 - 博客园](https://www.cnblogs.com/ljhdo/p/5178225.html)  


## 结构
使用Neo4j创建的图（Graph）基于属性图模型，在该模型中，每个实体都有ID（Identity）唯一标识，每个节点由标签（Lable）分组，每个关系都有一个唯一的关系类型。

标签用于对节点进行分组，相当于节点的类型，拥有相同标签的节点属于同一个分组。一个节点可以拥有零个，一个或多个标签，因此，一个节点可以属于多个分组。对分组进行查询，能够缩小查询的节点范围，提高查询的性能。
属性是一个键值对（Key/Value），用于为节点或关系提供扩展的信息。一般情况下，每个节点都有name属性，用于命名节点，通常情况下，name属性的值是唯一的。

## Schema
Neo4j的模式（Schema）通常是指索引、约束和统计，通过创建模式，Neo4j能够获得查询性能的提升和建模的便利；Neo4j数据库的模式可选的，也可以是无模式的。

### 索引
> [Indexes - Cypher Manual](https://neo4j.com/docs/cypher-manual/current/indexes/)  

```
    CREATE INDEX ON :Person(firstname)
    CREATE INDEX ON :Person(firstname, surname)
```

### 约束
> [Constraints - Cypher Manual](https://neo4j.com/docs/cypher-manual/current/constraints/)  

### 统计信息

当使用Cypher查询图形数据库时，Cypher脚本被编译成一个执行计划，执行该执行计划获得查询结果。为了生成一个性能优化的执行计划，Neo4j需要收集统计信息以对查询进行优化。当统计信息变化到一定的赋值时，Neo4j需要重新生成执行计划，以保证Cypher查询是性能优化的

## Pattern
模式（Pattern）和模式匹配（Match）是Cypher的核心，使用模式来描述所需数据的形状，该模式使用属性图的结构来描述，通常使用小括号()表示节点，-->表示关系，-[]->表示关系和关系的类型，箭头表示关系的方向。

节点模式 (Variable:Lable1:Lable2{Key1:Value1,Key2,Value2}) 
- 节点可以有多个标签用于匹配，{}内则是匹配节点的属性值

关系模式  在属性图中，节点之间存在关系，关系通过[]表示，节点之间的关系通过箭头()-[]->()表示
- 关联节点模式: 节点之间通过关系联系在一下，由于关系具有方向性，因此，-->表示存在有向的关系，--表示存在关联，不指定关系的方向
    - `(a)-[r]->(b)` ：该模式用于描述节点a和b之间存在有向的关系r，
    - `(a)-->(b)`：该模式用于描述a和b之间存在有向关系；
- 变长路径的模式: 从一个节点，通过直接关系，连接到另外一个节点，这个过程叫遍历，经过的节点和关系的组合叫做路径（Path），路径是由节点和关系的有序组合
    - `(a)-->(b)`：是步长为1的路径，节点a和b之间有关系直接关联；
    - `(a)-->()-->(b)`：是步长为2的路径，从节点a，经过两个关系和一个节点，到达节点b；
    - Cypher语言支持变长路径的模式，变长路径的表示方式是：`[*N..M]`，N和M表示路径长度的最小值和最大值

************************

# 应用
> [hokaso/hocassian-people-neo4j: NoSQL可视化人脉图谱项目](https://github.com/hokaso/hocassian-people-neo4j)  
> [NTDXYG/Neo4j: 基于电影知识图谱和微信小程序的智能问答系统](https://github.com/NTDXYG/Neo4j)  
> [lonngxiang/Knowledge-map-of-family-tree （姓氏家族家谱知识图谱）](https://github.com/lonngxiang/Knowledge-map-of-family-tree)  


