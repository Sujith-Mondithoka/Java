# 12 · Talking About Your Experience 🔴🔴
**Time needed: 60 minutes, said out loud**

---

## First, the context: you are pitching as a backend engineer now

Your resume is positioned as **Software Engineer, Backend — Java · Spring Boot · Camunda ·
PostgreSQL**, and the React work sits underneath as supporting. That is the right call for
a Java and Spring Boot interview, and it is honest, because the backend work is substantial.

**What is genuinely strong:**

- **You built the backends, not just consumed them.** Spring Boot, Spring Data JPA and
  PostgreSQL for two applications on a platform used by 10,000+ corporate clients.
- **You have real numbers:** card processing time cut **60%**, an audit system writing
  **50,000+ transactions a day**, **1,000+ monthly reports**.
- **You have unusual depth for your level** — Camunda BPMN, AOP with `@Aspect`, Liquibase
  migrations, JasperReports, FileNet, Kafka and RabbitMQ. Most candidates at two years have
  CRUD APIs and nothing else.
- **You worked a real release process** — JUnit, SIT/UAT, Bamboo CI/CD, code review.

**The one thing to manage:** being full-stack can read as unfocused in a backend interview.
Lead with backend, mention React once as useful context, and move on.

---

## 🔴 "Tell me about yourself" — your script

**Now → What you built → Why this role.** Under two minutes.

> "I am a backend engineer with about a year and a half of production experience, most
> recently at Zensar on Standard Bank South Africa's Service Online platform, which is used
> by around 10,000 corporate clients.
>
> I built the Spring Boot and PostgreSQL backends for two self-service applications — a
> business card application and an online transaction recall workflow. Both had multi-stage
> approval processes, so I modelled those as Camunda BPMN workflows, which took card
> processing time down by about 60%.
>
> The piece I am most pleased with is an audit logging system I built with Spring AOP. The
> requirement was to capture every report download and email for compliance, and rather than
> adding a logging call to dozens of endpoints, I used `@Aspect` pointcuts so the audit logic
> lives in one class and the business code is untouched. It writes over 50,000 transactions a
> day to PostgreSQL.
>
> I also worked on the React side of the same platform, so I have seen the API from the
> consumer's end — but backend is where I want to specialise, which is why this role
> interested me."

Practise twice. Time it. **End on why this role.**

---

## Your four stories

### Story 1 🔴🔴 — The AOP audit system *(lead with this)*

This is your best story because it is an **architecture** decision, not just a feature.

> "The requirement was to audit every report download and email for compliance. The obvious
> approach is to add a logging call inside each endpoint, but that means touching dozens of
> files, and it is easy to miss one — and worse, easy for the next person adding an endpoint
> to forget.
>
> So I used aspect-oriented programming. A pointcut matches the methods, and the aspect runs
> around them. The audit logic lives in one class, the business code is untouched, and it
> cannot be forgotten when someone adds a new endpoint. It writes more than 50,000
> transactions a day to PostgreSQL."

**Follow-ups to be ready for:**

- *"What is a pointcut versus an advice?"* → A **pointcut** is the expression that selects
  which methods to intercept. An **advice** is the code that runs — `@Before`, `@After`,
  `@Around`. `@Around` is the one that can see both the arguments and the return value.
- *"How does Spring AOP work underneath?"* → **Proxies**. Spring wraps the bean in a proxy —
  a JDK dynamic proxy if it implements an interface, CGLIB otherwise — and the proxy runs
  the advice before delegating. **And the same caveat as `@Transactional`: an internal
  `this.method()` call bypasses the proxy, so the aspect does not fire.** Saying that
  unprompted is a genuinely strong moment.
- *"What was the performance impact of writing 50,000 rows a day?"* → Be honest about what
  you did. If the writes were asynchronous or batched, say so. If not, say what you would do
  now — an async write or a queue, so auditing never slows the request it is auditing.

### Story 2 🔴 — The Camunda approval workflow

> "The card application had a multi-stage approval flow. Rather than encoding the state
> machine in application code with status columns and conditionals scattered around, we
> modelled it as a BPMN process in Camunda. The engine tracks which step each application is
> at, so the approval rules live in one place and changing the process does not mean
> rewriting business logic. That took processing time down about 60%."

**If they do not know Camunda, explain it simply:** "It is a workflow engine — you define
the process as a diagram and it manages the state transitions and the tasks waiting on
people."

**The general point to land**, which matters more than the tool: *"the value is that the
process is explicit and in one place, instead of being implied by status flags spread across
the codebase."*

### Story 3 — REST APIs and the frontend contract

You built REST APIs consumed by a 14-screen React frontend, and you also wrote that
frontend. That is a useful angle few candidates have:

> "Because I worked on both sides, I paid attention to the API as a contract. Consistent
> error shapes so the frontend has one thing to handle, proper status codes, and pagination
> on list endpoints. When you have been the consumer of a badly shaped API you design
> differently."

### Story 4 — Testing and release

JUnit unit and integration tests for REST APIs and workflow logic, validated through SIT and
UAT. **The detail worth adding:** what you tested. Workflow state transitions are the
valuable tests — that an approved application cannot be approved twice, that a rejected one
cannot move back. Those are the rules that cost money.

---

## 🔴🔴 The three questions your resume invites

### 1. 🔴🔴 The gap — you left in February

Your resume shows **Dec 2024 – Feb 2026**, and it is now late September. **That is about
seven months, and it is the first thing an interviewer will notice.** Prepare this properly;
it matters more than any technical answer in this file.

Two or three sentences, factual, calm, no apology:

> "[The real reason — the project rolled off, the client engagement ended, a personal
> reason.] Since then I have been [what you have actually done — deepening backend skills,
> building X, interviewing selectively]. I was clear that I wanted a backend-focused role
> rather than taking the next thing available, and this one matches that."

**Fill in the truth. Do not invent anything.** Project roll-offs and bench situations are
extremely common in the services industry and no interviewer will hold one against you.

**Then show the time was used.** This is the part that turns the gap from a negative into a
neutral or better:

- Be **specific**: "I went through the Spring Boot documentation properly and rebuilt X"
  beats "I was upskilling" by a mile.
- Your **GenAI Level 1 and 2 certifications** are dated 2025, so mention any learning since.
- If you have built anything, have it on GitHub and mention it.

⚠️ **Do not let this be vague.** A seven-month gap with a clear story is fine. A seven-month
gap with a mumbled answer is the thing that loses the interview.

### 2. 🔴 "You look like a frontend developer. Why backend?"

Your GitHub and portfolio are React-heavy, and your resume lists React under skills. Expect
this.

> "I have done both, and on the Service Online platform I did both on the same product. What
> I found is that the problems I enjoyed most were on the backend — the Camunda workflow
> modelling, the AOP audit design, getting the data model and transactions right. The
> frontend work I am glad to have done, because it made me better at designing APIs, but
> backend is where I want the depth."

That is credible because it explains the frontend rather than hiding it.

### 3. The AI tools on your resume

You list Claude, GitHub Copilot and "LLM-assisted coding" under skills, plus GenAI
certifications. At a services company that is more likely to be a **positive** — Infosys is
pushing AI-assisted delivery hard — but be ready to answer well:

> "I use them for a first draft, for explaining unfamiliar code, and as a second pair of eyes
> in review. But I do not commit anything I could not explain and defend myself, because I am
> accountable for it either way. And I would follow whatever the client's policy is on what
> can be pasted into an external tool — on a banking project that is a real constraint."

That second sentence is the one that matters. Say it.

---

## ✅ Before Saturday
1. Say the "tell me about yourself" script out loud, twice. Time it.
2. Write down the **real one-sentence reason** for the gap, and what you have done since.
   Say it until it sounds calm rather than defensive.
3. Rehearse the AOP story **including** the proxy follow-up.
4. Be able to say the numbers without hesitating: **60%, 50,000+ a day, 1,000+ monthly
   reports, 10,000+ clients**.
5. Have the "why backend" answer ready.
