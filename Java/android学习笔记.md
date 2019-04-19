# 一、Android生命周期
## 1，Activity生命周期
### 1,Activity的四种状态
			1,Running状态：一个新Activity启动入栈后，它在屏幕最前端，
			  处于栈的最顶端，此时它处于可见并和用户交互的激活状态。
			2,Paused状态：当Activity被另一个透明或者Dialog样式的Activity覆盖时的状态
			  此时它依然与窗口管理器保持连接，系统继续微乎其内部状态，所以它仍然可见，
			  但它已经失去了焦点，固不可与用户交互。
			3,Stopped状态：当Activity不可见时，Activity处于Stopped状态。
			  Activity将继续保留在内存中保持的所有状态和成员信息，假设系统其他地方需要内
			  存这是他是被回收对象的主要候选。当Activity处于Stopped状态时，一定要保存当前
			  数据和当时UI状态，否则一旦Activity退出或者关闭时，当前的的数据和UI状态将随丢失
			4,Killed状态：Activity被“杀死”以后后者被启动之前，处于Killed状态，这时
			  Activity已被移出Activity堆栈中，需要重新启动才可以显示和使用。
	转换关系：Running状态可转换成Paused状态或者Stopped状态；Paused状态可转换成Stopped状
			 态；Running状态、Paused状态和Stopped状态都可转换成Killed状态；Killed状态
			 可转换成Running状态
### 2,Activity的事件的回调方法
			1,onCreate()方法：在创建Activity是被调用。使用Eclipse等创建项目时会自动创建
			  一个Activity，并重写onCreate(Bundle savedInstanceState)方法，用于
			  Activity的执行初始化。
			2,onStart()方法：启动Activity时被回调，也就是当一个Activity变为显示时被回调。
			3,onRestart()方法：重启Activity时被调用，该方法总是在onStart以后执行。
			4,onPaused()方法：暂停Activity时被调用。在该方法执行完毕以前，下一个
			  Activity都不能被恢复。该方法通常用于持久保存数据。
			5,onResume()方法：当Activity由暂停状态恢复为活动状态时被调用。调用该方法后
			  该Activity位于Activity栈的栈顶。该方法总是在onPause()方法后执行。
			6,onStop()方法：停止Activity是被调用。
			7,onDestroy()方法：销毁Activity是被调用。
# 二、UI设计
## 1,界面布局
### 1,相对布局（RelativeLayout）：
##### 放入其中的组件是相对于兄弟组件，或者是父容器的位置进行排列的
###### RelativeLayout常用属性：
- android:gravity
> 用于设置布局管理器中个子组件的摆放位置  

- android:ignoreGravity
> 用于指定那个组件不受gravity属性的影响
###### RelativeLayout.LayoutParams支持的常用属性
- android:layout_above
> 其属性值为其他UI组建的id属性，用于指定该组件位于那个组件的上方

- android:layout_alignBottom
> 其属性值为其他UI组件的id属性，用于指定该组件与那个组件的下边界对齐

- android:layout_alignLeft
> 其属性值为其他UI组件的id属性，用于指定该组件与哪个组件的左边界对齐

- android:layout_alignParentBottom
> 其属性值为boolean值，用于指定该组件是否与布局管理器的底端对齐

- android：layout_alignParentLeft
> 其属性值为boolean值，用于指定该组件是否与布局管理器的左端对齐

- android:layout_alignRight
> 其属性值为其他UI组件的id属性，用于指定该组件与哪个组件的右边界对齐

- android:layout_alignTop
> 其属性值为其他UI组件的id属性，用于指定该组件与哪个组件的上边界对齐

- android:layout_below
> 其属性值为其他UI的id属性，用于指定该组件位于哪个组件的下方

- android:layout_toLeftOf
> 其属性值为其他UI组件的id属性，用于指定该组件位于哪个组件的左侧

- android:layout_toRightOf
> 其属性值为其他UI组件的id属性，用于指定该组件位于哪个组件的左侧
		
### 2,线性布局(LinearLayout)
##### 将放入其中的组件按照垂直或者水平方向来布局，也就是控制放入其中的组件横向排列或纵向排列
###### LinearLayout常用的属性
- android:orientation
> 用于设置布局管理器内组件的排列方式，可选值为horizontal和vertical，默认值为vertical。其  
> 中horizontal表示水平排列，vertical表示垂直排列

- android：gravity
> 用于设置布局管理器内组件的显示位置，其可选值为包括top、bottom、left、right、  
> center\_vertical、fill\_vercal、center\_horizontal、fill\_horizontal、center、  
> fill、clip\_vertical和clip\_vertical。这些值也可以同时同时指定，各属性值之间用竖线  
> 隔开(竖线前后不能有空格)。如指定右下角：right|bottom

### 3，帧布局(frameLayout)：
##### 每加入一个组件都将创建一个空白的区域，通常称为一帧，这些帧都会被放置在屏幕的左上角，多个组件层叠在屏幕排序，后面的组件将会覆盖前面的组件
###### FrameLayout常用属性
- android:foreground
> 设置该帧布局的前景图像

- android:froegroundGravity
> 定义绘制前景图像的gravity属性，也就是前景图像现实的位置

### 4，表格布局(TableLayout)
##### 与常见的表格类似，一行、列形式来管理放入其中的UI组件。在表格布局中可以添加多个TableRow标记，表示表格的一列
###### TableLayout支持的的属性
- android:collapseColumns
> 设置需要隐藏的列的列序号（序号从0开始）,多个列序号之间用“，”分隔

- android:shrinkColumn
> 设置允许被收缩的列的列序号(序号从0开始)，多个列序号之间用“，”分隔

- android:stretchColumn
> 设置允许被拉伸的列的列序号(序号从0开始),多个列序号之间用","分隔

### 5，网格布局(GridLayout)
##### 屏幕被虚拟的细线划分成行、列和单元格，每个单元格放置一个组件，并且这个组件也可以跨行或跨列摆放
###### GridLayout常用的属性
- android:columnCount
> 用于指定网格的最大列数

- android:rowCount
> 用于指定网格的最大行数

###### GridLayout.LayoutParams常用的属性
- android:layout_column
> 用于指定该子组件位于网格的第几行

- android:layout_columnSpan
> 用于指定该子组件横向跨几列(索引从0开始)

-android：layout_row
> 用于指定该组件位于网格的第几行(索引从0开始)

- android:layout_rowSpan
> 用于指定该子组件纵向跨几行

- android:layout_gravity
> 用于指定该组件采用什么方式占据该网格的空间，其可选值有top、bottom、left、right、  
> center\_vertical、fill\_vertical、center\_horizontal、fill\_horizontal、  
> center、fill、clip\_vertical、clip\_horizontal、start、end

## 2，界面组件

## 3，界面事件
### 1,按键事件
### 2，触摸事件
### 3，点击事件
		
# 三、Intent
## Intent（意图）
### 无返回参数
#### 1,显示启动
##### 指在启动时必须在Intent中指明要启动的Activity所在的类
> 创建意图  
> Intent intent=new Intent(MainActivity.this, test_Activity.class);  
> 启动Activity(无返回值)  
> startActivity(intent);  
#### 2,隐示启动
##### 指由Android系统根据Intent的action(动作)和data(数据)决定启动哪一个Activity
> 创建意图  
> Intent intent=new Intent();  
> 为Intent设置动作  
> intent.setAction(Intent.ACTION_VIEW);  
> 为Intent设置数据(Uri.parse用于把字符串解释成URI对象)  
> intent.setData(Uri.parse("https://github.com/dragonhht"));   
> 将Intent传递给Activity   
> startActivity(intent);

#### 标准Activity action说明
- ACTION_MAIN  
	作为初始Activity启动，没有数据输入输出
- ACTION_VIEW  
	将数据显示给用户
- ACTION_ATTACH_DATA  
	指定某块数据将被附加到其他地方
- ACTION_EDIT  
	将数据显示给用户用于编辑
- ACTION_PICK  
	从数据中选择一项，并返回该项
- ACTION_CHOOSER  
	显示Activity选择器，允许用户在继续前按需选择
- ACTION_GET_CONTENT  
	允许用户选择特定类型的数据并将其返回
- ACTION_DIAL  
	使用提供的数据拨打电话
- ACTION_CALL  
	使用提供的数据给某人拨打电话
- ACTION_SEND  
	向某人发送消息，接受者未指定
- ACTION_SENDTO  
	向某人发送信息，接受者已指定
- ACTION_ANSWER  
	接听电话
- ACTION_INSERT  
	在给定容器中插入空白项
- ACTION_DELETE  
	从容器中删除给定的数据
- ACTION_RUN  
	无条件运行数据
- ACTION_SYNC  
	执行数据同步
- ACTION_PICK_ACTIVITY  
	挑选给定Intent的Activity，返回选择的类
- ACTION_SEARCH  
	执行查询
- ACTION_WEB_SEARCH  
	执行联机查询
- ACTION_FACTORY_TEST  
	工厂测试的主入口点

### 有返回参数
> 创建意图  
> Intent intent=new Intent(MainActivity.this, test_Activity.class);  
> startActivityForResult(intent, 0x717);  //使用startActivityForResult启动新的Activity  
#
>Intent intent=getIntent();   // 获取Intent对象  
>setResult(0x717, intent);   //设置返回的结果码，并返回调用该Activity的Activity
		

### 3,Activity间交互数据
#### 使用Bundle
- 存放数据
> Bundle bundle=new Bundle();  //创建并实例化一个Bundle对象  
> bundle.putString("test", "Myname");  //将数据放入Bundle  
> intent.putExtras(bundle);     //将Bundle对象添加到Intent对象中

- 接收数据
> Intent intent=getIntent();   // 获取Intent对象  
> Bundle bundle=intent.getExtras();  //获取传递的数据包  
> String value=bundle.getString("test");    //通过键获取数据

### 4,Intent过滤器

# 四、四大组件

## 1,BroadcastReceiver
### 用于接收广播通知的组件。
#### 基本步骤:
###### 1. 编写Receiver类，继承BroadcastReceiver类，重写onReceive方法
###### 2. 在AndroidManifest.xml中注册BroadcastReceiver
><receiver android:name=".Receiver">  
><intent-filter>  
>       <action android:name="android.provider.Telephony.SMS_RECEIVED" />  
></intent-filter>  
></receiver>

###### 3. 在AndroidManifest.xml文件中添加允许接受短信的权限
><uses-permission android:name="android.permission.RECEIVE_SMS" />


## 2、Service
#### 用于在后台完成用户指定的操作

### 生命周期中一些重要的回调方法
- onCreate（）
> 当服务第一次创建时，系统调用方法执行一次性建立过程，如果服务已经启动，该方法不被调用

- onStartCommand()
> 当其他组件，例如Activity调用startService()方法请求服务启动时，系统调用该方法，一旦该方法执行，服务就启动(处于“started”状态)并在后台无限期运行。如果开发人员实现该方法，则需要在任务完成时调用stopSelf()或stopService()方法停止服务(如果仅想提供绑定，则不必实现该方法)  

- onBind()
> 当其他组件调用bindService()方法想与服务绑定时，系统调用该方法。在该方法的实现中，开发人员必须通过返回IBinder提供客户端用来与服务通信的接口。该方法必须实现，但如果不想绑定，则应该放回null

- onUnBind()
> 当调用者通过UNbindService()函数取消绑定Service时，onUnBind()方法将被调用如果onUnBind()函数返回true，表示重新绑定服务时，onRebind（）函数将被调用

- onDestroy（）
> 当服务不再使用并将销毁时，系统调用该方法。服务应该实现该方法来清理诸如线程、注册监听器、接受者等资源。这是服务收到的最后的调用。  


###创建Service的步骤

- 创建一个继承Service的子类,根据需要重写一些方法
- 在AndroiManifest.xml文件中配置Service(在<application\>中增加<service\>子标签)


# 五，图像绘制
## 1,绘制2D图像
### 1,创建画布
>1，创建一个继承View类的视图，对于xml引用必须有:  
>  public DrawView(Context context, AttributeSet attrs)  
>  public DrawView(Context context, AttributeSet attrs, int defStyleAttr)等构造方法  
>2，在布局文件中删除默认组件,使用帧布局管理器，并添加自定义视图  
>3，在onDraw方法中编写绘图代码

# 六，网络技术
## 1，通过http访问网络
### 1，使用HttpURLConnection访问网络

# 七,android6.0新增重点特性
## 权限机制
### 新增API
- checkSelfPermission
> 用于检测app是否拥有权限

- requestPermissions()
> 申请权限

- onRequestPermissionResult()
> 处理回调结果

- shouldShowRequestPermissionRationale
> 用于对用户进行解释，该权限作用(在用户拒接权限后出现)

### 权限添加步骤
- 在AndroidManifest中添加需要的权限

- 检查权限

- 申请授权

- 处理权限申请回调
（具体实现代码--我的音乐播放器）



