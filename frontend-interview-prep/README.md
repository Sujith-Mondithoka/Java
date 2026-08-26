# WeMakeScholars — Frontend Developer Interview Prep
### Your recruiter's war-room plan · Interview: tomorrow 10:00 AM

> **How to use this folder:** Read this file first (10 min). Then work the numbered
> files in order. Every file follows the same 3-part structure as your Java revision
> plan: **Why it exists → Where it's useful → Questions & model answers.**
> Anything marked 🔴 is *highly likely to be asked* — do not skip it.

---

## 1. Recruiter's read on this JD

I've placed dozens of candidates into orgs like this one. Here's what the JD is
actually telling you, line by line:

| What the JD says | What it really means for your interview |
|---|---|
| "React and Next.js" | Next.js is **not** optional garnish. They will ask rendering strategies (SSR/SSG/ISR/CSR) and why. **File 03 is your highest-ROI file.** |
| "Making Things Fast" *(highlighted in their own doc)* | The person who wrote this JD cares about it. Core Web Vitals, image optimization, bundle size, lazy loading. **File 04.** |
| "look great on every device" | Responsive CSS, Flexbox vs Grid, mobile-first. **File 05.** |
| "perform well on search engines" | SEO is a *revenue* function here — they acquire students via Google search. Metadata, semantic HTML, SSR-for-crawlers. **File 04.** |
| "plug REST APIs and data into the frontend" | fetch/axios, loading & error states, race conditions, auth headers. **File 06.** |
| "reusable components, readable, maintainable code" | They will ask you to justify a component API, and probably do a small machine-coding task. **File 07.** |
| "Partnering with designers and product" | Behavioural round. Have stories ready. **File 08.** |
| 18-month commitment, 2-month notice, WFO, 1st & 3rd Sat working | These *will* be asked as filter questions. Scripted answers in **File 08.** |

**The single biggest differentiator in this interview:** most candidates for a
4–6 LPA frontend role can *use* React. Very few can explain **why Next.js exists**
and **what problem SSR solves for an SEO-driven business**. WeMakeScholars lives
or dies on organic search traffic for education-loan keywords. If you connect your
technical answers back to *"this helps your pages rank and load fast for students
on slow mobile networks"*, you will sound like an engineer, not a bootcamp grad.
Say it once in the interview. Once. It lands.

---

## 2. Likely interview structure (my prediction)

For a company of ~250 people hiring at 4–6 LPA, expect **2–3 rounds**, often
compressed into one day:

1. **Technical screening (45–60 min)** — JS fundamentals, React hooks, "explain
   your project", CSS/responsive. Files 01, 02, 05.
2. **Machine coding / live task (45–60 min)** — build a small component:
   search+filter list, a form with validation, a counter/todo/accordion, or an API
   fetch with loading & error states. File 07.
3. **Tech lead / manager round (30 min)** — Next.js, performance, SEO, how you
   work with backend & design, code-quality opinions. Files 03, 04, 06, 08.
4. **HR (20 min)** — commitment, notice period, salary, relocation, working
   Saturdays. File 08.

---

## 3. THE SCHEDULE — from now until 10:00 AM tomorrow

You said you have until 10 AM tomorrow. Time is the scarce resource, so this plan
is **ruthlessly prioritised**. If you fall behind, drop from the bottom, never
from the top.

### 🔥 TODAY — Afternoon / Evening

| Time | Block | File | Goal |
|---|---|---|---|
| **T+0:00 → 0:15** | Read this file | `README.md` | Know the battle plan |
| **T+0:15 → 1:30** | **React core** 🔴 | `02-react.md` | Hooks, state, keys, lifecycle, re-renders |
| **T+1:30 → 2:45** | **Next.js** 🔴🔴 | `03-nextjs.md` | SSR/SSG/ISR/CSR + routing + why it exists |
| **T+2:45 → 3:00** | ☕ Break — walk, no phone | — | Memory consolidates during breaks |
| **T+3:00 → 4:00** | **JavaScript core** 🔴 | `01-javascript.md` | Closures, `this`, async, event loop |
| **T+4:00 → 5:00** | **Performance + SEO** 🔴 | `04-performance-seo.md` | Core Web Vitals — their highlighted line |
| **T+5:00 → 5:45** | Dinner. Actually eat. | — | — |
| **T+5:45 → 6:45** | **Machine coding** 🔴 | `07-machine-coding.md` | Type out 2 problems yourself. Don't read — *build*. |
| **T+6:45 → 7:30** | **Project story** 🔴 | `09-your-projects.md` | Script your 2-min project pitch out loud |
| **T+7:30 → 8:15** | **HR + behavioural** | `08-hr-and-behavioural.md` | Commitment, notice, salary — say them aloud |
| **T+8:15 → 8:45** | REST APIs | `06-rest-api-integration.md` | Skim + the 4 code patterns |
| **By 11:30 PM** | **SLEEP.** | — | Non-negotiable. Tired > underprepared. |

> **Cramming past midnight is a net negative.** A sleep-deprived candidate blanks
> on `useEffect` dependency arrays they knew perfectly at 1 AM. I have watched it
> happen. Go to bed.

### 🌅 TOMORROW — Morning

| Time | Block | File |
|---|---|---|
| **07:00 – 07:20** | Wake, shower, coffee, no phone doomscroll | — |
| **07:20 – 08:00** | **Cheat sheet only** — nothing new | `10-final-cheatsheet.md` |
| **08:00 – 08:30** | HTML/CSS skim | `05-html-css-responsive.md` |
| **08:30 – 09:00** | Say your project pitch + intro **out loud, twice** | `09-your-projects.md` |
| **09:00 – 09:20** | Re-read your questions **for them** | `08-hr-and-behavioural.md` §6 |
| **09:20 – 09:40** | Setup check: laptop, charger, network, ID, resume copies, water | — |
| **09:40 – 09:55** | Close every file. Breathe. Sit up straight. | — |
| **10:00** | **Go.** | — |

**Rule for tomorrow morning: learn NOTHING new.** New material after 07:00 only
displaces what's already consolidated and spikes your anxiety. Revision only.

---

## 4. Files in this folder

| File | Topic | Priority |
|---|---|---|
| `01-javascript.md` | JS fundamentals — closures, `this`, event loop, async, ES6 | 🔴 High |
| `02-react.md` | React — hooks, state, re-renders, keys, context, patterns | 🔴 Highest |
| `03-nextjs.md` | Next.js — SSR/SSG/ISR, routing, App Router, why it exists | 🔴 Highest |
| `04-performance-seo.md` | Core Web Vitals, optimization, SEO — *their highlighted line* | 🔴 High |
| `05-html-css-responsive.md` | Semantic HTML, Flexbox/Grid, responsive, accessibility | 🟠 Medium |
| `06-rest-api-integration.md` | fetch/axios, loading & error states, auth, race conditions | 🟠 Medium |
| `07-machine-coding.md` | Live-coding problems **with full solutions** | 🔴 High |
| `08-hr-and-behavioural.md` | HR filters, salary, commitment + questions to ask them | 🔴 High |
| `09-your-projects.md` | How to pitch *your* GitHub projects | 🔴 High |
| `10-final-cheatsheet.md` | One-page, tomorrow-morning-only revision | 🔴 Read last |

---

## 5. Three rules for the room

1. **Never say "I don't know" and stop.** Say: *"I haven't used that in
   production, but my understanding is X — is that the direction you mean?"*
   Interviewers hire people who reason out loud, not people who recite.
2. **Think out loud in the coding round.** Silence reads as being stuck. Narrate:
   *"I'll hold the input in state, debounce it, then filter the list…"*
3. **Tie answers to their business once.** *"Since students find you through
   Google, SSR matters here more than in a dashboard app."* That one sentence
   makes you memorable in a stack of 40 CVs.

---

## 6. Note on your resume

Your resume PDF lives on your local Windows machine (`C:\Users\sujit\Downloads\…`),
which this session can't read. So `09-your-projects.md` is built from your **public
GitHub repositories** instead. Open that file, check the project details match
what's on your resume, and correct anything that's off — the interviewer will
have the PDF in front of them, so the two must agree.
