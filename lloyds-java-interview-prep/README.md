# Lloyds — Software Engineer (Java · Spring Boot · Microservices)
### Grade C Software Engineer · Banking domain
### Interview: **today, 17 September, 2:00 PM IST** — Microsoft Teams

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

### 🔴 Two details that change how you should pitch yourself

**1. It is a Grade C Software Engineer role.** Lloyds uses internal grades, and Grade C is an
**early-career engineering grade** — roughly the band for someone with a couple of years, not
a lead or architect. *(I cannot confirm the exact internal mapping, but the level is
consistent with your 1 year 8 months.)*

**This is good news, and it should change your posture.** They are not expecting
architectural ownership or production Kafka. They are expecting solid fundamentals, clear
thinking, honesty about your level, and evidence that you write careful code. **That is
exactly the profile you have.** Stop worrying about the gaps and go and be precise about
what you have done.

**2. It is explicitly the banking domain.** Your Tradu work is financial services —
onboarding, identity verification, payments across multiple vendors. That is KYC and money
movement, which is the same shape of problem a retail bank has.

**Say it in your opening, and use banking language when you describe it:**
> "The platform handled user onboarding and identity verification — effectively KYC — and
> processed transactions through several payment vendors. So a lot of what I worked on was
> money movement and the checks around it, which I imagine maps fairly closely to what you
> do."

**What the banking domain means for your answers all day:** whenever you describe a design or
a fix, add the sentence most candidates never say — **"and here is how we would know
afterwards what happened."** Audit trails, traceable logging, idempotency so a payment is
never taken twice, authorisation enforced server side, never logging sensitive data. That
instinct is the single clearest signal to a bank that you understand their world.

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

## 3. The plan — you have hours, not days

**Interview is at 2:00 PM IST today on Teams.** Work the list below in order and stop when
you run out of time. It is ordered so that if you only get through the first three items you
have still covered the things most likely to decide the outcome.

### Do these in order

| # | What | Minutes | File |
|---|---|---|---|
| **1** | **Your experience + the four honesty answers** — say them **out loud** | 40 | `11-your-experience.md` |
| **2** | **Microservices Q7** — the depth answer. Read it twice. | 15 | `05-microservices.md` |
| **3** | **Core Java and Collections** — HashMap, then the rest | 50 | `01-core-java.md` |
| **4** | **Spring Boot** — DI, annotations, bean scope, exception handling | 40 | `03-spring-boot.md` |
| **5** | **Testing and code review** — your strongest ground | 30 | `13-engineering-practice.md` |
| **6** | **JPA, N+1, `@Transactional`** | 30 | `04-jpa-hibernate.md` |
| **7** | **Behavioural** — the 7 questions, out loud | 25 | `12-behavioural-and-values.md` |
| **8** | **SQL and indexing** | 20 | `08-sql-and-databases.md` |
| **9** | Skim only: REST/security, then Java 8 | 20 | `07`, `02` |

**If you have very little time, do 1, 2 and 3 and nothing else.** Items 1 and 2 are the ones
where an unprepared answer actively costs you; item 3 is the one most likely to be asked.

### The last hour before 2 PM

| When | What |
|---|---|
| **T-60** | **Cheat sheet only.** Nothing new. | `14-final-cheatsheet.md` |
| **T-35** | Say out loud, twice: your intro, the microservices-depth answer, the "why did the role end" answer |
| **T-20** | **Test the Teams link now, not at 1:58.** Camera, microphone, audio. Sign in early. |
| **T-15** | Resume open on screen, notepad and pen, water, phone silent, quiet room, plain background |
| **T-5** | Close every other tab. Sit up. Breathe out slowly. |
| **2:00** | Join. Smile before you speak. |

### Teams specifics
- **Join five minutes early.** If the link fails you want to be emailing the recruiter at
  1:56, not 2:01.
- Have the **meeting ID and passcode** to hand as a fallback in case the link misbehaves.
- Have a **phone hotspot ready** in case your connection drops — and if it does, rejoin and
  carry on; it happens and nobody holds it against you.
- If they ask you to share your screen for coding, **close anything you would not want seen**
  beforehand.

**Learn nothing new after T-60.** It only displaces what has settled and raises your anxiety.

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
