---
title: 时间
date: 2018-12-20 10:44:57
tags: 
    - Time
categories: 
    - 计算机基础
---

**目录 start**

1. [时间](#时间)
    1. [基础概念](#基础概念)
        1. [GMT](#gmt)
        1. [UTC](#utc)
        1. [CST](#cst)
        1. [DST](#dst)

**目录 end**|_2020-06-24 02:06_|
****************************************
# 时间
## 基础概念
### GMT
> 格林尼治标准时间（Greenwich Mean Time，GMT）是指位于伦敦郊区的皇家格林尼治天文台的标准时间，因为本初子午线被定义在通过那里的经线。

为了方便，在不需要精确到秒的情况下，通常将 GMT 和 UTC 视作等同。但 UTC 更加科学更加精确，它是以原子时为基础，在时刻上尽量接近世界时的一种时间计量系统。它的出现是现代社会对于精确计时的需要。

### UTC
> [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)

协调世界时，又称世界统一时间、世界标准时间、国际协调时间, 也会被称为"Zulu time"

> 实际地区无关的夏令时缩写：
- 主要的夏令时包括EDT(Eastern Daylight Time)，CDT(Central Daylight Time )，PDT(Pacific Daylight Time)。非夏令时包括CST(Central Standard Time)，PST(Pacific Standard Time)。

### CDT

中国标准时间（CST）和中国夏令时(CDT)

1986年至1991年，中华人民共和国在全国范围实行了六年夏令时，每年从4月中旬的第一个星期日2时整（北京时间）到9月中旬第一个星期日的凌晨2时整（北京夏令时）。除1986
年因是实行夏令时的第一年，从5月4日开始到9月14日结束外，其它年份均按规定的时段施行。1992年4月5日后不再实行。

### CST
> 中国处于东八区 所以是 UTC+8 

但是CST其实可以表示四个时区, 被MySQL中的CST坑了才发现到这个`十四个小时问题`, 但是Linux以及大多数软件中的CST都是指UTC+8

| 时间 | 全称 | 时区 |
|:----|:----|:----|
| 美国中部时间     | Central Standard Time (USA)       | UTC-6:00
| 澳大利亚中部时间 | Central Standard Time (Australia) |  UTC+9:30
| 中国标准时间     | China Standard Time               | UTC+8:00
| 古巴标准时间     | Cuba Standard Time                | UTC-4:00

### DST
> DST是Daylight Saving Time的缩写，称为阳光节约时，在我国称为夏时制，又称夏令时，是一种为节约能源而人为调整地方时间的制度。

> [Daylight saving time](https://en.wikipedia.org/wiki/Daylight_saving_time)

