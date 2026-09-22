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

## 1. The job description, decoded

Service line: **Engineering Services**. Preferred skills: **Core Java** and **Spring Boot**.
This is a build role, and the spec is unusually specific — which is good news, because it
tells you exactly what to revise.

### What it names, and where it is covered

| The JD asks for | Your position | File |
|---|---|---|
| **Core Java (8/11/17+)** | ⚠️ You list Java 8 — know what 11 and 17 added | `01`, `02` |
| **Spring Boot** | ✅ Strong — you built two backends | `03` |
| **Spring MVC** | Know the DispatcherServlet flow | `03`, Q3b |
| **Spring Data JPA, Hibernate** | ✅ Strong | `04` |
| **Spring Security** | ✅ You did RBAC on the card flow | `07` |
| **Microservices architecture** | ⚠️ "Strong understanding" — read Q7, answer honestly | `05` |
| **RESTful APIs** | ✅ Strong — consumed by a 14-screen React frontend | `03`, `11` |
| **SQL: Oracle, MySQL, PostgreSQL, SQL Server** | ✅ PostgreSQL and MySQL. The skills transfer; say so | `08` |
| **Git** | ✅ Git and Bitbucket | `15`, Q8 |
| **Maven or Gradle** | ✅ Maven. Know the lifecycle | `15`, Q7 |
| **JUnit, Mockito** | ⚠️ **Your resume says JUnit, not Mockito.** Close this gap | `15`, Part A |
| **Cloud platforms** (integration) | ⚠️ Docker yes, cloud no. Answer honestly | `12`, `15` Q13 |
| **Code reviews, coding standards** | ✅ You did these | `14` |
| **Agile ceremonies** | ✅ Scrum and Jira — have a line on each ceremony | `15`, Part C |
| **Technical documentation** | ✅ Swagger. And Liquibase for schema | `15`, Q11 |
| **Production deployment support** | ✅ Bamboo CI/CD, SIT/UAT | `15`, Q12 |

### The four gaps, and the pattern for all of them

**Mockito · cloud platforms · Java 11/17 · microservices depth.**

None is disqualifying. The answer pattern is the same every time: **name the boundary, then
show the understanding.**

> "My mocking has been lighter than my JUnit usage, so I would not overstate it — but I
> understand the model: mock the collaborators you do not own, stub with `when/thenReturn`,
> verify interactions." *…then demonstrate it.*

At one to two years that is a strong answer. Claiming depth and then failing the second
question is not — and the second question always comes.

**Mockito is the one to actually fix this week**, not just frame. It is named in the JD, it
takes an hour to learn properly, and it is the cheapest marks available. File 15, Part A.

### Where you are genuinely strong

- **You built the backends**, not just consumed them — Spring Boot, Spring Data JPA and
  PostgreSQL for two applications on a platform used by 10,000+ corporate clients.
- **Real numbers**: card processing time down **60%**, an audit system writing **50,000+
  transactions a day**, 1,000+ monthly reports.
- **Unusual depth for your level** — Camunda BPMN, Spring AOP with `@Aspect`, Liquibase,
  JasperReports, FileNet, Kafka and RabbitMQ. Most candidates at two years have CRUD APIs.
- **The JD's whole responsibilities list is things you have done**: requirements analysis
  with BAs, code reviews, troubleshooting and optimisation, Agile ceremonies, documentation,
  supporting releases.

### And DSA, which you asked about

Infosys almost always includes a coding question, and it is what candidates most often walk
into cold. Set expectations correctly: **arrays, strings, HashMap counting, two pointers,
basic recursion, sorting and searching**, sometimes a linked list or stack. Easy to
lower-medium. **They essentially never ask dynamic programming or graphs** — if you are on DP
on Friday night, stop.

What they check: compiling Java without an IDE, the right collection and why, edge cases,
**stating complexity**, and **thinking out loud**. The last two are free marks most
candidates drop. Files 09 and 10, and every solution in them is compile-tested.

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
| 0:30 | **Spring MVC — the DispatcherServlet flow** 🔴 | `03-spring-boot.md` Q3b |

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
| 1:15 | **JUnit, Mockito, Maven, Agile** 🔴🔴 — the JD names all of it | `15-testing-build-agile.md` |
| 0:45 | **Spring Security and JWT** 🔴 — named in the JD | `07-spring-security-jwt.md` |
| 0:45 | **Delivery and code review** 🔴 | `14-delivery-and-code-review.md` |
| 0:30 | **HR and managerial** 🔴 — say these out loud | `13-hr-and-behavioural.md` |
| 0:45 | **Re-do your five weakest DSA problems from memory** 🔴🔴 | `09`, `10` |
| 0:30 | Skim: messaging, then system design | `06`, `11` |
| — | **Sleep properly.** Do not cram Friday night. | — |

### Saturday morning

45 minutes on `16-final-cheatsheet.md` and nothing else. Then say your intro, the gap answer
and the AOP story out loud, twice. **Learn nothing new.**

### If you fall behind
Drop in this order: system design → messaging → Spring Security → microservices beyond Q7.
**Never drop:** Core Java, Spring Boot, JPA, DSA Part 1, file 12, or **file 15 Part A
(Mockito)** — that last one is named in the JD and missing from your resume.

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
| `07-spring-security-jwt.md` | Authentication, RBAC, JWT — **named in the JD** | 🔴 High |
| `08-sql-and-databases.md` | Joins, indexing, EXPLAIN, optimisation | 🔴 High |
| `09-dsa-arrays-strings.md` | **Patterns, complexity, arrays, strings, hashing** | 🔴 Highest |
| `10-dsa-structures.md` | **Linked lists, stacks, recursion, search, trees** | 🔴 High |
| `11-system-design.md` | Design framework and worked examples | 🟠 Medium |
| `12-your-experience.md` | **Your stories, the gap, "why backend"** | 🔴 Highest |
| `13-hr-and-behavioural.md` | HR round, salary, questions to ask | 🔴 High |
| `14-delivery-and-code-review.md` | Code review, estimation, working with clients | 🔴 High |
| `15-testing-build-agile.md` | **JUnit, Mockito, Maven, Git, Agile ceremonies** | 🔴 Highest |
| `16-final-cheatsheet.md` | One page. Saturday morning only. | 🔴 Read last |

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
