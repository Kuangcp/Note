---
title: MarkDown
date: 2018-11-21 10:56:52
tags: 
categories: 
---

💠

- 1. [Markdown](#markdown)
    - 1.1. [基本格式](#基本格式)
        - 1.1.1. [居中](#居中)
    - 1.2. [基本元素](#基本元素)
        - 1.2.1. [文本](#文本)
        - 1.2.2. [分割线](#分割线)
        - 1.2.3. [链接](#链接)
        - 1.2.4. [图片](#图片)
        - 1.2.5. [列表](#列表)
        - 1.2.6. [头信息](#头信息)
        - 1.2.7. [代码块](#代码块)
    - 1.3. [流程图](#流程图)
    - 1.4. [SVG](#svg)
    - 1.5. [Github](#github)

💠 2024-03-23 17:52:21
****************************************
# Markdown
> [Github: markdown](https://guides.github.com/features/mastering-markdown/) 
> [ Markdown 编辑器语法指南](https://segmentfault.com/markdown)
> [Markdown教程](http://www.markdown.cn/)  
> [CSDN的Markdown案例](https://github.com/kuangcp/Notes/blob/master/Article/CSDN的Markdown案例.md)

> [Github: markup](https://github.com/github/markup)`丰富的标记性文本格式` |

> [Github: emoji character](https://www.webfx.com/tools/emoji-cheat-sheet/)

**************

## 基本格式
### 居中
```
    <center> 

    </center>
```
> 注意这俩标签前后都需要一行空行

## 基本元素
### 文本
1. 斜体 `*content*` 或者 `_content_`
1. 粗体 `**content**`
1. 删除 `~content~`
1. 粗斜 `***content***` 或者 `___content___`

### 分割线
- `***`
- `---`
- `___`

### 链接
1. `[name](url)` 推荐
1. [[name|url]
1. [name][targetNum]
    - 末尾: [targetNum]: url

### 图片
1. `![description](url)`
1. ![description][targetNum]
    - 末尾: [targetNum]: url "description"

### 列表
> 注意符号和内容之间都要有空格隔开

- **无序列表** : `- ` 或  `* `
- **有序列表** : `1. ` (markdown渲染的时候会自动排序 1 也可以换成任意非0正整数)

- 列表中还能嵌套 引用, 例如: `- > content` 或者 `>1. content`

> 关于有序列表中的块状结构破坏有序性的问题
- 当需要出现代码块, 图片, 表格 等块状结构时, 只需将整体进行缩进, 就可以保证后续的有序性  

例如: 
1. a
    ```sh
    echo hi
    ```
1. b

### 头信息
> 仅仅是github的语法, gitlab 当成了代码块进行渲染, gitee 则完全是乱的.

```yml
    --- 
    layout: post
    title: "关于WEB开发中引入javascript文件方式的一点建议"
    wordpress_id: 12
    wordpress_url: http://wsria.com/?p=12
    date: 2009-02-07 18:24:46 +08:00
    category: javascript
    tags: 
    - jquery
    - prototype
    - dojo
    - ext
    - 建议
    ---
```
- 可以有多种数据结构 yml  ini 
    - 一般用于描述文件元信息; 静态博客生成器用于生成博客的标签等信息;

### 代码块
1. 行级 反引号
1. 多行 三个反引号独立行进行包裹

************************

## 流程图
- [plantUML](http://plantuml.com)

## SVG 
- 作为图片引入 `![]()`
- HTML代码块引入
    ```
    <div width="100%" style="overflow-x: auto;"> 
        <svg width="140" height="170">
            <title>SVG Sample</title>
            <desc>This is a sample to use SVG in markdown on the website cnblogs.</desc>
            <circle cx="70" cy="95" r="50" style="stroke: black; fill: none;"/>
        </svg>
    </div>
    ```

************************

## Github 
> [比较全面的Github格式 GFM](https://github.com/guodongxiaren/README)  
> [Github readme stats](https://github.com/anuraghazra/github-readme-stats)  
> [Awesome Badges](https://github.com/Envoy-VC/awesome-badges)  

_目录规则（页内跳转）_

- `[](#标题名)` 不需要编码
- `【Name】`看成Name 忽略这对符号 
    - 同理还有  `/` 中英文的 逗号 句号 冒号 小数点 问号
- 空格会变成 - 

_文件内容_
- 一行显示上 58列 就要换行
- 行末加上两个空格即是换行, 直接回车键换行是没有用的
- *todo* 未完成 `[ ]` 已完成 `[X]`

_列表的折叠写法_
```
    ### Demo
    <details>
    <summary>查看全部</summary>
    * [`chunk`](#chunk)
    </details>
```

_md文件的头属性_
```
    ---
    title: 泛型
    tags: Java, 泛型
    ---
```

```diff
+ python
- java
```
