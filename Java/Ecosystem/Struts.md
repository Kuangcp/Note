`目录 start`
 
- [Struts2笔记](#struts2笔记)
    - [常见问题](#常见问题)
    - [1.【struts基本运行过程】](#1struts基本运行过程)
    - [2.【搭建Struts2开发环境】](#2搭建struts2开发环境)
        - [2.1 访问Action的URL：](#21-访问action的url)
        - [2.2 URL 默认搜索特性 ：](#22-url-默认搜索特性-)
        - [2.3 如果没有给Action指定class：](#23-如果没有给action指定class)
        - [2.4 如果找不到Action：](#24-如果找不到action)
        - [2.5 URL的后缀名可以自定义（会覆盖原本的配置）](#25-url的后缀名可以自定义（会覆盖原本的配置）)
    - [3.【action标签的配置】](#3action标签的配置)
        - [3.1 【关于result的配置】](#31-关于result的配置)
        - [3.2 【模式匹配】](#32-模式匹配)
    - [4.【action类型转换】](#4action类型转换)
            - [【注意】](#注意)
        - [4.1【与Servlet解耦】](#41与servlet解耦)
        - [4.2 【通过实现接口struts2自动注入】](#42-通过实现接口struts2自动注入)
    - [5.【文件上传】](#5文件上传)
        - [5.1 struts2框架的文件上传：](#51-struts2框架的文件上传)
    - [6. 【文件下载】](#6-文件下载)
    - [7.【校验】](#7校验)
        - [7.1 【struts2手动验证】：](#71-struts2手动验证)
        - [7.2【struts2框架验证(xml方式)】:](#72struts2框架验证xml方式)
    - [8.【自定义拦截器】](#8自定义拦截器)
        - [8.1 【如何自定义拦截器】](#81-如何自定义拦截器)
            - [1、 所有的拦截器都需要实现Interceptor接口或者继承Interceptor接口的扩展实现类](#1、-所有的拦截器都需要实现interceptor接口或者继承interceptor接口的扩展实现类)
            - [2、要重写init()、intercept()、destroy()方法](#2、要重写init、intercept、destroy方法)
                - [3、 在struts.xml配置文件中，进行注册](#3、-在strutsxml配置文件中进行注册)
    - [9.【ognl学习】](#9ognl学习)
        - [9.1【valueStack】：](#91valuestack)
        - [9.2 【理解OGNL Context】 上下文](#92-理解ognl-context-上下文)
        - [9.3 【OGNL表达式】【示例JSP】](#93-ognl表达式示例jsp)
                - [1.如果访问其他Context中的对象，由于他们不是根对象，所以在访问时，需要添加前缀。<br>](#1如果访问其他context中的对象由于他们不是根对象所以在访问时需要添加前缀<br>)
                - [2.如果要访问根对象（即ValueStack）中对象的属性，则可以省略命名对象，直接访问该对象的属性即可。<br>](#2如果要访问根对象（即valuestack）中对象的属性则可以省略命名对象直接访问该对象的属性即可<br>)
            - [用法3:构造Map](#用法3构造map)
            - [【“$”有两个主要的用途】](#“$”有两个主要的用途)
        - [9.4【OGNL标签】](#94ognl标签)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Struts2笔记
* 使用ognl表达式在页面debug，<s:debug></s:debug>
* 使用的jar包不仅要放在library里，如果运行时需要，就要加载lib目录下

```xml
<result-types>
	...
	<result-type name="myresult" class="com.foo.MyResult" />
</result-types>
```
* action没有result，执行的方法没有返回值(void)，方法里写上out.write(JSON); 调用action方就能收到JSON字符串
* result标签类型默认是转发，要显示说明是重定向

## 常见问题
- action是单例还是多例的？
    - 多例的，可以在构造器中证明
- struts2有哪三个类重要的类？
    - ActionContext Action的上下文
    - ServletActionContext 建立struts2与Servlet的通信基础
    - ActionInvocation struts2的总的上下文
- struts2的数据都在值栈中，怎么保证数据的安全性？值栈的生命周期是？
    - 因为ValueStack在ActionContext中，而ActionContext又是在ThreadLocal中，所以是线程安全的，
    - 值栈的生命周期是一次请求，当前的action，actionContext，ValueStack 生命周期是一致的
- 自己写的action是由谁调用的？
- ActionProxy和拦截器的意义？

## 1.【struts基本运行过程】
1.浏览器的各种事件，发起一个URL的请求，
2.被项目的默认过滤器监听到了，调用对应的action，(需要配置好xml文件的package和action标签）
3.若action有绑定拦截器，就先执行拦截器里的方法
4.由action里运行方法（这里是真正的代码处理的地方）的return值来确定等会跳转的结果页面（配置xml文件的result标签）

## 2.【搭建Struts2开发环境】
（或者直接使用MyEclipse的快速搭建，struts2.1+Hibernate3.3.2+JSTL1.2.2(本机jdk7.45+tomcat7.08)）
* 1、找到Struts2应用所需要使用到的JAR包（特别注意不能和Hibernate的JAR包有重复的，不然就报错）

Struts2.3.3版本的开发必需JAR包：
```
	sm-3.3.jar
	sm-commons-3.3.jar
	sm-tree-3.3.jar
	ommons-fileupload-1.2.2.jar
	ommons-io-2.0.1.jar
	ommons-lang3-3.1.jar
	ommons-logging-1.1.1.jar
	reemarker-2.3.19.jar
	avassist-3.11.0.GA.jar
	gnl-3.0.5.jar
	truts2-core-2.3.3.jar
	work-core-2.3.3.jar
```

* 2、 创建JSP文件
* 3、 创建Action文件（实现了Struts的Action接口的普通类,或者继承ActionSupport类）
* 4、 编写Struts2的配置文件Struts.xml
* 5、 在web.xml中加入Struts2 框架启动的过滤器配置（核心过滤器）

### 2.1 访问Action的URL：
package的namespace加上Action的名字加上后缀

### 2.2 URL 默认搜索特性 ：
`/a/b/c/d/df.action`
`/a/df.action`
- 这两个是等价的，上面长的那个同样分解为两部分，前半部分的路径是从d到a
	- 依次向上搜索的，直到找到，否则才会报错，所以说，只要根是对的，中间可以乱写，但是会影响性能

### 2.3 如果没有给Action指定class：
- `struts.xml`继承的`struts-default.xml` 中配置了一个默认的class，所以说不会报错
	- `<default-class-ref name=""/>`

### 2.4 如果找不到Action：
- 就需要配置默认的Action名称，没有的话，就会报错。有就执行那个了
	- `<default-action-ref name=""/>`

### 2.5 URL的后缀名可以自定义（会覆盖原本的配置）
- 在struts.xml 中配置:
	- （使用多个的话，用逗号分隔）默认是action和空
	- name : 框架自带配置文件 default.properties中常量名
	- value ：常量值
	`<constant name="struts.action.extension" value="myth"></constant>`
- 或者：
	- src下新建一个`default.properties` 里面只写需要修改的常量
		- `struts.action.extension=myth `
	
> 若两者都修改了按以下顺序：
1. struts-default.xml
2. struts-plugin.xml
3. struts.xml
4. struts.properties
5. web.xml
> 若有相同的常量配置好，后者覆盖前者  建议在struts.xml中配置

```xml
	<-- 配置URL后缀 默认是action或空-->
	<constant name="struts.action.extension" value="myth"></constant>
	<-- 配置国际化资源文件被修改时，是否重新加载 默认是false -->
	<constant name="struts.i18n.reload" value="true"></constant>
	<-- 配置struts2框架的配置文件修改时，是否重新加载 默认是false-->
	<constant name="struts.configuration.xml.reload" value="true"></constant> 
	<--
		配置struts2的模式 
		false 生产模式 默认是false
		true 开发模式 需要更多的调试信息 会自动将上面两个常量设置为true
	-->
	<constant name="struts.devMode" value="true"></constant>
```

- 自定义使用的 struts.xml 不仅路径，还有名字，方便多人开发
- 规范一般是一个action对应于一个xml文件，所以在struts.xml中引入xml文件要：
- `<include file=""></include>` file的路径都是以src为起点，注意把点换成 /

## 3.【action标签的配置】
### 3.1 【关于result的配置】

```xml
    <struts>
	<package name="resulttype" namespace="/resulttype" extends="struts-default">
	<!-- 这是action的执行入口，里面定义返回类型，或者转发重定向啥的 -->
	<action name="resulttypeAction" class="com.myth.resulttype.resulttypeAction">
		<!-- 默认是转发 type属性：是指定type类型-->
		<!-- <result name="success" type="dispatcher">/resulttype/success.jsp</result> -->
		<!--
		 	result标签的标准写法  验证了一个特性，可以在重定向后再重定向，这在原本的JSP中是不允许的
		 	 转发：dispatcher
		-->
		<result name="success" type="dispatcher">
			<param name="location">/resulttype/success.jsp</param>
		</result>
		<result name="jqgrid" type="dispatcher">
			<param name="location">/resulttype/Jqgrid.jsp</param>
		</result>
		<!-- 重定向到jsp 和后面的重定向action底层代码是一样的-->
		<!-- <result name="success" type="redirect">
			<param name="location">/resulttype/success.jsp</param>
		</result> -->
		
		<!-- 重定向到Action (可以是别的配置文件里的，只要引入到了主配置文件struts.xml就可以)-->
		<!-- <result name="success" type="redirectAction">
			
				actionName:指定的是struts.xml文件 中action标签中name属性的值
				namespace：指定的是struts.xml文件action对应的package的namespace值
			 
			<param name="actionName">helloWorldAction</param>
			<param name="namespace">/primer</param>
		</result> -->
	</action>
	<!-- 不写result就是默认返回文本 -->
	<action name="JSONAction" class="com.myth.resulttype.resulttypeAction" method="Json">
		<!-- <result type="json"/> -->
	</action>
	</package> 
	</struts>
```
### 3.2 【模式匹配】
```xml
	<struts>
		<package name="pattern" namespace="/pattern"  extends="struts-default">
			<!-- 全局result 之后的可以不用配置了相当于全局变量，如果之后的action配置了，那就是局部变量覆盖原理-->
			<!-- <global-result>
				<result name="success">/pattern/success.jsp</result>
			</global-result> -->
			
			<!-- 框架中默认是运行的execute，如果自定义就更改那个method属性 -->
			<action name="BookAction" class="com.myth.pattern.BookAction">
				<result name="success">/pattern/success.jsp</result>
				<result name="add">/pattern/BookAction.jsp</result>
			</action>
			<!-- 
				通配符的使用，可以匹配任意长字符 
			-->
			<!-- <action name="*_add" class="com.myth.pattern.BookAction" method="add">
				<result name="success">/pattern/success.jsp</result>
				<result name="add">/pattern/BookAction.jsp</result>
			</action> -->
			<!-- 问题出现了，如果没有下面两个action，访问的都会是bookaction没错
			可是有了上面的通配符的action，下面还能正常运行，这是因为覆盖？ -->
			<!-- <action name="BookAction_add" class="com.myth.pattern.BookAction" method="add">
				<result name="success">/pattern/success.jsp</result>
				<result name="add">/pattern/BookAction.jsp</result>
			</action>
			<action name="UserAction_add" class="com.myth.pattern.UserAction" method="add">
				<result name="success">/pattern/success.jsp</result>
				<result name="add">/pattern/UserAction.jsp</result>
			</action> -->
			<!-- 
				上面两个可以改写 (1)匹配的是通配符的第一个子串
			 -->
			<!-- <action name="*_add" class="com.myth.pattern.{1}" method="add">
				<result name="success">/pattern/success.jsp</result>
				<result name="add">/pattern/{1}.jsp</result>
			</action> -->
			
			<!-- <action name="BookAction_add" class="com.myth.pattern.BookAction" method="add">
				<result name="add">/pattern/BookAction.jsp</result>
			</action>
			<action name="BookAction_delete" class="com.myth.pattern.BookAction" method="delete">
				<result name="success">/pattern/success.jsp</result>
			</action>
			<action name="UserAction_add" class="com.myth.pattern.UserAction" method="add">
				<result name="add">/pattern/UserAction.jsp</result>
			</action>
			<action name="UserAction_delete" class="com.myth.pattern.UserAction" method="delete">
				<result name="success">/pattern/success.jsp</result>
			</action> -->
			<!-- 
				改写： 
					{1}：通配符 * 的第一个子串
					{2}：通配符 * 的第二个子串
					{0}：通配符 * 的整个串
			-->
			<action name="*_*" class="com.myth.pattern.{1}" method="{2}">
				<result name="success">/pattern/success.jsp</result>
				<result name="add">/pattern/{1}.jsp</result>
			</action>
			<!-- 动态方法调用：（默认开启，已经配置关闭了）链接写法：namespace+actionname+！+方法名
					那么在配置中不用配置method方法，而是由页面的指定的方法名来调用相应的方法
				<a href="${pageContext.request.contextPath }/pattern/BookAction!add.action">添加图书</a>
				<a href="${pageContext.request.contextPath }/pattern/BookAction!delete.action">删除图书</a>
			 -->
			<!-- <action name="BookAction" class="com.myth.pattern.BookAction">
				<result name="success">/pattern/success.jsp</result>
				<result name="add">/pattern/BookAction.jsp</result>
			</action> -->
		</package>
	</struts>
```
**2.3以上版本使用通配**
```xml
	<action name="user_*"  class="userAction" method="{1}">                                  
	    <result name="success">/WEB-INF/jsp/login.jsp</result>                  
	    <allowed-methods>login</allowed-methods>                                      
	</action>
```
- **总结**：在struts2.3之前的版本，正常的配置就可以了，
	- 但在struts2.3版本之后，使用通配符调用方法时，内部会验证是否允许访问该方法，
	- 所以要加上`<allowed-methods>方法名1，方法名2…</allowed-methods>`代码。

## 4.【action类型转换】

* 1、从JSP页面上的**输入框提交给action**时，只要在action中声明同名变量，定义setget方法,那之后直接使用get方法就能获取到值。
    * 封装成对象再setget也是一样可以的但是在JSP上的input的name上要加对象名做前缀。
    * 还可以批量添加数据，就使用Collection集合 Collection<T> ts;同样的加setget方法，
    * 但是在JSP上的多个input的name就要写成这种格式**ts[0].name ts[1].name......**

* 2、当struts有些类型无法转换时，就需要自定义转换器
	* **【基于字段】（局部）**
	* 在当前action包下新建 convert.properties 文件名是自定义的
	* 在该文件中 `xwork.default.fieldvalue=无效的字段值 "{0}".`
	* 在struts.xml文件加载该资源文件
    
```xml
<constant name="struts.custom.i18n.resources" 
	value="cn.itcast.converter.converter,
			cn.itcast.i18n.resources">
</constant>
```
* **【基于类】（全局）：**
	* 在src目录下新建一个`xwork-conversion.properties`文件
	* 内容： 待转换的类型=类型转换器的全类名
	* 例如：`java.util.Date=cn.itcast.convert.DataConverter`
* 3、result标签名为input的是默认为错误页面的跳转方向
	在错误页面调出错误信息：`<s:fielderror fieldName="createTime"/>`
	* 【针对每个字段给出提示信息】
		在converte.properties中添加一行 `invalid.fieldvalue.createTime=****`


####【注意】
JSP页面中引入struts标签 `<%@ taglib uri="/struts-tags" prefix="s" %>`
* 创建完文件后记得一定要添加到struts.xml文件中去，若没加，也可以在JSP页面中直接使用

### 4.1【与Servlet解耦】
struts2 对 HttpServletRequest HttpSession ServletContext进行了封装成了Map对象
* 【方法一】:   通过ServletActionContext类直接获取
	这个类是action执行的上下文对象，包括了parameter request session application等。
	
```java
	//分别三个属性的设置request session application
	HttpServletRequest request = ServletActionContext.getRequest();
		request.setAttribute("username", "username_request");
	Map sessionMap = ServletActionContext.getContext().getSession();
		sessionMap.put("username", "username_session");
	ServletContext sc = ServletActionContext.getServletContext();
		sc.setAttribute("username", "username_application");
```
JSP页面的获取：
```jsp
    ${requestScope.username}<br>
    ${sessionScope.username}<br>
    ${applicationScope.username}<br>
```

### 4.2 【通过实现接口struts2自动注入】
1. 实现这四个接口：ServletRequestAware，ServletResponseAware，ServletContextAware，SessionAware
2. 实例化对象分别是HttpServletRequest，HttpServletResponse，Map，ServletContext
3. 重写四个set方法，方法体写上this.** = **;

## 5.【文件上传】
* 【1】套路一致，但是在配置时，action里一定有input的result才可以
* 【2】<-- 配置文件上传的总大小 -->
	< constant name="struts.multipart.maxSize" value="2097152000"></ constant>
* 【3】错误提示配置
新建一个properties文件，名字自定义 加入到struts配置文件中去
```conf
	struts.messages.error.uploading=Error uploading: {0}
	struts.messages.error.file.too.large=File too large: {0} "{1}" "{2}" {3}
	struts.messages.error.content.type.not.allowed=Content-Type not allowed: {0} "{1}" "{2}" {3}
	struts.messages.error.file.extension.not.allowed=File extension not allowed: {0} "{1}" "{2}" {3}
```
- {0}：< input>标签的name 属性值
- {1}：上传文件的真实名称
- {2}：上传文件保存到临时目录的名称
- {3}：上传文件的类型（对于too.large来说是上传文件的大小）

### 5.1 struts2框架的文件上传：
* 单文件上传：
	* 在动作类action中声明相关属性：
			* 在动作类action中，要声明与页面中表单name属性同名的属性，同名的属性的类型时File类型；
			* 在动作类action中，要声明[同名的属性]ContentType，类型时String类型；
			* 在动作类action中，要声明[同名的属性]FileName，类型时String类型
			* 给所有属性提供get和set方法
	* 在业务方法中，处理文件上传：
			* 获取要上传文件的路径，保存的位置
			* 在目标文件夹内，创建一个与上传文件同名的文件
			* 通过FileUtils工具类提供copyFile()方法，将临时文件内容拷贝到目标文件夹下的那个同名的文件
	* 设置上传文件的总大小
			* 在struts.xml文件中，<constant name="struts.multipart.maxSize" value="2097152000"></constant>
	* 设置上传文件的大小、类型和扩展名：
		* 在自定义的配置文件中，在action标签下：
```xml
<!-- 配置拦截器的参数，这里是文件上传拦截器 -->
<interceptor-ref name="defaultStack">
	<!-- 
		配置文件上传拦截器的参数
			* 与定义参数的顺序无关
			* 允许的类型(allowedTypes)和允许的扩展名(allowedExtensions)必须保持一致
		-->
	<!-- 
		* 配置上传文件的大小
			* struts.xml文件中配置的是上传文件的总大小
			* 这里配置的是上传文件的单个大小
		-->
	<param name="fileUpload.maximumSize">20971520</param>
	<!-- 配置上传文件允许的类型，如果配置多个值的话，用","隔开 -->
	<param name="fileUpload.allowedTypes">text/plain,application/msword</param>
	<!-- 配置上传文件的扩展名，如果配置多个值的话，用","隔开 -->
	<param name="fileUpload.allowedExtensions">.txt</param>
</interceptor-ref>
```
* 自定义上传文件的错误提示信息：
	* 在动作类action同目录下，创建一个名为fileuploadmessage.properties资源文件(名为自定义)
	* 改资源文件配置如下：
```conf
	struts.messages.error.uploading=Error uploading: {0}
	struts.messages.error.file.too.large=File too large: {0} "{1}" "{2}" {3}
	struts.messages.error.content.type.not.allowed=Content-Type not allowed: {0} "{1}" "{2}" {3}
	struts.messages.error.file.extension.not.allowed=File extension not allowed: {0} "{1}" "{2}" {3}
```	
		
* 多文件上传：
		* 所有流程于配置都与单文件上传一致。
		* 需要注意的是：
			* 在页面中，虽然是多文件上传，但是页面中表单的name属性的值必须保持一致；
			* 在动作类action中声明的相关属性，类型改成数组；
			* 在业务方法中，相关处理流程改成单文件上传的循环。

## 6. 【文件下载】
 1、下载文件时 压入值栈的名字如果含中文需要转码：fileName = new String(filename.getBytes(),"ISO-8859-1");
配置文件  filename=${filename}.xls

## 7.【校验】
### 7.1 【struts2手动验证】：
也就是说手动的是直接在action里，重写个validate方法就是了 
方法里只要按需求写this.addFieldError( key, value);语句就行了，后续的由框架来处理
* 首先要从页面中获取对应的标签name属性的值，在动作类action中声明 同名的属性，提供get和set方法

* 要继承ActionSupport类或者实现Validateable接口

* 重写Validateable接口的validate()方法
	* 前提是：要保证setUsername()、validate()、login()方法要按照这个先后顺序执行

* 如果登录失败，如何处理：
	* this.addFieldError( key, value);
		* key：错误提示字段
		* value：错误提示信息

* 什么时候才是验证通过？
	* 验证通过：1、map集合不存在；2、map集合存在并为空
	* 验证不通过：map集合存在并且不为空

* 分析需求：
	* 用户名不能为null ,""
	* 密码不能为null, "" ，并且密码的长度6-12之间 

* 针对所有业务方法进行验证还是针对某个指定业务方法进行验证？
	* 重写的validate()方法，针对所有业务方法进行验证
	* 重写的validate()方法加上要验证的指定的业务方法名(业务方法名的首字母大写)，实现针对某个指定的业务方法进行验证
		* 为什么要这样进行拼接？因为struts2框架底层拼接，如果不这样写，底层就找不到对应方法名


### 7.2【struts2框架验证(xml方式)】:
* 首先要从页面中获取对应的标签name属性的值，在动作类action中声明同名的属性，提供get和set方法

* 创建一个xml格式验证文件：
	* 命名方式：ActionClassName-validation.xml，ActionClassName指的是动作类action的名称
	* <validators>标签：根元素
	* field：指定action中要校验的属性，实际上就是页面中表单的name属性的值
		* name：指定页面中表单的name属性的值
	* field-validator：指定验证规则
		* type：指定验证规则名称，struts2框架提供的验证规则放在xwork-core-xxx.jar
				下的com\opensymphony\xwork2\validator\validators
				的default.xml配置文件。
	* param：向底层的验证规则传递的参数
	* message：验证失败时，提供的错误提示信息

* 如果要对指定方法进行验证的话：
	* xml验证文件的命名方式：ActionClassName-ActionName-validation.xml，
		ActionName对应的是struts.xml文件对应的action标签的name属性的值

## 8.【自定义拦截器】
* 【拦截器 特性】：

	拦截器一般是和对应的action绑定的，而原生的filter是对URL模式进行拦截的

	* 执行顺序：执行完struts中配置的拦截器栈中所有intercept方法后再执行action的execute方法
	* 当拦截器的 intercept方法  返回null就会继续执行action 
		如果在前面就调出来了action实例，并且执行了方法那么之后的action就不会再重复执行
	* 检查是否还有拦截器待执行，有就去执行，没有就会得到null，同样的继续执行action
			String result = invocation.invoke();
			return result;

### 8.1 【如何自定义拦截器】
#### 1、 所有的拦截器都需要实现Interceptor接口或者继承Interceptor接口的扩展实现类	
#### 2、要重写init()、intercept()、destroy()方法
	
* init()是在struts2框架运行时执行，在拦截器的生命周期中只执行一次，可以做必要的内容的初始化工作
* intercept()，是每一次请求就执行一次，做相关处理工作。
	* intercept()方法接收一个ActionInvocation接口的实例
	* 通过这个接口的实例，可以获取以下内容：

```java
	//cn.itcast.aop.UserAction @15b5783， 动作类的对象
System.out.println("invocation.getAction() : "+invocation.getAction());
	//cn.itcast.aop.UserAction @15b5783， 与invocation.getAction()方法获取的是同一的对象
System.out.println("invocation.getProxy().getAction() : "+invocation.getProxy().getAction());
	//userAction_save，自定义配置文件中的action标签的name属性的值
System.out.println("invocation.getProxy().getActionName() : "+invocation.getProxy().getActionName());
	//save，对应动作类指定要执行的方法名
System.out.println("invocation.getProxy().getMethod() : "+invocation.getProxy().getMethod());
	//	/aop，自定义配置文件中的package标签的namespace属性的值
System.out.println("invocation.getProxy().getNamespace() : "+invocation.getProxy().getNamespace());
```
* destroy()是在拦截器销毁前执行，在拦截器的声明周期中只执行一次。		
		
#####3、 在struts.xml配置文件中，进行注册
* 在配置文件中的package标签下，进行相关配置：
```xml
<interceptors>
	<!-- 声明自定义的拦截器 -->
	<interceptor name="expessionInterceptor" class="cn.itcast.aop.ExpessionInterceptor" />
	<!-- 声明自定义拦截器栈 -->
	<interceptor-stack name="expessionStack">
			<interceptor-ref name="defaultStack"/>
			<!-- 配置使用自定义拦截器 -->
			<interceptor-ref name="expessionInterceptor"/>
	</interceptor-stack>
</interceptors>
<!-- 配置修改struts2框架运行时，默认执行的是自定义拦截器栈 -->
<default-interceptor-ref name="expessionStack" />
```
后面跟着的就是action的配置了

	
## 9.【ognl学习】

### 9.1【valueStack】：
ValueStack实际上是一个接口，在struts2中利用OGNL时，实际上是哦那个的是实现了该接口的OgnlValueStack类，这个类是利用OGNL的基础
贯穿整个action生命周期，每个action类的对象都有一个valueStack对象，相当于一个数据的中转站，在其中保存了当前action对象和其他相关对象
struts框架把valueStack对象保存在名为 “struts.valueStack”的请求属性中（request中）
```java
	ValueStack vs = (ValueStack)request.getAttribute("struts.valueStack");
	vs.set("key","value");//实际上是放在了Map集合里再放在栈里的
	vs.getRoot().add(0,new Person());//把person对象压入List集合的0位置（栈顶）
```
### 9.2 【理解OGNL Context】 上下文
* OgnlValueStack类包含两个重要的属性：root 和 context 
     * 其中toot本质上是一个List集合
     * Context是一个Map（确切的说是一个OgnlContext对象）
* 在这个OgnlContext对象中，有一个默认的顶层对象 root OGNL访问context中这个默认顶层对象中的元素时不需要#号，直接通过名称来引用
而访问其他对象时， request，session，attr 等则需要#号引用。
* 总结：ognl Context包含ObjectStack属性和ContextMap属性
* 在底层类中的部分代码：
```java
public class OgnlValueStack implements ValueStack {
		CompoundRoot root;    ---  list集合
	transient Map<String, Object> context;  --- map集合
}
```								

### 9.3 【OGNL表达式】【示例JSP】
实际操作的不是值栈，而是值栈的属性：Context的上下文（就是一个Map集合）
* 使用EL表达式取值:
* 使用Ognl表达式取值:  【访问Map集合加#】
```jsp
${requestScope.username}<br>
${sessionScope.username}<br>
${applicationScope.username}<br><br><br><br>
```
#### 1.如果访问其他Context中的对象，由于他们不是根对象，所以在访问时，需要添加#前缀。<br>
```xml
<s:property value="#request.username"/><br>
<s:property value="#session.username"/><br>
<s:property value="#application.username"/><br><br>
<s:property value="#request['username']"/><br>
<s:property value="#parameters.cid[0]"/><br>
<s:property value="#attr.username"/><br><br>
```
> 访问对象栈中对象可不加#

#### 2.如果要访问根对象（即ValueStack）中对象的属性，则可以省略#命名对象，直接访问该对象的属性即可。<br>
```xml
<s:property value="msg"/><br><br>

<s:property value="name"/><br> 
<s:property value="sex"/><br>
<s:property value="age"/><br>
<s:property value="salary"/><br><br>
```
```java
// 深入理解值栈中的 ObjectStack
// 【后台代码：】 
vs.getRoot().add(0,new Person()); 
```
【若有多个name属性名】只取出栈中第一个

#### 用法3:构造Map
```xml
<s:radio list="#{'01':'男','02':'女'}"></s:radio><br><br><br><br>
<s:property value="#request.username"/><br>
<s:property value="%{#request.username}"/>
```	
%的用法：“%”符号的用途是在标签的属性值被理解为字符串类型时，告诉执行环境%{}里的是OGNL表达式。
%{}是万能用法，无论里面的表达式是不是ognl表达式，都会强制理解为ognl表达式
#### 【“$”有两个主要的用途】

1 *  用于在国际化资源文件中，引用OGNL表达式<br>
`<s:text name="ognl" /><br><br>`
在properties文件中配置：`ognl=${error} ognl`
取的是值栈中的error属性  代码：`valueStack1.set("error", "error_valueStack");`

2 *  在Struts 2配置文件中，引用OGNL表达式<br>
`<s:property value="#parameters.msg[0]"/><br><br>`
`<result name="s" >ognl/ognl.jsp?msg=${msg}</result>`
这里的msg是request的param 使用 ${} 访问的都是值栈里的

`<s:debug></s:debug>` 能查看值栈状态
### 9.4【OGNL标签】
