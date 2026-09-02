# 01 · Core Java and Collections 🔴🔴
**Time needed: 105 minutes**

This is where Infosys screens hardest. Service company interviews go deep on
fundamentals, because fundamentals are what transfer across the many different client
projects they will put you on. Expect rapid-fire questions here.

**If you only master one topic in this file, make it HashMap.** It is the single most
asked Java interview question in India.

---

# Part A · OOP — the four pillars

You will be asked to name them and give an example of each. Have a real example
ready, not a "Dog extends Animal" one.

## Q1. Encapsulation
**What it is:** keeping data private and exposing it only through methods.

```java
public class Account {
    private double balance;                       // nobody can touch this directly

    public void deposit(double amount) {
        if (amount <= 0) throw new IllegalArgumentException("Amount must be positive");
        this.balance += amount;                   // the rule is enforced here
    }

    public double getBalance() { return balance; }
}
```

**Why it matters:** if `balance` were public, any code anywhere could set it to a
negative number and no validation would run. Encapsulation means the object protects
its own rules. In a banking system that is not a style preference.

## Q2. Inheritance
One class reuses another's behaviour with `extends`. A `SavingsAccount extends
Account` gets `deposit()` for free and adds interest calculation.

**The follow-up:** *"Why does Java not support multiple inheritance of classes?"*
> "Because of the diamond problem. If B and C both extend A and override the same
> method, and D extends both, the compiler cannot decide which version D inherits.
> Java avoids that by allowing only one superclass. You can implement multiple
> interfaces, and since Java 8 interfaces can have default methods — so if two
> interfaces give the same default method, the compiler forces you to override it and
> resolve the conflict explicitly."

## Q3. Polymorphism 🔴
"One interface, many implementations." Two kinds, and interviewers want both.

| | **Overloading** (compile-time) | **Overriding** (runtime) |
|---|---|---|
| What changes | Same method name, **different parameters** | Same signature, **different class** |
| Decided | At compile time, by the compiler | At runtime, by the actual object |
| Also called | Static polymorphism | Dynamic polymorphism |

```java
// Overloading - same name, different parameter lists
void notify(String email) { }
void notify(String email, String sms) { }

// Overriding - the subclass replaces the parent's behaviour
class Notifier      { void send() { System.out.println("generic"); } }
class EmailNotifier extends Notifier { @Override void send() { System.out.println("email"); } }

Notifier n = new EmailNotifier();
n.send();     // "email" - decided by the OBJECT, not the reference type
```

That last line is the whole point of runtime polymorphism, and it is what makes
Spring's dependency injection work: the field is declared as an interface, and the
concrete implementation is chosen at runtime.

**Trap:** *"Can you override a static method?"* → No. Static methods belong to the
class, not the instance, so they are **hidden**, not overridden. Which one runs is
decided by the reference type, not the object.

## Q4. Abstraction
Hiding *how* something works and exposing *what* it does.

### 🔴 Abstract class vs interface — near-certain question

| | Abstract class | Interface |
|---|---|---|
| Fields | Can have normal instance fields | Only `public static final` constants |
| Constructor | Yes | No |
| Methods | Abstract and concrete | Abstract, plus `default` and `static` since Java 8 |
| Inheritance | One only | Many |
| Access modifiers | Any | Methods are public |

**When to use which — say it this way:**
> "An abstract class is for an 'is-a' relationship where the subclasses share state
> and some common implementation — a base `Transaction` class holding amount and
> timestamp. An interface is a contract about capability with no shared state, like
> `Auditable` or `PaymentProcessor`. Since I can implement many interfaces but extend
> only one class, I default to interfaces and use an abstract class when there is real
> shared code and fields."

---

# Part B · Collections 🔴🔴

## Q5. The map of the framework

```
Collection (interface)
├── List    — ordered, allows duplicates      → ArrayList, LinkedList, Vector
├── Set     — no duplicates                   → HashSet, LinkedHashSet, TreeSet
└── Queue   — FIFO processing                 → PriorityQueue, ArrayDeque

Map (separate, NOT a Collection) — key/value  → HashMap, LinkedHashMap, TreeMap, Hashtable
```

⚠️ `Map` does **not** extend `Collection`. It stores pairs, not single elements. A
small detail interviewers like to check.

## Q6. ArrayList vs LinkedList 🔴

| | ArrayList | LinkedList |
|---|---|---|
| Structure | Growable array | Doubly linked list |
| Get by index | **O(1)** | O(n) — must walk the chain |
| Add/remove at end | O(1) amortised | O(1) |
| Add/remove in middle | O(n) — shifts elements | O(1) *once you are at the node* |
| Memory | Less | More — each node stores two pointers |

**Say this:**
> "I use ArrayList by default. Random access is O(1) and the elements sit together in
> memory, which is cache friendly. LinkedList only wins when I am inserting or removing
> frequently in the middle while already holding a reference to that position. In
> practice that is rare, and even for a queue I would use ArrayDeque."

**How does ArrayList grow?** It starts at capacity 10, and when full it creates a new
array about **1.5 times** the size and copies everything across. That copy is why
`new ArrayList<>(expectedSize)` matters when you know the size up front.

## Q7. 🔴🔴 How does HashMap work internally?
**Learn this properly. It is the most asked Java question in Indian interviews.**

### Storing a value — `map.put(key, value)`
1. Java calls `key.hashCode()` to get an int.
2. HashMap applies its own **hash spreading** on top: `h ^ (h >>> 16)`. This mixes the
   high bits into the low bits, because the next step only uses the low bits.
3. It finds the bucket: `index = (n - 1) & hash`, where `n` is the array length. Since
   `n` is always a power of two, this is a fast bitwise AND instead of a modulus.
4. If the bucket is empty, it stores the entry there.
5. If the bucket already has entries — a **collision** — it walks them comparing with
   `equals()`. Same key means replace the value; otherwise append the new entry.

### The structure
Internally it is an **array of buckets**, and each bucket holds a **linked list** of
entries. Since **Java 8**, once a single bucket exceeds **8 entries** (and the table is
at least 64 long) that list is converted into a **balanced red-black tree**, turning
worst-case lookup from O(n) into O(log n). Below 6 entries it converts back.

### Resizing
Default capacity **16**, load factor **0.75**. When size passes 16 × 0.75 = **12**, the
array doubles to 32 and everything is **rehashed** into new buckets. Resizing is
expensive, which is why you presize a map you know will be large.

### Complexity
O(1) average for get and put. O(log n) worst case since Java 8, thanks to treeification.

### 🔴 The follow-up that catches people: equals and hashCode
> "If you use a custom object as a key you must override both `hashCode()` and
> `equals()`. The contract is that **equal objects must have equal hash codes**. If I
> override `equals` but not `hashCode`, two objects that are equal can produce
> different hash codes, land in different buckets, and the map will never find the
> entry I stored. That is also why HashMap keys should be **immutable** — if a field
> used in the hash changes after insertion, the entry is effectively lost, because it
> is sitting in a bucket that no longer matches its hash."

## Q8. HashMap vs Hashtable vs ConcurrentHashMap 🔴

| | HashMap | Hashtable | ConcurrentHashMap |
|---|---|---|---|
| Thread safe | No | Yes | Yes |
| How | — | Locks the **whole map** | Locks only the affected **bucket** |
| Null key/value | One null key, many null values | Neither | Neither |
| Performance | Fastest single-threaded | Slow — everything serialises | Fast under concurrency |
| Status | Standard | **Legacy, do not use** | Standard for concurrent use |

> "Hashtable synchronises every method, so all threads queue behind one lock. That is
> why it is effectively obsolete. ConcurrentHashMap locks at bucket level, so threads
> writing to different buckets do not block each other, which is why it scales."

## Q9. HashSet vs LinkedHashSet vs TreeSet

| | Ordering | Backing structure | Complexity |
|---|---|---|---|
| HashSet | None guaranteed | HashMap | O(1) |
| LinkedHashSet | **Insertion order** | HashMap + linked list | O(1) |
| TreeSet | **Sorted** | Red-black tree | O(log n) |

Useful detail: `HashSet` is literally a `HashMap` where every value is the same dummy
object. That is why its rules about `hashCode` and `equals` are identical.

## Q10. Fail-fast vs fail-safe iterators
> "Fail-fast iterators, like ArrayList's and HashMap's, throw
> `ConcurrentModificationException` if the collection is structurally modified while
> iterating. They track a `modCount` and check it on each `next()`. Fail-safe
> iterators, like ConcurrentHashMap's or CopyOnWriteArrayList's, work on a snapshot or
> allow concurrent access, so they do not throw — but they may not reflect the very
> latest changes."

**How do you remove safely while iterating?** Use `iterator.remove()`, or
`collection.removeIf(predicate)`. Never `list.remove()` inside a for-each loop.

## Q11. Comparable vs Comparator 🔴

```java
// Comparable - the class defines its OWN natural ordering. One only.
class Txn implements Comparable<Txn> {
    public int compareTo(Txn other) { return this.date.compareTo(other.date); }
}

// Comparator - ordering defined OUTSIDE the class. As many as you like.
Comparator<Txn> byAmount = Comparator.comparing(Txn::getAmount);
list.sort(byAmount.reversed());
```
> "Comparable is the natural order and lives inside the class, so there can be only
> one. Comparator lives outside, so I can have several — sort transactions by date on
> one screen and by amount on another without touching the entity."

---

# Part C · Strings, immutability and memory

## Q12. Why is String immutable? 🔴
Once created, a String's value can never change. `s.concat("x")` returns a **new**
String.

**The four reasons — give at least two:**

1. **String pool.** Java reuses identical literals to save memory. That is only safe if
   nobody can change them underneath other references.
2. **Security.** Usernames, file paths and DB URLs are Strings. If they were mutable, a
   value could be validated and then changed before use.
3. **Thread safety.** Immutable objects can be shared across threads with no locking.
4. **Hashcode caching.** String caches its hash, which makes it a fast HashMap key.
   That is only valid if the value cannot change.

## Q13. String vs StringBuilder vs StringBuffer
| | Mutable? | Thread safe | Use when |
|---|---|---|---|
| String | No | Yes (immutable) | Fixed values |
| StringBuilder | Yes | **No** | Building strings — the default |
| StringBuffer | Yes | Yes (synchronised) | Legacy; rarely needed |

> "Concatenating in a loop with `+` creates a new String every iteration, so a
> thousand-iteration loop creates a thousand throwaway objects. StringBuilder mutates
> one buffer, so it is O(n) instead of O(n²)."

## Q14. `==` vs `.equals()`
`==` compares **references** — are these the same object in memory.
`.equals()` compares **values** — as defined by the class.

```java
String a = "hello";                  // goes into the string pool
String b = "hello";                  // reuses the SAME pooled object
String c = new String("hello");      // forces a NEW object on the heap

a == b        // true  - same pooled reference
a == c        // false - different objects
a.equals(c)   // true  - same characters
```
This is a favourite quick question. Learn the three lines.

## Q15. Stack vs Heap
- **Stack** — one per thread. Holds method calls, local variables and references. Freed
  automatically when the method returns.
- **Heap** — shared by all threads. Holds all objects. Managed by the garbage collector.

`StackOverflowError` means runaway recursion. `OutOfMemoryError` means the heap is
full, usually a leak or an unbounded collection.

---

# Part D · Exceptions

## Q16. Checked vs unchecked 🔴

```
Throwable
├── Error              — JVM level, do not catch (OutOfMemoryError)
└── Exception
    ├── RuntimeException  — UNCHECKED (NullPointerException, IllegalArgumentException)
    └── everything else   — CHECKED (IOException, SQLException)
```

- **Checked**: the compiler forces you to catch it or declare `throws`. Represents
  recoverable, expected conditions — a missing file, a network failure.
- **Unchecked**: extends `RuntimeException`. Usually a programming bug. No compiler
  enforcement.

**Say this:**
> "In application code I mostly use unchecked exceptions and a custom hierarchy — a
> `TransactionNotFoundException` extending `RuntimeException` — because forcing every
> caller to catch and rethrow adds noise. I handle them centrally in Spring with
> `@ControllerAdvice` so the API returns a consistent error shape. It also matters for
> `@Transactional`, because by default Spring only rolls back on unchecked exceptions."

That last sentence connects two topics and sounds like real experience. Use it.

## Q17. try-with-resources and finally
```java
try (Connection conn = dataSource.getConnection()) {
    // conn.close() is called automatically, even if an exception is thrown
}
```
Anything implementing `AutoCloseable` works. This replaced the old
`finally { if (conn != null) conn.close(); }` pattern.

**Trap:** *"Does `finally` always run?"* → Almost always. Not if the JVM exits
(`System.exit()`) or the thread is killed. And if `finally` contains a `return`, it
overrides the one in `try` — which is why you never return from `finally`.

## Q18. `throw` vs `throws` vs `final` vs `finally` vs `finalize`
- `throw` — actually raise an exception now.
- `throws` — declare that this method may raise one.
- `final` — a constant, a non-overridable method, or a non-extendable class.
- `finally` — the block that runs whatever happens.
- `finalize()` — a deprecated, unreliable method the GC used to call. Never use it.

---

## ✅ Check yourself before moving on
1. Explain **HashMap put and get end to end** — hashing, buckets, collisions,
   treeification, resizing. Out loud, without notes.
2. Explain the `equals`/`hashCode` contract and what breaks if you ignore it.
3. Overloading vs overriding, with an example of each.
4. Abstract class vs interface, and when you would pick each.
5. Explain the three lines of the `==` vs `.equals()` String example.
