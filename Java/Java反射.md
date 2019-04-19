# 1， 获取类

- 通过Object类中的getClass()方法

```
String str = "你好";
Class<?> cls = str.getClass();
```

- 通过具体的类名的位置

```
Class<?> cls = java.lang.String.class;
```

- 通过forName()

```
Class<?> cls = Class.forName("java.lang.String");
```

# 2， 通过类获取对象实例

```
// 该类须有无参构造器
Book book = (Book) cls.newInstance();
```

# 3, 利用反射调用类的其他结构

- 操作构造方法

  - 使用newInstance()操作无参构造方法

  > 使用Class类中的newInstance()方法进行实例化操作， 但该方法必须要求类有无参构造方法

  - 使用Class类中的getConstructors()获取所有构造方法

  ```
  Class<?> cls = Class.forName("first.Book");
  Constructor<?>[] constructors = cls.getConstructors();
  ```

  - 使用Class类中的getConstructor获取指定参数类型的构造方法

  ```
  Class<?> cls = Class.forName("first.Book");
  Constructor constructor = cls.getConstructor(String.class, String.class);
  // 实例化对象
  Book book = (Book) constructor.newInstance("java", "123");
  System.out.println(book);
  ```

- 操作类中方法

  - 获取类本身定义的方法， 不包含由继承获取到的方法

    - 获取所有方法

    ```
    Class<?> cls = Class.forName("first.Book");
    Method[] methods = cls.getDeclaredMethods();
    for (Method method : methods) {
        System.out.println(method);
    }
    ```

    - 获取指定的方法

    ```
    // 传入方法名和参数类型
    Method method = cls.getDeclaredMethod("setName", String.class);
    ```

  - 获取所有方法， 包含由继承获取到的方法

    - 获取所有方法

    ```
    Class<?> cls = Class.forName("first.Book");
    Method[] methods = cls.getMethods();
    for (Method method : methods) {
        System.out.println(method);
    }
    ```

    - 获取指定的方法

    ```
    Method method = cls.getMethod("setName", String.class);
    ```

  - 调用方法

  ```
  Class<?> cls = Class.forName("first.Book");
  Object object = cls.newInstance();
  Method method = cls.getMethod("setName", String.class);
  // 调用方法
  method.invoke(object, "hello");
  ```

- 调用成员

  - 取得自己定义的成员

    - 取得所有成员

    ```
    Class<?> cls = Class.forName("first.Book");
    Field[] fields = cls.getDeclaredFields();
    for (Field field : fields) {
        System.out.println(field);
    }
    ```

    - 获取单个成员

    ```
    Class<?> cls = Class.forName("first.Book");
    Field field = cls.getDeclaredField("name");
    System.out.println(field);
    ```

  - 取得所有成员， 包含由继承获取的成员， 但无法取得私有

    - 取得所有成员

    ```
    Class<?> cls = Class.forName("first.Book");
    Field[] fields = cls.getFields();
    for (Field field : fields) {
        System.out.println(field);
    }
    ```

  - 获取值

  ```
  Class<?> cls = Class.forName("first.Book");
  Object object = cls.newInstance();
  Field field = cls.getDeclaredField("name");
  // 取消封装
  field.setAccessible(true);
  // 设置值
  field.set(object, "你好");
  System.out.println(field.get(object));
  ```

# 4, 属性文件内容操作

- 通过ResourceBundle获取classPath下的属性文件

```
ResourceBundle bundle = ResourceBundle.getBundle("test");
String city = bundle.getString("name");
```

- 通过Properties对象获取配置文件

```
Properties pro = new Properties();
pro.load(new FileInputStream(new File("./test.properties")));
String name = (String) pro.get("name");
```

- 使用Properties保存配置文件

```
Properties pro = new Properties();
pro.setProperty("name", "java");
pro.setProperty("study", "sdf");
pro.store(new FileOutputStream(new File("test.properties")), "one file");
```

# 5, 注解

- 获取类的注解

```
Class<?> cls = Class.forName("first.Book");
Annotation[] as = cls.getAnnotations();
for (Annotation a : as) {
    System.out.println(a);
}
```

- Annotation的三个作用范围

  - CLASS

  > 程序编译时起作用

  - RUNTIME

  > 程序运行时起作用

  - SOURCE

  > 在源代码中起作用

- 自定义Annotation

  ```
  @Retention(value = RetentionPolicy.RUNTIME)
  public @interface GetItem {
      // 设置属性内容
      String name() default "hello";
      String value();
  }
  ```

- 获取指定的Annotation

```
Class<?> cls = Class.forName("first.Book");
GetItem annotation = cls.getAnnotation(GetItem.class);
System.out.println(annotation.name());
System.out.println(annotation.value());
```
