# 13 · Delivery, Code Review and Working With Clients 🔴🔴
**Time needed: 60 minutes**

---

## First, the context: read this job description again

Almost the entire responsibilities section of this posting is about things that are
**not writing code**:

> *"interface with the client for quality assurance, issue resolution and ensuring high
> customer satisfaction… understand requirements, create and review designs, validate the
> architecture… participate in project estimation, provide inputs for solution delivery,
> conduct technical risk planning, perform code reviews and unit test plan reviews… lead
> and guide your teams towards developing optimized high quality code deliverables,
> continual knowledge management and adherence to the organizational guidelines and
> processes."*

The only technical requirement listed is **Java and Spring Boot**, as both primary and
preferred skill. Everything else in that block is about **how you deliver**.

**What that tells you:** this is not a pure coding role. It is Infosys's analyst-shaped
template — someone who can be put in front of a client, review other people's work, and be
trusted to follow process. The technical round will still test Java and Spring Boot
properly, but there will be a second conversation about all of the above, and most
candidates walk into it with nothing prepared.

**The good news:** your resume already contains evidence for nearly every item. Code
reviews, QA coordination, requirement analysis, deployment validation, production incident
resolution. You have done these things. What you need is to have the answers **ready**, and
to describe them as ownership rather than participation.

⚠️ **One framing note.** You have under two years of experience, so do not claim to have
led a team. Claim what is true: you reviewed code, you coordinated with QA, you handled
production issues. Then show you understand what the next level up involves. Interviewers
respect that far more than an inflated claim they can puncture with one follow-up.

---

## Q1. 🔴 "Have you done code reviews? What do you look for?"

Near-certain, because the JD names it explicitly.

**Say this.**
> "Yes, code reviews were part of our normal process — both getting mine reviewed and
> reviewing others'.
>
> I look in a rough order of importance. First **correctness**: does it do what the
> requirement says, and are the edge cases handled — nulls, empty results, boundary
> values. Second **error handling**: are exceptions handled at the right level, or is
> something being swallowed silently, which is the worst outcome because the failure
> becomes invisible.
>
> Then **the data layer**, because that is where I have found the most real problems.
> Is there an N+1 sitting in a loop, is a query missing an index it will need, is
> `@Transactional` on the right method. Then **tests** — not the count, but whether the
> meaningful cases are covered. And last **readability**: naming, method length,
> duplication. That matters, but I would not block a change on it alone."

**The follow-up: "How do you give the feedback?"** This is really a communication question.
> "I separate what must change from what is a suggestion, and say which is which — a
> comment that just says 'this could be better' wastes everyone's time. I ask rather than
> instruct when I am not sure of the context, because often there is a reason I cannot see.
> And if a thread goes past two or three replies I stop typing and talk to the person,
> because that usually means we are misunderstanding each other rather than disagreeing."

**Real-time example.** In a card management change, a reviewer's comment on my code was
that a status update was not inside the transaction boundary, so a failure partway through
would have left the record updated but the audit row missing. That was a correctness bug a
test would not have caught, and it is the kind of thing I look for now when I review
someone else's.

---

## Q2. 🔴 "What is a unit test plan review? What makes a test plan good?"

Explicitly in the JD, and most candidates have never thought about it.

**Say this.**
> "A test plan review is checking that the tests cover the right things **before** the code
> is written or signed off, rather than discovering the gap in UAT.
>
> What I look for is whether the tests cover **behaviour and rules**, not just lines. A
> suite with high coverage that only tests the happy path is worse than a smaller suite
> that tests the rules that actually matter. So I check three things: is the happy path
> covered, are the **failure and boundary cases** covered, and are the **state transitions**
> covered — the transitions that must be **prevented** as much as the ones that are allowed."

**Real-time example — this is directly on your resume.**
> "On the business card workflow I wrote unit tests for state transition validation. The
> important tests were not 'an approval succeeds' — they were the negative ones: an already
> approved request cannot be approved again, a rejected request cannot move back to
> pending, and a requester cannot approve their own request. Those are the rules that cost
> money if they break, and they are exactly what a test plan review should be checking for."

**If they ask about coverage targets:**
> "Coverage tells you what was executed, not what was verified. A test with no assertion
> still counts towards it. I would rather aim for the critical paths being genuinely tested
> than chase a percentage, though a very low number is still a useful warning sign."

---

## Q3. 🔴 "How do you estimate effort?"

In the JD as "participate in project estimation". Give a method, not a number.

**Say this.**
> "I break the work down until the pieces are small enough that I can actually picture doing
> them — API changes, data model changes, the tests, and the integration. Estimating a
> whole feature in one number is guessing; estimating six small pieces is much closer.
>
> I explicitly include the things people leave out: testing, code review turnaround, and
> integration issues. Integration is where estimates fail most often, because it is the
> part that depends on other people.
>
> And I state the assumptions with the estimate. If I have assumed the API contract is
> fixed and it then changes, the estimate should be revisited rather than just missed —
> stating the assumption is what makes that conversation possible instead of it looking
> like a slip."

**Real-time example.** A change that looks like one field on a screen is rarely one field:
it is the DTO, the validation, the entity and migration, the query, the tests, and the
downstream event if anything consumes it. Walking that list is how I avoid estimating the
visible part only.

**If they ask about techniques:** mention that you have worked in Agile with story points
and relative sizing, and that the value of a group estimate is mostly in surfacing the
different assumptions people are holding, not in the number itself.

---

## Q4. 🔴 "What is technical risk planning? Give me an example."

The JD phrase is "conduct technical risk planning". Most people freeze on this. It is
simpler than it sounds: **what could go wrong, how likely, how bad, and what we do about it.**

**Say this.**
> "It is identifying what could go wrong technically before it does, and deciding on the
> response in advance rather than during the incident.
>
> On a change I would ask: what does this depend on that is outside my control; what happens
> under a load much higher than we test with; what is the blast radius if it fails; and how
> would we roll it back. Then for the serious ones, either mitigate it in the design or agree
> a fallback."

**Real-time example — use your own migration.**
> "When we moved email notifications from synchronous sending to RabbitMQ, the obvious risk
> was that the queue or consumer goes down and notifications silently stop — which is worse
> than the timeout we were fixing, because a timeout is visible and silence is not. So the
> mitigations were retries with backoff, a dead letter queue so a failing message moves
> aside instead of blocking the queue, and alerting on the DLQ so somebody actually finds
> out. Asynchronous processing without a DLQ and monitoring just moves the failure somewhere
> nobody is looking."

That answer is strong because the risk is real, and the mitigations are specific.

---

## Q5. 🔴 "How do you review a design, or validate an architecture?"

The JD says "create and review designs, validate the architecture". You are not expected to
be an architect. You are expected to ask sensible questions.

**Say this.**
> "I check it against the requirement first — does the design actually do what was asked,
> and are the non-functional parts stated: expected volume, response time, what has to be
> consistent versus what can be eventual.
>
> Then the practical questions. Where does the data live and who owns it. What happens when
> a dependency is unavailable. Is anything a single point of failure. How is it secured, and
> is authorisation enforced server side. How will we know it is working in production —
> logging, correlation IDs, metrics. And how does it get released and rolled back.
>
> The last one I ask is whether it is more complex than the problem requires. Simplicity is
> a real design property, and complexity that is not paying for itself is a cost forever."

**Real-time example.** Publishing transaction state changes to Kafka rather than calling the
compliance and reporting services directly was a design decision with a trade-off: it
removed the coupling and let each consumer read at its own pace, at the cost of eventual
consistency and a harder debugging story. Being able to state the cost of your own design,
not just its benefit, is what a design review is for.

---

## Q6. 🔴 "How do you handle a client raising a quality issue?"

The JD's first line is client interfacing for quality assurance and issue resolution. You
worked with a UK bank, so you have real material.

**Say this.**
> "First, acknowledge quickly and separate the two things: what we do to contain it now, and
> what caused it. Clients get much more anxious about silence than about the problem itself.
>
> Then get to the actual facts before promising anything — reproduce it, check the logs and
> what changed recently. I do not commit to a cause or a timeline until I know, but I do
> commit to when I will come back with an update, and I keep that.
>
> Then fix, verify, and say plainly what happened and what we have changed so it does not
> recur. That last part is what actually restores confidence."

**Real-time example.** Production incidents I worked on were diagnosed by analysing SQL
execution plans and application logs to find the root cause, then coordinating the fix with
QA before it went out. The important part was not the fix, it was that QA validated it in
SIT before it reached the client again.

**The line that lands with a services company:**
> "Being wrong quickly and openly costs far less than being confident and wrong slowly."

---

## Q7. "How do you guide or mentor someone more junior?"

Answer honestly at your level.

**Say this.**
> "I have not formally led a team, so I will answer about what I have actually done. Most of
> it has been through code review and pairing on problems. What I have learned is that
> pointing at the answer does not stick — explaining why, or asking the question that gets
> them there, does.
>
> The other thing is writing things down. If I explain the same thing twice, that is a
> documentation gap, not a person problem."

That answer is credible, and the honesty at the start makes the rest believable.

---

## Q8. "Knowledge management" and "adherence to processes" — what do these mean?

Both are literally in the JD, and both sound like filler until you answer them concretely.

**Knowledge management — say this.**
> "Making sure what I know is not only in my head. In practice that is API documentation
> that is actually current — we used Swagger, so it lives with the code rather than drifting
> in a separate document — plus runbooks for things like what to check when the queue backs
> up, and proper handover notes when someone rotates off. The test is whether someone else
> could pick up my work if I were away, and I would rather find that out deliberately than
> during an emergency."

**Adherence to processes — say this.**
> "In a bank the process exists for a reason, and the reason is usually that something went
> wrong once. We had a defined SDLC — requirement analysis, design, implementation, unit
> tests, then SIT and UAT before release — with code review and deployment validation as
> gates. I have never found the process to be the bottleneck; what slows things down is
> ambiguity in requirements, which is why I push to get those pinned down early."

---

## Q9. "How do you handle unclear or changing requirements?"

**Say this.**
> "I do not start building on an assumption I have not confirmed. I write down what I have
> understood, including what is missing, and go back with **specific** questions rather than
> asking them to clarify — a specific question with a proposed default is much faster for
> someone to answer, and it gets a decision on record.
>
> When requirements change mid-work, the important thing is to say immediately what it means
> for the estimate and what else it affects, rather than quietly absorbing it. Absorbing
> changes silently is how a project ends up late with nobody able to explain why."

**Real-time example.** On the recall workflow there were states where it was not defined who
was allowed to act. Rather than pick something, I listed the cases, proposed a default for
each, and asked for confirmation. That took a short call instead of a long email thread, and
it meant the rules were written down rather than living in the code.

---

## Q10. "What makes code high quality?" *(the JD says "optimized high quality code deliverables")*

**Say this.**
> "Four things, roughly in order.
>
> It is **correct**, including the cases that are not the happy path. It is **readable**,
> because it will be read far more often than it is written, and the next person may be me
> in six months. It is **tested** where it matters, particularly the rules that cost money
> if they break. And it **performs acceptably under real data volumes**, not just the ten
> rows in a developer's local database — which is the specific mistake behind both of the
> performance problems I fixed, because both were fine in testing and slow in production.
>
> The one I would add for a bank is **traceability**. If something goes wrong, can we tell
> what happened, who did it and when. That is why proper logging and an audit trail are part
> of the deliverable, not an extra."

---

## ✅ Check yourself before moving on
1. What you look for in a code review, **in order**, and how you give the feedback.
2. What makes a good unit test plan — and the negative state-transition example.
3. Your estimation method, including stating assumptions.
4. The RabbitMQ risk-planning example, with the DLQ and alerting.
5. How you handle a client-raised quality issue, in four steps.
