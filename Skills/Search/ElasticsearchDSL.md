---
title: ElasticsearchDSL
date: 2026-10-26 17:08:27
tags: 
categories: 
---


💠

- 1. [概述](#概述)
- 2. [一、文本检索类 Query](#一文本检索类-query)
    - 2.1. [1. match](#1-match)
    - 2.2. [2. match_phrase](#2-match_phrase)
    - 2.3. [3. multi_match](#3-multi_match)
- 3. [二、精准匹配类 Query](#二精准匹配类-query)
    - 3.1. [4. term](#4-term)
    - 3.2. [5. ids](#5-ids)
    - 3.3. [6. regexp](#6-regexp)
- 4. [三、范围与通配查询](#三范围与通配查询)
    - 4.1. [7. range](#7-range)
    - 4.2. [8. exists](#8-exists)
    - 4.3. [9. wildcard](#9-wildcard)
- 5. [四、复合逻辑查询（bool）](#四复合逻辑查询bool)
    - 5.1. [bool](#bool)
    - 5.2. [nested](#nested)
    - 5.3. [has_child](#has_child)
- 6. [五、聚合分析（Aggregations）](#五聚合分析aggregations)
    - 6.1. [Bucket 聚合](#bucket-聚合)
        - 6.1.1. [terms](#terms)
        - 6.1.2. [histogram](#histogram)
        - 6.1.3. [date_range](#date_range)
    - 6.2. [Metric 聚合](#metric-聚合)
    - 6.3. [Pipeline 聚合](#pipeline-聚合)
- 7. [六、特殊场景查询](#六特殊场景查询)
    - 7.1. [geo](#geo)
    - 7.2. [function_score](#function_score)
- 8. [七、结果控制](#七结果控制)
    - 8.1. [sort](#sort)
    - 8.2. [highlight](#highlight)
    - 8.3. [分页与字段控制](#分页与字段控制)
- 9. [八、关键对比速查表](#八关键对比速查表)
    - 9.1. [文本匹配方式对比](#文本匹配方式对比)
    - 9.2. [term 与 match 对比](#term-与-match-对比)
    - 9.3. [must 与 filter 对比](#must-与-filter-对比)
    - 9.4. [terms 与 histogram 对比](#terms-与-histogram-对比)
- 10. [Mapping 设计要点](#mapping-设计要点)
    - 10.1. [双字段设计](#双字段设计)
    - 10.2. [避免深分页](#避免深分页)
- 11. [医疗多维检索最佳实践模板](#医疗多维检索最佳实践模板)

💠 2026-10-26 17:08:27
****************************************
#  概述

Elasticsearch 的 DSL（Domain Specific Language）基于 JSON，核心分为两大体系：

| 体系 | 职责 | 算分（Score） | 缓存 | 类比 SQL |
|------|------|:---:|:---:|---------|
| **Query（查询）** | 解决「像不像」- 全文匹配、语义相关度排序 | ✅ | ❌ | SELECT + ORDER BY |
| **Filter（过滤）** | 解决「是不是」- 硬性条件筛选，有缓存加速 | ❌ | ✅ | WHERE |

---

#  一、文本检索类 Query

## 1. match

对输入进行分词后逐个去倒排索引匹配。**最常用的文本匹配方式**。

```json
{ "match": { "field_name": { "query": "输入文本", "operator": "or" } } }
```

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `operator` | `"or"` = 任一命中；`"and"` = 全部命中 | `or` |
| `minimum_should_match` | 最少匹配的分词数，支持 `"75%"` 或 `-2` 等负数 | 动态 |
| `boost` | 字段权重，大于 1 提升相关性分数 | 1.0 |
| `fuzziness` | 模糊匹配，自动修正拼写错误，如 `"AUTO"` | `OFF` |
| `analyzer` | 指定使用的分词器 | 字段 Mapping 中定义 |

**示例：**
```json
{
  "match": {
    "abstract_en": {
      "query": "stroke thrombolysis",
      "operator": "and"
    }
  }
}
```

## 2. match_phrase

要求分词**顺序一致且紧挨着**，适合疾病名、手术名等专业术语。

```json
{ "match_phrase": { "field_name": { "query": "输入短语" } } }
```

| 参数 | 说明 |
|------|------|
| `slop` | 允许词语之间间隔的字数（偏移容忍度），默认 0 |
| `boost` | 字段权重 |

**示例：**
```json
{
  "match_phrase": {
    "article_title_en": "acute ischemic stroke",
    "slop": 2  // 允许词语间最多间隔 2 个其他词
  }
}
```

> ⚠️ `slop` 设为 0 时要求完全连续；增大 slop 可容错但降低精确度。

## 3. multi_match

在多个字段中同时搜索，有三种模式：

```json
{ "multi_match": { "query": "输入文本", "fields": ["field1", "field2"], "type": "best_fields" } }
```

三种 type 对比：

| type | 行为 | 适用场景 |
|------|------|----------|
| **`best_fields`** (默认) | 每个字段独立打分，取最高分 | 大部分场景，标题+摘要组合搜索 |
| **`most_fields`** | 跨所有字段统计命中数，总分累加 | 希望尽可能多地命中字段 |
| **`cross_fields`** | 把所有字段当作一个整体处理 | 同一概念分散在不同字段，如 "stroke Zhang"（疾病名 + 作者名） |

可选参数：`zero_terms_query`（分词后为空的行为）、`auto_generate_synonyms_phrase_query`（是否对同义词启用 phrase 匹配，默认 true）。

> 💡 `multi_match` + `"type": "phrase"` 底层等价于在每个字段上执行 `match_phrase`。

---

#  二、精准匹配类 Query

## 4. term

针对 **keyword 类型**、数字、布尔值、日期。**不会分词**。

```json
// 单个精确值
{ "term": { "field_name": "exact_value" } }

// 多选精确匹配（等价 SQL IN）
{ "terms": { "field_name": ["value1", "value2"] } }
```

| 注意点 | 说明 |
|--------|------|
| 不可用于 text 字段的 `_text` 部分 | 否则直接精确字符串匹配（无分词效果极差） |
| 应使用 `.keyword` | 如 `journal.raw` 或 `status.keyword` |
| terms 在 ES 7.x+ 推荐用数组写法 | 旧版逗号分隔写法已废弃 |

## 5. ids

```json
{ "ids": { "values": ["doc_id_1", "doc_id_2", "doc_id_3"] } }
```

## 6. regexp

```json
{ "regexp": { "field_name": "pattern.*" } }
```

⚠️ 慎用！正则查询性能较差，不支持 oneshot 以外的标志位优化。

---

#  三、范围与通配查询

## 7. range

适用于数字、日期、keyword 的区间过滤。

```json
{ "range": { "pub_year": { "gte": 2020, "lte": 2026 } } }
```

| 操作符 | 含义 |
|--------|------|
| `gt` | > 严格大于 |
| `gte` | ≥ 大于等于 |
| `lt` | < 严格小于 |
| `lte` | ≤ 小于等于 |

## 8. exists

```json
{ "exists": { "field": "author_name" } }
```

常用于筛选「某字段不为空」的文档。

## 9. wildcard

```json
{ "wildcard": { "field_name": { "value": "zhang*" } } }
```

`*` 代表零个或多个字符，`?` 代表单个字符。⚠️ 以通配符开头（如 `*abc`）会导致全扫描，性能极差，尽量避免。

---

#  四、复合逻辑查询（bool）

## bool

`bool` 是 ES DSL 的容器结构，将各类子查询组合为复杂的搜索逻辑。

```json
{
  "bool": {
    "must":     [ /* 必须匹配，贡献算分 */ ],
    "should":   [ /* 满足其一即可，贡献算分 */ ],
    "must_not": [ /* 必须不匹配，不算分 */ ],
    "filter":   [ /* 必须匹配，不算分但有缓存 */ ]
  }
}
```

**四个子句对比：**

| 子句 | 必须匹配？ | 贡献算分？ | 有缓存？ | 对应关系 |
|------|:---:|:---:|:---:|---------|
| `must` | ✅ | ✅ | ❌ | AND |
| `should` | 条件必需 ✅ | ✅ | ❌ | OR |
| `must_not` | ✅ | ❌ | ✅ | NOT |
| `filter` | ✅ | ❌ | ✅ | WHERE |

**minimum_should_match — should 触发门槛：** 当 `must` 和 `should` 并列时，默认 `should` 只需满足 **0** 个（仅用于加分）。若需强制至少 N 个命中：

```json
{
  "bool": {
    "must": [...],
    "should": [{ "match": {...} }, { "match": {...} }],
    "minimum_should_match": 1
  }
}
```

- 写数字：至少命中 N 个
- 写百分比：`"75%"` — 至少 75%
- 写负数：`"-2"` — 总数量减 2

## nested

针对 `nested` 类型字段，保持内部数组对象的独立性。

```json
{
  "nested": {
    "path": "comments",
    "query": { "bool": { "must": [
      { "match": { "comments.author": "john" } },
      { "match": { "comments.content": "great" } }
    ]}}
  }
}
```

> ⚠️ 不用 `nested` 时，ES 会把数组打散成独立的 doc，导致 `author=john AND content=great` 可能匹配到不同数组元素。

## has_child

```json
// 查找存在符合条件的子文档的父文档
{ "has_child": { "type": "review", "query": { "match": { "rating": 5 } } } }

// 查找存在符合条件父文档的子文档
{ "has_parent": { "type": "article", "query": { "match": { "title": "stroke" } } } }
```

---

#  五、聚合分析（Aggregations）

Aggregations 返回当前结果集的**统计信息**，常配合前端筛选项（漏斗导航）使用。与 `query` 同级。

## Bucket 聚合

### terms

```json
{ "aggs": { "by_doc_type": { "terms": { "field": "doc_type", "size": 10 } } } }
```

| 参数 | 说明 |
|------|------|
| `size` | 返回 top-N 个 bucket，默认 10 |
| `min_doc_count` | 最低文档数阈值，默认 1 |
| `order` | 排序规则，如 `{ "_count": "desc" }` |

### histogram


```json
{
  "aggs": {
    "year_distribution": {
      "date_histogram": {
        "field": "publication_time",
        "calendar_interval": "year"
      }
    },
    "score_distribution": {
      "histogram": {
        "field": "score",
        "interval": 10
      }
    }
  }
}
```

| 参数 | 说明 |
|------|------|
| `calendar_interval` | 日历单位：`second`/`minute`/`hour`/`day`/`month`/`quarter`/`year` |
| `fixed_interval` | 固定毫秒：`"1h"` / `"7d"` |
| `interval` | histogram 专用：步长数值 |
| `offset` | 偏移量，如 `"offset": 1h` 让桶从 :01 开始 |

### date_range

```json
{
  "aggs": {
    "age_ranges": {
      "date_range": {
        "field": "publication_time",
        "format": "yyyy-MM-dd",
        "ranges": [
          { "to": "2015-01-01" },
          { "from": "2015-01-01", "to": "2020-01-01" },
          { "from": "2020-01-01" }
        ]
      }
    }
  }
}
```

## Metric 聚合

| 聚合名 | 作用 | 示例 |
|--------|------|------|
| `avg` | 平均值 | `"avg_price": { "avg": { "field": "price" } }` |
| `sum` | 求和 | `"total_views": { "sum": { "field": "views" } }` |
| `min` / `max` | 最小/最大 | |
| `stats` | 同时返回 count/min/max/avg/sum | |
| `extended_stats` | stats + std_dev/variance | |
| `percentiles` | 百分位数 | |
| `cardinality` | 近似去重计数 | `"distinct_authors": { "cardinality": { "field": "author_id" } }` |
| `top_hits` | 组内 Top 文档 | 用于每组展示代表性文档 |

## Pipeline 聚合

```json
{
  "aggs": {
    "by_year": {
      "date_histogram": { "field": "date", "calendar_interval": "year" },
      "aggs": {
        "avg_temp": { "avg": { "field": "temp" } },
        "temp_moving_avg": {
          "moving_average": { "buckets_path": "avg_temp" }
        }
      }
    }
  }
}
```

常用 pipeline：`moving_average` / `derivative`（导数）/ `bucket_script`（自定义公式）

---

#  六、特殊场景查询

## geo

```json
{ "geo_shape": { "location": { "shape": { "type": "point", "coordinates": [116.4, 39.9] } } } }
{ "geo_distance": { "distance": "10km", "location": { "lat": 39.9, "lon": 116.4 } } }
```

## function_score

在默认 BM25 基础上叠加业务逻辑权重：

```json
{
  "function_score": {
    "query": { "match": { "title": "stroke" } },
    "functions": [
      { "field_value_factor": { "field": "view_count", "modifier": "log1p" } },
      { "random_score": {} }
    ],
    "score_mode": "multiply",
    "boost_mode": "multiply"
  }
}
```

常见 `score_mode`：`first` / `max` / `min` / `average` / `multiply` / `sum`
常见 `boost_mode`：`multiply` / `replace` / `sum` / `avg` / `max` / `min`

---

#  七、结果控制

## sort

```json
"sort": [
  { "publication_time": { "order": "desc" } },
  { "_score": { "order": "desc" } }
]
```

| 排序方式 | 语法 | 说明 |
|----------|------|------|
| 字段排序 | `{ "field": { "order": "asc" } }` | 数字/日期/keyword |
| 相关度排序 | `"_score"` | 基于 Query 得分 |
| 脚本排序 | `{ "_script": { "type": "long", "script": "...", "order": "desc" } }` | 复杂逻辑 |
| 距离排序 | `{ "_geo_distance": { "field": {...}, "order": "asc" } }` | 按距离由近到远 |

## highlight

```json
{
  "highlight": {
    "fields": {
      "article_title_en": { "type": "unified", "fragment_size": 150 },
      "abstract_en": {}
    }
  }
}
```

| 高亮类型 | 说明 |
|----------|------|
| `unified` (默认) | 最新统一高亮引擎，速度快 |
| `fvh` | 最快，要求 `term_vector: with_positions_offsets` |
| `plain` | 兜底方案，纯文本匹配，速度最慢 |

## 分页与字段控制

```json
{
  "from": 0,       // 跳过条数（默认 0）
  "size": 20,      // 返回条数（默认 10）
  "_source": ["title", "abstract"],  // 只返回指定字段（或 false 表示不返回 body）
  "track_total_hits": true   // ES 7+ 默认限制 10000，设为 false 禁用此限制
}
```

> ⚠️ **深分页坑**：`from + size` 超过 10000 时报错。大数据量导出请使用 `search_after`：

```json
// 首次查询（需带唯一排序字段）
{ "size": 20, "sort": [{ "publication_time": "desc" }, { "_id": "desc" }], "query": {...} }

// 后续查询（使用上一页最后一条的 sort 值）
{ "size": 20, "search_after": [1640995200000, "doc_abc123"], "sort": [...], "query": {...} }
```

---

#  八、关键对比速查表

## 文本匹配方式对比

| 特性 | `match` | `match_phrase` | `multi_match` |
|------|---------|----------------|---------------|
| 分词后匹配 | ✅ | ✅ | ✅ |
| 要求顺序一致 | ❌ | ✅ | 取决于 type |
| 要求紧挨着 | ❌ | ✅（受 slop 影响） | 取决于 type |
| 多字段搜索 | ❌ | ❌ | ✅ |
| 最佳场景 | 通用全文搜索 | 专业术语、固定搭配 | 跨字段联合搜索 |

## term 与 match 对比

| 特性 | `term` | `match` |
|------|--------|---------|
| 适用字段类型 | keyword / 数字 / 布尔 | text |
| 会分词吗？ | ❌ 精确匹配 | ✅ 先分词再匹配 |
| 适用场景 | 状态筛选、分类、ID | 标题、摘要内容搜索 |
| 写 "急性脑卒中" | 找包含完整 "急性脑卒中" 的值 | 分词后逐个匹配各词 |

## must 与 filter 对比

| 特性 | `must` | `filter` |
|------|--------|----------|
| 必须匹配？ | ✅ | ✅ |
| 贡献算分？ | ✅ | ❌ |
| 结果有缓存？ | ❌ | ✅（显著提速） |
| 适用场景 | 需要相关度排序的文字搜索 | 确定性硬过滤（年份、分区、类型） |

## terms 与 histogram 对比

| 特性 | `terms` | `date_histogram` |
|------|---------|-------------------|
| 分组依据 | 字段的实际取值 | 时间轴上的等距刻度 |
| 桶数量 | 取决于基数（可用 size 限制） | 由时间跨度 + interval 决定 |
| 适用场景 | 分类统计（期刊、语言、类型） | 时间趋势（年度发文、月度活跃度） |

---

#  Mapping 设计要点

## 双字段设计

对既需要搜索又需要精确筛选的字段，配置双属性：

```json
{
  "journal": {
    "type": "text",
    "fields": {
      "raw": { "type": "keyword" }
    }
  }
}
```

- `journal` → `match` / `match_phrase` → 全文检索
- `journal.raw` → `term` / `filter` / `terms agg` → 精确筛选与聚合

## 避免深分页

用户通常只看前几页。大数据量导出用 `search_after` 替代 `from/size`，ES 默认限制 `from + size ≤ 10000`。

---

#  医疗多维检索最佳实践模板

```json
{
  "size": 20,
  "from": 0,
  "track_scores": true,
  "query": {
    "bool": {
      "must": [
        // ── Query 层：语义匹配 + 算分排序 ──
        {
          "bool": {
            "must": [
              {
                "multi_match": {
                  "type": "phrase",
                  "query": "acute ischemic stroke",
                  "fields": ["article_title_en", "abstract_en"]
                }
              }
            ],
            "should": [
              {
                "multi_match": {
                  "type": "phrase",
                  "query": "thrombolytic therapy",
                  "fields": ["article_title_en", "abstract_en"]
                }
              }
            ],
            "minimum_should_match": 1
          }
        }
      ],
      "filter": [
        // ── Filter 层：确定性硬条件 + 缓存加速 ──
        { "term": { "status": "published" } },
        { "range": { "pub_year": { "gte": 2020, "lte": 2026 } } }
      ]
    }
  },
  "sort": [{ "publication_time": { "order": "desc" } }],
  "aggs": {
    // ── 聚合层：返回筛选项数量供前端渲染 ──
    "by_doc_type":  { "terms": { "field": "doc_type" } },
    "by_jcr_zone":  { "terms": { "field": "jcr_zone" } },
    "by_year":      { "date_histogram": { "field": "pub_year", "calendar_interval": "year" } }
  }
}
```

**分层思路：**
1. **Must 层**放 LLM 解析出的医学逻辑树（Query 算分）
2. **Filter 层**放用户二次勾选的确定条件（Filter 缓存）
3. **Sort 层**选择时间排序或 `_score` 按相关性排序
4. **Aggs 层**返回各类别的计数，驱动前端筛选漏斗
