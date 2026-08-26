# 02 · React 🔴 (Highest priority)
**Budget: 75 minutes** · This is the core of the role. Expect 15–20 minutes of
pure React questioning plus a coding task built on it.

---

## Where React fits (the "why" answer — lead with this)

> "Before React, updating a page meant hand-writing DOM manipulation — find the
> node, change it, keep it in sync with your data. That gets unmaintainable fast.
> React flips it: you describe **what the UI should look like for a given state**,
> and React figures out the minimal DOM changes. It's declarative instead of
> imperative. On top of that, the component model means a `LoanCard` or `BankRow`
> is written once and reused across the whole site — which is what the JD means by
> 'reusable components'."

---

## Q1 🔴 What is the Virtual DOM? How does reconciliation work?

"The Virtual DOM is a lightweight JS object tree describing the real DOM. When
state changes, React builds a new tree, **diffs** it against the previous one, and
applies only the changed nodes to the real DOM. Real DOM operations are expensive —
they trigger layout and paint — so batching the minimum set of them is the win."

**Diffing heuristics (this is the senior-sounding detail):**
1. Different element **type** → tear down the old subtree, build a new one.
2. Same type → keep the node, update only changed attributes.
3. Lists are matched by **`key`**.

**"Is the Virtual DOM faster than direct DOM manipulation?"** — a trick question.
"Not inherently — hand-optimised DOM code can beat it. The Virtual DOM buys
*predictability and maintainability* at a very good performance level, and stops
me from accidentally writing something much slower."

---

## Q2 🔴 Why do lists need a `key`? Why is index a bad key?

"`key` gives React a stable identity for each item across renders. Without it,
React falls back to position, so inserting at the top makes it think every item
changed."

**The example that proves you actually understand it:**
"With `key={index}`, if I have a list of inputs and delete the first item,
React sees the item that *was* index 1 now at index 0 and just updates its props —
so the typed value from the deleted row stays visible on the wrong row. With a
stable `key={item.id}`, React knows that item is gone and unmounts it correctly."

Index is acceptable **only** when the list is static, never reordered, filtered,
or added to.

---

## Q3 🔴 Props vs State

| Props | State |
|---|---|
| Passed **in** from parent | Owned **inside** the component |
| Read-only (immutable to the child) | Mutable via the setter |
| Change → parent re-renders child | Change → this component re-renders |
| Like function arguments | Like a local variable that persists |

**Follow-up: "How does a child update the parent?"**
→ "The parent passes a callback down as a prop; the child calls it. Data flows
down, events flow up — that's one-way data flow. If a value is needed by two
siblings, I **lift the state up** to their nearest common parent."

---

## Q4 🔴 `useState` — the three traps they test

```js
const [count, setCount] = useState(0);
```

**Trap 1 — state updates are asynchronous and batched.**
```js
setCount(count + 1);
setCount(count + 1);   // only +1 total — both read the same stale `count`
setCount(c => c + 1);
setCount(c => c + 1);   // +2 — functional updater gets the latest value
```
"Use the functional form whenever the new state depends on the old."

**Trap 2 — never mutate state.**
```js
items.push(newItem); setItems(items);       // ❌ same reference, no re-render
setItems([...items, newItem]);              // ✅ new reference
setUser({ ...user, verified: true });       // ✅
```
"React compares with `Object.is`. Same reference means 'nothing changed'."

**Trap 3 — lazy initial state.** `useState(expensiveFn())` runs on *every* render;
`useState(() => expensiveFn())` runs once.

---

## Q5 🔴 `useEffect` — dependency array, cleanup, and when NOT to use it

```js
useEffect(() => { /* runs after every render */ });
useEffect(() => { /* runs once on mount */ }, []);
useEffect(() => { /* runs when `id` changes */ }, [id]);
useEffect(() => {
  const t = setInterval(tick, 1000);
  return () => clearInterval(t);            // cleanup: on unmount + before next run
}, []);
```

**What effects are for:** synchronising with something *outside* React — data
fetching, subscriptions, timers, direct DOM/browser APIs, analytics.

🔴 **"When should you NOT use useEffect?"** — a strong-candidate question:
"For anything derivable from existing state. If I have `items` and a `query`, the
filtered list is just `items.filter(...)` computed during render — putting it in
state plus an effect adds an extra render and a whole class of sync bugs."

**Cleanup matters:** without `clearInterval`/`removeEventListener`/`abort`, you
leak memory and get "can't update state on an unmounted component" warnings.

**Why an effect runs twice in dev:** React 18 StrictMode intentionally
mounts→unmounts→remounts to surface missing cleanup. Development only.

---

## Q6 🔴 All the hooks — one line each

| Hook | Purpose |
|---|---|
| `useState` | local state |
| `useEffect` | side effects / sync with outside systems |
| `useContext` | read context without prop drilling |
| `useRef` | mutable value that **doesn't** trigger re-render; DOM access |
| `useMemo` | cache an expensive **value** between renders |
| `useCallback` | cache a **function reference** between renders |
| `useReducer` | complex state with many transitions (Redux-lite) |
| `useLayoutEffect` | like `useEffect` but fires **before paint** (measure DOM) |
| Custom hook | any reusable `useXyz` function that calls other hooks |

**🔴 Rules of Hooks + why:** Only call hooks at the **top level** of a component or
custom hook — never inside conditions, loops, or nested functions. "React tracks
hooks by **call order**, not by name. A conditional hook shifts the order between
renders and React hands you the wrong state."

---

## Q7 🔴 `useMemo` vs `useCallback` vs `useRef`

```js
const filtered   = useMemo(() => items.filter(i => i.bank === bank), [items, bank]); // caches a VALUE
const handleAdd  = useCallback((id) => setCart(c => [...c, id]), []);               // caches a FUNCTION
const inputRef   = useRef(null);                                                     // persists, no re-render
```

- `useCallback(fn, deps)` **is** `useMemo(() => fn, deps)`.
- They only pay off when the child is wrapped in `React.memo`, or when the value
  is a dependency of another hook, or the computation is genuinely expensive.

🔴 **"Should you wrap everything in useMemo?"** → "No. Memoization isn't free —
it costs memory and a dependency comparison every render. Premature memoization
adds noise. I profile with React DevTools first, then memoize the hot path."
*That answer alone separates you from most candidates at this level.*

**`useRef` two uses:** (1) grab a DOM node — `inputRef.current.focus()`;
(2) hold a mutable value across renders without re-rendering — a timer ID, a
previous value, an "is first render" flag.

---

## Q8 🔴 What causes a re-render? How do you stop unnecessary ones?

**Causes:** own state changed · props changed · parent re-rendered · context value
changed. (Note: **a parent re-rendering re-renders all children by default**, even
if their props are identical.)

**Fixes, in the order I'd apply them:**
1. `React.memo(Child)` — skip re-render if props are shallow-equal.
2. `useCallback` / `useMemo` on props passed into memoized children (otherwise a
   fresh function/object reference defeats `React.memo` every time).
3. **Move state down** — keep it in the smallest component that needs it.
4. **Lift content up / `children`** — pass an expensive subtree as `children` so
   it isn't recreated by the re-rendering parent.
5. Split contexts so an unrelated update doesn't re-render every consumer.

---

## Q9 🔴 Controlled vs uncontrolled components

```jsx
// Controlled — React state is the single source of truth
<input value={email} onChange={e => setEmail(e.target.value)} />

// Uncontrolled — the DOM holds the value, you read it via ref
<input ref={emailRef} defaultValue="" />
```
"I default to controlled: it makes validation, conditional disabling of the submit
button, and formatting straightforward. Uncontrolled is fine for simple forms or
file inputs (`<input type="file">` is always uncontrolled), and it avoids a
re-render per keystroke on very large forms."

---

## Q10 Context API — and its limits

```jsx
const AuthContext = createContext(null);
<AuthContext.Provider value={{ user, login }}>{children}</AuthContext.Provider>
const { user } = useContext(AuthContext);
```
**Solves:** prop drilling — passing `user` through five layers that don't use it.
**Good for:** theme, auth/current user, language, cart.
🔴 **Limit:** "Context isn't a state manager and it isn't optimised for frequent
updates — **every consumer re-renders when the value changes**. If the value is an
object literal in the Provider, that's a new reference every render, so everything
re-renders. I memoize the value, and split high-frequency state into its own
context or reach for Redux Toolkit / Zustand when the state graph gets big."

---

## Q11 Class vs Function components / lifecycle mapping
| Class | Hook equivalent |
|---|---|
| `componentDidMount` | `useEffect(fn, [])` |
| `componentDidUpdate` | `useEffect(fn, [dep])` |
| `componentWillUnmount` | the cleanup `return` inside `useEffect` |
| `this.state` / `setState` | `useState` / `useReducer` |

"Function components with hooks are the standard now — less boilerplate, no `this`,
and logic is reusable through custom hooks instead of HOCs and render props.
I can read classes in legacy code, but I write functions."

---

## Q12 Custom hooks — *have one ready, it's a green flag*
```js
function useDebounce(value, delay = 500) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const t = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(t);
  }, [value, delay]);
  return debounced;
}
// usage: const q = useDebounce(query); useEffect(() => { search(q) }, [q]);
```
"A custom hook is just a function starting with `use` that calls other hooks. It
shares **stateful logic**, not state — two components using `useDebounce` get
independent state. I've used `useFetch`, `useDebounce`, and `useLocalStorage`."

---

## Q13 Error boundaries · Suspense · lazy
```jsx
const Dashboard = React.lazy(() => import('./Dashboard'));
<Suspense fallback={<Spinner />}><Dashboard /></Suspense>
```
- `React.lazy` + `Suspense` → **code splitting**: that route's JS downloads only
  when needed, shrinking the initial bundle (ties directly to file 04).
- **Error boundary** = a class component with `componentDidCatch` /
  `getDerivedStateFromError` that renders a fallback instead of a white screen.
  "Hooks can't do this yet — it's the one place I still write a class, or use
  `react-error-boundary`."

---

## Q14 State management — what would you pick and why?
"Local `useState` first. Shared-but-simple → Context. Server data → **React Query
/ SWR**, because most 'global state' is actually cached server state and those
libraries give you caching, refetching, and loading/error states for free.
Genuinely complex client state → Redux Toolkit or Zustand. I wouldn't put Redux
in a project this size just to hold a user object — that's ceremony without value."

---

## Q15 Quick-fire
- **Fragment?** `<>...</>` — group children without an extra DOM wrapper node.
- **JSX?** Syntax sugar compiled to `React.createElement()`. Browsers never see JSX.
- **Why `className`?** `class` is a reserved word in JS.
- **Prop drilling?** Threading props through components that don't use them → Context.
- **Composition over inheritance?** React has no component inheritance — you nest
  and pass `children`.
- **Conditional render?** `{isLoading && <Spinner/>}` or a ternary. ⚠️ `{count && …}`
  renders a literal `0` when count is 0 — use `count > 0 &&`.
- **Can `key` be a prop you read?** No, `key` is consumed by React itself.
- **`React.memo` vs `useMemo`?** memo = component; useMemo = value.

---

### ✅ Self-check before moving on
1. Explain re-render causes and three ways to reduce them.
2. Write `useDebounce` from memory.
3. Say the "index as key" failure case out loud in 20 seconds.
