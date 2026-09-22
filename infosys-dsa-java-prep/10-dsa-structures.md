# 10 · DSA Part 2 — Linked Lists, Stacks, Recursion, Searching, Trees 🔴
**Time needed: 2 hours. Type the starred ones.**

Lower probability than Part 1, but a linked list or stack question is common enough that
being blank on one would hurt. Trees are less likely at this level — know the traversals and
move on.

---

## Part A · Linked lists 🔴

### The node, and why you write a dummy head
```java
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}
```

**The single most useful trick:** a **dummy head** node removes almost every special case
around "what if the list is empty" or "what if I delete the first node".

### ⭐ Reverse a linked list
*The most asked linked list question, by a distance.*

```java
public static ListNode reverse(ListNode head) {
    ListNode prev = null, curr = head;
    while (curr != null) {
        ListNode next = curr.next;   // remember where we were going
        curr.next = prev;            // flip the pointer
        prev = curr;                 // shuffle both forward
        curr = next;
    }
    return prev;                     // prev is the new head
}
```
**Trace it out loud** — three pointers, and the order of the four lines matters. If you
assign `curr.next = prev` before saving `next`, you have lost the rest of the list.
O(n) time, O(1) space.

### ⭐ Find the middle — the two-pointer trick
```java
public static ListNode middle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;       // moves twice as fast
    }
    return slow;
}
```

### ⭐ Detect a cycle — Floyd's algorithm
```java
public static boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;   // they can only meet inside a loop
    }
    return false;
}
```
**Say:** "A `HashSet` of visited nodes also works and is easier to explain, but it is O(n)
space. Floyd's is O(1) — if there is a cycle, the fast pointer eventually laps the slow one."

Knowing *both* and choosing, out loud, is what scores.

### Merge two sorted lists
```java
public static ListNode merge(ListNode a, ListNode b) {
    ListNode dummy = new ListNode(0), tail = dummy;
    while (a != null && b != null) {
        if (a.val <= b.val) { tail.next = a; a = a.next; }
        else                { tail.next = b; b = b.next; }
        tail = tail.next;
    }
    tail.next = (a != null) ? a : b;    // attach whatever is left
    return dummy.next;
}
```
The dummy head is why this has no special cases.

### Remove the nth node from the end
Two pointers, n apart: advance the first n steps, then move both until the first hits the
end. The second is now at the node before the one to delete. Use a dummy head so deleting
the first node is not special.

---

## Part B · Stacks and queues 🔴

**Stack** is LIFO — use `Deque<Integer> stack = new ArrayDeque<>()`.
⚠️ **Do not use the legacy `Stack` class.** It extends `Vector` and is synchronised, so it is
slower and its iteration order is famously confusing. Saying "`ArrayDeque`, because
`java.util.Stack` is a legacy synchronised class" is a small detail that lands well.

**Queue** is FIFO — `Queue<Integer> q = new LinkedList<>()` or `ArrayDeque`.

### ⭐ Balanced brackets
*The classic stack question.*
```java
public static boolean isBalanced(String s) {
    Deque<Character> stack = new ArrayDeque<>();
    Map<Character, Character> pairs = Map.of(')', '(', ']', '[', '}', '{');

    for (char c : s.toCharArray()) {
        if (c == '(' || c == '[' || c == '{') {
            stack.push(c);
        } else if (pairs.containsKey(c)) {
            if (stack.isEmpty() || stack.pop() != pairs.get(c)) return false;
        }
    }
    return stack.isEmpty();          // leftovers mean unclosed brackets
}
```
The two edge cases interviewers check: a closing bracket when the stack is **empty**, and
leftovers on the stack **at the end**. Mention both.

### Next greater element
For each element, the next larger one to its right. A **monotonic stack** does it in O(n)
instead of O(n²): push indices, and whenever the current value exceeds the value at the top
of the stack, you have found that index's answer — pop and record.

### Implement a queue using two stacks
Push onto `in`. To pop, if `out` is empty, drain `in` into `out` and pop from there. Each
element moves at most twice, so it is **amortised O(1)**. Saying "amortised" is the point of
the question.

---

## Part C · Recursion 🔴

### The three rules
1. A **base case** that stops it. Without one you get `StackOverflowError`.
2. The recursive call must move **toward** the base case.
3. Trust the recursion — assume the smaller call works, and handle only this level.

### Factorial and Fibonacci
```java
public static long factorial(int n) {
    if (n <= 1) return 1;                    // base case
    return n * factorial(n - 1);
}

// iterative Fibonacci - prefer this
public static long fib(int n) {
    if (n <= 1) return n;
    long prev = 0, curr = 1;
    for (int i = 2; i <= n; i++) {
        long next = prev + curr;
        prev = curr; curr = next;
    }
    return curr;
}

// if they insist on recursion, memoise it
public static long fibMemo(int n, Map<Integer, Long> memo) {
    if (n <= 1) return n;
    return memo.computeIfAbsent(n, k -> fibMemo(k - 1, memo) + fibMemo(k - 2, memo));
}
```
**Say:** "Naive recursive Fibonacci is O(2ⁿ) because it recomputes the same subproblems.
Memoising makes it O(n). Iterative is O(n) time and O(1) space, so that is what I would
actually write."

That comparison is the whole reason the question is asked.

### Recursion vs iteration
> "Recursion is clearer for genuinely recursive structures — trees, nested directories. But
> each call uses a stack frame, so deep recursion risks `StackOverflowError`, and Java does
> not do tail-call optimisation. For a linear loop I use iteration."

---

## Part D · Searching and sorting 🔴

### ⭐ Binary search — write it correctly
```java
public static int binarySearch(int[] sorted, int target) {
    int lo = 0, hi = sorted.length - 1;
    while (lo <= hi) {                       // <= , not <
        int mid = lo + (hi - lo) / 2;        // avoids integer overflow
        if (sorted[mid] == target) return mid;
        if (sorted[mid] < target) lo = mid + 1;
        else                      hi = mid - 1;
    }
    return -1;
}
```
**Two details interviewers look for:** `lo + (hi - lo) / 2` rather than `(lo + hi) / 2`,
which can overflow; and `while (lo <= hi)`, because with `<` you miss the last element.
O(log n), **and it only works on sorted data** — say that.

### Sorting — what to know, not how to implement

| Algorithm | Time | Space | Stable |
|---|---|---|---|
| Bubble / insertion | O(n²) | O(1) | yes |
| Merge sort | **O(n log n)** | O(n) | **yes** |
| Quick sort | O(n log n) avg, O(n²) worst | O(log n) | no |
| Heap sort | O(n log n) | O(1) | no |

**What Java actually uses:** `Collections.sort` and `Arrays.sort` on **objects** use TimSort,
a stable merge sort. `Arrays.sort` on **primitives** uses dual-pivot quicksort, which is not
stable — but stability is meaningless for primitives, which is why that is fine.

**Stable** means equal elements keep their relative order. It matters when you sort by one
field and then another.

```java
list.sort(Comparator.comparing(Employee::getDept)
                    .thenComparing(Employee::getSalary, Comparator.reverseOrder()));
```
Being able to write a chained comparator is more likely to be asked than implementing a sort.

---

## Part E · Trees — know the traversals, do not over-invest

```java
class TreeNode { int val; TreeNode left, right; }
```

### The four traversals
```java
// INORDER - left, node, right. On a BST this gives SORTED order.
void inorder(TreeNode n, List<Integer> out) {
    if (n == null) return;
    inorder(n.left, out); out.add(n.val); inorder(n.right, out);
}

// PREORDER  - node, left, right   (used to copy a tree)
// POSTORDER - left, right, node   (used to delete a tree)

// LEVEL ORDER (BFS) - uses a QUEUE, not recursion
List<Integer> levelOrder(TreeNode root) {
    List<Integer> out = new ArrayList<>();
    if (root == null) return out;
    Queue<TreeNode> q = new LinkedList<>();
    q.add(root);
    while (!q.isEmpty()) {
        TreeNode n = q.poll();
        out.add(n.val);
        if (n.left != null)  q.add(n.left);
        if (n.right != null) q.add(n.right);
    }
    return out;
}
```

**The one fact to have ready:** *"Inorder traversal of a binary search tree gives you the
values in sorted order."* That is the most commonly asked tree fact.

### Height, and BST search
```java
int height(TreeNode n) {
    return n == null ? 0 : 1 + Math.max(height(n.left), height(n.right));
}
```
BST search is O(log n) on a balanced tree and **O(n) on a degenerate one** — which is why
self-balancing trees like red-black exist. That connects straight back to `TreeMap` and to
HashMap's treeified buckets, and making that connection unprompted sounds very good.

**Do not spend Saturday morning on tree problems.** Know the four traversals, the BST/inorder
fact, and the height function. That is proportionate.

---

## ✅ Practice plan for this file
Type these from an empty file: **reverse a linked list · detect a cycle · balanced
brackets · binary search.**

Reverse-a-linked-list and balanced brackets are the two most likely to appear. Practise
tracing the reversal out loud with three pointers — explaining it is harder than writing it.
