---
title: Neo4j
date: 2024-10-13 17:59:27
tags: 
categories: 
---


💠

- 1. [Neo4j](#neo4j)
    - 1.1. [安装](#安装)

💠 2024-10-13 17:59:27
****************************************
# Neo4j
> [Neo4j Graph Database & Analytics | Graph Database Management System](https://neo4j.com/)  


## 安装

- `docker run  --publish=7474:7474 --publish=7687:7687 neo4j:5.24`
- [Neo4j: Can't log in: Neo.ClientError.Security.Unauthorized: The client is unauthorized due to authentication failure - Stack Overflow](https://stackoverflow.com/questions/53687901/neo4j-cant-log-in-neo-clienterror-security-unauthorized-the-client-is-unauth)  
`neo4j-admin dbms set-initial-password pwdtest123` 然后重启
- http://localhost:7474/browser/  bolt协议，用户名 neo4j 

> [快速入门 Neo4J教程](https://juejin.cn/post/7146016720388358181)  

