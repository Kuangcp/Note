`目录 start`
 
- [HTML5](#html5)
    - [参考资料](#参考资料)
    - [特俗字符](#特俗字符)
    - [基础结构标签](#基础结构标签)
        - [head](#head)
            - [meta](#meta)
            - [title](#title)
            - [base](#base)
            - [link](#link)
            - [style](#style)
        - [script](#script)
        - [常用结构](#常用结构)
            - [form](#form)
            - [label](#label)
            - [关于引用](#关于引用)
            - [插入和删除](#插入和删除)
    - [数据存储](#数据存储)
        - [cookie](#cookie)
        - [LocalStorage和SessionStorage](#localstorage和sessionstorage)
            - [清除](#清除)
- [XML](#xml)
    - [XML文件头含义](#xml文件头含义)
    - [XML的元素](#xml的元素)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# HTML5
## 参考资料
> [HTML5 教程 | 菜鸟教程](http://www.runoob.com/html/html5-intro.html)  
> [HTML5 教程 | W3School](http://www.w3school.com.cn/html5/)
## 特俗字符

```html
  空格:&nbsp;代表一个半角空格
  < :&lt;
  > :&gt;
  & ：&amp;
  ￥ :&yen;
  × :&times
  ÷ ：&divide;
```
## 基础结构标签
### head
```html
  <head> 元素是所有头部元素的容器。<head> 内的元素可包含脚本，指示浏览器在何处可以找到样式表，提供元信息，等等。
  以下标签都可以添加到 head 部分：<title>、<base>、<link>、<meta>、<script> 以及 <style>。

```
#### meta
```html
  元数据（metadata）是关于数据的信息。
  <meta> 标签提供关于 HTML 文档的元数据。元数据不会显示在页面上，但是对于机器是可读的。
  典型的情况是，meta 元素被用于规定页面的描述、关键词、文档的作者、最后修改时间以及其他元数据。
  <meta> 标签始终位于 head 元素中。
  元数据可用于浏览器（如何显示内容或重新加载页面），搜索引擎（关键词），或其他 web 服务。
  针对搜索引擎的关键词
  一些搜索引擎会利用 meta 元素的 name 和 content 属性来索引您的页面。
  下面的 meta 元素定义页面的描述：
  <meta name="description" content="Free Web tutorials on HTML, CSS, XML" />
  下面的 meta 元素定义页面的关键词：
  <meta name="keywords" content="HTML, CSS, XML" />
  name 和 content 属性的作用是描述页面的内容。
```
#### title
```html
  <title> 标签定义文档的标题。
  title 元素在所有 HTML/XHTML 文档中都是必需的。
  title 元素能够：
      定义浏览器工具栏中的标题
      提供页面被添加到收藏夹时显示的标题
      显示在搜索引擎结果中的页面标题
```
#### base
```html
  <base> 标签为页面上的所有链接规定默认地址或默认目标（target）：
```

#### link
```html
<link> 标签定义文档与外部资源之间的关系。
<link> 标签最常用于连接样式表：
```

#### style
> `<style>` 标签用于为 HTML 文档定义样式信息。您可以在 style 元素内规定 HTML 元素在浏览器中呈现的样式：
```html
  <head>
    <style type="text/css">
      body {background-color:yellow}
      p {color:blue}
    </style>
  </head>
```
### script
`<script> 标签用于定义客户端脚本，比如 JavaScript。`

********************
> 以上的link script style 等引用外部资源的标签要注意路径问题
1. / 开头则是相对于项目的根路径来定位的
2. 开头为空,就是相对于该页面的的相对路径.` 被URL尾部多输入一个/坑过,所以最好采用第一种稳妥`
3. ..开头就是相对于该页面的相对父路径

### 常用结构
#### form
```html
  <form action="save.php" method="post" >
      <label>爱好:</label>
      <select>
        <option value="看书">看书</option>
        <option value="旅游">旅游</option>
        <option value="运动">运动</option>
        <option value="购物">购物</option>
      </select>
  </form>
```
#### label
label标签不会向用户呈现任何特殊效果，它的作用是为鼠标用户改进了可用性。如果你在 label 标签内点击文本，就会触发此控件。
就是说，当用户单击选中该label标签时，浏览器就会自动将焦点转到和标签相关的表单控件上（就自动选中和该label标签相关连的表单控件上）。
注意：标签的 for 属性中的值应当与相关控件的 id 属性值一定要相同。

#### 关于引用
```html
<blockquote>这是长的引用。</blockquote>
<q>这是短的引用。</q>

```
`使用 blockquote 元素的话，浏览器会插入换行和外边距，而 q 元素不会有任何特殊的呈现。`
#### 插入和删除
```html
  <p>一打有 <del>二十</del> <ins>十二</ins> 件。</p>
```

## 数据存储

### cookie
### LocalStorage和SessionStorage
> [基础详细的一篇博客](http://www.cnblogs.com/st-leslie/p/5617130.html)

#### 清除
> [HTML5中的localStorage什么时候会被清空?](https://segmentfault.com/q/1010000000123500)  
> [翻译：清除各个浏览器中的数据研究](http://www.zhangxinxu.com/wordpress/2012/09/%E7%BF%BB%E8%AF%91%EF%BC%9A%E6%B8%85%E9%99%A4%E5%90%84%E4%B8%AA%E6%B5%8F%E8%A7%88%E5%99%A8%E4%B8%AD%E7%9A%84%E6%95%B0%E6%8D%AE%E7%A0%94%E7%A9%B6/)

- 自己在火狐中尝试了下,清除 网络内容缓存 对localStorage没有影响

***********************************
```html
1.为了确保浏览器能够正确读取字符的编码，整个字符编码必须放置在文档的前512个字符中
2.HTML中不需要声明JavaScript的type属性

刷新iframe 的父页面
  iframe页面是内嵌到父页面的，当点击iframe页面的服务器控件时，默认只刷新iframe页面，父页面是不会刷新的。若想刷新父页面，可以使用js来实现，如
     1. parent.location.reload();
     这种方法会重新加载整个页面。但如果要在原页面的基础上传递参数，则可以使用下面的方法：
     2.top.document.location.href='xxx.aspx?id=xx'。
     但这两种方法都有一个共同的缺点，就是iframe内嵌页面的状态不会保存了，刷新后会重新回到第一次加载的状态。


=========================1、输入框点击清空==============

<input name="textfield" type="text" id="textfield" value="请输入内容" onclick="this.value=''" />

2、输入框点击显示提示内容

操作：鼠标点击输入框出现提示内容，再次点击清空内容可以进行输入。

<input type="text" name="textfield2" id="textfield2" onblur="note_click(this);" onclick="note_click(this)" />
  <script type="text/javascript">
  function note_click(target)
  {
   if(target.value=='')
   {
    target.style.color="#B0B0B0";
    target.value="请输入数字";
   }
   else if(target.value=="请输入数字")
   {
    target.style.color="#000000";
    target.value="";
   }
  }
 </script>

 ====================================【HTML标签笔记】==========================================
                                    
<i></i>：斜体
<u></u>：下划线
<b></b>:粗体
<strong></strong>:更粗
<s></s>:删除线
<sup></sup>上标
<sub></sub>下标
face:字体设置
<p align="right"></p>  //align：设置水平对齐方式
<hr>：水平线
noshade:去掉阴影部分
<pre></pre>:预排版标记


HTML项目符号
<ul>
<li>  
</li>
</ul>
常用属性type，取值：disc代表小黑点，circle代表空心圆，square代表实心方块
注意：<ul>和<li>是块元素

HTML是编号列表（有序列表）
<ol>
<li>
</li>
</ol>
常用属性：type和start

滚动字幕标记<marquee>
常用属性：direction:滚动方向，取值：up,down,left,right
          width:滚动宽度
          height:滚动高度
          bgcolor:滚动背景色
          scrollamount:滚动步长值
          scrolldelay:两步之间的停留时间，以毫秒为单位，1s=1000毫秒
          loop:循环滚动次数
图片标记
<img 属性="值">
常用属性:height
         width
         align:left/center/right
         src（图片路径/相对路径）
         Hspace:图片与左右文字之间的距离（水平距离）
         Vspace:图片与上下文字之间的距离（垂直距离）


超级链接 (行内元素)
<a 属性="值">.......</a>
  href：目标文件的地址URL，该URL可以是相对地址，也可以是绝对地址
  target:目标文件的显示窗口
         _blank:在新窗口中打开目标文件
         _self:在当前窗口中打开（默认打开），相当于“替换”操作。
         -parent:在父级窗口来打开目标文件
         _top：在顶级窗口来打开目标文件。
         1.（1）远程的绝对地址
 访问远程的文件，总是以域名、开机名开头
    <a href="http://xxx.com">协议是http://的就是远程的绝对地址
  (2)本地的绝对路径
    访问本地的绝对路径，是以file:///开头的绝对地址
2.相对地址URL
 （1）当前文件和目标文件是同级关系
　（２）当前文件与目标文件所在的文件夹是同级关系，先找“文件夹名”，然后再找“文件名”，也就是目标文件位于下一级。
   (3)目标文件位于上一层目录中，往上找对应的目录，再找目录中的文件。往上找使用../符号表示
     ../代表上一层目录
     ../../代表上两层目录
     ............
  ---------特殊的链接---------
 <a 属性="xx/Winrar.rar"></a>下载Winrar解压缩文件
   邮箱链接
   <a 属性=“mailto:邮箱地址”></a>
  普通空链接
  <a 属性="#"></a> 
     js链接
  <a 属性="javascript:window.close()">关闭窗口的意思</a>
    ------锚点链接-------
      含义：锚点链接，是在一个网页的不同区域进行跳转，锚点理解为“定义记号”。
      定义锚点：<a  name="锚点名称"></a>
      跳转到锚点（记号）
       语法：<a href="锚点名称">........</a>
        例如：<a href="#锚点名称">.........</a>

  --------<meta>标记------------
 <meta>的主要作用，是提供网页的元信息，比如，指定网页的搜索关键字。
 <meta>标记有两个属性1.http-equiv和name
   （1）设置网页的字符集
      <meta http-equiv="Content-Type" content="text/html;charset="utf-8"/>
   （2）网页自动刷新
      <meta http-equiv="refresh" content="2">
      <meta http-equiv="refresh" content="2;url=http://www.baidu.com">//二秒钟后，跳转到百度
   2.name属性
   name属性主要用于设置网页的搜索关键字、版权信息、作者等。
    (1)设置网页搜索关键字
    <meta name="keywords" content="关键字内容"/>
    (2)设置网页描述信息
      <title></title>
      <meta name="description" content="描述信息内容">

   ------XHTML简介----------
   XHTML的目地是为了取代HTML
   XHTML的标记和HTML一模一样
   XHTML的语法要比HTML严格的多
   XHTML是可扩展超文本标注预言
    ----------XHTML编写规范--------------
   所有标记和属性要全小写
   单边标记必须关闭如<br/>
   所有的属性都必须有值，如：<hr noshade>-----><hr noshade="noshade"/>
   标记之间要顺序嵌套，外层套内层，一层套一层。
   XHTML网页必须要有DTD文档类型定义代码。

     ------DTD文档类型定义------------
   DTD文档类型定义的目地：是一种验证机制，也就是说检验一下你写的XHTML标记语言是否合法。
   

    DTD一共有三大类型
      （1）严格型的DTD
        在严格的DTD中，不能再使用各种表现的标记，如:<font>、<b>、<body bgcolor>等，(要求必须使用CSS来取代各种表现标记。)
   严格型DTD表现方式：<!DOCTYPE html PUBLIC"-//W3C//DTD XHTML 1.0 Strict//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml-strict.dtd>
      (2)过渡型DTD
         在过渡型的DTD中，可以继续使用HTML中的表现的写法。
         这些表现标记，还可以使用。如：<font>、<b>、<body bgcolor>
    过渡型的DTD的表达方式：<!DOCTYPE html PUBLIC"-//W3C//DTD XHTML 1.0 Transitional//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml-Transitional.dtd>
      (3)框架的DTD
    框架的DTD表现方式:<!DOCTYPE html PUBLIC"-//W3C//DTD XHTML 1.0 Frameset//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml-frameset.dtd>
         ----------表格学习--------------
   表格标签-------块元素
    1.表格的结构
      <table>
      <tr>  //代表的行，这里代表一行
      <td></td>  //代表单元格
      </tr>
      </table>
     2.<table>属性
      1.width:宽度
      2.height:高度
      3.Align:表格水平对其方式,left、center、right
      4.Border:边框粗细
      5.bgcolor:表格背景色
      6.background:背景图片URL
      7.cellpadding:单元格边线到内容间的距离（填充距离）
      8.cellspacing:单元格与单元格之间的距离（间距）
      9.bordercolor:边框颜色
      10.rules:合并单元格边框线，取值：all //友情提醒因为学习的html没有接触css所以才用rules，rules兼容性不好，一般都用CSS取代他。
      
       3.<tr>属性----行标记
         1.bgcolor:
         2.height:
         3.align:
         4.valign:垂直居中，取值top（上）、middle(中)、bottom(下)

       4.<td>或<th>属性
         1.width:
         2.height:
         3.bgcolor:
         4.background:
         5.align:
         6.valign:
         7.rowspan:上下单元格合并
         8.colspan:左右单元格合并     
       
      -------表单学习------
    1.表单的概念
    表单主要用来获取客户端用户数据（信息）的，如注册表单、查询表单、登录表单等。
    2.<form>标记属性------块元素
      name:
      method:表单的提交方式,取值：get/post
      action:制定表单的处理程序，一般是PHP文件
      enctype:制定表单数据的编码方式（解密方式），这个属性只能用在method="post"的情况下.
           （1）application/x-www-form-urldecoded  //默认的传递
            (2) multipart/form-data  //如果你上传文件，该值必须它自己
        注意：上传文件一定要有enctype="multipart/form-data"

       3.GET方法和POST方法
      （1）GET提交方式
         GET方式，是将表单数据追加到action指定的处理程序的后面，然后向服务器发送请求。
            注意：地址栏传数据的方式，默认就是GET方式。，
         GET方式的特点：1.GET方式不能提交敏感数据，如：密码。。
                        2.GET方式值提交少量数据，因为地址栏的长度有限制，大约100外字符
                        3.GET方式下不能上传附件
         (2)POST表单提交方式
              POST提交方式，它不是将表单数据追加到地址上，而是直接传给表单处理程序。

             POST方式的特点：
                1.POST提交的数据相对安全。
                2.POST可以提交海量数据。
                3.POST方式可以上传附件。
    
             单行文本域
    语法格式<input type="text" 属性 ="值"/>
    常用属性：     
        name:文本框的名字，只能以字母开头
        type:表单元素的类型
        value:文本框中的值
        size：文本框的长度，以“字符”为单位。
        maxLength：最多可以输入多少个字符，超出的就输不进去了。
        readonly：只读属性。可以选中，但不能修改，如readonly="readonly"
        disabled:禁用属性，不能选中，不能修改，如:disabled="disabled"

          单行密码域
        语法格式<input type="password" 属性 ="值">
        常用属性和单行文本域属性一样。
           
          单选按钮
     语法格式<input type="radio" name="sex" 属性 ="值" />
      常用属性：
              Name:元素的名称
              Value：元素的值，该value中数据将发往服务器。
              Cheaked:默认选择哪一项，如:cheacked="checked"
      注意：一组单选按钮，只能选择一个，但name的值必须一致。
 
             复选框
     语法格式：<input type="checkbox" 属性="值"/>
      常用属性：
            name：元素名称
            value：元素的值
            checked:默认选中，如checked="checked"
             
              下拉列表
       语法格式：<select name="">
                   <option>xxx内容</option>
                 </select>
        常用属性：name
        option属性：value和selected
               selected：默认选中，如selected="selected"

               文本区域
           <textarea name="名称" cols="宽度" row="高度"></textarea>
             常用属性：name:
                       cols:宽度，是指多少个字符串
                       rows:高度，是指几行高
                提示：<textarea>和</textarea>之间是默认文本
  
                    各种按钮学习
       提交按钮：<input type="submit" value="提交表单"/>
       重置按钮：<input type="reset" value="重置填写"/>
       图片按钮: <input type="image" src="图片后缀"/>
       普通按钮：要与js结合使用，如下代码：<input type="button" onclick="javascript:windows.close()" value="关闭窗口"/>
         
            上传文件域
       语法格式：<input type="file" 属性=“属性”/>
       常用属性：
               name：表单元素的名称
               value：表单元素的值，这个值其实就是上传的文件名。
        语法格式例子：<input type="file" name="uploadfile">

                  隐藏域
      功能：隐藏域就是看不见的一个框。传递一些值，而这个值又不想让别人看见。
      用处：主要用于php后台程序。
      语法格式：<input type="hidden" name="" value=""/>



实战运用：制作网页http://www.chinayarn.com/mart/index2011.asp/http://www.nanshanski.com/index-cn.asp/http://www.jingying.com.cn/参考如下


    html的注释：<!--内容-->     //注意注释的内容是不会显示的，注释的目地是为了维护方便。

      -----网页多媒体-----
网页上的视频大多数为flash格式的，因为flash的兼容性比较好。
    以flash动画为例，播放flash动画的代码如下，这个代码不用记，看懂就行。
    <object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,29,0"  
width="1000" height="202" >  
<param name="movie" value="images/banner.swf">  
<param name="quality" value="heigh">  
<param name="wmode" value="trandsparent">  
<embed        src="images/banner.swf"  width="1000" height="202"  quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" wmode="transparent">
</embed>  
</object>  
             以上标记的说明：<object>标记，是IE中引入多媒体的标记。
                             <embed>标记：是netscape中引入多媒体的标记


    ----------图片热点（图像地图）---------
    图片热点含义：绘一张图片加多个链接，默认情况下，一张图只能加一个链接。
    标记结构：
          <img src="xxx.jpg/png" usemap="#Map" />
          <map id="Map">
          <area shape="热区形状" coords="热区坐标" href="链接地址" />
          </map>
        (1)<area>标记常用属性
               shape:热区的形状，取值：rect（矩形），circle（圆形），polygon（多边形）
               coords:热区的坐标（位置）
           如果shape="rect"时，那么，coords="x1,y1,x2,y2" 例如：corrds=“50，50，200，150”
                                  *(x1,y1)为矩形左上角的坐标值,(x2,y2)为矩形右上角坐标值。so (x2-x1)和(y2-y1)可知矩形的长和宽。
           如果shape="circle"时，那么，coords="x,y,r",其中(x,y)为圆心坐标，而r是圆的半径。

        -----------普通框架-----------
    1.框架的概念：框架技术：将一个浏览器窗口划分成若干个小窗口，每个小窗口显示一个独立的网页。
    
    2.框架集和框架页
     框架集<frameset>:主要用来划分窗口的
     框架页<frame>:主要用来制定窗口默认显示的网页地址

     框架与窗户很像
       打比方： 一个窗户由窗格（框架集）和玻璃（框架页）构成。
                先规划窗格，然后再确定每个窗格中放的玻璃。（先有结构，后有内容。）

      框架网页的DID必须是：<!DOCTYPE html PUBLIC"-//W3C//DTD XHTML 1.0 Frameset//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml-frameset.dtd>
            代码如下：<frameset cols="200,*" frameborder="yes" border="">
                      <frame src="xx.html"/>
                      <frame src="xx.html"/>
                      </frameset>
                      （1）<frameset>常用属性属性
                              cols：划分左右型框架
                                1.cols="200,*" //左框架的宽度为200px，剩下的都是右框架。
                                2.cols="180,*,180" //左框架和右框架的宽分别为180px，剩下的都是中间框架。
                                3.cols="20%,*" //另类写法，划分框架时，可以用百分比来表示
                              rows：划分上下型框架
                                1.rows="200,*" //上框架的高度为200px，剩下的都是下框架。
                                2.row="180,*,180" //上框架和下框架的高度分别为180px，剩下的的都是中间框架。
                       注意：cols和rows不能两个同时用。
                      （2）frameborder:是否显示框架的边框线，取值1或0，亦yes/no
                           border:边框线的粗细
                           bordercolor:边框的颜色
                           3.<frame>框架页的属性
                              (1)src：该小窗口中，默认显示的网页地址。
                                 noresize:不能调整小窗口的大小，如noresize="noresize"
                                 scrolling:是否显示滚动条，取值：auto,no,yes
                                 name:给当前小窗口起个名字，这个name就是给<a>标记target属性来用的。
                          提示做网站后台时，返回首页的相关代码：<a href="" target="_top">
```
# XML
## XML文件头含义
```
  web-app 是web.xml的根节点标签名称
  version 是版本的意思
  xmlns是web.xml文件用到的命名空间
  xmlns:xsi是指web.xml遵循xml规范
  xsi:schemaLocation是指具体用到的schema资源（对文档的限制）
```

## XML的元素
XML中元素的标记是自定义的，并具有明确的含义，其组织结构是树形的层次结构，每个元素及其
子元素 并不是XML规范好的，而是用户根据自己需要来自定义的，就像是我写坦克大战时用的文件
保存法，就需要有一定的格式来读取（辨认）所读取的数据是什么类型
      XML文档结构清晰，易读，而且是根据开放的标准建立的

