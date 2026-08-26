# 09 · Pitching Your Projects 🔴
**Budget: 45 minutes — out loud, standing up, twice.**

> ⚠️ **Verify this file against your actual resume.** Your resume PDF is on your
> local machine and this session can't read it, so the project list below comes
> from your **public GitHub repositories**. The interviewer will be reading the
> PDF, so where the two disagree, the PDF wins — edit this file to match.

---

## Why this matters more than any single technical question

At 4–6 LPA, everyone in the pipeline has a todo app. **The differentiator isn't the
project — it's whether you can explain a decision you made inside it.** A candidate
who says *"I used index as key at first and it broke when I deleted rows, so I
switched to ids"* beats a candidate with a flashier project and no story, every
time. Interviewers are listening for evidence you've hit real problems.

---

## Your public repos — the ones worth talking about

| Repo | What it demonstrates | Use it to answer |
|---|---|---|
| **MultistepForm** | multi-step state, validation, controlled inputs | "state management", "forms", "a hard bug" |
| **medify** | API integration, booking/search flow, real app | "REST APIs", "biggest project" |
| **expenseTracker** | CRUD, derived totals, list rendering | "state + derived data" |
| **task-manager** | CRUD, filtering, persistence | "component design" |
| **xpagination** | pagination logic, edge cases, API data | "pagination", "edge cases" |
| **bot-ai** | async flows, streaming/chat UI, loading states | "async", "loading states" |
| **Portfolio / sujith-mondithoka.github.io** | responsive layout, deployment, performance | "responsive design", "SEO/perf" |
| **NFT-project / order-summary-component / XIntroSection** | pixel-accurate design → code | "translating wireframes" ← *the JD's opening line* |

**Pick your top 2** and prepare them properly. Mention the rest only in passing.
I'd lead with **medify** (most app-like) and **MultistepForm** (best decision story).

---

## The 2-minute project pitch — the structure to fill in

Use this skeleton for each of your two main projects:

1. **What it is, in one line.** *"Medify is a doctor-appointment booking app —
   search hospitals by state and city, pick a slot, and it holds your bookings."*
2. **Your stack and why.** *"React with functional components and hooks, React
   Router for routes, and a public REST API for the hospital data. Styled with
   [X] because [reason]."*
3. **One hard problem and how you solved it.** ← **The part they're actually
   listening for.** *"The search results took a noticeable moment and the UI
   flashed empty, so I added explicit loading and empty states rather than
   rendering nothing — and I debounced the input so it wasn't firing a request per
   keystroke."*
4. **One thing you'd do differently now.** ← **The maturity signal.**
   *"I'd move the API calls out of the components into a `useHospitals` custom
   hook — right now the fetch logic is duplicated in two places. And I'd add error
   handling for a failed request, which I skipped."*

**That fourth point is the single highest-leverage sentence in your interview.**
Self-critique reads as senior. It also lets you control the follow-up: they'll ask
about *the thing you already thought through*, not the thing you're weak on.

---

## Prepared answers for the standard project questions

**"Walk me through your biggest project."** → the 4-part pitch above.

**"Why did you choose React for this?"**
> "Component reuse and declarative state. The booking list, the card and the form
> all repeat across pages — writing them once and passing props saved a lot of
> duplication, and I don't have to manually sync the DOM when the data changes."

**"How did you handle state?"**
> "`useState` locally, lifted to the nearest common parent when two components
> needed it. I didn't add Redux — for that size it'd be ceremony. If it grew, I'd
> reach for Context for the user/session and React Query for server data."

**"How did you handle API errors?"** → Be honest. If you didn't handle them fully:
> "Only partially — I handled the loading state but not failures. Reading up on it
> since, I'd wrap the call in try/catch, check `res.ok` because fetch doesn't throw
> on a 404, and render a retry state." *(Honesty + the correct fix beats bluffing.)*

**"How would you make it faster?"** → Pull from file 04: image optimisation, code
splitting the routes, debouncing the search, virtualising the long list, and
measuring with Lighthouse first.

**"How would you add tests?"**
> "React Testing Library for components — testing what the user sees rather than
> internal state — and Jest for utility functions. I'd start with the form
> validation and the booking flow, since those are where a regression actually
> costs something."

**"Did you deploy it?"** → Say where (Netlify/Vercel/GitHub Pages) and mention
anything you hit: environment variables, build config, routing 404s on refresh with
client-side routing. Deployment problems are great, concrete, real-work stories.

---

## 🔴 Tonight's homework — do not skip this

1. **Open your top 2 repos and re-read your own code.** Nothing sinks a candidate
   faster than not recognising code they wrote six months ago.
2. For each, write down: **one decision** you made and **one thing you'd change**.
3. Make sure both **run locally** — `npm install && npm run dev` — and have the
   deployed links ready to paste.
4. Say the 2-minute pitch out loud. Time it. If it's over 2:30, cut the setup.

---

## Bridging thin experience honestly

If Next.js on your resume is tutorial-level, use this line:
> "My production-style work is React; with Next.js I've built at a project level
> rather than shipped at scale. But I understand what it's solving — server
> rendering for SEO and first paint, ISR for content that changes periodically —
> and I'd be able to contribute quickly."

**Then immediately demonstrate it** using file 03. Interviewers respect a candidate
who marks the boundary of their own knowledge accurately, because it means they can
trust everything said inside the boundary. That trust is what gets you hired.
