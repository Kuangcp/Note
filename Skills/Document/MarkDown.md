`目录 start`
 
- [Markdown](#markdown)
    - [基础格式](#基础格式)
        - [链接](#链接)
        - [图片](#图片)
        - [列表](#列表)
        - [头信息](#头信息)
    - [流程图](#流程图)
    - [Github](#github)

`目录 end` |_2018-08-30_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Markdown
> [markup](https://github.com/github/markup)`丰富的标记性文本格式`  
> [Markdown教程](http://www.markdown.cn/)  
> [CSDN的Markdown案例](https://github.com/kuangcp/Notes/blob/master/Article/CSDN的Markdown案例.md)
> [ Markdown 编辑器语法指南](https://segmentfault.com/markdown)

**************
## 基础格式

### 链接
1. [name](url) 推荐
1. [[name|url]]
1. [name][targetNum]
    - 末尾: [targetNum]: url

### 图片
1. ![description](url)
1. ![description][targetNum]
    - 末尾: [targetNum]: url "description"

### 列表
> 注意符号和内容之间都要有空格隔开

- **无序列表** : `- ` 或  `* `
- **有序列表** : `1. ` (markdown渲染的时候会自动排序 1 也可以换成任意非0正整数)

- 列表中还能嵌套 引用, 例如: `- > `
### 头信息
```
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
## 流程图
```flow
st=>start: Start
e=>end
op=>operation: My Operation
cond=>condition: Yes or No?

st->op->cond
cond(yes)->e
cond(no)->op
```

**************
## Github 
> [比较全面的Github格式 GFM](https://github.com/guodongxiaren/README)

_目录规则（页内跳转）_

- `[](#标题名)` 不需要编码
- `【Name】`看成Name 忽略这对符号 
    - 同理还有  `/` 中英文的 逗号 句号 冒号 小数点 问号
- 空格会变成 - 

****
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

*****
_md文件的头属性_
```
    ---
    title: 泛型
    tags: Java, 泛型
    ---
```

```diff
+ fsd
- 发的所发生的
```
