# 05 · Scenario Questions — Built From Your Own Work 🔴🔴
**Round 2 is "project experience, problem solving and fitment".** That round is mostly
scenario questions, and they will be aimed at what is on your resume — because that is the
only thing the interviewer knows about you.

Every scenario below is one they can plausibly build from your CV. The answers are grounded in
what you actually did on Service Online.

---

## How to answer ANY scenario question — the five steps

Most candidates jump straight to a fix. The marks are in the method.

```
1. CLARIFY     One or two questions. "Is it slow for everyone, or one client?"
2. DIAGNOSE    Say how you would FIND OUT before saying what you would change.
3. CAUSES      Give the likely causes, most likely first.
4. FIX + COST  The fix, and what it trades away. Nothing is free.
5. PREVENT     What you would add so it does not happen again.
```

**Step 5 is the one almost nobody does**, and it is what separates someone who fixes tickets
from someone you would trust with a service. A test, a log line, an alert, a validation.

> **The sentence to reuse all day:** *"Before I change anything I would want to know where the
> time is actually going — my first guess is usually wrong."* You have earned the right to say
> that: on the Lighthouse work your first guess *was* wrong, and measuring is what found it.

---

# Part A · Frontend scenarios

## S1 🔴 "Your My Requests page now has 500 applications and takes 6 seconds to load. Fix it."

**Clarify:** Is the 6 seconds the API call, or the rendering? Is the data paginated server-side
or do we fetch everything?

**Diagnose:** *"The Network tab tells me whether the time is the request or the render. The
React DevTools Profiler tells me how long the commit takes and how many components rendered."*

**Causes, most likely first:**
1. The API returns all 500 rows — the payload itself is the cost.
2. All 500 rows render at once, so 500 components mount.
3. Re-rendering the whole list on every filter or tab change.

**Fix, with the trade-off:**
> "First choice is **server-side pagination** — the API returns 20 rows and a page count. It is
> the biggest win because it fixes the payload *and* the render, and it keeps working as the
> data grows. The cost is a round trip per page, which I would soften by keeping the previous
> page cached.
>
> If the product insists on one scrolling list, I would **virtualise** it with something like
> `react-window` so only the visible rows are in the DOM — 500 rows becomes about 20 nodes.
> And I would memoise the row component so changing a filter does not re-render every row."

**Memory angle, if they probe:** 500 mounted rows means 500 component instances plus their DOM
nodes held in the heap. Virtualising drops that to the visible window, which is why it helps
memory as much as speed.

**Prevent:** *"A performance budget on that page, and I would test with realistic data volumes
— this is the classic bug that passes testing with ten rows and fails in production."*

## S2 🔴 "A user fills in 9 screens of the Business Card form, presses back, and loses everything."

This is your own feature, so answer it as a design question you already solved.

> "That is almost certainly state scoped to the wrong component. If each step owns its own
> state, navigating away unmounts the step and the state is destroyed with it.
>
> The way I built it, **all the form data lives in the parent wizard component** and each step
> is a presentational component receiving values and an onChange. Moving between steps unmounts
> the step but not the parent, so nothing is lost.
>
> If the requirement is surviving a **refresh or a closed tab**, that is a different problem —
> in-memory state cannot survive that. Then you persist: either to `localStorage` on each step,
> or better for this case, save a draft server-side so it works across devices. On Business
> Card the application had a real status, so an incomplete one was a persisted draft the client
> could return to — which is also what the My Requests 'Incomplete' tab showed."

**That last connection is strong** — two of your features explaining each other.

## S3 "The notification bell shows 3 unread, but the user has already read them."

**Causes:** the count is cached and never refetched · it is fetched once on mount and the app
is a long-lived SPA · the read action updates the server but not the local state · two
components hold separate copies of the count.

> "First I would check whether the server is right — if the API returns 3, it is a backend
> problem; if it returns 0 and the UI shows 3, it is stale client state.
>
> For the client case, the fix is a single source of truth. The count lives in one place in
> Redux, and the action that marks something read updates it. I would also refetch on window
> focus, because an SPA left open on a second tab goes stale, and that is exactly when users
> notice."

**Prevent:** *"Avoid two components deriving the same number independently — that is how they
drift."*

## S4 🔴 "Your session-timeout popup fires while users are actively typing."

Your own feature again, and a nice judgement question.

> "That means the timer is measuring time since **login** rather than time since **last
> activity**. The fix is to reset the countdown on real user activity — keypress, click,
> scroll, and any API call going out.
>
> Two details matter. I would **throttle** the activity handler, because resetting a timer on
> every mousemove is wasteful. And the client timer must stay aligned with the **server's**
> session expiry — if the server expires the session at 30 minutes, a client clock that has
> drifted will either warn too late or keep someone 'logged in' on a dead session. The server
> is the source of truth; the popup is only a courtesy."

**Prevent:** *"And the cleanup matters — if the listeners and the interval are not removed on
unmount, you leak the component and can end up with several timers running at once."*

## S5 🔴 "A user types 'axis' in a search box. Results flash, then the wrong results appear."

> "That is a **race condition**. Typing fires a request per keystroke; 'ax' and 'axis' are both
> in flight, and if the older one answers last it overwrites the newer results.
>
> Two fixes, and I would use both. **Debounce** the input by about 400ms, so nine keystrokes
> become one request instead of nine. And **cancel the previous request** with an
> `AbortController` in the `useEffect` cleanup, so a stale response can never land.
>
> That cleanup solves a second problem at the same time — without it you also get the 'state
> update on an unmounted component' warning when the user navigates away mid-request."

**Prevent:** *"Handle all four states — loading, error, empty and success. An empty dropdown
with no message is the thing that makes it look broken."*

## S6 "Typing one character in a form re-renders 50 components."

> "I would open the **React DevTools Profiler**, record one keystroke and see what rendered and
> why — it tells you whether it was props, state or the parent.
>
> The usual cause is that the input's state lives too high up, so every keystroke re-renders
> the whole page. Three fixes, in order: **move the state down** into the smallest component
> that needs it; wrap expensive children in `React.memo`; and if the parent passes callbacks,
> wrap them in `useCallback`, because a new function each render is a new object in memory and
> `React.memo` compares by reference, so it would never match.
>
> On a large form I would also consider React Hook Form, which keeps fields uncontrolled —
> that is what we used on the 14-screen Business Card flow so the whole form did not re-render
> per keystroke."

## S7 "After a release the Lighthouse score dropped from 88 to 70. Find out why."

> "First, compare like with like — same page, same network throttling, ideally the same
> machine, because Lighthouse varies run to run.
>
> Then I would look at what the release changed. The usual suspects are a new dependency
> inflating the bundle, an image added without dimensions, or a lazy-loaded route that is now
> imported eagerly — one static import can pull a whole chunk back into the main bundle, which
> quietly undoes code-splitting.
>
> I would run the bundle analyser before and after. And I would check which metric moved: LCP
> points at an image or the server, CLS at a layout shift from a missing dimension, INP at new
> JavaScript blocking the main thread."

**Prevent:** *"Lighthouse in CI with a budget, so the build flags the regression instead of
someone noticing weeks later."*

---

# Part B · Backend scenarios

## S8 🔴🔴 "An API is fast in testing and takes 8 seconds in production. Why?"

The single most likely backend scenario for your profile.

**Clarify:** Is it slow for all requests or some? Did it change after a release, or degrade
gradually?

> "Gradual degradation with no code change points at **data volume** — something that was fine
> with a hundred rows is not fine with a hundred thousand.
>
> I would find out where the time goes before changing anything: application timings or logs
> first to confirm it is the database, then SQL logging to count the queries.
>
> The most likely cause is **N+1** — one query loads the list and then each row triggers its
> own query for a relation. A hundred rows becomes a hundred and one round trips, and in
> testing with five rows you never notice. The fix is a join fetch, an `@EntityGraph`, or best
> for a read-only screen, a **DTO projection** that selects only the needed columns.
>
> If it is one slow query rather than many, I would run `EXPLAIN` — a full table scan on a
> column in the `WHERE` clause means a missing index."

**The cost, which you should volunteer:** *"An index speeds up reads but every insert and
update has to maintain it, so I add them deliberately on a write-heavy table rather than by
default."*

**Memory angle:** *"N+1 is also a memory problem — every one of those queries puts entities
plus their snapshots into the persistence context, so you fill the heap with objects a screen
may need three fields from."*

**Prevent:** *"Test with production-like data volumes, and log a warning when a request exceeds
a threshold so it surfaces before a client reports it."*

## S9 🔴🔴 "Two approvers open the same card application and click Approve at the same moment."

A perfect question for your Camunda approval work, and it is really about concurrency.

> "Both transactions read the status as PENDING, both decide it is approvable, and both write
> APPROVED. So it is approved twice and you get two approval records. That is a **lost update**
> — and on a financial workflow it is an audit problem, not just a data problem.
>
> The fix I would reach for first is **optimistic locking** — a `@Version` column on the
> entity. Hibernate includes the version in the update's `WHERE` clause, so the second write
> affects zero rows and throws `OptimisticLockException`. I catch that and tell the second
> approver the application has already been actioned, and show them the current state.
>
> The alternative is **pessimistic locking**, `SELECT ... FOR UPDATE`, which makes the second
> transaction wait. I would avoid it here because it holds a database lock, and genuine
> collisions are rare — optimistic costs nothing when there is no conflict."

**The follow-up to pre-empt:** *"A double-click by one user is the same shape of bug. That one
I would also guard with idempotency — the same request key should not create a second
approval."*

## S10 🔴 "A client says they downloaded a report, but it is not in your audit log."

This is a trap question built straight from your AOP system — and the best answer is one almost
nobody gives.

> "The first thing I would check is whether the method was called **through the proxy**. Spring
> AOP works by wrapping the bean in a proxy, so if some other method inside the same class
> called the download method directly with `this.download(...)`, the call never goes through
> the proxy and the aspect never fires. That is the same caveat as `@Transactional`, and it is
> the most likely cause of a silently missing audit record.
>
> After that: does the **pointcut expression** actually match that method — a new endpoint
> added in a different package would not be picked up. And is the audit insert failing and
> being swallowed somewhere, which would make the audit silently incomplete rather than
> noisily broken."

**Prevent, and this is the strong part:**
> "An audit trail you cannot trust is worse than none, because you believe it. So I would want
> the audit write to fail loudly, or go onto a queue so a database problem cannot lose it, and
> an alert if the audit volume drops unexpectedly — for a system writing 50,000 a day, a sudden
> drop is the signal that something stopped matching."

## S11 "Your audit logging starts slowing down the APIs it audits."

> "That means the audit write is happening **inside** the request. At 50,000 a day that is
> fine; at ten times that, the insert is on the critical path of every call.
>
> I would move it off the request: publish the audit event to a queue and let a consumer write
> it, so the API returns as soon as the business work is done. We had RabbitMQ and Kafka on the
> platform, so that path existed.
>
> The trade-off is honest though — it becomes **eventually consistent**, and if the consumer
> is down the audit lags. For compliance data that is a decision to take with the business, not
> alone. So: a durable queue, retries, a dead-letter queue, and alerting on it. An async audit
> with no DLQ just moves the failure somewhere nobody is looking."

**A cheaper middle option to mention:** batching inserts rather than one per call.

## S12 🔴 "You need to add an approval step to the Camunda workflow, but 200 applications are in flight."

> "The problem is that in-flight process instances are running the old definition. If I just
> deploy a new one, the running instances either carry on with the old flow or, worse, end up
> in an inconsistent state.
>
> Camunda handles this with **versioned process definitions** — deploying creates a new
> version, and existing instances keep running the version they started on. So the safe default
> is: new applications get the new flow, the 200 in flight finish on the old one.
>
> If the business needs the existing ones migrated — say the new step is a regulatory
> requirement — that is a deliberate **process instance migration**, mapping old activities to
> new ones, and I would do it in a lower environment first with a plan to roll back."

**The judgement line:** *"The first question I would ask is which of those two the business
actually wants, because it is a business decision and the technical work is different."*

## S13 🔴 "Add a column to a table a live application is using. How do you deploy it safely?"

> "With **Liquibase**, which we used, so the change is a versioned changeset reviewed like any
> other code rather than someone running SQL by hand.
>
> The rule is to make it **backwards compatible**, because for a window the old code and the
> new schema run together. So: add the column as **nullable** or with a default, deploy the
> schema change first, then deploy the code that uses it. Never add a NOT NULL column with no
> default to a populated table — it fails or locks.
>
> Removing a column is the same idea in reverse: stop writing to it, deploy, then drop it in a
> later release once nothing references it. Expand first, contract later."

**Prevent:** *"And the changeset needs to be tested on a copy with real data volumes — a
migration that takes two seconds on an empty table can lock a large one for minutes."*

## S14 "A third-party payment or document service you call starts timing out."

Your FileNet integration makes this credible.

> "The immediate danger is not that one call fails — it is that every thread waiting on that
> call piles up until the service runs out of threads and stops serving requests it could have
> answered. One slow dependency takes the whole service down.
>
> So, first: **every network call needs a timeout**. A call with no timeout is the actual bug.
> Then a **circuit breaker** — after a failure threshold it opens and fails fast instead of
> waiting, and after a cool-down it lets a test call through. Failing fast protects both sides:
> my threads stay free, and the struggling service gets room to recover.
>
> Then the question is what to do in the fallback. For a document download, degrade gracefully
> — tell the user it is temporarily unavailable. For something that must not be lost, queue it
> and retry.
>
> And retries only on **idempotent** operations. Retrying a payment blindly can charge someone
> twice."

## S15 "You need to send 50,000 notification emails for a platform announcement."

Your notification work makes this a natural question.

> "Not in a request, and not in a loop. I would publish the work to a queue and have consumers
> process it, which gives me three things: the triggering request returns immediately, the work
> survives a restart, and I can scale consumers.
>
> Then the practical constraints: the email provider will **rate limit**, so I throttle rather
> than firing 50,000 at once. Each message needs to be **idempotent** — keyed on something like
> user plus announcement id — because at-least-once delivery means a consumer can see the same
> message twice, and sending a customer the same email twice is a visible failure.
>
> And I would track delivery status so support can answer 'did they get it?', with failures
> going to a dead-letter queue rather than disappearing."

---

# Part C · Judgement and teamwork scenarios
*Round 2 is explicitly about fitment. These matter more than people expect.*

## S16 🔴 "QA raises a bug you cannot reproduce."

> "I assume it is real — 'works on my machine' is not a finding. Usually the difference is
> data, environment or sequence, so I ask for the exact steps, the account used, the
> environment and the time, then look at the logs for that window rather than trying to guess.
>
> If I still cannot reproduce it, I pair with the tester and watch them do it. That has found
> it more often than anything else, because the step they did not think worth mentioning is
> usually the one that matters.
>
> If it is genuinely intermittent, I add logging around the suspect path and wait for it to
> happen again, rather than guessing at a fix. A fix for a bug you have not reproduced is a
> guess you have shipped."

## S17 "You are halfway through a sprint and realise your estimate was badly wrong."

> "Say it immediately, at the next stand-up at the latest. The cost of a slipped estimate is
> small; the cost of finding out on the last day is that nobody could re-plan around it.
>
> I would come with specifics rather than just 'it is bigger' — what I found, how much more I
> think it is, and options: cut scope, split it so the core ships this sprint, or take the
> extra time. That makes it a decision someone can take rather than a problem handed over.
>
> Then I would look at what I missed in the estimate, because that is usually integration or
> testing, which is the part people forget."

## S18 "A reviewer leaves a comment you disagree with."

> "I assume they can see something I cannot, so I ask before I argue — often there is context
> about the codebase I do not have.
>
> If I still disagree after understanding it, I say so with a reason, not a preference: a case
> it breaks, or a concrete cost. And I separate 'this is wrong' from 'I would have done it
> differently' — the second is not worth blocking over.
>
> If we are still apart after two or three exchanges, I stop typing and go and talk to them.
> Long review threads are usually a misunderstanding rather than a real disagreement."

## S19 🔴 "You find a security problem in code already in production."

> "Escalate immediately — this is the one case where I would not sit on it to investigate
> first. I tell my lead straight away, because the decision about disclosure and timing is not
> mine to make.
>
> Then: how exposed is it, has it been exploited, can we mitigate quickly even before a proper
> fix. And I would be careful where I write the details — a public ticket describing exactly
> how to exploit something unpatched is its own problem.
>
> In a banking context there is usually a defined process for this, and following it matters
> more than being fast on my own."

## S20 "You join navAjna and get a legacy codebase with no tests and no documentation."

A very likely question, given the JD says you work across multiple client projects.

> "I would not start by refactoring. First I read — trace one important request end to end,
> from the controller through the service to the database, because that teaches you the
> conventions faster than reading files at random.
>
> I would get it running locally and change something small and low-risk, to prove I can build,
> test and deploy it.
>
> Then I would add tests **as I go** rather than as a project — when I touch an area, I write
> a test for the behaviour I am about to change, so it is pinned before I change it. Trying to
> retro-fit full coverage up front never gets finished and nobody thanks you for it.
>
> And I would write down what I learn as I go, because the gaps are obvious to me in week one
> and invisible by week six."

## S21 "A teammate's PR works, but you think the approach is wrong."

> "It depends on how wrong. If it works and is just not how I would have done it, that is my
> preference and I would let it go, or mention it as a non-blocking comment.
>
> If I think it will cause a real problem — a performance issue at scale, something that will
> be hard to change later — I say so, with the specific scenario where it breaks rather than an
> opinion. And I would offer to pair on it rather than leaving a wall of comments, because a
> ten-minute conversation beats a twenty-comment thread."

## S22 "A client stakeholder asks you directly for a change, bypassing the process."

Worth having, because the JD mentions client stakeholders.

> "I would not say no, and I would not just do it. I would understand what they actually need —
> sometimes the ask is a solution and the real need is different.
>
> Then I take it back through the proper channel — my lead or the BA — so it gets prioritised
> and does not quietly displace committed work. What I would not do is silently absorb it,
> because then the sprint slips and nobody knows why.
>
> The tone matters though. 'Let me check how we fit that in and come back to you today' lands
> very differently from 'you need to raise a ticket'."

---

## ✅ The five scenarios to rehearse out loud

If you only prepare five, make them these — they are the most likely and the most revealing:

1. **S8** — the API that is fast in testing and slow in production *(N+1, your strongest ground)*
2. **S9** — two approvers at once *(concurrency, from your own workflow)*
3. **S10** — the missing audit record *(the AOP proxy answer almost nobody gives)*
4. **S1** — the slow list page *(your Lighthouse work, reframed as a problem to solve)*
5. **S20** — the legacy codebase with no tests *(very likely, given their multi-project model)*

**And remember step 5 every time: what you would add so it does not happen again.**
