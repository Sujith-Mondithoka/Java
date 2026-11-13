# IBM — Java Backend Developer
### Neelima Jana · Client **IBM**, payroll **JOY IT** · Hyderabad · F2F **Monday 16 / Tuesday 17 November**

---

## How this guide is written

Every topic follows the same four steps:

1. **The context** — what it is and what problem it solves, in plain words.
2. **A simple example** — small code you can follow.
3. **Why it matters** — where it is used in real work.
4. **"Say this"** — the answer to give in the room.

**Every question has a written answer** in the words you would say, and most carry a
**real-world example** anchored to the banking platform you actually worked on. Learn the
shape, not the wording.

---

## 1. Who you are interviewing with

| | |
|---|---|
| **Client** — where you would sit and work | **IBM** |
| **Payroll** — who employs you and pays you | **JOY IT** (JOY IT Solutions / JOY IT Consulting) |
| **Employment type** | Full-time with JOY |
| **Location** | Hyderabad |
| **Recruiter** | Prasanthi P, JOY IT |
| **Mode** | AI interview (**done — you passed at 69%**), then F2F Monday/Tuesday |

This is a standard staffing arrangement: **JOY IT is your employer, IBM is the client.** It is
the same shape as your current position — Zensar employs you, C. Hoare & Co is the client. Say
that out loud if it comes up, because it means the model is already familiar to you and you
have worked successfully inside it for eighteen months. That reassures a vendor recruiter more
than anything else you can say, because their real fear is a candidate who accepts and then
backs out over the payroll question.

**What it means for Monday:** JOY has already screened you with the AI round, and a vendor does
not usually run a second technical round of its own. So the F2F is most likely **IBM's
technical panel** — prepare to impress the client. Expect IBM-style questions: fundamentals,
depth on what you actually built, and clean reasoning rather than buzzwords.

**Note the mode line: "F2F — Monday, Tuesday."** Two days. That may mean candidates spread
across both days, or more than one round for you. **Do not assume Monday is the end of it** —
keep Tuesday as free as you can.

> 🔴 **Payroll, contract length, conversion to IBM, appraisals and benefits are real questions —
> and none of them belong in the technical round.** Keep them for Prasanthi, on the phone,
> before you accept anything. The full list is in **file 14, section 6b**.

---

## 2. The JD, decoded against your resume

This is the spec you are being interviewed against. Ten responsibilities and twelve required
skills. Here is where you stand on every line of it.

### What they will ask you to have *done* — the responsibilities

| The JD says | You | File |
|---|---|---|
| Design, develop, test and deploy backend services in Java and Spring Boot | Two production platforms at a UK bank | `01`–`03`, `13` |
| Build and maintain microservices-based applications | Classifieds — Eureka, API Gateway, three services | `05` |
| Develop RESTful APIs **and integrate with third-party services** | APIs yes; integration is the one to rehearse | `03`, `05` Q2b |
| **Optimise performance, scalability and security** | **Your single strongest line: 15s → 6s, 2–3s → under 1s** | `04`, `08`, `13` |
| Work with **relational and NoSQL** databases | MySQL deeply; MongoDB on your resume | `08`, `08` Q7 |
| Collaborate with frontend developers, QA and business stakeholders | Daily, with a client team in another country | `15` |
| Implement CI/CD pipelines and support DevOps practices | Worked inside a release process, did not own a pipeline | `10` ⚠️ |
| **Troubleshoot production issues and provide timely resolutions** | Real incident experience — lead with it | `13` Story 4, `15` |
| Write clean, maintainable, well-documented code | Say what "clean" means to you concretely | `15` |
| Participate in code reviews and technical discussions | Yes — have an example of feedback you gave *and* received | `15` |

**Read that list again.** Six of the ten are things you have genuinely done, two are strengths
you can prove with numbers, and only one is a real gap. That is a good position.

### What they will ask you to *know* — the required skills

| The JD asks | Your position | File |
|---|---|---|
| **Java 8 / 11 / 17+** | Java 8 solid; know what 11 and 17 added | `01`, `02` |
| **Spring Framework, Boot, MVC, Data JPA** | All four, in production | `03` |
| **Microservices architecture** | Built one end to end | `05` |
| **RESTful APIs** | Yes, with proper exception handling | `03`, `12` |
| **Hibernate / JPA** | Yes — and you tuned it, which is better | `04` |
| **MySQL, PostgreSQL, Oracle** | MySQL deeply; the others are dialect differences | `08` |
| **Git, Maven, Gradle** | Git and Maven yes; one line on how Gradle differs | `15` |
| **Docker, Kubernetes, containerisation** | **Not on your resume — the main gap** | `09` 🔴🔴 |
| **Kafka, RabbitMQ, ActiveMQ** | **Kafka and RabbitMQ in production, for different reasons** | `06` |
| **JWT, OAuth2, application security** | JWT and Spring Security RBAC; OAuth2 is reading | `07` |
| **Jenkins, GitHub Actions, Azure DevOps** | Used the output, did not build the pipeline | `10` ⚠️ |

### ⚠️ Your three real gaps

**1. Docker and Kubernetes 🔴🔴 — close this one.** It is the only required skill you have no
exposure to, and "containerization" is spelled out as its own bullet. Three hours of reading
closes it to interview standard. **File 09, Friday evening.**

**2. CI/CD tooling ⚠️** — you have worked inside a SIT/UAT release process without owning the
pipeline. That is a normal position at your experience and easy to say well. **File 10.**

**3. OAuth2 ⚠️** — you have JWT, which is not the same thing. The distinction itself is the
answer: *OAuth2 is how a token is obtained; JWT is a format a token can be written in.*
**File 07, Q6b.**

Everything else on that list is either yours already or a dialect difference from something
that is.

### 🔴 The pattern for every gap — use it all day

**Name the boundary first, then show the understanding.**

> *"I have not owned the container and deployment side — that was a separate team on our
> platform. So I would call that understanding rather than hands-on. What I do know is the
> model and why it is used…"*

Then explain it properly. **With a 1+ year requirement, that is a strong answer** — they are
not expecting a DevOps engineer. Claiming hands-on Kubernetes and then being asked why a pod is
in CrashLoopBackOff is what loses you the room, and the second question always comes.

### ✅ What this JD does *not* ask for — stop worrying about it

- **It does not ask for a domain.** Your banking background is a bonus with IBM, not a
  requirement. Use it as evidence that you understand regulated, audited systems — do not build
  your whole pitch on it.
- **It does not ask for 3+ years.** See below.
- **It does not ask for frontend, cloud certifications, or system design at scale.** If those
  come up they are conversation, not assessment.

### ✅ On the experience band — this is good news

**The JD says "Experience Required: 1+".**

You have roughly **18 months of backend engineering** and about **two years four months of
professional experience** in total. **You clear that bar comfortably.** Do not treat your
experience as something to defend — it is not the issue in this process, and carrying that
worry into the room will show.

Two things still hold, for a different reason:

- **Answer with dates, and never round up.** Not because the bar is a risk, but because JOY IT
  verifies against payslips and Form 16 at offer stage, and your salary is fixed from the
  verified number. Getting caught costs the offer after you have resigned somewhere.
- **A "1+" posting tells you what the bar in the room is.** They expect to interview people
  with one year of experience, so the panel is testing **fundamentals done properly** — explain
  a HashMap, find an N+1, say what `@Transactional` actually does, write a clean query — not
  architecture war stories. You have all of that *plus* production performance numbers and two
  messaging systems used for different reasons. **Depth where a one-year candidate would be
  thin is exactly how you stand out.**

File 13 section 5 has the wording.

---

## 3. What Monday will probably look like

### 🔴 First: the format is not confirmed

The JOY IT JD states the mode plainly: **"AI interview, F2F — Monday, Tuesday."**

So the pipeline is **AI screen → face to face**, and you have already cleared the AI screen at
69%. The F2F spans **two days**, which usually means either several candidates across two days,
or more than one round for you across Monday and Tuesday — so do not assume Monday is the end
of it. Keep Tuesday loose if you can.

HR could not confirm whether Monday is a written assessment, a technical interview, or both.
Plan for both; it covers every case and costs nothing if only one happens. Do not treat that as
two preparations. The overlap is about 80%; only the *form of the answer* changes.

- **If it is a written test** → read `00b-if-its-a-written-test.md`. Output traps, stream
  tasks, SQL by hand, and how to lay out a descriptive answer so a marker can score it fast.
- **If it is an interview** → read `00-ai-round-debrief.md`. You already sat the AI screen and
  passed at 69%, so the panel has your transcript and knows exactly where to dig. That file is
  the ten threads they will come back to.

**It is in person.** HR is sending venue details and timing tomorrow, so treat Monday as a
visit to an office: printed cheat sheet, resume copies, phone probably left at reception, and
most likely more than one round in the same visit. `00b` has the full checklist and the mail
to send back.

Read **both**. And block the whole of Monday — if the written test and the interview run on
the same day, the gap between them is often short and the invitation arrives with little
notice. `00b` has the message to send the recruiter today.

### If it is the interview, the rounds usually run like this


**Round 1 — Technical (45–60 min).** Core Java, collections, Spring Boot, JPA, SQL, usually a
coding question. → Files 01–04, 08, 11.

**Round 2 — Technical / architecture (45–60 min).** Microservices, messaging, security,
containers and CI/CD, plus a deep dive into what you built. → Files 05, 06, 07, 09, 10, 12, 13.

**Round 3 — Managerial / HR (20–30 min).** Client-facing fit, the gap, availability, salary.
→ Files 14, 15.

> ⚠️ This is my prediction from how these roles usually run, not something I can confirm. Ask
> the recruiter what the rounds are — it costs nothing and they usually tell you.

**The BFSI instinct to carry into every answer:** whenever you describe a design or a fix, add
the sentence most candidates never say — **"and here is how we would know afterwards what
happened."** Audit trail, traceable logging, idempotency so a payment is never taken twice,
authorisation enforced server side, no sensitive data in logs. You worked on a bank's systems;
that instinct is yours to show.

---

## 4. The three-day plan — Friday evening to Sunday

### Friday evening (tonight) — the two files written for Monday

Before anything else: **`00-ai-round-debrief.md`, in full.** It is the highest-value hour you
have, whichever format Monday takes. Then `00b-if-its-a-written-test.md`. Then the block below.

### Friday evening, continued — close the biggest gap

| Block | Topic | File |
|---|---|---|
| 0:15 | Read this file | `README.md` |
| 1:30 | **Docker and Kubernetes** 🔴🔴 — your largest gap, named three times | `09-docker-kubernetes.md` |
| 0:45 | **CI/CD and DevOps** 🔴 | `10-cicd-and-devops.md` |
| 0:30 | **Your experience** — the gap answer and the band answer, out loud | `13-your-experience.md` §5 |

### Saturday — the core, where most of the interview lives

| Block | Topic | File |
|---|---|---|
| 1:45 | **Core Java and Collections** 🔴🔴 — HashMap above all | `01-core-java.md` |
| 1:30 | **Spring Boot** 🔴🔴 | `03-spring-boot.md` |
| 1:15 | **JPA, Hibernate, N+1** 🔴🔴 — your own story | `04-jpa-hibernate.md` |
| 1:00 | **SQL, indexing, Oracle/Postgres/Mongo** 🔴 | `08-sql-and-databases.md` |
| 0:45 | **Java 8, and what 11 and 17 added** 🔴 | `02-java8-functional.md` |
| Evening | **Your four stories, said out loud** 🔴🔴 | `13-your-experience.md` |

### Sunday — architecture, security and rehearsal

| Block | Topic | File |
|---|---|---|
| 1:15 | **Microservices** 🔴 | `05-microservices.md` |
| 1:00 | **Kafka, RabbitMQ, ActiveMQ** 🔴 — your differentiator | `06-kafka-rabbitmq.md` |
| 0:45 | **Spring Security, JWT and OAuth2** 🔴 | `07-spring-security-jwt.md` |
| 1:00 | **Coding round** — type the problems, do not read them | `11-coding-round.md` |
| 0:45 | **Delivery, code review, Maven/Gradle** | `15-delivery-and-code-review.md` |
| 0:45 | **HR and managerial** — say these out loud | `14-hr-and-behavioural.md` |
| 0:30 | Skim: system design | `12-system-design.md` |
| By 11pm | **Sleep.** Do not cram Sunday night. | — |

### Monday morning
45 minutes on `16-final-cheatsheet.md` and nothing else. Then say out loud, twice: your intro,
the gap answer, and the 15s → 6s story. **Learn nothing new.**

### If you fall behind
Drop in this order: system design → coding round → delivery → Java 11/17 detail.
**Never drop:** Core Java, Spring Boot, JPA, file 09 (Docker/Kubernetes), or file 13.

---

## 5. The files

| File | Topic | Priority |
|---|---|---|
| `00-ai-round-debrief.md` | **The AI round, and the ten threads Monday will dig into** | 🔴 Read first |
| `00b-if-its-a-written-test.md` | **Output traps, stream tasks, SQL by hand, written answers** | 🔴 Read second |
| `01-core-java.md` | OOP, collections, HashMap internals, exceptions | 🔴 Highest |
| `02-java8-functional.md` | Streams, lambdas, Optional, **Java 11 and 17** | 🔴 High |
| `03-spring-boot.md` | IoC, DI, annotations, bean scopes, Spring MVC | 🔴 Highest |
| `04-jpa-hibernate.md` | JPA, lazy vs eager, **N+1**, transactions | 🔴 Highest |
| `05-microservices.md` | Patterns, Eureka, gateway, resilience, saga | 🔴 High |
| `06-kafka-rabbitmq.md` | Kafka vs RabbitMQ vs **ActiveMQ** — your edge | 🔴 High |
| `07-spring-security-jwt.md` | Spring Security, JWT, **OAuth2 and OIDC** | 🔴 High |
| `08-sql-and-databases.md` | Indexing, EXPLAIN, **Oracle/Postgres/Mongo** | 🔴 High |
| `09-docker-kubernetes.md` | **Containers, images, pods, services, probes** | 🔴🔴 **Biggest gap** |
| `10-cicd-and-devops.md` | **Pipelines, Jenkins/Actions/Azure, deployment** | 🔴 High |
| `11-coding-round.md` | Coding problems with full solutions | 🟠 Medium |
| `12-system-design.md` | Design framework and worked examples | 🟠 Medium |
| `13-your-experience.md` | **Your stories, the gap, the experience band** | 🔴 Highest |
| `14-hr-and-behavioural.md` | HR round, salary, questions to ask | 🔴 High |
| `15-delivery-and-code-review.md` | Code review, estimation, **Maven/Gradle** | 🔴 High |
| `16-final-cheatsheet.md` | One page. Monday morning only. | 🔴 Read last |

---

## 6. Three rules for the room

**1. Name your boundary before they find it.** You are two years in, applying to a 3–6 band,
with four technology gaps. Saying *"I have not owned that — here is what I do understand"*
first makes everything else you say trustworthy. Bluffing collapses on the follow-up.

**2. Give the why, not just the what.** "HashMap stores key-value pairs" is a textbook answer.
"It gives O(1) lookup because it hashes the key to a bucket instead of scanning" is an
engineer's. Same length, completely different impression.

**3. Bring every answer back to something you did.** You have a UK bank, real performance
numbers, Kafka and RabbitMQ used for different reasons, and production incidents you
root-caused. That is more concrete evidence than most candidates with four years. Use it.
