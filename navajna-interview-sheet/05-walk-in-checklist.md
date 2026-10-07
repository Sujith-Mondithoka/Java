# 05 · Walk-In Checklist and One-Page Recall 🔴
**Read the night before, and again in the auto on the way.**

---

## Carry these — the JD lists them explicitly

- [ ] **Updated resume** — 3 printed copies
- [ ] **Government photo ID** — Aadhaar or PAN
- [ ] **Education certificates** — B.Tech degree and marks memos
- [ ] Payslips / offer letter / relieving letter from Zensar, in case they ask
- [ ] Pen and a small notebook
- [ ] Phone charged, with your GitHub and portfolio reachable — **it is face to face, so you
      can actually show your work**
- [ ] Water

**Address:** Level 3 & 4, Karan Arcade, Plot #78, Patrika Nagar, HITEC City, Hyderabad 500081.
**Leave early.** HITEC City traffic is unpredictable and arriving flustered costs you the
first ten minutes. Both rounds are the same day, so expect to be there a while — eat first.

---

## The 10 answers that carry this interview

1. **HashMap** — `hashCode()` → spread `h ^ (h >>> 16)` → bucket `(n-1) & hash`; collisions
   chain, over 8 entries becomes a red-black tree; capacity 16, load factor 0.75, resizes at 12.
2. **equals/hashCode** — equal objects must have equal hash codes, or the map looks in the
   wrong bucket and never finds the entry.
3. **Re-renders** — own state · props · **parent re-rendered** · context. Fix with
   `React.memo` → `useCallback`/`useMemo` → move state down.
4. **`key`** — stable identity. Index breaks on delete or reorder; React reuses the wrong DOM
   node and the typed value stays on the wrong row.
5. **Four states** — loading, error, **empty**, success. Empty is the one people forget.
6. **`fetch` does not throw on 404 or 500** — check `res.ok` and throw yourself.
7. **JWT** — header.payload.signature, **signed not encrypted**, nothing sensitive inside.
   Authorisation must be server-side; a hidden button is not security.
8. **N+1** — one query for the list, one per row for the relation. JOIN FETCH,
   `@EntityGraph`, batch fetch, or a DTO projection.
9. **`@Transactional` / AOP proxy** — an internal `this.method()` call bypasses the proxy, so
   nothing fires.
10. **Microservices** — independent deploy, scale, fault isolation; **cost** is network
    failure, no distributed transaction, harder debugging. *Say the cost.*

---

## Your numbers — say them without hesitating

**20,000+** corporate clients · **Lighthouse 62 → 88** · **60%** off card processing ·
**50,000+** audit transactions a day · **1,000+** monthly reports · **14-screen** onboarding
flow · **7-screen** recall workflow · **3+** features reusing your components ·
**40%** fewer re-renders on QKart · Core Web Vitals **65 → 82** at Pixelvide.

---

## The three sentences that decide this

**Opening:** *"…and I am available to join immediately, so the seven-day window is not a
problem for me."* **Say this in the first two minutes.**

**The gap:** two sentences, the real reason, then **specifically** what you have done since
February — Crio.Do, anything you have built, the GenAI certifications. Then pivot back to
availability.

**Track:** *"Frontend primarily — React, Redux and TypeScript are my day-to-day. But I built
the Spring Boot backends for the same applications, so I can work across both."*

---

## In the room

- **Structure your answers.** "Three things —" then give three.
- **Say your answer and stop.** Over-explaining is the commonest nervous habit.
- **Think out loud in the coding question.** Silence reads as stuck.
- **Ask the edge cases before you code.** Null, empty, duplicates.
- **State the complexity before they ask.**
- **If you do not know it:** *"I have not used that directly — my understanding is X. Is that
  the direction you mean?"* Never bluff; the second question always comes.
- **Ask them questions.** Round 2 is fitment; make it a conversation.

---

## The last five minutes before you walk in

You have shipped five production features on a banking platform used by 20,000 clients, both
ends of the stack, with real numbers attached. For a role asking 1–3 years, that is a strong
profile — and you can start next week, which most of the queue cannot.

Sit up. Breathe out slowly. Smile before you speak.

**Go get it.**
