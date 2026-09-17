# 05 · Microservices 🔴🔴
**Time needed: 60 minutes**

**Microservices is named in the role** — Java, Spring Boot and Microservices — and it is in
your resume summary and skills list. **So you will be asked, and you need to be ready for
the depth question**, because your project description is a Spring Boot backend rather than
a distributed system you designed.

**Q7 deals with that directly, and honestly.** Read it before the interview. The short
version: do not claim to have architected a microservices platform. Claim what is true,
then demonstrate that you understand the model and its trade-offs. At 1 year 8 months
nobody expects you to have designed one. They do expect you to know why they exist and what
they cost.

If you are short of time, the highest-value parts are **Q1** (the patterns and what you
give up), **Q2** (how services communicate), **Q3** (circuit breaker) and **Q7**.

---

## First, the context: monolith vs microservices

### The monolith
One deployable application containing everything: users, transactions, reporting,
notifications. One codebase, one build, one database.

**It is not a bad thing.** It is simple to develop, simple to deploy, and a single
transaction can span the whole system. Most applications should start here.

**Where it hurts as it grows:**
- One small change means redeploying everything.
- One memory leak in reporting takes down payments too.
- You cannot scale only the part that is busy — you scale the whole thing.
- A large team constantly blocks itself in one codebase.

### Microservices
Split it into independent services, each owning one business capability, each with its
own database, communicating over the network.

**What you gain:** independent deployment, independent scaling, fault isolation, and
teams that can work without waiting for each other.

**What you pay — say this part, because it shows judgement:**
> "You are trading code complexity for **operational and distributed-systems**
> complexity. Network calls fail, so you need retries and circuit breakers. There is no
> single transaction across services, so you need eventual consistency. Debugging spans
> several services, so you need distributed tracing and centralised logging. It is the
> right trade at a certain scale, but for a small application a well-structured
> monolith is usually the better engineering decision."

That last sentence is what separates a candidate who has *used* microservices from one
who has *read* about them. Interviewers hear the buzzword version all day, and at a bank
the costs are the half they care about — because they are the ones who live with them.

---

## Q1. 🔴 The core patterns — and which you used

```
                     ┌────────────────┐
   Client  ───────►  │  API Gateway   │   single entry point, routing, auth
                     └───────┬────────┘
                             │  asks "where is service X?"
                     ┌───────▼────────┐
                     │ Service Registry│   Eureka
                     └───────┬────────┘
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
  ┌──────────┐        ┌────────────┐       ┌─────────────┐
  │ Auth svc │        │  Ad CRUD   │       │ Master Data │
  │  own DB  │        │   own DB   │       │   own DB    │
  └──────────┘        └────────────┘       └─────────────┘
```

**1. Service Registry / Discovery — Eureka.**
Services are on dynamic hosts and ports, and instances come and go. Hard-coding
addresses does not work. Each service **registers** itself with Eureka on startup and
sends heartbeats; callers **look up** the current instances by service name.
> "Without discovery I would be hard-coding hostnames, which breaks the moment a service
> scales or moves. With Eureka a caller asks for `ad-service` and gets a live list."

**2. API Gateway.**
One entry point for all clients. It handles **routing**, and centralises the things you
do not want to repeat in every service: authentication, rate limiting, CORS, request
logging.
> "Without a gateway the client would need to know every service's address, and every
> service would need its own copy of the auth logic. The gateway puts the cross-cutting
> concerns in one place."

*(This is exactly the "Microservices API Management" the JD asks for. Say the words.)*

**3. Database per service.**
Each service owns its data; no other service touches its tables. This is what makes
independent deployment real — you can change your schema without coordinating with
other teams.
**The cost:** no joins across services, and no single ACID transaction. Which leads to
the next two patterns.

**4. Config Server** — externalised configuration for all services, so a change does not
require a rebuild.

**5. Circuit breaker** — see Q3.

## Q2. How do services talk to each other? 🔴

**Synchronous — REST or gRPC.** The caller waits for a reply.
```java
@FeignClient(name = "master-data-service")     // declarative HTTP client
public interface MasterDataClient {
    @GetMapping("/categories/{id}")
    CategoryDto getCategory(@PathVariable Long id);
}
```
Simple, and you get an immediate answer. But it creates **temporal coupling**: if the
callee is down, the caller fails too. Chains of synchronous calls multiply latency and
failure probability.

**Asynchronous — messaging over Kafka or RabbitMQ.** The caller publishes an event and
moves on.
> "The publisher does not know or care who consumes it, and if a consumer is down the
> message waits in the queue. That removes the temporal coupling. The cost is eventual
> consistency — the effect is not immediate — and harder debugging, because the flow is
> no longer a straight line."

**How to choose — the rule to state:**
> "If I need the answer to continue, synchronous. If I am telling the rest of the system
> that something happened, asynchronous. On a trading platform, calling a payment vendor to
> initiate a transfer is synchronous — I need the result. Telling downstream systems that a
> transaction settled, so they can log it for compliance and update reporting, is the second
> kind: those consumers should not be able to block the transaction from completing."

**A good anchor for you:** Tradu integrated multiple payment vendors. Vendor calls are the
synchronous, must-have-an-answer case — and they are also exactly where timeouts, retries
and circuit breakers matter, which leads into Q3.

## Q3. 🔴 Resilience — circuit breaker, retry, timeout

**The problem:** service A calls B, B becomes slow. A's threads pile up waiting. A runs
out of threads and dies, so C which calls A dies too. One slow service takes down the
system. That is a **cascading failure**.

**Circuit breaker** — three states, know all three:

| State | Behaviour |
|---|---|
| **Closed** | Normal. Calls pass through, failures are counted. |
| **Open** | Failure threshold exceeded. Calls **fail immediately** without trying. |
| **Half-open** | After a wait, let a few test calls through. Success closes it, failure opens it again. |

```java
@CircuitBreaker(name = "masterData", fallbackMethod = "defaultCategory")
public CategoryDto getCategory(Long id) { return client.getCategory(id); }

public CategoryDto defaultCategory(Long id, Throwable t) {
    return CategoryDto.unknown();      // degrade gracefully instead of failing
}
```
Resilience4j is the current library; Hystrix is the older one, now retired.

> "Failing fast protects both sides. The caller does not exhaust its threads waiting,
> and the struggling service gets breathing room to recover instead of being hammered."

**Real-time example.** The advertisement service calls the master data service for
category names. If master data goes down without a circuit breaker, every ad request hangs
on that call until it times out, the ad service's thread pool fills, and the ad service
stops serving requests it could have answered perfectly well. With a breaker and a
fallback, ads still render — just with a placeholder category. **Degraded is much better
than down**, and that sentence is the point of the whole pattern.

Also mention **timeouts** (never make a network call without one) and **retry with
exponential backoff and jitter** — and that you only retry **idempotent** operations,
because retrying a payment could charge someone twice.

## Q4. 🔴 Distributed transactions and the Saga pattern

**The problem:** placing an order must reserve stock, take payment and create a
shipment — in three different services with three databases. There is no `@Transactional`
that spans them.

**Saga** — break it into a sequence of local transactions, each publishing an event that
triggers the next. If a step fails, run **compensating transactions** to undo the
earlier ones.

```
Order created → Payment taken → Stock reserved → Shipment booked
                                       ✗ fails
              ← refund payment  ←  cancel order        (compensation)
```

Two flavours: **choreography** (services react to each other's events — simple, but the
overall flow is not written down anywhere) and **orchestration** (a coordinator drives
the steps — clearer and easier to debug, but it is another component to run).

Mention **eventual consistency**: the system is briefly inconsistent, and the business
has to accept that. In banking that decision belongs to the business, not the developer.

**Real-time example.** A withdrawal spanning services would be: debit the account, call the
payment vendor, record the payout. If the vendor call fails after the account was already
debited, you cannot roll back across two systems — you publish a compensating event that
credits the account back and records why. The compensation is itself an auditable business
action, not a silent undo. In a regulated financial system that is exactly how it has to
work, because the reversal has to be explainable afterwards.

**Idempotency** matters here: a consumer may receive the same message twice, so
processing must be safe to repeat. The usual approach is a unique message or request ID
that you record and check before acting.


**Say this.**
> "Once each service has its own database there is no distributed transaction to fall back
> on, so a business operation spanning services becomes a sequence of local transactions,
> each publishing an event that triggers the next. If a step fails, you cannot roll the
> earlier ones back, so you run **compensating transactions** that undo them as new
> business actions.
>
> The two styles are choreography, where services react to each other's events, and
> orchestration, where a coordinator drives the sequence. Choreography is simpler to start
> but the overall flow is not written down anywhere, so I would prefer orchestration for
> anything with more than about three steps or anything auditable.
>
> The thing to be explicit about with the business is that this is eventual consistency —
> there is a window where the system is partly updated. That is a business decision, not a
> technical one, and in finance it needs to be an informed one."

## Q5. Observability — the question people forget
> "Once a request crosses five services, a stack trace is not enough. You need three
> things. **Centralised logging**, so all logs land in one place — ELK or Splunk.
> **Distributed tracing** with a correlation ID passed through every call, so you can
> follow one request end to end — Sleuth with Zipkin, or OpenTelemetry. And **metrics
> and health checks**, through Actuator and Prometheus, so you see latency and error
> rates per service."

Your resume mentions resolving production incidents by analysing logs, so this connects.

## Q6. Other things they may ask

**How do you version an API?** URL versioning (`/api/v1/...`) is the most common and the
most visible. The real rule is to make **additive** changes — adding an optional field
is backwards compatible; removing or renaming one is not.

**How do you handle security between services?** The gateway validates the JWT once,
then services trust the network boundary, or pass the token along and each validates it.
Service-to-service can use mTLS.

**What is the Strangler Fig pattern?** How you migrate a monolith gradually: put a proxy
in front, move one capability at a time to a new service, and route that path to the new
one. The monolith shrinks until it disappears. Nobody sensible does a big-bang rewrite.

**What is a bounded context?** From domain-driven design — the boundary within which a
model has one consistent meaning. It is the sane way to decide **where to split
services**: by business capability, not by technical layer.
> "The wrong split is a 'database service' and a 'business logic service', because every
> change touches both. The right split is by business capability — orders, payments,
> notifications — so most changes stay inside one service."

**How small should a service be?** Not about lines of code:
> "Small enough that one team can own it and understand it fully, and large enough that
> a typical change does not require modifying three services at once. If every feature
> spans multiple services, the boundaries are wrong."

---

## Q7. 🔴🔴 "Tell me about your microservices experience" — answer this honestly

This is the question to prepare most carefully, because your resume lists microservices but
your project description is a Spring Boot backend for a trading platform. An interviewer
will notice, and the worst outcome is claiming architectural ownership and then unravelling
on the second follow-up.

**The good news:** at 1 year 8 months nobody expects you to have designed a distributed
system. They expect you to be honest about your level and to understand the model. Honesty
plus understanding beats a claim you cannot defend — every experienced interviewer has seen
the second one, and they stop trusting everything else you said.

### The answer to give

> "I should be clear about the level I have worked at. On Tradu I built and consumed REST
> services within a Spring Boot backend — controllers, services, the business components
> behind them, and the APIs the React frontend consumed. The platform integrated multiple
> payment vendors, so I worked across service boundaries and with external APIs, including
> the failure handling that comes with them.
>
> What I have not done is own the architecture of a multi-service system end to end — the
> service decomposition, the discovery and gateway layer. I understand how those work and
> why they are there, and I have been building toward that."

**Then immediately show the understanding**, because this is where you recover the ground:

> "The way I think about it is that microservices buy independent deployment, independent
> scaling and fault isolation, and you pay for it with network failure, no distributed
> transaction, and much harder debugging. So for a small system a well-structured monolith
> is usually the better engineering decision, and the split makes sense when teams start
> blocking each other or one part needs to scale differently from the rest."

**That paragraph is the whole answer.** Most candidates recite the benefits. Saying the
costs, unprompted, is what makes an interviewer think you have actually thought about it.

### Follow-ups you should be ready for

- *"How would you split a monolith?"* → By **business capability**, not technical layer.
  Onboarding, payments, trading, reporting — not "the database service" and "the logic
  service", where every change touches both. Mention the **strangler fig** approach:
  proxy in front, move one capability at a time, never a big-bang rewrite.
- *"How do services find each other?"* → Service discovery, so addresses are not hard-coded
  and instances can scale and move. Eureka is the Spring Cloud implementation; in a
  Kubernetes environment the platform provides it.
- *"What is the API gateway for?"* → One entry point, and the place for cross-cutting
  concerns — authentication, rate limiting, routing — instead of duplicating them in every
  service.
- *"What happens when a downstream service is slow?"* → Timeouts always, then a circuit
  breaker and a fallback. See Q3. **Tie it to the payment vendors on your resume** — a
  vendor that hangs must not take your service down with it.

### 🔴 The one thing not to do
Do not say "yes, I worked on microservices" and leave it there. If you are asked how many
services, how they communicated, or how you handled a partial failure, and you have no
answer, the interviewer discounts everything else you said. **Name your level first.** It
costs you nothing and it buys credibility for the rest of the conversation.

## ✅ Check yourself before moving on
1. Explain monolith vs microservices **including what you give up**.
2. Explain the three circuit breaker states and why failing fast helps both sides.
3. Explain the Saga pattern and compensating transactions.
4. Explain why you would use messaging instead of a REST call, with your Kafka example.
5. Give the honest Q7 answer — your level, then the trade-offs — without notes.
