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

💠 2024-10-13 18:30:08
****************************************
# Neo4j
> [Neo4j Graph Database & Analytics | Graph Database Management System](https://neo4j.com/)  

## 安装

- `docker run  --publish=7474:7474 --publish=7687:7687 neo4j:5.24`
- [Neo4j: Can't log in: Neo.ClientError.Security.Unauthorized: The client is unauthorized due to authentication failure - Stack Overflow](https://stackoverflow.com/questions/53687901/neo4j-cant-log-in-neo-clienterror-security-unauthorized-the-client-is-unauth)  
`neo4j-admin dbms set-initial-password pwdtest123` 然后重启
    - 或者运行时添加环境变量 `--env NEO4J_AUTH=neo4j/neo4jpassword` 
- http://localhost:7474/browser/  bolt协议，用户名 neo4j 

### 驱动

Python

> [Neo4j Python Driver 5.25 — Neo4j Python Driver 5.25](https://neo4j.com/docs/api/python-driver/current/)  

************************

# 使用
> [快速入门 Neo4J教程](https://juejin.cn/post/7146016720388358181)  
> [Neo4j图数据库及Cypher语法基础 | Quantum Bit](https://www.eula.club/blogs/Neo4j%E5%9B%BE%E6%95%B0%E6%8D%AE%E5%BA%93%E5%8F%8ACypher%E8%AF%AD%E6%B3%95%E5%9F%BA%E7%A1%80.html)  

