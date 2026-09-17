# 11 · Talking About Your Experience 🔴🔴
**Time needed: 60 minutes, said out loud**

---

## First, the context: your real position

You have **1 year 8 months** at Zensar on **Tradu**, a trading platform for FXCM, covering
user onboarding, identity verification and transaction processing across multiple payment
vendors. Java and Spring Boot backend, React frontend, deployed on AWS.

**What is genuinely strong here:**

- **The domain transfers directly.** Lloyds is a bank. You have worked on KYC-style identity
  verification and money movement through payment vendors. Most candidates at your level
  have worked on something generic.
- **You worked across the full development cycle**, not just coding: unit tests with JUnit 5
  and Mockito, defect verification, root cause analysis, refactoring, logging, code quality
  through SonarQube, and Agile delivery in JIRA. That is the profile a bank wants.
- **You collaborated with a frontend team**, so you have had to think about the API as a
  contract someone else consumes — which is exactly what "API design" questions are about.

**What to be careful about:** at 1 year 8 months, your credibility comes from being
precisely calibrated. **Claim what you did, name where your depth ends, and let the
fundamentals carry the rest.** Section 5 covers the four places your resume invites a
follow-up you need to be ready for.

---

## 🔴 "Tell me about yourself" — your script

Structure: **Now → What you built → Why this role.** Under two minutes.

> "I am a Java backend developer with a bit under two years of experience, most recently at
> Zensar working on Tradu, a trading platform for FXCM.
>
> It is a Java and Spring Boot backend with a React frontend, deployed on AWS, and it covers
> user onboarding, identity verification and transaction processing across several payment
> vendors. My work was the backend business components and REST APIs behind those flows —
> the controllers and services, the validation and exception handling, and the API security
> with Spring Security. I wrote the JUnit and Mockito tests for what I built, and I spent a
> fair amount of time on defect analysis and refactoring, including improving the logging so
> issues were faster to diagnose.
>
> What draws me to this role is that it is the same domain and the same stack, but on a
> product being built and run long term rather than a client project. I want to go deeper on
> Spring Boot and on distributed systems, and do it somewhere the quality bar is high — which
> in a bank it has to be."

Practise this twice. Time it. **End on why this role**, not on a list of technologies.

---

## Your stories — build these from what you actually did

For each: **what it was → what you decided → what was hard → what you would do differently.**
That last one is what makes an answer sound senior rather than junior.

⚠️ **Fill in the specifics yourself.** These are frames, not scripts. An invented detail
falls apart on the second follow-up and costs you the room.

### Story 1 🔴 — An API you built end to end *(lead with this)*

The frame:

> "One of the flows I owned was [onboarding / a payment flow / a transaction endpoint]. The
> work was the controller and service layer, the validation on the way in, and the exception
> handling so the frontend got a consistent error contract rather than stack traces.
>
> The part that needed thought was [the real decision — where validation belonged, how to
> represent state, how to handle a vendor's error responses]. I went with [X] because [Y].
>
> I wrote JUnit and Mockito tests over the service logic, particularly [the case that
> mattered], because that is the part that would be expensive to get wrong."

**Be ready for:** *what did you validate and where*, *what did the error response look like*,
*what did you mock and why*.

### Story 2 🔴 — Working with external payment vendors

This is your most interesting story for a bank, because it is about failure.

> "The platform integrated multiple payment vendors, so a lot of the work was dealing with
> systems we did not control. Different response shapes, different error semantics, and calls
> that can time out or hang.
>
> [What you actually did — mapped vendor responses to a common internal model / handled
> specific failure codes / added logging around the boundary so failures were diagnosable.]"

**Then show you understand the general problem**, which is the part that scores:

> "The thing I have taken from it is that any call to an external system needs a timeout, and
> it needs to be idempotent or guarded, because on a payment you cannot afford to retry
> blindly and debit someone twice. Beyond that a circuit breaker stops a vendor that has gone
> slow from taking your own service down with it."

### Story 3 — A defect you root-caused

Your resume says root cause analysis, so expect to be asked for one.

Use STAR and land on **what changed afterwards**: a test added, a log line added, a check
added. That turns a firefighting story into a quality story — which is what a bank is
listening for.

### Story 4 — Refactoring and logging

> "I refactored existing code for readability and maintainability, and improved the logging
> so problems were faster to diagnose. The logging one mattered more than it sounds — when a
> transaction fails in production you need to be able to follow what happened without
> attaching a debugger."

**If they push on logging, the good detail is:** log at the boundaries, include an
identifier you can trace a request by, never log card numbers, credentials or personal
data — and in a regulated environment that last one is a compliance matter, not a style
preference.

---

## 🔴🔴 Section 5 — The four questions your resume invites

Prepare all four. None is a problem; all are a problem if you improvise them.

### 1. 🔴🔴 "How much microservices experience do you have?"

Your resume lists microservices; your project description is a Spring Boot backend. **The
full answer is in file 05, Q7** — read it properly. The short version:

Name your level first — REST services within a Spring Boot backend, working across service
boundaries and with external vendor APIs — say plainly that you have not owned a
multi-service architecture end to end, then demonstrate that you understand the model and
its **costs**. Honesty plus understanding beats a claim that unravels.

### 2. 🔴 "You have Kafka, AWS, Docker and Jenkins listed. How deep is that?"

Your resume already says "Apache Kafka fundamentals" and "exposure to" for the cloud and
DevOps tools. **That wording is good — hold the line on it in the room.** The trap is being
flattered into overclaiming when an interviewer sounds interested.

> "I would call that exposure rather than depth. I have used Jenkins and SonarQube as part of
> our pipeline and Docker in the development setup, and the application was deployed on AWS,
> but I was not the person owning the infrastructure. With Kafka I know the model —
> topics, partitions, consumer groups, and why you would publish an event instead of making a
> synchronous call — but I have not run it in production."

Then, if it is a Kafka conversation, go to file 06 and show the understanding. **Saying "I
know the model but have not run it in production" is a completely respectable answer at your
level.** Claiming production Kafka and then being asked about consumer group rebalancing is
not.

### 3. 🔴 Your employment ended in July 2026

Your resume shows **Dec 2024 – Jul 2026**, and it is now September. That is roughly two
months, which is short and recent — but it will be asked, because interviewers always ask.

Two or three sentences, factual, no apology:

> "[The real reason — the project ended / the client engagement wound down / I chose to move
> on.] Since then I have been [what you have actually been doing — interviewing, strengthening
> Spring Boot and microservices, building something]. I have been looking for a product
> role rather than taking the next client project."

**Fill in the truth.** A two-month gap between roles is completely unremarkable. The only
thing that makes it a problem is sounding evasive about it.

**If you have been learning, be specific.** "I have been working through Spring Boot and
distributed systems, and built [X]" is worth far more than "I have been upskilling".

### 4. 🔴 The AI tools on your resume

You have listed ChatGPT, GitHub Copilot and Claude under skills and in your experience:
*"Used ChatGPT, GitHub Copilot, and Claude AI for debugging, code review, and
documentation."*

**Expect a question about it, and expect it to have an edge**, because at a bank there are
two real concerns behind it: can you work without the tools, and do you understand what you
may and may not paste into them.

**The answer that lands:**

> "I use them the way I would use a senior colleague to think out loud with — for a first
> draft, for explaining an unfamiliar piece of code, or for spotting something in review. But
> I do not commit anything I could not explain and defend myself, because I am accountable
> for it either way, and generated code is confidently wrong often enough that you have to
> read it properly.
>
> The other part is data. In a regulated environment you cannot paste proprietary code,
> customer data or credentials into a public tool. I would follow whatever the organisation's
> policy is on approved tooling — and I would want to know what that policy is on day one."

That second paragraph is the one that matters. It tells a bank you understand the risk
without being asked, which is exactly the instinct they are screening for.

> **Worth considering before the interview:** the line about AI tools is unusual on a resume
> and it invites this question. It is not wrong to have it there — used well it shows
> modern working — but decide deliberately whether you want to keep it, because it will be
> asked about. If you keep it, have the answer above ready.

---

## ✅ Before the interview
1. Say the "tell me about yourself" script out loud, twice. Time it.
2. Fill in Stories 1 and 2 with **real specifics** from Tradu, and say them out loud.
3. Rehearse all four answers in section 5 — especially the microservices one.
4. Write down the **real one-sentence reason** the role ended in July.
5. Have your GitHub and anything you have built since ready to show.
