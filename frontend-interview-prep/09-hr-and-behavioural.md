# 09 · HR, Behavioural & the Offer Conversation 🔴
**Budget: 45 minutes — and say every answer OUT LOUD.**
Reading these silently is worth about 20% of saying them. Your mouth needs the
reps, not your eyes.

---

## 1. 🔴 "Tell me about yourself" — the first 90 seconds

This is the only answer worth memorising almost word-for-word, because it sets the
tone for everything after. Structure: **Present → Path → Why here.**

> "I'm a frontend developer working primarily with React and JavaScript. Most of my
> work has been building interfaces from designs and wiring them to REST APIs —
> I've built a multi-step form with validation, a paginated data table, an expense
> tracker, and several component-level UI builds, all on my GitHub.
>
> What I've focused on recently is the part beyond 'it works' — how fast the page
> loads, how it behaves on a mid-range phone, and writing components other people
> can reuse.
>
> That's why this role stood out. WeMakeScholars gets students through search, so
> the frontend has to be fast and crawlable — that's exactly the Next.js and
> performance work I want to be doing full-time, and on a product where the page
> loading properly actually decides whether a student gets a loan."

**Rules:** under 2 minutes · no life story from school onwards · end on *why them*.
Practise it twice out loud tonight and twice tomorrow morning. That's it.

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

**"What's your notice period?"** → State it plainly and give a joining date.
"I can join in X days." *(Their own 2-month notice applies once you're employed
there — nothing to answer now.)*

**"Are you okay with work from office in Hyderabad?"** → "Yes." Full stop. Don't
open a negotiation you weren't asked to have.

**"1st and 3rd Saturdays are working."** → "That's fine — I saw it in the JD, and
it makes sense given you work with banks."

**"Timings are 10–11 AM login, 8 hours."** → "Works for me."

> ⚠️ If any of these are genuinely a problem for you, say so **now**, politely.
> Accepting and renegotiating later burns the relationship and your reference.

---

## 4. 🔴 Salary — the CTC is 4–6 LPA, so play the band

**"What are your salary expectations?"**

If you have prior experience / a current CTC:
> "I'm looking in the range of ₹X to ₹Y. That said, I'm more focused on the role
> and the learning here than on a specific number — if the fit is right on both
> sides, I'm confident we can agree on something."

If you're early-career with no strong anchor:
> "I'd like to understand the band for this role first. I saw the JD mentions 4 to 6
> LPA — I'm comfortable within that range, and I'd expect to be placed based on how
> the technical rounds go."

**Tactics:**

- **Don't name a number below 4** — you'd be bidding against yourself under their
  own published floor.

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

**"Tell me about a challenging bug."**
> "In my multi-step form, state was resetting when users moved between steps.
> (S/T) I'd been remounting the step components, so their local state was being
> destroyed. (A) I lifted the form state into the parent and passed values down, so
> each step became a controlled presentational component. (R) The bug went away and
> the code got simpler — adding a new step became a config change instead of new
> state logic. It taught me to ask *who owns this state* before writing it."

**"A time you disagreed with someone."**
> "A design had a filter panel that pushed the content far down on mobile. I flagged
> that it would hurt the mobile experience, but instead of just objecting I built a
> quick version with a collapsible drawer so we could compare. We went with the
> drawer. I've learned that showing an alternative works far better than arguing
> about one."

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
