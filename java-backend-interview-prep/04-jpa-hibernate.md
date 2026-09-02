# 04 · JPA, Hibernate and the N+1 Problem 🔴🔴
**Time needed: 75 minutes**

**This file contains your best story.** Both your performance achievements — 15s → 6s
and 2–3s → under 1s — came from fixing N+1 queries. When the interviewer asks about
Hibernate, you are not reciting theory, you are describing something you did. Make
sure you can explain the mechanism precisely enough to prove that.

---

## First, the context: what is JPA and what is Hibernate?

Your database stores **rows in tables**. Your Java code works with **objects**. Someone
has to translate between them. Doing it by hand means endless JDBC boilerplate:
open a connection, build SQL, loop the ResultSet, map each column to a field, close
everything.

**ORM (Object-Relational Mapping)** automates that translation.

- **JPA** is the *specification* — a set of interfaces and annotations. It is a standard,
  not an implementation.
- **Hibernate** is the most common *implementation* of that specification.
- **Spring Data JPA** is a layer above both that generates repository implementations
  from method names, so you rarely write queries at all.

> "JPA is the specification, Hibernate is the implementation, and Spring Data JPA is
> the abstraction on top that generates the repository code. Coding against JPA
> interfaces means I could switch the provider without rewriting my entities."

---

## Q1. Entity mapping basics
```java
@Entity
@Table(name = "transactions")
public class Transaction {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 20)
    private String accountNumber;

    private BigDecimal amount;

    @Enumerated(EnumType.STRING)      // store "PENDING", not 0 - ordinals break on reorder
    private TxnStatus status;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "customer_id")
    private Customer customer;
}
```
⚠️ `@Enumerated(EnumType.STRING)` is worth mentioning. The default is `ORDINAL`, which
stores the enum's position as a number — so inserting a new value in the middle of the
enum silently corrupts every existing row. In banking data that is a serious bug.

## Q2. 🔴 Lazy vs eager loading

- **EAGER** — the related entity is loaded immediately, with the parent.
- **LAZY** — a proxy is put in place, and the real data is only fetched when you first
  access it.

**The defaults, which they may ask you to recite:**

| Relationship | Default |
|---|---|
| `@OneToOne` | EAGER |
| `@ManyToOne` | EAGER |
| `@OneToMany` | LAZY |
| `@ManyToMany` | LAZY |

**Say this:**
> "I set `@ManyToOne` to LAZY explicitly, because the default is EAGER and that means
> every time I load a transaction I also load its customer, even when I only wanted the
> amount. On a list of a thousand transactions that is a thousand unnecessary joins or
> queries."

**Real-time example.** `Transaction` has a `@ManyToOne` to `Customer` and to `Account`.
The recall list screen shows only reference number, amount and status — no customer data
at all. With the EAGER default, every single row still dragged its customer and account
across, which is a large part of why that page was slow. Setting them LAZY meant the list
query loaded only what the screen actually displays.

**The catch with LAZY:** if you access a lazy field after the persistence context is
closed, you get `LazyInitializationException`. The correct fixes are to fetch what you
need in the query (a join fetch), or map to a DTO inside the transaction. The wrong fix
is `spring.jpa.open-in-view=true`, which keeps the session open for the whole request
and hides the problem while making it worse.

## Q3. 🔴🔴 The N+1 problem — your story

**This is the most important answer in this file. Be able to explain it in 60 seconds.**

### What it is
```java
List<Transaction> txns = txnRepository.findAll();       // 1 query - gets 100 transactions

for (Transaction t : txns) {
    System.out.println(t.getCustomer().getName());      // 1 query EACH - 100 more
}
```
One query to get the list, then N more queries — one per row — to load each row's
relation. Hence **N+1**. With 100 transactions that is **101 database round trips**
instead of one or two.

### Why it is so slow
Each round trip has network latency. Even at 5ms each, 100 extra queries is half a
second of pure waiting, and it grows linearly with the data. This is why a report that
was fine in testing crawls in production — the row count went up.

### How to find it
> "Turn on `spring.jpa.show-sql` or set the Hibernate SQL logger to DEBUG, then load
> the page and count the queries. If you see the same query repeating with a different
> ID, that is N+1. I also looked at execution plans to confirm which queries were
> actually costly."

### How to fix it — know all four

**1. JOIN FETCH — the usual fix.**
```java
@Query("SELECT t FROM Transaction t JOIN FETCH t.customer WHERE t.status = :status")
List<Transaction> findByStatusWithCustomer(@Param("status") TxnStatus status);
```
One query, everything loaded.

**2. `@EntityGraph` — the declarative version.**
```java
@EntityGraph(attributePaths = {"customer", "account"})
List<Transaction> findByStatus(TxnStatus status);
```

**3. Batch fetching** — turns N queries into N/batch queries.
```yaml
spring.jpa.properties.hibernate.default_batch_fetch_size: 25
```

**4. A DTO projection** — the best option for a read-only report.
```java
@Query("SELECT new com.bank.dto.TxnReportDto(t.id, t.amount, c.name) " +
       "FROM Transaction t JOIN t.customer c WHERE t.status = :status")
List<TxnReportDto> findReportData(@Param("status") TxnStatus status);
```
This selects only the columns you need, avoids loading full entities into the
persistence context, and skips dirty-checking entirely.

⚠️ **The trap with JOIN FETCH:** fetching **two** collections in one query produces a
cartesian product. Fetch one collection at a time, or use batch fetching for the second.
Mentioning this unprompted marks you out.

### 🔴 Your version of the answer
> "On the recall reports, generation was taking about 15 seconds. I turned on SQL
> logging and saw the same query repeating once per row — a classic N+1, because the
> report walked each transaction's related entities. I replaced it with a projection
> query that joined and selected only the columns the report needed, added indexes on
> the columns in the WHERE and JOIN clauses, and rewrote a couple of inefficient JOINs.
> That took it from 15 seconds to 6. On the Business Card APIs the same pattern was
> costing 2 to 3 seconds per call, and fixing the N+1 plus setting the right
> associations to lazy brought it under a second."

Practise that until it is fluent. It answers "tell me about performance tuning",
"tell me about Hibernate", and "tell me about a difficult problem" all at once.

## Q4. 🔴 `@Transactional`

```java
@Transactional
public void recallTransaction(Long id) {
    Transaction txn = repo.findById(id).orElseThrow();
    txn.setStatus(RECALLED);                 // no save() needed - dirty checking
    auditService.record(txn);
    // commit on normal return, rollback on a RuntimeException
}
```

**The three things they ask:**

**1. What does it actually do?** Spring creates a **proxy** around the bean. The proxy
opens a transaction before the method, commits after it returns, and rolls back on
failure.

**2. When does it roll back?** By default on **unchecked** exceptions
(`RuntimeException` and `Error`) only. A checked exception **commits** unless you say
`@Transactional(rollbackFor = Exception.class)`. This surprises people and is a
favourite question.

**3. 🔴 Why does `@Transactional` not work when you call the method from inside the
same class?**
> "Because it works through a proxy. An external caller goes through the proxy, so the
> transaction starts. But an internal call — `this.otherMethod()` — bypasses the proxy
> entirely and calls the real method directly, so no transaction is started. The fix is
> to move that method into a separate bean, so the call goes through the proxy again."

That is a senior-level answer and interviewers remember it.

**Propagation, briefly:** `REQUIRED` is the default — join the existing transaction or
start one. `REQUIRES_NEW` suspends the current one and starts an independent one, which
is what you want for audit logging that must persist even if the main work rolls back.

**Real-time example — the clearest use of `REQUIRES_NEW`.** A recall attempt fails
validation halfway through and the main transaction rolls back, which is correct: no
partial state is written. But the **audit record of the attempt must survive**, because
compliance needs to know someone tried. If the audit insert joins the main transaction it
is rolled back with everything else. `REQUIRES_NEW` on the audit method gives it its own
transaction that commits independently.

In a banking system that is not a nicety — an audit trail that disappears when something
fails is worse than no audit trail, because you believe it.

**Isolation levels**, in one line each:
- `READ_UNCOMMITTED` — can see uncommitted data (dirty reads). Rarely used.
- `READ_COMMITTED` — only committed data. The usual default in PostgreSQL and Oracle.
- `REPEATABLE_READ` — the same row reads the same within a transaction. MySQL's default.
- `SERIALIZABLE` — full isolation, slowest.

**Real-time example — why isolation matters here.** Two approvers open the same card
request and click Approve at the same moment. Both transactions read the status as
PENDING, both see it as approvable, and both write APPROVED — so the request is approved
twice and two approval records exist. That is a **lost update**.

The fixes are optimistic locking with an `@Version` column, so the second write fails and
can be retried, or a `SELECT ... FOR UPDATE` pessimistic lock. Optimistic is usually the
right choice, because genuine collisions are rare and it does not hold database locks.

## Q5. Hibernate caching
- **First-level cache** — the persistence context. **Always on**, scoped to one
  transaction. Loading the same entity twice in one transaction hits the database once.
- **Second-level cache** — optional, shared across transactions, needs a provider like
  Ehcache or Hazelcast. Good for reference data that rarely changes, such as a list of
  branch codes. Not for data that changes often.
- **Query cache** — caches query results. Must be used with the second-level cache and
  is easy to get wrong.

**Real-time example.** Branch codes, currency codes and transaction-status descriptions
are read on nearly every request and change perhaps twice a year. That is textbook
second-level cache material. Transactions themselves are **never** cached that way — the
data changes constantly and stale financial data is worse than a slow query.

## Q6. Spring Data JPA repositories
```java
public interface TxnRepository extends JpaRepository<Transaction, Long> {

    // Spring generates the query FROM THE METHOD NAME
    List<Transaction> findByStatusAndAmountGreaterThan(TxnStatus status, BigDecimal amt);

    Optional<Transaction> findByReferenceNumber(String ref);

    // your own JPQL when the name would get silly
    @Query("SELECT t FROM Transaction t WHERE t.createdAt BETWEEN :from AND :to")
    List<Transaction> findInRange(@Param("from") LocalDate from, @Param("to") LocalDate to);

    // native SQL when you need database-specific features
    @Query(value = "SELECT * FROM transactions WHERE MATCH(notes) AGAINST(:q)", nativeQuery = true)
    List<Transaction> search(@Param("q") String q);
}
```
Hierarchy: `Repository` → `CrudRepository` → `PagingAndSortingRepository` →
`JpaRepository`. Each adds methods; `JpaRepository` adds JPA-specific ones like
`flush()` and `saveAll()`.

**Pagination**, which you should mention for any list endpoint:
```java
Page<Transaction> page = repo.findByStatus(PENDING, PageRequest.of(0, 20, Sort.by("createdAt").descending()));
```

## Q7. `save()` vs `saveAndFlush()`, and entity states
Three states: **transient** (a new object, not known to Hibernate), **persistent**
(managed by the persistence context — changes are tracked automatically), **detached**
(was persistent, but the context has closed).

**Dirty checking** is the thing to mention: for a managed entity you do not need to call
`save()`. At flush time Hibernate compares the entity with its loaded snapshot and
issues an UPDATE only for the fields that changed.

`saveAndFlush()` pushes the SQL to the database immediately instead of waiting for the
transaction to commit. Useful when you need a generated ID within the same transaction.

## Q8. `getOne`/`getReferenceById` vs `findById`
`findById` hits the database and returns `Optional`. `getReferenceById` returns a
**lazy proxy** without querying — useful when you only need to set a foreign key
relationship and never read the object's fields. Touching a field on a proxy for a row
that does not exist throws `EntityNotFoundException`.

---

## ✅ Check yourself before moving on
1. Explain the N+1 problem, how you detect it, and **four** ways to fix it.
2. Tell your 15s → 6s story in under 60 seconds, with the mechanism.
3. Explain why `@Transactional` does nothing on an internal method call.
4. State the default rollback behaviour and how to change it.
5. Give the fetch-type defaults for all four relationship annotations.
