# 01 · Round 1 — Core Java 🔴🔴
**Both tracks start here.** The JD asks for *"Core Java (OOP, collections, exception
handling)"* for backend, and *"working knowledge of Java"* for frontend.

**Every topic in this file also explains where the memory goes**, in plain English with a
small example. Memory questions come up a lot in Java interviews, and more importantly,
knowing where things live is what makes the rest of the answers make sense.

---

# Part 0 · How Java uses memory 🔴🔴
*Read this first. Everything after it refers back here.*

## The two places things are kept

Java keeps your data in two main places: the **stack** and the **heap**.

```
   STACK  (one per thread)              HEAP  (one, shared by all threads)
   ┌──────────────────────┐            ┌──────────────────────────────┐
   │ main()               │            │                              │
   │   int count = 5      │            │   the actual objects live    │
   │   String name ───────┼───────────►│   here                       │
   │   List items ────────┼───────────►│                              │
   └──────────────────────┘            └──────────────────────────────┘
     small, fast, automatic               big, shared, cleaned by GC
```

**The stack** holds one box per running method, called a *frame*. Inside the frame are the
method's local variables. When the method finishes, the whole frame is thrown away
instantly. Each thread gets its own stack, so stack data is never shared.

**The heap** holds every **object** you create with `new`. There is only one heap and all
threads share it. Nothing is removed by hand — the **garbage collector** removes objects
that nothing points at any more.

## The one rule that explains almost everything

> **Primitives hold the value. Objects hold a reference — an address pointing into the heap.**

```java
int count = 5;                  // the value 5 is IN the stack frame
String name = new String("Sujith");  // the OBJECT is in the heap,
                                     // the stack only holds its address
```

So when you write `int a = 5; int b = a;` you copied the value — two independent 5s. When you
write `List a = ...; List b = a;` you copied the *address* — both names point at **one**
list, and changing it through either name changes the same object.

### The example that makes it click
```java
void change(int number, StringBuilder text) {
    number = 99;              // changes only this method's copy
    text.append(" world");    // changes the OBJECT both names point at
}

int n = 5;
StringBuilder s = new StringBuilder("hello");
change(n, s);

System.out.println(n);   // 5           - unchanged, we copied the value
System.out.println(s);   // hello world - changed, we copied the address
```

**Java is always pass-by-value.** For objects, the *value being copied is the address*. That
is why the first one did not change and the second one did. This is a classic interview
question and this example answers it.

## The other memory areas, briefly

- **Metaspace** — holds the *class* information: method code, field names, and so on. Loaded
  once per class, not per object. (Before Java 8 this was called PermGen.)
- **String pool** — a special area of the heap where text literals are kept and reused. More
  on this below.
- **Static fields** — one copy shared by the whole program, living with the class rather
  than with any object.

## Two errors, and what each one means

| Error | What ran out | Usual cause |
|---|---|---|
| **StackOverflowError** | The stack | Recursion with no base case — frames pile up forever |
| **OutOfMemoryError** | The heap | Too many live objects — usually something unbounded, like loading a whole table into a list instead of paginating |

🔴 **Say this if asked about memory generally:**
> "The stack holds method frames and local variables, one stack per thread, and it is cleaned
> up automatically when a method returns. The heap holds all the objects and is shared across
> threads, and the garbage collector removes objects nothing references any more. A primitive
> variable holds its value directly; an object variable holds a reference into the heap."

## Garbage collection in one minute
> "The garbage collector removes objects that are no longer **reachable** — nothing in the
> program points at them any more. Setting a variable to `null` or letting it go out of scope
> makes the object eligible; it does not delete it immediately. The heap is split into a
> young area, where new objects go and most die quickly, and an old area for objects that
> survive. Cleaning the young area is quick and frequent; cleaning the old area is slower."

**A memory leak in Java** is not an unfreed pointer — it is **keeping a reference you no
longer need**, usually in a long-lived collection or a static field, so the GC is not allowed
to collect it.

---

# Part 1 · OOP

## The four pillars, with memory

| Pillar | Plain meaning | Your example |
|---|---|---|
| **Encapsulation** | Keep fields private; let people change them only through methods that check the change is allowed | A card application's status goes through a method that verifies the transition is legal |
| **Inheritance** | A class reuses another class's code with `extends` | A base entity holding id and timestamps |
| **Polymorphism** | The same call runs different code depending on the real object | A `Notifier` interface with email and SMS versions; Spring injects the right one |
| **Abstraction** | Show *what* it does, hide *how* | The controller depends on a service interface, not the implementation |

**Memory — what an object actually costs:**
```java
Application app = new Application();
```
`new` allocates space in the **heap** for all the object's fields, plus a small header the JVM
uses for its own bookkeeping. The variable `app` sits in the **stack** and holds the address.
A subclass object holds its own fields **and** all the fields it inherited, in one block —
inheritance does not create two objects.

**Memory — where methods live:** method *code* is stored once per class in **Metaspace**, not
copied into every object. A million objects of one class means a million sets of fields in the
heap, but only **one** copy of the code.

**Overloading vs overriding** — same name with different parameters, decided at compile time ·
same signature in a subclass, decided at runtime by the real object.
**You cannot override a static method.** It is *hidden*, and which one runs depends on the
reference type, because static methods belong to the class, not to any object.

**Abstract class vs interface** — abstract class when there is genuinely shared **state and
code** (one only); interface for a **contract** (as many as you like).
**Memory note:** an interface adds no fields, so implementing ten interfaces costs no extra
object memory. Extending a class *does* add its fields to every instance.

**Why no multiple inheritance of classes?** The diamond problem — if two parents override the
same method, the compiler cannot pick one. Interfaces are allowed because when two `default`
methods clash, the compiler forces you to override and choose.

---

# Part 2 · Collections 🔴🔴

```
Collection
├── List   in order, duplicates allowed  → ArrayList, LinkedList
├── Set    no duplicates                 → HashSet, LinkedHashSet, TreeSet
└── Queue  first in, first out           → ArrayDeque, PriorityQueue

Map (NOT a Collection) key → value       → HashMap, LinkedHashMap, TreeMap
```

| | Get by index | Search | Order kept | Thread safe |
|---|---|---|---|---|
| ArrayList | **O(1)** | O(n) | insertion | no |
| LinkedList | O(n) | O(n) | insertion | no |
| HashMap | — | **O(1)** average | **none** | **no** |
| LinkedHashMap | — | O(1) | insertion | no |
| TreeMap | — | O(log n) | **sorted** | no |
| ConcurrentHashMap | — | O(1) | none | **yes, per bucket** |

## 🔴 ArrayList vs LinkedList — the memory answer is the whole answer

```
ArrayList    one array, items side by side in memory
             [ ref ][ ref ][ ref ][ ref ][ empty ][ empty ]

LinkedList   separate node objects, scattered, joined by pointers
             [prev|val|next] ←→ [prev|val|next] ←→ [prev|val|next]
```

**Memory:** an `ArrayList` is **one array object** in the heap holding references, so it is
compact. A `LinkedList` creates a **separate node object for every element**, and each node
stores the value plus a *previous* and a *next* pointer — roughly three times the overhead per
item, scattered across the heap.

**Why that matters for speed:** because an ArrayList's slots sit next to each other, the CPU
loads neighbouring items into its cache together, so walking it is fast. LinkedList nodes are
in different places, so every step is a fresh memory lookup.

> "I use ArrayList by default — O(1) access by index, and the elements sit together in memory
> which is cache friendly. LinkedList only wins when I am repeatedly inserting or removing in
> the middle at a position I already hold, and it costs about three times the memory per
> element because every item is a separate node with two pointers."

**How ArrayList grows:** it starts with room for 10. When full it creates a **new, bigger
array** (about 1.5×), copies everything across, and the old array becomes garbage. So a list
that grows to a million items has allocated and thrown away several large arrays along the
way — which is why `new ArrayList<>(expectedSize)` matters when you know the size.

## 🔴🔴 HashMap internals — including where the memory goes

**What `put` does, step by step:**
> "`put` calls `hashCode()` on the key, then HashMap mixes the bits with `h ^ (h >>> 16)` and
> picks the bucket with `(n - 1) & hash` — a fast bitwise AND instead of a division, which
> works because the capacity is always a power of two.
>
> If the bucket is empty it stores the entry there. If not, that is a **collision**, so it
> walks the entries comparing keys with `equals()` — a matching key replaces the value,
> otherwise the new entry is added to that bucket. Since Java 8, once one bucket holds more
> than **8** entries it converts from a linked list to a **red-black tree**, so the worst case
> drops from O(n) to O(log n).
>
> Default capacity **16**, load factor **0.75**, so at **12** entries it doubles the table and
> rehashes everything into the new buckets."

**Memory — what a HashMap actually holds:**
```
table (one array in the heap)
 [0] → null
 [1] → Node{hash, key, value, next} → Node{...}      ← a collision chain
 [2] → null
 [3] → Node{hash, key, value, next}
```
Three things cost memory: **one array** for the table, **one `Node` object per entry** (each
holding the hash, a key reference, a value reference and a next pointer), and empty slots —
with a 0.75 load factor, roughly a quarter of the table is deliberately empty to keep
collisions rare.

**Resizing is expensive in memory too:** doubling means allocating a new array **twice the
size** while the old one still exists, then rehashing every entry. For a moment both arrays
are in the heap.

### 🔴 equals and hashCode — and why keys should be immutable
> "**Equal objects must have equal hash codes.** If I override `equals` but not `hashCode`,
> two objects that are equal can produce different hashes, land in different buckets, and the
> map never finds what I stored.
>
> It is also why keys should be immutable. The bucket was chosen from the hash **at insert
> time**. If a field used in the hash changes afterwards, the entry is stranded in a bucket
> that no longer matches — the object is still in memory, but unreachable through the map."

### Quick answers
- **HashMap vs Hashtable** → Hashtable locks the whole map and is legacy. Use
  **ConcurrentHashMap**, which locks per bucket so threads writing to different buckets do not
  block each other.
- **HashSet vs TreeSet** → O(1) unordered vs O(log n) sorted. **Memory:** a `HashSet` is
  literally a `HashMap` where every value is the same shared dummy object — so it costs about
  the same as a map.
- **fail-fast** → `ConcurrentModificationException`, detected with a `modCount` counter.
  Remove with `iterator.remove()` or `removeIf`, never `list.remove()` inside a for-each.
- **Comparable vs Comparator** → natural order inside the class (one) vs order defined outside
  it (as many as you want).

---

# Part 3 · Strings and memory 🔴🔴
*This is where memory questions are asked most often.*

## Why String is immutable
Once made, a String's characters can never change. `s.concat("x")` returns a **new** String
and leaves the original alone.

**The four reasons:**
1. **The string pool** needs it (below) — sharing is only safe if nobody can change it.
2. **Security** — Strings hold URLs, file paths and credentials. If they could change, a value
   could be checked and then altered before use.
3. **Thread safety** — something that cannot change is safe to share with no locking.
4. **The hash is cached** — which makes String a fast map key, and that cache is only valid
   because the value is fixed.

## 🔴🔴 The string pool — the question they love

```java
String a = "hello";                 // goes in the POOL
String b = "hello";                 // reuses the SAME pooled object
String c = new String("hello");     // forces a NEW object outside the pool

a == b          // true   - same object
a == c          // false  - different objects
a.equals(c)     // true   - same characters
c.intern() == a // true   - intern() returns the pooled one
```

```
          HEAP
   ┌────────────────────────────────┐
   │  String Pool                   │
   │    "hello"  ◄── a, b           │   one object, two names
   │                                │
   │  "hello"    ◄── c              │   a second, separate object
   └────────────────────────────────┘
```

> "Text written as a literal goes into the string pool, and identical literals share one
> object — so `==` happens to be true. `new String(...)` deliberately creates a separate
> object in the heap, so `==` is false even though the characters match. That is why I always
> compare strings with `.equals()` — `==` works by accident until it does not."

## 🔴 String vs StringBuilder — a memory question disguised as a speed question

```java
// BAD - inside a loop
String result = "";
for (String part : parts) {
    result = result + part;      // creates a NEW String object every time
}

// GOOD
StringBuilder sb = new StringBuilder();
for (String part : parts) {
    sb.append(part);             // changes ONE buffer
}
String result = sb.toString();
```

> "Because String is immutable, `+` in a loop cannot change the existing object — it builds a
> new one each time and throws the old one away. A thousand iterations creates a thousand
> throwaway objects for the garbage collector, and it is O(n²) because it copies everything
> each round. StringBuilder keeps one internal character array and appends into it, so it is
> O(n) and allocates far less."

`StringBuffer` is the same as StringBuilder but synchronised — older, slower, rarely needed.

## 🔴 The Integer cache — a favourite trick question
```java
Integer a = 127, b = 127;
Integer c = 128, d = 128;

a == b        // true   - Java keeps a cache of Integer objects from -128 to 127
c == d        // false  - outside the cache, so two separate objects
c.equals(d)   // true
```
> "Java pre-creates Integer objects for −128 to 127 and reuses them, so `==` is true in that
> range. Above it, autoboxing creates a new object each time, so `==` compares two different
> addresses. Always `.equals()` for boxed types."

**Memory point worth adding:** `int` is a primitive held in the stack; `Integer` is an object
in the heap with a reference pointing at it. So `List<Integer>` of a million numbers is a
million small heap objects, not a compact block of ints — which is why `int[]` is far lighter
than `List<Integer>`.

---

# Part 4 · Exception handling

```
Throwable
├── Error                 JVM-level trouble — do not catch (OutOfMemoryError)
└── Exception
    ├── RuntimeException  UNCHECKED — NullPointerException, IllegalArgumentException
    └── everything else   CHECKED   — IOException, SQLException
```

- **Checked** = the compiler makes you catch it or declare `throws`. **Unchecked** = usually a
  bug in the code.
- **`finally` always runs**, except if the JVM exits. **Never `return` from `finally`** — it
  swallows the real return value and any exception.
- **try-with-resources** closes anything `AutoCloseable` automatically, even when an exception
  is thrown.
- **`throw`** raises one now; **`throws`** declares that a method might.

**Memory:** an exception is an object in the heap like any other, and creating one captures
the **stack trace** — a snapshot of every frame on the stack at that moment. That is why
exceptions are not free, and why using them for ordinary control flow in a loop is slow.

🔴 **Connect it to Spring:**
> "I use unchecked custom exceptions with a shared `BusinessException` parent, handled
> centrally by `@RestControllerAdvice` so the API returns one error shape. Unchecked matters
> for `@Transactional` too, because by default Spring only rolls back on unchecked
> exceptions."

---

# Part 5 · Java 8 — streams and lambdas

```java
Map<Status, Long> byStatus = apps.stream()
        .filter(a -> a.getAmount() > 1000)
        .collect(Collectors.groupingBy(Application::getStatus, Collectors.counting()));
```

- **Intermediate operations are lazy** (`filter`, `map`, `sorted`); **terminal operations
  trigger the work** (`collect`, `forEach`, `reduce`, `findFirst`). A stream is used once.
- **`map` vs `flatMap`** — one-to-one vs one-to-many then flattened into a single stream.
- **The four interfaces:** `Predicate`→filter, `Function`→map, `Consumer`→forEach,
  `Supplier`→a value made only when needed. One abstract method each.
- **Optional** — use `map`, `orElse`, `orElseThrow`; not `isPresent` + `get`.

**Memory — why laziness matters:**
> "Because the intermediate steps are lazy, the stream does not build an intermediate list at
> each stage. `filter` then `map` passes each element through both steps one at a time, so
> only one element is in flight. If each stage built its own list, a million-row stream with
> three stages would allocate three million-element lists."

⚠️ `sorted()` is the exception — it **must** hold everything in memory to sort it. And
`collect(toList())` builds the final list, which is the point.

**Memory — lambdas:** a lambda that uses no outside variables can be reused by the JVM rather
than created fresh each time. A lambda that **captures** a variable has to hold onto it, which
is why captured local variables must be effectively final — the lambda keeps a copy, and
letting it change would be ambiguous.

---

# Part 6 · The likely coding question

Expect **one** easy problem: reverse a string, palindrome, first non-repeating character, word
frequency, find duplicates, second largest.

```java
// first non-repeating character
Map<Character, Integer> counts = new LinkedHashMap<>();   // LinkedHashMap keeps order
for (char c : s.toCharArray()) counts.merge(c, 1, Integer::sum);
for (var e : counts.entrySet()) if (e.getValue() == 1) return e.getKey();
return null;
```
**Memory to mention:** `O(k)` extra space, where k is the number of distinct characters — the
map holds one entry per distinct character, not per character in the string.

```java
// second largest - no sorting, no extra memory
int first = Integer.MIN_VALUE, second = Integer.MIN_VALUE;
for (int n : nums) {
    if (n > first) { second = first; first = n; }
    else if (n > second && n != first) second = n;
}
```
**Memory to mention:** `O(1)` extra space — two numbers, whatever the array size. Sorting would
be O(n log n) time and may copy the array.

### The four free marks almost everyone drops
1. **Ask the edge cases first** — null, empty, duplicates, upper/lower case.
2. **Say the brute force and its cost**, then improve it. *"Two nested loops is O(n²) — a
   HashMap makes the lookup O(1), so one pass."*
3. **Talk while you write.** Silence looks like being stuck.
4. **State time AND space at the end**, before they ask. Most candidates give only time.

---

## ✅ Before you walk in
1. Stack vs heap, and the `change(int, StringBuilder)` example that proves pass-by-value.
2. HashMap `put` end to end, plus what it holds in memory — table array, one Node per entry.
3. The string pool, with the four lines of `a == b` / `a == c`.
4. Why `+` in a loop is slow — new object each time, O(n²), garbage.
5. The Integer cache, −128 to 127.
