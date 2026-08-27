# WeMakeScholars — Frontend Developer Interview Prep
### Your plan for tonight and tomorrow morning · Interview: 10:00 AM

---

## How this guide is written

Every topic follows the same shape, so you always know what you are reading:

1. **The context** — what the thing is, and what problem it solves, in plain words.
2. **A simple example** — small code you can actually follow.
3. **Why it matters** — where it is used in real work.
4. **"Say this"** — the answer to give in the room.

You are not meant to memorise the answers. You are meant to understand the idea, so
that when the question comes out slightly differently, you can still answer it.

---

## 1. Where you actually stand

Read this first, because it changes how you should behave tomorrow.

**You are not a fresher.** You have about 1 year 4 months of production experience at
Zensar building for Standard Bank South Africa, plus a 5 month internship. You have
shipped features used by 10,000+ corporate banking clients, and you have real numbers
to prove it (Lighthouse 62 to 88, 50,000+ daily audit transactions, 60% faster card
processing).

Most people applying for this role will have college projects. You have production
React and TypeScript in a bank, plus full stack Spring Boot work.

**Three consequences:**

1. **Do not undersell yourself.** No "I only did small parts". Speak like someone who
   has shipped software that handles other people's money.
2. **Aim at the top of the 4 to 6 LPA band**, not the middle. See file 09.
3. **You are an immediate joiner.** Your last role ended in March, so you can start
   now while most candidates are serving 60 or 90 days. That is worth real money to a
   hiring manager. Say it clearly.

**But your resume also creates four questions you must be ready for:** the gap since
March, why you left Zensar, why a pure frontend role when you have Java, and how much
Next.js you have really used. All four are answered in **file 10**. Do not walk in
without them.

---

## 2. What the job description is really telling you

I have read a lot of these. Here is what each line means for your interview.

| The JD says | What it means for you |
|---|---|
| "React and Next.js" | Next.js is not optional. They will ask about rendering strategies, and they will notice your Next.js is migration work rather than ownership. **File 03 is your biggest opportunity.** |
| "Making Things Fast" *(they highlighted this in their own document)* | The person who wrote the JD cares about it, and **you already have this story** (Lighthouse 62 to 88). **Files 04 and 10.** |
| "look great on every device" | Responsive CSS, Flexbox and Grid, mobile first. **File 05.** |
| "perform well on search engines" | SEO is how this company gets customers. Server rendering, metadata, semantic HTML. **Files 03 and 04.** |
| "plug REST APIs and data into the frontend" | fetch and axios, loading and error states, race conditions. **File 06.** |
| "reusable components, readable, maintainable code" | They will ask how you would design a component, and probably give you a coding task. **Files 07 and 08.** |
| "Partnering with designers and product" | Behavioural round. Have real stories ready. **File 09.** |
| 18 month commitment, 2 month notice, work from office, 1st and 3rd Saturdays | These will be asked as filter questions. Scripted answers in **File 09.** |

### The two things that will set you apart

**First, your performance story.** Their JD highlights speed. You have a real,
measured example of fixing it on a production banking dashboard. Almost nobody at
this level has that. Get it into the conversation early.

**Second, Next.js reasoning.** Almost everyone applying can **use** React. Very few
can explain **why Next.js exists** and **what problem server rendering solves for a
business that depends on Google search**.

WeMakeScholars finds students through organic search. If your technical answers
connect back to *"this helps your pages get found and load fast for students on slow
phones"*, you stop sounding like a bootcamp graduate and start sounding like an
engineer.

Say it **once**, at the right moment. Not five times.

---

## 3. What the interview will probably look like

For a 250 person company hiring at this level, expect 2 or 3 rounds, often on the
same day.

**Round 1 — Technical screening (45 to 60 min).**
JavaScript fundamentals, React hooks, TypeScript, "walk me through your work at
Standard Bank", some CSS.
→ Files 01, 02, 05, 10, 11.

**Round 2 — Machine coding or a live task (45 to 60 min).**
Build a small component. Usually a search and filter list, a form with validation,
or fetching and displaying data.
→ File 07.

**Round 3 — Tech lead or manager (30 min).**
Next.js, performance, SEO, system design, how you work with backend and design.
→ Files 03, 04, 06, 08.

**Round 4 — HR (20 min).**
Commitment, notice period, salary, working Saturdays.
→ File 09.

---

## 4. The schedule — from now until 10:00 AM tomorrow

Time is your scarce resource, so this is ordered by importance. **If you fall
behind, drop things from the bottom, never from the top.**

### Today, afternoon and evening

| Time | What | File |
|---|---|---|
| **0:00 – 0:15** | Read this file | `README.md` |
| **0:15 – 1:30** | **React** 🔴 | `02-react.md` |
| **1:30 – 2:45** | **Next.js** 🔴🔴 | `03-nextjs.md` |

| **2:45 – 3:30** | **Your experience** 🔴🔴 — the 4 hard questions, out loud | `10-your-projects.md` |
| **3:30 – 4:30** | **JavaScript** 🔴 | `01-javascript.md` |
| **4:30 – 5:15** | **TypeScript, state management, testing** 🔴 | `11-typescript-redux-testing.md` |
| **5:15 – 6:00** | Dinner. Actually eat properly. | — |
| **6:00 – 6:45** | **Performance and SEO** 🔴 | `04-performance-seo.md` |
| **6:45 – 7:45** | **Machine coding** 🔴 — type the code, do not read it | `07-machine-coding.md` |
| **7:45 – 8:30** | **System design** 🔴 | `08-system-design.md` |
| **8:30 – 9:15** | **HR answers** — salary, the gap, notice period | `09-hr-and-behavioural.md` |
| **9:15 – 9:45** | REST APIs, quick read | `06-rest-api-integration.md` |
| **By 11:30 PM** | **Sleep.** This is not optional. | — |

> **Studying past midnight will make you worse, not better.** A tired candidate
> blanks on things they knew perfectly at 1 AM. Go to bed.

### Tomorrow morning

| Time | What | File |
|---|---|---|
| **07:00 – 07:20** | Wake up, shower, coffee. No scrolling. | — |
| **07:20 – 08:00** | **Cheat sheet only** | `12-final-cheatsheet.md` |
| **08:00 – 08:30** | HTML and CSS, quick read | `05-html-css-responsive.md` |
| **08:30 – 09:00** | Say your intro and the 4 hard questions **out loud, twice** | `10-your-projects.md` |
| **09:00 – 09:20** | Re-read the questions you will ask them | `09-hr-and-behavioural.md` §6 |
| **09:20 – 09:40** | Check laptop, charger, internet, ID, resume copies, water | — |
| **09:40 – 09:55** | Close everything. Sit up straight. Breathe. | — |
| **10:00** | **Go.** | — |

**Rule for tomorrow morning: do not learn anything new.** New material after 7 AM
only pushes out what you already know and makes you anxious. Revision only.

---

## 5. The files

| File | Topic | Priority |
|---|---|---|
| `01-javascript.md` | Closures, event loop, async, `this`, ES6, debounce | 🔴 High |
| `02-react.md` | Hooks, re-renders, keys, context, controlled inputs | 🔴 Highest |
| `03-nextjs.md` | CSR / SSR / SSG / ISR, App Router, Server Components, SEO | 🔴 Highest |
| `04-performance-seo.md` | Core Web Vitals, how to diagnose slowness, SEO checklist | 🔴 High |
| `05-html-css-responsive.md` | Semantic HTML, box model, Flexbox vs Grid, mobile first | 🟠 Medium |
| `06-rest-api-integration.md` | fetch vs axios, the four states, race conditions, CORS | 🟠 Medium |
| `07-machine-coding.md` | 8 coding problems with full working solutions | 🔴 High |
| `08-system-design.md` | How to answer design questions, with 8 worked examples | 🔴 High |
| `09-hr-and-behavioural.md` | Salary, notice period, STAR stories, questions to ask | 🔴 High |
| `10-your-projects.md` | Your Standard Bank stories + the 4 hard resume questions | 🔴🔴 Highest |
| `11-typescript-redux-testing.md` | TypeScript, Redux, Zustand, React Query, testing | 🔴 High |
| `12-final-cheatsheet.md` | One page. Tomorrow morning only. | 🔴 Read last |

There are also PDF versions in `pdf/`. The cheat sheet is designed to be printed.

---

## 6. Three rules for the interview room

**1. Never just say "I don't know" and stop.**
Say this instead:
> "I have not used that directly. My understanding is that it does X. Is that the
> direction you mean?"

Interviewers hire people who can reason out loud. They do not hire people who can
only recite.

**2. Keep talking during the coding round.**
Silence makes them think you are stuck. Narrate what you are doing:
> "I will hold the input in state, debounce it, then filter the list…"

**3. Connect one answer to their business.**
> "Since students find you through Google, server rendering matters more here than
> it would in an internal dashboard."

One sentence like that is what makes an interviewer remember you out of forty CVs.

---

## 7. A note on accuracy

File 10 is built from your actual resume, so every story in it should match what the
interviewer is reading. If any detail there is wrong, fix it tonight, because they
will ask about the exact lines.

Two things to check before the interview:

- **Your QKart repo and live demo both load.** A dead link is worse than no link.
- **You can explain how every number on your resume was measured.** If you cannot
  defend a number, do not repeat it unprompted.
