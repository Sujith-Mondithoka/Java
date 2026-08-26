# 09 · HR, Behavioural & the Offer Conversation 🔴
**Time needed: 45 minutes. Say every answer OUT LOUD.**

Reading these silently is worth about a fifth of saying them. Your mouth needs the
practice, not your eyes.

---

## 1. 🔴 "Tell me about yourself" and the four hard questions

**Your full script for this is in file 10, section "Tell me about yourself".**
It is built from your real Standard Bank experience, so use that version.

File 10 also has prepared answers for the four questions your resume creates, and
you must have all four ready:

1. **"Your last role ended in March. What have you been doing since?"**
2. **"Why did you leave Zensar?"**
3. **"You have Java and Spring Boot. Why a pure frontend role?"**
4. **"How much Next.js have you actually used?"**

Do not walk into the room without solid answers to those. They are the most
predictable questions you will face tomorrow.

**Rules for the opening answer:** under two minutes, no life story starting from
school, and finish on *why this company*. Say it twice tonight and twice in the
morning.

---

## 2. 🔴 "Why WeMakeScholars?" — do the homework, it's 3 sentences

Use their own facts back at them:
> "Three reasons. It's a 10-year-old, 250-person organisation, so it's stable but
> still building — I'd rather own real features than maintain someone else's legacy
> code. Second, the product is free for students and funded under Digital India, so
> the frontend genuinely decides whether someone finds and completes a loan
> application — the work has a visible outcome. Third, it's a search-driven product,
> which means Next.js, SSR and Core Web Vitals aren't optional here. That's the
> skill set I want to grow in."

**Never say:** "I need a job", "I want to learn", "the package is good".
**Do mention** you know they were inaugurated by Dr. Shashi Tharoor / recognised by
Forbes / won the ET award — once, lightly. It shows you read.

---

## 3. 🔴 The filter questions — answer instantly and without hedging

These decide whether you move forward. Hesitation here reads as "will leave in six
months", which is precisely what the 18-month clause exists to prevent.

**"We need an 18-month commitment. Are you comfortable?"**
> "Yes. I'm looking for a place to build depth, not to switch in a year — 18 months
> is about the minimum time to actually own something end to end. I'd just like to
> understand how it's documented in the offer."

*(Asking that follow-up is not a red flag — it's professional. **Do read the clause
before you sign**: ask whether it's a written commitment or a bond with a financial
penalty, and whether any amount is recoverable if you leave early. Ask it calmly
at offer stage, not in round one.)*

**"What's your notice period?"** → **This is an advantage for you. Use it.**
Your Zensar role ended in March, so you are an immediate joiner. Most candidates
they interview will be serving 60 or 90 days.

> "I'm available immediately. I can join as soon as you need me to."

Say it plainly and with a slight lift. For a hiring manager who needs someone
productive this quarter, "immediate" is worth real money and sometimes wins the
offer on its own. *(The 2 month notice in the JD is what you would serve at
WeMakeScholars once employed. It is not a question about you now.)*

**"Are you okay with work from office in Hyderabad?"** → "Yes." Full stop. Don't
open a negotiation you weren't asked to have.

**"1st and 3rd Saturdays are working."** → "That's fine — I saw it in the JD, and
it makes sense given you work with banks."

**"Timings are 10–11 AM login, 8 hours."** → "Works for me."

> ⚠️ If any of these are genuinely a problem for you, say so **now**, politely.
> Accepting and renegotiating later burns the relationship and your reference.

---

## 4. 🔴 Salary — the band is 4 to 6 LPA, and you should be aiming at the top of it

### Your position, honestly
You have about 1 year 4 months of production experience on a real banking platform,
plus an internship, plus full stack ability. **That profile sits at the top of a 4 to
6 LPA band, not the middle.** Candidates with only college projects are the ones who
get placed at 4.

So your target is **6**, and your job in the technical rounds is to earn it before
the number is ever discussed.

### The answer to give
> "I saw the range in the job description and I'm comfortable working within it.
> Given that I've been shipping production React and TypeScript on a banking platform
> for the last year and a half, including the performance work I mentioned, I'd be
> looking at the upper end of that band. But I'm more interested in the role than in
> a specific number, and I'm sure we can agree something if the fit is right."

### If they ask for your previous CTC
Answer honestly with the real figure. Payslip verification is routine, and a lie
found later costs you the offer after you have already resigned from somewhere else.
If your previous CTC was low, do not let it anchor you:

> "That was my package as a fresher joining a service company. I'd expect this role
> to reflect what I can do now rather than what I started on."

### Tactics

- **Never name a number below 4.** That is their published floor. Going under it
  means bidding against yourself.

- **Let them go first if you can.** "What range have you budgeted for this role?" is
  a completely normal question.

- If you want the top of the band, **earn it in the technical round first**, then
  cite it: "Based on the Next.js and performance work we discussed, I'd be looking
  at the upper end."

- Ask **CTC vs in-hand** breakdown at offer stage — how much is fixed, variable,
  and what's deducted. A 6 LPA CTC and a 6 LPA fixed are different jobs.

- Never lie about your current CTC. Payslip verification is routine.

---

## 5. Behavioural questions — answer with **STAR**
**S**ituation → **T**ask → **A**ction → **R**esult. Keep it under 90 seconds and
always land on a result.

**"Tell me about a challenging technical problem."**
Use the dashboard performance story. It is your strongest.
> "**(Situation)** We consolidated four separate modules into one requests page and
> dashboard for corporate users. **(Task)** After the merge the page felt slow, and
> Lighthouse was at 62. **(Action)** I measured first with Lighthouse and the DevTools
> Performance tab rather than guessing. The two real causes were the bundle size,
> because we had merged four modules into one, and unnecessary re-renders, because
> our Redux selectors were creating new arrays on every store update. I added code
> splitting with `React.lazy` and memoised the selectors with `createSelector`.
> **(Result)** Lighthouse went from 62 to 88, about 35% faster on initial load. What I
> took from it is that measuring first saves time, because the obvious suspect is
> often not the real one."

**"Tell me about a challenging bug."**
> "**(S/T)** On the Business Card application, which is fourteen screens, users were
> losing what they had typed when they navigated back a step. **(A)** The cause was
> that each step was holding its own local state, so going back unmounted the
> component and destroyed it. I lifted all the form data into the parent wizard and
> made each step a controlled presentational component. **(R)** The bug went away and
> the code got simpler. Adding a new screen became a small change instead of new state
> logic. It taught me to ask *who should own this state* before writing any of it."

**"A time you disagreed with someone."**
> "We needed an audit trail of who downloaded or emailed each report. The initial
> suggestion was to add logging code inside each of those methods. I was concerned
> about touching a lot of working business logic for something that was really a
> cross-cutting concern. Rather than just objecting, I put together an AOP approach
> using `@Aspect` pointcuts and showed that it captured the same information without
> changing a single line of the existing logic. We went with that. I have learned
> that showing an alternative works much better than arguing about one."

**"Tight deadline?"** → Talk about scoping: shipping the core flow properly and
flagging what you cut, rather than shipping everything half-done. Managers hire
people who communicate trade-offs early.

**"Your weakness?"** → Real, but bounded, plus the fix:
> "I used to over-polish UI details before the feature was fully working. I've
> started building the working version first and reviewing the polish at the end —
> it keeps me from spending an hour on a hover state that gets redesigned anyway."
> *(Never "I'm a perfectionist" or "I work too hard". Both read as rehearsed.)*

**"Where do you see yourself in 3 years?"** → "Owning a significant part of a
frontend codebase — the person who's the reference point for performance and
component architecture on the team." *(Aligns with 18 months. Don't say "starting
my own company" or "moving abroad".)*

**"How do you work with designers?"** → "I go through the design early and ask about
the states the mock doesn't show — loading, error, empty, long text, small screens.
Catching those in a 10-minute conversation is far cheaper than in QA."

**"How do you keep code maintainable?"** → "Small components with one job, clear
naming, no magic numbers, shared logic in custom hooks, and a folder structure
someone new can navigate. My test is whether a teammate can change it without
asking me how it works."

---

## 6. 🔴 Questions YOU ask them — *never say "no, I'm good"*

Have 4 ready; ask 2–3. Ending with no questions reads as no interest.

**Technical (ask these in the tech round):**

1. "Is the frontend on the App Router or Pages Router, and are you migrating?"
2. "How do you currently handle rendering strategy for the public pages — mostly SSG/ISR, or SSR?"
3. "Do you track Core Web Vitals in production, and is there a performance budget?"
4. "What does the frontend-to-backend workflow look like — do you get API contracts up front?"
5. "Is there a shared component library, or does each page build its own?"

**Role / team (ask in the manager or HR round):**

6. "What would a successful first three months in this role look like?"
7. "How big is the frontend team, and would I own features end to end?"
8. "Is there code review, and who reviews frontend work?"

**The one that makes you memorable — ask it in the manager round:**
> "What's the biggest frontend problem you're hoping this hire helps solve?"

Then **listen**, and connect your answer to it. That's how you close.

---

## 7. Logistics for tomorrow

- Laptop charged + charger · backup mobile hotspot · water · pen and notebook.
- 2 printed copies of your resume, plus a copy open on your laptop.
- Your GitHub open in a tab — and **your best 2 projects running**, so "can you show
  me?" gets a yes in five seconds, not a five-minute build.

- Reach 15 minutes early. If it's online, join 5 minutes early and test camera/mic.
- Dress: smart casual — collared shirt. Slightly overdressed beats underdressed.
- Know your own resume cold. **Anything on it is fair game** — if you listed a
  technology you touched once, be ready to say "I've used it at a project level."

---

## 8. If you get stuck in the room

- **Don't freeze, narrate.** "Let me think about that for a second."
- **Don't bluff.** "I haven't used that directly. My understanding is X — is that
  the direction you mean?" That answer has never cost anyone an offer. Bluffing has.

- **Ask for the goal.** "Is the tricky part here the state, or the API side?"
- If you fumble a question, let it go. Candidates lose interviews by mentally
  re-litigating question 4 while answering question 7.
