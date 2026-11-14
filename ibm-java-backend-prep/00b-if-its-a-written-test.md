# 00b · If Monday Is a Written Assessment 🔴🔴
**Time needed: 60 minutes. Read this the moment you finish file 00.**

---

## The situation

HR has told you Monday is **a technical written assessment, a technical interview, or
both** — and they do not yet know which. That is normal for a GCC pipeline — the
client decides the format and the vendor finds out late.

**Do not treat this as two separate preparations.** The overlap is roughly 80%. The same
Java, the same Spring Boot, the same SQL, the same messaging. What changes is the *form of
the answer*, and that is what this file is for.

There is one piece of good news worth holding on to. **A written test removes the thing
that makes interviews hard**: there is no panel reading your face, no follow-up pouncing
on a half-answer, no pressure to fill a silence. It rewards exactly the kind of revision
you can do this weekend — precise, recallable facts. If anything, a written round is the
easier of the two for someone in your position, because it does not care that your
experience is 2 years rather than 3.

**One thing to do before Monday:** reply to HR and ask, politely, two questions —
*roughly how long is the assessment, and is it on a platform like HackerRank or Mettl, or
written answers?* Most recruiters will tell you if asked directly, and it costs nothing.
Even "about 90 minutes, online" narrows it enormously. If they still do not know, prepare
for shape A below, because it is the most common.

---

## The three shapes it could take

**Shape A — an online test platform (most likely).** HackerRank, Mettl, Talscale or
similar. Usually 60–120 minutes, usually a mix: multiple-choice on Java and SQL, one or
two coding problems, sometimes a few short descriptive boxes. Often proctored through your
webcam, and often you cannot go back to a previous section once you move on.

**Shape B — descriptive written answers.** A document or form with 8–15 questions:
*"Explain the difference between `HashMap` and `ConcurrentHashMap`"*, *"Write a query to
find the second highest salary"*, *"How would you handle a failed message in RabbitMQ?"*
Marked by a human on precision and completeness.

**Shape C — a design or case write-up.** Less common at this level, but possible for a
BFSI client: *"Design a service that processes incoming payment files"*, written as prose
in 30–45 minutes.

Prepare for A and B. C is covered by file 12, and the structure at the end of this file
handles it.

---

## 🔴 What changes about your revision

In an interview, "it is roughly this" passes. **In a written test it does not.** Three
specific shifts:

**1. Exact names matter.** You cannot wave at an annotation — you have to spell it.
`@Transactional`, `@RestControllerAdvice`, `@EntityGraph`, `@KafkaListener`,
`@RabbitListener`, `spring.jpa.hibernate.ddl-auto`. Spend ten minutes just reading the
annotation names in files 03, 04 and 07 out loud.

**2. Output-based questions appear.** MCQ sections love "what does this print?" These are
not about reasoning — they are about knowing ten specific traps. They are below, and they
are the highest-value thing in this file because they are pure marks.

**3. You have to write SQL cold, by hand, with no database to try it on.** Most people are
far worse at this than they expect. There is a drill list below.

---

## 🔴 The ten output traps — learn these, they are free marks

**1. String pool and `==`**

```java
String a = "java";
String b = "java";
String c = new String("java");
System.out.println(a == b);        // true  - both point at the SAME pooled object
System.out.println(a == c);        // false - new String() forces a NEW heap object
System.out.println(a.equals(c));   // true  - equals compares the characters
```

String literals live in the string pool inside the heap, and identical literals share one
object. `new String()` always allocates a separate one. `==` compares references, `equals`
compares contents.

**2. The Integer cache**

```java
Integer x = 127, y = 127;
Integer p = 128, q = 128;
System.out.println(x == y);   // true  - cached
System.out.println(p == q);   // false - outside the cache, two objects
```

Java pre-caches boxed Integers from **−128 to 127**. Above that, autoboxing creates a new
object each time. This is one of the most-asked MCQs in existence.

**3. `finally` beats `return`**

```java
int f() {
    try { return 1; }
    finally { System.out.println("finally runs"); }
}
```

`finally` runs even when the `try` returns — it executes before the method actually hands
the value back. (If `finally` itself returns, it overwrites the value entirely, which is
why you should never return from a `finally`.)

**4. Initialisation order.** Static block → static variables, once when the class loads.
Then for each object: instance initialiser block → constructor. Parent before child, always.

**5. `HashMap` versus `Hashtable` versus `ConcurrentHashMap` on nulls.** `HashMap` allows
one null key and many null values. `Hashtable` allows neither. `ConcurrentHashMap` allows
neither — and that is the one people get wrong.

**6. `remove(int)` versus `remove(Object)`**

```java
List<Integer> list = new ArrayList<>(List.of(10, 20, 30));
list.remove(1);                      // removes INDEX 1 -> removes 20
list.remove(Integer.valueOf(10));    // removes the VALUE 10
```

**7. Pass by value.** Java is always pass by value. For an object, the *reference* is
copied — so the method can change the object's fields, but reassigning the parameter
changes nothing outside.

**8. Overloading versus overriding.** Overloading is resolved at **compile** time by the
declared type. Overriding is resolved at **runtime** by the actual object. A `static`
method cannot be overridden — it is hidden, and the declared type wins.

**9. `ConcurrentModificationException`.** Modifying a collection while iterating it with a
for-each throws this. Remove through the `Iterator`, or use `removeIf`, or iterate a copy.

**10. Autoboxing NPE in a ternary.** A ternary mixing `Integer` and `int` unboxes the
`Integer` — and a null one throws `NullPointerException` on a line with no obvious method
call on it.

---

## 🔴 The Java 8 written tasks — these come up constantly

Written rounds love streams, because they are easy to mark. Be able to write these five
from memory. Say the result type out loud as you write each one.

```java
// 1. group employees by department
Map<String, List<Employee>> byDept = employees.stream()
        .collect(Collectors.groupingBy(Employee::getDepartment));

// 2. count word frequency
Map<String, Long> freq = words.stream()
        .collect(Collectors.groupingBy(w -> w, Collectors.counting()));

// 3. find duplicates in a list
Set<Integer> seen = new HashSet<>();
Set<Integer> dupes = nums.stream().filter(n -> !seen.add(n)).collect(Collectors.toSet());

// 4. highest paid employee per department
Map<String, Optional<Employee>> topPerDept = employees.stream()
        .collect(Collectors.groupingBy(Employee::getDepartment,
                 Collectors.maxBy(Comparator.comparing(Employee::getSalary))));

// 5. second highest salary, distinct
Optional<Double> second = employees.stream()
        .map(Employee::getSalary).distinct()
        .sorted(Comparator.reverseOrder())
        .skip(1).findFirst();
```

Two facts they often ask alongside these: streams are **lazy** — nothing runs until the
terminal operation — and `map` transforms one-to-one while `flatMap` flattens a stream of
collections into one stream.

---

## 🔴 SQL you must be able to write by hand

No database to test against, so write these out on paper twice this weekend. Six patterns
cover most of what gets asked:

```sql
-- 1. second highest salary
SELECT MAX(salary) FROM employee WHERE salary < (SELECT MAX(salary) FROM employee);

-- 2. nth highest, the modern way
SELECT salary FROM (
  SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk FROM employee
) t WHERE rnk = 2;

-- 3. duplicates
SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1;

-- 4. department-wise count, only the big ones
SELECT d.name, COUNT(e.id) AS headcount
FROM department d LEFT JOIN employee e ON e.dept_id = d.id
GROUP BY d.name HAVING COUNT(e.id) > 5;

-- 5. rows in one table with no match in the other
SELECT c.* FROM customer c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;

-- 6. most recent row per group
SELECT * FROM (
  SELECT t.*, ROW_NUMBER() OVER (PARTITION BY account_id ORDER BY created_at DESC) rn
  FROM txn t
) x WHERE rn = 1;
```

**The theory question that always travels with these:** `WHERE` filters rows *before*
grouping, `HAVING` filters groups *after*. And the join family: `INNER` keeps only
matches, `LEFT` keeps everything on the left, `FULL OUTER` keeps both sides.

---

## How to write a descriptive answer that scores

This is the part candidates get wrong. They either write two lines, or they write a page.
Both lose marks. **A marker is looking for specific keywords and a clear structure**, and
they are reading fast.

**Use four moves, every time. Five to eight lines total:**

1. **One-line definition.**
2. **Why it exists / what problem it solves.**
3. **A concrete example — ideally from your own project.**
4. **When you would and would not use it.**

**Example — "Explain `@Transactional`":**

> `@Transactional` marks a method so that everything inside it runs in one database
> transaction — it all commits together or it all rolls back together.
>
> Spring implements it with a proxy: the proxy opens the transaction before your method
> runs and commits or rolls back after it returns. By default it rolls back on unchecked
> exceptions only, not on checked ones.
>
> I used it on a service method that updated a transaction's state and wrote an audit row,
> because leaving one written without the other would have been a compliance problem.
>
> Two things to watch: it only works on calls that come through the proxy, so a method
> calling another method in the same class bypasses it entirely; and the transaction holds
> a database connection for its whole duration, so slow work like an HTTP call does not
> belong inside one.

That is four short paragraphs and it names proxy, rollback behaviour, self-invocation and
connection holding. **That is what an 85% answer looks like** — same content as the spoken
version, laid out so a marker can see it in ten seconds.

**Example — "How do you make sure a message is not lost in RabbitMQ?"** Here, a numbered
list beats prose, because the answer *is* a chain:

> 1. Publisher confirms, so the producer knows the broker actually took the message.
> 2. A durable exchange and durable queue, so they survive a broker restart.
> 3. Persistent messages, so they are written to disk and not held only in memory.
> 4. Manual acknowledgement in the consumer, after the work succeeds — not on receipt.
> 5. Limited retries with backoff, then a dead letter queue, so a poison message cannot
>    spin forever.
> 6. An idempotent consumer, because this design is at-least-once and a redelivery must
>    not do the work twice.

Six numbered links, no padding. Markers love it.

---

## Sitting the test — the mechanics that cost people marks

**Attempt everything.** There is rarely negative marking. A blank is guaranteed zero; a
reasoned guess is not.

**Read whether you can go back.** Many platforms lock a section once you leave it. Check
before you move on, not after.

**Budget the time before you start.** If it is 90 minutes with 30 MCQs and two coding
problems: 30 minutes for the MCQs, 25 per problem, 10 spare. Write the clock times down.
When a problem overruns its budget, leave it and come back — a finished brute force scores
more than an elegant half-solution.

**On the coding problems: get something working first.** Write the straightforward version,
make sure it compiles and passes the sample cases, *then* improve it. A working O(n²) beats
a broken O(n). If the platform shows sample tests, run them before you submit.

**State the complexity.** One comment line — `// O(n) time, O(n) space` — on every coding
answer. It costs five seconds and it is frequently part of the rubric.

**If you are stuck on a coding problem, write your approach in a comment.** Partial credit
for a described approach is common. An empty box gets nothing.

**Do not tab-switch if it is proctored.** Many platforms log it and some auto-flag you.
Close everything else before you start.

**Practical checks the morning of:** charged laptop plus charger, a stable connection,
photo ID beside you, webcam working, a quiet room, a pen and paper for working out, and
the test link opened five minutes early rather than one minute late.

---

## 🔴 If Monday is BOTH — and plan as if it is

HR has now said they do not know whether Monday is the written assessment, the technical
interview, **or both**. So plan for both. It is the only version that covers every case,
and it costs you nothing if only one happens.

### How "both" usually runs

Most GCC and vendor pipelines run it as a **filter followed by a conversation, on the same
day**: the written test first, a gap while it is marked, then the interview for whoever
cleared the cut-off. Sometimes the order is reversed, and sometimes the gap is ten minutes
rather than two hours.

**What that means practically:**

- **Block the whole day.** Do not schedule anything after it. Assume 3–4 hours end to end,
  and assume the gap between the two is unpredictable and possibly very short.
- **Stay reachable in the gap.** Phone charged and on, email open. A same-day interview
  invitation often arrives with 15 minutes' notice, and missing it reads as not interested.
- **Eat beforehand, and keep water next to you.** This sounds trivial. It is not — a
  written test plus an interview is a long concentration day, and the interview is the part
  where being tired shows.

### 🔴 The rule that matters most: what you write becomes the interview script

This is the single most important thing in this file, and it is the same lesson as your AI
round. **If both happen on the same day, the interviewer will very likely have your written
answers in front of them.** They are the cheapest possible source of questions, and a panel
will use them.

So two rules while you write:

**1. Never write something you cannot defend out loud an hour later.** If you write
"we used RS256 for token signing", expect *"why RS256 over HS256?"* If you cannot answer
that, write what you actually did — HS256 with a shared secret — and the interview question
becomes one you can answer. An honest, simpler written answer you can defend beats an
impressive one you cannot.

**2. Keep a note of what you wrote.** If the platform allows paper, jot two or three words
per descriptive answer — "lazy/eager: per-query", "Rabbit: 6 links", "second highest:
DENSE_RANK". In the gap, read your own notes. Walking into the interview knowing what the
interviewer just read is a genuine advantage, and it stops you contradicting yourself,
which is the one unrecoverable mistake.

### If the interview comes first instead

Then the written test afterwards is mostly a formality to confirm what you said — and the
same rule applies in reverse. Write answers that match what you just told them. Do not
suddenly produce a more advanced version of a story in writing.

### What to ask HR today

Send one short message. Most recruiters answer this, and every answer narrows your planning:

> "Thanks — just so I can block the time correctly: roughly how long should I keep free on
> Monday, and is the assessment on a platform like HackerRank or Mettl, or written answers?
> And if there is an interview the same day, is it likely to be straight after?"

That is polite, it is practical, and it is the kind of question a recruiter is pleased to
get rather than annoyed by. Even "keep the afternoon free" tells you it is probably both.

**If they still do not know by Sunday, assume both, and assume written first.**

---

## 🔴 "Venue details" — read that word carefully

HR has said you will get a mail tomorrow with **venue details and timing**. That word
matters. Venue means a place, which means **this is almost certainly in person, not a
link**. Treat it as in person until the mail says otherwise.

That single fact resolves most of the uncertainty, and it has consequences.

### What in person changes

**1. A written test at a venue is usually pen and paper, or their machine.** Either way:
no IDE, no autocomplete, no compiler, no Google. Everything in this file that says "write
it by hand" stops being a study technique and becomes the actual exam condition. Do the
SQL and the stream tasks on paper this weekend — not in an editor.

**2. Your handwriting is part of the answer.** A marker who cannot read it does not award
the mark. Write larger than feels natural, leave a blank line between answers, and number
them to match the question paper.

**3. Your phone will probably be deposited at reception.** Most client sites and vendor
offices take phones, especially in BFSI. **So print the cheat sheet.** Four pages, stapled,
in your bag. If it only exists on your phone, you will not have it in the twenty minutes
before you are called in — which is exactly when it is worth the most.

**4. In person usually means more rounds in one visit.** Companies do not bring people to
an office for forty-five minutes. If they are getting you there, expect written plus
technical, and quite possibly an HR or managerial conversation the same day. Skim file 14
before Monday so that round does not catch you cold — especially notice period,
availability, and salary expectation, which you should have a number for before you walk
in, not while you are sitting there.

**5. Dress formals.** The client is a bank. Formal, conservative, comfortable enough to sit
in for several hours.

### 🔴 The mail arrives tomorrow — eleven things to check in it

Do not just note the time. Read it properly and extract these. If any are missing, that is
your reply:

1. **Exact address**, with floor, building and a landmark.
2. **Reporting time versus interview time** — they are often different, and the reporting
   time is the one that binds you.
3. **Contact name and phone number** for the day. Save it in your phone *and* write it on
   paper, because your phone may be at reception.
4. **Expected duration**, which tells you whether it is both rounds.
5. **Format** — written, interview, or both, if they finally say.
6. **Documents to carry** — usually ID, resume copies, sometimes payslips, offer letter or
   education certificates. BFSI clients ask for more than most.
7. **Whether to bring a laptop.**
8. **Entry or security requirements** — some sites need the ID name to match exactly, some
   pre-register visitors a day ahead.
9. **Who you are meeting**, if named. Worth a quick look.
10. **Parking or nearest station**, if you are travelling yourself.
11. **Whether it is JOY IT's office or IBM's.** This is the one most people skip, and it tells
    you who is actually interviewing you. IBM's office means the client panel; JOY's office
    means the vendor is running it, which changes the tone more than the content.

### Reply to that mail the same day

Confirm fast. Vendors chase several candidates for one slot, and a prompt confirmation is
quietly noticed. One short mail covers the confirmation and your remaining questions:

> "Thank you — confirming I will be there on Monday [date] at [reporting time] at [venue].
>
> Two quick questions so I can plan the day: roughly how long should I keep free, and
> should I expect a written assessment, a technical discussion, or both? Also, please let
> me know if there are any documents you would like me to bring apart from my ID and
> resume copies.
>
> Looking forward to it."

Polite, short, and it gets you the format answer you have been missing.

### What goes in the bag on Sunday night

Pack it the night before, not on Monday morning.

- **Printed cheat sheet**, four pages, stapled.
- **Three or four printed copies of your resume.** The panel may not have one.
- **Photo ID**, plus whatever documents the mail asks for.
- **Two pens**, and a plain notepad.
- Passport photos, if asked for.
- Water and something small to eat — a long day with an unpredictable gap.
- The contact number **written on paper**.

### Check the route on Sunday

Look up the journey properly: how long, which route, what time you need to leave to arrive
**twenty to thirty minutes early**. Arriving early is free; arriving flustered costs you
the first ten minutes of the first round, which is where impressions form. If the venue is
far enough to be a real journey, plan for traffic and leave earlier than the map says.

---

## If it turns out to be the interview instead

Then file 00 is your preparation and this file was an hour well spent anyway — every trap
above is also an interview question. Walk in with the eight fixed facts from file 00 and
the ten threads rehearsed.

**And if it is the written test, the interview is still coming**, just a round later. So
nothing you prepare this weekend is wasted; it only changes the order you use it in.

---

## Your weekend — two days, and a 9am start

**The interview is Monday at 9:00 am, in person.** A 9am slot almost always means the written
assessment runs first, so treat this file as the live one.

**Saturday (today)** — file 00 first, then this file: the ten output traps, the five stream
tasks, the six SQL patterns. **Write them by hand, on paper.** Then the core files: 09, 01, 03,
04.

**Sunday 9:00 am** — sit down at the same hour as the exam and write the traps, the streams and
the SQL again from memory, no notes. Whatever comes out wrong is your afternoon.

**Sunday afternoon** — 08, 02, 06, 05, 07, 10, then three coding problems on paper.

**Sunday evening** — the 20-minute drill from file 00, standing up. Then pack the bag, lay the
clothes out, set the alarm, and sleep. Do not cram.

**Monday** — 45 minutes on the printed cheat sheet, eat properly, leave early enough to be at
the venue by 8:30. Learn nothing new.

---

## ✅ Check yourself before moving on

- [ ] I have asked HR the length and platform of Monday's assessment.
- [ ] I can answer all ten output traps without looking.
- [ ] I can write the five stream tasks from memory.
- [ ] I can write the six SQL patterns by hand.
- [ ] I know the four-move shape of a descriptive answer and have written one out.
- [ ] I have a time budget plan and I know to get something working before optimising.
- [ ] ID, charger, quiet room and a working webcam are sorted.
