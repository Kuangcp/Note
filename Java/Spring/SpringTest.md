---
title: SpringTest
date: 2018-12-21 10:53:35
tags: 
    - Spring
categories: 
    - Java
---

💠

- 1. [Spring Test](#spring-test)
    - 1.1. [注解](#注解)
        - 1.1.1. [Spring Boot测试注解](#spring-boot测试注解)
        - 1.1.2. [Mock和Spy注解](#mock和spy注解)
        - 1.1.3. [配置注解](#配置注解)
        - 1.1.4. [事务和上下文注解](#事务和上下文注解)
        - 1.1.5. [MockMvc相关](#mockmvc相关)
        - 1.1.6. [数据库测试注解](#数据库测试注解)
        - 1.1.7. [最佳实践](#最佳实践)

💠 2026-01-16 16:14:52
****************************************
# Spring Test

> [参考: Getting Started with Mockito @Mock, @Spy, @Captor and @InjectMocks](https://www.baeldung.com/mockito-annotations?utm_source=tuicool&utm_medium=referral) 
> [参考: Mockito – Using Spies](https://www.baeldung.com/mockito-spy)

## 注解

### Spring Boot测试注解

**1. @SpringBootTest**
- **用途**：启动完整的Spring应用上下文进行集成测试
- **特点**：加载所有Bean，模拟完整应用环境
- **使用场景**：集成测试、端到端测试

```java
@SpringBootTest
@RunWith(SpringRunner.class)  // JUnit 4
// 或 @ExtendWith(SpringExtension.class)  // JUnit 5
class ApplicationTest {
    @Autowired
    private UserService userService;
    
    @Test
    void testService() {
        // 测试代码
    }
}
```

**2. @WebMvcTest**
- **用途**：只加载Web层（Controller），不加载Service、Repository
- **特点**：轻量级，只测试Controller层
- **配合**：通常配合`@AutoConfigureMockMvc`使用

```java
@WebMvcTest(UserController.class)
@AutoConfigureMockMvc
class UserControllerTest {
    @Autowired
    private MockMvc mockMvc;
    
    @MockBean
    private UserService userService;
    
    @Test
    void testController() throws Exception {
        mockMvc.perform(get("/users/1"))
            .andExpect(status().isOk());
    }
}
```

**3. @DataJpaTest**
- **用途**：只加载JPA相关组件，使用内存数据库（H2）
- **特点**：自动配置内存数据库，事务自动回滚
- **使用场景**：Repository层测试

```java
@DataJpaTest
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
class UserRepositoryTest {
    @Autowired
    private UserRepository userRepository;
    
    @Test
    void testSave() {
        User user = new User("test");
        userRepository.save(user);
        assertThat(userRepository.findById(user.getId())).isPresent();
    }
}
```

**4. @JsonTest**
- **用途**：测试JSON序列化/反序列化
- **特点**：只加载JSON相关组件

```java
@JsonTest
class UserJsonTest {
    @Autowired
    private JacksonTester<User> json;
    
    @Test
    void testSerialize() throws Exception {
        User user = new User("test");
        assertThat(json.write(user)).isEqualToJson("user.json");
    }
}
```

**5. @RestClientTest**
- **用途**：测试REST客户端（RestTemplate、WebClient）
- **特点**：只加载REST客户端相关组件

```java
@RestClientTest(UserClient.class)
class UserClientTest {
    @Autowired
    private UserClient userClient;
    
    @MockRestServiceServer
    private MockRestServiceServer server;
    
    @Test
    void testClient() {
        server.expect(requestTo("/users/1"))
            .andRespond(withSuccess("{}", MediaType.APPLICATION_JSON));
        // 测试代码
    }
}
```

### Mock和Spy注解

**6. @MockBean**
- **用途**：在Spring容器中用Mock对象替换真实Bean
- **特点**：会注册到Spring容器中，可以被@Autowired注入
- **使用场景**：需要Mock Spring管理的Bean

```java
@SpringBootTest
class UserServiceTest {
    @MockBean
    private UserRepository userRepository;  // Mock的Bean
    
    @Autowired
    private UserService userService;  // 真实Bean，但依赖Mock的Repository
    
    @Test
    void testService() {
        when(userRepository.findById(1L))
            .thenReturn(Optional.of(new User("test")));
        // 测试代码
    }
}
```

**7. @SpyBean**
- **用途**：在Spring容器中用Spy对象包装真实Bean
- **特点**：部分Mock，未Mock的方法调用真实实现
- **使用场景**：需要部分Mock Spring管理的Bean

```java
@SpringBootTest
class UserServiceTest {
    @SpyBean
    private UserRepository userRepository;  // Spy的Bean
    
    @Test
    void testService() {
        // 真实方法会被调用
        doReturn(Optional.empty())
            .when(userRepository).findById(1L);  // 只Mock特定方法
        // 测试代码
    }
}
```

**@MockBean vs @Mock：**
- `@MockBean`：Spring管理的Bean，注册到容器中
- `@Mock`：普通Mock对象，需要手动注入（Mockito）

### 配置注解

**8. @TestPropertySource**
- **用途**：覆盖测试环境的配置属性
- **特点**：优先级高于application.properties

```java
@SpringBootTest
@TestPropertySource(properties = {
    "app.name=test-app",
    "app.version=1.0.0"
})
class ConfigTest {
    @Value("${app.name}")
    private String appName;
    
    @Test
    void testConfig() {
        assertThat(appName).isEqualTo("test-app");
    }
}
```

**9. @ActiveProfiles**
- **用途**：激活指定的Profile配置
- **特点**：加载对应profile的配置文件

```java
@SpringBootTest
@ActiveProfiles("test")
class ProfileTest {
    // 会加载application-test.properties
}
```

**10. @TestConfiguration**
- **用途**：定义测试专用的配置类
- **特点**：不会影响主应用的配置

```java
@SpringBootTest
class TestConfigExample {
    @TestConfiguration
    static class TestConfig {
        @Bean
        @Primary
        public UserService testUserService() {
            return new TestUserService();
        }
    }
}
```

### 事务和上下文注解

**11. @Transactional**
- **用途**：测试方法执行后自动回滚
- **特点**：默认回滚，保持数据库干净

```java
@SpringBootTest
@Transactional  // 测试后自动回滚
class TransactionalTest {
    @Test
    void testSave() {
        // 数据库操作会被回滚
    }
    
    @Test
    @Rollback(false)  // 不回滚
    void testSaveWithoutRollback() {
        // 数据库操作会提交
    }
}
```

**12. @DirtiesContext**
- **用途**：标记测试会污染Spring上下文
- **特点**：测试后重新加载上下文

```java
@SpringBootTest
class DirtiesContextTest {
    @Test
    @DirtiesContext  // 方法级别
    void testMethod() {
        // 测试后重新加载上下文
    }
}

@DirtiesContext(classMode = DirtiesContext.ClassMode.AFTER_CLASS)
class DirtiesContextClassTest {
    // 类级别：所有测试后重新加载上下文
}
```

### MockMvc相关

**13. @AutoConfigureMockMvc**
- **用途**：自动配置MockMvc，用于测试Controller
- **特点**：无需手动创建MockMvc实例

```java
@WebMvcTest(UserController.class)
@AutoConfigureMockMvc
class MockMvcTest {
    @Autowired
    private MockMvc mockMvc;
    
    @Test
    void testController() throws Exception {
        mockMvc.perform(get("/users"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$[0].name").value("test"));
    }
}
```

**14. @AutoConfigureWebTestClient**
- **用途**：自动配置WebTestClient（WebFlux）
- **特点**：用于测试响应式Web应用

```java
@WebFluxTest(UserController.class)
@AutoConfigureWebTestClient
class WebFluxTest {
    @Autowired
    private WebTestClient webTestClient;
    
    @Test
    void testController() {
        webTestClient.get()
            .uri("/users")
            .exchange()
            .expectStatus().isOk();
    }
}
```

### 数据库测试注解

**15. @Sql**
- **用途**：执行SQL脚本初始化或清理数据
- **特点**：测试前后执行SQL

```java
@SpringBootTest
class SqlTest {
    @Test
    @Sql("/test-data.sql")  // 测试前执行
    @Sql(scripts = "/cleanup.sql", executionPhase = Sql.ExecutionPhase.AFTER_TEST_METHOD)
    void testWithData() {
        // 测试代码
    }
}
```

**16. @AutoConfigureTestDatabase**
- **用途**：配置测试数据库
- **特点**：可以替换为内存数据库

```java
@DataJpaTest
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
// Replace.NONE: 使用真实数据库
// Replace.ANY: 使用内存数据库（默认）
class DatabaseTest {
    // 测试代码
}
```

### 最佳实践

**1. 选择合适的测试切片**
- `@WebMvcTest`：只测试Controller
- `@DataJpaTest`：只测试Repository
- `@SpringBootTest`：完整集成测试

**2. Mock vs Spy**
- `@MockBean`：完全Mock，适合外部依赖
- `@SpyBean`：部分Mock，适合需要真实逻辑的场景

**3. 测试隔离**
- 使用`@Transactional`保持数据库干净
- 使用`@DirtiesContext`隔离上下文污染

**4. 配置管理**
- 使用`@TestPropertySource`覆盖配置
- 使用`@ActiveProfiles`切换环境

> 参考：
> - [Spring Boot Testing](https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.testing)
> - [Spring Test Framework](https://docs.spring.io/spring-framework/docs/current/reference/html/testing.html) 

