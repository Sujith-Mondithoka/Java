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

## 🔴🔴 Section 5 — The three things on your resume to sort out tonight

These are the parts of your resume an interviewer will probe. None of them is a problem.
All of them are a problem if you are working out the answer live.

### 1. 🔴 The two gaps in your timeline

Lay your own dates out:

```
2022          B.Tech, Bapatla Engineering College
2022 – 2023   (gap, about 10 months)
May 2023      JSPIDERS Java Full Stack programme
Jan 2024      programme ends
2024          (gap, about 11 months)
Dec 2024      Zensar - Software Engineer (Backend)
```

**You will be asked about both.** The answer is short, factual and unapologetic. Two or
three sentences, then move on.

> "I graduated in 2022 and spent that period preparing to move into development properly
> rather than taking the first thing available. I did the JSPIDERS Java full stack
> programme through 2023 into early 2024, and then [the real reason for 2024 — job
> searching in a slow hiring market / a family reason / preparing and interviewing]. I
> joined Zensar in December 2024 and have been building backend banking systems since."

**Fill in the real reason yourself. Do not invent one.** Gaps in 2022–2024 are extremely
common — that was a slow hiring period for freshers across the industry, and interviewers
know it. Evasiveness is the only thing that turns a gap into a problem.

### 2. 🔴🔴 The employer that is missing from this version of your resume

An earlier version of your resume listed **Talent Acquisition Executive at Artifint
Technologies LLC, Feb 2024 – Dec 2024**. This version does not.

**Two reasons to think carefully about that before tomorrow:**

**It creates the gap.** With that role included, the 2024 gap disappears entirely — the
timeline runs training, then work, then Zensar, with nothing unexplained.

**Infosys runs formal background verification, and in India that includes your employment
history.** If PF was deducted at Artifint, the employment sits in your EPFO/UAN record.
An employer that shows up in verification but not on the resume reads as concealment, which
is treated far more seriously than the job itself ever would be. That risk is real and it
lands *after* you have accepted an offer.

**My recommendation, and it is your call:** put it back. It fills the gap, it is verifiable
anyway, and — read this JD again — the first responsibility listed is *"interface with the
client for quality assurance… ensuring high customer satisfaction"*. You spent a year in
**technical** recruitment, screening and coordinating interviews for engineering roles.
Almost nobody applying for this role can say they are comfortable in client conversations
and have evidence for it.

**If you include it, the answer is:**
> "I finished my B.Tech in Computer Science in 2022, so development was always where I was
> heading, and I did the JSPIDERS Java programme to build the skills properly. The role at
> Artifint was technical recruitment — I was screening and coordinating interviews for
> engineering positions, so I was close to the work I wanted to do. [The real reason it
> happened.] I moved into engineering at Zensar in December 2024.
>
> Honestly, that year was more useful than it sounds. I spent it in conversations with
> engineers and clients every day, and I am comfortable in requirement and client
> discussions in a way that is not always true of people who came straight through."

**If you keep it off**, then be ready to account for Feb–Dec 2024 truthfully if asked, and
be aware of what verification may surface. Never state that you were not working during a
period when you were.

### 3. "So how much experience do you have exactly?"

Your summary says **"2+ years building enterprise banking applications"**, but the Zensar
role runs from **December 2024**, which is about **1 year 9 months** as of early September
2026.

Infosys verifies dates against payslips and employment letters, and your band and offer are
set from that number, so this is the wrong place to round up.

**In the interview, answer with dates rather than a rounded number:**
> "I have been in my engineering role since December 2024, so about a year and nine
> months."

Straightforward, verifiable, and it removes the issue completely. If you also count the
recruitment year as professional experience, say that separately rather than folding it into
"2+ years of backend engineering".

**If you have time tonight**, soften the summary line to "close to 2 years" or drop the
number and let the dates speak. It costs you nothing and removes a line an interviewer can
pick at.

---

## Questions about your numbers
If they ask how you measured 15s → 6s, or 2–3s → under 1s, be ready with: application
timings and logs before and after, plus the query counts from SQL logging. If the numbers
came from someone else's measurements or a monitoring dashboard, say so — attributing
accurately is better than being vague.

---

## ✅ Before the interview
1. Say the "tell me about yourself" script out loud, twice. Time it.
2. Write down the **real one-sentence reason** for each gap in your timeline, and decide
   whether the Artifint role goes back on the resume. Say both out loud until they sound
   calm rather than defensive.
3. Decide how you will state your experience duration, and make the resume match.
4. Be able to say every number without hesitating: **15→6, 2–3→under 1, 3 services,
   200+ profiles**.
5. Have one production-incident story with a **what changed afterwards** ending.
