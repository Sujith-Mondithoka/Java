# 13 · Talking About Your Experience 🔴🔴
**Time needed: 60 minutes, said out loud**

---

## First, the context: your real position

You are stronger for this role than you probably feel, for three specific reasons.

**1. You have real numbers.** 15 seconds to 6 seconds. 2–3 seconds to under 1 second.
Most candidates say "I optimised the API." You can say what was wrong, what you changed,
and what it became. In a services company interview that is rare and it is remembered.

**2. You have banking domain experience.** The JD asks for "one or two industry domain
knowledge". You worked on a UK private bank's transaction recall and card management
systems. Infosys staffs projects by domain, and someone who already understands banking
workflows is easier to place. Easier to place means easier to hire.

**3. You used Kafka and RabbitMQ for different reasons.** Not just "we had messaging" —
a task queue for one job and an event log for another. That is a design decision, and
it is the most senior-sounding thing on your resume.

**What to watch:** your experience is about 1 year 6 months of engineering. Do not
oversell it (see section 5), and do not undersell it either. Depth on the things you
actually did beats vague claims about things you did not.

---

## 🔴 "Tell me about yourself" — your script

Structure: **Now → What you have built → Why this role.** Under two minutes.

> "I am a backend developer with close to two years of experience, currently at Zensar
> working on banking systems for C. Hoare & Co, a private bank in the UK.
>
> My work is Java and Spring Boot with Spring Data JPA and MySQL, and I have built two
> platforms there: a transaction recall system and a business card management system.
> Both were REST APIs with role-based access control, and both had performance problems
> when I picked them up — I took report generation from 15 seconds to 6, and the card
> APIs from 2 to 3 seconds down to under a second, mostly by removing N+1 queries and
> indexing properly.
>
> The part I enjoyed most was moving work off the request thread. I replaced synchronous
> email sending with RabbitMQ so bulk approvals stopped timing out, and used Kafka to
> publish transaction state changes to compliance and reporting consumers.
>
> I have also built a microservices project of my own with Eureka and an API Gateway,
> which is why this role interested me — it is Java, Spring Boot and microservices, which
> is exactly the direction I have been moving in."

Practise this twice today and twice on the morning of the 5th. Time it.

---

## Your four stories, prepared properly

For each: **what it was → what you decided → what was hard → what you would change.**
The fourth is what makes an answer sound senior.

### Story 1 🔴 — The report that took 15 seconds *(lead with this)*

> "Report generation on the recall platform was taking about 15 seconds, and users were
> complaining. My first assumption was that the query itself was heavy, but I turned on
> SQL logging and saw the same query repeating once per row — a classic N+1, because the
> report was walking each transaction's related entities.
>
> I replaced it with a projection query that joined and selected only the columns the
> report needed, so it stopped loading full entities. Then I looked at the execution
> plans, added indexes on the columns used in the WHERE and JOIN clauses, and rewrote a
> couple of JOINs that were forcing full scans. That took it from 15 seconds to 6.
>
> What I took from it is to measure first. My initial guess was wrong, and if I had acted
> on it I would have spent a day tuning a query that was not the problem."

**Follow-ups to be ready for:** *What is N+1?* (file 04) *How did you know which index to
add?* (`EXPLAIN`, file 08) *Why 6 seconds and not 1?* — be honest: some of it was the
sheer data volume and the report's scope, and the next step would have been caching or
pre-aggregating.

### Story 2 🔴 — The APIs that timed out on bulk approvals

> "On the business card system, approvals were sending emails synchronously inside the
> request. A single approval was slow, and bulk approvals were timing out — which was
> worse than slow, because the approval had actually succeeded but the user saw a
> failure.
>
> I moved the email to a RabbitMQ message and a separate consumer. The API went back to
> responding in milliseconds, and a mail server problem stopped being an API problem —
> the messages just wait in the queue.
>
> Separately the same APIs had N+1 issues, so I fixed those and set the right
> associations to lazy, which brought response times from 2 to 3 seconds down to under a
> second."

**The reasoning to make explicit:** the email is not something the user is waiting for,
so it does not belong in the request.

### Story 3 — Kafka for transaction state changes

Use this when asked about architecture or about Kafka. The key point is *why* Kafka and
not a queue — the full answer is in file 06, Q1.

> "Transaction state changes needed to reach more than one consumer — compliance logging
> and report generation, with more likely later. With a queue the first consumer takes
> the message and the others never see it. With Kafka each consumer group reads the same
> events independently at its own pace, the events are retained so a consumer that was
> down can catch up, and compliance can replay history if it needs to rebuild."

### Story 4 — A production incident

Your resume says you resolved production incidents by analysing execution plans and
logs. Have one concrete example ready, in STAR form: what broke, how you found it, what
you did, what happened, and what changed afterwards so it would not recur.

**The part that matters most is the last one.** "We added an alert / added an index /
added a test so it would be caught earlier" turns a firefighting story into a
process-improvement story — which is exactly the JD's *"assess current processes,
identify improvement areas"*.

---

## Your Classifieds project
Covered in file 05, Q7. Keep it brief unless they ask — your professional work is
stronger. Its value is showing that you have designed a microservices system end to end
rather than only worked inside one service.

---

## 🔴🔴 Section 5 — The three questions your resume creates for THIS role

Prepare all three. None is disqualifying. Being caught without an answer is what costs you.

### 1. 🔴🔴 The experience band — the JD says 3–6 years

Your dates:

```
Feb 2024 – Dec 2024   Talent Acquisition Executive, Artifint     ~10 months
Dec 2024 – Jun 2026   Software Engineer (Backend), Zensar        ~18 months
                      total professional experience              ~2 years 4 months
                      of which backend engineering               ~1 year 6 months
```

**You are under the stated band.** Face it calmly rather than hoping it does not come up.

**First, the reassurance:** you have the interview. Someone looked at your profile, saw the
dates, and still wanted to talk. Experience ranges in postings are sourcing guidance, not a
hard gate, and services companies hire across bands when the evidence is strong.

**Second, and this matters more here than anywhere:** NCG is a services company placing people
into a client's GCC. **Your rate and your level are set from verified dates.** Background
verification against payslips and employment letters is routine. So **never round up** — being
caught costs the offer at the worst possible moment, after you have resigned somewhere.

**The answer, if it is raised directly:**
> "In engineering, from December 2024 to June 2026 — about a year and a half — and around two
> and a half years of professional experience in total. I know that is below the range on the
> posting.
>
> What I would say is that it has been dense for the time. I have worked on a UK bank's
> platforms end to end — REST APIs with Spring Boot and JPA, event-driven work with both Kafka
> and RabbitMQ, Spring Security with role-based access control — and I have real performance
> results: report generation from 15 seconds to 6, and API response from 2–3 seconds to under
> one. I have also handled production incidents and root cause analysis. I would rather be
> judged on that than on the number."

**Do not volunteer it if they do not raise it.** Do not dodge it if they do. And do not
apologise — say it the way you would state any other fact.

### 2. 🔴🔴 The gap — you left in June

Your resume shows **Dec 2024 – June 2026**, and it is now **mid-November**. That is roughly
**five months**, and it is the first thing an interviewer notices.

Two or three sentences. Factual. Calm. No apology.

> "[The real reason — the project rolled off / the engagement ended / a personal reason.] Since
> then I have been [specifically what you have done]. I was deliberate about wanting a backend
> role in financial services rather than taking the next thing available, which is why this one
> interested me."

**Fill in the truth. Do not invent anything.** Project roll-offs are routine in the services
industry and no interviewer holds one against you.

**At five months, "I was upskilling" is not enough — be specific**, and this is where the
weekend's work pays off twice:
- If you have been learning **Docker, Kubernetes or cloud**, say so — it is exactly what this
  JD asks for and what you are closing this weekend. *"I have been working through
  containerisation and deployment, which was the part of my last role I was furthest from."*
  That is honest, verifiable by the conversation you are about to have, and turns the gap into
  initiative.
- Anything on GitHub. Any certification.

**Then close on availability:** you can join immediately, which for a staffing-led role with a
client waiting is a genuine advantage. Say it.

### 3. 🔴 "Why recruitment, and then development?"

It is in the middle of your resume, so it will be asked. Answer directly, then turn it.

> "I finished my B.Tech in Computer Science in 2022, so development was always the plan, and I
> did the JSPIDERS Java full stack programme to build the skills properly. The Artifint role
> was **technical** recruitment — I was screening and coordinating interviews for engineering
> positions, so I was close to the work I wanted to do. [The real reason it happened.] I moved
> into engineering at Zensar in December 2024.
>
> That year was more useful than it sounds, honestly. I spent it talking to engineers and
> clients every day, and I am comfortable in requirement and client conversations in a way that
> is not always true of people who came straight through."

**Read the JD again:** *"close collaboration with frontend, QA, and business stakeholders"*,
*"client-facing environment"*, *"collaborate with... business stakeholders to translate
requirements into technical solutions."* This is a **client-facing GCC role**. You have a year
of evidence that you can hold a professional conversation with a stranger about technical work.
Almost nobody else in the queue can say that. **Do not present it as a detour — present it as
why you are comfortable with the client-facing half of this job.**

---

## Questions about your numbers
If they ask how you measured 15s → 6s, or 2–3s → under 1s, be ready with: application
timings and logs before and after, plus the query counts from SQL logging. If the numbers
came from someone else's measurements or a monitoring dashboard, say so — attributing
accurately is better than being vague.

---

## ✅ Before the interview
1. Say the "tell me about yourself" script out loud, twice. Time it.
2. Write down the **real one-sentence reason** for the 2022–2023 gap, and rehearse the
   recruitment-to-development answer plus the "less than 3 years" answer. Say all three out
   loud until they sound calm rather than defensive.
3. Decide how you will state your experience duration, and make the resume match.
4. Be able to say every number without hesitating: **15→6, 2–3→under 1, 3 services,
   200+ profiles**.
5. Have one production-incident story with a **what changed afterwards** ending.
