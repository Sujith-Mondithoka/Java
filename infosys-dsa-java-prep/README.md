# Infosys — Java, Spring Boot and DSA Prep
### For Sujith Mondithoka · Interview: **Saturday 26 September** · 4 days from today

---

## How this guide is written

Every topic follows the same four steps:

1. **The context** — what it is and what problem it solves, in plain words.
2. **A simple example** — small code you can follow.
3. **Why it matters** — where it is used in real work.
4. **"Say this"** — the answer to give in the room.

**Every question has a written answer** in the words you would say, and most carry a
**real-world example** anchored to the enterprise banking platform you actually worked on.

Do not memorise them word for word. Learn the shape, so that when the question comes out
slightly differently you can still answer it.

---

## 1. What you are preparing for

**Java and Spring Boot** is the brief, and you have asked to cover **DSA** alongside it.
That is the right instinct — Infosys almost always includes a coding question, and it is the
part candidates most often walk into cold.

### Set your DSA expectations correctly

This matters, because over-preparing the wrong thing is the classic way to waste four days.

**What Infosys asks:** arrays, strings, HashMap-based counting, two pointers, basic
recursion, sorting and searching, sometimes a linked list or a stack. Usually **one or two
problems**, at easy to lower-medium difficulty.

**What they almost never ask:** dynamic programming, graphs, tries. **If you find yourself
on DP on Friday night, stop.**

**What they are really checking:** can you write compiling Java without an IDE, do you pick
the right collection and know why, do you handle edge cases, can you state complexity, and
do you talk while you think. The last two are free marks that most people drop.

### Your position

You are strong here, and you should go in knowing it:

- **You built real backends** — Spring Boot, Spring Data JPA and PostgreSQL for two
  applications on a platform used by 10,000+ corporate clients.
- **You have numbers**: card processing time down **60%**, an audit system writing
  **50,000+ transactions a day**, 1,000+ monthly reports.
- **You have unusual depth for your level** — Camunda BPMN, Spring AOP with `@Aspect`,
  Liquibase, JasperReports, FileNet, Kafka and RabbitMQ. Most candidates at two years have
  CRUD APIs and nothing else.

**Two things to prepare rather than hope about**, both in file 12:
1. **You left in February.** That is roughly seven months, and it is the first thing an
   interviewer will notice. Rehearse this more than any technical answer.
2. **"Why backend, when your GitHub looks frontend?"** You need a clean answer.

---

## 2. What the interview will probably look like

**Round 1 — Technical (45–60 min).** Core Java, collections, Java 8, Spring Boot, JPA, SQL,
plus a coding question. → Files 01–04, 08, 09, 10.

**Round 2 — Technical / project (30–45 min).** A deep dive into what you built, plus
microservices, messaging and design. → Files 05, 06, 11, 12.

**Round 3 — Managerial and HR (20–30 min).** Delivery process, behaviour, the gap, salary,
location. → Files 13, 14.

> ⚠️ This is my prediction from how these interviews usually run, not something I can confirm.
> Ask your recruiter what the rounds are — it is a normal question and it costs nothing.

---

## 3. The four-day plan

### Tuesday (today) — Java fundamentals
*The thing they screen hardest on.*

| Block | Topic | File |
|---|---|---|
| 0:15 | Read this file | `README.md` |
| 1:45 | **Core Java and Collections** 🔴🔴 — HashMap above all | `01-core-java.md` |
| 1:00 | **Java 8 — streams, lambdas, Optional** 🔴 | `02-java8-functional.md` |
| 0:45 | **DSA: complexity table + the hashing pattern** 🔴🔴 — type them | `09-dsa-arrays-strings.md` |

### Wednesday — Spring Boot and the data layer

| Block | Topic | File |
|---|---|---|
| 1:30 | **Spring Boot** 🔴🔴 — DI, annotations, bean scope, `@ControllerAdvice` | `03-spring-boot.md` |
| 1:15 | **JPA, Hibernate, N+1, `@Transactional`** 🔴🔴 | `04-jpa-hibernate.md` |
| 1:00 | **SQL and indexing** 🔴 | `08-sql-and-databases.md` |
| 0:45 | **DSA: two pointers + sliding window** 🔴 — type them | `09-dsa-arrays-strings.md` |

### Thursday — DSA day, and your stories

| Block | Topic | File |
|---|---|---|
| 1:30 | **DSA Part 1, finish and re-do the ones you got wrong** 🔴🔴 | `09-dsa-arrays-strings.md` |
| 1:30 | **DSA Part 2 — linked lists, stacks, recursion, binary search** 🔴 | `10-dsa-structures.md` |
| 1:00 | **Your experience** 🔴🔴 — the AOP story, the gap, "why backend" | `12-your-experience.md` |
| 0:45 | **Microservices** 🟠 — especially Q7, the honest answer | `05-microservices.md` |

### Friday — the rest, and rehearsal

| Block | Topic | File |
|---|---|---|
| 1:00 | **Delivery and code review** 🔴 | `14-delivery-and-code-review.md` |
| 0:45 | **HR and managerial** 🔴 — say these out loud | `13-hr-and-behavioural.md` |
| 0:45 | **Spring Security and JWT** 🟠 | `07-spring-security-jwt.md` |
| 0:45 | **Re-do your five weakest DSA problems from memory** 🔴🔴 | `09`, `10` |
| 0:30 | Skim: messaging, then system design | `06`, `11` |
| — | **Sleep properly.** Do not cram Friday night. | — |

### Saturday morning

45 minutes on `15-final-cheatsheet.md` and nothing else. Then say your intro, the gap answer
and the AOP story out loud, twice. **Learn nothing new.**

### If you fall behind
Drop in this order: system design → messaging → Spring Security → microservices beyond Q7.
**Never drop:** Core Java, Spring Boot, JPA, DSA Part 1, or file 12.

---

## 4. The files

| File | Topic | Priority |
|---|---|---|
| `01-core-java.md` | OOP, Collections, HashMap internals, String, exceptions | 🔴 Highest |
| `02-java8-functional.md` | Streams, lambdas, functional interfaces, Optional | 🔴 High |
| `03-spring-boot.md` | IoC, DI, annotations, bean scopes, auto-configuration | 🔴 Highest |
| `04-jpa-hibernate.md` | JPA, lazy vs eager, **N+1**, transactions, caching | 🔴 Highest |
| `05-microservices.md` | Patterns, resilience, saga — **read Q7** | 🟠 Medium |
| `06-kafka-rabbitmq.md` | Messaging, queue vs event log | 🟠 Medium |
| `07-spring-security-jwt.md` | Authentication, RBAC, JWT | 🟠 Medium |
| `08-sql-and-databases.md` | Joins, indexing, EXPLAIN, optimisation | 🔴 High |
| `09-dsa-arrays-strings.md` | **Patterns, complexity, arrays, strings, hashing** | 🔴 Highest |
| `10-dsa-structures.md` | **Linked lists, stacks, recursion, search, trees** | 🔴 High |
| `11-system-design.md` | Design framework and worked examples | 🟠 Medium |
| `12-your-experience.md` | **Your stories, the gap, "why backend"** | 🔴 Highest |
| `13-hr-and-behavioural.md` | HR round, salary, questions to ask | 🔴 High |
| `14-delivery-and-code-review.md` | Code review, estimation, working with clients | 🔴 High |
| `15-final-cheatsheet.md` | One page. Saturday morning only. | 🔴 Read last |

---

## 5. Three rules for the room

**1. In the coding round, keep talking.** Silence reads as stuck. Narrate: *"I'll count with
a HashMap so the lookup is O(1), then find the first with a count of one."*

**2. Always say the brute force first, with its cost.** *"Two nested loops is O(n²) — I can
do better with a map."* Then improve it. Jumping straight to a memorised optimal solution
shows nothing.

**3. Give the why, not just the what.** "HashMap stores key-value pairs" is a textbook
answer. "It gives O(1) lookup because it hashes the key to a bucket instead of scanning" is
an engineer's answer. Same length, completely different impression.
