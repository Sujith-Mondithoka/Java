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

## 1. 🔴 Who you are actually interviewing with — and the two JDs

You now have **two job descriptions for what looks like the same client**, and it is worth
being clear about the structure before Monday, because it affects what you ask and what you
negotiate.

### The arrangement

| | |
|---|---|
| **Client** — where you would actually sit and work | **IBM** |
| **Payroll** — who employs you and pays you | **JOY IT** (JOY IT Solutions / JOY IT Consulting) |
| **Employment type** | Full-time with JOY |
| **Location** | Hyderabad |
| **Recruiter** | Prasanthi P, JOY IT |
| **Mode** | AI interview (**done — you passed at 69%**), then F2F Monday/Tuesday |

This is a standard staffing arrangement: **JOY IT is your employer, IBM is the client.** It is
the same shape as your current position — Zensar employs you, C. Hoare & Co is the client. Say
that out loud if it comes up, because it means the model is already familiar to you and you
have worked successfully inside it for eighteen months.

**What it means for Monday:** the F2F is most likely **IBM's technical panel**, not JOY's. JOY
has already screened you with the AI round; a vendor does not usually run a second technical
round of its own. So prepare to impress **the client**, and expect IBM-style questions —
fundamentals, depth on what you actually built, and clean reasoning rather than buzzwords.

### 🔴 The thing to clarify: NCG and JOY IT

Earlier you were given a **NCG (NetConnect Global)** JD for a GCC Java Backend role, also for
IBM, also Hyderabad, also Monday. Now JOY IT has sent an IBM JD with the same interview days.

Most likely one of two things is happening:

1. **They are the same opportunity**, and NCG and JOY IT are both vendors on IBM's panel — or
   one is subcontracting to the other.
2. **They are two different IBM requirements** that happen to be running the same week.

> ⚠️ **This matters, and it is worth one phone call today.** If two vendors submit the *same
> candidate* to the *same client requirement*, the client usually accepts only the first
> submission and may drop the profile altogether to avoid a dispute between vendors. That is a
> bad way to lose a role you have already passed a round for.

**Ask Prasanthi directly, today. It is a normal question and recruiters respect it:**

> "Quick question before Monday — I was also approached for an IBM Java backend role in
> Hyderabad by another vendor. I want to make sure my profile has not gone to IBM twice for the
> same requirement, because I know that can cause problems. Could you confirm which requirement
> you have submitted me for?"

Then ask the same of the NCG recruiter. Whichever submitted you first is the one to go with;
tell the other honestly. **Do not let both run silently.**

### The other questions worth asking JOY IT before you accept anything

Not on Monday with the IBM panel — these are for Prasanthi, on the phone:

- Is this a **permanent JOY position deployed to IBM**, or tied to a fixed project duration?
- **Contract length**, if there is one, and what happens at the end of it.
- Is there a path to **conversion to IBM payroll**, and has it happened for others?
- **Who manages your appraisal and increment** — JOY or the IBM lead?
- Which IBM account or project, and what is the tech stack on it day to day?

**None of this belongs in the technical round.** Keep it with the recruiter.

---

## 2. The JD, decoded against your resume

The posting lists a lot of technologies. Here is what you actually have, and what you do not.

### ✅ Where you are strong — these are the bulk of the interview

| The JD asks | You | File |
|---|---|---|
| **Core Java 8+** | Java 8+, OOP, collections, exceptions | `01`, `02` |
| **Spring Boot, Spring MVC, Spring Data JPA** | All three, in production | `03` |
| **Hibernate / JPA** | Yes — and you tuned it | `04` |
| **RESTful APIs** | Yes, with exception handling | `03`, `12` |
| **Microservices architecture** | The Classifieds platform — Eureka, API Gateway, 3 services | `05` |
| **Kafka, RabbitMQ** | **Both, in production, for different reasons** | `06` |
| **JWT, application security** | Spring Security RBAC, JWT | `07` |
| **MySQL, query optimisation, indexing** | Yes, with real numbers | `08` |
| **MongoDB / NoSQL** | On your resume | `08` |
| **Git, Maven** | Yes | `15` |
| **Performance tuning, profiling** | **15s → 6s and 2–3s → under 1s** | `04`, `13` |
| **Production troubleshooting, root cause analysis** | Yes — execution plans and logs | `13`, `15` |
| **BFSI domain** | **A UK private bank. This is a real advantage.** | throughout |

### ⚠️ Where you have gaps — four of them, all manageable

| The JD asks | Your position | File |
|---|---|---|
| **Docker, Kubernetes, containerisation** | **Not on your resume at all.** Named three times in the JD | `09` 🔴🔴 |
| **Jenkins / GitHub Actions / Azure DevOps** | You worked *inside* a SIT/UAT release process, did not own a pipeline | `10` 🔴 |
| **OAuth2** | You have JWT and Spring Security, not a full OAuth2 integration | `07` Q6b |
| **PostgreSQL, Oracle, ActiveMQ, Gradle, Java 11/17** | Adjacent to what you have — dialect and syntax, not new concepts | `08`, `06`, `15`, `02` |

### 🔴 The pattern for every gap — use it all day

**Name the boundary first, then show the understanding.**

> *"I have not owned the container and deployment side — that was a separate team on our
> platform. So I would call that understanding rather than hands-on. What I do know is the
> model and why it is used…"*

Then explain it properly. **At two years that is a strong answer.** Claiming hands-on Kubernetes
and then being asked why a pod is in CrashLoopBackOff is not — and the second question always
comes.

**Docker and Kubernetes are the one gap worth genuinely closing this weekend.** You have three
days, it is three hours of reading, and it is named three times in the spec. File 09.

### ✅ On the experience band — this is now good news

The earlier NCG posting said **3–6 years**, and a lot of file 13 was written to handle being
under it.

**The JOY IT / IBM JD says "Experience Required: 1+".**

You have roughly **18 months of backend engineering** and about **two years four months of
professional experience** in total. **You clear that bar comfortably.** Stop treating your
experience as something to defend — it is not the issue in this process, and carrying that worry
into the room will show.

Two things still hold, for a different reason:

- **Answer with dates, and never round up.** Not because the band is a risk, but because JOY IT
  will verify against payslips and Form 16 at offer stage, and your salary is fixed from the
  verified number. Getting caught costs the offer after you have resigned somewhere.
- **A "1+" posting means they expect to interview people with less experience than you.** That is
  an advantage: the bar in the room is fundamentals done properly, not architecture war stories.
  Depth on what you actually built will stand out.

File 13 section 5 has the wording, now rewritten for this bar.

### What the JOY IT JD adds that NCG's did not

Four things appear in this JD that are worth ten minutes each:

| New in this JD | Where you stand | File |
|---|---|---|
| **"relational and NoSQL databases"** | MongoDB is on your resume — be ready to say what you used it for and when you would choose it over MySQL | `08` Q7 |
| **"integrate with third-party services"** | You have done API work; the interview answer is timeouts, retries, circuit breaker and idempotency | `05` Q2b |
| **"troubleshoot production issues and provide timely resolutions"** | A real strength — you have incident stories | `13` Story 4 |
| **"Git, Maven, Gradle"** | Git daily, Maven yes; know Gradle's difference in one line | `15` |

Everything else in the JOY IT JD — Java 8/11/17, Spring Boot, Spring MVC, Spring Data JPA,
microservices, REST, Hibernate, MySQL/PostgreSQL/Oracle, Docker, Kubernetes, Kafka, RabbitMQ,
ActiveMQ, JWT, OAuth2, Jenkins, GitHub Actions, Azure DevOps — **is already covered in this
pack.** The two JDs are about 90% the same list. You are not starting again.

---

## 3. What Monday will probably look like

### 🔴 First: the format is not confirmed

The JOY IT JD states the mode plainly: **"AI interview, F2F — Monday, Tuesday."**

So the pipeline is **AI screen → face to face**, and you have already cleared the AI screen at
69%. The F2F spans **two days**, which usually means either several candidates across two days,
or more than one round for you across Monday and Tuesday — so do not assume Monday is the end of
it. Keep Tuesday loose if you can.

HR could not confirm whether Monday is a written assessment, a technical interview, or both.
Plan for both; it covers every case and costs nothing if only one happens. Do not treat that as two preparations. The overlap is about 80%;
only the *form of the answer* changes.

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
numbers, Kafka and RabbitMQ used for different reasons, and production incidents you root-caused.
That is more concrete evidence than most candidates with four years. Use it.
