# Shiro学习

-   Shiro依赖

```
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-core</artifactId>
    <version>1.2.2</version>
</dependency>
```


-   初体验(认证及授权)

```kotlin
class ShiroTest {

    val simpleAccountRealm = SimpleAccountRealm()

    @Before
    fun addUser() {
        simpleAccountRealm.addAccount("huang", "123", "admin", "user")
    }

    /**
     * Shiro初体验.
     */
    @Test
    fun testShiro() {

        // 构建SecurityManager
        val manager = DefaultSecurityManager()
        manager.setRealm(simpleAccountRealm)

        // 提交请求认证
        SecurityUtils.setSecurityManager(manager)
        val subject = SecurityUtils.getSubject()

        // 模拟用户token
        val token = UsernamePasswordToken("huang", "123")

        // 登录
        subject.login(token)
        println(subject.isAuthenticated)

        // 检查用户是否具有角色
        subject.checkRoles("admin", "user")

        // 退出
        subject.logout()
        println(subject.isAuthenticated)
    }

}
```

-   从ini文件中回去定义的用户账号信息

```kotlin
    fun firstTest() {
        // 也可使用IniRealm加载ini文件信息
        //val realm = IniRealm("classpath:shiro.ini")
    
        // 加载ini文件信息，并创建SecurityManager
        val factory = IniSecurityManagerFactory("classpath:shiro.ini")
        val manager = factory.instance
        SecurityUtils.setSecurityManager(manager)

        val subject = SecurityUtils.getSubject()

        val token = UsernamePasswordToken("lonestarr", "vespa")
        subject.login(token)

        println(subject.isAuthenticated)

        println(subject.hasRole("schwartz"))
    }
```

-   从数据库中获取权限信息(数据库表信息可由JdbcRealm类中的查询语句了解结构,也可使用自定义的表结构，但需自定义查询语句，但查询结果字段要一致)

```kotlin
    fun testJdbc() {
        // 数据源设置
        dataSource.url = "jbdc:mysql://localhost:3306/shiro"
        dataSource.username = "root"
        dataSource.password = "123"

        // 创建JdbcRealm
        val jdbcRealm = JdbcRealm()
        // 设置数据源
        jdbcRealm.setDataSource(dataSource)

        // 构建SecurityManager
        val manager = DefaultSecurityManager()
        manager.setRealm(jdbcRealm)
        // 提交请求认证
        SecurityUtils.setSecurityManager(manager)
        val subject = SecurityUtils.getSubject()
        // 模拟用户token
        val token = UsernamePasswordToken("huang", "123")
        // 登录
        subject.login(token)
        
        // 我们的数据库表可与系统的不一致，则需要自定义查询语句如
        // val authenticatQuery = "select password from users where username = ?"
        // jdbcRealm.setAuthenticationQuery(authenticatQuery)
        
        println(subject.isAuthenticated)
        // 检查用户是否具有角色
        subject.checkRoles("admin", "user")
        // 退出
        subject.logout()
        println(subject.isAuthenticated)
    }
```

-   [自定义Realm](./src/test/kotlin/hht/dragon/shiro/MyRealm.kt)

-   加密

    -   校验时

    ```kotlin
    // 加密
    val matchaer = HashedCredentialsMatcher()
    // 使用md5加密
    matchaer.hashAlgorithmName = "md5"
    // 设置加密次数
    matchaer.hashIterations = 1
    myRealm.credentialsMatcher = matchaer
    ```

    -   使用盐时在自定义Realm中设置盐
    
    ```kotlin
    // 设置盐
    simpleAuthenticationInfo.credentialsSalt = ByteSource.Util.bytes("huang")
    ```

## SpringBoot 整合 Shiro

-   依赖

```
<!-- 需使用web依赖，不能使用webFlux -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>

<!--Shiro-->
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-core</artifactId>
    <version>1.4.0</version>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-spring</artifactId>
    <version>1.4.0</version>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-web</artifactId>
    <version>1.4.0</version>
</dependency>
```

### 使用Java配置

> `SecurityManager`需使用`WebSecurityManager`,实现类为`DefaultWebSecurityManager`

```kotlin
@Configuration
@Order(1)
class ShiroConfig {

    /**
     * Shiro过滤器.
     */
    @Bean
    fun shiroFilter(securityManager: SecurityManager) : ShiroFilterFactoryBean {
        println("ShiroFilter")
        val factoryBean = ShiroFilterFactoryBean()

        // 设置SecurityManager
        factoryBean.securityManager = securityManager

        // 设置登录界面请求，不设置则默认访问根目录下的"/login.jsp"
        factoryBean.loginUrl = "/static/login.html"
        // 设置登录成功后的跳转链接
        factoryBean.successUrl = "/index"
        // 设置未授权界面
        factoryBean.unauthorizedUrl = "/403"

        // 拦截器
        val filterChainDefinitionMap = LinkedHashMap<String, String>()

        // 配置不会被拦截的链接,按顺序判断
        // anon ：  请求可匿名访问
        filterChainDefinitionMap["/static/**"] = "anon"
        filterChainDefinitionMap["/login"] = "anon"

        // 配置退出过滤器,其中的具体的退出代码Shiro已经替我们实现了
        filterChainDefinitionMap["/logout"] = "logout"

        filterChainDefinitionMap["/user"] = "user"

        // 拦截器会按配置从上往下检查，所以"/**"请求放在最后
        // authc : 所有url都必须认证通过才可以访问
        filterChainDefinitionMap["/**"] = "authc, roles[admin]"

        factoryBean.filterChainDefinitionMap = filterChainDefinitionMap
        println("Shiro拦截器配置完毕" )

        return factoryBean
    }

    /**
     * 配置SecurityManager.
     */
    @Bean
    fun securityManager() : SecurityManager {
        val manager = DefaultWebSecurityManager()
        manager.setRealm(getRealm())
        SecurityUtils.setSecurityManager(manager)
        return manager
    }

    /**
     * 配置自定义Realm.
     */
    @Bean
    fun getRealm() : MyRealm {
        val realm = MyRealm()
        realm.credentialsMatcher = hashedCredentialsMatcher()
        return realm
    }

    /**
     * 配置加密.
     */
    @Bean
    fun hashedCredentialsMatcher() : HashedCredentialsMatcher {
        val matcher = HashedCredentialsMatcher()
        matcher.hashAlgorithmName = "md5"
        matcher.hashIterations = 1
        return matcher
    }
}
```

-   用户登录

```kotlin
    @GetMapping("/login")
    fun login(userName: String, password: String) : Mono<String> {
        val subject = SecurityUtils.getSubject()

        val token = UsernamePasswordToken(userName, password)
        return try {
            subject.login(token)
            Mono.just("登录成功")
        } catch (e : Exception) {
            e.printStackTrace()
            Mono.just("登录失败")
        }
    }
```

### 使用注解

-   需使用AOP，则需要添加AOP依赖

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-aop</artifactId>
</dependency>
```

-   配置相关配置

```kotlin
    @Bean
    fun lifecycleBeanPostProcessor(): LifecycleBeanPostProcessor {
        return LifecycleBeanPostProcessor()
    }

    @Bean
    fun authorizationAttributeSourceAdvisor(securityManager: SecurityManager): AuthorizationAttributeSourceAdvisor {
        val authorizationAttributeSourceAdvisor = AuthorizationAttributeSourceAdvisor()
        authorizationAttributeSourceAdvisor.securityManager = securityManager
        return authorizationAttributeSourceAdvisor
    }
```

-   使用

> 在Controller层的方法中使用注解,如

```kotlin
    @RequiresRoles("admin")
    @GetMapping("/test")
    fun test() : Mono<String> {
        return Mono.just("测试注解")
    }
```

-   Session管理

    -   [自定义SessionDao](./src/main/kotlin/hht/dragon/shiro/session/SessionDao.kt)
    
    > 可自定义Session的保存，获取等方式，即可用于Session共享
    
    -   [自定义SessionManager](./src/main/kotlin/hht/dragon/shiro/session/MyWebSessionManager.kt)
    
    -   配置
    
    ```kotlin
        /**
         * 配置SessionManager.
         */
        @Bean
        fun sessionManager() : SessionManager {
            val manager = MyWebSessionManager()
            manager.sessionDAO = sessionDao()
            return manager
        }
    
        @Bean
        fun sessionDao() : SessionDao {
            return SessionDao()
        }

        /**
         * 配置SecurityManager.
         */
        @Bean
        fun securityManager() : SecurityManager {
            var manager = DefaultWebSecurityManager()
            manager.setRealm(getRealm())
            // 在SecurityManager中设置sessionManager
            manager.sessionManager = sessionManager()
            SecurityUtils.setSecurityManager(manager)
            return manager
        }
    ```
