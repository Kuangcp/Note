---
title: Graph
date: 2024-10-13 18:28:55
tags: 
categories: 
---

💠

- 1. [图数据库](#图数据库)
- 2. [概念](#概念)
- 3. [QL 查询语言](#ql-查询语言)
    - 3.1. [Cypher](#cypher)
    - 3.2. [Gremlin](#gremlin)
    - 3.3. [SPARQL](#sparql)

💠 2024-11-14 14:23:28
****************************************
# 图数据库

Neo4j、OrientDB、ArangoDB、JanusGraph、HugeGraph、Dgraph、TigerGraph、Memgraph、NebulaGraph、SurrealDB、Cayley

> [DB-Engines Ranking - popularity ranking of graph DBMS](https://db-engines.com/en/ranking/graph+dbms)  

[memgraph](https://github.com/memgraph/memgraph)C++ 内存，Cypher查询，兼容Neo4j  
[vesoft-inc/nebula](https://github.com/vesoft-inc/nebula)C++ 分布式，nGQL查询语言，兼容部分Cypher语法  
[surrealdb/surrealdb](https://github.com/surrealdb/surrealdb)Rust 分布式， 类SQL/GraphQL查询 `偏业务应用`  
[dgraph-io/dgraph](https://github.com/dgraph-io/dgraph)Go 分布式，GraphQL查询 `偏业务应用`  
[orientechnologies/orientdb](https://github.com/orientechnologies/orientdb)`多模数据库（图，文档，全文索引）`  

[cayleygraph/cayley](https://github.com/cayleygraph/cayley)`Google开源`  

> 作为存储，支撑[知识图谱](/Ai/KnowledgeGraph.md)

# 概念

一个属性图是有向图，由顶点（Vertex），边（Edge），标签（Lable），关系类型（Relationship Type）和属性（Property）组成。

在属性图形中，节点和关系是最重要的实体，顶点也称作节点（Node），边也称作关系（Relationship）。
所有的节点是独立存在的，但是可以为节点设置标签，那么拥有相同标签的节点属于一个分组，也就是一个集合。关系通过关系类型来分组，类型相同的关系属于同一个集合。
节点可以有0个、1个或多个标签，但是关系必须设置关系类型，并且只能设置一个关系类型。

关系是有向的，关系的两端是起始节点和结束节点，通过有向的箭头来标识方向，节点之间的双向关系通过两个方向相反的关系来标识。

图算法操作库
> [jgrapht/jgrapht: Master repository for the JGraphT project](https://github.com/jgrapht/jgrapht)  

************************

# QL 查询语言
> [Neo4j - Cypher vs Gremlin query language - Stack Overflow](https://stackoverflow.com/questions/13824962/neo4j-cypher-vs-gremlin-query-language)  
> [opencypher/cypher-for-gremlin](https://github.com/opencypher/cypher-for-gremlin)  

> [一文了解各大图数据库查询语言（Gremlin vs Cypher vs nGQL）| 操作入门篇-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1594313)  

## Cypher
> [openCypher · openCypher](http://opencypher.org/) | [Cypher (query language) - Wikipedia](https://en.wikipedia.org/wiki/Cypher_(query_language))  

> [Cypher Cheat Sheet](https://neo4j.com/docs/cypher-cheat-sheet/5/aura-dbe/)`使用手册`  
> [Graph Database](https://github.com/albertoventurini/graphdb-intellij-plugin)  

Neo4j、RedisGraph、AgensGraph(PG+插件)

```c
    MATCH (n) RETURN n limit 10
    //  删除所有关系
    MATCH ()-[r]->() delete(r)
    // 查询 疾病 关联的 所有病征
    MATCH (d:疾病)-[:疾病的症状]->(s:疾病症状) WHERE d.名称 = '血栓形成' RETURN s
```

## Gremlin
> [Gremlin中文文档](https://tinkerpop-gremlin.cn/#traversal)  

Janus Graph、InfiniteGraph、Cosmos DB、Amazon Neptune

## SPARQL

> [SPARQL Query Language for RDF](https://www.w3.org/TR/rdf-sparql-query/)  