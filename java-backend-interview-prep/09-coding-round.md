# 09 · Coding Round 🔴
**Time needed: 90 minutes. Write the code, do not read it.**

Reading solutions feels productive and is nearly worthless. Open an IDE and type these
from an empty file.

---

## What to expect at Infosys

The coding bar for an experienced hire at a services company is **moderate**. They are
not asking for dynamic programming. Expect:

- String and array manipulation
- Collections and HashMap usage
- Java 8 stream problems
- One "write a small class" or design question
- Sometimes SQL instead of code

**They are checking:** can you write correct, compiling Java; do you handle edge cases;
do you talk while you work. Not whether you know a clever trick.

**The process, which is half the marks:**
1. **Restate the problem.** "So I need to return the first character that appears once,
   and null if there isn't one?"
2. **Ask about edge cases** *before* coding. Empty input? Nulls? Case sensitivity?
3. **Say your approach out loud.** "I'll count with a LinkedHashMap so I keep order,
   then find the first with a count of one."
4. **Then write it.**
5. **Trace one example** out loud when done.
6. **State the complexity.** They almost always ask, so beat them to it.

---

## Problem 1 🔴 — First non-repeating character
*The most common Java string question in Indian interviews.*

```java
public static Character firstNonRepeating(String input) {
    if (input == null || input.isEmpty()) return null;

    Map<Character, Integer> counts = new LinkedHashMap<>();   // preserves insertion order
    for (char c : input.toCharArray()) {
        counts.merge(c, 1, Integer::sum);
    }

    for (Map.Entry<Character, Integer> e : counts.entrySet()) {
        if (e.getValue() == 1) return e.getKey();
    }
    return null;
}
```
**Say:** "LinkedHashMap, not HashMap, because I need insertion order to find the *first*
one. Two passes, so O(n) time and O(k) space where k is the distinct character count."

## Problem 2 🔴 — Reverse a string, and check a palindrome
```java
public static String reverse(String s) {
    if (s == null) return null;
    return new StringBuilder(s).reverse().toString();
}

// they often want it without the library method
public static String reverseManual(String s) {
    char[] chars = s.toCharArray();
    int left = 0, right = chars.length - 1;
    while (left < right) {
        char tmp = chars[left];
        chars[left++] = chars[right];
        chars[right--] = tmp;
    }
    return new String(chars);
}

public static boolean isPalindrome(String s) {
    String clean = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
    int left = 0, right = clean.length() - 1;
    while (left < right) {
        if (clean.charAt(left++) != clean.charAt(right--)) return false;
    }
    return true;
}
```
The two-pointer palindrome is better than reversing and comparing, because it can exit
early and uses no extra string. Say that.

## Problem 3 🔴 — Duplicates in an array
```java
// find duplicates
public static Set<Integer> findDuplicates(int[] nums) {
    Set<Integer> seen = new HashSet<>();
    Set<Integer> dupes = new HashSet<>();
    for (int n : nums) {
        if (!seen.add(n)) dupes.add(n);   // add() returns false if already present
    }
    return dupes;
}

// remove duplicates, keeping order
public static List<Integer> removeDuplicates(List<Integer> nums) {
    return new ArrayList<>(new LinkedHashSet<>(nums));
}
```
`seen.add(n)` returning false is the neat part — one lookup instead of `contains` then
`add`.

## Problem 4 🔴 — Stream problems
These are very likely, because your resume says Java 8.

```java
// count word frequency
Map<String, Long> freq = Arrays.stream(sentence.toLowerCase().split("\\s+"))
        .collect(Collectors.groupingBy(w -> w, Collectors.counting()));

// second highest number
Optional<Integer> second = nums.stream()
        .distinct()
        .sorted(Comparator.reverseOrder())
        .skip(1)
        .findFirst();

// group employees by department
Map<String, List<Employee>> byDept = employees.stream()
        .collect(Collectors.groupingBy(Employee::getDepartment));

// highest paid employee per department
Map<String, Optional<Employee>> topPerDept = employees.stream()
        .collect(Collectors.groupingBy(Employee::getDepartment,
                 Collectors.maxBy(Comparator.comparing(Employee::getSalary))));

// sum of even numbers
int sum = nums.stream().filter(n -> n % 2 == 0).mapToInt(Integer::intValue).sum();

// sort a map by value, descending
Map<String, Integer> sorted = map.entrySet().stream()
        .sorted(Map.Entry.<String, Integer>comparingByValue().reversed())
        .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,
                                  (a, b) -> a, LinkedHashMap::new));
```
That last one is worth practising — the four-argument `toMap` with `LinkedHashMap::new`
is needed to keep the sort order, and people always forget it.

## Problem 5 — Two sum
```java
public static int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> seen = new HashMap<>();     // value -> index
    for (int i = 0; i < nums.length; i++) {
        int need = target - nums[i];
        if (seen.containsKey(need)) return new int[]{ seen.get(need), i };
        seen.put(nums[i], i);
    }
    return new int[]{};
}
```
**Say:** "The brute force is two nested loops, O(n²). Storing what I have seen in a
HashMap makes the lookup O(1), so it becomes one pass, O(n) time and O(n) space. That is
the classic time-for-space trade."

Talking about the brute force *first*, then improving it, is exactly what they want.

## Problem 6 — Fibonacci and factorial
```java
// iterative - preferred, no stack growth
public static long fib(int n) {
    if (n <= 1) return n;
    long prev = 0, curr = 1;
    for (int i = 2; i <= n; i++) {
        long next = prev + curr;
        prev = curr;
        curr = next;
    }
    return curr;
}

// recursive with memoisation, if they ask for recursion
public static long fibMemo(int n, Map<Integer, Long> memo) {
    if (n <= 1) return n;
    return memo.computeIfAbsent(n, k -> fibMemo(k - 1, memo) + fibMemo(k - 2, memo));
}
```
Naive recursion is O(2ⁿ) and will be called out. Memoisation makes it O(n).

## Problem 7 — Reverse words, count vowels, anagram
```java
public static String reverseWords(String s) {
    String[] words = s.trim().split("\\s+");
    Collections.reverse(Arrays.asList(words));
    return String.join(" ", words);
}

public static boolean isAnagram(String a, String b) {
    if (a == null || b == null || a.length() != b.length()) return false;
    char[] x = a.toCharArray(), y = b.toCharArray();
    Arrays.sort(x); Arrays.sort(y);
    return Arrays.equals(x, y);
}
```
For anagram, mention the alternative: counting characters in a map is O(n) versus
O(n log n) for sorting. Naming the trade-off scores.

## Problem 8 — "Write a class" questions

**Singleton, thread safe:**
```java
public class ConfigManager {
    private static volatile ConfigManager instance;
    private ConfigManager() { }

    public static ConfigManager getInstance() {
        if (instance == null) {                          // first check, no lock
            synchronized (ConfigManager.class) {
                if (instance == null) {                  // second check, with lock
                    instance = new ConfigManager();
                }
            }
        }
        return instance;
    }
}
```
This is **double-checked locking**. `volatile` is essential — without it another thread
can see a partially constructed object due to instruction reordering.

**Say the better answer too:** "In a Spring application I would not write this at all.
A `@Component` is already a singleton in the container, and that is easier to test than
a static instance. The enum singleton is also simpler if I truly need one outside Spring."

**Immutable class:**
```java
public final class Money {                       // final: cannot be subclassed
    private final BigDecimal amount;             // final fields
    private final String currency;

    public Money(BigDecimal amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }
    public BigDecimal getAmount() { return amount; }   // no setters
}
```
The four rules: make the class `final`, all fields `private final`, no setters, and if a
field is mutable (a `Date`, a `List`) return a **defensive copy** from the getter rather
than the field itself.

---

## Java-specific traps they enjoy

**"What does this print?"**
```java
Integer a = 127, b = 127;
Integer c = 128, d = 128;
System.out.println(a == b);   // true  - Integer cache covers -128..127
System.out.println(c == d);   // false - outside the cache, different objects
System.out.println(c.equals(d)); // true
```

```java
String s1 = "abc";
String s2 = "abc";
String s3 = new String("abc");
s1 == s2          // true  - string pool
s1 == s3          // false
s1.equals(s3)     // true
s1 == s3.intern() // true  - intern() returns the pooled instance
```

```java
System.out.println(0.1 + 0.2 == 0.3);   // false - floating point
// which is exactly why money uses BigDecimal
```

---

## ✅ Practice plan for this file
Type problems **1, 3, 4 and 5** from an empty file, no copy-paste. If you can write
those four while explaining what you are doing, you can handle this round.
