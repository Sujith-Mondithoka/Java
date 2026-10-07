# 02 · Round 1 — Backend Track 🔴
### *Skim this even if you go frontend — Round 1 includes core Java either way, and Round 2 will cover your Spring Boot work.*

The JD asks for: **Core Java** · **Spring, Spring Boot, Hibernate/JPA** · **REST APIs and
microservices** · **SQL, preferably Oracle** · **JUnit and a mocking framework such as
Mockito** · **comfortable in Linux**.

**Two of those are your thin areas — Oracle and Linux.** They are at the end of this file
with honest answers. Everything before that you can speak to from real work.

---

## Spring Boot

**IoC and DI in one line** → *"Inversion of Control means the framework creates and wires the
objects instead of my class doing `new`. Dependency injection is the mechanism. The benefit
is my class depends on an interface, so I can swap the implementation and inject mocks in
tests."*

**🔴 Constructor injection, and why** → fields can be `final`, dependencies cannot be missing,
and you can test with `new Service(mock)` with no Spring context at all. A constructor with
eight parameters also makes bad design visible, which field injection hides.

**Annotations:** `@SpringBootApplication` (= `@Configuration` + `@EnableAutoConfiguration` +
`@ComponentScan`) · `@RestController` (= `@Controller` + `@ResponseBody`) · `@Service` ·
`@Repository` (**also translates DB exceptions** into Spring's hierarchy) · `@Autowired` ·
`@Qualifier` · `@Value` · `@Transactional` · `@RestControllerAdvice`.

**REST mapping:** `@GetMapping`/`@PostMapping`/`@PutMapping`/`@DeleteMapping`,
`@PathVariable` (from the URL), `@RequestParam` (query string), `@RequestBody` (JSON body),
`@Valid` (triggers Bean Validation before your method runs).

**🔴 Bean scopes** → **singleton is the default**, one instance for the whole context. So
**keep beans stateless** — a mutable instance field is a concurrency bug, and on a banking
platform an audit failure, because two requests overwrite each other's value. Request data
belongs in parameters, not fields.

**Memory — why singleton is the default:** one `@Service` object sits in the heap for the
whole application's life, however many requests arrive. A thousand concurrent requests share
that one object; what is *not* shared is each request's **stack**, which holds its own local
variables. That is exactly why locals are safe and instance fields are not.

```java
@Service
public class ApplicationService {
    private String currentUser;          // ❌ ONE field, shared by every request

    public void approve(String user) {   // ✅ a parameter lives in THIS request's stack frame
        ...
    }
}
```
Two requests running `approve` at the same moment each get their own stack frame, so the
parameter is private to each. The field is one piece of heap memory they both write to — and
the second one wins.

**Global exception handling** — worth volunteering:
```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(ApplicationNotFoundException.class)
    public ResponseEntity<ErrorResponse> notFound(ApplicationNotFoundException ex) {
        return ResponseEntity.status(404).body(new ErrorResponse("NOT_FOUND", ex.getMessage()));
    }
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> all(Exception ex) {
        log.error("Unexpected", ex);                       // log the detail...
        return ResponseEntity.status(500)
            .body(new ErrorResponse("INTERNAL_ERROR", "Something went wrong"));  // ...leak nothing
    }
}
```
*"One consistent error shape for the frontend, and a stack trace never reaches the client —
it tells an attacker your framework versions and internal structure."*

**Spring MVC / DispatcherServlet** → front controller: every request hits the
`DispatcherServlet`, handler mapping picks the controller method, a handler adapter invokes it
and binds arguments, a message converter (Jackson) turns the return value into JSON.
*Practical value: a 404 is handler mapping, bad JSON is the converter, a binding failure is
the adapter.*

**Auto-configuration** → `@ConditionalOnClass` and `@ConditionalOnMissingBean`. Boot
configures a DataSource if a driver is on the classpath and you have not defined one — and
the moment you define your own bean, yours wins.

---

## JPA and Hibernate

**JPA** is the specification, **Hibernate** the implementation, **Spring Data JPA** the layer
that generates repositories from method names.

**Fetch defaults** — asked often: `@ManyToOne` and `@OneToOne` are **EAGER**; `@OneToMany` and
`@ManyToMany` are **LAZY**. *"I set `@ManyToOne` to LAZY explicitly, because otherwise loading
a list of applications drags every related entity across even when the screen shows three
columns."*

### 🔴 N+1 — the classic question
> "One query loads the list, then each row's relation loads with its own query — 100 rows
> becomes 101 round trips. I find it by turning on SQL logging and counting queries; the same
> query repeating with a different id is the signature. Fixes: a **JOIN FETCH**, an
> **`@EntityGraph`**, **batch fetching**, or a **DTO projection** for a read-only screen,
> which selects only the columns needed and skips loading entities entirely."

**N+1 costs memory as well as time**, which few candidates mention: each of those 101 queries
returns entities that go into the persistence context with their snapshots. So you are not
only paying 101 network round trips, you are filling the heap with objects the screen may only
need three fields from.

**`@Transactional`** → Spring wraps the bean in a **proxy** that opens a transaction before
the method and commits after. Two things to know:
- It rolls back on **unchecked** exceptions only, unless you set `rollbackFor`.
- 🔴 **An internal `this.method()` call bypasses the proxy, so no transaction starts.** The
  same is true of your AOP aspect — a strong point to make, because you built one.

**Dirty checking** → a managed entity needs no `save()`; Hibernate compares it with the loaded
snapshot at flush time and updates only changed columns.

**Memory — the persistence context is a cache in your heap.** For dirty checking to work,
Hibernate keeps **two copies** of every entity you load inside the transaction: the entity
itself and a snapshot of how it looked when loaded. That is the *first-level cache*, and it is
always on.

**Two consequences worth saying out loud:**
- Loading 100,000 rows in one transaction puts 200,000 objects in the heap, and that is a very
  common cause of `OutOfMemoryError` in batch jobs. The fixes are paging, or clearing the
  persistence context periodically.
- A **DTO projection** avoids all of it — it selects only the columns you need and never puts
  managed entities in the context, so there is no snapshot and no dirty checking. That is why
  it is the right choice for a read-only screen or report.

**Details you can claim from your own work:** `@Enumerated(EnumType.STRING)` not the ordinal
default · `BigDecimal` for money, never `double` · **Liquibase** for versioned schema
migrations, so a schema change is reviewable and repeatable across SIT, UAT and production.

---

## REST and microservices

**REST design** → nouns not verbs (`/applications/{id}/approve` as a sub-resource), correct
status codes (201 + Location on create, 204 on delete, 400 vs 401 vs 403 vs 404, 409 for a
conflict), **pagination on every list endpoint**, URL versioning, **DTOs at the boundary not
entities** — returning entities leaks your schema and causes lazy-loading surprises during
serialisation.

**🔴 Microservices — answer honestly about depth**
> "On the Service Online platform I built Spring Boot services and REST APIs consumed by
> other parts of the platform and by the React frontend, and the platform used Kafka and
> RabbitMQ between components. What I have not done is own the decomposition — deciding
> service boundaries, standing up discovery and a gateway.
>
> The way I think about it: microservices buy independent deployment, scaling and fault
> isolation, and you pay with network failure, no distributed transaction and harder
> debugging. For a small system a well-structured monolith is usually the better call."

**Saying the cost unprompted is what scores.** Most candidates recite only the benefits.

**Resilience, if pushed:** always a timeout; a **circuit breaker** (closed → open → half-open)
so a slow dependency does not exhaust your threads; retry **only idempotent** operations.

---

## JUnit and Mockito — named in the JD

```java
@ExtendWith(MockitoExtension.class)
class ApplicationServiceTest {
    @Mock ApplicationRepository repository;
    @Mock NotificationSender notifier;
    @InjectMocks ApplicationService service;

    @Test
    void notifiesOnApproval() {
        when(repository.findById(1L)).thenReturn(Optional.of(new Application(1L, PENDING)));

        service.approve(1L, "authoriser-7");

        ArgumentCaptor<Application> saved = ArgumentCaptor.forClass(Application.class);
        verify(repository).save(saved.capture());
        assertEquals(APPROVED, saved.getValue().getStatus());
        verify(notifier).send(eq("authoriser-7"), any(Message.class));
    }
}
```

- `@Mock` creates the double · `@InjectMocks` builds the class under test with mocks injected
  · `@Spy` wraps a real object · `@MockBean` is the Spring-context version.
- `when().thenReturn()` stubs · `verify()` asserts an interaction happened ·
  `ArgumentCaptor` asserts on **what** was passed.
- **Void methods:** you cannot assert a return, so `verify(...)`. To make one throw you need
  `doThrow(ex).when(mock).method()` — `when(mock.voidMethod())` will not compile.
- **Coverage** tells you what *ran*, not what was *verified* — a test with no assertion still
  counts.

🔴 **Be honest if asked how much Mockito you have used.** Your resume lists JUnit, Jest and
React Testing Library. *"I have written JUnit tests for REST APIs and workflow logic validated
through SIT and UAT, and Jest and RTL on the frontend. My Mockito usage has been lighter than
my JUnit usage, so I would not overstate it — but I understand the model."* Then show the
example above.

---

## 🔴 SQL — and the Oracle question

Your databases are **PostgreSQL and MySQL**; the JD says *"preferably Oracle"*. That is a
preference, not a requirement, and **SQL skill transfers almost entirely.** Say so plainly:

> "My production work has been PostgreSQL, with MySQL before that. I have not used Oracle
> specifically, but the SQL is largely the same — joins, indexing, execution plans and query
> tuning all transfer. The differences I would expect are dialect-level: sequences rather
> than auto-increment, `ROWNUM` or `FETCH FIRST` instead of `LIMIT`, `NVL` instead of
> `COALESCE`, and `SELECT ... FROM DUAL` for a scalar. I would be productive quickly."

**That answer is much better than pretending.** Knowing the four specific differences proves
you actually understand what varies, which is the real question.

**Core SQL to have ready:**
- **Joins** — INNER (matches only), LEFT (all from the left, nulls on the right). *"Rows with
  no match"* = `LEFT JOIN ... WHERE right.id IS NULL`. ⚠️ A condition on the right table in
  the `WHERE` of a LEFT JOIN silently makes it an INNER JOIN — it belongs in the `ON`.
- **`WHERE` vs `HAVING`** — rows before grouping vs groups after aggregation.
- **Indexing** — a B-tree mapping values to rows; turns a full scan into O(log n). **Always
  say the cost**: every insert and update maintains every index, so you add them deliberately.
  **Left-most prefix rule** — an index on `(status, created_at)` does not serve `created_at`
  alone. Index killers: a **function on the column**, a **leading `%`** in LIKE.
- **EXPLAIN** — `type: ALL` means full scan; check which index was used and the row estimate.
- **ACID** — the transfer example: debit and credit must be atomic or money disappears.

---

## 🔴 Linux — the JD asks for "working comfortably in Linux"

Be honest about level, then show the working set. Most of this you have done via Docker, Git
and deployments.

```bash
ls -la · cd · pwd · cp · mv · rm -rf · mkdir -p · find . -name "*.log"
cat · less · head -50 · tail -f app.log          # tail -f is THE one for live logs
grep -i "error" app.log · grep -rn "ClassName" . · grep -c "Exception" app.log
ps -ef | grep java · kill -9 <pid> · top · df -h · free -m
chmod 755 run.sh · chown · export VAR=value
scp file user@host:/path · ssh user@host
java -jar app.jar · tail -f nohup.out
```

**The answer that sounds like real use, not a cheat sheet:**
> "Comfortable at the level a developer needs — navigating, finding things and reading logs.
> The commands I actually live in are `tail -f` on an application log while reproducing an
> issue, `grep` to find an exception or a string across a codebase, `ps -ef | grep java` to
> check what is running, and `df -h` when something fails for no obvious reason and the disk
> turns out to be full. I would not call myself a systems administrator."

**One pipeline worth knowing** — it looks good and is genuinely useful:
```bash
grep "ERROR" app.log | awk '{print $5}' | sort | uniq -c | sort -rn | head
# the most frequent error types, most common first
```

---

## ✅ Before you walk in
1. HashMap internals, and the N+1 answer with four fixes.
2. Why `@Transactional` does nothing on an internal call — and that your AOP aspect has the
   same proxy caveat.
3. The microservices answer: your level, then the **costs**.
4. The Oracle answer, with the four dialect differences.
5. The Linux answer, with `tail -f`, `grep`, `ps -ef`.
