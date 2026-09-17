# Lloyds — Software Engineer (Java · Spring Boot · Microservices)
### Interview prep for Vallu Ravikoti Narendra

---

## How this guide is written

Every topic follows the same four steps:

1. **The context** — what the thing is and what problem it solves, in plain words.
2. **A simple example** — small code you can actually follow.
3. **Why it matters** — where it is used in real work.
4. **"Say this"** — the answer to give in the room.

**Every question in this guide has a written answer** in the words you would say, and most
carry a **real-world example**. The examples are anchored to a **trading and payments
platform**, because that is what you worked on — so the analogy you reach for in the room is
one you actually understand.

Do not memorise them word for word. Learn the shape, so when the question comes out
slightly differently you can still answer it.

---

## 1. Who you are interviewing with

**Lloyds Banking Group** is the UK's largest retail and commercial banking group — Lloyds
Bank, Halifax, Bank of Scotland and Scottish Widows. They are several years into a large
technology transformation, moving off legacy systems towards cloud-hosted, API-driven
services, and they have built a substantial engineering organisation in India through the
**Lloyds Technology Centre in Hyderabad**. If you are interviewing in India, that is almost
certainly the entity.

**What that means for you, practically:**

- **It is a regulated bank.** Security, auditability, data privacy and change control are
  not optional extras — they are the job. An answer that includes "and here is how we would
  know afterwards what happened" lands better here than almost anywhere else.
- **It is a product and platform organisation, not a services company.** They are hiring
  someone to own and run a service over time, not to be deployed to whichever client needs a
  body. Answers about maintainability, testing and observability carry real weight.
- **Your domain transfers.** Tradu is a trading platform with onboarding, identity
  verification and payments across multiple vendors. That is financial services, with KYC
  and money movement. **Say that early** — domain familiarity is worth a lot to a bank.

> ⚠️ **Verify the format with your recruiter.** What follows is my prediction based on how
> this kind of role is usually run, not something I can confirm for your specific process.
> It is a completely normal thing to ask: *"Could you tell me what the rounds look like and
> what each one focuses on?"* Most recruiters answer that happily, and it costs you nothing.

---

## 2. What the interview will probably look like

**Round 1 — Technical (45–60 min).**
Core Java, collections, Spring Boot, REST, Hibernate/JPA, SQL. Usually one coding question.
→ Files 01, 02, 03, 04, 08, 09.

**Round 2 — Technical / design (45–60 min).**
Microservices and how services communicate and fail, API design, security, testing, and a
deep dive into what you actually built.
→ Files 05, 06, 07, 10, 11, 13.

**Round 3 — Behavioural and values (30–45 min).**
How you work, how you handle disagreement and mistakes, how you approach quality and risk.
UK banks typically run this as a structured competency interview with prepared questions,
so **prepared examples matter more here than in a typical Indian services interview.**
→ File 12.

### The three things that decide this interview for you

**1. Honest calibration.** You have 1 year 8 months. Nobody expects architecture ownership.
They expect solid fundamentals, clear thinking, and no overclaiming. **The single fastest
way to lose this is to claim depth you do not have** — file 05, Q7 and file 11 handle the
two places where your resume invites that.

**2. Fundamentals, cleanly explained.** Collections, Spring Boot, JPA and SQL, explained
with the *why*, not just the *what*. That is what a 2-year hire is actually assessed on.

**3. Quality practice.** JUnit 5, Mockito, SonarQube, code review, logging, root cause
analysis — all on your resume, and all things a regulated bank genuinely values. **File 13
is the one most candidates at your level have nothing prepared for**, and it is where you
can look better than your years.

---

## 3. The plan

I do not know your interview date. Below is a **two-day plan**; if you have only one day,
use the compressed version underneath.

### Day 1 — fundamentals

| Block | Topic | File |
|---|---|---|
| 0:00 – 0:15 | Read this file | `README.md` |
| 0:15 – 2:00 | **Core Java and Collections** 🔴🔴 — HashMap above all | `01-core-java.md` |
| 2:00 – 3:00 | **Java 8 — streams, lambdas, Optional** 🔴 | `02-java8-functional.md` |
| 3:00 – 3:15 | Break | — |
| 3:15 – 4:45 | **Spring Boot** 🔴🔴 | `03-spring-boot.md` |
| 4:45 – 6:00 | **JPA, Hibernate and N+1** 🔴🔴 | `04-jpa-hibernate.md` |
| Evening | **Your experience** — fill in the templates, say them out loud | `11-your-experience.md` |

### Day 2 — the rest, and the parts about you

| Block | Topic | File |
|---|---|---|
| 0:00 – 1:15 | **Microservices** 🔴🔴 — especially Q7, the honest answer | `05-microservices.md` |
| 1:15 – 2:00 | **REST, Spring Security and JWT** 🔴 | `07-spring-security-jwt.md` |
| 2:00 – 2:45 | **SQL and indexing** 🔴 | `08-sql-and-databases.md` |
| 2:45 – 3:00 | Break | — |
| 3:00 – 4:00 | **Testing, code review and engineering practice** 🔴🔴 | `13-engineering-practice.md` |
| 4:00 – 5:00 | **Coding round** — type the problems, do not read them | `09-coding-round.md` |
| 5:00 – 5:45 | **Behavioural and values** 🔴 — say these out loud | `12-behavioural-and-values.md` |
| 5:45 – 6:15 | Skim: messaging, then system design | `06`, `10` |

### Interview day

| Time | What |
|---|---|
| 45 min | **Cheat sheet only.** Nothing new. | `14-final-cheatsheet.md` |
| 30 min | Say out loud, twice: your intro, the microservices-depth answer, two project stories |
| 20 min | Re-read the questions you will ask them |
| 20 min | Laptop, charger, network, ID, printed resume, water |

**Learn nothing new on the day.** It only displaces what has settled and raises your anxiety.

### If you only have one day

Do, in this order, and stop when you run out: **01 Core Java → 03 Spring Boot → 11 your
experience → 05 microservices (Q7 especially) → 13 engineering practice → 04 JPA → 14 cheat
sheet.** Skip 02, 06, 08, 09 and 10 entirely if you must.

**Never skip:** Core Java, Spring Boot, file 11, and file 05 Q7.

---

## 4. The files

| File | Topic | Priority |
|---|---|---|
| `01-core-java.md` | OOP, Collections, HashMap internals, String, exceptions | 🔴 Highest |
| `02-java8-functional.md` | Streams, lambdas, functional interfaces, Optional | 🔴 High |
| `03-spring-boot.md` | IoC, DI, annotations, bean scopes, auto-configuration | 🔴 Highest |
| `04-jpa-hibernate.md` | JPA, lazy vs eager, **N+1**, transactions, caching | 🔴 High |
| `05-microservices.md` | Patterns, communication, resilience — **read Q7** | 🔴 Highest |
| `06-kafka-rabbitmq.md` | Messaging — you have fundamentals only, answer accordingly | 🟠 Medium |
| `07-spring-security-jwt.md` | Authentication, authorisation, JWT, API security | 🔴 High |
| `08-sql-and-databases.md` | Joins, indexing, EXPLAIN, optimisation | 🔴 High |
| `09-coding-round.md` | Coding problems with full solutions | 🔴 High |
| `10-system-design.md` | Design framework and worked examples | 🟠 Medium |
| `11-your-experience.md` | **Your Tradu stories, and the four honesty questions** | 🔴 Highest |
| `12-behavioural-and-values.md` | Competency round, questions to ask, logistics | 🔴 High |
| `13-engineering-practice.md` | **Testing, Mockito, code review, SonarQube, CI/CD** | 🔴 Highest |
| `14-final-cheatsheet.md` | One page. Interview morning only. | 🔴 Read last |

---

## 5. Three rules for the room

**1. Never say "I don't know" and stop.** Say instead:
> "I have not used that directly. My understanding is that it does X — is that the direction
> you mean?"

**2. Give the *why*, not just the *what*.** "HashMap stores key-value pairs" is a textbook
answer. "It gives O(1) lookup because it hashes the key to a bucket instead of scanning" is
an engineer's answer. Same length, completely different impression.

**3. Name your level before they have to ask.** You are 1 year 8 months in. Saying "here is
what I have done, and here is where my depth ends" early makes everything else you say more
credible. It is the opposite of a weakness in an interviewer's eyes.
