# Infosys — Java Backend Developer Interview Prep
### For Neelima Jana · Interview: 5 September · Plan starts 2 September

---

## How this guide is written

Every topic follows the same four steps, so you always know what you are reading:

1. **The context** — what the thing is and what problem it solves, in plain words.
2. **A simple example** — small code you can actually follow.
3. **Why it matters** — where it is used in real work.
4. **"Say this"** — the answer to give in the room.

Do not memorise the answers. Understand the idea, so that when the question comes
out slightly differently, you can still answer it.

---

## 1. What the job description is really telling you

The posting is an Infosys "Infoscion" template, so most of it describes how Infosys
works rather than the role itself. The part that actually decides your interview is
near the bottom:

> **Primary skills: Java → Spring Boot. Technology → Microservices.**
> **Preferred: Microservices API Management, Java → Spring Boot.**

That is the whole technical brief. **Java, Spring Boot and Microservices.** Files 01
to 06 cover those, and they are where you should spend most of your three days.

But do not skip the rest of the posting, because it tells you what the **managerial
round** will be about:

| The JD says | What it means for you |
|---|---|
| "problem definition, effort estimation, diagnosis, solution generation" | They want to see structured thinking, not just coding. **File 10.** |
| "research… literature surveys… vendor evaluation… build POCs" | Learning agility. Be ready for "how do you learn a new technology?" |
| "create requirement specifications… define to-be processes" | You will be asked how you handle unclear requirements. **File 12.** |
| "diagnose the root cause of issues, seek clarifications" | Your production-incident story is directly relevant. **File 11.** |
| "work with clients… refining, analyzing, structuring relevant data" | Client communication. **This is where your recruitment background helps you.** |
| "assess current processes, identify improvement areas" | Your two performance-optimisation stories are exactly this. |
| "one or two industry domain knowledge" | You have **banking**. Say so early and often. |

### The two things that make you a strong fit

**1. You have real performance numbers.** 15 seconds to 6 seconds. 2–3 seconds to
under 1 second. Most candidates at this level say "I optimised the API." You can say
what was wrong (N+1 queries), what you did (indexing, lazy loading, refactored
JOINs), and what changed. That is rare, and Infosys interviewers dig for exactly
this.

**2. You have banking domain experience.** The JD explicitly asks for "one or two
industry domain knowledge". You worked on a UK private bank's transaction recall and
card management systems. Infosys staffs by domain, so this makes you easier to place,
and easier to place means easier to hire.

---

## 2. What the interview will look like

Infosys typically runs **two or three rounds**, often on the same day.

**Round 1 — Technical (45–60 min).**
Core Java, Collections, Java 8, Spring Boot, Hibernate/JPA, SQL, and usually one
coding question. Expect rapid-fire questions rather than long discussions.
→ Files 01, 02, 03, 04, 08, 09.

**Round 2 — Technical / Architecture (30–45 min).**
Microservices, messaging, security, design questions, and a deep dive into your
projects. This is where your Kafka and RabbitMQ work stands out.
→ Files 05, 06, 07, 10, 11.

**Round 3 — Managerial + HR (20–30 min).**
Behavioural questions, the JD's consulting language, your career change, notice
period, location, salary.
→ File 12.

> **A note on Infosys specifically.** They are a large services company, so the
> technical bar is "solid and reliable" rather than "brilliant". They screen hard for
> **fundamentals** (Core Java and Collections especially), **communication**, and
> **whether you will be easy to deploy to a client**. Depth on HashMap internals will
> serve you better here than a clever algorithm.

---

## 3. The three-day plan

### Day 1 — Tuesday 2 September (today, from now)
*Goal: the fundamentals they screen hardest on.*

| Block | Topic | File |
|---|---|---|
| 0:00 – 0:15 | Read this file | `README.md` |
| 0:15 – 2:00 | **Core Java and Collections** 🔴🔴 | `01-core-java.md` |
| 2:00 – 3:00 | **Java 8 — streams, lambdas, Optional** 🔴 | `02-java8-functional.md` |
| 3:00 – 3:15 | Break | — |
| 3:15 – 4:45 | **Spring Boot and dependency injection** 🔴🔴 | `03-spring-boot.md` |
| 4:45 – 6:00 | **JPA, Hibernate and the N+1 problem** 🔴🔴 | `04-jpa-hibernate.md` |
| Evening | Say your two performance stories out loud | `11-your-experience.md` §2 |

### Day 2 — Wednesday 3 September
*Goal: the primary skill on the JD, plus your differentiators.*

| Block | Topic | File |
|---|---|---|
| 0:00 – 1:30 | **Microservices** 🔴🔴 | `05-microservices.md` |
| 1:30 – 2:30 | **Kafka and RabbitMQ** 🔴 | `06-kafka-rabbitmq.md` |
| 2:30 – 3:15 | **Spring Security and JWT** 🔴 | `07-spring-security-jwt.md` |
| 3:15 – 4:30 | **SQL and query optimisation** 🔴 | `08-sql-and-databases.md` |
| 4:30 – 6:00 | **Coding round practice — write the code, do not read it** | `09-coding-round.md` |
| Evening | **Your experience and the career change** 🔴 | `11-your-experience.md` |

### Day 3 — Thursday 4 September
*Goal: consolidate, and prepare the non-technical half.*

| Block | Topic | File |
|---|---|---|
| 0:00 – 1:15 | **Backend system design** 🔴 | `10-system-design.md` |
| 1:15 – 2:15 | **HR and managerial round** 🔴 | `12-hr-and-behavioural.md` |
| 2:15 – 3:30 | Re-do the coding problems you got wrong | `09-coding-round.md` |
| 3:30 – 4:30 | Weak areas from days 1 and 2 — your call | — |
| 4:30 – 5:00 | Say your intro and project pitches out loud, twice | `11-your-experience.md` |
| By 11:00 PM | **Sleep.** | — |

### Day 4 — Friday 5 September, interview day

| Time | What |
|---|---|
| Wake, then 45 min | **Cheat sheet only** — `13-final-cheatsheet.md` |
| 30 min | Say your intro, the career-change answer and both project stories out loud |
| 20 min | Re-read the questions you will ask them |
| 20 min | Laptop, charger, network, ID, printed resumes, water |
| Before | Close everything. Breathe. |

**Learn nothing new on interview day.** New material only pushes out what has already
settled and raises your anxiety. Revision only.

---

## 4. The files

| File | Topic | Priority |
|---|---|---|
| `01-core-java.md` | OOP, Collections, HashMap internals, String, exceptions | 🔴 Highest |
| `02-java8-functional.md` | Streams, lambdas, functional interfaces, Optional | 🔴 High |
| `03-spring-boot.md` | IoC, DI, annotations, bean scopes, auto-configuration | 🔴 Highest |
| `04-jpa-hibernate.md` | JPA, lazy vs eager, **N+1**, transactions, caching | 🔴 Highest |
| `05-microservices.md` | Patterns, Eureka, API Gateway, resilience, saga | 🔴 Highest |
| `06-kafka-rabbitmq.md` | Messaging, when to use which — your differentiator | 🔴 High |
| `07-spring-security-jwt.md` | Authentication, RBAC, JWT flow | 🟠 Medium |
| `08-sql-and-databases.md` | Joins, indexing, execution plans, optimisation | 🔴 High |
| `09-coding-round.md` | Coding problems with full solutions | 🔴 High |
| `10-system-design.md` | Backend design questions and a framework | 🟠 Medium |
| `11-your-experience.md` | Your stories, and the two hard resume questions | 🔴 Highest |
| `12-hr-and-behavioural.md` | Infosys HR, the career change, salary, questions to ask | 🔴 High |
| `13-final-cheatsheet.md` | One page. Interview morning only. | 🔴 Read last |

PDF versions are in `pdf/`. The cheat sheet is meant to be printed.

---

## 5. Three rules for the room

**1. Never say "I don't know" and stop.** Say instead:
> "I have not used that directly. My understanding is that it does X — is that the
> direction you mean?"

Service company interviewers are checking whether you can reason and whether you will
admit a gap honestly. Both matter more than knowing everything.

**2. Always give the *why*, not just the *what*.**
"HashMap stores key-value pairs" is a textbook answer. "HashMap gives O(1) lookup
because it hashes the key to a bucket index instead of scanning" is an engineer's
answer. Same length, completely different impression.

**3. Bring every answer back to something you actually did.**
You have banking projects with real numbers. When you explain the N+1 problem, finish
with "that is exactly what took our report generation from 15 seconds to 6." That is
the sentence they remember.

---

## 6. Two things on your resume to sort out before the 5th

Read **file 11, section 5** properly. There are two items that a careful interviewer
will ask about, and Infosys runs formal background verification, so both need a clear
and honest answer ready:

1. Your summary says **"2+ years"**, but Dec 2024 to Sept 2026 is about **21 months**.
2. The move from **Talent Acquisition Executive** to **Software Engineer**.

Neither is a problem. Both are a problem if you are caught unprepared by them.
