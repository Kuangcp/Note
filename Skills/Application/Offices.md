---
title: Offices
date: 2024-09-23 11:44:36
tags: 
categories: 
---


💠

- 1. [Excel](#excel)
- 2. [CSV](#csv)

💠 2024-09-23 11:44:36
****************************************

# Excel 
主要分为 xls 和 xlsx

- xls 专有二进制
- xlsx zip包

|  | xls | xlsx |
|:---|:---|:---|
| 年份 | 2003之前 | 2007及以后 |
| 格式 | 专有二进制CBF格式 | zip+xml |
| 兼容性 | 只能Office，其他软件有兼容问题 | 开放性格式，兼容更好 |
| 安全性 | 定制化 | 复用zip加密，更成熟 |
| 容量 | 65536行 乘 256列 | 1,048,576行 乘 16,384列 |

> [Excel 规范与限制](https://support.microsoft.com/zh-cn/office/excel-%E8%A7%84%E8%8C%83%E4%B8%8E%E9%99%90%E5%88%B6-1672b34d-7043-467e-8e27-269d656771c3)  

由于Excel最大行数为104w行，导出超量数据时，通常会拆分Sheet，或者退而使用csv格式

************************

# CSV
注意Windows平台会对文件带上BOM头，用于区分字符集编码 [BOM](/Skills/CS/CharacterEncoding.md#关于-bom)
对csv文件追加 EF BB BF 三个字节 以实现对Office的兼容，WPS会自动检测和切换解析的字符集编码
```java
FileOutputStream fos = new FileOutputStream(new File(this.csvFileAbsolutePath));
    	byte [] bs = { (byte)0xEF, (byte)0xBB, (byte)0xBF};   //new added
    	fos.write(bs);
    	fos.close();
```

