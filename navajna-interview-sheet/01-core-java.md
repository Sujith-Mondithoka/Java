# 01 · Round 1 — Core Java 🔴🔴
**Both tracks open here.** The JD names *"Core Java (OOP, collections, exception handling)"*
for backend and *"working knowledge of Java"* for frontend. This is the most compressed
version of what you need; the long explanations are in your Infosys guide if you want depth.

---

## OOP — have one real example each

| Pillar | One-line answer | Your example |
|---|---|---|
| **Encapsulation** | Private fields, access through methods that validate | A card application's status cannot be set directly — it goes through a method that checks the transition is legal |
| **Inheritance** | Reuse behaviour via `extends`; one superclass only | A base entity with id, created/updated timestamps |
| **Polymorphism** | Same call, different implementation at runtime | A `Notifier` interface with email and SMS implementations; Spring injects the right one |
| **Abstraction** | Expose *what*, hide *how* | A service interface the controller depends on, not the implementation |

**Overloading vs overriding** — compile time, different parameters · runtime, same signature
in a subclass. **You cannot override a static method** — it is *hidden*, and which one runs
depends on the reference type.

**Abstract class vs interface** — abstract class for shared **state and code**, one only;
interface for a **contract**, many. Since Java 8 interfaces can have `default` and `static`
methods. *"I default to interfaces and use an abstract class when there is genuinely shared
state."*

**Why no multiple inheritance of classes?** The diamond problem — if two parents override the
same method the compiler cannot choose. Interfaces are allowed because with conflicting
`default` methods the compiler forces you to override and resolve it explicitly.

---

## Collections — the highest-probability topic

```
Collection
├── List   ordered, duplicates OK   → ArrayList, LinkedList
├── Set    no duplicates            → HashSet, LinkedHashSet, TreeSet
└── Queue  FIFO                     → ArrayDeque, PriorityQueue

Map (NOT a Collection) key→value    → HashMap, LinkedHashMap, TreeMap
```

| | Get by index | Search | Order | Thread safe |
|---|---|---|---|---|
| ArrayList | **O(1)** | O(n) | insertion | no |
| LinkedList | O(n) | O(n) | insertion | no |
| HashMap | — | **O(1)** avg | **none** | **no** |
| LinkedHashMap | — | O(1) | insertion | no |
| TreeMap | — | O(log n) | **sorted** | no |
| ConcurrentHashMap | — | O(1) | none | **yes, per bucket** |

### 🔴🔴 HashMap internals — learn this properly, it is asked more than anything else
> "`put` calls `hashCode()` on the key, then HashMap spreads the bits with `h ^ (h >>> 16)`
> and finds the bucket with `(n - 1) & hash` — a bitwise AND rather than a modulus, which
> works because the capacity is always a power of two.
>
> If the bucket is empty it stores the entry. If not, that is a collision, so it walks the
> entries comparing with `equals()` — same key replaces the value, otherwise it appends.
> Since Java 8, once a bucket passes **8 entries** the list becomes a **red-black tree**, so
> worst case goes from O(n) to O(log n).
>
> Default capacity **16**, load factor **0.75**, so at **12** entries it doubles and rehashes."

### 🔴 The equals/hashCode contract
> "**Equal objects must have equal hash codes.** If I override `equals` but not `hashCode`,
> two equal objects can hash to different buckets, so the map never finds what I stored. It
> is also why map keys should be immutable — if a field used in the hash changes after
> insertion, the entry is stranded in a bucket that no longer matches."

### Quick answers
- **ArrayList vs LinkedList** → ArrayList by default: O(1) index access and contiguous memory.
  LinkedList only wins for frequent middle insertion at a known position.
- **ArrayList growth** → starts at 10, grows ~1.5× and copies. Presize when you know the size.
- **HashMap vs Hashtable** → Hashtable locks the whole map and is legacy; use
  ConcurrentHashMap, which locks per bucket.
- **HashSet vs TreeSet** → O(1) unordered vs O(log n) sorted. `HashSet` is a `HashMap` with a
  dummy value.
- **fail-fast** → `ConcurrentModificationException` via `modCount`. Remove with
  `iterator.remove()` or `removeIf`, never `list.remove()` inside a for-each.
- **Comparable vs Comparator** → natural order inside the class (one) vs ordering outside it
  (many).

---

## Exception handling

```
Throwable
├── Error                 JVM level — do not catch
└── Exception
    ├── RuntimeException  UNCHECKED — NullPointerException, IllegalArgumentException
    └── others            CHECKED   — IOException, SQLException
```

- **Checked** = compiler forces catch or `throws`. **Unchecked** = programming errors.
- **`finally` always runs**, except `System.exit()` or the JVM dying. **Never `return` from
  `finally`** — it swallows the real return and any exception.
- **try-with-resources** closes anything `AutoCloseable` automatically, even on exception.
- **`throw` vs `throws`** — raise one now vs declare it may happen.
- 🔴 **Connect it to Spring:** *"I use unchecked custom exceptions with a common
  `BusinessException` parent, handled centrally by `@RestControllerAdvice` so the API returns
  one error shape. Unchecked also matters because `@Transactional` only rolls back on
  unchecked exceptions by default."*

---

## Strings and memory
- **String is immutable** — because of the string pool, security (it is used for URLs and
  credentials), thread safety, and a cached hash that makes it a fast map key.
- **String vs StringBuilder vs StringBuffer** — immutable · mutable, not synchronised (use
  this) · mutable, synchronised, legacy. Concatenating in a loop with `+` is O(n²).
- `==` compares references, `.equals()` compares values. `new String("a") != "a"` but
  `.equals` is true.
- **Stack** holds method frames and locals, per thread. **Heap** holds objects, shared,
  garbage collected.

---

## Java 8 — likely for both tracks

```java
// filter → map → collect
List<String> names = apps.stream()
        .filter(a -> a.getStatus() == PENDING)
        .map(Application::getReference)
        .collect(Collectors.toList());

// group and count
Map<Status, Long> byStatus = apps.stream()
        .collect(Collectors.groupingBy(Application::getStatus, Collectors.counting()));
```

- **Intermediate ops are lazy** (`filter`, `map`, `sorted`); **terminal ops trigger**
  (`collect`, `forEach`, `reduce`, `findFirst`). A stream is consumed once.
- **`map` vs `flatMap`** — one-to-one vs one-to-many then flattened.
- **Functional interfaces:** `Predicate`→filter, `Function`→map, `Consumer`→forEach,
  `Supplier`→lazy value. One abstract method each.
- **Optional** — use `map`/`orElse`/`orElseThrow`, not `isPresent` + `get`.
- **Lambda** = implementation of a one-method interface, without the boilerplate.

---

## Likely coding question (keep it simple — this is a walk-in, not a DSA screen)

Expect **one** easy problem: reverse a string, palindrome, first non-repeating character,
count word frequency, find duplicates, FizzBuzz, second largest.

```java
// first non-repeating character
Map<Character, Integer> counts = new LinkedHashMap<>();   // LinkedHashMap for order
for (char c : s.toCharArray()) counts.merge(c, 1, Integer::sum);
for (var e : counts.entrySet()) if (e.getValue() == 1) return e.getKey();
return null;

// second largest
int first = Integer.MIN_VALUE, second = Integer.MIN_VALUE;
for (int n : nums) {
    if (n > first) { second = first; first = n; }
    else if (n > second && n != first) second = n;
}
```

**The four free marks everybody drops:**
1. **Ask the edge cases first** — null, empty, duplicates, case sensitivity.
2. **Say the brute force and its cost**, then improve it. *"Two nested loops is O(n²) — a
   HashMap makes the lookup O(1), so one pass."*
3. **Talk while you write.** Silence reads as stuck.
4. **State time and space at the end**, before they ask.
