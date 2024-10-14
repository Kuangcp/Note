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

💠 2024-10-14 19:26:20
****************************************
# 图数据库

Neo4j、OrientDB、ArangoDB、JanusGraph、HugeGraph、Dgraph、TigerGraph

> [DB-Engines Ranking - popularity ranking of graph DBMS](https://db-engines.com/en/ranking/graph+dbms)  

# 概念

一个属性图是有向图，由顶点（Vertex），边（Edge），标签（Lable），关系类型（Relationship Type）和属性（Property）组成。

在属性图形中，节点和关系是最重要的实体，顶点也称作节点（Node），边也称作关系（Relationship）。
所有的节点是独立存在的，但是可以为节点设置标签，那么拥有相同标签的节点属于一个分组，也就是一个集合。关系通过关系类型来分组，类型相同的关系属于同一个集合。
节点可以有0个、1个或多个标签，但是关系必须设置关系类型，并且只能设置一个关系类型。

关系是有向的，关系的两端是起始节点和结束节点，通过有向的箭头来标识方向，节点之间的双向关系通过两个方向相反的关系来标识。

************************

# QL 查询语言
> [Neo4j - Cypher vs Gremlin query language - Stack Overflow](https://stackoverflow.com/questions/13824962/neo4j-cypher-vs-gremlin-query-language)  
> [opencypher/cypher-for-gremlin](https://github.com/opencypher/cypher-for-gremlin)  

## Cypher
> [Cypher Cheat Sheet](https://neo4j.com/docs/cypher-cheat-sheet/5/aura-dbe/)`使用手册`  
> [albertoventurini/graphdb-intellij-plugin](https://github.com/albertoventurini/graphdb-intellij-plugin)  

```c
    MATCH (n) RETURN (n)
    -- 查询 疾病 关联的 所有病征
    MATCH (d:疾病)-[:疾病的症状]->(s:疾病症状) WHERE d.名称 = '血栓形成' RETURN s
```

## Gremlin
> [Gremlin中文文档](https://tinkerpop-gremlin.cn/#traversal)  
