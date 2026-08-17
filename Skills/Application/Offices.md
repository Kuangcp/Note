---
title: Offices
date: 2024-09-23 11:44:36
tags: 
categories: 
---

💠

- 1. [Offices](#offices)
- 2. [Excel](#excel)
- 3. [CSV](#csv)

💠 2026-08-17 17:46:17
****************************************
# Offices
Ai领域将办公附件的解析成Markdown的需求更高频了

> [firecrawl/anydoc: Convert Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, and PDF to clean Markdown](https://github.com/firecrawl/anydoc)  

| 项目                                                                  | Stars | 支持格式                                   | 核心特点                                                                  | 最佳场景                       |
| ------------------------------------------------------------------- | ----- | -------------------------------------- | --------------------------------------------------------------------- | -------------------------- |
| **[MarkItDown](https://github.com/microsoft/markitdown)**           | ~172k | PDF/DOCX/PPTX/XLSX/图片/音频/EPUB/HTML/ZIP | 微软出品，万能转换，插件扩展，一行命令搞定                                                 | 快速批量处理、多格式统一入口             |
| **[MinerU](https://github.com/opendatalab/MinerU)**                 | ~77k  | PDF/DOCX/PPTX/XLSX/图片                  | 高精度结构恢复，公式→LaTeX，表格→HTML，84种语言OCR                                     | 学术论文、复杂报告、扫描件              |
| **[Docling](https://github.com/DS4SD/docling)**                     | ~64k  | PDF/DOCX/PPTX/XLSX/HTML/图片/音频          | IBM 出品，统一 `DoclingDocument` 中间表示，MCP Server，LangChain/LlamaIndex 原生集成 | 自托管 RAG Pipeline、Agent 工具链 |
| **[Marker](https://github.com/VikParuchuri/marker)**                | ~38k  | PDF/PPTX/DOCX/XLSX/EPUB/图片             | 速度快，布局保真，可选 LLM 二次清洗表格                                                | 批量转换、多语言文档、GPU 环境          |
| **[Unstructured](https://github.com/Unstructured-IO/unstructured)** | ~15k  | PDF/DOCX/PPTX/图片/HTML/邮件               | 输出语义元素类型（Title/Table/ListItem），适合精细 Chunking                          | 需要按元素类型做 Chunking 策略的 RAG  |
| **[Zerox](https://github.com/getomni-ai/zerox)**                    | ~12k  | PDF/图片                                 | 纯 VLM 方案，把每页当图片丢给视觉模型出 Markdown                                       | 排版极复杂的扫描件、手写体              |
| **[Dolphin](https://github.com/bytedance/dolphin)** (字节)            | 较新    | PDF/图片                                 | Vision Transformer 驱动，本地运行，布局还原好                                      | 本地部署、隐私要求高                 |
| **[PyMuPDF](https://github.com/pymupdf/PyMuPDF)**                   | ~6k   | PDF                                    | 底层 C 引擎，极快，支持坐标/字体/颜色级提取                                              | 大规模数字 PDF 预处理、PDF 操作       |
| [firecrawl/anydoc](https://github.com/firecrawl/anydoc)| ~15k+ |  Word/PPT/Excel/OpenDocument/RTF/EPUB/CSV/PDF（文本型）| Rust 引擎，中位数 4.4ms；14 种格式全覆盖；统一文档模型 + 单一序列化器，输出一致性最高；内容检测不依赖扩展名；Node.js/Python/CLI/WebAssembly 多绑定；零外部依赖；Agent Skill 一键接入  | 追求极致速度、格式全覆盖、零部署成本的本地转换；Agent 工具链直接集成| 

| 你的需求                         | 推荐工具              |
| ---------------------------- | ----------------- |
| 格式最全、安装最简单                   | **MarkItDown**    |
| 学术/技术 PDF，公式+表格要准            | **MinerU**        |
| 要接入 LangChain/LlamaIndex，自托管 | **Docling**       |
| 需要语义标签做精细 Chunking           | **Unstructured**  |
| 扫描件/手写/复杂排版                  | **Zerox**（VLM 方案） |
| 追求极致速度，数字 PDF 为主             | **PyMuPDF** + 后处理 |
| 想直接当 RAG 系统用                 | **RAGFlow**       |


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

