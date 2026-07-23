---
title: Offices
date: 2024-09-23 11:44:36
tags: 
categories: 
---

💠

- 1. [Excel](#excel)
- 2. [CSV](#csv)

💠 2026-07-23 09:45:02
****************************************

# Excel 
> [Microsoft Excel - Wikipedia](https://en.wikipedia.org/wiki/Microsoft_Excel)  

主要分为 xls、xlsx 和 xlsb

- xls 专有二进制
- xlsx zip包+xml
- xlsb zip包+二进制 (Binary Interchange File Format 12)

|  | xls | xlsx | xlsb |
|:---|:---|:---|:---|
| 年份 | 2003之前 | 2007及以后 | 2007及以后 |
| 格式 | 专有二进制CBF格式 | zip+xml | zip+二进制(BIFF12) |
| 兼容性 | 只能Office，其他软件有兼容问题 | 开放性格式，兼容更好 | 仅Excel/WPS，第三方库支持有限 |
| 安全性 | 定制化 | 复用zip加密，更成熟 | 复用zip加密，更成熟 |
| 容量 | 65536行 乘 256列 | 1,048,576行 乘 16,384列 | 1,048,576行 乘 16,384列 |
| 性能 | 中等 | 慢（xml解析开销） | 快（二进制读写，省去xml解析） |
| 体积 | 中等 | 较大 | 小（比xlsx小30%-50%） |

> [Excel 规范与限制](https://support.microsoft.com/zh-cn/office/excel-%E8%A7%84%E8%8C%83%E4%B8%8E%E9%99%90%E5%88%B6-1672b34d-7043-467e-8e27-269d656771c3)  

由于Excel工作表最大行数为104w行(xls，xlsx，xlsb都受此限制)，导出超量数据时，通常会拆分Sheet，或者退而使用csv格式。

xlsb 还独有 **Power Pivot 数据模型**（VertiPaq 引擎）可突破此限制——它不在工作表中存数据，而是用内存列式压缩引擎（xVelocity），支持上亿行，仅受物理内存约束，查询使用 DAX 公式而非 Excel 公式。
- 但是无论是 Java 的 Apache POI、EasyExcel，还是 Go 语言的 Excelize，全网没有任何一个开源的第三方轻量级库，支持直接在 Linux 服务器上通过代码把数据直接写进 Excel 的 Power Pivot 数据模型中。因为这属于微软底层高度加密的 SQL Server Analysis Services 内核技术。
- 曲线方式可以将数据导出到csv，创建一个空的 xlsb 文件（读取同目录的csv，配置 Excel 属性为“打开时自动刷新数据”），zip交付给用户

************************

# CSV
注意Windows平台会对文件带上BOM头，用于区分字符集编码 [BOM](/Skills/CS/CharacterEncoding.md#关于-bom)  
对csv文件追加 EF BB BF 三个字节 以实现对Office的兼容，而WPS会自动检测和切换解析的字符集编码
```java
	FileOutputStream fos = new FileOutputStream(new File(this.csvFileAbsolutePath));
			byte [] bs = { (byte)0xEF, (byte)0xBB, (byte)0xBF};   //new added
			fos.write(bs);
			fos.close();
```

