# 02 · Java 8 and Functional Programming 🔴
**Time needed: 60 minutes**

Your resume says "Java 8+", so this **will** be tested. Interviewers usually ask you to
explain streams and then write one on the spot.

---

## First, the context: what problem did Java 8 solve?

Before Java 8, processing a collection meant writing *how* to loop:

```java
// imperative - you describe every step
List<String> names = new ArrayList<>();
for (Txn t : txns) {
    if (t.getAmount() > 1000) {
        names.add(t.getCustomerName().toUpperCase());
    }
}
Collections.sort(names);
```

Java 8 let you describe *what* you want instead:

```java
// declarative - the intent is visible in one read
List<String> names = txns.stream()
        .filter(t -> t.getAmount() > 1000)
        .map(t -> t.getCustomerName().toUpperCase())
        .sorted()
        .collect(Collectors.toList());
```

Same result, but the second reads as a sentence: filter, map, sort, collect. That is
the point — less boilerplate and clearer intent.

---

## Q1. What is a lambda? 🔴
A short way to write an implementation of an interface that has exactly one method.

```java
// before Java 8
Runnable r = new Runnable() {
    public void run() { System.out.println("running"); }
};

// with a lambda
Runnable r = () -> System.out.println("running");
```

The compiler knows `Runnable` has one method, so you only supply the body.

## Q2. What is a functional interface? 🔴
An interface with **exactly one abstract method**. That is what makes it a valid target
for a lambda. `@FunctionalInterface` is optional but makes the compiler enforce it.

**The four you must know:**

| Interface | Method | Takes | Returns | Used by |
|---|---|---|---|---|
| `Predicate<T>` | `test(T)` | T | boolean | `filter` |
| `Function<T,R>` | `apply(T)` | T | R | `map` |
| `Consumer<T>` | `accept(T)` | T | void | `forEach` |
| `Supplier<T>` | `get()` | nothing | T | `orElseGet`, lazy values |

```java
Predicate<Txn> isLarge  = t -> t.getAmount() > 1000;
Function<Txn, String> name = t -> t.getCustomerName();
Consumer<Txn> log       = t -> System.out.println(t);
Supplier<Txn> empty     = () -> new Txn();
```

Also worth naming: `BiFunction<T,U,R>` (two arguments), `UnaryOperator<T>` (T to T),
and `BinaryOperator<T>` (two Ts to one T, used by `reduce`).

## Q3. Method references
Shorthand for a lambda that just calls one method.

```java
.map(t -> t.getCustomerName())   →   .map(Txn::getCustomerName)
.forEach(x -> System.out.println(x))  →  .forEach(System.out::println)
```

## Q4. 🔴🔴 Streams — intermediate vs terminal operations

**This distinction is asked constantly.**

**Intermediate** operations return another Stream and are **lazy** — they do nothing
until a terminal operation runs. `filter`, `map`, `flatMap`, `sorted`, `distinct`,
`limit`, `skip`, `peek`.

**Terminal** operations produce a result and **trigger** the whole pipeline.
`collect`, `forEach`, `reduce`, `count`, `min`, `max`, `anyMatch`, `allMatch`,
`findFirst`.

```java
txns.stream().filter(t -> t.getAmount() > 1000);   // NOTHING happens - no terminal op
```

**Why laziness matters — the answer that impresses:**
> "Because intermediate operations are lazy, the stream can fuse them into a single
> pass and stop early. `stream().filter(...).findFirst()` does not filter the whole
> list and then take the first — it stops at the first match. With `limit(10)` on a
> million records, only enough elements are processed to produce ten."

**A stream can only be consumed once.** Reusing one throws
`IllegalStateException: stream has already been operated upon or closed`.

## Q5. The stream methods you must be able to write 🔴

```java
// filter + map + collect
List<String> big = txns.stream()
        .filter(t -> t.getAmount() > 1000)
        .map(Txn::getCustomerName)
        .collect(Collectors.toList());

// sum with reduce, and the shorter specialised form
double total = txns.stream().mapToDouble(Txn::getAmount).sum();
double same  = txns.stream().map(Txn::getAmount).reduce(0.0, Double::sum);

// GROUP BY - very commonly asked
Map<String, List<Txn>> byStatus =
        txns.stream().collect(Collectors.groupingBy(Txn::getStatus));

// group and count
Map<String, Long> countByStatus =
        txns.stream().collect(Collectors.groupingBy(Txn::getStatus, Collectors.counting()));

// group and sum
Map<String, Double> totalByStatus = txns.stream()
        .collect(Collectors.groupingBy(Txn::getStatus,
                 Collectors.summingDouble(Txn::getAmount)));

// sort by a field, descending
txns.stream().sorted(Comparator.comparing(Txn::getAmount).reversed())

// flatMap - flatten nested collections into one stream
List<Item> all = orders.stream()
        .flatMap(o -> o.getItems().stream())
        .collect(Collectors.toList());
```

🔴 **`map` vs `flatMap`** is a guaranteed question:
> "`map` transforms one element into one element. `flatMap` transforms one element
> into a **stream** of elements and then flattens them all into a single stream. If
> each order has a list of items, `map` gives me a stream of lists, and `flatMap`
> gives me a stream of items."

## Q6. Optional 🔴
Introduced to make "this might be absent" explicit in the type, instead of returning
`null` and hoping the caller checks.

```java
Optional<Txn> found = repository.findById(id);

// good
String name = found.map(Txn::getCustomerName).orElse("Unknown");
found.ifPresent(t -> log.info("Found {}", t.getId()));
Txn txn = found.orElseThrow(() -> new TransactionNotFoundException(id));

// bad - this is just a null check with extra steps
if (found.isPresent()) { Txn t = found.get(); }
```

> "Optional makes the possibility of absence part of the method signature, so the
> caller cannot ignore it by accident. I use `map`, `orElse` and `orElseThrow` rather
> than `isPresent` and `get`, because that defeats the purpose. Spring Data returns
> `Optional` from `findById` for exactly this reason."

**`orElse` vs `orElseGet`** — a good detail: `orElse(buildDefault())` evaluates the
argument **always**, even when a value is present. `orElseGet(() -> buildDefault())`
only runs it when needed. It matters when the default is expensive.

## Q7. Parallel streams — and when not to use them
```java
list.parallelStream().filter(...).collect(...);
```
> "It splits the work across the fork-join pool. It only helps with a large dataset and
> a genuinely CPU-bound operation with no shared mutable state. For small collections
> the coordination overhead makes it slower, and for I/O-bound work like database calls
> it is the wrong tool. I would measure before using it, not assume."

## Q8. Other Java 8 features worth naming
- **Default and static methods in interfaces** — let you add a method to an interface
  without breaking every existing implementation.
- **`java.time`** — `LocalDate`, `LocalDateTime`, `Duration`. Immutable and thread
  safe, unlike the old `Date` and `Calendar`.
- **`CompletableFuture`** — asynchronous composition, useful for calling several
  services in parallel.

## Q9. Later versions, in one line each
If asked "what have you used beyond Java 8":
- **Java 11** — `var` for local variables, `String.isBlank()`, `strip()`, `lines()`.
- **Java 17 (LTS)** — records, sealed classes, switch expressions, text blocks.
- A **record** is a compact immutable data carrier: `record TxnDto(String id, double amount) {}`
  generates the constructor, getters, `equals`, `hashCode` and `toString`. Very useful
  for DTOs.

---

## ✅ Check yourself before moving on
1. Write a stream that groups transactions by status and sums the amount in each group.
   From memory.
2. Explain intermediate vs terminal, and why laziness lets a stream stop early.
3. Explain `map` vs `flatMap` in two sentences.
4. Name the four core functional interfaces and which stream method uses each.
