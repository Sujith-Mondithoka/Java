# 02 · React 🔴 (Most important technical file)
**Time needed: 75 minutes**

This is the main skill for the job. Expect 15 to 20 minutes of React questions,
plus a coding task built on React.

---

## First, the context: what problem does React solve?

### Life before React
To change something on a page, you had to find the element and change it by hand:

```js
document.getElementById('count').innerText = count;
document.getElementById('warning').style.display = count > 5 ? 'block' : 'none';
document.getElementById('btn').disabled = count === 0;
```

This is called **imperative** code. You give step by step instructions.

The problem is keeping everything in sync. If `count` changes in five places, you
must remember to update all three lines in all five places. Miss one and the screen
shows the wrong thing. In a big app this becomes impossible to manage.

### What React does instead
You describe **what the screen should look like for a given state**. React works
out what to change in the page.

```jsx
function Counter({ count }) {
  return (
    <div>
      <p>{count}</p>
      {count > 5 && <p>That is a lot</p>}
      <button disabled={count === 0}>Reset</button>
    </div>
  );
}
```

You never touch the DOM. You change `count`, and React updates the screen.
This is called **declarative** code.

### The second big idea: components
A component is a reusable piece of UI. Write `<LoanCard />` once, use it on the home
page, the search page and the comparison page. This is what the job description
means by "reusable components".

### Say this
> "React is declarative. Instead of writing instructions to change the DOM, I
> describe what the UI should look like for the current state, and React updates the
> DOM for me. That removes a whole class of bugs where the screen and the data go
> out of sync. The component model also means I build something like a loan card
> once and reuse it everywhere."

---

## Q1. What is the Virtual DOM? 🔴

### What it means
The real DOM is the actual page in the browser. Changing it is **slow**, because
the browser may have to recalculate layout and repaint pixels.

The Virtual DOM is a **plain JavaScript copy** of what the page should look like.
It is just an object in memory, so making it is cheap and fast.

### How an update works
1. State changes.
2. React builds a **new** Virtual DOM tree.
3. React compares it with the **previous** tree. This comparison is called
   **diffing**.

4. React finds the smallest set of real changes and applies only those.

Example: a list of 100 rows and you change one name. React does not rebuild 100
rows in the browser. It changes one piece of text.

### The rules React uses when comparing
- Different element type (`<div>` became `<span>`)? Throw away the old one, build new.
- Same type? Keep the element, only update the attributes that changed.
- For lists, match items by their **`key`**.

### A trick question: "Is the Virtual DOM faster than direct DOM manipulation?"
The honest answer scores better than "yes".
> "Not always. Hand written DOM code can be faster if it is done perfectly. The
> Virtual DOM gives you very good performance without you having to think about it,
> and it makes the code much easier to maintain. That trade is worth it."

---

## Q2. Why do lists need a `key`? Why is index a bad key? 🔴

### What a key does
A key is a **name tag** for each item in a list. It tells React "this is the same
item as before" across renders.

```jsx
{loans.map(loan => <LoanCard key={loan.id} loan={loan} />)}
```

Without keys, React can only go by position. If you insert an item at the top, React
thinks every item changed, and does far more work than needed.

### Why index is dangerous, with a concrete example
Say you have three text inputs:

```
index 0 → Apple    (user typed "hello" in this box)
index 1 → Banana
index 2 → Cherry
```

Now delete **Apple**. The array becomes `[Banana, Cherry]`.

With `key={index}`:
```
index 0 → Banana   ← React thinks: "item 0 is still here, its text just changed"
index 1 → Cherry
```
React **reuses** the first input box. The text "hello" the user typed is still
sitting in it, but now it is next to Banana. The data moved but the DOM did not.

With `key={item.id}`:
React sees that the item with id "apple" is gone. It removes that input box
completely, along with the typed text. Correct behaviour.

### When is index acceptable?
Only when the list never changes order, never gets items removed, and has no
internal state. A static footer menu is fine. Anything the user can edit is not.

---

## Q3. Props vs State 🔴

### The simple difference
- **Props** come from **outside** (the parent). The child cannot change them.
- **State** lives **inside** the component. The component can change it.

Think of a component as a function. Props are the arguments passed in. State is a
variable it keeps for itself.

```jsx
function LoanCard({ bank, rate }) {          // props, given by the parent
  const [expanded, setExpanded] = useState(false);   // state, owned here

  return (
    <div>
      <h3>{bank} — {rate}%</h3>
      <button onClick={() => setExpanded(!expanded)}>
        {expanded ? 'Hide' : 'Show'} details
      </button>
    </div>
  );
}
```

### How does a child send data back to the parent?
Data flows **down** through props. Events flow **up** through callbacks.
The parent passes a function down, and the child calls it.

```jsx
// Parent
<SearchBar onSearch={(text) => setQuery(text)} />

// Child
<input onChange={(e) => props.onSearch(e.target.value)} />
```

### "Lifting state up"
If two sibling components need the same value, neither can own it. Move the state
**up** to their closest shared parent, then pass it down to both.

```
        Parent  ← state lives here
       /      \
  SearchBar   ResultList
```

---

## Q4. `useState` — the three traps 🔴

```jsx
const [count, setCount] = useState(0);
//     ↑ value   ↑ function to change it   ↑ starting value
```

### Trap 1: state updates are not instant
```jsx
setCount(count + 1);
setCount(count + 1);
// count only goes up by 1, not 2
```
Both lines read the same old `count`. React batches the updates and applies them
after the current work finishes.

**Fix — use the function form.** React passes you the latest value:
```jsx
setCount(c => c + 1);
setCount(c => c + 1);
// now it goes up by 2 ✅
```
Rule: if the new value depends on the old value, use the function form.

### Trap 2: never change state directly
```jsx
items.push(newItem);
setItems(items);          // ❌ screen does not update
```
React checks "is this the same object as before?" It is the same array, just with
one more item inside. So React decides nothing changed and skips the re-render.

```jsx
setItems([...items, newItem]);              // ✅ a brand new array
setUser({ ...user, verified: true });       // ✅ a brand new object
```
Always create a new array or object.

### Trap 3: expensive starting values
```jsx
useState(readFromLocalStorage())      // ❌ runs on every single render
useState(() => readFromLocalStorage())// ✅ runs once, on the first render
```

---

## Q5. `useEffect` 🔴

### What it is for
`useEffect` is for talking to things **outside** React. For example:

- fetching data from an API
- setting a timer
- adding a browser event listener
- saving to localStorage

### The dependency array controls when it runs
```jsx
useEffect(() => { ... });           // after EVERY render (rarely what you want)
useEffect(() => { ... }, []);       // once, when the component appears
useEffect(() => { ... }, [userId]); // when userId changes
```

### Cleanup: the part people forget
The function you `return` from an effect is the cleanup. React runs it when the
component disappears, and before running the effect again.

```jsx
useEffect(() => {
  const id = setInterval(tick, 1000);

  return () => clearInterval(id);   // ← cleanup
}, []);
```

Without cleanup, the timer keeps running after the component is gone. It tries to
update a component that no longer exists. That is a memory leak, and you will see
warnings in the console.

Things that need cleanup: timers, event listeners, API subscriptions, and in flight
fetch requests.

### 🔴 When should you NOT use useEffect?
This question separates good candidates from average ones.

**Do not use an effect for data you can calculate.**

```jsx
// ❌ Wrong: extra state, extra render, and it can go out of sync
const [filtered, setFiltered] = useState([]);
useEffect(() => {
  setFiltered(items.filter(i => i.bank === bank));
}, [items, bank]);

// ✅ Right: just calculate it while rendering
const filtered = items.filter(i => i.bank === bank);
```
The second version is shorter, has no extra render, and can never be stale.

### Why does my effect run twice in development?
React 18 StrictMode mounts your component, unmounts it, and mounts it again on
purpose. It does this to reveal missing cleanup. It only happens in development,
never in production.

---

## Q6. The hooks list

| Hook | What it is for |
|---|---|
| `useState` | Store a value that changes and should re-render the screen |
| `useEffect` | Talk to the outside world (API, timers, browser) |
| `useContext` | Read shared data without passing props down every level |
| `useRef` | Store a value that survives renders but does **not** re-render |
| `useMemo` | Remember a calculated **value** so it is not recalculated |
| `useCallback` | Remember a **function** so it is not recreated |
| `useReducer` | Manage complex state with many different actions |
| Custom hook | Your own reusable `useSomething` function |

### 🔴 The Rules of Hooks, and the reason behind them
**Only call hooks at the top level.** Never inside an `if`, a loop, or a nested
function.

```jsx
if (isLoggedIn) {
  const [name, setName] = useState('');   // ❌ never do this
}
```

**Why?** React does not know your hooks by name. It tracks them by **the order they
are called**. First hook, second hook, third hook. If an `if` skips one, the order
shifts, and React gives you the wrong value from the wrong hook.

---

## Q7. `useMemo`, `useCallback` and `useRef` 🔴

### `useMemo` — remember a value
```jsx
const total = useMemo(() => {
  return loans.reduce((sum, l) => sum + l.amount, 0);
}, [loans]);
```
The calculation only runs again when `loans` changes. On other renders React reuses
the stored answer.

### `useCallback` — remember a function
```jsx
const handleAdd = useCallback((id) => {
  setCart(c => [...c, id]);
}, []);
```

**Why would a function need remembering?** Every render creates a **new** function
object. Even though the code is identical, it is a different object in memory. If
you pass it to a child wrapped in `React.memo`, the child sees a "new" prop and
re-renders anyway. `useCallback` keeps the same function object.

### `useRef` — a box that does not trigger re-renders
Two uses.

**1. Reach a DOM element:**
```jsx
const inputRef = useRef(null);
useEffect(() => { inputRef.current.focus(); }, []);
return <input ref={inputRef} />;
```

**2. Keep a value between renders without re-rendering:**
```jsx
const timerId = useRef(null);        // storing a timer id
const isFirstRender = useRef(true);  // a flag
```

**useState vs useRef in one line:** changing state re-renders the screen. Changing a
ref does not.

### 🔴 "Should you wrap everything in useMemo?"
Say **no**. This is a maturity signal.
> "No. Memoization is not free. React still has to store the value and compare the
> dependencies on every render. If the calculation is cheap, memoizing it can be
> slower than just doing it. I profile with React DevTools first and memoize where
> there is a real problem."

---

## Q8. What causes a re-render? How do you stop unnecessary ones? 🔴

### A component re-renders when:
1. Its own state changed.
2. Its props changed.
3. **Its parent re-rendered.** This happens even if its props are identical.
4. A context it uses changed.

Point 3 surprises people. By default, when a parent re-renders, all its children
re-render too.

### How to fix it, in the order you should try
**1. `React.memo`** — skip the re-render if the props are the same.
```jsx
const LoanCard = React.memo(function LoanCard({ loan }) { ... });
```

**2. `useCallback` / `useMemo` on the props you pass to it.**
`React.memo` compares props. If you pass a fresh function or object every render,
the comparison always fails and `React.memo` does nothing.

**3. Move state down.** If only a small part of the page uses a piece of state, put
that state in a smaller component. Then only that part re-renders.

**4. Split your contexts.** If one context holds both the theme and the cart, every
cart change re-renders everything using the theme too.

---

## Q9. Controlled vs uncontrolled inputs 🔴

**Controlled** — React state holds the value. React is the source of truth.
```jsx
const [email, setEmail] = useState('');
<input value={email} onChange={e => setEmail(e.target.value)} />
```

**Uncontrolled** — the DOM holds the value. You read it when you need it.
```jsx
const emailRef = useRef();
<input ref={emailRef} defaultValue="" />
// later: emailRef.current.value
```

### Which one, and why
Use **controlled** by default. Because the value is in state, you can:

- validate as the user types
- disable the submit button when the form is invalid
- format the value, for example adding commas to an amount
- reset the form easily

Use **uncontrolled** for very large forms where a re-render on every keystroke is
too slow, or for file inputs. `<input type="file">` is always uncontrolled, because
for security reasons JavaScript cannot set its value.

---

## Q10. Context API 🔴

### The problem it solves: prop drilling
The logged in user is needed deep in the tree. Without context you pass it through
every level, even components that do not use it:

```
App (has user)
 └ Layout      (passes user, does not use it)
    └ Sidebar  (passes user, does not use it)
       └ Menu  (passes user, does not use it)
          └ Avatar   ← finally uses it
```

### How context fixes it
```jsx
const AuthContext = createContext(null);

// near the top
<AuthContext.Provider value={{ user, logout }}>
  <Layout />
</AuthContext.Provider>

// anywhere below, at any depth
const { user } = useContext(AuthContext);
```

Good for values that rarely change: the current user, the theme, the language.

### 🔴 The limitation you must mention
**Every component using a context re-renders whenever the context value changes.**

And this is a common mistake:
```jsx
<AuthContext.Provider value={{ user, logout }}>
```
That object literal is **created fresh on every render**. So it is always "new", and
every consumer re-renders every time, even if `user` did not change.

Fix:
```jsx
const value = useMemo(() => ({ user, logout }), [user]);
<AuthContext.Provider value={value}>
```

> "Context solves prop drilling, but it is not a state manager. It is not optimised
> for values that change often, because every consumer re-renders. For server data
> I would use React Query instead, and for large client state, Redux Toolkit or
> Zustand."

---

## Q11. Custom hooks

A custom hook is just a function whose name starts with `use` and which calls other
hooks. It lets you reuse **logic**, not UI.

```jsx
function useDebounce(value, delay = 500) {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debounced;
}

// using it
const query = useDebounce(searchText, 400);
useEffect(() => { callApi(query); }, [query]);
```

Important detail: each component that calls `useDebounce` gets its **own separate
state**. The hook shares the logic, not the data.

Have one custom hook ready to describe. It is a strong signal.

---

## Q12. Code splitting and error boundaries

### Code splitting with lazy and Suspense
By default, all your code is bundled into one big JavaScript file. The user
downloads the admin dashboard even if they never open it.

```jsx
const Dashboard = React.lazy(() => import('./Dashboard'));

<Suspense fallback={<Spinner />}>
  <Dashboard />
</Suspense>
```
Now the dashboard code downloads only when it is needed. The initial page loads
faster. This connects directly to file 04 on performance.

### Error boundary
If any component throws an error during render, React unmounts the whole app and
the user sees a blank white page. An error boundary catches that and shows a
fallback instead.

```jsx
class ErrorBoundary extends React.Component {
  state = { hasError: false };
  static getDerivedStateFromError() { return { hasError: true }; }
  render() {
    if (this.state.hasError) return <p>Something went wrong.</p>;
    return this.props.children;
  }
}
```
This is the one place where you still write a class component. Hooks cannot do it
yet. In practice most teams use the `react-error-boundary` package.

---

## Q13. Class components vs function components

| Class (old) | Function + hooks (current) |
|---|---|
| `componentDidMount` | `useEffect(fn, [])` |
| `componentDidUpdate` | `useEffect(fn, [dep])` |
| `componentWillUnmount` | the cleanup `return` inside `useEffect` |
| `this.state`, `this.setState` | `useState` |

> "Function components with hooks are the standard now. There is less boilerplate,
> no confusion with `this`, and logic can be reused through custom hooks instead of
> higher order components. I can read class components in older code, but I write
> function components."

---

## Q14. Which state management would you choose?

Answer with a decision path, not a favourite library:

1. **Local `useState`** first. Most state belongs to one component.
2. **Lift it up** if two siblings need it.
3. **Context** for values that are shared widely and change rarely, like the user
   or the theme.

4. **React Query or SWR** for server data. Most "global state" is really a copy of
   server data, and these libraries handle caching, refetching, loading and error
   states for you.

5. **Redux Toolkit or Zustand** only when client state is genuinely complex.

> "I would not add Redux to a project just to hold a user object. That is extra
> setup with no benefit."

---

## Q15. Quick questions

- **What is JSX?** It looks like HTML but it is JavaScript. A build tool converts
  `<div>Hi</div>` into `React.createElement('div', null, 'Hi')`. The browser never
  sees JSX.

- **Why `className` and not `class`?** `class` is a reserved word in JavaScript.
- **What is a Fragment?** `<>...</>` groups elements without adding an extra `<div>`
  to the page.

- **How do you render conditionally?** `{isLoading && <Spinner />}` or a ternary.
- **⚠️ The `0` trap:** `{count && <p>...</p>}` renders a literal `0` on the screen
  when count is 0, because `0` is falsy but React still prints it. Write
  `{count > 0 && <p>...</p>}`.

- **`React.memo` vs `useMemo`?** `React.memo` wraps a component. `useMemo` caches a
  value inside a component.

- **Can you read `key` as a prop?** No. React uses it internally, the component
  never receives it.

---

## ✅ Check yourself before moving on
1. Explain the four things that cause a re-render, and three ways to reduce them.
2. Write `useDebounce` from memory.
3. Explain the "index as key" problem using the delete example, in 30 seconds.
4. Explain why `items.push(x); setItems(items)` does not update the screen.
