# 11 · Talking About Your Experience 🔴🔴
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

**What to watch:** your experience is about 1 year 9 months of engineering. Do not
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

## 🔴🔴 Section 5 — The three questions your resume and the postings create

None of these is a problem. All of them are a problem if you work out the answer live.

### 1. 🔴🔴 "Posting B asks for 3 to 15 years. You have less than that."

Your dates:

```
Dec 2024 – present   Software Engineer (Backend), Zensar   ~1 year 9 months
Feb 2024 – Dec 2024  Talent Acquisition Executive          ~10 months
                     total professional experience         ~2 years 7 months
```

**First, the reassurance.** You applied and you have an interview. Somebody looked at your
profile, saw your dates, and still wanted to talk. Experience ranges in postings are
sourcing guidance, not a gate, and a large services company hires across bands. The
interview would not be happening if this were disqualifying.

**Second, never round up.** Infosys verifies dates against payslips and employment letters,
and your band and offer are set from the verified number. Claiming three years is the
easiest thing in the world to catch, and it costs you the offer at the worst possible
moment — after you have resigned.

**The answer if it is raised directly:**
> "In engineering, since December 2024, so about a year and nine months — and around two
> and a half years of professional experience in total. I know that is at the lower end of
> the range.
>
> What I would say is that it has been dense. I have owned features end to end on two
> banking platforms, taken report generation from 15 seconds to 6 and API responses from 2
> to 3 seconds down to under a second, and worked the full SDLC including code reviews, QA
> coordination and production incident resolution. I would rather be judged on that than on
> the number."

Say it calmly and without apologising. **Do not volunteer it if they do not raise it** —
but do not dodge it either if they do.

**And this is the reason file 13 matters so much for you.** The thing a shorter tenure
usually means is less exposure to reviews, estimation and client work. You have that
exposure. Being fluent about it is the single strongest way to close the perceived gap.

### 2. 🔴 The gap between graduation and your first role

```
2022          B.Tech, Bapatla Engineering College
2022 – 2023   gap, about 10 months
May 2023      JSPIDERS Java Full Stack programme begins
Jan 2024      programme ends
Feb 2024      Artifint - Talent Acquisition Executive
Dec 2024      Zensar - Software Engineer (Backend)
```

Putting the Artifint role back on your resume was the right call — it closes what would
otherwise have been an eleven-month hole in 2024, and it is verifiable through your
employment record anyway, so leaving it off would have been the riskier choice.

That leaves **one gap: 2022 to mid-2023.** Two sentences, factual, no apology:

> "I graduated in 2022 and spent that period preparing to move into development properly
> rather than taking the first thing available. [The real reason — job market, further
> preparation, a family reason.] I started the JSPIDERS Java full stack programme in May
> 2023."

**Fill in the real reason. Do not invent one.** That was a slow hiring period for freshers
across the industry and interviewers know it. Evasiveness is the only thing that turns a gap
into a problem.

### 3. 🔴 "Why recruitment, and then development?"

Certain to be asked, because it is right there in the middle of your resume. Answer it
directly and then **turn it into the strength it actually is.**

> "I finished my B.Tech in Computer Science in 2022, so development was always the plan, and
> I did the JSPIDERS Java programme to build the skills properly. The Artifint role was
> **technical** recruitment — I was screening and coordinating interviews for engineering
> positions, so I was close to the work I wanted to be doing. [The real reason it happened.]
> I moved into engineering at Zensar in December 2024.
>
> Honestly, that year was more useful than it sounds. I spent it talking to engineers and
> to clients every day, and I am comfortable in requirement and client conversations in a
> way that is not always true of people who came straight through."

**Read the first line of both postings again:** *"interface with the client for quality
assurance, issue resolution and ensuring high customer satisfaction."* Infosys is a
consulting business. You have a year of evidence that you can hold a professional
conversation with a stranger about a technical role — and almost nobody else in this
pipeline can say that. Do not present it as a detour. Present it as the reason you are
comfortable with the client-facing half of this job.

### One more thing: your summary still says "2+ years"

Dec 2024 to now is about 1 year 9 months, and the summary attributes "2+ years" to building
backend systems. If you have ten minutes tonight, change it to "close to 2 years" or drop
the number and let the dates speak. It removes a line an interviewer can pick at, and it
costs you nothing.

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
