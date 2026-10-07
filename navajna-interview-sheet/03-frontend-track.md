# 03 · Round 1 — Frontend Track 🔴🔴
### *The track I would take. Your strongest ground.*

The JD asks for: **React.js and Redux** (components, hooks, state management) · **ES6+ /
TypeScript, HTML5, CSS3** · **REST integration including JWT authorisation** · **Jest unit
testing** · **browser-based debugging** · **working knowledge of Java**.

**You have every one of those in production.** This file is the compressed version — answers,
not explanations.

---

## React — the questions that will come

**Why React?** *"It is declarative — I describe what the UI should look like for a given
state and React works out the DOM changes, instead of me keeping the DOM and the data in sync
by hand. Plus the component model: I built reusable components and Redux patterns used across
three or more features on the platform."*

**Virtual DOM** → a JS object tree; React diffs the new tree against the old (reconciliation)
and applies the minimum real DOM changes, because DOM operations trigger layout and paint.

**Memory — JavaScript keeps things in a stack and a heap too**, the same split as Java:

```js
let count = 5;                    // a number - the value sits in the stack
let user  = { name: 'Sujith' };   // the OBJECT is in the heap,
                                  // `user` holds a reference to it
```
Primitives (number, string, boolean, null, undefined) hold their value. Objects, arrays and
**functions** are heap values, and the variable holds a reference. That single fact explains
three React behaviours at once:

- **Why mutating state does nothing.** `items.push(x)` changes the object in the heap but the
  reference is unchanged, so React's comparison sees the same address and skips the render.
  `[...items, x]` allocates a **new** array at a **new** address, which is what React detects.
- **Why `useCallback` exists.** A function is a heap object. Every render creates a *new* one
  at a *new* address, even though the code is identical — so a `React.memo` child sees a
  "changed" prop. `useCallback` keeps the same object.
- **What the Virtual DOM is.** A tree of plain JS objects in the heap — cheap to build and
  throw away, which is the whole reason the approach works.

**🔴 `key` and why index is dangerous** → A key is a stable identity across renders. With
`key={index}`, deleting the first item makes React think the item at index 0 just changed its
props, so it **reuses the DOM node** — a typed input value stays on the wrong row. With
`key={item.id}` React knows that item is gone and unmounts it. Index is fine only for a
static list that is never reordered or filtered.

**Props vs state** → in from the parent, read-only · owned here, changed via the setter. Data
flows down, events flow up through callbacks. Two siblings need it → **lift the state up**.

### 🔴 What causes a re-render, and how you stop unnecessary ones
Own state changed · props changed · **the parent re-rendered** (even with identical props) ·
context value changed.

Fixes, in order: `React.memo` → `useCallback`/`useMemo` on the props you pass it → **move
state down** → split contexts.

> **Your answer, and it is a strong one:** *"On the platform I took Lighthouse from 62 to 88.
> Two of the three things were render-related: route-based code-splitting with `React.lazy`,
> so each module's JS only downloads when opened, and **memoising the Redux selectors**,
> because unmemoised selectors returned a new array each call, so every connected component
> saw a changed prop and re-rendered on unrelated state changes."*

That is the best technical story you have for this interview. Have it ready.

### Hooks
| Hook | For |
|---|---|
| `useState` | local state |
| `useEffect` | sync with the outside — fetch, timers, subscriptions |
| `useRef` | a value that persists **without** re-rendering; DOM access |
| `useMemo` / `useCallback` | cache a value / a function reference |
| `useContext` | read shared data without prop drilling |
| `useReducer` | complex state with many transitions |

**Rules of hooks** → top level only, never in a condition or loop. **Why:** React tracks
hooks **by call order**, so a skipped hook shifts the order and you get the wrong state.

**`useEffect` dependency array** → no array = every render · `[]` = once on mount · `[x]` =
when x changes. The `return` is **cleanup** — clear timers, remove listeners, abort fetches,
or you leak and get "setState on an unmounted component".

**Memory — this is what a leak in React actually is.** JavaScript frees an object when nothing
references it any more. A timer, an event listener or an open request **still holds a
reference to your component's function and everything it closed over** — so the component is
removed from the screen but cannot be freed.

```jsx
useEffect(() => {
  const id = setInterval(tick, 1000);
  window.addEventListener('resize', onResize);

  return () => {                      // without this, both keep the component alive
    clearInterval(id);
    window.removeEventListener('resize', onResize);
  };
}, []);
```
A page the user opens and closes fifty times then holds fifty live components in memory. That
is the real reason cleanup matters — the console warning is just the symptom.

**Memory — closures.** A closure keeps the whole scope it captured alive. That is what makes
`useState` and debounce work, and it is also why a forgotten listener holds on to so much.

🔴 **When NOT to use `useEffect`** → for anything derivable. `const filtered =
items.filter(...)` during render beats storing it in state and syncing it in an effect.

**Three `useState` traps:** updates are batched so `setCount(c => c + 1)` when the new value
depends on the old · **never mutate** — `items.push()` keeps the same reference so React skips
the render; use `[...items, x]` · `useState(() => expensive())` to run the initialiser once.

**Controlled vs uncontrolled** → React state is the source of truth vs the DOM holds it.
*"I default to controlled — it makes validation and disabling the submit button
straightforward. On the 14-screen Business Card flow I used **React Hook Form**, which keeps
fields uncontrolled for performance so the whole form does not re-render on every keystroke."*

---

## Redux

**Why Redux and not just Context?** → *"Context solves prop drilling but every consumer
re-renders when the value changes, and it does no caching. Redux gives one store, predictable
updates through reducers, and the DevTools action log — which matters when several distant
parts of the app read and write the same state."*

**The flow:** `dispatch(action)` → reducer (pure function: old state + action → new state) →
store updates → connected components re-read.

**Redux Toolkit** → `createSlice` collapses action types, creators and the reducer into one
place. 🔴 **"Why can you write `state.items.push()` in RTK?"** → *"Immer. You mutate a draft
and Immer produces a correctly copied new state, so it is still immutable — it just removes
the spread operators."*

**🔴 Memoised selectors** → `createSelector` from Reselect only recomputes when its inputs
change and returns the same reference otherwise. **This is your Lighthouse story — be ready
to explain it, because you listed it.**

**Memory — say it this way, it is the clearest version of your story:**
```js
// ❌ allocates a NEW array in the heap on every call
const selectPending = state => state.apps.filter(a => a.status === 'PENDING');

// ✅ returns the SAME array reference until state.apps actually changes
const selectPending = createSelector([state => state.apps],
                                     apps => apps.filter(a => a.status === 'PENDING'));
```
> "The unmemoised version returns a new array every time it runs. React compares props by
> reference, not by contents — so even when the data was identical, the address had changed,
> every connected component saw a new prop and re-rendered on unrelated state changes.
> Memoising it meant the same reference came back until the input genuinely changed."

**Trade-off to mention:** memoisation is not free — it stores the last inputs and the last
result, so it trades a little memory for avoided work. Worth it on a hot path, not worth it
everywhere.

---

## JavaScript / TypeScript

- **`var` vs `let`/`const`** → function vs block scope; `const` prevents reassignment, not
  mutation of the object.
- **Closure** → a function that remembers the scope it was created in. It is how `useState`
  and debounce both work.
- **Event loop** → one call stack; slow work goes to the browser, callbacks queue, and
  **microtasks (Promises) drain fully before any macrotask (`setTimeout`)**.
  `console.log('A'); setTimeout(…'B'); Promise.then(…'C'); console.log('D')` → **A D C B**.
- **`==` vs `===`** → always `===`. **`??` vs `||`** → `||` replaces any falsy value, so
  `0 || 10` is 10; `??` only replaces null/undefined.
- **Spread is a shallow copy** — nested objects are still shared.
- **TypeScript, why** → *"It catches a whole class of bugs before the code runs, especially
  around API response shapes, and it makes refactoring safe because the compiler shows every
  place that breaks. I was part of the platform's migration to React 18, Next.js and
  TypeScript."*
- `interface` vs `type` → both describe objects; only `type` does unions. `any` disables
  checking, `unknown` forces you to narrow first.

---

## 🔴 REST integration and JWT — named explicitly in the JD

```jsx
const [data, setData]       = useState([]);
const [loading, setLoading] = useState(true);
const [error, setError]     = useState(null);

useEffect(() => {
  const controller = new AbortController();
  (async () => {
    try {
      setLoading(true); setError(null);
      const res = await fetch('/api/applications', {
        headers: { Authorization: `Bearer ${token}` },
        signal: controller.signal,
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);   // fetch does NOT throw on 4xx/5xx
      setData(await res.json());
    } catch (e) {
      if (e.name !== 'AbortError') setError(e.message);
    } finally { setLoading(false); }
  })();
  return () => controller.abort();          // cleanup: cancel on unmount
}, []);
```

**Three things to point out unprompted:**
1. **`res.ok`** — `fetch` resolves on 404 and 500; only a network failure rejects. You throw.
2. **`AbortController` in the cleanup** — stops the stale-response race condition *and* the
   unmounted-component warning.
3. **The four states: loading, error, empty, success.** *Empty* is the one people forget —
   "No applications match" beats a blank area.

**JWT** → `header.payload.signature`. **Signed, not encrypted** — anyone can base64-decode the
payload, so nothing sensitive goes in it. Sent as `Authorization: Bearer <token>`. The server
validates the signature and expiry, so no session lookup is needed.
🔴 **Storage:** an `httpOnly` cookie is safer than `localStorage`, because JavaScript cannot
read it, so an injected script cannot steal it. **And authorisation must be enforced
server-side** — hiding a button in the UI is not security.
**401 vs 403** → not authenticated vs authenticated but not allowed. Handle 401 in one place
(an axios interceptor) and redirect to login.

---

## Jest and testing — named in the JD

```jsx
test('shows an error when the reference is blank', async () => {
  render(<ApplicationForm />);
  await userEvent.click(screen.getByRole('button', { name: /submit/i }));
  expect(await screen.findByText(/reference is required/i)).toBeInTheDocument();
});
```
**The principle to state:** *"React Testing Library makes you test what the **user** sees and
does — query by role and label, not by class name. The test then survives a refactor: if I
rewrite the internals but the behaviour is the same, it still passes."*

Note the accessibility overlap — if you cannot query by role or label, the markup probably is
not accessible. **You built WCAG 2.1-compliant notification preferences, so you can say that
with a straight face.**

`jest.fn()` for a mock function, `jest.mock('./api')` for a module, `screen.findBy*` (async)
vs `getBy*` (sync) vs `queryBy*` (returns null, for asserting absence).

---

## Browser debugging — the JD asks for this specifically

- **Elements** — inspect the DOM and computed styles; check what CSS is actually winning.
- **Console** — errors and logs.
- **Network** — status codes, payloads, timing, and whether a call even fired. **Throttle to
  Slow 4G** to see what a real user sees.
- **Performance** — record an interaction, find long tasks and layout thrashing.
- **React DevTools Profiler** — *"this is how I found the unnecessary re-renders behind the
  Lighthouse score."*
- **Sources** — breakpoints, step through, inspect scope. Better than `console.log` once you
  are past a trivial bug.

**Core Web Vitals**, in case performance comes up: **LCP < 2.5s** (is it there) · **CLS < 0.1**
(does it stay still — set image dimensions) · **INP < 200ms** (does it respond).

---

## HTML / CSS quick answers
- **Semantic HTML** → `<header> <nav> <main> <button>` — accessibility, SEO, readability. A
  `<button>` is keyboard-focusable and announced correctly; a `<div onClick>` is not.
- **Flexbox vs Grid** → one dimension vs two. `grid-template-columns: repeat(auto-fit,
  minmax(260px, 1fr))` is a responsive grid with no media queries.
- **`box-sizing: border-box`** → width includes padding and border, which is what you expect.
- **Responsive** → mobile-first with `min-width` queries, the viewport meta tag, relative
  units, `clamp()` for fluid type.
- **Centre** → `display: grid; place-items: center`.

---

## ✅ Before you walk in
1. The Lighthouse 62 → 88 story **with the mechanism** — code-splitting, `React.lazy`,
   memoised selectors. In under 60 seconds.
2. The index-as-key failure, with the delete example.
3. The four states, and `res.ok`.
4. What a JWT is, and why it is not secret.
5. The four causes of a re-render and three ways to reduce them.
