# 08 · SQL and Query Optimisation 🔴
**Time needed: 75 minutes**

Your resume claims SQL tuning, indexing and execution plan analysis. That is unusual at
this level and it is genuinely valuable — but it also means you **will** be tested on it.
An interviewer who sees "identified and removed N+1 queries, added strategic indexing"
will ask you to explain indexing properly.

---

## Q1. Joins — know all four
```sql
-- INNER: only rows that match in both tables
SELECT t.id, c.name FROM transactions t
INNER JOIN customers c ON t.customer_id = c.id;

-- LEFT: every row from the left, NULLs where the right has no match
SELECT c.name, t.id FROM customers c
LEFT JOIN transactions t ON t.customer_id = c.id;     -- includes customers with no txns

-- RIGHT: the mirror image. Rarely used - people rewrite it as a LEFT JOIN.
-- FULL OUTER: everything from both sides. MySQL does not support it directly.
```

**The classic question:** *"Find customers with no transactions."*
```sql
SELECT c.* FROM customers c
LEFT JOIN transactions t ON t.customer_id = c.id
WHERE t.id IS NULL;
```
The `WHERE ... IS NULL` after a LEFT JOIN is the pattern. Learn it.

⚠️ **A trap worth knowing:** putting a condition on the right-hand table in the `WHERE`
clause of a LEFT JOIN silently turns it into an INNER JOIN, because `NULL` fails the
condition. If you want to filter the joined table without losing left rows, the
condition belongs in the `ON` clause.


**Say this.**
> "An inner join returns only rows that match on both sides. A left join returns every row
> from the left table and nulls where the right has no match, which is what I use when the
> absence is the thing I care about — customers with no transactions, or requests with no
> approval yet. Right joins are the mirror image and people usually rewrite them as left
> joins for readability.
>
> The trap is putting a condition on the right-hand table in the `WHERE` clause of a left
> join. Null fails the condition, so those rows are dropped and you have silently turned it
> back into an inner join. The condition has to go in the `ON` clause."

## Q2. 🔴🔴 Indexing — the answer that matters most here

### What an index actually is
> "An index is a separate sorted structure, usually a **B-tree**, that maps column values
> to row locations. Without one, the database does a **full table scan** — it reads every
> row to find matches, which is O(n). With one, it walks the tree, which is O(log n).
> It is the same reason you use the index at the back of a book instead of reading every
> page."

### When an index helps
- Columns in a `WHERE` clause
- Columns you `JOIN` on — **especially foreign keys, which are not indexed automatically
  in MySQL's InnoDB unless you add them**
- Columns in `ORDER BY` and `GROUP BY`

### 🔴 The cost — always mention this, it is what shows real understanding
> "Indexes are not free. Every `INSERT`, `UPDATE` and `DELETE` has to update every index
> on that table, so over-indexing slows down writes. They also take disk space. On a
> write-heavy table I index deliberately, not by default — the right number is the
> smallest set that serves the actual query patterns."

Saying only "indexes make queries faster" is the answer of someone who read it. Saying
"and they slow down writes, so I add them deliberately" is the answer of someone who has
tuned a real system.

### Composite indexes and the left-most prefix rule
```sql
CREATE INDEX idx_txn_status_date ON transactions (status, created_at);
```
This index serves:
- `WHERE status = 'PENDING'` ✅
- `WHERE status = 'PENDING' AND created_at > '2026-01-01'` ✅

But **not** `WHERE created_at > '2026-01-01'` alone ❌ — because the index is sorted by
`status` first. This is the **left-most prefix rule**, and it is a favourite question.
Column order in a composite index matters.

**Real-time example.** The recall report always filters by status and then by a date
range: `WHERE status = 'PENDING' AND created_at BETWEEN ? AND ?`. So the index is
`(status, created_at)` in that order — the equality column first, the range column
second. Reversed, as `(created_at, status)`, the index is far less effective, because the
range scan happens first and status cannot narrow it. Getting that column order right was
part of the 15-second to 6-second fix.

### What stops an index being used
```sql
WHERE YEAR(created_at) = 2026        -- ❌ a function on the column defeats the index
WHERE created_at >= '2026-01-01'     -- ✅ same meaning, index usable

WHERE account_number LIKE '%1234'    -- ❌ a leading wildcard cannot use a B-tree
WHERE account_number LIKE '1234%'    -- ✅ prefix match is fine
```
Mentioning these two unprompted is a strong signal.

### Clustered vs non-clustered
- **Clustered** — the table rows are physically stored in this order. One per table; in
  InnoDB it is the primary key.
- **Non-clustered** — a separate structure pointing back to the row.

### Covering index
An index containing every column a query needs, so the database answers it from the
index alone and never touches the table. Sometimes the biggest single win available.

**Real-time example.** A dashboard count of pending recalls per branch needs only
`status` and `branch_code`. An index on `(status, branch_code)` covers it, so the database
answers from the index and never reads a single table row. On a large transactions table
that is the difference between milliseconds and seconds.

## Q3. 🔴 EXPLAIN — how you actually diagnose
Your resume says you analysed execution plans. Be ready to describe the process.

```sql
EXPLAIN SELECT t.id, c.name FROM transactions t
JOIN customers c ON t.customer_id = c.id
WHERE t.status = 'PENDING';
```

**What you look for:**

| Column | What matters |
|---|---|
| `type` | `ALL` = full table scan, the thing to fix. `ref` or `range` is good. `const`/`eq_ref` is best. |
| `key` | Which index was actually used. `NULL` means none. |
| `rows` | Estimated rows examined. A big number here is the problem. |
| `Extra` | `Using filesort` or `Using temporary` mean extra work. `Using index` is a covering index — good. |

**Say the process, not just the tool:**
> "I start from the slow query log or the application timings to find *which* query is
> slow — there is no point optimising the wrong one. Then I run `EXPLAIN` on it. If the
> type is `ALL` and the row count is large, it is doing a full scan, and I look at what
> the `WHERE` and `JOIN` columns are and whether an index exists. After adding one I
> re-run `EXPLAIN` to confirm it is actually being used, and re-measure the query time.
> Adding an index without checking the plan afterwards is guessing."

## Q4. Normalisation, and when to break it
- **1NF** — atomic values, no repeating groups.
- **2NF** — 1NF, and no partial dependency on part of a composite key.
- **3NF** — 2NF, and no non-key column depending on another non-key column.

> "Normalisation removes duplication, so there is one place to update a fact and no
> inconsistency. The cost is more joins. **Denormalisation** deliberately duplicates data
> to avoid expensive joins on read-heavy paths — for example storing a customer name on a
> report table so a reporting query does not join. It is a trade: faster reads, but now
> you have two copies to keep in sync."

## Q5. Common query questions

**Second-highest salary** — asked constantly:
```sql
SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);

-- or, more generally, the Nth highest
SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;
```

**Find duplicates:**
```sql
SELECT email, COUNT(*) FROM customers GROUP BY email HAVING COUNT(*) > 1;
```

**🔴 `WHERE` vs `HAVING`:** `WHERE` filters **rows before** grouping. `HAVING` filters
**groups after** aggregation. You cannot use an aggregate in `WHERE`.

**`UNION` vs `UNION ALL`:** `UNION` removes duplicates, which costs a sort. `UNION ALL`
keeps everything and is faster. Use `UNION ALL` unless you actually need deduplication.

**`DELETE` vs `TRUNCATE` vs `DROP`:** `DELETE` removes rows, can have a `WHERE`, is
logged and can be rolled back. `TRUNCATE` empties the table quickly, no `WHERE`, resets
auto-increment. `DROP` removes the table itself.

**Window functions**, worth knowing one:
```sql
SELECT name, salary, department,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_in_dept
FROM employees;
```
Unlike `GROUP BY`, a window function keeps every row and adds a computed column.


**Say this when they give you a query to write.**
> "Let me state what I am aiming for first — I want the second highest distinct salary, so
> I need to handle duplicates, and decide what should happen if there is no second value."

Then write it. The pattern that scores is: restate, mention the edge case, write, then say
the complexity or the index it would need. For the duplicates query, mention that
`GROUP BY ... HAVING COUNT(*) > 1` is the standard shape and that on a large table the
grouped column wants an index.

## Q6. ACID
- **Atomicity** — all of the transaction, or none of it.
- **Consistency** — the database moves from one valid state to another; constraints hold.
- **Isolation** — concurrent transactions do not corrupt each other.
- **Durability** — once committed, it survives a crash.

**The banking example makes this concrete:** a transfer is a debit and a credit. Without
atomicity, a crash between them destroys money. Use that example — it fits your domain.


**Say this — use the banking example, it is your domain.**
> "A transfer is the clearest example. Debiting one account and crediting another must be
> **atomic** — both or neither, because a crash between them destroys money.
> **Consistency** means constraints still hold afterwards, so the ledger still balances.
> **Isolation** means two concurrent transfers on the same account cannot interleave and
> produce a wrong balance. And **durability** means once it is committed it survives a
> crash — the customer has been told it happened, so it has to have happened.
>
> That is also why I would not move something like a ledger entry to eventual consistency
> without the business explicitly agreeing to it."

## Q7. SQL vs NoSQL — you have MongoDB on your resume
> "I would use a relational database when the data is structured and relational and I
> need ACID transactions — which is most of banking. MongoDB suits flexible or evolving
> schemas, document-shaped data, and cases where horizontal scaling matters more than
> joins. The real question is the access pattern: if I am constantly joining, that is a
> relational shape, and forcing it into documents means duplicating data everywhere."

## Q8. Pagination at the database level
```sql
SELECT * FROM transactions ORDER BY created_at DESC LIMIT 20 OFFSET 0;
```
> "OFFSET pagination degrades on deep pages, because the database still has to scan and
> discard everything before the offset. Page 5,000 is slow. **Keyset pagination** —
> `WHERE created_at < :lastSeen ORDER BY created_at DESC LIMIT 20` — stays fast because
> the index seeks straight to the position."

That is a strong detail for a reporting-heavy system, which yours was.

---

## ✅ Check yourself before moving on
1. Explain what an index is, **and its cost on writes**.
2. Explain the left-most prefix rule with the composite index example.
3. Give two things that stop an index being used.
4. Describe your EXPLAIN process end to end.
5. Write the "customers with no transactions" query from memory.
6. Explain `WHERE` vs `HAVING`.
