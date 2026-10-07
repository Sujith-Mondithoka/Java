# 04 · Round 2 — Your Projects, and the Hard Questions 🔴🔴
**Round 2 is explicitly "project experience, problem solving and fitment".** At a company of
this size, the people across the table are likely the people you would work with — so this
round is genuinely about whether they want you on the team.

---

## 🔴 "Tell me about yourself" — your opening 90 seconds

Lead with the stack, land on availability.

> "I am a software engineer with about a year and a half of production experience, most
> recently at Zensar on Standard Bank South Africa's Service Online platform — an enterprise
> banking platform used by around 20,000 corporate clients.
>
> I worked full-stack on it. On the frontend that was React, Redux and TypeScript — I built a
> 14-screen onboarding flow, the My Requests page, and the notification feed, and I took the
> Lighthouse score from 62 to 88 with code-splitting and selector memoisation. On the backend
> I built the Spring Boot, JPA and PostgreSQL services behind those screens, including a
> Camunda approval workflow and an AOP audit system.
>
> Frontend is where my depth is, but I have shipped both, which is why this role interested
> me — and **I am available to join immediately**, so the seven-day window is not a problem."

**Practise this twice tonight.** Time it. The last line is the one they are listening for.

---

## Your four stories

Each: **what it was → a decision you made → what was hard → what you would do differently.**
That last part is what makes an answer sound senior rather than junior.

### Story 1 🔴 — Lighthouse 62 → 88 *(lead with this on the frontend track)*
> "The platform's pages were slow. I profiled with Lighthouse and React DevTools rather than
> guessing. Two things stood out. We were shipping every module in the initial bundle, so I
> added **route-based code-splitting with `React.lazy`** — each module's JavaScript only
> downloads when it is opened. And the **Redux selectors were not memoised**, so they returned
> a new array on every call; every connected component saw a changed prop and re-rendered on
> completely unrelated state changes. Memoising them stopped that.
>
> 62 to 88. What I took from it is to measure first — my first guess about the cause was
> wrong."

That last sentence is worth saying. It shows method, not luck.

### Story 2 🔴 — The AOP audit system *(lead with this on the backend track)*
> "We needed every report download and email captured for compliance. The obvious approach is
> a logging call inside each endpoint, but that is dozens of files and easy for the next
> person to forget. So I used Spring AOP — a pointcut matches the methods and the aspect runs
> around them, so the audit logic lives in one class and the business code is untouched. It
> records 50,000+ transactions a day to PostgreSQL."

**Follow-up to have ready:** *pointcut* selects which methods, *advice* is the code that runs
(`@Before`, `@After`, `@Around`). Spring uses a **proxy**, so — like `@Transactional` — an
internal `this.method()` call does not trigger the aspect. Saying that unprompted is strong.

### Story 3 — Business Card, owned end to end
A 14-screen React onboarding flow with React Hook Form and **two-layer validation**, plus the
Spring Boot / JPA / PostgreSQL backend and a Camunda BPMN approval workflow. **60% off card
processing time.**

**The point to make about the two layers:** *"Client-side validation is for the user's
convenience — it is not a security control, because anyone can bypass the browser and post
straight to the API. So the same rules are enforced server-side."* In a banking context that
lands well.

**On the multi-step form:** all the form state lives in the parent, so moving backwards never
destroys what was entered. React Hook Form keeps fields uncontrolled, so the whole form does
not re-render on every keystroke.

### Story 4 — Recall Transactions, and accessibility
7 accessible multi-step screens with **navigation guards**, Spring Boot REST APIs, JPA and a
Camunda process, replacing a branch-only paper process.
> "A recall is a financial instruction, so a user accidentally hitting back or closing the tab
> midway was a real problem — hence the guards. And the screens were built accessible: labels
> tied to inputs, keyboard navigation, errors announced rather than only shown in red. I did
> the same for the notification preferences, which were WCAG 2.1 compliant."

---

## 🔴🔴 The three questions you must not fumble

### 1. The eight-month gap — prepare this above everything else
You left Zensar in **February**. It is now **October**. That is roughly **eight months**, and
it is the first thing an interviewer will notice.

**Two or three sentences. Factual. Calm. No apology.**

> "[The real reason — the project rolled off / the engagement ended / a personal reason.]
> Since then I have been [specifically what you did]. I was deliberate about wanting a
> hands-on product role rather than taking the next thing available, and I am available to
> start immediately."

**Fill in the truth — do not invent anything.** Project roll-offs are routine in the services
industry and nobody holds one against you.

**But at eight months, "I was upskilling" is not enough.** Be specific and have evidence:
- The **Crio.Do Software Development Fellowship** is on your resume as ongoing — say what you
  have built or completed in it.
- Anything on GitHub since February. Have it ready to show — this is a **face-to-face**
  interview, so you can literally open it.
- The GenAI Level 1 and 2 certifications.

**Then pivot to availability**, which turns the liability into the asset:
> "It does mean I can join inside your seven-day window, which I know matters for this role."

### 2. "You look full-stack. Which do you actually want?"
Do not hedge — hedging reads as not knowing what you want.

> "Frontend is where my depth is — React, Redux and TypeScript are what I work in daily, and
> the performance and component work is what I enjoy most. But I have built and owned the
> Spring Boot backends for the same applications, so I am comfortable across the stack. For
> this role I would want to be on the frontend side, while being useful on backend tickets
> when the team needs it."

*(Swap the emphasis if you decide on backend — but decide.)*

### 3. "Why navAjna?"
Use their own words back at them — the JD talks about working across multiple client projects.

> "Two reasons. The JD says you work across multiple client projects over time, with different
> domains and stacks — that suits me, because I have already worked both ends of a stack and
> been through a migration to React 18, Next.js and TypeScript. I would rather keep learning
> new codebases than do the same thing for three years.
>
> And it is a smaller team than my last project, where I was one of many on a large platform.
> I want work where I own features end to end and see the impact — which I did on Business
> Card and Recall, and that was the most satisfying part of the job."

**Do not say** "it is a good opportunity" or "for growth".

---

## 🔴 Communication is being screened for

The hiring brief for this role says candidates should be **smart in communication skills**,
and the JD asks for *"good communication skills and the ability to collaborate with team
members and client stakeholders."*

**Four things that make the difference in a face-to-face:**

1. **Structure your answers.** "Three things —" then actually give three. It sounds organised
   and it stops you rambling.
2. **Finish your sentences and stop.** Trailing off and over-explaining is the most common
   nervous habit. Say your answer, then be quiet.
3. **If you do not know something, say so cleanly** — *"I have not used that directly. My
   understanding is X — is that the direction you mean?"* That has never cost anyone an
   offer. Bluffing has.
4. **Ask questions back.** It makes it a conversation rather than an interrogation, and in a
   fitment round that is the whole point.

---

## Questions to ask them

Have four, ask two or three. Ending with "no, I'm good" reads as no interest.

1. "Which client project would this role start on, and what is the stack there?"
2. "How is the team structured — would I own features end to end, or work on parts of a larger piece?"
3. "What does the code review and release process look like?"
4. "The JD mentions working across multiple client projects — how often does that rotation happen in practice?"
5. **The closing one:** "What would a successful first three months look like in this role?"

Then **listen**, and connect your answer back to it.

---

## Logistics

| | |
|---|---|
| **Notice period** | **Immediately available.** Say it early and clearly — the JD rules out longer notice periods, so this is your edge. |
| **Location** | Hyderabad, 5 days from office. You are local. Say so. |
| **Salary** | Know your last fixed CTC and your target **before** you walk in. Never inflate — it is verified against payslips. Ask for the fixed/variable split at offer stage. |
| **Education** | B.Tech is explicitly accepted by the JD. You are not disadvantaged by not being CDAC. |
