---
title: Python 操作 Offices文档
date: 2018-12-15 12:08:39
tags: 
    - Offices
categories: 
    - Python
---

**目录 start**
 
1. [Offices文档](#offices文档)
    1. [Word](#word)
    1. [Excel](#excel)
        1. [xlrd](#xlrd)
        1. [pandas](#pandas)

**目录 end**|_2019-04-19 13:04_| [Kuangcp](https://github.com/Kuangcp/Note) | [yi-yun](https://github.com/yi-yun/Memo)
****************************************
# Offices文档
## Word

## Excel 
> [](http://www.python-excel.org/)
> [参考: Python-Excel 模块哪家强？](https://zhuanlan.zhihu.com/p/23998083)

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
