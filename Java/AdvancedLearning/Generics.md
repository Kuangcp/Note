`目录 start`
 
- [泛型](#泛型)
    - [入门](#入门)
        - [简单使用](#简单使用)
            - [类型擦除](#类型擦除)
        - [约束和局限性](#约束和局限性)
        - [泛型类型的继承规则](#泛型类型的继承规则)
        - [通配符类型](#通配符类型)
            - [子类型限定的通配符 extends](#子类型限定的通配符-extends)
            - [超类型限定的通配符 super](#超类型限定的通配符-super)
                - [应用](#应用)
            - [无限定通配符](#无限定通配符)
            - [通配符捕获](#通配符捕获)
        - [反射和泛型](#反射和泛型)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 泛型
> [开始学习的兴趣来源](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665514015&idx=1&sn=12409f705c6d266e4cd062e78ce50be0&chksm=80d67c5cb7a1f54a68ed83580b63b4acded0df525bb046166db2c00623a6bba0de3c5ad71884&scene=21#wechat_redirect)

[参考博客: Java总结篇系列：Java泛型](http://www.cnblogs.com/lwbqqyumidi/p/3837629.html)  
泛型，即“参数化类型”。一提到参数，最熟悉的就是定义方法时有形参，然后调用此方法时传递实参。  
那么参数化类型怎么理解呢？顾名思义，就是将类型由原来的具体的类型参数化，类似于方法中的变量参数，此时类型也定义成参数形式（可以称之为类型形参），然后在使用/调用时传入具体的类型（类型实参）。  
[参考博客: Java深度历险（五）——Java泛型](http://www.infoq.com/cn/articles/cf-java-generics)
## 入门
>泛型程序设计划分为三个熟练级别 基本级别就是仅仅使用泛型类,典型的是像ArrayList这样的集合--不必考虑他们的工作方式和原因,大多数人会停留在这个级别.直到出现了什么问题. 当把不同的泛型类混合在一起的时候,或是对类型参数一无所知的遗留代码进行对接时,可能会看到含糊不清的错误消息.如果这样的话,就需要系统的进行学习Java泛型来系统地解决问题.  
> 泛型类可以看作普通类的工厂  -- Java核心技术卷 2004(1.5)  

### 简单使用
>- [简单泛型类示例](https://github.com/Kuangcp/JavaBase/blob/master/src/main/java/com/generic/simple/Pair.java)

例如该行定义 : `public abstract class RoomCache<P extends PlayerBO, M extends MemberBO, V extends VideoDataBO<M>, R extends RoomBO<M, V>> extends AbstractCache<PlatformRoomId, R> {}`

- 类型变量使用大写的一个字母这是代表:
    - `E` 集合的元素类型 
    - `K V` 表示表的关键字和值的类型 
    - `T U S` 等就表示任意类型
    - 

#### 类型擦除
- 不同于C++的泛型,C++是将模板类组合出来的生成一个新的类,Java则是进行类型擦除,然后再类型强转
- 例如 `public static <T extends Comparable> T min (T[] list)`
    - 擦除后就只剩下一个方法 `public static Comparable min(Comparable[] list)`
-  [泛型类擦除示例](https://github.com/Kuangcp/JavaBase/blob/master/src/main/java/com/generic/simple/DateInterval.java)

- 例如该方法签名 `public static  <T extends Comparable & Serializable> T getMax(T[]list)`
    - 限制了必须是实现了两个接口的类才能使用, 估计为了少创关键字所以使用的是extends关键字来表示T要实现两个接口
    - 同样的可以加在类的签名上,进行限制类的泛型类型 `public class Pair <T extends Comparable>{} `

> 在Java的继承中,可以根据需要拥有多个接口超类型,但限定中至多只有一个类,如果用一个类作为限定,他必须是限定列表中的第一个

******************************
### 约束和局限性
> 以下代码示例:涉及的类Pair在上述的代码中已经定义, Human和Student是继承关系
> 并且因为看的 Java核心技术卷 比较老 jdk是1.5的所以没有用7的菱形语法简化泛型 7可以省去右边的类型: `Pair<Double> pair = new Pair<>();`

- | _不能使用基本类型实例化类型参数_
    - 也就是说没有`Pair<double>`只有`Pair<Double>`
    - 因为类型擦除后,类型是Object并不能放double的值, 但是这样做与Java语言中基本类型的独立状态相一致.
    - 当包装器类型(wrapper type)不能接受替换时,可以使用独立的类和方法处理他们  
- | _运行时类型查询(eq或者instanceof)只适用于原始类型_
    - 比如`Pair<T>` 和`Pair<String>`是等价的,因为类型擦除
    - `Pair<String> pair1` `Pair<Date> pair2` pair1.getClass()和pair2.getClass()是等价的都是返回Pair.class
- | _不能抛出也不能捕获泛型类实例_
    - 错误的示例:
        - `public class Problem<T> extends Exception{}`
        - `public static <T extends Throwable> void doWork(){try{}catch(T t){}}`
    - 正确示例:
        - 在异常声明中使用类型变量 
        - `public static <T extends Throwable> void doWork() throws T{.. catch(){throw t;}}`
- | _参数化类型的数组不合法_
    - 例:`Pair<String>[] list = new Pair<String>[10];`
    - 因为擦除后 list是Pair[]类型,然后就能转成Object[], 就失去了泛型的作用
    - 如果要使用的话最好直接使用集合 ArrayList:` ArrayList<Pair<String>>`,安全又高效
```java
    Object[] array = list;
    array[0] = "hi";//  编译错误
    array[0] = new Pair<Date>(); //通过数组存储的检测,但实际上类型错误了,所以禁止使用参数化类型的数组
```

- | _不能实例化类型变量(T)_
    - 非法 `new T(){}`
```java
    public Pair(){
        first = new T();
        second = new T();
    }
    first = T.class.newInstance() //非法 T.class是不合法的
    //要实例化一个Pair<T>的对象就要如下:
    public static <T> Pair<T> initPair(Class<T> c){
        try{
            return new Pair<T>(c.newInstance(), c.newInstance());
        }catch (Exception e){
            return null;
        }
    }
    // 如下调用
    Pair<String> pair = Pair.initPair(String.class);
    // 因为Class本身是泛型, String.class其实是Class<String>的实例
    // 也不能实例化为一个数组 new T[5]
```
- | _泛型类的静态上下文中类型变量无效_
    - 不能在静态域中使用类型变量 如下:
    - 如果这段代码能执行,那就可以声明一个 Singleton<Random> 共享随机数生成类,
    - 但是声明之后,类型擦除,就只剩下了Singleton类,并不能做对应的事情,所以禁止这样的写法
```java
    private static T first; // 错误
    public static T getFirst(){ // 错误
        return first;
    }
```
- | _注意泛型擦除后的冲突_
    - 当类型擦除时,不能创建引发冲突的相关条件
    - 例如 新实现一个类型变量约束的equals方法就会和Object原方法冲突 补救方法就是重命名该方法了
    
```java
    public class Pair<T>{
        public boolean equals (T value){
            return ..
        }
    }
```
`泛型规范说明`
-  要想支持擦除的转换,就需要强行限制一个类或类型变量不能同时成为两个接口类型的子类,而这两个接口是同一接口的不同参数化
    - 以下代码就是非法的, GregorianCalendar 实现了两个接口,两个接口是Comparable接口的不同参数化,这是不允许的
```java
    class Calendar implements Comparable<Calendar>{}
    class GregorianCalendar extends Calendar implements Comparable<GregorianCalendar>{} // 错误
```
- 但是如下又是合法的
```java
    class Calendar implements Comparable{}
    class GregorianCalendar extends Calendar implements Comparable{}
```
- 很有可能是桥方法有关,不可能有两个一样的桥方法(因为两个接口其实是一个接口的不同参数化,桥方法的方法签名是一致的)

*******************************************
### 泛型类型的继承规则

> 例如 父子类: Human Student  那么 Pair<Human> Pair<Student> 是继承(inherit)关系么,答案是否定的!!

```java
    Pair<Human> humans = new Pair<Human>(man, woman);
    Pair<Student> classmates = humans;// illegal, but suppose it wasn't
    classmates.setSecond(junior) // 如果上面合法,那么这里是肯定可以执行的, 因为泛型类型变成了Student
    //那么就有了问题了,原有的人类类型限制的对象中,出现了小学生
    //所以不允许这样的类型变量约束的类进行多态
    
    // 但是数组可以这样写是因为数组会有自己的检查保护
    Human[] humans = {man, woman};
    Student[] students = humans;
    students[0] = junior ;// 虚拟机将抛出 ArrayStoreException 异常
```

******************
> 永远可以将参数化类型转换为一个原始类型, Pair<Human> 是原始类型Pair的一个子类型,转换成原始类型也会产生错误  
> [相关测试类](https://github.com/Kuangcp/JavaBase/blob/master/src/test/java/com/generic/simple/PairTest.java)  
```java
    Pair<Human> humans = new Pair<Human>(man, woman);
    Pair other = humans;
    other.setFirst(new String("wtf"))// 只是会有一个编译时的警告(类型未检查),但实际上都看得出这明显是错误的
    // 那么在后续代码中继续当做Human对象进行引用,必然就会有ClassCastException
    // 所以这样的写法尽量避免,这里的设计 就失去了泛型程序设计提供的附加安全性.(挖的坑)
```

***************
> 泛型类可以扩展或实现其他的泛型类,就这一点而言,和普通类没有什么区别

- 例如 ArrayList<T> 实现List<T>接口, 这意味着一个ArrayList<Student>可以转换为List<Studnet> 
    - 但是一个ArrayList<Student>不是ArrayList<Human>或者List<Student>.

**************************************************************************

### 通配符类型
#### 子类型限定的通配符 extends
> 通配符上限  顾名思义,就是限定为该类及其子类, 例如: `Pair<? extends Human>` 表示任何Pair泛型类型并且他的类型变量要为Human的子类  

> 例如编写一个方法 `public static void printMessage(Pair<Human> human){}`  
> 正如上面所说, Pair<Student>类型的变量是不能放入这个方法的,因为泛型变量是没有继承关系, 这时候就可以使用这个通配符:  
>> `public static void printMessage(Pair<? extends Human>)` 可以get不能set
```java
    Pair<Human> humans = new Pair<Human>(man, woman);
    Pair<? extends Human> classmates = humans;// 编译通过
    classmates.setSecond(junior) // 编译错误,泛型约束起作用了

    // 分析其泛型类实现可以理解为:
    ? extends Human getFirst()
    void setFirst(? extends Human)
    // 这样的话是不可能调用setFirst方法, 对于编译器来说,只是知道入参是Human的子类,但是类型并不明确,所以不能正常调用
    // 使用get方法就不会有问题, 泛型起作用了.将get返回值赋值给Human的引用也是完全合法的,这就是引入该统通配符的关键之处
```

#### 超类型限定的通配符 super
> 通配符下限  顾名思义就是限定为父类, 通配符限定和类型变量限定十分相似, 但是可以指定一个超类型限定(supertype bound)  
> `? super Student` 这个通配符就限定为Student的所有超类型(super关键字已经十分准确的描述了这种关系)  
>> 带有超类型限定的通配符的行为和前者相反,可以为方法提供参数,但不能使用返回值即 可以 set 但是不能get

```java
    // Pair<? super Student> 例如这种定义
    void setFirst(? super Student)
    ? super Student getFirst()
    // 编译器不知道setFirst方法的确切类型,但是可以用任意Student对象(或子类型) 调用他, 而不能使用Human对象调用.
    // 然而,如果调用getFirst,泛型没有起作用,只能将返回值用Object接收
```
> [以上两种情况的相关测试类](https://github.com/Kuangcp/JavaBase/blob/master/src/test/java/com/generic/simple/PairTest.java) 

> 总结: 类定义上的泛型变量:  
>> 子类型限定: <? extends Human> 是限定了不能set,但是保证了get  
>> 超类型限定: <? super Student> 限定了不能正确get,但是保证了set.  

##### 应用
> [参考博客: 使用通配符简化泛型使用](https://www.ibm.com/developerworks/cn/java/j-jtp04298.html)

- 示例1:`public static <T extends Comparable<T>> T min(T[] list);`
    - 限定了入参和返回值是 是实现了Comparable接口的某个类型 因为Comparable也是一个泛型类, 所以也进行限定类型
    - 这样的写法要比 T extends Comparable 更为彻底
    - 例如计算一个String数组的最小值 T 就是 String类型的, String是Comparable<String>的子类型
        - 但是当处理GregorianCalendar, GregorianCalendar是Calendar的子类, 并且Calendar实现了`Comparable<Calendar>`
        - 因此GregorianCalendar实现的是`Comparable<Calendar>`, 而不是Comparable<GregorianCalendar>
        - 这种情况下 `public static <T extends Comparable<? super T>> T min(T[] list)` 就是安全的

- 示例2: `public static <T extends ExcelTransform> List<T> importExcel(Class<T> target)`
    - 该方法实现了, 传入继承了ExcelTransform接口的类对象, 得到该类的List集合
    - `<T extends ExcelTransform> boolean` 这样写编译没报错, 那么就是说, 就是一个泛型的定义, 后面进行引用, 省的重复写
    - 简单的写法就是 `public static <T> List<T> importExcel(Class<T> target)`

- 示例3: Spring4.x 添加的泛型依赖注入 , 使用的JPA就是依赖该技术   [spring学习笔记（14）——泛型依赖注入](http://blog.csdn.net/u010837612/article/details/45582043)

> 对于应用程序员, 可能很快的学会掩盖这些声明, 想当然地认为库程序员做的都是正确的, 如果是一名库程序员, 一定要习惯于通配符  
> 否则还要用户在代码中随意地添加强制类型转换直至可以通过编译.

#### 无限定通配符
> TODO 对其使用场景 尚有疑问,以后再解

```java
    // 例如 Pair<?>
    ? getFirst() // 方法的返回值只能赋值给一个Object
    void setFirst(?) // 方法不能被调用,甚至不能用Object调用.
    // Pair<?> 和 Pair 本质的不同在于: 可以用任意Object对象调用原始的Pair类的setObject(set方法,因为类型擦除 入参是Object, 简称setObject)方法 
```
- 例如 [这个hasNull()方法](https://github.com/Kuangcp/JavaBase/blob/master/src/test/java/com/generic/simple/PairTest.java)用来测试一个pair是否包含了指定的对象, 他不需要实际的类型.

#### 通配符捕获
> TODO 学习和理解使用场景

- 如果编写一个交换的方法  
```java
    public static void swap (Pair<?> p){
        ? temp = p.getFirst(); // 错误, 不允许将?作为类型
        p.setFirst(p.getSecond());
        p.setSecond(temp);
    }
```
- 但是可以编写一个辅助方法
```java
    public static <T> void swapHelper(Pair<T> p){
        T temp = p.getFirst();
        p.setFirst(p.getSecond());
        p.setSecond(temp);
    }
```
- swapHelper是一个泛型方法, 而swap不是, 它具有固定的Pair<?>类型的参数, 那么现在就可以这样写:
    - `public static void swap(Pair<?> p){swapHelper(p);}`
    - 这种情况下, swapHelper方法的参数T捕获通配符, 它不知道是哪种类型的通配符,但是这是一个明确的类型 并且<T>swapHelper 在T指出类型时,才有明确的含义
    - 当然,这种情况下并不是一定要用通配符, 而且我们也实现了没有通配符的泛型方法

> 但是下面这个通配符类型出现在计算结果中间的示例

```java
    public static void maxMinBonus(Student[] students, Pair<? super Student> result){
        minMaxBonus(students, result);
        swapHelper(result);
    }
    // 在这里,通配符捕获机制是不可避免的, 但是这种捕获只有在许多限制情况下才是合法的.
    // 对于编译器而言, 必须能够确信通配符表达的是单个, 确定的类型.
```

### 反射和泛型
> [官方Java7的Class文档](https://docs.oracle.com/javase/7/docs/api/java/lang/Class.html) | []()
> 现在Class类是泛型的, 例如String.class实际上是Class<String>类的对象(事实上是唯一的对象)  
> 类型参数十分有用, 这是因为他允许Class<T>方法的返回类型更加具有针对性.下面Class<T>的方法就使用了类型参数
```java
    T newInstance()
    T cast(Object obj)
    T[] getEnumConstants()
    Class<? super T> getSuperclass()
    Constructor<T> getConstructor(Class... paramterTypes)
    Constructor<T> getDeclaredConstructor(Class... paramterTypes)
```
- newInstance方法返回一个示例, 这个实例所属的类由默认的构造器获得, 它的返回类型目前被声明为T, 其类型与Class<T>描述的类相同, 这样就免除了类型转换.
- 如果给定的类型确实是T的一个子类型, cast方法就会返回一个现在声明为类型T的对象, 否则, 抛出一个BadCastException异常
- 如果这个类不是enum类或类型T的枚举值的数组, getEnumConstants方法将返回Null.
- 最后, getConstructor与getDeclaredConstructor方法返回一个Constructor<T>对象.Constructor类也已经变成泛型, 以便 newInstance方法有一个正确的返回类型.

TODO 还要继续看书

```java
    // 传入一个Class对象, 得到Class对应类型的实例
    public <T> T get(Class<T> target, String name);
    // 加上约束
    public <T extends Runable> T get(Class<T> target, String name);
```