# 00 · The AI Round — What They Already Know 🔴🔴
**Time needed: 90 minutes. Do this one FIRST, before any other file.**

---

## What just happened, and why it matters more than you think

You passed the AI screening at **69%**. That got you to Monday, which is what it was for.
But understand what that round actually was, because it changes how you prepare.

**It was not a quiz.** Look at the shape of it. Ten questions, and every single one
followed the same five-rung ladder:

| Rung | What they asked | What they were testing |
|---|---|---|
| 1 | "What does your day to day look like?" | Is the resume real? |
| 2 | "When did you start, has it been continuous?" | Does the timeline hold up? |
| 3 | "Walk me through something you built" | Can you describe your own work? |
| 4 | "What exactly was causing it? What did you change?" | Do you know the **mechanism**? |
| 5 | "How did you decide X over Y?" / "Tell me when it broke" | Did you **own** it, or watch someone own it? |

Rungs 1–3 are cheap. Anyone who did the work can answer them. **Rungs 4 and 5 are where
the marks live**, and they are where a 69 comes from instead of an 85.

Count them in your own transcript. Of the ten questions, **six** were rung 4 or 5:

- "What *exactly* was causing the extra queries?"
- "How did you *decide* which associations stay lazy?"
- "Tell me about a time token handling caused a *real issue*."
- "What happened if the consumer was *down*?"
- "How did you make sure messages were *not lost*?"
- "Walk me through one *production issue* in that event flow, end to end."

That is not an accident. That is the interview design.

---

## 🔴 Rule one: the transcript is now evidence

Monday's panel will very likely have your AI transcript and your score in front of them.
This has two consequences, and the second one is the opportunity.

**First — do not contradict yourself.** Whatever you said yesterday is on record. If you
said the report went from 15 seconds to 6, it is 15 to 6 on Monday too. If you said the
emails went through RabbitMQ, they do not quietly become Kafka. Inconsistency between
rounds is the single fastest way to lose a panel, because it makes everything else you
say suspect.

**Second — they already know where to dig.** A human panel with a 69% transcript does not
re-ask the easy questions. They start at the rung where you got thin and push one level
further. So the ten threads below are not "topics that might come up". They are **the most
likely questions on Monday**, and you now have a weekend to be excellent at exactly them.

That is a large advantage. Most candidates walk in blind. You have the question paper.

### Your consistency sheet — these facts are now fixed

Read this list out loud once. These are on record. Do not improvise new versions.

- Close to **two years** of experience; currently at **Zensar**, client **C. Hoare & Co**,
  a UK private bank.
- Two platforms: **transaction recall** and **business card management**.
- Java, Spring Boot, Spring Data JPA, MySQL, REST, role-based access with **JWT**.
- Report generation: **15 seconds → 6 seconds**, by killing an N+1 and indexing properly.
- Card APIs: **2–3 seconds → under 1 second**.
- **RabbitMQ**: email on approval, moved off the request thread because bulk approvals
  were timing out.
- **Kafka**: transaction state-change events published for **compliance and reporting**.
- Side project: microservices with **Eureka and an API Gateway**.

---

## The ten threads, and where Monday starts

For each one: what they were really testing, the follow-up that is coming, the answer,
and the trap.

---

### Thread 1 — "Give me a quick picture of your day to day"

**What it tested:** whether two years of experience is two years of *engineering*.

**Monday's version is more specific.** Expect: *How big is your team? Who reviews your
code? What is your release cadence? Who writes the stories? How do you get requirements
from the bank?* Vague answers here read as inflated experience, and that suspicion then
colours every technical answer that follows.

**Have these ready as facts, not as feelings:**

- Team size, and how many are backend.
- Your ceremonies — stand-up daily, sprint length (say the number: two weeks), who runs it.
- Code review: who reviews yours, roughly how many PRs a week, what a reviewer usually
  pulls you up on.
- How work reaches you — JIRA from a BA, a client call, a production ticket.
- Your split: roughly how much is new features, how much is defects and support.

**The answer shape:**

> "A sprint is two weeks. Most mornings start with stand-up, then I am on whatever story
> I picked up — usually a new endpoint or a change to an existing one on the card system.
> Work comes in as JIRA stories from our BA, and anything urgent comes in as a production
> ticket from the client side. Everything goes through a pull request before it merges;
> my reviewer is normally our senior developer, and the thing he pushes back on most is
> test coverage on the service layer. Roughly 70% new work, 30% defects and support."

**Trap:** do not say "I work on Java and Spring Boot" and stop. That is rung 1 and it
scores nothing. They asked for a *picture*. Give them the week.

---

### Thread 2 — "When did you first use Java seriously? Has it been continuous?"

**What it tested:** the gap-and-overlap check. They are reconciling your dates.

**Monday's version:** *What were you doing at Artifint?* And, because of your timeline,
possibly: *what have you been doing since June?*

**Answer it flatly and without apology.** Roughly ten months at Artifint in talent
acquisition, then into engineering at Zensar. Do not round the engineering time up —
the band on this JD is 3–6 years, you are under it, they know, and you are in the process
anyway. Candidates lose offers for inflating dates, never for stating them.

If the gap since June comes up, say what you did with it in one sentence — and the
honest answer right now is that you have been strengthening exactly the areas this role
asks for, which is true and is in the rest of this pack. Then stop talking.

**Trap:** over-explaining. One clean sentence, then silence. Section 13 §5 has the full
wording.

---

### Thread 3 — "Something non-trivial in Java — collections, exceptions, or OO design"

**This is your biggest scoring opportunity on Monday, and I think it cost you marks
yesterday.**

Look at what they asked for: **collections, exception handling, or object-oriented
design.** Look at where you went: **Hibernate**. The very next question was "tell me more
about the Hibernate side" — so they followed you, but you answered a *framework* question
when they asked a *language* question.

A human panel will come back for the one you did not give them. Expect:
*Forget the framework for a second — tell me about a time you had to pick a data
structure, or where equals and hashCode mattered.*

**Have a real Java-level story ready. Two good ones from your own work:**

**Option A — grouping in memory instead of querying per row.** This sits right next to
your N+1 story, so it is true and it is connected:

> "When I rewrote the report, part of the fix was in Java, not SQL. Instead of looking up
> each transaction's related rows one at a time, I pulled them back in a single query and
> grouped them in memory with a `Map<Long, List<Detail>>` keyed on the parent id, using
> `Collectors.groupingBy`. That turned N lookups into one pass over the result set.
>
> The reason that is a HashMap and not a list scan is the lookup cost — HashMap hashes the
> key and goes more or less straight to the bucket, so lookup stays flat as the report
> grows. A nested loop over a list would have been O(n×m), which is the same shape of
> problem I had just removed at the database level."

**Option B — equals and hashCode.** This is the classic, and interviewers love it:

> "I hit this with entities in a `HashSet`. Two objects that were the same row were being
> treated as different, because the entity did not override `equals` and `hashCode`, so
> it fell back to object identity. Once I overrode both on the business key, it behaved.
>
> The rule is that if you override `equals` you must override `hashCode`, because a
> HashSet finds the bucket by hashCode first and only then compares with equals. If two
> equal objects return different hashcodes they land in different buckets and never get
> compared. The related trap is mutating a field that is part of the key after the object
> is already in the map — the hashcode changes, the object is in the wrong bucket, and you
> cannot find it again even though it is in there."

**If they push on exception handling**, the answer is your `@RestControllerAdvice`: custom
exceptions for business failures, one handler turning them into proper status codes and a
consistent error body, nothing swallowed, nothing leaking a stack trace to the client.
File 01 has the full version.

---

### Thread 4 — "What exactly was causing the extra queries?"

**You are strong here.** The N+1 story is your best asset and it held up — they went
deeper rather than moving on, which is a good sign.

**Monday's version goes one level down.** Expect any of:

**"How did you *see* it?"** — SQL logging on (`spring.jpa.show-sql`, or better, the
Hibernate statistics / `p6spy`), hit the endpoint once, count the queries. One query for
the list, then the same query repeating once per row with a different id. That repetition
*is* the diagnosis.

**"Why is one query per row so much slower than one query?"** — because the cost is not
the database work, it is the round trip. Each call is a network hop plus parse plus
execute plus result handling. Two hundred rows is two hundred round trips, and latency
multiplies. The database is often barely working while the application waits.

**"You said you used a projection — why not just a fetch join?"** This is the good one,
and here is the answer:

> "A fetch join would have fixed the N+1, and I did use join fetch in places. But for the
> report specifically I went with a projection, because the report only needed about eight
> columns and a fetch join loads whole entities into the persistence context. That means
> Hibernate holds every one of those objects, takes a snapshot of each for dirty checking,
> and compares them at flush — for a read-only report that is pure overhead and real
> memory. A projection selects just the columns into a DTO, nothing is managed, nothing is
> dirty-checked. So the rule I use is: fetch join when I need the entities, projection when
> I only need to display values."

That paragraph alone is worth several points, because almost nobody says the dirty-checking
part.

---

### Thread 5 — "How did you decide which associations stay lazy and which are eager?"

**🔴 I think this is one of the questions that cost you marks.** It is a design-judgement
question, and the honest answer most people give — "I made the important ones eager" — is
the wrong answer. Learn the right one, because it is short and it sounds senior.

**The right answer:**

> "I do not really decide it per mapping — I keep everything lazy in the mapping and make
> eagerness a per-query decision instead.
>
> The reason is that `EAGER` in the mapping is global. Once it is there, every single query
> that touches that entity pays for it, including the ones that never look at the
> association, and you cannot turn it off at query time. Lazy is the opposite — it costs
> nothing by default, and when a particular use case does need the data, I opt in with a
> join fetch or an entity graph for that query only.
>
> The catch people miss is that `@ManyToOne` and `@OneToOne` are **eager by default** in
> JPA, so leaving them alone is already a decision. I set those to `LAZY` explicitly.
> `@OneToMany` and `@ManyToMany` are lazy by default, which is correct.
>
> For the report, the associations stayed lazy and the report query fetched what it needed
> itself. So the same entity stays cheap everywhere else in the application."

**Be ready for the follow-up: "what if you need two collections?"** You cannot fetch-join
two collections in one query — Hibernate throws `MultipleBagFetchException`, and even if it
did not you would get a cartesian product. Options: use `Set` instead of `List`, use
`@EntityGraph`, use two queries, or `@BatchSize` so Hibernate loads the children in batches
of N instead of one at a time.

**And: "what is `LazyInitializationException`?"** You touched a lazy association after the
persistence context closed — usually in the controller or during JSON serialisation, after
the `@Transactional` service method returned. Fix it by fetching what you need inside the
transaction, not by turning on open-session-in-view, which just hides it and holds the
connection longer.

---

### Thread 6 — "Walk me through JWT, login to request validation"

**What it tested:** whether you understand the flow or just used a library.

**Monday's version will be the filter chain.** Expect: *Where does your filter sit? What
does Spring do with the token after you validate it? How does `@PreAuthorize` know the
role?*

**The full walk-through, in order — rehearse this one out loud:**

> "Login hits an authentication endpoint with username and password. I pass those to the
> `AuthenticationManager`, which runs them through the provider against the stored BCrypt
> hash. If it passes, I build a JWT — subject is the user, claims carry the roles, plus
> issued-at and expiry — and sign it. That token goes back to the client, and nothing is
> stored server side, which is the point: the server stays stateless.
>
> On every later request the client sends `Authorization: Bearer <token>`. I have a filter
> extending `OncePerRequestFilter`, registered before
> `UsernamePasswordAuthenticationFilter`. It pulls the token out, verifies the signature
> with the secret, checks expiry, and if that passes it builds an authentication object
> carrying the user and their authorities and puts it in the `SecurityContextHolder`.
>
> From that point Spring Security treats the request as authenticated. The context is held
> in a ThreadLocal for the life of that request and cleared at the end. So when a
> controller method has `@PreAuthorize("hasRole('ADMIN')")`, the method interceptor reads
> the authorities out of that context and decides. The session policy is STATELESS, so no
> HTTP session is created at all.
>
> If the token is missing or bad the entry point returns 401. If the token is fine but the
> role is not allowed, the access denied handler returns 403. That distinction matters —
> 401 means I do not know who you are, 403 means I know and you still cannot."

**One sentence that will impress them, if signing comes up:**

> "We signed with HS256 and a shared secret, which is fine when one service issues and
> verifies. If other teams' services had to verify the token, I would move to RS256 so the
> private key stays with the auth service and everyone else only holds the public key."

---

### Thread 7 — "A time token handling caused a real issue in testing or production"

**🔴 This is the hardest question they asked you, and the most likely to have been thin.**
A vague answer here reads as "I configured security once and it worked", which is a
junior signal.

**Pick ONE of these, whichever actually happened to you, and make it concrete.** All four
are real, common, and show the right instincts:

**(a) The `ROLE_` prefix.** The best one if it is true:

> "Everything authenticated fine but every admin endpoint came back 403. The token carried
> a `roles` claim of `ADMIN`, and my converter was putting `ADMIN` straight in as the
> authority — but `hasRole('ADMIN')` prepends `ROLE_` and looks for `ROLE_ADMIN`, so it
> never matched. I found it by printing the authorities in the security context on a test
> request. The fix was to prefix them in the converter. What it taught me is the difference
> between `hasRole` and `hasAuthority` — `hasRole` adds the prefix for you, `hasAuthority`
> does not, and mixing them is why that bug is so common."

**(b) Expiry and no refresh.** Users were being bounced mid-task — tokens were short-lived
and there was no refresh flow, so a long bulk operation outlived the token. Fix: refresh
token, and the client retries once on a 401 after refreshing.

**(c) Clock skew.** Tokens rejected as expired or not-yet-valid between environments
because the machine clocks disagreed by a few seconds. Fix: allow a small clock skew on
validation and fix NTP on the hosts.

**(d) No revocation — and this is a strong answer because it shows you know the weakness
of the thing you used:**

> "We had to disable a user immediately, and that exposed the real limitation of JWTs:
> they are self-contained, so the server cannot un-issue one. Until it expires it is valid.
> We handled it with short expiry plus a small revocation check on sensitive endpoints,
> but the honest answer is that revocation is the one thing sessions do better than JWTs,
> and if a system needs instant revocation everywhere, that is a reason to think twice
> about stateless tokens."

**Trap:** do not say "we never had any issue." Nobody believes it, and it wastes the
question. If genuinely nothing broke in production, say so and give the testing one — the
question offered you "testing or production" for exactly that reason.

---

### Thread 8 — "Why RabbitMQ instead of a synchronous call?"

**You are strong here, and this is the thing on your resume that sounds most senior** —
you used two messaging systems for two different reasons. Say that explicitly on Monday;
it is a design decision and it reads as such.

**The answer, tightened:**

> "Approvals were sending the email inside the request. One approval was slow. Bulk
> approvals timed out — and that was worse than slow, because the approval had actually
> committed, so the user saw a failure for something that had succeeded and would approve
> it again.
>
> Sending the email is not something the user is waiting for. So the API publishes a
> message and returns, and a separate consumer sends the mail. The API went back to
> responding in milliseconds, and a mail server outage stopped being an API outage — the
> messages just wait.
>
> RabbitMQ rather than Kafka because this is a work queue, not an event log. One job, one
> consumer, done, gone. I wanted competing consumers and per-message acknowledgement, which
> is what Rabbit is built for."

---

### Thread 9 — "What if the consumer was down? The queue backed up? How were messages not lost?"

**🔴 This is the other question I suspect cost you marks**, because the full answer has
five or six parts and most people name two. Learn the whole chain — and notice that it is
a *chain*, where any missing link loses the message.

**Walk it in order, publisher to consumer:**

**1. The publish is confirmed.** Without publisher confirms, `send()` returning does not
mean the broker has it. With `publisher-confirm-type=correlated`, the broker acks and I
know. A publisher return tells me if it was unroutable.

**2. Exchange and queue are durable, and the message is persistent.** Durable means the
queue survives a broker restart; persistent means the message is written to disk rather
than held only in memory. You need both — a persistent message on a non-durable queue
still dies with the broker.

**3. The consumer acknowledges manually, after the work succeeds.** This is the important
one. On auto-ack the message is gone the moment it is delivered, so if the consumer dies
mid-send the email is lost forever. With manual ack I ack *after* the mail server accepts
it; if the consumer dies first the message was never acked and Rabbit redelivers it.

**4. Retry with backoff, then a dead letter queue.** Not infinite requeue — a message that
can never succeed (bad address) would otherwise spin forever and block the queue. So:
a few retries, then route it to a DLQ via `x-dead-letter-exchange`, and the DLQ is
monitored so a human sees it.

**5. Prefetch is limited.** Without it one consumer grabs a large batch of unacked
messages; if it dies they all have to be redelivered, and the other consumers sit idle.

**6. The consumer is idempotent.** Because all of the above gives you *at-least-once*
delivery, not exactly-once. A redelivery must not send the same email twice, so the
consumer checks whether that notification was already sent before sending.

**Now the "consumer down / backing up" half, and this is where you can shine:**

> "If the consumer is down, the messages accumulate in the queue, which is the point —
> nothing is lost and the API is unaffected. What I would watch is queue depth, because a
> backlog is not free. RabbitMQ has a memory high watermark, and if the broker crosses it,
> it applies flow control and starts blocking publishers. So a consumer that has been dead
> long enough eventually slows down the API that publishes — the problem comes back round.
> That is why queue depth gets an alert rather than just a dashboard.
>
> The fix for a backlog is horizontal: more consumers on the same queue, competing for
> messages. And you can bound the damage up front with a message TTL and a max queue
> length, so old messages dead-letter instead of filling the broker."

**One honest sentence to add if you did not personally configure all of this:** "Some of
that was already in place on the project and I worked within it — the part I set up myself
was X." Honesty on the boundary costs you nothing and buys you credibility everywhere else.

---

### Thread 10 — "Kafka for compliance logging — what were you publishing, and why Kafka?"

**They flagged this one themselves: "I want to come back to that."** When an interviewer
says that, it means the thread was interesting and underexplored. **It is close to certain
this comes up on Monday.** Give it real time this weekend.

**What you were publishing — be concrete about the event:**

> "Transaction state changes. When a recall moved state — raised, approved, rejected,
> settled — the service published an event carrying the event id, the transaction id, the
> previous state, the new state, who performed it, and the timestamp. Keyed on the
> transaction id.
>
> The shape matters: it is a fact that already happened, named in the past tense, and it is
> immutable. Compliance does not want the current state of a row — they want the history of
> who did what, when. A database row tells you where things ended up. The event stream tells
> you how they got there."

**Why Kafka and not RabbitMQ — four reasons, and the first is the real one:**

**1. Retention.** RabbitMQ is a queue: once a message is acked it is gone. Kafka is a log:
messages stay for the retention period whether or not anyone read them. For compliance
that is the whole point — the record has to still exist afterwards.

**2. Replay.** Because the log is still there, a consumer can reset its offset and reprocess.
When reporting had a bug, we fixed the consumer and re-read from an earlier offset. With a
queue that data would already have been deleted on ack and the only recovery is from source.

**3. Multiple independent consumers.** Compliance and reporting are separate consumer
groups reading the same partitions, each with its own offset, neither affecting the other.
Adding a third consumer later needs no change to the producer. On Rabbit you are into
fan-out exchanges and a queue per consumer, and it is still deleted on ack.

**4. Ordering per key.** Keying on transaction id puts every event for one transaction on
the same partition, and a partition is ordered. So the compliance view of a single
transaction is guaranteed to be in sequence. Kafka gives no ordering *across* partitions —
and that distinction is worth saying out loud, because it is the next question.

**The one-liner to close on:**

> "Rabbit was a work queue — one job, one consumer, done and gone. Kafka was a durable
> record several teams read independently and can re-read. Different problems."

---

### Thread 11 — "A production issue in that event flow, tracked down end to end"

**This was the last question, and "end to end" is the key phrase.** They want the *method*,
not just the bug. Marks come from the sequence: symptom → where you looked first → what
that ruled out → the actual cause → the fix → what you changed so it could not recur.

**Four templates. Pick the one that really happened.** The first is the most common and the
most impressive:

**(a) Out-of-order events, because of the partition key.**

> "Compliance reported that a transaction showed as approved before it showed as raised.
>
> First thing I checked was whether we had published them in the wrong order — we had not,
> the producer logs had the right sequence with the right timestamps. That ruled out the
> service.
>
> The cause was the partition key. The events for that transaction were going out without a
> key, so Kafka spread them across partitions, and ordering only holds *within* a
> partition. Two consumers on two partitions processed them in whatever order they arrived.
>
> The fix was to key every event on the transaction id, which guarantees all events for one
> transaction land on the same partition and stay in order. And I made the consumer defensive
> as well — it ignores a state change older than the one it has already recorded — because
> ordering is a guarantee I would rather not be the only line of defence."

**(b) Duplicates in the compliance store.** Same event recorded twice after a consumer
restart or a rebalance, because Kafka is at-least-once and the offset had not been
committed before the crash. Fix: a unique constraint on the event id and an upsert, making
the consumer idempotent. The lesson line: "at-least-once means the consumer has to be
idempotent — that is not optional, it is part of the design."

**(c) Growing consumer lag.** Compliance events arriving minutes late. Found it by watching
consumer group lag climbing while the producer rate was flat — so the problem was the
consumer, not the volume. Inside the consumer was a slow synchronous call per message.
Fixed by batching and increasing partitions plus consumers so the work parallelised.

**(d) Missing events.** The publish happened inside a transaction that later rolled back,
or the producer send failed asynchronously and nobody checked the callback — so the row
changed and no event was ever recorded, which for compliance is the worst outcome. Fix: a
transactional outbox — write the event to an outbox table in the same database transaction
as the state change, and a separate publisher reads the outbox and sends it. Now the event
and the state change cannot disagree.

**However you tell it, mention how you *traced* it:**

- A correlation id carried on the event and put into the logging MDC, so one id finds the
  request in the API logs and the matching record in the consumer logs.
- Consumer group lag, to tell "stuck" apart from "slow" apart from "not published".
- Counting what was published against what was stored for a time window, to prove whether
  anything was actually missing.

---

## 🔴 The six specifics that most likely cost you the 31%

A 69 is not "wrong answers". A 69 is correct answers without the detail that proves you
were the one who did it. These six things turn a 69-shaped answer into an 85-shaped one:

1. **Name the config, not just the concept.** Not "we made sure messages weren't lost" but
   "durable queue, persistent message, manual ack after the send, three retries then DLQ."
2. **Give the number.** 15 to 6. 2–3 to under 1. Two-week sprints. Three retries. Numbers
   are the cheapest credibility there is.
3. **Say what you ruled out.** "I assumed the query was heavy, turned on SQL logging, and
   my assumption was wrong" scores higher than going straight to the right answer, because
   it shows method rather than memory.
4. **Name the trade-off you accepted.** Projection instead of fetch join, and why. Rabbit
   instead of Kafka, and why. HS256 and when you would move to RS256. Every real decision
   has a cost; naming it proves you made the decision rather than inherited it.
5. **Say what you would do differently.** One sentence at the end of each story. This is
   the single strongest senior signal available to you, and it is free.
6. **Mark the boundary out loud.** "The cluster was the platform team's — what my service
   had to provide was X." Admitting a limit makes everything else you claim believable.

---

## The 20-minute drill — do this twice before Monday

Set a timer. Say these out loud, standing up, no notes. Record yourself once if you can
stand listening to it.

1. Your day to day, with the numbers in it — **60 seconds**.
2. The N+1 story, ending with why a projection and not a fetch join — **2 minutes**.
3. Lazy by default, eager per query, and `@ManyToOne` is eager unless you say otherwise —
   **60 seconds**.
4. JWT login to request validation, in order, ending on 401 versus 403 — **2 minutes**.
5. The token bug you picked, with the symptom first — **90 seconds**.
6. The six-link chain for not losing a Rabbit message — **2 minutes**.
7. Kafka versus Rabbit for compliance, four reasons, ending on the one-liner — **2 minutes**.
8. The event-flow bug, symptom → ruled out → cause → fix → prevention — **2 minutes**.

If any of those eight comes out vague, that is your study for the evening — not a new
topic. **You already know what they are going to ask. Almost nobody gets that.**

---

## ✅ Check yourself before moving on

- [ ] I can state my eight fixed facts without hesitating or changing a number.
- [ ] I have a Java-level story (collections or equals/hashCode) that is not Hibernate.
- [ ] I can say why a projection beats a fetch join for a read-only report.
- [ ] I can say why lazy belongs in the mapping and eager belongs in the query.
- [ ] I have picked ONE token bug and can tell it symptom-first.
- [ ] I can name all six links in the message-durability chain.
- [ ] I can give four reasons for Kafka over RabbitMQ for compliance.
- [ ] I have picked ONE event-flow bug and can tell it end to end, including how I traced it.
