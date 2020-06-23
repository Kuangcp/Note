---
title: Hexo
date: 2018-12-14 09:21:42
tags: 
    - Hexo
    - Blog
categories: 
    - 工具
---

**目录 start**

1. [Hexo](#hexo)
    1. [安装 hexo](#安装-hexo)
        1. [主配置文件](#主配置文件)
        1. [插件](#插件)
    1. [文章相关](#文章相关)
        1. [配置](#配置)
            1. [tags](#tags)
            1. [categories](#categories)
        1. [新建文章](#新建文章)

**目录 end**|_2020-06-24 02:06_|
****************************************
# Hexo
> [Official Doc](https://hexo.io/zh-cn/docs/index.html)

> 参考 [博客](http://stonebegin.com/hexo+github.html) | [部署Hexo](http://letus.club/2016/04/04/deploy-hexo-and-change-theme/)

- [ ] 在docker中下拉笔记仓库, 然后构建, 然后推送到github的page上
- [ ] 其实可以更为简单, 使用 travis.ci 进行构建和发布 [参考](https://notes.iissnan.com/2016/publishing-github-pages-with-travis-ci/)  
travis 令人发指的缺点是 Git Commit 信息无法自定义

## 安装 hexo
1. `npm install -g hexo`
1. 新建一个目录然后初始化 `hexo init` 
1. 根据md生成静态资源文件 `hexo generate` | ` hexo g`
1. 本地试运行 `hexo server` | ` hexo s`
1. 清除静态文件` hexo clean`
1. 发布到远程 `hexo deploy` | `hexo d`

### 主配置文件
> [官网配置说明](https://hexo.io/zh-cn/docs/configuration.html)
- 当前目录下的`_config.yml`是主配置文件

- Site 部分
    - subtitle: 对自己的描述或者对网站的描述
    - description: 对网站的描述，提供给搜索引擎看的
    - author: 作者
    - language: 中文是zh-CN
    - timezone: 不填就好，系统自己会计算时区
- URL
    - url: 填写你自己网站的域名
    - root: 如果你的网站首页就在你github仓库的根目录下，则不用修改，否则改成你网站首页所在目录即可。

- Extensions
    - theme 填写`/themes`文件夹下的`主题文件夹名字` [官方主题](https://hexo.io/themes/)    
    - 选好对应的主题只要 `git clone` 在`/themes`文件夹下即可
    - 例如 next主题 [官方使用文档](http://theme-next.iissnan.com/getting-started.html)

- Deployment
    - type: git
    - repo: 仓库URL
    - branch: master 分支，一般是master

- 安装 工具 `npm install hexo-deployer-git --save`

> [更多发布方式](https://hexo.io/docs/deployment.html)   
### 插件
> [indigo](https://github.com/yscoder/hexo-theme-indigo) `一个Material Design风格的Hexo主题`

> [next](https://github.com/iissnan/hexo-theme-next)

## 文章相关
### 配置
#### tags
> `source/tags/index.md`

```
---
title: "tags"
type: tags
layout: "tags"
---
```

#### categories
> `source/categories/index.md`

```yml
---
title: "categories"
type: categories
layout: "categories"
---
```
### 新建文章
- `hexo new "postName"` #postName是文章的名字
    - 文章的开头具有 时间，标题，分类， 标签等信息
- 然后生成`hexo g` 发布 `hexo d`


