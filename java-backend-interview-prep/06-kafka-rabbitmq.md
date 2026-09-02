# 06 · Kafka and RabbitMQ 🔴
**Time needed: 60 minutes**

This is your **differentiator**. Most candidates at this level have Spring Boot and
Hibernate. Far fewer have used both Kafka and RabbitMQ in production, and your resume
says you used each for a *different reason*. That is the interesting part — be ready to
explain the reasoning, not just name the tools.

---

## First, the context: why messaging at all?

### The problem you actually solved
An approval endpoint that sends an email synchronously:

```java
@PostMapping("/approve/{id}")
public ResponseEntity<?> approve(@PathVariable Long id) {
    cardService.approve(id);          //  200 ms
    emailService.send(...);           //  2-4 seconds, and it can fail or hang
    return ResponseEntity.ok();       //  the user has been waiting the whole time
}
```

Three problems:
1. **The user waits** for something they do not care about.
2. **If the mail server is slow, the API times out** — and to the user it looks like the
   approval failed, even though it succeeded.
3. **Bulk approvals multiply it.** 50 approvals means 50 sequential email sends inside
   the request.

### The fix
```java
@PostMapping("/approve/{id}")
public ResponseEntity<?> approve(@PathVariable Long id) {
    cardService.approve(id);                       // 200 ms
    rabbitTemplate.convertAndSend("email.queue", new EmailMessage(...));  // ~1 ms
    return ResponseEntity.ok();                    // returns immediately
}
```
A separate consumer picks the message up and sends the email. The API responds in
milliseconds. If the mail server is down, the message waits in the queue and is
delivered when it recovers, instead of being lost.

**Say it this way:**
> "The email is not part of what the user is waiting for, so it should not be inside the
> request. Moving it to RabbitMQ meant the API returned immediately, the timeouts during
> bulk approvals stopped, and a mail server outage no longer failed the approval — the
> messages just queued up until it came back."

That is exactly what your resume says you did. Make sure the *reasoning* comes out, not
just the tool name.

---

## Q1. 🔴🔴 Kafka vs RabbitMQ — when do you use which?

**This is the question your resume invites.** You used both, so you will be asked to
justify it.

| | **RabbitMQ** | **Kafka** |
|---|---|---|
| Model | Message **broker** / queue | Distributed **event log** |
| After consumption | Message is **removed** | Message **stays** for its retention period |
| Consumers | Usually one consumer per message | **Many** independent consumers read the same events |
| Replay | No | **Yes** — reset the offset and re-read |
| Routing | Rich — exchanges, routing keys, topics | Simple — topics and partitions |
| Ordering | Per queue | **Per partition** |
| Throughput | High | **Very high** — designed for streams |
| Best for | Task queues, work distribution, RPC-style | Event streaming, audit trails, multiple subscribers |

**The one-line distinction to memorise:**
> "RabbitMQ is a **postbox** — a message is delivered to a worker and then it is gone.
> Kafka is a **ledger** — events are appended and stay there, and any number of consumers
> can read them at their own pace, including re-reading from the past."

### 🔴 Your answer, using your own project
This is the strongest version, because it is true and it shows you chose deliberately:

> "I used them for two different jobs.
>
> **RabbitMQ for the email notifications.** That is a task queue: one message, one
> worker, do the job, and the message is done. I did not need to keep it or replay it —
> I needed the work off the request thread so bulk approvals stopped timing out.
>
> **Kafka for publishing transaction state changes.** That is an event stream, and
> several downstream consumers needed it — compliance logging and report generation, and
> potentially more later. With Kafka each consumer group reads independently at its own
> pace, and because the events are retained, a consumer that was down can catch up, and
> compliance can replay history if it needs to rebuild. With a queue, the first consumer
> would take the message and the others would never see it."

**That last sentence is the technical heart of it.** It shows you understand the
difference rather than having used whatever the team had.

---

## Q2. RabbitMQ concepts

```
Producer → Exchange → (routing rules) → Queue → Consumer
```

The **exchange** is the piece people forget. A producer never sends to a queue
directly; it sends to an exchange, which decides which queues get a copy.

| Exchange type | Routes by |
|---|---|
| **Direct** | Exact routing key match |
| **Topic** | Wildcard pattern — `txn.*.approved` |
| **Fanout** | Copies to **every** bound queue, ignoring the key |
| Headers | Header values |

```java
@RabbitListener(queues = "email.queue")
public void handle(EmailMessage msg) {
    emailSender.send(msg);        // ack on normal return; requeue or DLQ on exception
}
```

**Acknowledgements.** The broker only removes a message once the consumer acknowledges
it. If the consumer crashes mid-processing, the message is redelivered — so processing
must be **idempotent**.

**Dead Letter Queue (DLQ).** Where messages go after repeated failures, instead of being
retried forever or dropped silently. Mentioning DLQs unprompted signals production
experience:
> "Without a DLQ a poison message either blocks the queue or gets retried indefinitely.
> With one, it moves aside after N attempts, gets alerted on, and someone can inspect it
> without holding up everything behind it."

## Q3. Kafka concepts 🔴

```
Topic: transaction-events
├── Partition 0 → [ msg ][ msg ][ msg ]      ← ordered within the partition
├── Partition 1 → [ msg ][ msg ]
└── Partition 2 → [ msg ][ msg ][ msg ]
```

**Topic** — a named stream of events.
**Partition** — a topic is split into partitions, which is how Kafka scales. Order is
guaranteed **within** a partition, not across the topic.
**Offset** — each consumer's position in a partition. Consumers commit their offsets, so
they can resume where they left off.
**Consumer group** — consumers in the same group **share** the partitions, one partition
per consumer at a time. Consumers in **different** groups each get **all** the messages.

That last point is the mechanism behind your answer in Q1: compliance and reporting are
two different consumer groups, so both see every event.

🔴 **How do you guarantee ordering in Kafka?**
> "By partition key. All messages with the same key go to the same partition, and order
> is guaranteed within a partition. So for transaction events I would key by account or
> transaction ID, which guarantees that everything about one transaction is processed in
> order, while different transactions still spread across partitions for throughput."

**Delivery guarantees** — know the three:
- **At most once** — commit the offset before processing. Fast, may lose messages.
- **At least once** — commit after processing. **The common default.** May duplicate, so
  consumers must be idempotent.
- **Exactly once** — possible with Kafka transactions, but costly and complex.

> "In practice most systems run at-least-once and make consumers idempotent, because
> exactly-once across a distributed system is expensive. For financial events I would
> record a processed-message ID and check it before acting, so a redelivery is a no-op."

**Replication.** Each partition has a leader and followers on other brokers. If the
leader dies, a follower is promoted. That is Kafka's durability story.

## Q4. Quick comparison questions

**"Why not just use a database table as a queue?"**
> "It works at small scale, and people do it. But you end up building polling, locking,
> retries, dead-lettering and back-pressure yourself, and polling a table is wasteful and
> adds latency. A broker gives you all of that, plus push delivery."

**"What happens if a message fails?"**
Retry with backoff, then a dead letter queue after N attempts, then alert. Never silently
swallow.

**"What if the same message arrives twice?"**
Idempotency: a unique message ID recorded on the consumer side, or design the operation
so applying it twice has the same effect as once.

**"How do you not lose messages?"**
Producer side: acknowledgements and retries. Broker side: persistence and replication.
Consumer side: acknowledge only **after** successful processing.

---

## ✅ Check yourself before moving on
1. Kafka vs RabbitMQ in one sentence each, then **your** reason for using both.
2. Explain consumer groups and why two groups both receive every event.
3. Explain how ordering works in Kafka and how you would key transaction events.
4. Explain why at-least-once delivery means consumers must be idempotent.
5. Tell the email-timeout story with the reasoning, in 45 seconds.
