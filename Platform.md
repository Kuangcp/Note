`目录 start`
 
- [代码托管平台](#代码托管平台)
    - [Gitee](#gitee)
        - [URL规则](#url规则)
    - [Github](#github)
        - [URL规则](#url规则)
        - [MarkDown规则](#markdown规则)
        - [wiki](#wiki)
        - [Bandage图标](#bandage图标)
    - [Gitea](#gitea)
        - [自建](#自建)
- [二进制包仓库](#二进制包仓库)
- [代码质量检测平台](#代码质量检测平台)
    - [codeclimate](#codeclimate)
    - [codebeat](#codebeat)
    - [codacy](#codacy)
- [综合开发平台](#综合开发平台)
    - [华为云](#华为云)
    - [阿里云](#阿里云)
        - [ECS](#ecs)
        - [ACM](#acm)
        - [OSS](#oss)
    - [百度开发平台](#百度开发平台)
        - [CCE](#cce)
        - [BOS](#bos)
        - [BAE](#bae)
        - [其他应用](#其他应用)
            - [翻译](#翻译)
    - [腾讯](#腾讯)
        - [域名](#域名)
        - [CVM](#cvm)
        - [COS](#cos)
        - [微信公众号](#微信公众号)
    - [网易](#网易)
        - [有道智云](#有道智云)
    - [微软](#微软)
        - [翻译](#翻译)
- [云存储](#云存储)
    - [NextCloud](#nextcloud)
    - [坚果云](#坚果云)
    - [七牛云](#七牛云)
- [智能机器人平台](#智能机器人平台)
    - [图灵机器人](#图灵机器人)
- [评论系统](#评论系统)
- [消息推送](#消息推送)
    - [极光推送](#极光推送)
    - [GoEasy](#goeasy)
- [文档](#文档)
    - [文档托管](#文档托管)
    - [文档转换](#文档转换)
- [接口平台](#接口平台)
    - [今日头条](#今日头条)
- [测试平台](#测试平台)
- [培训](#培训)

`目录 end` |_2018-08-09_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************

# 代码托管平台
## Gitlab
> [Site](https://gitlab.com/)

功能丰富, 集成了 CI/CD, 也能自己搭建 社区版, 免费的私有库, 用于团队协作的功能比较多

## Gitee
> 码云,国内的github [帮助文档](http://git.mydoc.io/)


也是有私有库, 但是私有库有数量限制, 不过那个数挺大的, 1000 还是多少, 但是分支图的显示不喜欢, 分支都没有闭合, 真难受

### URL规则
- HTTPS & SSH
    - `HTTPS:` https://gitee.com/kcp1104/MythRedisClient.git
    - `SSH:` git@gitee.com:kcp1104/MythRedisClient.git

***********************************
## Github
> 全球范围性的网站  [开发者文档](https://developer.github.com/v3/) 

1. 在github上修改了项目后，或者以后是和别人一起开发，就要先git pull origin （master）将别人的分支和自己的分支都拉下来确保是最新，
    - 再进行`git push -u origin master` 才能正确提交代码，如果不pull，提交是注定失败的，还会扰乱分支图

- [少有人知的 GitHub 使用技巧](https://segmentfault.com/a/1190000000475547)
### URL规则
> github仓库的URL规则
>> git.io 是短网址服务
- HTTP & SSH
    - `SSH:` git@github.com:Kuangcp/Script.git
    - `HTTPS:` https://github.com/Kuangcp/Script.git

- 目录：
    - `https://github.com/用户/项目/tree/分支/相对根目录的目录`
- 文本文件：
    - `https://github.com/用户/项目/blob/分支/文件目录`
- 二进制文件，例如图片：
    -  `https://raw.githubusercontent.com/用户/项目/分支/文件目录`

> 例如同仓库下的这个文件`/Linux/Docker.md` 可以直接这样写，方便调用，最好最前面不要加`.`这个表示当前目录的 

### MarkDown规则
> [更多详情>>](/Skills/Document/MarkDown.md#github)

### wiki
> 其实也是一个git仓库, 以特定格式进行显示而已
- 侧栏的目录依赖于 `_Sidebar.md` 文件
其显示规则类似于Markdown语法: 
```
  * [[Introduction|Home]]
  * Basic Utilities
    * [[Using/avoiding null|UsingAndAvoidingNullExplained]]
```
> 其中 [[名称|URL]] 类似于 []()  URL的md后缀也要去掉,不然就跳转到md文件的源路径了
> 允许md以文件夹多结构的形式存在, 但是最终的目录规则是扁平的, 直接就是文件名,没有目录名

### Bandage图标
> [shields](https://shields.io/)

- 规则 https://img.shields.io/badge/note-JavaSE-blue.svg
    - 如果是中文则要转码
    - 颜色: brightgreen green yellowgreen yellow orange red lightgrey blue ff69b4 (也就是说可以设置任意颜色)

*********************************************
## Gitea
> [官网](https://gitea.io/zh-cn/) 

### 自建
- 使用docker安装比较简单
    - 配置数据库，一定要是外网的。或者容器互联
`/data/gitea/conf/app.ini` Docker中要修改的配置，都是改成对外的配置
```conf
ROOT_URL         = http://git.kuangcp.top/
DOMAIN           = git.kuangcp.top
SSH_PORT         = 22
SSH_DOMAIN       = kuangcp.top
```
然后还需修改本地的SSH配置才能正常使用
********************************************************
# 二进制包仓库
- [JFrog Bintray](https://bintray.com/kuangcp) 
- [Maven Central Repository ](http://mvnrepository.com/)

# 代码质量检测平台
## codeclimate
> [官网](https://codeclimate.com/dashboard)

要求比较严格, 有详细的说明
## codebeat
> [官网](https://codebeat.co/)

要求比较严格
## codacy
> [官网](https://app.codacy.com/projects)

要求比较宽松

*****************************
# 综合开发平台
## 华为云
- [CSE微服务相关文档](http://support.huaweicloud.com/devg-cse/cse_03_summary.html)

********************************************
## 阿里云

### ECS
> 阿里云主机, 学生有优惠 9.9每月 1核2g

> 域名因为是兼并了万网，所以功能更强大， 现在还支持搭建免费的DNS服务器了
### ACM
> 应用配置管理 [入门文档](https://help.aliyun.com/document_detail/59964.html?spm=a2c4g.11186623.6.546.yaM0cp)
> [如何用ACM简化你的Spring Cloud微服务环境配置管理](https://zhuanlan.zhihu.com/p/33525168?group_id=942728800581259264)

### OSS
> 对象存储

```
资费项 	    计费项 	       标准型单价 	    低频访问型单价 	归档型单价
存储费用 (注①) 	数据存储 	0.148元/GB/月 	0.08元/GB/月 	0.033/GB/月
流量费用 (注①) 	内/外网流入流量（数据上传到OSS） 	免费 	免费 	免费
	内网流出流量（通过ECS云服务器下载OSS的数据） 	免费 	免费 	免费
	外网流出流量 	00:00-08:00（闲时）：0.25元/GB 8:00-24:00（忙时）：0.50元/GB
	CDN回源流出流量 	0.15元/GB 	0.15元/GB 	0.15元/GB
	跨区域复制流量 	0.50元/GB 	0.50元/GB 	0.50元/GB
请求费用 
	所有请求类型 	0.01元/万次 	0.1元/万次 	0.1元/万次
数据处理费用 (注②)
 	图片处理 	每月0-10TB：免费>10TB：0.025元/GB 	每月0-10TB：免费>10TB：0.025元/GB  	无
	视频截帧 	0.1元/千张 	0.1元/千张 	无
	数据取回 	免费 	0.0325元/GB 	0.06元/GB
```
**************************************
## 百度开发平台

**********
### CCE
> 容器引擎  -> [入门必看](https://cloud.baidu.com/doc/CCE/GettingStarted.html)  
> 其实就是镜像仓库,比阿里云的好用 域名很短

### BOS
> 对象存储 [计价方式](https://cloud.baidu.com/doc/BOS/Pricing.html#.E6.8C.89.E9.9C.80.E8.AE.A1.E8.B4.B9)  
> 关于流量定价中的CDN回源流量, 大致是当你开了CDN加速, 然后CDN为了刷新缓存要去你对象存储源获取最新的文件, 这个消耗的流量  
> 同样支持文件夹  

_存储空间价格_  
```
计费项 	标准存储单价（元/GB/月） 	低频存储单价（元/GB/月） 	冷存储单价（元/GB/月）  
存储空间 	0.128 	0.08 	0.048  
```
_请求次数价格_  
```
计费项 	规格 	标准存储单价（元/万次） 	低频存储单价（元/万次） 	冷存储单价（元/万次）  
写请求次数 	PUT,COPY,DELETE 	0.01 	0.25 	0.5  
读请求次数 	GET Bucket,GET OBJECT及其他所有请求 	0.01 	0.05 	0.1  
```
_数据取回价格_
```
计费项 	规格 	标准存储单价（元/GB） 	低频存储单价（元/GB） 	冷存储单价（元/GB）
数据取回 	- 	NA 	0.03 	0.15
```
_流量价格_
```
计费项 	标准存储 & 低频存储 & 冷存储单价（元/GB）
外网数据流出 	0.6
CDN回源流出 	0.14
跨区域数据流出 	0.6
```
****************
### BAE
> 应用引擎，简单的说就是一个提供了环境，你只需上传打包好的可执行文件就可以运行起来了  
> 本来的话是比较简单容易上手的, 但是现在要备案了, 就玩不了了

- 短期使用收费没有很高，十分灵活，就是前期学习入门 配置略麻烦。适合演示使用，例如毕设。
    - 并且还提供一定免费额度的 MySQL Redis MongoDb （只能BAE的内网访问）
    - 还有自动测试

*******************
### 其他应用
- [百度脑图](http://naotu.baidu.com/)`在线思维导图创作`
- [站内搜索](https://zn.baidu.com/cse/home/index)`不用自己写搜索了`

#### 翻译
> [官网](http://api.fanyi.baidu.com/api/trans/product/index) `免费注册, 每月有 2000,000 字符 免费额度`

*******************************************************
## 腾讯
### 域名
> [域名检测工具](https://cloud.tencent.com/product/tools)
### CVM
> 云服务器  
> 学生优惠是 10元每月1核1g 60则是2核2g

### COS
> 对象存储 [官方文档](https://cloud.tencent.com/document/product/436)  
> 同样的支持文件夹,还可以拖动文件夹上传,算是最好用的一个了  

_免费额度_
```
    资源类型 	资源子类型 	       每月免费额度
    存储空间 	存储空间 	         50 GB
    流量 	     外网下行流量 	     10 GB
    流量 	     腾讯云 CDN 回源流量 	10 GB
    请求 	     读请求 	           100 万次
    请求 	     写请求 	           100 万次
```

### 微信公众号
`2017-12-21 21:41:43`
- 不说了反正都是Shit一样的接口设计和返回值  希望会变好，碰过就不想再弄了！！！

## 网易
### 有道智云
> [官网](https://ai.youdao.com/gw.s)

## 微软

### 翻译
`每月 2000,000 字符免费`

> [文档](https://azure.microsoft.com/en-us/services/cognitive-services/translator-text-api/)
> [api](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-reference)
> [定价](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/translator-text-api/)

*************************************************
# 云存储
## NextCloud
> 当自己具有服务器的时候, 搭建自己的私有云盘

## 坚果云

## 七牛云
> 免费存储额度10g流量额度10g, 但是不能创建文件夹  

****************************************************
# 智能机器人平台
## 图灵机器人

**************
# 评论系统
- [畅言](http://changyan.kuaizhan.com/)

************************************************ 
# 消息推送
## 极光推送
> [官网](https://www.jiguang.cn/) `做Android IOS的消息推送和短信等推送`

## GoEasy
- [示例](http://goeasy.io/cn/started)

*********************************
# 文档
## 文档托管
- [看云](https://www.kancloud.cn/dashboard)

_showdoc_
- [showdoc](https://www.showdoc.cc/web/#/)`开源,也具有Docker方式` | [示例](https://www.showdoc.cc/web/#/demo?page_id=7)
- Docker安装: [官方文档](https://www.showdoc.cc/web/#/help?page_id=65610) `跑起来也就几十M内存占用`
    - `git clone https://github.com/star7th/showdoc`
    - 进入项目目录 然后 `docker build -t showdoc ./`
    - `docker run -d --name showdoc -p 4999:80 showdoc`
    - `http://localhost:4999/install/` 然后为了保险起见进容器删除项目根目录的install目录即可
    - 数据与备份 Sqlite/showdoc.db.php 是数据库; 如果有图片就还要备份图片,所以解耦就还是不上传图片了

## 文档转换
- [pandoc](http://pandoc.org/try/)

# 接口平台
## 今日头条
> 今日头条灵犬系统 API `https://m.toutiao.com/detector/api/detect/?text=`URL

************************************************************
# 测试平台
- [自动API测试](https://www.eolinker.com/#/index)
- [吆喝科技](http://www.appadhoc.com/)`A/B测试 灰度上线`

*************************************************
# 培训
- [咕泡](http://www.gupaoedu.com/)`看起来很有深度, 就是有点贵`
- [集智](https://jizhi.im/index)

