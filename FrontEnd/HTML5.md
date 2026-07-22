---
title: HTML5
date: 2018-11-21 10:56:52
tags: 
categories: 
    - 前端
---

💠

- 1. [HTML5](#html5)
    - 1.1. [参考资料](#参考资料)
    - 1.2. [特殊字符](#特殊字符)
    - 1.3. [数据存储](#数据存储)
        - 1.3.1. [Cookie](#cookie)
        - 1.3.2. [LocalStorage和SessionStorage](#localstorage和sessionstorage)
            - 1.3.2.1. [清除](#清除)
        - 1.3.3. [IndexDB](#indexdb)
- 2. [Notification](#notification)
- 3. [PWA](#pwa)

💠 2026-07-22 14:05:33
****************************************
# HTML5
## 参考资料
> [HTML5 教程 | 菜鸟教程](http://www.runoob.com/html/html5-intro.html)  
> [HTML5 教程 | W3School](http://www.w3school.com.cn/html5/)

## 特殊字符

```html
  空格:&nbsp;代表一个半角空格
  < :&lt;
  > :&gt;
  & ：&amp;
  ￥ :&yen;
  × :&times
  ÷ ：&divide;
```

## 数据存储

### Cookie

### LocalStorage和SessionStorage
> [基础详细的一篇博客](http://www.cnblogs.com/st-leslie/p/5617130.html)

#### 清除
> [HTML5中的localStorage什么时候会被清空?](https://segmentfault.com/q/1010000000123500)  
> [翻译：清除各个浏览器中的数据研究](http://www.zhangxinxu.com/wordpress/2012/09/%E7%BF%BB%E8%AF%91%EF%BC%9A%E6%B8%85%E9%99%A4%E5%90%84%E4%B8%AA%E6%B5%8F%E8%A7%88%E5%99%A8%E4%B8%AD%E7%9A%84%E6%95%B0%E6%8D%AE%E7%A0%94%E7%A9%B6/)

- 在火狐中 清除 网络内容缓存 对localStorage没有影响

### IndexDB

************************

# Notification 
> [MDN](https://developer.mozilla.org/en-US/docs/Web/API/notification)

# PWA
> [Progressive web apps | MDN](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)  
> [pwa builder](https://www.pwabuilder.com/)  

| 技术                              | 作用                | 标准来源        |
| ------------------------------- | ----------------- | ----------- |
| **Service Worker**              | 后台代理、离线缓存、推送通知    | HTML5 / W3C |
| **Web App Manifest**            | 定义 App 名称、图标、启动方式 | W3C         |
| **Cache API**                   | 程序化控制资源缓存         | HTML5       |
| **Fetch API**                   | 网络请求拦截            | HTML5       |
| **Push API / Notification API** | 消息推送、本地通知         | W3C         |
| **Background Sync**             | 后台同步              | W3C         |


| 特性        | PWA（HTML5）          | WebView 壳子（Android）  |
| --------- | ------------------- | -------------------- |
| **技术栈**   | 纯 Web（JS/HTML/CSS）  | Android Kotlin + Web |
| **打包**    | 不需要，浏览器直接安装         | 需要 APK               |
| **离线能力**  | ✅ Service Worker 缓存 | ✅ 本地文件缓存             |
| **推送通知**  | ✅ Push API          | ✅ 原生 + Web           |
| **后台运行**  | ⚠️ 受限               | ✅ 更稳定                |
| **应用商店**  | ❌ 不能上架（国内）          | ✅ 可以                 |
| **系统级功能** | ❌ 有限（相机、蓝牙等）        | ✅ 完整原生能力             |
| **缓存控制**  | JS 代码控制             | Android 代码控制         |
