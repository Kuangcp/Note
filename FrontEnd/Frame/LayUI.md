`目录 start`
 
- [LayUI](#layui)
    - [使用](#使用)
        - [模块化](#模块化)
        - [非模块化](#非模块化)
    - [组件](#组件)
        - [Layer](#layer)
        - [树形](#树形)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# LayUI

## 使用

### 模块化
> 写法稍微复杂了些,但是提高了页面加载速度

_引入核心文件:_
```html
    <link rel="stylesheet" href="../layui/css/layui.css"/>
    <script src="../layui/layui.js"></script>
```
_使用layer模块:_
```js
    layui.use(['layer'], function(){
        var layer = layui.layer;
        layer.msg('Hello World');
    });
```

### 非模块化

## 组件

### Layer
> [layer组件](http://layer.layui.com/?alone) 十分强大
> [layer 移动版](http://layer.layui.com/mobile/api.html)


_弹出页面层_
- [ ] 如何将script 标签内容直接引入 
```js
    layer.open({
      type: 1,
      area: ['600px', '360px'],
      shadeClose: true, //点击遮罩关闭
      content: 'test'
    });
```
```html
    <script type="text/html" id="test">
    <input type="text" />
    </script>
```
_弹出页面中异步提交表单_
```html
    <script type="text/html" id="set_key">
        <form id="set-form" class="set-form">
            <input type="text" id="key" required/> <->
            <input type="text" id="value" required/><br><br>
            <button>新增 string</button>
        </form>
    </script>
    <button onclick="string()">String</button>
```
```js

    function string(){
        var set_content = $("#set_key").html()
        layer.tab({
            area: ['500px', '520px'],
            tab: [{
                title: 'set', 
                content: set_content
            }]
        });        
        $("#set-form").submit(function(e){
            e.preventDefault();
            set();
        });
    }
    function set(){
        var key = $("#key").val()
        var value = $("#value").val()
        handlePost('/key',  {
            key: key, 
            value: value
        }, function(data){
            console.log(data)
        }, function(data){
            console.log(data)
        })
    }
}
```
### 树形
> [基于layui树形菜单写的树形列表（treetable）](https://segmentfault.com/a/1190000011812724)



