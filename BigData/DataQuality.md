---
title: DataQuality
date: 2024-05-07 19:32:22
tags: 
categories: 
---

💠

- 1. [Data Quality](#data-quality)
- 2. [Topic](#topic)
    - 2.1. [大宽表周期滚动更新时 不同版本间的数据质量分析](#大宽表周期滚动更新时-不同版本间的数据质量分析)

💠 2024-05-08 20:26:55
****************************************
# Data Quality


************************

# Topic

> [数据一致性比对（番外）](https://developer.aliyun.com/article/1204687)  

## 大宽表周期滚动更新时 不同版本间的数据质量分析
背景： A1表 A2表 表结构一致，内容数据有区别，例如A1包含1月的销售数据 A2包含1-2月销售数据。  
诉求： 由于A1 A2表都是经过ETL过程产生的数据表，需要检查确认A2表中1月的数据是否存在较大程度的偏离，以及SKU变化情况（新增，删除，变更，一致）需要生成A1A2所有列加差异状态列拼接的结果大宽表。  

注意前提：业务主键所标识的数据不能重复
实现方案：

A： 
1. 依据业务主键做两个表之间的集合差运算先找出 新增和删除
1. 选择A1表作为驱动表， 分批找出 not in 新增和删除的主键， 即变更或一致的主键数据， 依据A1表数据拎出A2表数据，Java应用层计算得到差异细节，写入到结果表

B：
1. `A1 LEFT JOIN A2` 一步得到结果大宽表, 强依赖底层数据引擎的大宽表JOIN能力，像CK就不适合。
1. 扫描结果大宽表，应用层计算差异，更新到差异状态列