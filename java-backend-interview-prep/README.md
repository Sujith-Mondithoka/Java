# Infosys — Java Backend Developer Interview Prep
### For Neelima Jana · Interview: **tomorrow, 5 September, 4:00 PM**

---

## How this guide is written

Every topic follows the same four steps, so you always know what you are reading:

1. **The context** — what the thing is and what problem it solves, in plain words.
2. **A simple example** — small code you can actually follow.
3. **Why it matters** — where it is used in real work.
4. **"Say this"** — the answer to give in the room.

**Every one of the 71 questions in this guide has a written answer** in the words you
would actually say, and most carry a **real-time example** from the banking systems you
worked on. That is deliberate: at this level, "give me a real-time example" is asked as a
question in its own right, and a banking example from your own project beats a textbook
one every time.

Do not memorise them word for word. Learn the shape, so when the question comes out
slightly differently you can still answer it.

---

## 1. What the job description is really telling you

Read the posting again carefully, because it says two things that change how you prepare.

### The only technology listed is Java and Spring Boot

> **Primary skills: Technology → Java → Springboot**
> **Preferred Skills: Technology → Java → Springboot**

That is the entire technical brief. Not microservices, not cloud, not a messaging platform.
**Core Java, Spring Boot, and the data layer underneath them** are what the technical round
will test, and that is where most of your time should go.

Microservices, Kafka and RabbitMQ are still worth knowing — they are on your resume, so you
will be asked about them, and the JD does say "validate the architecture" — but they are
supporting material here, not the main event.

### Almost everything else in the posting is about how you deliver

> *"interface with the client for quality assurance, issue resolution and ensuring high
> customer satisfaction… understand requirements, create and review designs, validate the
> architecture… participate in project estimation, provide inputs for solution delivery,
> conduct technical risk planning, perform code reviews and unit test plan reviews… lead
> and guide your teams towards developing optimized high quality code deliverables,
> continual knowledge management and adherence to the organizational guidelines and
> processes."*

| The JD says | What it means for you |
|---|---|
| "interface with the client for quality assurance, issue resolution" | Your production-incident and QA coordination experience. **File 13.** |
| "understand requirements… create and review designs" | How you handle unclear requirements, and what you check in a design. **File 13.** |
| "validate the architecture" | Your Classifieds project, and being able to state a design's **cost** as well as its benefit. **Files 05 and 13.** |
| "project estimation… technical risk planning" | Two questions most candidates have nothing prepared for. **File 13.** |
| "code reviews and unit test plan reviews" | Named explicitly. Your resume says you did both. **File 13.** |
| "lead and guide your teams" | Answer honestly at your level — do not claim to have led a team. **File 13, Q7.** |
| "knowledge management… adherence to processes" | Swagger docs, runbooks, and your SIT/UAT release process. **File 13.** |

**This is not a pure coding role.** It is Infosys's analyst-shaped template: someone who can
be put in front of a client, review other people's work, and be trusted to follow process.
There will be a second conversation about all of the above, and most candidates arrive with
nothing ready for it. **File 13 is your edge here** — and your resume already contains
evidence for nearly every line of it.

### The three things that make you a strong fit

**1. You have real numbers.** 15 seconds to 6 seconds. 2–3 seconds to under 1 second. Most
candidates say "I optimised the API." You can say what was wrong, what you changed, and what
it became.

**2. You have banking domain experience.** A UK private bank's transaction recall and card
management systems. Infosys staffs by domain, and easier to place means easier to hire.

**3. You have done the delivery work this JD asks about** — code reviews, QA coordination,
requirement analysis, production incident resolution, deployment validation. It is all on
your resume. You just need to describe it as ownership rather than participation.

---

## 2. What the interview will look like

Infosys typically runs **two or three rounds**, often on the same day.

**Round 1 — Technical (45–60 min).**
Core Java, Collections, Java 8, Spring Boot, Hibernate/JPA, SQL, and usually one
coding question. Expect rapid-fire questions rather than long discussions.
→ Files 01, 02, 03, 04, 08, 09.

**Round 2 — Technical / Delivery (30–45 min).**
A deep dive into your projects, plus the delivery half of the JD: code review, test plan
review, estimation, risk planning, and how you work with a client. Messaging and
microservices come up here because they are on your resume.
→ Files 11, 13, then 05, 06, 07, 10.

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

## 3. The plan — tonight and tomorrow morning

You have this evening and tomorrow until about 3 PM. That is roughly **ten working
hours**, so this is ordered strictly by what the interview is most likely to test.

**If you fall behind, drop from the bottom. Never from the top.**

### Tonight — 4 September

| Time | Topic | File |
|---|---|---|
| **6:00 – 6:15** | Read this file | `README.md` |
| **6:15 – 7:45** | **Core Java and Collections** 🔴🔴 — HashMap above all | `01-core-java.md` |
| **7:45 – 8:45** | **Spring Boot** 🔴🔴 | `03-spring-boot.md` |
| **8:45 – 9:15** | Dinner. Actually eat. | — |
| **9:15 – 10:15** | **JPA, Hibernate and N+1** 🔴🔴 — your own story | `04-jpa-hibernate.md` |
| **10:15 – 10:45** | **Your experience** 🔴🔴 — say it out loud, do not just read | `11-your-experience.md` |
| **10:45 – 11:15** | **Delivery and code review** 🔴🔴 — the JD's other half | `13-delivery-and-code-review.md` |
| **By 11:30 PM** | **Sleep.** Non-negotiable. | — |

> **Do not study past midnight.** A tired candidate blanks on things they knew perfectly
> at 1 AM. The 4 PM slot is late enough that being rested matters more than one extra hour
> tonight.

### Tomorrow morning — 5 September

| Time | Topic | File |
|---|---|---|
| **8:00 – 8:45** | **Delivery and code review** 🔴🔴 — finish it properly, out loud | `13-delivery-and-code-review.md` |
| **8:45 – 9:30** | **Java 8 — streams, lambdas, Optional** 🔴 | `02-java8-functional.md` |
| **9:30 – 10:15** | **SQL and indexing** 🔴 | `08-sql-and-databases.md` |
| **10:15 – 11:00** | **Coding round** — type three problems, do not read them | `09-coding-round.md` |
| **11:00 – 11:30** | Break. Get away from the screen. | — |
| **11:30 – 12:15** | **Microservices** 🟠 — on your resume, so expect questions | `05-microservices.md` |
| **12:15 – 12:45** | **Kafka and RabbitMQ** 🟠 — your differentiator | `06-kafka-rabbitmq.md` |
| **12:45 – 13:30** | **HR and managerial** 🔴 — say these out loud | `12-hr-and-behavioural.md` |
| **13:30 – 14:00** | Skim only: Security, then System design | `07`, `10` |

### Tomorrow afternoon — the last two hours

| Time | What |
|---|---|
| **14:00 – 14:45** | **Cheat sheet only.** Nothing new. | `14-final-cheatsheet.md` |
| **14:45 – 15:15** | Say **out loud, twice**: your intro, the career-change answer, the 15s→6s story |
| **15:15 – 15:40** | Laptop, charger, network, ID, printed resumes, water, documents |
| **15:40 – 15:55** | Close every file. Sit up. Breathe. |
| **16:00** | **Go.** |

### If you run out of time

Drop in this order, from the first thing to sacrifice:

1. System design (file 10) — skim the six-step framework only
2. Spring Security (file 07) — learn the JWT structure and the RBAC story
3. Microservices and messaging (files 05, 06) — know your own project and the Kafka
   versus RabbitMQ answer; skip the rest
4. Coding round (file 09) — do problems 1, 3 and 4 only

**Never drop:** Core Java, Spring Boot, JPA and N+1, your own experience, or file 13.
Those five are the interview, because Java and Spring Boot are the only technologies the
JD names and everything else in it is about delivery.

---

## 4. The files

| File | Topic | Priority |
|---|---|---|
| `01-core-java.md` | OOP, Collections, HashMap internals, String, exceptions | 🔴 Highest |
| `02-java8-functional.md` | Streams, lambdas, functional interfaces, Optional | 🔴 High |
| `03-spring-boot.md` | IoC, DI, annotations, bean scopes, auto-configuration | 🔴 Highest |
| `04-jpa-hibernate.md` | JPA, lazy vs eager, **N+1**, transactions, caching | 🔴 Highest |
| `05-microservices.md` | Patterns, Eureka, API Gateway, resilience, saga | 🟠 Medium |
| `06-kafka-rabbitmq.md` | Messaging, when to use which — your differentiator | 🟠 Medium |
| `07-spring-security-jwt.md` | Authentication, RBAC, JWT flow | 🟠 Medium |
| `08-sql-and-databases.md` | Joins, indexing, execution plans, optimisation | 🔴 High |
| `09-coding-round.md` | Coding problems with full solutions | 🔴 High |
| `10-system-design.md` | Backend design questions and a framework | 🟠 Medium |
| `11-your-experience.md` | Your stories, and the two hard resume questions | 🔴 Highest |
| `12-hr-and-behavioural.md` | Infosys HR, salary, questions to ask | 🔴 High |
| `13-delivery-and-code-review.md` | **Code review, test plan review, estimation, risk, clients** | 🔴 Highest |
| `14-final-cheatsheet.md` | One page. Interview morning only. | 🔴 Read last |

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

Neither is a problem. Both are a problem if you are caught unprepared by them, and you
have one evening to decide how you will answer each. Do that tonight, not tomorrow.
