---
title: JavaScript
date: 2018-11-21 10:56:52
tags: 
    - 基础
categories: 
    - JavaScript
---

💠

- 1. [JavaScript](#javascript)
    - 1.1. [数据类型](#数据类型)
        - 1.1.1. [字符串](#字符串)
    - 1.2. [函数](#函数)
        - 1.2.1. [函数传值](#函数传值)
    - 1.3. [JSON](#json)
    - 1.4. [常用功能小模块](#常用功能小模块)
        - 1.4.1. [输入校验](#输入校验)
    - 1.5. [Ajax](#ajax)
    - 1.6. [事件](#事件)
        - 1.6.1. [键盘](#键盘)
        - 1.6.2. [鼠标](#鼠标)
    - 1.7. [常用库和框架](#常用库和框架)
        - 1.7.1. [Jquery](#jquery)
        - 1.7.2. [echarts](#echarts)
    - 1.8. [资源文件](#资源文件)
        - 1.8.1. [图片](#图片)

💠 2024-07-07 18:00:42
****************************************
# JavaScript

## 数据类型

### 字符串
- 字符串转码:
    - [参考博客:JS字符串相关转码函数](http://www.cnblogs.com/xcsn/archive/2013/05/15/3079373.html)

## 函数
### 函数传值
```js
    function handlerGet(url, role, success, fail) {
    var request = $.ajax({
        method: 'GET',
        url : 'xxx'+url
    });
    request.done(success);
    request.fail(fail);
    }
    function testRole() {
        handlerGet('/world', 'student',
            function (data) {
                layer.msg('获取成功');
            }, function (data) {
                layer.msg('身份认证已过期， 请重新登录');
            })
    }
```
**********************
## JSON
> [json 数据 添加 删除 排序](http://blog.51yip.com/jsjquery/1583.html)

- 直接点引用属性或者a['b']的方式,
    - 迭代集合:自带foreach循环 `data.forEach(function(value){})`

- 但是有时候不能使用，会undefined，eval('('+data+')')解析后才能用
    - 原因在于Response Headers 的 `Content-Type:application/json;charset=UTF-8` 如果回应的类型是 text/plain 就需要使用 eval('('+data+')')才能用
    - 如果设置成JSON就可以直接点引用和循环迭代, _并且不需要强制的JSON规范, 值为数字时不加双引号也是正常解析的_

```js
    var array = {
        "a": "abc",
        "b": [1, 2, 3, 4, 5, 6],
        "c": 3,
        "d": {
            "name": "james",
            "age": 28
        },
        "e": null,
        "f": true
    };

    //遍历array方式1
    for (var x in array) {
        if (typeof array[x] == 'object' && array[x] != null) {
            for (var y in array[x]) {
                console.log(">>key = " + y + " value = " + array[x][y]);
            }
        } else {
            console.log("key = " + x + " value = " + array[x]); // 非array object
        }
    }
```
## 常用功能小模块
### 输入校验

- [Blog:关于Input的输入校验](http://yuncode.net/code/c_5039bb4a3fccf28)`数字,字母汉字等限制`

## Ajax
> [参考: 使用 Fetch](https://developer.mozilla.org/zh-CN/docs/Web/API/Fetch_API/Using_Fetch)

```js
function get(url, handle) {
    let httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', url, true);
    httpRequest.send();
    /**
        * 获取数据后的处理程序
        */
    httpRequest.onreadystatechange = function () {
        if (httpRequest.readyState === 4 && httpRequest.status === 200) {
            handle(httpRequest)
        }
    };
}

function post(url, data, handle) {
    let xhr = new XMLHttpRequest();
    //使用HTTP POST请求与服务器交互数据
    xhr.open("POST", url, true);
    //设置发送数据的请求格式
    xhr.setRequestHeader('content-type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            handle(xhr.responseText)
        }
    }
    //将用户输入值序列化成字符串
    xhr.send(JSON.stringify(data));
}
```

## 事件
### 键盘

### 鼠标
> [JavaScript 鼠标滚轮事件](https://www.web-tinker.com/article/20037.html)

************************

## 常用库和框架
- lozad.js 懒加载
- [网页底部的浏览 ](https://www.logicbig.com/tutorials/java-ee-tutorial/jpa/group-by-criteria.html) 
- [游戏手柄模拟](https://www.phaser-china.com/example-30.html)

### Jquery
> jquery有是slim版(没有ajax的精简版 ) [JQuery官网](http://jquery.com/) | [Jquery教程](http://www.w3school.com.cn/jquery/index.asp)

- 事件绑定 `$('#Button').on('click', function(){})`
- 在HTML的DOM上绑定数据:设置 `data-*` 属性 然后jq拿到元素直接调用 `$(this).data('id')`拿到值就可以避免函数传值

_原生方式异步提交Form_
```js
    $("#set-form").submit(function(e){
        e.preventDefault();
        console.log('prepare submit')
    });
```

### echarts
> [官网](http://echarts.baidu.com/index.html) | 做图表展示很简单

***************************************

## 资源文件
### 图片
> [参考: JS 图片转Base64](http://www.cnblogs.com/wujingtao/p/5196836.html)
