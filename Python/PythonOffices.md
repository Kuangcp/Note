---
title: Python 操作 Offices文档
date: 2018-12-15 12:08:39
tags: 
    - Offices
categories: 
    - Python
---

💠

- 1. [Offices文档](#offices文档)
    - 1.1. [Word](#word)
    - 1.2. [Excel](#excel)
        - 1.2.1. [xlrd](#xlrd)
        - 1.2.2. [pandas](#pandas)

💠 2024-04-22 20:07:13
****************************************
# Offices文档
## Word

## Excel 
> [Working with Excel Files in Python](http://www.python-excel.org/)
> [参考: Python-Excel 模块哪家强？](https://zhuanlan.zhihu.com/p/23998083)

> 大文件读取性能优化
- 问题： pandas读取 200M+ Excel时会耗时很久，思路将Excel转换为CSV

### xlrd 
> [Github addr](https://github.com/python-excel/xlrd)

```python
    import xlrd 

    data = xlrd.open_workbook('monster.xlsx')
    table = data.sheets()[0]   
    nrows = table.nrows
    for i in range(nrows):
        for cell in table.row_values(i):
            print(cell, ' | ', end='')
        print()
```

### pandas 
> [Official Site](http://pandas.pydata.org/)
