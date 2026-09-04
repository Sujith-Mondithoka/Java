# 05 · Microservices 🟠
**Time needed: 45 minutes on the current plan**

⚠️ **Read this first.** This posting lists **only Java and Spring Boot** as primary and
preferred skills — microservices is not named. So this file is no longer top priority.

It still matters for two reasons: microservices, Eureka and API Gateway are on **your
resume**, so you will be asked about them, and the JD does say **"validate the
architecture"**, which is a design-review conversation.

**So learn this file for your own project and the trade-offs, not for depth on every
pattern.** If you are short of time, the parts that earn marks are Q1 (the patterns and
what you give up), Q3 (circuit breaker), and Q7 (your Classifieds walkthrough). The rest
is useful but not where this interview will be decided.

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
who has *read* about them. Interviewers at Infosys hear the buzzword version all day.

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
> that something happened, asynchronous. On the recall platform, publishing transaction
> state changes to Kafka for compliance logging and reporting was clearly the second
> kind — those consumers do not need to block the transaction from completing."

**That is your project. Use it as the example.**

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

**Real-time example.** A recall spanning services would be: mark the transaction as
recalled, reverse the ledger entry, notify the customer. If the ledger reversal fails
after the transaction was already marked, you cannot simply roll back across two
databases — you publish a compensating event that returns the transaction to its previous
state and records why. The compensation is itself an auditable business action, not a
silent undo. In finance that is exactly how it has to work.

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

## Q7. Your Classifieds project — how to present it

Have this ready as a 90-second walkthrough:

> "I built a three-service classifieds platform. An **authentication service** issuing
> and validating JWTs, an **advertisement service** with the CRUD operations, and a
> **master data service** for reference data like categories and locations. Each has its
> own database, so they can be deployed independently.
>
> **Eureka** handles service discovery, so services resolve each other by name rather
> than hard-coded addresses. An **API Gateway** sits in front as the single entry point
> and does the routing, which also means authentication is handled in one place rather
> than duplicated in each service.
>
> I added **global exception handling** with `@RestControllerAdvice` so all three
> services return the same error shape, and **DTO validation** with Bean Validation, so
> bad requests are rejected at the boundary rather than deep in the business logic.
> Security is a JWT layer with role-based access control across the services."

**Be ready for the honest follow-ups:**
- *"Did you deploy it?"* — answer truthfully. If it ran locally with Docker Compose, say
  that.
- *"How did you handle a service being down?"* — if you did not add a circuit breaker,
  say so and describe what you would add now. That is a better answer than inventing one.
- *"Why three services and not one?"* — it is a learning project; say so, and then show
  you know the trade-offs from the section above. Honesty plus understanding beats a
  bluff that collapses.

---

## ✅ Check yourself before moving on
1. Explain monolith vs microservices **including what you give up**.
2. Explain the three circuit breaker states and why failing fast helps both sides.
3. Explain the Saga pattern and compensating transactions.
4. Explain why you would use messaging instead of a REST call, with your Kafka example.
5. Give the 90-second Classifieds walkthrough without notes.
