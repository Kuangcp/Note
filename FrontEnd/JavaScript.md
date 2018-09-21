`目录 start`
 
- [JavaScript](#javascript)
    - [数据类型](#数据类型)
        - [字符串](#字符串)
    - [函数](#函数)
        - [函数传值](#函数传值)
    - [JSON](#json)
    - [常用功能小模块](#常用功能小模块)
        - [输入校验](#输入校验)
    - [Ajax](#ajax)
    - [事件](#事件)
        - [鼠标](#鼠标)
            - [滚轮](#滚轮)
    - [常用库和框架](#常用库和框架)
        - [Jquery](#jquery)
            - [Ajax](#ajax)
            - [form插件](#form插件)
        - [echarts](#echarts)
    - [资源文件](#资源文件)
        - [图片](#图片)

`目录 end` |_2018-08-10_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# JavaScript

## 数据类型
> 虽然是弱类型,但还是要注意一下


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
> [js 原生 post请求](https://segmentfault.com/q/1010000005162727)

> [参考博客: 使用 Fetch](https://developer.mozilla.org/zh-CN/docs/Web/API/Fetch_API/Using_Fetch)

## 事件


### 鼠标

#### 滚轮
> [JavaScript 鼠标滚轮事件](https://www.web-tinker.com/article/20037.html)



## 常用库和框架
- lozad.js 懒加载

### Jquery
> jquery有是slim版(没有ajax的精简版 ) [JQuery官网](http://jquery.com/) | [Jquery教程](http://www.w3school.com.cn/jquery/index.asp)

- 事件绑定 `$('#Button').on('click', function(){})`
- 在HTML的DOM上绑定数据:设置 `data-*` 属性 然后jq拿到元素直接调用 `$(this).data('id')`拿到值就可以避免函数传值

_原生方式异步提交_
```js
    $("#set-form").submit(function(e){
        e.preventDefault();
        console.log('prepare submit')
    });
```
#### Ajax
> [ajax文档](https://api.jquery.com/jQuery.ajax/)

#### form插件
```js
// 使用jquery 的 form插件进行异步提交
$(".submit").on('click', function () {
    console.log('dfs')
    // var jk = $("#contents").submit()
    var options = {
        // target:'#contents', //后台将把传递过来的值赋给该元素
        url:'../teacher/topic/add', //提交给哪个执行
        type:'POST',
        success: function(data){
            console.log(data)
        } //显示操作提示
    };
    $('#contents').ajaxSubmit(options);
})
```

### echarts
> [官网](http://echarts.baidu.com/index.html) | 做图表展示很简单


## 资源文件
### 图片
> [参考博客: JS 图片转Base64](http://www.cnblogs.com/wujingtao/p/5196836.html)
