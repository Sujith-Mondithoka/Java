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
systems. IBM staffs projects by domain, and someone who already understands banking
workflows is easier to place. Easier to place means easier to hire.

**3. You used Kafka and RabbitMQ for different reasons.** Not just "we had messaging" —
a task queue for one job and an event log for another. That is a design decision, and
it is the most senior-sounding thing on your resume.

**What to watch:** the JD asks for **1+ years** and you have more than that, so experience is
not the problem in this process. Do not oversell it — dates get verified — and do not undersell
it either. Depth on the things you actually did beats vague claims about things you did not.

---

## 🔴🔴 "Tell me about yourself" — your script

This is the first ninety seconds and it sets the whole interview. Get it right and the panel
spends the rest of the time asking about the things *you* chose to mention.

### ⚠️ First, settle one thing: present tense or past?

Your dates are **Dec 2024 – Jun 2026** at Zensar, and it is now November. In the AI round you
were asked about "your current role right now" and you answered. **Whatever you said there is
what you say on Monday** — the two have to match.

- **Still employed at Zensar** → use the script exactly as written below.
- **Left in June** → change the opening line to *"Until June I was a backend engineer at
  Zensar, working for C. Hoare & Co, a private bank in the UK"*, and keep everything else in
  the past tense. Section 5 of this file covers the follow-up.

**Pick one now, say it the same way every time, and do not improvise a third version in the
room.**

### The script — about 90 seconds

**Structure: who you are → what you built → the numbers → the judgement call → why this role.**

> "I am Neelima. I am a Java backend developer with about two and a half years of
> professional experience, the last year and a half of it as a backend engineer at Zensar,
> working for C. Hoare and Company — a private bank in the UK.
>
> My day to day is Java and Spring Boot — REST APIs with Spring Data JPA and MySQL, with
> role-based access control using JWT. I have owned two platforms there end to end: a
> transaction recall system and a business card management system.
>
> The part I would pick out is performance. Both platforms had problems when I picked them
> up. Report generation was taking about fifteen seconds — I traced it to an N+1, one query
> per row, replaced it with a projection query and fixed the indexes, and brought it down to
> six. The card APIs were two to three seconds, and those came down to under one.
>
> I also moved work off the request thread. Approvals were sending emails inside the request,
> so bulk approvals were timing out — I moved that to RabbitMQ with a separate consumer.
> Separately, I published transaction state changes to Kafka for compliance and reporting. A
> queue for one and an event log for the other, because they are different problems.
>
> Outside of that I built a microservices project of my own with Eureka and an API Gateway,
> which is part of why this role interested me. Java, Spring Boot, microservices and
> messaging is exactly the direction I have been moving in — and having worked on a bank's
> systems, I am used to environments where auditability and access control are not optional."

**Then stop.** Do not trail off into "...so, yeah, that's about me." Finish on the last
sentence and let the silence sit. The panel will take it from there, and they will almost
certainly ask about the fifteen seconds or about Kafka — which is exactly what you want,
because both are prepared.

### The 40-second version — if they say "briefly"

Some panels ask for a quick version, especially when there are several candidates waiting.

> "I am Neelima, a Java backend developer, about two and a half years in, the last year and a
> half at Zensar on a UK private bank's platforms. Java, Spring Boot, Spring Data JPA, MySQL,
> REST APIs with JWT-based access control. The work I am proudest of is performance — I took
> report generation from fifteen seconds to six by removing an N+1, and the card APIs from two
> to three seconds down to under one — and moving work off the request thread with RabbitMQ
> and Kafka. Microservices and messaging is the direction I want to keep going in, which is
> why this role."

### The written version — if the assessment asks for a profile

Four lines, no padding, same facts:

> Java backend developer with ~2.5 years' experience, ~18 months as a backend engineer at
> Zensar on platforms for C. Hoare & Co, a UK private bank. Core stack: Java, Spring Boot,
> Spring MVC, Spring Data JPA, Hibernate, MySQL, REST APIs, Spring Security with JWT.
> Performance work: report generation 15s → 6s (N+1 removal, projection query, indexing);
> card APIs 2–3s → under 1s. Event-driven work with RabbitMQ (asynchronous notifications)
> and Kafka (transaction state-change events for compliance and reporting). Built a
> microservices project with Eureka and an API Gateway.

### 🔴 Why this script works — do not "improve" it on the day

Five things are doing the work. If you shorten it, keep these:

1. **It opens with a number, not an adjective.** "Two and a half years" beats "passionate and
   hardworking", which every other candidate says.
2. **It names a real client in a real domain.** A UK private bank is specific and checkable,
   and it signals regulated systems without you claiming domain expertise.
3. **It contains four numbers.** 15 → 6, 2–3 → under 1. Numbers are the cheapest credibility
   available, and almost nobody at this level has them.
4. **It shows a decision, not just activity.** "A queue for one and an event log for the
   other, because they are different problems" is the most senior sentence in the script. It
   is also true, which is why it survives follow-up.
5. **It ends by connecting to the JD** — microservices and messaging — so the panel's next
   question lands in your prepared territory.

### Delivery

- **Slow down on the numbers.** Say "fifteen seconds to six" with a small pause after it. It
  is the line you most want them to remember.
- **Do not list technologies like a shopping list.** Group them: "Java and Spring Boot",
  "Kafka and RabbitMQ". A list sounds memorised; a group sounds lived.
- **Say the client's name properly** — C. Hoare and Company. Fumbling your own client sounds
  like you were not close to the work.
- **Practise it standing up, out loud, four times**: twice today, twice tomorrow. Time it. If
  it runs past two minutes, cut the microservices sentence, not the numbers.
- **Do not memorise it word for word.** Learn the five beats — who, what you built, the
  numbers, the judgement call, why this role — and let the words vary.

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

### 1. ✅ The experience band — the JD says **1+ years**

Your dates:

```
Feb 2024 – Dec 2024   Talent Acquisition Executive, Artifint     ~10 months
Dec 2024 – Jun 2026   Software Engineer (Backend), Zensar        ~18 months
                      total professional experience              ~2 years 4 months
                      of which backend engineering               ~1 year 6 months
```

**The IBM / JOY IT posting asks for 1+ years. You are above it, not below it.**

**Drop any defensive posture about your experience.** It changes how you sit in the room: you
are not someone hoping to be let in under the bar, you are someone comfortably inside it who
has real production numbers. Those are different people to interview, and panels can tell which
one is sitting in front of them.

**If they ask how much experience you have, answer it plainly and move on:**

> "About two and a half years professional, of which around a year and a half is backend
> engineering — December 2024 to June 2026 at Zensar, on a UK private bank's platforms."

Then keep going into what you built. No apology, no hedging, no "only".

**Two things still matter, for a different reason:**

**1. Never round up.** JOY IT will verify your dates against payslips and Form 16 before the
offer, and your salary is set from the verified number. Inflating it costs the offer at the
worst possible moment — after you have resigned somewhere else.

**2. A "1+" requirement tells you what the bar in the room is.** They expect to interview
people with one year of experience. That means the panel is testing **fundamentals done
properly**, not architecture war stories: can you explain a HashMap, can you find an N+1, do
you know what `@Transactional` actually does, can you write a clean query. You have all of that
*plus* production performance work and two messaging systems. **Play to that gap — depth where
a one-year candidate would be thin is exactly how you stand out.**

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
