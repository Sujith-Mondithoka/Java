# 03 · Spring Boot 🔴🔴
**Time needed: 90 minutes**

"Java → Spring Boot" is listed as the **primary skill** on the job description. Along
with Core Java, this is where most of your technical round will be spent.

---

## First, the context: what problem does Spring solve?

### The problem: tight coupling
Without Spring, an object creates the things it depends on:

```java
public class TransactionService {
    private final EmailNotifier notifier = new EmailNotifier();   // hard-wired
}
```

Two problems. To switch to SMS you must edit this class. And in a unit test you cannot
replace the notifier with a fake, so your test sends real emails.

### The solution: Inversion of Control
The object stops creating its dependencies and **receives** them instead:

```java
@Service
public class TransactionService {
    private final Notifier notifier;                    // an interface

    public TransactionService(Notifier notifier) {      // handed in from outside
        this.notifier = notifier;
    }
}
```

Now the class depends on an interface, not a concrete class. Something else decides
which implementation to supply. That "something else" is the Spring container.

**Inversion of Control (IoC)** is the principle: control of creating objects is
inverted, moving from your class to the framework.
**Dependency Injection (DI)** is how Spring implements it: it constructs objects and
passes their dependencies in.

**Say it in one line:**
> "IoC is the principle that the framework, not my class, controls object creation and
> wiring. Dependency injection is the mechanism. The practical benefit is that my
> classes depend on interfaces, so I can swap implementations and inject mocks in
> tests without changing the class."

### And Spring Boot on top of Spring
Plain Spring needed a lot of XML and manual configuration. Spring Boot adds:
- **Auto-configuration** — sees a database driver on the classpath and configures a
  DataSource for you.
- **Starter dependencies** — `spring-boot-starter-web` pulls in a compatible set of
  libraries so you are not resolving versions by hand.
- **Embedded server** — Tomcat is inside the JAR, so `java -jar app.jar` runs it. No
  separate application server to install.
- **Production features** — Actuator gives health checks and metrics endpoints.

> "Spring Boot is Spring with opinionated defaults. It removes the configuration work
> so you start with a running application and override only what you need."

---

## Q1. 🔴 The three types of injection, and which to use

```java
// 1. CONSTRUCTOR injection - what you should use
@Service
public class TxnService {
    private final TxnRepository repo;
    public TxnService(TxnRepository repo) { this.repo = repo; }
}

// 2. FIELD injection - convenient, but avoid
@Autowired private TxnRepository repo;

// 3. SETTER injection - for genuinely optional dependencies
@Autowired public void setRepo(TxnRepository repo) { this.repo = repo; }
```

**Why constructor injection — four reasons, give two or three:**
1. The field can be `final`, so the object is **immutable** once built.
2. Dependencies **cannot be missing** — the object cannot be constructed without them.
3. **Testable without Spring** — `new TxnService(mockRepo)` just works. With field
   injection you need reflection or a Spring context.
4. It makes bad design **visible** — a constructor with eight parameters is obviously
   doing too much. Field injection hides that.

Since Spring 4.3, if a class has one constructor you do not even need `@Autowired`.

## Q2. 🔴 The annotations you must know

| Annotation | What it does |
|---|---|
| `@SpringBootApplication` | The main class. Combines the next three. |
| `@Configuration` | This class defines beans |
| `@EnableAutoConfiguration` | Turn on Boot's auto-config |
| `@ComponentScan` | Scan this package and below for components |
| `@Component` | A generic Spring-managed bean |
| `@Service` | A `@Component` marking business logic |
| `@Repository` | A `@Component` for data access — **also translates DB exceptions** into Spring's `DataAccessException` hierarchy |
| `@Controller` | Returns view names |
| `@RestController` | `@Controller` + `@ResponseBody` — returns JSON |
| `@Autowired` | Inject a dependency |
| `@Qualifier("name")` | Choose between multiple beans of the same type |
| `@Primary` | Make one bean the default when several match |
| `@Value("${prop}")` | Inject a property from configuration |
| `@Bean` | Declare a bean from a method, usually for third-party classes |
| `@Transactional` | Wrap the method in a database transaction |
| `@ControllerAdvice` | Global exception handling across controllers |

**Trap:** *"`@Component` vs `@Service` vs `@Repository` — is there a functional
difference?"*
> "Technically `@Service` and `@Component` behave identically; the difference is
> intent, so the layer is obvious to a reader and to tooling. `@Repository` is the
> exception — it does real work, translating vendor-specific database exceptions into
> Spring's `DataAccessException` hierarchy, so my service layer is not coupled to a
> particular database's error codes."

## Q3. REST annotations
```java
@RestController
@RequestMapping("/api/transactions")
public class TxnController {

    @GetMapping("/{id}")
    public TxnDto get(@PathVariable Long id) { ... }

    @GetMapping
    public List<TxnDto> search(@RequestParam(defaultValue = "0") int page) { ... }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public TxnDto create(@Valid @RequestBody CreateTxnRequest req) { ... }

    @PutMapping("/{id}")
    public TxnDto replace(@PathVariable Long id, @RequestBody TxnDto dto) { ... }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) { ... }
}
```
`@PathVariable` reads from the URL path. `@RequestParam` reads a query parameter.
`@RequestBody` deserialises the JSON body. `@Valid` triggers Bean Validation.

## Q4. 🔴 Bean scopes

| Scope | Meaning |
|---|---|
| **singleton** | **The default.** One instance for the whole application context. |
| prototype | A new instance every time it is requested. |
| request | One per HTTP request (web only). |
| session | One per HTTP session (web only). |

🔴 **The follow-up:** *"Singleton beans are shared across all requests. Is that a
problem?"*
> "Only if the bean holds mutable state. Spring beans should be stateless — request
> data belongs in method parameters and local variables, not in instance fields. A
> singleton service with a mutable instance field is a genuine concurrency bug,
> because many threads share that one object."

That answer shows you understand *why* the default is safe, which is what they are
checking.

## Q5. 🔴 Global exception handling
Nearly always asked, because it separates people who have shipped an API from people
who have followed a tutorial.

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(TransactionNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(TransactionNotFoundException ex) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
                .body(new ErrorResponse("TXN_NOT_FOUND", ex.getMessage()));
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidation(MethodArgumentNotValidException ex) {
        String msg = ex.getBindingResult().getFieldErrors().stream()
                .map(e -> e.getField() + ": " + e.getDefaultMessage())
                .collect(Collectors.joining(", "));
        return ResponseEntity.badRequest().body(new ErrorResponse("VALIDATION_ERROR", msg));
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleAll(Exception ex) {
        log.error("Unexpected error", ex);      // log the detail...
        return ResponseEntity.status(500)
                .body(new ErrorResponse("INTERNAL_ERROR", "Something went wrong"));
                                                 // ...but do not leak it to the client
    }
}
```

**Say why it matters:**
> "It keeps error handling out of every controller, so the API returns one consistent
> error shape. The last handler matters for security: I log the stack trace but return
> a generic message, because a raw stack trace tells an attacker about your framework
> versions and internal structure. On a banking system that is a real concern."

## Q6. Bean Validation
```java
public class CreateTxnRequest {
    @NotBlank(message = "Account number is required")
    private String accountNumber;

    @NotNull @DecimalMin(value = "0.01", message = "Amount must be positive")
    private BigDecimal amount;

    @Email private String notifyEmail;
}
```
`@Valid` on the `@RequestBody` triggers it, and a failure raises
`MethodArgumentNotValidException`, handled above.

⚠️ Note `BigDecimal` for money, never `double`. Floating point cannot represent decimal
fractions exactly, so `0.1 + 0.2` is not `0.3`. In a banking interview, using
`BigDecimal` for currency is a detail that gets noticed.

## Q7. Configuration and profiles
```yaml
# application.yml
spring:
  datasource:
    url: ${DB_URL}
    username: ${DB_USER}
    password: ${DB_PASSWORD}     # from environment, never committed
---
spring:
  config.activate.on-profile: dev
  jpa.show-sql: true
```
Run with `-Dspring.profiles.active=dev`. Profiles let one build behave differently per
environment without rebuilding.

```java
@ConfigurationProperties(prefix = "app.recall")   // type-safe, grouped config
public class RecallProperties { private int maxDays; private String queueName; }
```

## Q8. Spring Boot Actuator
Adds production endpoints: `/actuator/health` (used by load balancers and Kubernetes
to decide if the instance is alive), `/actuator/metrics`, `/actuator/info`.
Say that you would **secure these**, because they expose internals.

## Q9. How does auto-configuration actually work?
A step above the basics, and a good one to know:
> "Spring Boot ships configuration classes annotated with conditions such as
> `@ConditionalOnClass` and `@ConditionalOnMissingBean`. At startup it evaluates those
> conditions against what is on the classpath and what you have already defined. So if
> H2 is on the classpath and I have not declared a DataSource, it creates one — but the
> moment I define my own bean, `@ConditionalOnMissingBean` backs off and mine wins.
> That is why defaults never fight your own configuration."

## Q10. Testing a Spring Boot application
```java
@WebMvcTest(TxnController.class)          // controller layer only, fast
class TxnControllerTest {
    @Autowired MockMvc mockMvc;
    @MockBean TxnService service;          // replaces the real bean

    @Test void returns404WhenMissing() throws Exception {
        when(service.findById(1L)).thenThrow(new TransactionNotFoundException(1L));
        mockMvc.perform(get("/api/transactions/1")).andExpect(status().isNotFound());
    }
}
```
- `@SpringBootTest` loads the whole context — integration tests, slower.
- `@WebMvcTest` / `@DataJpaTest` load one slice — much faster.
- `@MockBean` swaps a bean for a Mockito mock.

Your resume mentions unit tests for state-transition validation, so be ready to say
what you actually tested and why.

---

## ✅ Check yourself before moving on
1. Explain IoC and DI, and why constructor injection is preferred — three reasons.
2. Explain what a singleton bean means for thread safety.
3. Write a `@RestControllerAdvice` handler from memory.
4. Explain how auto-configuration decides what to configure.
