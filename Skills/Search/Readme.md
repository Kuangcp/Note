# 搜索

[从零开始构建全文搜索引擎](https://mojotv.cn/go/golang-full-text-search-enginec)

> [typesense](https://github.com/typesense/typesense)
> [zincsearch](https://zincsearch-docs.zinc.dev/)  
> [opensearch-project/OpenSearch: 🔎 Open source distributed and RESTful search engine.](https://github.com/opensearch-project/OpenSearch)  


## RRF

| 项目     | 说明                                    |
| ------ | ------------------------------------- |
| **全称** | Reciprocal Rank Fusion（倒数排名融合）        |
| **作用** | **把多个检索结果（向量 + 关键词 + 结构化）融合成一个排序列表**  |
| **公式** | `score = Σ(1 / (k + rank_i))`，k 常取 60 |
| **优势** | 无需训练、对结果分布不敏感、**比加权融合更鲁棒**            |
| **场景** | **RAG 混合检索**：向量语义 + BM25 关键词 + 过滤条件   |

示例：同一查询，向量检索返回 [A, B, C]，BM25 返回 [B, A, D]  → RRF 融合后排序：[B, A, C, D]，取各自优势，去重归一。


# 推荐

