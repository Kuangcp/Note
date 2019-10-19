---
title: SpringShell.md
date: 2019-10-19 17:04:25
tags: 
categories: 
---

**目录 start**
 
1. [Spring Shell](#spring-shell)

**目录 end**|_2019-10-19 17:04_|
****************************************
# Spring Shell

-   添加依赖

```
<dependency>
    <groupId>org.springframework.shell</groupId>
    <artifactId>spring-shell-starter</artifactId>
    <version>2.0.0.RELEASE</version>
</dependency>
```

-   自定义命令

    ```java
    @ShellComponent
    public class MyShell {
    
        @ShellMethod("求和函数")
        public int add(@ShellOption(help = "第一个数", defaultValue = "0") int n1,
                       @ShellOption(help = "第二个数", defaultValue = "5") int n2) {
            return n1 + n2;
        }
    
    }
    ```

    -   说明：
        
        -   `@ShellComponent`注解：该注解表示该类作为命令集进行扫描
        
        -   `@ShellMethod`注解：该注解表示该方法为一个命令，当设置该注解的`key`属性时，则该命令为设置的key值。`key`可以有多个值，则表示命令可以有多个别名。如果`key`没有被设置，则默认为方法名
        
        -   `@ShellOption`注解：表示命令参数
        
        -   可以通过`help`命令查看所有命令解释,也可通过`help 命令名`来查看具体的命令
        
    -   运行: `add 1 2`
    
-   自定义参数键

    ```
    @ShellMethod(value = "求和函数", key = "sum", prefix = "-")
    public int sum(@ShellOption(help = "第一个数", defaultValue = "0") int a,
                   @ShellOption(help = "第二个数", defaultValue = "5", value = "-two") int b) {
        return a + b;
    }
    ```
    
    -   说明:
    
        -   `@ShellMethod`注解的`prefix`，可以设置命令默认的参数前缀，如该处设置为`-`(默认为`--`), 则命令`sum -a 1`可以设置第一个参数a的值
        
        -   `@ShellOption`注解的`value`，可以设置参数的键，如该处可使用命令`sum -two 3`将命令第二个参数b设置为3
        
-   将参数映射到集合或数组

    ```
    @ShellMethod(value = "求和函数")
    public int sum1(@ShellOption(arity = 4) int[] arrs) {
        int sum = 0;
        for (int n : arrs) {
            sum += n;
        }
        return sum;
    }
    ```
    
    -   说明:
    
        -   设置`@ShellOption`注解的`arity`，可以将多个参数用一个数组接收，此处表示该命令接收4个参数，并将它们依次放入数组,运行如下,`sum1 1 2 3 4`

-   参数为布尔型

    ```
    @ShellMethod("布尔型")
    public String bool(@ShellOption boolean yes) {
        return "yes is " + yes;
    }
    ```
    
    -   说明
    
        -   当参数为布尔型时,可使用类似与如下的方式将参数`yes`设置为`true`: `bool --yes`,如果不调用`--yes`来指定参数`yes`则该参数`yes`的值为`false`
        
-   校验参数

    ```
    @ShellMethod("str")
    public String echo(@Size(min = 3) String str) {
        return "str is " + str;
    }
    ```
    
    -   说明:
    
        -   使用校验注解，可检验输入的参数，如该处会检验输入的str的长度是否大于等于3
        
-   禁用和修改内置命令

    -   要禁用所有内置命令时，可以通过排除相关依赖
    
        ```
        <dependency>
            <groupId>org.springframework.shell</groupId>
            <artifactId>spring-shell-starter</artifactId>
            <version>2.0.0.RELEASE</version>
            <exclusions>
                <exclusion>
                    <groupId>org.springframework.shell</groupId>
                    <artifactId>spring-shell-standard-commands</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
        ``` 
        
    -   如果只是需要禁用部分内置命令，可以在启动类中将指定的命令禁用(不排除相关依赖，此处禁用`clear`方法)
    
        ```java
        @SpringBootApplication
        public class SpringShellStudyApplication {
        
            public static void main(String[] args) {
                String[] disabledCommands = {"--spring.shell.command.clear.enabled=false"};
                String[] fullArgs = StringUtils.concatenateStringArrays(args, disabledCommands);disabledCommands
                SpringApplication.run(SpringShellStudyApplication.class, fullArgs);
            }
        
        }
        ```
        
    -   重写并覆盖内置命令
    
        ```java
        @ShellComponent
        public class MyClearCommand implements Clear.Command {
        
            @ShellMethod("my clear")
            public void clear() {
                System.out.println("clear...");
            }
        }
        ```
        
        -   说明:
        
            -   需覆盖的命令不能被禁用
            
            -   新建一个类使用`@ShellComponent`标注，并实现你需要覆盖的命令的接口，然后重写和内置命令一样名称的命令
            
-   自定义参数转换器

    -   示例
    
        ```java
        /**
        *   数据模型
        */
        @Getter
        @Setter
        @ToString
        @AllArgsConstructor
        public class Model {
            private String name;
            private String host;
        }

        /**
        *   命令
        */
        @ShellComponent
        public class MyShell {
    
            @ShellMethod("Converter")
            public String converter(Model model) {
                return model.toString();
            }
        }

        /**
        *   转换器
        */
        @Component
        public class ModelConverter implements Converter<String, Model> {
        
        
            /**
             * 假设接收一个字符串，各属性间以@分开
             * @param s
             * @return
             */
            @Override
            public Model convert(String s) {
                String[] arrays = s.split("@");
                return new Model(arrays[0], arrays[1]);
            }
        }
        ```
        
        -   说明:
        
            -   编写命令时，参数使用实体类接收
            
            -   转换器需实现接口`org.springframework.core.convert.converter.Converter`，并交由Spring管理
