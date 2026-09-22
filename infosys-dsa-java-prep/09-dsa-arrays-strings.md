# 09 · DSA Part 1 — Patterns, Arrays, Strings, Hashing 🔴🔴
**Time needed: 3 hours across two sessions. Type every solution.**

> ✓ Every solution in files 09 and 10 has been **compiled and run against test cases**,
> including the edge cases. If yours does not behave the same way, it is a typo in your
> version, not a bug in the guide.

---

## First, the context: what DSA level does Infosys actually test?

Set your expectations correctly, because over-preparing the wrong thing is the most common
waste of time before a service-company interview.

**What they ask:** arrays, strings, HashMap-based counting, two pointers, basic recursion,
sorting and searching, sometimes a linked list or a stack. Usually **one or two problems**,
at what LeetCode would call **easy to lower-medium**.

**What they almost never ask:** dynamic programming, graph algorithms, tries, segment trees.
If you are spending Saturday morning on DP, stop.

**What they are actually checking:**

1. Can you write **compiling, correct Java** without an IDE completing it for you?
2. Do you reach for the **right collection** — and can you say why?
3. Do you handle **edge cases** — null, empty, single element, duplicates?
4. Can you state the **time and space complexity** without being asked?
5. Do you **talk while you think**?

Points 4 and 5 are free marks and most candidates drop them.

---

## How to run a coding question — the six steps

```
1. RESTATE      "So I need to return the first character that appears once,
                 and null if there isn't one?"
2. EDGE CASES   Ask before coding. Empty? Null? Case sensitive? Duplicates?
3. BRUTE FORCE  Say it out loud, with its complexity. Do not write it yet.
4. IMPROVE      "I can make the lookup O(1) with a HashMap, so one pass."
5. WRITE        Talking as you go.
6. TRACE + COST Walk one example through, then state time and space.
```

**Step 3 matters more than people think.** Saying *"the brute force is two nested loops,
O(n²) — I can do better with a map"* shows you can reason about cost. Jumping straight to
the optimal solution you memorised shows nothing.

---

## Complexity — the table you must know cold

| Operation | ArrayList | LinkedList | HashMap / HashSet | TreeMap / TreeSet |
|---|---|---|---|---|
| Access by index | **O(1)** | O(n) | — | — |
| Search by value | O(n) | O(n) | **O(1)** avg | O(log n) |
| Insert / delete at end | O(1)* | O(1) | **O(1)** avg | O(log n) |
| Insert / delete in middle | O(n) | O(1) at a known node | — | — |
| Keeps order | insertion | insertion | **no** | **sorted** |

\* amortised — occasionally it resizes and copies.

**Sorting** — `Collections.sort` / `Arrays.sort` on objects is **O(n log n)**, a stable
merge sort (TimSort). `Arrays.sort` on **primitives** is a dual-pivot quicksort, O(n log n)
average, and **not stable**. That distinction is a good detail to know.

**Binary search** — O(log n), but **only on sorted data**.

**The rule of thumb to say out loud:** *"If I am searching inside a loop, that is O(n²), and
a HashMap usually turns it into O(n) by trading space for time."* That single sentence
solves a large share of interview problems.

---

## Pattern 1 🔴🔴 — Hashing for counting and lookup
*The single most useful pattern. Half of all easy problems are this.*

### First non-repeating character
```java
public static Character firstNonRepeating(String input) {
    if (input == null || input.isEmpty()) return null;

    Map<Character, Integer> counts = new LinkedHashMap<>();   // insertion order!
    for (char c : input.toCharArray()) {
        counts.merge(c, 1, Integer::sum);
    }
    for (Map.Entry<Character, Integer> e : counts.entrySet()) {
        if (e.getValue() == 1) return e.getKey();
    }
    return null;
}
```
**Say:** "`LinkedHashMap`, not `HashMap`, because I need insertion order to find the *first*
one. Two passes, so O(n) time, O(k) space where k is the distinct character count."

### Two sum
```java
public static int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> seen = new HashMap<>();       // value -> index
    for (int i = 0; i < nums.length; i++) {
        int need = target - nums[i];
        if (seen.containsKey(need)) return new int[]{ seen.get(need), i };
        seen.put(nums[i], i);
    }
    return new int[]{};
}
```
**Say:** "Brute force is two nested loops, O(n²). Storing what I have already seen makes the
lookup O(1), so it becomes one pass — O(n) time, O(n) space. Classic time-for-space trade."

### Find and remove duplicates
```java
public static Set<Integer> findDuplicates(int[] nums) {
    Set<Integer> seen = new HashSet<>(), dupes = new HashSet<>();
    for (int n : nums) {
        if (!seen.add(n)) dupes.add(n);      // add() returns false if already present
    }
    return dupes;
}

public static List<Integer> removeDuplicatesKeepingOrder(List<Integer> nums) {
    return new ArrayList<>(new LinkedHashSet<>(nums));
}
```
`seen.add(n)` returning `false` is the neat bit — one lookup instead of `contains` then `add`.

### Anagram check
```java
public static boolean isAnagram(String a, String b) {
    if (a == null || b == null || a.length() != b.length()) return false;

    Map<Character, Integer> counts = new HashMap<>();
    for (char c : a.toCharArray()) counts.merge(c, 1, Integer::sum);
    for (char c : b.toCharArray()) {
        Integer n = counts.get(c);
        if (n == null) return false;
        if (n == 1) counts.remove(c); else counts.put(c, n - 1);
    }
    return counts.isEmpty();
}
```
**Say the trade-off:** "Sorting both and comparing is simpler but O(n log n). Counting is
O(n) with O(k) space. For a fixed alphabet I could use an `int[26]` instead of a map."

### Word / element frequency
```java
Map<String, Long> freq = Arrays.stream(sentence.toLowerCase().split("\\s+"))
        .collect(Collectors.groupingBy(w -> w, Collectors.counting()));

// highest frequency element
String top = Collections.max(freq.entrySet(), Map.Entry.comparingByValue()).getKey();
```

---

## Pattern 2 🔴 — Two pointers
*Use when the array is sorted, or when you work inward from both ends.*

### Palindrome
```java
public static boolean isPalindrome(String s) {
    if (s == null) return false;
    String clean = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
    int left = 0, right = clean.length() - 1;
    while (left < right) {
        if (clean.charAt(left++) != clean.charAt(right--)) return false;
    }
    return true;
}
```
**Say:** "Better than reversing and comparing, because it exits early on the first mismatch
and uses no extra string. O(n) time, O(1) extra space beyond the cleaned copy."

### Reverse in place
```java
public static String reverse(String s) {
    char[] c = s.toCharArray();
    int i = 0, j = c.length - 1;
    while (i < j) { char t = c[i]; c[i++] = c[j]; c[j--] = t; }
    return new String(c);
}
```
They often want this **without** `new StringBuilder(s).reverse()` — know both, offer the
library one first, then write the manual one if asked.

### Pair with a given sum in a *sorted* array
```java
public static int[] pairWithSum(int[] sorted, int target) {
    int lo = 0, hi = sorted.length - 1;
    while (lo < hi) {
        int sum = sorted[lo] + sorted[hi];
        if (sum == target) return new int[]{lo, hi};
        if (sum < target) lo++; else hi--;
    }
    return new int[]{};
}
```
**Say:** "O(n) time and **O(1) space** — better than the HashMap version, but only because
the input is sorted."

---

## Pattern 3 🔴 — Sliding window
*Use for "longest / shortest / maximum subarray or substring of size k, or satisfying X".*

### Maximum sum of a subarray of size k
```java
public static int maxSumOfSizeK(int[] nums, int k) {
    if (nums.length < k) return -1;
    int sum = 0;
    for (int i = 0; i < k; i++) sum += nums[i];

    int best = sum;
    for (int i = k; i < nums.length; i++) {
        sum += nums[i] - nums[i - k];        // slide: add new, drop old
        best = Math.max(best, sum);
    }
    return best;
}
```
**Say:** "Recomputing each window is O(n·k). Sliding reuses the previous sum, so it is O(n)."

### Longest substring without repeating characters
```java
public static int longestUnique(String s) {
    Map<Character, Integer> lastSeen = new HashMap<>();
    int best = 0, start = 0;
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (lastSeen.containsKey(c) && lastSeen.get(c) >= start) {
            start = lastSeen.get(c) + 1;      // shrink the window past the duplicate
        }
        lastSeen.put(c, i);
        best = Math.max(best, i - start + 1);
    }
    return best;
}
```
This is the hardest problem you are realistically likely to get. Worth practising twice.

---

## Pattern 4 — Array classics they actually ask

### Second largest / second highest
```java
public static int secondLargest(int[] nums) {
    int first = Integer.MIN_VALUE, second = Integer.MIN_VALUE;
    for (int n : nums) {
        if (n > first) { second = first; first = n; }
        else if (n > second && n != first) { second = n; }
    }
    return second;
}
```
**Say:** "Sorting and taking index n-2 is O(n log n) and breaks with duplicates. One pass is
O(n). The edge cases are an array shorter than two and all-equal elements."

### Missing number from 1..n
```java
public static int missingNumber(int[] nums, int n) {
    long expected = (long) n * (n + 1) / 2;
    long actual = 0;
    for (int x : nums) actual += x;
    return (int) (expected - actual);
}
```
Mentioning `long` to avoid overflow is a detail interviewers notice.

### Rotate an array by k
```java
public static void rotate(int[] nums, int k) {
    k %= nums.length;
    reverse(nums, 0, nums.length - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, nums.length - 1);
}
private static void reverse(int[] a, int i, int j) {
    while (i < j) { int t = a[i]; a[i++] = a[j]; a[j--] = t; }
}
```
The three-reversal trick: O(n) time, O(1) space. Worth memorising — it looks clever and it
is easy to remember.

### Move zeros to the end, keeping order
```java
public static void moveZeros(int[] nums) {
    int write = 0;
    for (int n : nums) if (n != 0) nums[write++] = n;
    while (write < nums.length) nums[write++] = 0;
}
```

---

## Pattern 5 — Java 8 stream versions
Because your resume says Java 8, they may ask for the stream form.

```java
// sum of even numbers
int sum = nums.stream().filter(n -> n % 2 == 0).mapToInt(Integer::intValue).sum();

// second highest distinct
Optional<Integer> second = nums.stream().distinct()
        .sorted(Comparator.reverseOrder()).skip(1).findFirst();

// group by a property
Map<String, List<Employee>> byDept = employees.stream()
        .collect(Collectors.groupingBy(Employee::getDepartment));

// highest paid per department
Map<String, Optional<Employee>> topPerDept = employees.stream()
        .collect(Collectors.groupingBy(Employee::getDepartment,
                 Collectors.maxBy(Comparator.comparing(Employee::getSalary))));

// sort a map by value, descending, keeping the order
Map<String, Integer> sorted = map.entrySet().stream()
        .sorted(Map.Entry.<String, Integer>comparingByValue().reversed())
        .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,
                                  (a, b) -> a, LinkedHashMap::new));
```
That last one is worth practising — the four-argument `toMap` with `LinkedHashMap::new` is
required to keep the sort order, and almost everyone forgets it.

⚠️ **Say the boundary:** "If this data were in the database I would do the grouping in SQL
with `GROUP BY` rather than streaming a million rows into memory." That shows judgement.

---

## Java traps they enjoy in coding rounds

```java
Integer a = 127, b = 127;
Integer c = 128, d = 128;
a == b            // true  - Integer cache covers -128..127
c == d            // false - outside the cache
c.equals(d)       // true

String s1 = "abc", s2 = "abc", s3 = new String("abc");
s1 == s2          // true  - string pool
s1 == s3          // false
s1.equals(s3)     // true

0.1 + 0.2 == 0.3  // false - floating point. Money uses BigDecimal.
```

---

## ✅ Practice plan for this file
Type these **from an empty file**, no copy-paste, talking out loud:
**first non-repeating · two sum · palindrome · max sum of size k · second largest.**

If you can write those five while explaining your reasoning, you are ready for this round.
