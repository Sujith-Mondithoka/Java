# 14 · HR, Managerial and the Offer Conversation 🔴
**Time needed: 60 minutes. Say every answer out loud.**

There is usually a separate managerial or HR conversation — with JOY IT rather than IBM — and
it is not a formality.
People clear the technical round and lose the offer here.

---

## 1. "Why this role?" — and be clear who is asking

**Two different people may ask this, and they want different answers.**

### If IBM's panel asks

They want to know why *this work*, not why *this company*. Keep it about the engineering.

> "Three reasons.
>
> The role is Java, Spring Boot and microservices, which is exactly what I have been doing and
> where I want to go deeper. That is a straightforward fit.
>
> Second, I have banking domain experience — I work on a UK private bank's transaction recall
> and card platforms — and IBM runs a lot of financial services work. I would rather build on a
> domain I already understand than start from nothing.
>
> Third, the responsibilities in the spec are the parts I actually enjoy: performance and
> scalability work, troubleshooting production issues, and working directly with QA and
> stakeholders rather than only inside a ticket. I have done all three at Zensar."

That third point is your real differentiator — most candidates at this level talk only about
writing features. Use it.

### If JOY IT asks

They want to know you understand and are comfortable with the arrangement, and that you will not
drop out when you realise the payroll is theirs rather than IBM's. Say so directly:

> "I am clear on the structure — JOY would be my employer and IBM the client. That is the same
> model I work in today: Zensar employs me and the bank is the client, and I have worked that way
> for the last eighteen months. I am comfortable with it, and I know how to work with a client
> team rather than treat them as someone else's problem."

**That answer is worth real money to a vendor recruiter**, because the thing they fear most is a
candidate who accepts and then backs out over the payroll question.

## 2. "Why are you leaving Zensar?"

**Never criticise your current employer.** Frame it as moving toward something.

> "I have had good exposure at Zensar — I have owned features end to end on two banking
> platforms and worked across the full SDLC. What I am looking for now is more depth in
> microservices architecture rather than mostly working within one application, and more
> direct client-facing work. This role is explicitly microservices and consulting
> oriented, which is why I applied."

If asked about compensation, it is acceptable to say it is *a* factor, but never the
first one you mention.

## 3. The JD's own language — prepare these four

The posting is full of consulting phrases. Each one is a question waiting to be asked.

**"How do you handle unclear or incomplete requirements?"** *(the JD's "problem
definition" and "seek clarifications")*
> "I do not start building on an assumption. I write down what I have understood,
> including the gaps, and take it back with specific questions rather than 'please
> clarify'. On the recall workflow there were states where it was not defined who could
> act, so I listed the cases, proposed a default for each, and asked them to confirm.
> That is much faster to answer than an open question, and it gets a decision recorded."

**"How do you estimate effort?"** *(the JD's "effort estimation")*
> "I break the work into pieces small enough to reason about — API changes, data model
> changes, testing, integration — and estimate those rather than the feature as a whole.
> I add time explicitly for testing and for integration issues, because those are what
> people forget. And I flag what the estimate assumes, so if an assumption turns out to
> be wrong the estimate can be revisited rather than just being missed."

**"How do you learn a new technology?"** *(the JD's "research, literature surveys, POCs")*
> "Official documentation first, because tutorials teach you one path and the docs tell
> you the model. Then I build a small proof of concept, because reading does not surface
> the problems. When I picked up Kafka I built a small producer and consumer before
> touching the real system, which is where I actually understood consumer groups and
> offsets. Then I check how it is used in the existing codebase, since conventions there
> matter more than my preferences."

**"How do you approach diagnosing a production issue?"** *(the JD's "diagnose the root
cause")*
Use your real process from file 10, Design 5: reproduce if possible, check logs and
timings, form a hypothesis, verify it before fixing, fix, then add something that would
have caught it earlier. Finish with a concrete example.

## 4. Standard behavioural questions — use STAR

**S**ituation → **T**ask → **A**ction → **R**esult. Under 90 seconds. Always end on a
result.

**"Tell me about a challenging technical problem."** → The 15s → 6s story (file 11).

**"A time you disagreed with someone."** → Best if it is a technical disagreement you
resolved with evidence rather than opinion. The pattern that works: you raised the
concern, then brought data or a working alternative instead of just objecting.

**"A time you made a mistake."** → Have one. Refusing to answer this looks worse than
the mistake. Pick something real, own it plainly, and finish with what you changed. A
missed edge case caught in QA, with "and I added a test for that state transition
afterwards", is a good shape.

**"How do you handle pressure or a tight deadline?"** → Scope, communicate early, do not
silently slip. You worked in SIT and UAT cycles, so you know what happens when something
half-finished reaches testing.

**"What is your weakness?"** → Real, bounded, with the fix.
> "Coming from a non-linear route into development, I was initially slower at reading
> large unfamiliar codebases than people who had been doing it longer. I have got much
> better by tracing one request end to end through the code before changing anything,
> rather than jumping straight to the file I think is responsible."

Never "I am a perfectionist" or "I work too hard".

**"Where do you see yourself in 3 years?"**
> "Owning a service or a module end to end, and being the person on the team who is
> trusted with performance and data-layer problems. Longer term I would like to move
> toward solution design, which is part of why the consulting side of this role appeals."

**"How do you work in a team?"** → Mention code reviews (you do them), QA coordination
(on your resume), and being specific in reviews rather than vague.

## 5. Logistics questions — answer instantly

| Question | How to answer |
|---|---|
| **Notice period** | State it exactly. If it is 60 or 90 days, say so, and mention whether buyout is possible. Do not guess. |
| **Based in / relocate?** | The role is **Hyderabad**. Your resume says "open to relocate anywhere in India / remote", so say it clearly and early. If you are already in or near Hyderabad, say that first — vendors strongly prefer local candidates because joining is faster. Only claim it if it is true; they will hold you to it. |
| **Work from office?** | An IBM client site in Hyderabad will mostly be office-based, and a vendor-payroll role gives you less flexibility to negotiate that. Answer directly rather than hoping. |
| **Shifts / on-call?** | Client projects sometimes need overlap with UK or US hours. You already work with a UK client, so say that — you know what it involves. |
| **Do you have other offers?** | Honest and brief. Do not invent leverage; it usually backfires. |

⚠️ If any of these are genuinely a problem, say so **now**, politely. Accepting and
renegotiating later damages the relationship and your reference.

## 6. Salary

**Know your numbers before the call:** your current fixed CTC, your current total CTC,
and the number you want. Do not do arithmetic live.

**When asked for expectations:**
> "My current CTC is [X]. Based on my experience with Java, Spring Boot, microservices
> and messaging, and my banking domain background, I am looking for [Y]. But I am
> interested in the role and the project, so if the fit is right I am open to discussing
> it."

**Rules:**
- **Never lie about your current CTC.** JOY IT verifies with payslips and Form 16.
  Being caught costs the offer, usually after you have resigned elsewhere.
- **Ask for the breakup** at offer stage: fixed, variable, retention bonus, and what the
  in-hand figure is. Large companies often put a meaningful share in variable pay.
- **Ask how the salary is structured on JOY's payroll** — fixed versus variable, and whether any
  part is tied to the IBM engagement continuing. This matters more in a vendor arrangement than
  in a direct one.
- If they ask first, it is completely normal to ask **"what range have you budgeted for
  this role and level?"**

## 6b. 🔴 The payroll question — JOY IT employs you, IBM is the client

This is new since the earlier version of this guide, and it is the part most candidates handle
badly. **Do not raise it with the IBM panel.** Keep every one of these for Prasanthi at JOY IT,
on the phone, before you accept anything.

**What to establish:**

1. **Is the position permanent with JOY, or tied to the IBM project?** "Full-Time with JOY" in
   the mail suggests permanent, but confirm what happens if the IBM engagement ends — do they
   redeploy you, is there a bench, or does the employment end?
2. **Contract duration**, if there is one, and notice period on both sides.
3. **Conversion.** Has anyone moved from JOY payroll onto IBM's directly, and after how long?
   Ask for the honest answer, not the sales one. A vague answer here is itself information.
4. **Who writes your appraisal** — a JOY manager who does not see your work, or the IBM lead who
   does? This affects your increments more than the starting salary.
5. **Which IBM account and project**, and the day-to-day stack on it. "Java backend at IBM" can
   mean a modern Spring Boot product team or a fifteen-year-old maintenance application, and
   those are very different for your next move.
6. **Benefits** — insurance, PF, leave policy. These are JOY's, not IBM's, and vendors vary a
   lot.
7. **Where you would sit** — IBM's office, JOY's office, or hybrid.

**How to ask without sounding suspicious.** Tone matters; curiosity, not interrogation:

> "I am genuinely interested, and I just want to understand the engagement properly so there are
> no surprises later. Could you tell me how the arrangement works — is it a permanent JOY role
> deployed to IBM, which account it is, and who I would report to day to day?"

**The honest framing for yourself:** vendor payroll at a large client is a completely normal way
to work in Indian IT, and it is exactly what you do now. It is not something to be wary of. But
the terms vary a great deal between vendors, and the time to find out is **before** you resign,
not after.

---

## 7. 🔴 Questions YOU ask them

Have four ready, ask two or three. Ending with "no, I'm good" reads as no interest.

**Technical:**
1. "Which domain would this role sit in — is it financial services, given the skills?"
2. "Is the project greenfield microservices, or modernising an existing monolith?"
3. "What does the current stack look like — Spring Boot version, cloud platform, CI/CD?"
4. "How large is the team, and would I own a service end to end?"

**Role and growth:**
5. "What would a successful first three months look like?"
6. "Is there scope to move toward design and client-facing work over time?"
7. "How does the team handle certification and upskilling for someone at this level?"

**The one that makes you memorable, for the managerial round:**
> "What is the biggest technical problem the team is dealing with right now that this
> hire would help with?"

Then **listen**, and connect your answer to it. That is how you close.

## 8. On the day

- Two printed copies of your resume, and a copy open on your laptop.
- **Know your own resume cold.** Everything on it is fair game — Kafka, RabbitMQ,
  Eureka, JWT, Hibernate lazy loading, MongoDB, execution plans. If you touched something
  briefly, say so honestly rather than overstating.
- Carry your ID, and have your employment and education documents ready — JOY IT
  onboarding is document heavy.
- If it is online: join five minutes early, test camera and microphone, sit somewhere
  quiet with a plain background, and keep an offline copy of your notes in case the
  network drops.
- Dress smart. Slightly overdressed beats underdressed.

## 9. If you get stuck

- **Do not freeze — narrate.** "Let me think about that for a second" is a complete and
  acceptable sentence.
- **Do not bluff.** "I have not used that directly. My understanding is X — is that the
  direction you mean?" has never cost anyone an offer. Bluffing has, because the next
  question exposes it.
- **Ask what they are getting at.** "Do you mean at the database level or in the
  application?"
- If you fumble one question, let it go. People lose interviews by replaying question 4
  while answering question 7.
