# NCG — GCC Java Backend Developer (BFSI)
### Neelima Jana · Interview: **Monday 16 November** · Hyderabad · Job ID 88875

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

## 1. A note on who you are interviewing with

The job description is from **NCG (NetConnect Global)** — a digital engineering and
professional services company, Hyderabad, hiring for a **GCC** role in **BFSI**.

You mentioned IBM. **GCC** means **Global Capability Centre** — the in-house engineering centre
a large enterprise runs in India. NCG is a services company that staffs those centres, so the
most likely arrangement is **NCG is the employer and the GCC is the client**.

> 🔴 **Confirm this with the recruiter before Monday — it is a completely normal question and
> it changes things that matter to you:**
> - Who is on the payroll — NCG, or the client directly?
> - Is this a deputation to a client site, and is there a path to conversion?
> - Which client, and which platform would you be on?
>
> *"Could you tell me a bit about the engagement — would I be on NCG payroll working at the
> client's GCC, and which client is it?"* Ask it early, in the HR or screening conversation.

**What is certain from the JD** either way: **Java, Spring Boot, microservices, BFSI, Hyderabad,
client-facing, reporting to a technical lead.** That is what you prepare for.

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

### 🔴 On the experience band

The posting says **Level 3 (3–6 years)**. Your engineering experience is **December 2024 to June
2026 — about 18 months** — plus the recruitment year, so roughly **two years four months
professional**.

**You are under the band.** You already have the interview, so someone looked at your profile
and still wanted to talk; ranges are sourcing guidance, not a gate. But **answer with dates and
never round up** — these roles verify against payslips, and your band and offer are set from the
verified number. The full answer is in **file 13, section 5**.

---

## 3. What Monday will probably look like

### 🔴 First: the format is not confirmed

HR has said Monday is **either a technical written assessment or a technical interview** —
they do not yet know which. Do not treat that as two preparations. The overlap is about 80%;
only the *form of the answer* changes.

- **If it is a written test** → read `00b-if-its-a-written-test.md`. Output traps, stream
  tasks, SQL by hand, and how to lay out a descriptive answer so a marker can score it fast.
- **If it is an interview** → read `00-ai-round-debrief.md`. You already sat the AI screen and
  passed at 69%, so the panel has your transcript and knows exactly where to dig. That file is
  the ten threads they will come back to.

Read **both**. Ask the recruiter the length and the platform — most will tell you if asked.

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
