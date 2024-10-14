---
title: Graph
date: 2024-10-13 18:28:55
tags: 
categories: 
---

💠

- 1. [图数据库](#图数据库)
- 2. [QL 查询语言](#ql-查询语言)
    - 2.1. [Cypher](#cypher)

💠 2024-10-14 16:13:01
****************************************
# 图数据库

Neo4j、OrientDB、ArangoDB、JanusGraph、HugeGraph、Dgraph、TigerGraph

> [DB-Engines Ranking - popularity ranking of graph DBMS](https://db-engines.com/en/ranking/graph+dbms)  

************************

# QL 查询语言
## Cypher
> [Cypher Cheat Sheet](https://neo4j.com/docs/cypher-cheat-sheet/5/aura-dbe/)`使用手册`  
> [albertoventurini/graphdb-intellij-plugin](https://github.com/albertoventurini/graphdb-intellij-plugin)  

```c
    MATCH (n) RETURN (n)
    -- 查询 疾病 关联的 所有病征
    MATCH (d:疾病)-[:疾病的症状]->(s:疾病症状) WHERE d.名称 = '血栓形成' RETURN s
```