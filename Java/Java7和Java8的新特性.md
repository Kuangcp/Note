# Java 7
## 1, Switch中支持String
> Java6之前case语句中的常亮只支持 byte, char, short, int或枚举变量,Java7中增加了String

## 2, 数值文本
### 1, 二进制文本
-	Java7之前处理二进制 `int x = Integer.parseInt("1100110", 2)`
-	Java7处理二进制 `int x = 0b1100110`

### 2, 数字中可使用下划线
-	Java7中为区分 100000000 和 10000000 可使用
```
long n1 = 100_000_000;
long n2 = 10_000_000;
```

## 3, 异常处理
> try-with-resources特性,使得不用手动关闭流(但有些情况下还是无法关闭的,如不能正确构建流的情况下)
```
File file = new File("xmlStudy/src/main/java/xml/study/test.xml");
        try (InputStream inputStream = new FileInputStream(file)) {
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
```

## 4, 新 I/O (NIO.2)
### 1, Path
```
// 创建路径
Path list = Paths.get("xmlStudy");
// 获取文件名
System.out.println(list.getFileName());
// 获取名称元素数量
System.out.println(list.getNameCount());

File file = new File("test.xml");
// 将旧API的File转换成新的Path
Path path = file.toPath();
// 将Path转换成File
File fiel2 = path.toFile();
```

### 2, 文件系统 I/O
-	创建和删除文件
```
// 创建文件
Path path = Paths.get("test2.xml");
Path file = Files.createFile(path);
// 删除文件
Files.delete(path);
```

-	文件的复制和移动
```
// 复制
Path source = Paths.get("test2.xml");
Path path = Paths.get("src/test2.xml");
Files.copy(source, path);
// 移动
Path path = Paths.get("test2.xml");
Path source = Paths.get("src/test2.xml");
 Files.move(source, path);
```

-	读写数据 (可指定文件的打开方式, WRITE, READ, APPEND (StandardOpenOption.WRITE))
```
Path path = Paths.get("test.txt");
// 打开一个带缓冲区的读取器
try (BufferedReader reader =
                     Files.newBufferedReader(path, StandardCharsets.UTF_8)) {
String line;
while ((line = reader.readLine()) != null) {
       System.out.println(line);
     }
}
// 打开带有一个缓冲区的写入器
try (BufferedWriter writer =
                     Files.newBufferedWriter(path)) {
    writer.write("测试");
 }
// java7简化后的读取全部行和字节
List<String> lines = Files.readAllLines(path);
byte[] bytes = Files.readAllBytes(path);
System.out.println(lines);
```

-	异步 I/O
	-	将来式
	
	```
    Path path = Paths.get("test.txt");
    // 异步打开文件
    AsynchronousFileChannel channel = AsynchronousFileChannel.open(path);
    // 读取100000字节
    ByteBuffer buffer = ByteBuffer.allocate(100_000);
    Future<Integer> result = channel.read(buffer, 0);
    while (!result.isDone()) {
        System.out.println("其他事");
    }
    // 获取结果
    Integer bytesRead = result.get();
    System.out.println(bytesRead);
    ```
    -	回调式
    
    ```
    Path path = Paths.get("test.txt");
    // 异步打开文件
    AsynchronousFileChannel channel = AsynchronousFileChannel.open(path);
    // 读取100000字节
    ByteBuffer buffer = ByteBuffer.allocate(100_000);
    channel.read(buffer, 0, buffer, new CompletionHandler<Integer, ByteBuffer>() {
    // 读取调取完成时的回调方法
    @Override
    public void completed(Integer result, ByteBuffer attachment) {
       System.out.println(result);
    }
    @Override
    public void failed(Throwable exc, ByteBuffer attachment) {
       System.out.println(exc.getMessage());
     }
     });
     ```
# Java8
## 1, Lambda表达式
格式 `参数列表 -> Lambda主体`
> 可以在函数式接口上使用Lambda表达式 (函数式接口就是只定义一个抽象方法的接口)
-	Lambda表达式的示例
```
// Runnable使用Lambda表达式
Runnable r1 = () -> System.out.println("Lamdba表达式");
// 作为参数时使用
public void proccess(Runnable r) {
	r.run();
}
proccess(() -> System.out.println("Lamdba表达式"));
```

-	使用Java自带的函数式接口

	-	Predicate
	> 该接口定义了一个名叫test的抽象方法,它接受泛型T对象, 并返回boolean
	```
    Predicate<String> predicate = (String s) -> !s.isEmpty();
    ```
   -	Consumer
   	> 该接口定义了一个名叫accept的抽象方法, 它接受泛型T的对象,没有返回自(void).  
   	> 如果需要访问类型为T的对象,并对其执行某些操作,就可以使用该接口
   ```
    public <T> void forEach(List<T> list, Consumer<T> c) {
        for (T s : list) {
            c.accept(s);
        }
    }
    public void test() {
        forEach(Arrays.asList(1, 2, 3, 4, 5, 6),
                (s) -> System.out.println(s));
    }
   ```
   -	Function
   > 该接口定义了一个叫做apply的方法, 他接受一个泛型T对象的对象, 并返回一个泛型R的对象  
   > 如果你需要定义一个Lambda,将输入对象的信息映射到输出, 就可以使用这个接口
   ```
   public <T, R> List<R> map(List<T> list, Function<T, R> f) {
        List<R> result = new ArrayList<>();
        for (T s : list) {
            result.add(f.apply(s));
        }
        return result;
    }
    public void test() {
        List<String> list = Arrays.asList("haha", "in", "k");
        List<Integer> l = map(list,
                (s) -> s.length());
        for (int i : l) {
            System.out.println(i);
        }
    }
   ```
-	方法引用
格式 `静态类名或对象名::引用的类中的方法`

## 2, 流
> 它允许你以声明性的方式处理数据

-	示例
```
// 接收结果的集合
        List<String> resule =
                menu.stream()  // 从menu中获取流, 把stream换成parallelStream就可利用多线程
                    .filter(d -> d.getCalories() > 300) // 建立操作流,首先选出高热量的菜肴
                    .map(Dish::getName)                  // 获取菜名
                    .limit(3)                            // 只选前三个
                    .collect(toList());                  // 将结果存入另一个List中
        System.out.println(resule);

        menu.parallelStream()
                .forEach(System.out::println);
```

-	构建流

	-	由值构建流
	```
    Stream<String> stream = Stream.of("java7", "java8", "Lambda");
    ```
    -	由数组构建流
    ```
    int[] number = {1, 2, 3, 4, 5, 6, 7};
    int sum = Arrays.stream(number).sum();
    System.out.println(sum);
    ```
    -	由文件生成流
    > java.nio.file.Files中有很多静态方法都会返回一个流

	-	由函数生成流: 创建无限流
		-	迭代
		```
        Stream.iterate(0, n -> n + 2)
                .limit(10)
                .forEach(System.out::println);
        ```
        -	生成
        ```
        Stream.generate(Math::random)
                .limit(5)
                .forEach(System.out::println);
        ```

-	收集数据


## 3, 用Optional取代null
-	声明一个空的Optional
```
Optional<Car> optCar = Optional.empty();
```
-	根据一个空值创建Optional
```
// 如果car是一个null, 会立即抛出NullPointerException, 而不是等到访问car的属性时才返回错误
Optional<Car> optCar = Optional.of(car);
```
-	可接受空值的Optional
```
// 如果car时null, 则得到的Optional就是一个空对象
optPerson = Optional.ofNullable(car);
```