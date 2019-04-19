# Extjs的使用
 - 引入相关文件
> ext-all.js  
> extjs文件夹中的resource文件夹内的所有文件

 - 使用入口
> Ext.onReady():ExtJS Application的入口...就相当于Java或C#的main函数.

``` stylus
<script type="text/javascript">
        Ext.onReady(function () {
            Ext.MessageBox.alert('标题', 'Hello World!');
        });
 </script>
```
# 相关组件的使用

## 1, 对话框
> Ext.MessageBox.alert('标题', 'Hello World!');

## 2,窗体组件

``` stylus
var win = new Ext.Window({
                title: '窗口',
                width: 476,
                height: 374,
                html: '<div>这里是窗体内容</div>',
                resizable: true,
                modal: true,
                closable: true,
                maximizable: true,
                minimizable: true
            });
            win.show();
```
 - 说明
> (1)var win = new Ext.Window({}):创建一个新的Window窗体对象。  
(2)title: '窗口'：窗体的标题。  
(3)width: 476,height: 374：宽度及高度。  
(4)html: '\<div>这里是窗体内容\</div>'：窗体内部显示的html内容。  
(5)resizable: true：是否可以调整窗体的大小，这里设置为 true。  
(6)modal: true：是否为模态窗体[什么是模态窗体？当你打开这个窗体以后，如果不能对其他的窗体进行操作，那么这个窗体就是模态窗体，否则为非模态窗体]。  
(7)closable:true：是否可以关闭，也可以理解为是否显示关闭按钮。  
(8)maximizable: true：是否可以最大化，也可以理解为是否显示最大化按钮。  
(9)minimizable: true：是否可以最小化，也可以理解为是否显示最小化按钮。  
(10)win.show()：窗体展示。

## 3,表单

``` stylus
 var form = new Ext.form.FormPanel({
                    frame: true,
                    title: '表单标题',
                    style: 'margin:10px',
                    html: '<div style="padding:10px">这里表单内容</div>'
                });
                var win = new Ext.Window({
                    title: '窗口',
                    width: 476,
                    height: 374,
                    html: '<div>这里是窗体内容</div>',
                    resizable: true,
                    modal: true,
                    closable: true,
                    maximizable: true,
                    minimizable: true,
                    items: form
                });
                win.show();
```
 - 说明
> (1)var form = new Ext.form.FormPanel({}):创建一个新的form表单对象。  
(2)title: '表单标题'：表单的标题，如果不加的话，不会出现上面的浅色表单标题栏。  
(3)style: 'margin:10px':表单的样式，加了个外10px的外边距。  
(4)html: '\<div style="padding:10px">这里表单内容\</div>'：表单内显示html的内容。  

## 4,文本框

``` stylus
//初始化标签中的Ext:Qtip属性。
            Ext.QuickTips.init();
            Ext.form.Field.prototype.msgTarget = 'side';
            //用户名input
            var txtusername = new Ext.form.TextField({
                width: 140,
                allowBlank: false,
                maxLength: 20,
                name: 'username',
                fieldLabel: '用户名称',
                blankText: '请输入用户名',
                maxLengthText: '用户名不能超过20个字符'
            });
            //密码input
            var txtpassword = new Ext.form.TextField({
                width: 140,
                allowBlank: false,
                maxLength: 20,
                inputType: 'password',
                name: 'password',
                fieldLabel: '密码',
                blankText: '请输入密码',
                maxLengthText: '密码不能超过20个字符'
            });
            //表单
            var form = new Ext.form.FormPanel({
                frame: true,
                title: '表单标题',
                style: 'margin:10px',
                html: '<div style="padding:10px">这里表单内容</div>',
                items: [txtusername, txtpassword]
            });
            //窗体
            var win = new Ext.Window({
                title: '窗口',
                width: 476,
                height: 374,
                html: '<div>这里是窗体内容</div>',
                resizable: true,
                modal: true,
                closable: true,
                maximizable: true,
                minimizable: true,
                items: form
            });
            win.show();
```
 - 说明
> (1)Ext.QuickTips.init()：QuickTips的作用是初始化标签中的Ext:Qtip属性，并为它赋予显示提示的动作。  
(2)Ext.form.Field.prototype.msgTarget = 'side'：TextField的提示方式为：在右边缘，如上图所示，参数枚举值为"qtip","title","under","side",id(元素id)，
   side方式用的较多，右边出现红色感叹号，鼠标上去出现错误提示。  
(3)var txtusername = new Ext.form.TextField():创建一个新的TextField文本框对象。  
(4)allowBlank: false：不允许文本框为空。  
(5)maxLength: 20：文本框的最大长度为20个字符，当超过20个字符时仍然可以继续输入，但是Ext会提示警告信息。  
(6)name: 'password'：表单名称，这个比较重要，因为我们在与服务器交互的时候，服务端是按name接收post的参数值。  
(7)fieldLabel: '用户名'：文本框前面显示的文字标题，如“用户名”，“密码”等。  
(8)blankText: '请输入用户名'：当非空校验没有通过时的提示信息。  
(9) maxLengthText: '用户不能超过20个字符'：当最大长度校验没有通过时的提示信息。  

## 5,按钮

``` stylus
 //初始化标签中的Ext:Qtip属性。
            Ext.QuickTips.init();
            Ext.form.Field.prototype.msgTarget = 'side';
            //提交按钮处理方法
            var btnsubmitclick = function () {
                Ext.MessageBox.alert('提示', '你点了确定按钮!');
            }
            //重置按钮"点击时"处理方法
            var btnresetclick = function () {
                Ext.MessageBox.alert('提示', '你点了重置按钮!');
            }
            //重置按钮"鼠标悬停"处理方法
            var btnresetmouseover = function () {
                Ext.MessageBox.alert('提示', '你鼠标悬停在重置按钮之上!');
            }
            //提交按钮
            var btnsubmit = new Ext.Button({
                text: '提交',
                handler: btnsubmitclick
            });
            //重置按钮
            var btnreset = new Ext.Button({
                text: '重置',
                listeners: {
                    'mouseover': btnresetmouseover,
                    'click': btnresetclick
                }
            });
            //用户名input
            var txtusername = new Ext.form.TextField({
                width: 140,
                allowBlank: false,
                maxLength: 20,
                name: 'username',
                fieldLabel: '用户名称',
                blankText: '请输入用户名',
                maxLengthText: '用户名不能超过20个字符'
            });
            //密码input
            var txtpassword = new Ext.form.TextField({
                width: 140,
                allowBlank: false,
                maxLength: 20,
                inputType: 'password',
                name: 'password',
                fieldLabel: '密码',
                blankText: '请输入密码',
                maxLengthText: '密码不能超过20个字符'
            });
            //表单
            var form = new Ext.form.FormPanel({
                frame: true,
                title: '表单标题',
                style: 'margin:10px',
                html: '<div style="padding:10px">这里表单内容</div>',
                items: [txtusername, txtpassword],
                buttons: [btnsubmit, btnreset]
            });
            //窗体
            var win = new Ext.Window({
                title: '窗口',
                width: 476,
                height: 374,
                html: '<div>这里是窗体内容</div>',
                resizable: true,
                modal: true,
                closable: true,
                maximizable: true,
                minimizable: true,
                buttonAlign: 'center',
                items: form
            });
            win.show();
```
 - 说明
> (1)var btnsubmit = new Ext.Button():创建一个新的Button按钮对象。  
(2)handler: btnsubmitclick：当用户点击的时候[即js中的onclick事件]执行方法btnsubmitclick。  
(3)listeners: {'mouseover': btnresetmouseover,'click': btnresetclick}：当用户点击的时候[即js中的onclick事件]执行方法btnresetclick，  
    鼠标悬停时执行方法btnresetmouseover。  
(4)handler与listeners的区别：  
    handler:执行的是首发事件，click是button这个组件的首发事件。这就是handler的运行方式：被某个组件的首要event所触发。  
            handler是一个特殊的listener。  
    listener：是一个事件名 + 处理函数的组合，事件监听，如上例代码所示，我们监听了两个事件"click"，与"mouseover"事件，并且会顺序执行。  

## 6,单选框和复选框

``` stylus
//----------------------单选组开始----------------------//
            var radiogroup = new Ext.form.RadioGroup({
                fieldLabel: '性别',
                width: 100,
                items: [{
                    name: 'sex',
                    inputValue: '0',
                    boxLabel: '男',
                    checked: true
                }, {
                    name: 'sex',
                    inputValue: '1',
                    boxLabel: '女'
                }]
            });
            //获取单选组的值
            radiogroup.on('change', function (rdgroup, checked) {
                alert(checked.getRawValue());
            });
            //----------------------单选组结束----------------------//
            //----------------------复选组开始----------------------//
            var checkboxgroup = new Ext.form.CheckboxGroup({
                fieldLabel: '兴趣爱好',
                width: 170,
                items: [{
                    boxLabel: '看书',
                    inputValue: '0'
                }, {
                    boxLabel: '上网',
                    inputValue: '1'
                }, {
                    boxLabel: '听音乐',
                    inputValue: '2'
                }]
            });
            //获取复选组的值
            checkboxgroup.on('change', function (cbgroup, checked) {
                for (var i = 0; i < checked.length; i++) {
                    alert(checked[i].getRawValue());
                }
            });
            //----------------------复选组结束----------------------//
```
 - 说明
> (1)var radiogroup = new Ext.form.RadioGroup():创建一个新的单选按钮组。  
(2)name: 'sex'：单选按钮组是按照 name 属性来区分的，同一组中的单选按钮才能单选，  
    如果name属性设置错误，该按钮将会被认为是其他组。  
(3)inputValue: '0'：选择框的值。  
(4)boxLabel: '男':选择框后面的文字说明。  
(5)checked.getRawValue()：获取选择框的选中值，由于单选框只有一个选中值，可以直接获取，  
    而复选框可以多选，所以要循环取出。  
	
## 7,下拉列表

``` stylus
//----------------------下拉列表开始----------------------//
            //创建数据源[数组数据源]
            var combostore = new Ext.data.ArrayStore({
                fields: ['id', 'name'],
                data: [[1, '团员'], [2, '党员'], [3, '其他']]
            });
            //创建Combobox
            var combobox = new Ext.form.ComboBox({
                fieldLabel: '政治面貌',
                store: combostore,
                displayField: 'name',
                valueField: 'id',
                triggerAction: 'all',
                emptyText: '请选择...',
                allowBlank: false,
                blankText: '请选择政治面貌',
                editable: false,
                mode: 'local'
            });
            //Combobox获取值
            combobox.on('select', function () {
                alert(combobox.getValue());
            })
            //----------------------下拉列表结束----------------------//
```
 - 说明
> (1)var combostore = new Ext.data.ArrayStore():创建一个新的数组数据源。  
(2)fields: ['id', 'name']：数据源包含两列，列名分别为'id','name'。  
(3)data: [[1, '团员'], [2, '党员'], [3, '其他']]:数据源对应的数据，例：id:1,name:团员。  
(4)var combobox = new Ext.form.ComboBox()：创建一个新的下拉列表。  
(5)store: combostore:数据源为上面创建的数据源，这个属性是combobox的必需属性。  
(6)displayField: 'name',valueField: 'id'：combobox对应数据源的显示列与值列，这两个属性也是必须的。  
(7)mode: 'local'：指定数据源为本地数据源，如果是本地创建的数据源，该属性也是必须的，如果数据源来自于服务器，   
(8)triggerAction: 'all'：请设置为”all”,否则默认 为”query”的情况下，你选择某个值后，再此下拉时，只出现匹配选项，  
    如果设为all的话，每次下拉均显示全部选项。  
(9)editable: false:默认情况下，combobox的内容是可以编辑的，该属性设置为false，
    使下拉列表只能选择不能编辑。  
(10)combobox.on('select', function () {alert(combobox.getValue());}):选择时alert出下拉列表的值。  

## 8,联动下拉列表

``` stylus
//----------------------下拉列表开始----------------------//
            //创建市数据源
            var combocitystore = new Ext.data.Store({
                //设定读取的地址
                proxy: new Ext.data.HttpProxy({ url: '/App_Ashx/Demo/City.ashx' }),
                //设定读取的格式
                reader: new Ext.data.JsonReader({ root: 'data' },
                    [{ name: 'id' }, { name: 'name'}])
            });
            //创建区数据源
            var comboareastore = new Ext.data.Store({
                //设定读取的地址
                proxy: new Ext.data.HttpProxy({ url: '/App_Ashx/Demo/Area.ashx' }),
                reader: new Ext.data.JsonReader({ root: 'data' },
                    [{ name: 'id' }, { name: 'name'}])
            });
            //创建市Combobox
            var comboboxcity = new Ext.form.ComboBox({
                id: 'comboboxcity',
                fieldLabel: '市',
                width: 120,
                store: combocitystore,
                displayField: 'name',
                valueField: 'id',
                triggerAction: 'all',
                emptyText: '请选择...',
                allowBlank: false,
                blankText: '请选择市',
                editable: false,
                mode: 'local', //该属性和以下方法为了兼容ie8
                listeners: {
                    'render': function () {
                        combocitystore.load();
                    }
                }
            });

            //创建区Combobox
            var comboareacity = new Ext.form.ComboBox({
                fieldLabel: '区',
                width: 120,
                store: comboareastore,
                displayField: 'name',
                valueField: 'id',
                triggerAction: 'all',
                emptyText: '请选择...',
                allowBlank: false,
                blankText: '请选择区',
                editable: false
            });
            //联动的实现
            comboboxcity.on('select', function () {
                comboareastore.baseParams.id = comboboxcity.getValue();
                comboareacity.setValue('');
                comboareastore.load();
            })
            //----------------------下拉列表结束----------------------//
```
 - 说明
> (1)var combocitystore = new Ext.data.Store():创建一个新的数据源。  
(2)proxy: new Ext.data.HttpProxy({ url: '/App_Ashx/Demo/City.ashx' })：数据代理为http代理，地址为/App_Ashx/Demo/City.ashx。  
(3)reader: new Ext.data.JsonReader({ root: 'data' },[{ name: 'id' }, { name: 'name'}]):读取json返回值根节点为data，对象列为id和name。  
这里要结合client与service观察,我在service端的输出如下：{data:[{id:1,name:'北京'},{id:2,name:'上海'}]}
(4)comboboxcity.on('select', function () {}：市选择变化时触发事件。  
(5)comboareastore.baseParams.id = comboboxcity.getValue()：注意，前面的comboareastore是区的数据源，  
当市变化时，我们给区的数据源加上个向service端发送的参数。  
(6)comboareacity.setValue('')：把区的下拉列表设置为空，由于非空验证，Ext会提示用户“请选择区”，这个地方也可以把加载出来的第一个区  
显示在区的下拉列表中，具体请自行实现吧。  
(7)comboareastore.load()：区的数据源重新加载。  

## 9,上传图片

``` stylus
//创建div组件
            var imagebox = new Ext.BoxComponent({
                autoEl: {
                    style: 'width:150px;height:150px;margin:0px auto;border:1px solid #ccc; text-align:center;padding-top:20px;margin-bottom:10px',
                    tag: 'div',
                    id: 'imageshow',
                    html: '暂无图片'
                }
            });
            //创建文本上传域
            var file = new Ext.form.TextField({
                name: 'imgFile',
                fieldLabel: '文件上传',
                inputType: 'file',
                allowBlank: false,
                blankText: '请浏览图片'
            });
            //提交按钮处理方法
            var btnsubmitclick = function () {
                if (form.getForm().isValid()) {
                    form.getForm().submit({
                        waitTitle: "请稍候",
                        waitMsg: '正在上传...',
                        success: function (form, action) {
                            Ext.MessageBox.alert("提示", "上传成功！");
                            document.getElementById('imageshow').innerHTML = '<img style="width:150px;height:150px" src="' + action.result.path + '"/>';
                        },
                        failure: function () {
                            Ext.MessageBox.alert("提示", "上传失败！");
                        }
                    });
                }
            }
            //重置按钮"点击时"处理方法
            var btnresetclick = function () {
                form.getForm().reset();
            }
            //表单
            var form = new Ext.form.FormPanel({
                frame: true,
                fileUpload: true,
                url: '/App_Ashx/Demo/Upload.ashx',
                title: '表单标题',
                style: 'margin:10px',
                items: [imagebox, file],
                buttons: [{
                    text: '保存',
                    handler: btnsubmitclick
                }, {
                    text: '重置',
                    handler: btnresetclick
                }]
            });
```
 - 说明
> (1)var imagebox = new Ext.BoxComponent():创建一个新的html标记。  
    官方解释如下：  
    This may then be added to a Container as a child item.
    To create a BoxComponent based around a HTML element to be created at render time, use the autoEl config option which takes the form of a DomHelper specification:  
(2) autoEl: {style: '',tag: 'div',id: 'imageshow', html: '暂无图片'}定义这个html标记的属性，如 标记为：div，id是多少等。  
    官方实例为：  
    var myImage = new Ext.BoxComponent({  
    autoEl: {  
        tag: 'img',  
        src: '/images/my-image.jpg'  
        }  
    });  
(3)var file = new Ext.form.TextField()：创建一个新的文件上传域。  
(4)name: 'imgFile':名称，重要，因为service端要根据这个名称接收图片。  
(5)inputType: 'file'：表单类型为文件类型。  
(6)waitTitle: "请稍候",waitMsg: '正在上传...',：上传等待过程中的提示信息。  
(7)document.getElementById('imageshow').innerHTML = '<img style="width:150px;height:150px" src="' + action.result.path + '"/>';这个是原生态的js，把imageshow的值换成图片。  


## 10,文本编辑器

``` stylus
 //创建文本上传域
            var exteditor = new Ext.form.HtmlEditor({
                fieldLabel: '员工描述'
            });
            //整合KE编辑器
            var keeditor = new Ext.form.TextArea({
                id: 'keeditor',
                fieldLabel: '员工描述',
                width: 700,
                height: 200
            });

            //表单
            var form = new Ext.form.FormPanel({
                frame: true,
                title: '表单标题',
                style: 'margin:10px',
                items: [exteditor, keeditor],
                listeners: {
                    'render': function () {
                        KE.show({
                            id: 'keeditor',
                            imageUploadJson: '/App_Ashx/Upload.ashx'
                        });
                        setTimeout("KE.create('keeditor');", 1000);
                    }
                }
            });
```
 - 说明
> (1) var exteditor = new Ext.form.HtmlEditor():创建一个新的html编辑器。  
(2) var keeditor = new Ext.form.TextArea()：创建一个新的TextArea。  
(3) listeners: {  
                'render': function () {  
                    KE.show({  
                        id: 'keeditor',  
                        imageUploadJson: '/App_Ashx/Upload.ashx'  
                    });  
                    setTimeout("KE.create('keeditor');", 1000);  
                }  
            }  
监听表单的 render 事件，创建 KE Editor.(2)，(3)中的id 要统一，否则无法显示。  
imageUploadJson: '/App_Ashx/Upload.ashx'，keeditor上传图片的后台执行文件  

## 11,布局

![enter description here][1]

### 1,ContainerLayout

![enter description here][2]

``` stylus
<div id="ContainerLayout" style="float: left; width: 300px">
    ContainerLayout：垂直方式放置
</div>

var box1 = new Ext.createWidget({
                autoEl: {
                    tag: 'div',
                    style: 'background:red;width:300px;height:30px',
                    html: 'box1'
                }
            });
            var box2 = new Ext.createWidget({
                autoEl: {
                    tag: 'div',
                    style: 'background:yellow;width:300px;height:30px',
                    html: 'box2'
                }
            });
            var box3 = new Ext.createWidget({
                autoEl: {
                    tag: 'div',
                    style: 'background:blue;width:300px;height:30px;color:#fff',
                    html: 'box3'
                }
            });
            var containerlayout = new Ext.Container({
                layout: 'form',
                items: [box1, box2, box3],
                renderTo: 'ContainerLayout'
            });
            //------ContainerLayout结束-----//
```
### 2,FormLayout
![enter description here][3]

``` stylus
<div id="FormLayout" style="float: left; width: 240px; padding-left: 10px;">
</div>

 //------FormLayout开始------//
            var formlayout = new Ext.Panel({
                title: 'FormLayout',
                layout: 'form',
                items: [
                    new Ext.form.TextField({ fieldLabel: '用户名' }),
                    new Ext.form.TextField({ fieldLabel: '密码' }),
                    new Ext.form.TextField({ fieldLabel: '重复密码' })
                ],
                renderTo: 'FormLayout'
            });
            //------FormLayout结束------//
```
### 3,ColumnLayout

![enter description here][4]

``` stylus
<div id="ColumnLayout" style="float: left; width: 500px; padding-left: 10px;">
</div>

//------ColumnLayout开始------//
            var ColumnLayout = new Ext.Panel({
                width: 600,
                title: 'ColumnLayout',
                layout: 'column',
                items: [
                    new Ext.form.FormPanel({ title: '第一列', columnWidth: .33, labelWidth: 50, items: [
                        new Ext.form.TextField({ fieldLabel: '用户名' })]
                    }),
                    new Ext.form.FormPanel({ title: '第二列', columnWidth: .33, labelWidth: 50, items: [
                        new Ext.form.TextField({ fieldLabel: '密码' })]
                    }),
                    new Ext.form.FormPanel({ title: '第三列', columnWidth: .34, labelWidth: 80, items: [
                        new Ext.form.TextField({ fieldLabel: '重复密码' })]
                    })
                ],
                renderTo: 'ColumnLayout'
            });
            //------ColumnLayout结束------//
```
### 4,BorderLayout
![enter description here][5]

``` stylus
<div id="BorderLayout" style="padding: 10px 0px; clear: both">
</div>

//------BorderLayout开始------//
            var BorderLayout = new Ext.Panel({
                title: 'BorderLayout',
                layout: 'border',
                width: 1100,
                height: 300,
                items: [
                    new Ext.Panel({ title: '上北', region: 'north', html: '可以放个logo什么的' }),
                    new Ext.Panel({ title: '下南', region: 'south', html: '版权信息？', autoEl: 'center' }),
                    new Ext.Panel({ title: '中间', region: 'center', html: '主面板' }),
                    new Ext.Panel({ title: '左东', region: 'west', html: '树型菜单或是手风琴' }),
                    new Ext.Panel({ title: '右西', region: 'east', html: '常用功能或是去掉？' })
                ],
                renderTo: 'BorderLayout'
            });
            //------BorderLayout结束------//
```
### 5,AccordionLayout

``` stylus
<div id="AccordionLayout" style="width: 300px; float: left; height: 200px">
</div>

//------AccordionLayout开始------//
            var AccordionLayout = new Ext.Panel({
                title: 'AccordionLayout',
                layout: 'accordion',
                height: 200,
                items: [
                    new Ext.Panel({ title: '用户管理', items: [new Ext.createWidget({ autoEl: { tag: 'div', html: '用户管理'} })] }),
                    new Ext.Panel({ title: '角色管理', items: [new Ext.createWidget({ autoEl: { tag: 'div', html: '角色管理'} })] }),
                    new Ext.Panel({ title: '系统管理', items: [new Ext.createWidget({ autoEl: { tag: 'div', html: '系统管理'} })] })
                ],
                renderTo: 'AccordionLayout'
            });
            //------AccordionLayout结束------//
```
### 6,FitLayout

``` stylus
<div id="FitLayout" style="width: 300px; float: left; height: 200px; padding-left: 10px;">
</div>

//------FitLayout结束------//
            var FitLayout = new Ext.Panel({
                title: 'FitLayout',
                height: 100,
                renderTo: 'FitLayout',
                layout: 'fit',
                items: [
                    new Ext.Panel({ bodyStyle: 'background:red', html: '使用了fit布局,填充满' }),
                    new Ext.Panel({ bodyStyle: 'background:yellow', html: '这个panel不会显示，因为是fit布局' })
                ]
            });
            var NoFitLayout = new Ext.Panel({
                title: 'NoFitLayout',
                height: 100,
                renderTo: 'FitLayout',
                items: [
                    new Ext.Panel({ bodyStyle: 'background:yellow', html: '未使用了fit布局,没有填充满' })
                ]
            });
            //------FitLayout结束------//
```
### 7,TableLayout

``` stylus
<div id="TableLayout" style="width: 400px; float: left; padding-left: 10px;">
</div>

//------TableLayout开始------//
            var TableLayout = new Ext.Panel({
                title: 'TableLayout',
                layout: 'table',
                layoutConfig: { columns: 3 },
                defaults: {
                    width: 133,
                    height: 100,
                    autoEl: 'center'
                },
                defaultType: 'panel',
                items: [
                    { html: '行1列1' },
                    { html: '行1列2' },
                    { html: '行[1,2]列3', rowspan: 2, height: 180 },
                    { html: '行2列[1,2]', colspan: 2, width: 266 }
                ],
                renderTo: 'TableLayout'
            });
            //------TableLayout结束------//
```


  [1]: http://pic002.cnblogs.com/images/2012/414533/2012062621054135.jpg
  [2]: ./images/2017-04-11%2019-29-21%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png "2017-04-11 19-29-21屏幕截图"
  [3]: ./images/FormLayout.png "FormLayout"
  [4]: ./images/ColumnLayout.png "ColumnLayout"
  [5]: ./images/BorderLayout.png "BorderLayout"