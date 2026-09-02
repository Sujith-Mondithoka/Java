# 10 · Backend System Design 🟠
**Time needed: 75 minutes**

At this level Infosys will not ask you to design Netflix. But the JD is full of
consulting language — *"problem definition, effort estimation, diagnosis, solution
generation and design"* — so expect one design question, and expect them to be watching
**how you think**, not whether you produce a perfect architecture.

---

## The framework — use it for every design question

```
1. CLARIFY      Ask 2-3 questions. Never start designing immediately.
2. SCOPE        State the core use cases you will design for.
3. API          What endpoints, what request and response shapes.
4. DATA MODEL   Tables or documents, and the key relationships.
5. FLOW         Walk one request end to end.
6. SCALE        What breaks first, and what you would do about it.
```

**Step 1 is the one candidates skip, and it is the one the JD explicitly asks for.**
"Problem definition" is literally in the job description.

**Clarifying questions that fit almost anything:**
- "Roughly what volume are we designing for — hundreds a day or millions?"
- "Is this read-heavy or write-heavy?"
- "Does this need to be strongly consistent, or is eventual consistency acceptable?"
- "Is there an existing system I am integrating with, or is this greenfield?"

That third question is a strong one to ask in a banking context, because the answer is
usually "strongly consistent for money, eventually consistent for notifications" — and
saying that shows domain judgement.

---

## Design 1 🔴 — A notification service
*Most likely for you, because your resume already describes half of it.*

**Clarify:** Which channels — email, SMS, push? Do we need delivery status? Are there
priorities, or is everything equal? Roughly what volume?

**The design:**
```
   Services  ──publish event──►  Kafka topic: notification-requests
                                          │
                                          ▼
                              Notification Service
                                 │  looks up user preferences
                                 │  renders the template
                                 ▼
                      ┌──────────┴──────────┐
                      ▼                     ▼
                 Email worker          SMS worker
                      │                     │
                      ▼                     ▼
                 SMTP provider         SMS gateway
                      │
                      └── failure ──► retry with backoff ──► DLQ after N attempts
```

**The points to make:**
- **Asynchronous, always.** The calling service must never wait for an email. This is
  exactly what you did with RabbitMQ.
- **Preferences and templates** live in the notification service, not scattered across
  callers. One place to change how something is worded.
- **Retry with exponential backoff**, then a dead letter queue, then an alert. Never
  silently drop a notification.
- **Idempotency**: a duplicate event must not send two emails. Key on an event ID and
  record what has been sent.
- **Delivery status** written back so support can answer "did the customer get it?"

Then land it: *"This is close to what I built — the async part with RabbitMQ for emails,
and Kafka for publishing state changes to several consumers."*

## Design 2 🔴 — A transaction recall / approval workflow
*Your actual domain. If they let you pick, pick this.*

**Clarify:** Who can raise a recall, who approves? Is there a time limit? Does it need an
audit trail? Single or multi-level approval?

**Data model:**
```
recall_request
  id, transaction_id, requested_by, reason, status, created_at, updated_at

recall_approval
  id, recall_request_id, approver_id, decision, comments, decided_at

audit_log
  id, entity_type, entity_id, action, actor, before_state, after_state, timestamp
```

**The state machine — draw it, it always impresses:**
```
DRAFT → SUBMITTED → UNDER_REVIEW → APPROVED → COMPLETED
                          │
                          └──────► REJECTED
```

**The points to make:**
- **Model the states explicitly** and validate transitions in one place. An approved
  request must never go back to draft. *(Your resume mentions unit tests for
  state-transition validation — say that here.)*
- **Authorisation server side.** A requester must not be able to approve their own
  request. Enforce in the service layer, not the UI.
- **Append-only audit log.** In banking every state change must be attributable — who,
  what, when, and what it was before. Never update audit rows.
- **Publish each state change as an event** for compliance and reporting consumers.
  That is your Kafka work.
- **Idempotency on submit**, so a double-click does not create two recall requests.

## Design 3 — A URL shortener
The classic warm-up. Know it in case it comes up.

**Core:** `POST /shorten` takes a long URL, returns a short code. `GET /{code}` returns
a **301 or 302 redirect**.

**Generating the code:** a base62 encoding of an auto-increment ID is simple and
collision-free. Hashing the URL is an alternative but needs collision handling.

**Scale points:** it is extremely read-heavy, so cache the code-to-URL mapping in Redis
in front of the database. The lookup must be a primary key or unique index hit.
Mention 301 (permanent, browser caches it, so you lose click analytics) versus 302
(temporary, every click reaches you) — that trade-off is the interesting part.

## Design 4 — "How would you design a REST API for X?"

The generic answer, which is worth having ready:

```
GET    /api/v1/transactions           list, with pagination and filters
GET    /api/v1/transactions/{id}      one
POST   /api/v1/transactions           create      → 201 + Location header
PUT    /api/v1/transactions/{id}      full replace
PATCH  /api/v1/transactions/{id}      partial update
DELETE /api/v1/transactions/{id}      remove      → 204
```

**The rules to state:**
- **Nouns, not verbs.** `/transactions/{id}/recall` as a sub-resource, not
  `/recallTransaction?id=`.
- **Correct status codes.** 201 for created, 204 for no content, 400 for bad input, 401
  vs 403, 404, 409 for a conflict, 422 for validation, 500 for server errors.
- **Pagination on every list endpoint.** Never return an unbounded collection.
- **Versioning** in the URL, and only additive changes within a version.
- **A consistent error shape** across every endpoint, via `@RestControllerAdvice`.
- **Idempotency** for non-safe operations, usually via a client-supplied key.
- **DTOs, never entities, at the boundary.** Returning entities leaks your schema, causes
  lazy-loading surprises during serialisation, and means a database change breaks your
  API contract.

That last point is a genuinely good one and few candidates say it.

## Design 5 — "This API is slow. What do you do?"
*You have lived this. Give a process, not a list of fixes.*

```
1. MEASURE     Where is the time actually going? Application logs and timings first,
               then the slow query log. Do not guess.

2. CATEGORISE  Is it the database, the application, or an external call?
               - Database  → N+1, missing index, bad JOIN
               - Application → inefficient loop, unnecessary object creation
               - External  → a synchronous call that should be async

3. FIX THE BIGGEST ONE FIRST

4. RE-MEASURE  Prove it. Compare before and after.
```

Then make it concrete: *"That is exactly the process that took the report from 15
seconds to 6. The measurement step told me it was N+1 rather than the query itself,
which I would not have guessed."*

**The honest line that scores:** *"My first assumption about the cause was wrong, which
is why I measure before optimising."*

---

## ✅ Check yourself before moving on
1. Recite the six-step framework.
2. Design the notification service out loud in 3 minutes, including retries and DLQ.
3. Draw the recall state machine and say why the audit log is append-only.
4. Give five REST API design rules, including DTOs at the boundary.
