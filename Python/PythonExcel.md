---
title: PythonExcel.md
date: 
tags: 
catagroies: 
---

**目录 start**
 
1. [Handle Excel](#handle-excel)
    1. [xlrd](#xlrd)
    1. [pandas](#pandas)

**目录 end**|_2018-12-13 12:06_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Handle Excel 

> [参考: Python-Excel 模块哪家强？](https://zhuanlan.zhihu.com/p/23998083)

## xlrd 
> [Github addr](https://github.com/python-excel/xlrd)

```python
import xlrd 

data = xlrd.open_workbook('vip-config.xlsx')
table = data.sheets()[0]   
nrows = table.nrows
for i in range(nrows):
    if i == 3:
        continue;
    for cell in table.row_values(i):
        print(cell)
```

## pandas 
> [Official Site](http://pandas.pydata.org/)
