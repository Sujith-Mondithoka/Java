# 10 · Talking About Your Experience 🔴
**Time needed: 45 minutes. Say every answer out loud.**

This file is built from your actual resume. Read it carefully, because the
interviewer will have that resume in front of them and will ask about these exact
lines.

---

## First, the context: your real position in this hiring process

Read this properly, because it changes how you should behave in the room.

**You are not a fresher.** You have around 1 year 4 months of production experience
at Zensar, building for Standard Bank South Africa, plus a 5 month internship. You
have shipped features used by 10,000+ corporate banking clients.

Most people applying for this role will have college projects and a bootcamp
certificate. You have:

- Real **production** React and TypeScript in a bank
- Real **performance numbers** (Lighthouse 62 → 88)
- Real **full stack** work (Spring Boot, JPA, PostgreSQL)
- Real **process** experience (SIT, UAT, Bamboo CI/CD, Agile)

**So do not interview like a fresher.** Do not apologise, do not undersell, and do
not say "I only did small parts". Speak like someone who has shipped software that
handles other people's money.

At the same time, do not be arrogant. The formula is: **calm, specific, and always
backed by a number or an outcome.**

---

## Your five best stories

Every behavioural or technical question can be answered from one of these. Learn the
shape of each one. Do not memorise word for word.

| Story | Use it to answer |
|---|---|
| **1. My Requests & Dashboard** | performance, refactoring, Redux, "biggest impact" |
| **2. Business Card (14 screens)** | complex forms, full stack, ownership, scale |
| **3. Recall Transactions (7 screens)** | multi-step forms, accessibility, replacing a manual process |
| **4. Report Logs (AOP audit)** | clean architecture, working without breaking things |
| **5. Notifications (RabbitMQ)** | event-driven thinking, real-time, accessibility |

---

## Story 1 🔴 — My Requests & Dashboard (your performance story)

**This is your strongest story for this specific job,** because their job
description highlights "Making Things Fast".

### The 90 second version
> "Corporate users of the Service Online platform had their requests spread across
> four separate modules. To check the status of something, they had to know which
> module it lived in. We consolidated all of that into one requests page and a
> real-time dashboard, in React 16 with Redux.
>
> The problem after we merged everything was performance. We had pulled four modules
> into one page, so the initial bundle got much bigger and the page felt slow. The
> Lighthouse performance score was 62.
>
> I attacked it in three ways. First, **code splitting with `React.lazy`** so each
> section only downloaded when it was actually opened. Second, **memoising the Redux
> selectors**, because unrelated state updates were re-rendering the whole dashboard.
> Third, general asset cleanup.
>
> That took Lighthouse from **62 to 88**, which was roughly a 35% faster initial
> load. For corporate users checking requests many times a day, that is a real
> difference."

### The follow up questions you will get, with answers

**"How did you know what to fix?"**
> "I measured first. Lighthouse gave the headline score, and the Chrome DevTools
> Performance tab showed where the time actually went. The Network tab showed the
> bundle size problem. I did not guess, because the obvious suspect is often not the
> real one."

**"What is selector memoization, and why did it help?"**
> "In Redux, a selector is a function that pulls a slice of state out of the store.
> If the selector creates a new array or object every time it runs, the component
> sees a new reference and re-renders, even when the underlying data is identical.
> Memoising it with `createSelector` from Reselect means the same input gives back
> the same reference, so the component only re-renders when the data really changed.
> On a dashboard with a lot of small state updates that made a large difference."

**"What is code splitting?"**
> "By default the build produces one big JavaScript file, so the user downloads
> everything even if they open one section. `React.lazy` with `Suspense` splits it
> per section, so the code downloads only when it is needed. The first paint gets
> much faster because there is less to parse."

**"Why was it slow in the first place?"**
Be honest and non-defensive:
> "Because we merged four modules into one page without splitting the bundle. It was
> a predictable consequence of the consolidation. We knew we would have to deal with
> it, and we did."

---

## Story 2 🔴 — Business Card (your ownership story)

### The 90 second version
> "Business Card was a **14 screen onboarding application** for corporate card
> requests, and I built both ends of it.
>
> On the frontend, React with **React Hook Form** and two layers of validation:
> field level rules as the user typed, and a full check before submission. On the
> backend, **Spring Boot with JPA and PostgreSQL**, and a **Camunda BPMN workflow**
> for the approval chain, since a card request has to pass through several approvers
> in order.
>
> Before this, card processing went through a manual branch process. Digitising it
> **cut processing time by around 60%**."

### Follow ups

**"14 screens is a lot. How did you manage the state?"**
This is the strongest technical answer you own. It is also exactly the system design
question in file 08.
> "All the form data lived in one place at the top, not inside each screen. If each
> screen owned its own state, going back a step would unmount that screen and destroy
> what the user had typed. Keeping the data in the parent meant each screen became a
> presentational component that receives values and an onChange, so navigation
> between steps was safe and adding a screen was straightforward."

**"What is Camunda, in simple terms?"**
> "It is a workflow engine. You draw the approval process as a BPMN diagram, with the
> steps and the decision points, and the engine tracks where each request currently
> is. The advantage is that the business rules for who approves what live in the
> workflow rather than being hard coded in Java, so changing the approval chain does
> not mean changing application code."

**"What is dual layer validation?"**
> "Field level validation as the user fills the form, so they get feedback
> immediately, and a full validation before submit so nothing invalid reaches the
> backend. And the backend validates again independently, because frontend validation
> is for user experience, not for security. Anyone can bypass it."

---

## Story 3 — Recall Transactions (your accessibility and UX story)

> "Recall Transactions let corporate clients recall a payment online. Before this it
> could only be done by visiting a branch.
>
> It was a **7 screen workflow** with **navigation guards**, so a user could not skip
> ahead past an incomplete step or lose their work by leaving accidentally. The
> backend was Spring Boot REST APIs with JPA and PostgreSQL, again with a Camunda
> process flow.
>
> Because it was a banking flow, the forms had to be properly accessible: correct
> labels, keyboard navigation, and errors announced to screen readers."

**"What is a navigation guard?"**
> "A check that runs before a route change. If the current step is incomplete or has
> unsaved changes, it either blocks the navigation or asks the user to confirm. In a
> payment recall flow, silently losing a half-completed form would be a serious
> problem."

---

## Story 4 — Report Logs (your clean architecture story)

**Use this when they ask about writing maintainable code.**

> "We needed an audit trail of who downloaded or emailed which report, which is a
> compliance requirement in banking. The obvious approach is to add logging code
> inside every download and email method, but that means touching a lot of working
> business logic and repeating the same lines everywhere.
>
> Instead I used **AOP with `@Aspect` pointcuts**. The aspect intercepts those API
> calls from outside and writes the audit record, so **no existing business logic
> changed at all**. It persists over **50,000 transactions a day** to PostgreSQL, and
> we generated more than a thousand monthly reports with JasperReports."

**Why this story works:** it shows you think about *where* code should live, not just
whether it runs. Say the line "no existing business logic changed" clearly. That is
the point of the story.

---

## Story 5 — Notifications (your event-driven story)

> "Notifications were previously done by polling, so the frontend kept asking the
> server whether anything had happened. That wastes requests and still leaves a
> delay.
>
> I replaced it with an event-driven system over **RabbitMQ**. When something
> happens, a message is published, and the notification is pushed instead of
> discovered. I also built role based notification preferences, and made the
> interface **WCAG 2.1 compliant**."

**"Polling vs event-driven, in one line?"**
> "Polling is the client asking 'anything new?' over and over. Event-driven is the
> server saying 'here is something new' when it actually happens. Fewer requests, and
> no delay."

---

## The QKart project

Mention it briefly if they ask about personal projects.
> "QKart is a full stack e-commerce single page app I built with React, TypeScript,
> Redux and Material UI. Authentication, product discovery, cart and checkout over
> REST APIs. I cut re-renders by about 40% using custom hooks, Context API and
> memoisation."

If they ask **how you measured the 40%**, answer honestly:
> "With the React DevTools Profiler. I recorded an interaction, looked at which
> components were re-rendering and why, and compared the render counts before and
> after."

⚠️ **Make sure the repository and the live demo actually work tonight.** If an
interviewer clicks the link and it 404s, that is worse than not listing it.

---

## 🔴 "Tell me about yourself" — your opening 90 seconds

This is the only answer worth almost memorising. Structure: **Now → What you built →
Why this role.**

> "I am a software engineer with about a year and a half of production experience.
> I was at Zensar working for Standard Bank South Africa, on their Service Online
> platform, which is used by over ten thousand corporate clients.
>
> I worked across the stack. On the frontend, React and TypeScript with Redux. I
> shipped five features there, including a consolidated requests dashboard where I
> took the Lighthouse score from 62 to 88, and two end-to-end self-service
> applications, one of them fourteen screens, where I built both the React frontend
> and the Spring Boot backend.
>
> What I enjoyed most was the frontend side, especially the performance work, and
> that is the direction I want to specialise in. That is why this role interested me.
> WeMakeScholars reaches students through search, so page speed and server rendering
> genuinely affect whether a student finds you and completes an application. That is
> the same kind of problem I was solving at Standard Bank, just with a much more
> direct impact."

**Practise this twice tonight and twice tomorrow morning. Time it. Keep it under two
minutes.**

---

## 🔴 The four hard questions your resume creates

Your resume is strong, but it raises four obvious questions. Prepare all four. Do
not let any of them catch you cold.

### 1. "Your last role ended in March. What have you been doing since?"

There is a gap of a few months. **They will ask.** The rule: answer briefly, without
apologising, and move forward.

Use whichever of these is **actually true for you**, and do not invent anything:

> "I was on the bench at the end of the project and my role was released in March. I
> used the time to move back to Hyderabad and to go deeper on the frontend side,
> specifically Next.js and TypeScript, because that is the direction I want my career
> to go. I have been interviewing selectively rather than taking the first thing
> available."

**The three rules for this answer:**
1. **Keep it short.** Two or three sentences. A long explanation sounds defensive.
2. **Say what you did with the time.** Learning, projects, family reasons, health,
   relocation — whatever is true. The worst answer is "just looking".
3. **Do not apologise.** A gap after a project ends is completely normal in service
   companies. Treat it as normal and they will too.

Then stop talking. Do not fill the silence.

### 2. "Why are you leaving, or why did you leave, Zensar?"

Never criticise your employer or your client. That is the trap.

> "The Standard Bank engagement was a good place to learn, and I got real ownership
> there. Two reasons for moving. First, I want to specialise in frontend rather than
> splitting across frontend and backend, and I want to work with Next.js properly.
> Second, I am based in Hyderabad now and I want to build here rather than in Pune.
> A product company also appeals to me more than services, because I would own a
> feature over time instead of handing it over at the end of a contract."

### 3. "You have Java and Spring Boot. Why do you want a pure frontend role?"

> "I enjoyed both, but the frontend is where I did my best work and where I care
> about the details. The performance work on the dashboard was the most satisfying
> thing I did. Having the backend experience actually helps me here — I can read an
> API, tell whether a response shape will be awkward for the UI, and have a useful
> conversation with the backend team instead of just consuming whatever I am given."

**This is a strength, not a weakness.** Say it as one.

### 4. "How much Next.js have you actually used?"

Be precise and honest. Your resume says you *contributed to* a React 18 / Next.js /
TypeScript migration. That is not the same as owning a Next.js app, and an
experienced interviewer will find the difference in two questions.

> "I contributed to the React 18, Next.js and TypeScript migration on the platform
> rather than starting a Next.js project from scratch. So I have worked in a Next.js
> codebase, and I have built with it outside work. I understand the rendering
> strategies and when to use each, but I would not claim I have run a large Next.js
> app in production on my own."

**Then immediately show the understanding** from file 03. Explain SSG, SSR, ISR and
CSR and which one you would pick for their bank listing pages. Interviewers respect
someone who marks the edge of their knowledge accurately, because it means they can
trust everything inside it.

---

## Questions about your numbers

Any number on your resume is fair game. Know where each one came from.

| Number | Be ready to explain |
|---|---|
| Lighthouse 62 → 88 | Code splitting, `React.lazy`, selector memoization |
| ~35% faster initial load | Derived from the load time improvement, measured in Lighthouse |
| 60% faster card processing | Manual branch process replaced with a digital Camunda workflow |
| 50,000+ daily transactions | Audit records written by the AOP aspect |
| 10,000+ corporate clients | The user base of the Service Online platform |
| Core Web Vitals 65 → 82 | Internship: lazy loading and asset optimisation |
| ~40% fewer re-renders | QKart, measured with the React DevTools Profiler |

⚠️ If you cannot explain how a number was measured, **do not repeat it unprompted**.
A number you cannot defend does more damage than no number at all.

---

## ✅ Before you finish this file
1. Say "Tell me about yourself" out loud, twice. Time it.
2. Say the Dashboard performance story out loud, in 90 seconds.
3. Say your answer for the gap since March. Keep it under three sentences.
4. Check that your QKart repo and live demo both load.
5. Have your GitHub and QKart open in browser tabs tomorrow, ready to show.
