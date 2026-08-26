# 01 · JavaScript Core 🔴
**Budget: 60 minutes** · Every frontend interview opens here. If you're shaky on
`this`, closures, or async, the rest of the interview never happens.

---

## Where JavaScript fits (the "why" answer)

> "HTML is the structure, CSS is the presentation, JavaScript is the behaviour.
> It's the only language browsers run natively, so every interaction — form
> validation, fetching loan data without a page reload, filtering a bank list —
> goes through it. React and Next.js are both just JavaScript libraries; nothing
> in them works if the fundamentals don't."

---

## Q1 🔴 `var` vs `let` vs `const`

| | `var` | `let` | `const` |
|---|---|---|---|
| Scope | function | block `{}` | block `{}` |
| Redeclare | yes | no | no |
| Reassign | yes | yes | **no** |
| Hoisting | hoisted, `undefined` | hoisted into **TDZ** (ReferenceError) | same as `let` |

**Model answer:** "`var` is function-scoped and gets hoisted as `undefined`, which
causes bugs — the classic one is `var` in a loop with `setTimeout` printing the
final value every time. `let` and `const` are block-scoped and sit in the Temporal
Dead Zone until declared, so accessing them early throws instead of silently
giving `undefined`. I default to `const`, use `let` when I must reassign, and
never use `var`."

**Follow-up trap:** *"Is a `const` object immutable?"*
→ "No. `const` only prevents **rebinding the variable**. `const user = {}` then
`user.name = 'A'` is fine; `user = {}` throws. For real immutability you'd use
`Object.freeze()`, or just copy with spread."

```js
for (var i = 0; i < 3; i++) setTimeout(() => console.log(i)); // 3 3 3
for (let i = 0; i < 3; i++) setTimeout(() => console.log(i)); // 0 1 2
```

---

## Q2 🔴 What is a closure? Where have you used one?

**Definition:** A closure is a function that remembers the variables from the
scope where it was **created**, even after that outer function has returned.

```js
function counter() {
  let count = 0;                 // private
  return () => ++count;          // closes over `count`
}
const inc = counter();
inc(); // 1
inc(); // 2  — `count` survived, but nothing else can touch it
```

**Where it's useful — say this, it's the part that impresses:**
- **Data privacy / module pattern** — `count` can't be modified from outside.
- **`useState` in React is literally a closure** — the hook holds your state in a
  closure inside React's fiber, and gives you back a getter and a setter.
- **Debounce / throttle** — the timer ID is held in a closure between calls.
- **Event handlers** that need to remember which item they belong to.

**Trap:** *"stale closure in React"* — a `useEffect` with `[]` deps captures the
first render's state forever. Fix: add the dep, or use the functional updater
`setCount(c => c + 1)`.

---

## Q3 🔴 Explain the event loop / why is JS single-threaded but async?

**Model answer (draw it if there's a whiteboard):**
"JavaScript has one call stack, so it runs one thing at a time. Anything slow —
a network call, a timer — is handed off to the browser's Web APIs, not to JS.
When that finishes, its callback is queued. The **event loop** checks: if the call
stack is empty, it pushes the next callback on. **Microtasks (Promises,
`queueMicrotask`) drain completely before the next macrotask (`setTimeout`,
events)** — that's the ordering people get wrong."

```js
console.log('1');
setTimeout(() => console.log('2'), 0);   // macrotask
Promise.resolve().then(() => console.log('3')); // microtask
console.log('4');
// Output: 1 4 3 2
```

**Why it matters practically:** a long synchronous loop blocks rendering and
freezes the UI — this is exactly what hurts INP (see file 04).

---

## Q4 🔴 Callback → Promise → async/await

- **Callback:** function passed in, called when done. Nesting them = *callback hell*.
- **Promise:** an object representing a future value. States: `pending → fulfilled | rejected`. Chainable with `.then()`, flattening the nesting.
- **async/await:** syntactic sugar over Promises. `await` pauses that function until the Promise settles — reads like sync code, errors with `try/catch`.

```js
async function getLoans() {
  try {
    const res = await fetch('/api/loans');
    if (!res.ok) throw new Error(`HTTP ${res.status}`);   // fetch does NOT throw on 404/500
    return await res.json();
  } catch (err) {
    console.error(err);
    throw err;
  }
}
```

🔴 **Guaranteed follow-up: "How do you fire multiple API calls in parallel?"**
```js
const [banks, offers] = await Promise.all([getBanks(), getOffers()]);
```
"Sequential `await`s run one after another — two 300 ms calls take 600 ms.
`Promise.all` fires both and waits for the slowest, so ~300 ms. If one rejecting
shouldn't kill the rest, I use `Promise.allSettled`."

| Method | Behaviour |
|---|---|
| `Promise.all` | all succeed, or reject on first failure |
| `Promise.allSettled` | waits for all, returns status of each |
| `Promise.race` | first to settle (win *or* lose) — good for timeouts |
| `Promise.any` | first to **succeed** |

---

## Q5 🔴 `this`, and how arrow functions differ

`this` is decided by **how a function is called**, not where it's defined:

| Call style | `this` is |
|---|---|
| `obj.fn()` | `obj` |
| `fn()` (standalone) | `undefined` in strict mode / `window` otherwise |
| `new Fn()` | the new instance |
| `fn.call(x)` / `.apply(x)` / `.bind(x)` | `x` |
| **Arrow function** | **inherited from the enclosing scope — cannot be rebound** |

```js
const user = {
  name: 'Sujith',
  regular() { console.log(this.name); },      // 'Sujith'
  arrow: () => console.log(this.name),        // undefined — took `this` from module scope
};
```

**Practical takeaway:** "Arrow functions are why we stopped writing
`this.handleClick = this.handleClick.bind(this)` in class components. In modern
React with hooks, `this` barely comes up — but it still matters for
`setTimeout(function(){...})` and object methods."

---

## Q6 ES6+ features you actually use daily
```js
const { name, email = 'n/a' } = user;          // destructuring + default
const [first, ...rest] = list;                 // rest
const next = { ...user, verified: true };      // spread (shallow copy)
const label = `Loan for ${name}`;              // template literal
const city = user?.address?.city ?? 'Unknown'; // optional chaining + nullish coalescing
```
🔴 **`??` vs `||`:** "`||` falls back on *any* falsy value, so `0 || 10` gives 10 —
wrong if 0 is a legitimate interest rate. `??` only falls back on `null`/`undefined`."

🔴 **Spread is a shallow copy:** nested objects are still shared references.
Deep copy: `structuredClone(obj)`.

---

## Q7 `==` vs `===` · null vs undefined
- `===` compares value **and** type, no coercion. Always use it.
- `==` coerces: `'5' == 5` → true, `null == undefined` → true, `0 == ''` → true.
- `undefined` = declared but never assigned (JS's default). `null` = *you*
  deliberately set "no value".
- Falsy list, memorise: `false, 0, -0, 0n, "", null, undefined, NaN`. Everything
  else — including `[]` and `{}` — is truthy.

---

## Q8 🔴 map vs forEach vs filter vs reduce
| Method | Returns | Use for |
|---|---|---|
| `forEach` | `undefined` | side effects only |
| `map` | **new array, same length** | transform — *the React list-rendering one* |
| `filter` | new array, subset | search / filter features |
| `find` | first matching **element** | look up one item |
| `reduce` | any single value | totals, grouping, flattening |

```js
const total = loans.reduce((sum, l) => sum + l.amount, 0);
const byBank = loans.reduce((acc, l) => {
  (acc[l.bank] ||= []).push(l);
  return acc;
}, {});
```
"They're all non-mutating except `forEach`'s side effects, which is why they fit
React — React needs a *new* array reference to detect a change."

---

## Q9 Event bubbling, capturing, delegation
- **Bubbling:** event fires on target, then travels up to ancestors (default).
- **Capturing:** top-down phase, opt in with `addEventListener(fn, true)`.
- **Delegation:** put **one** listener on the parent and read `e.target` — instead
  of 100 listeners on 100 rows. Fewer listeners, and it works for rows added later.
- `e.stopPropagation()` stops the travel; `e.preventDefault()` stops the browser's
  default (form submit, link navigation).

---

## Q10 🔴 Debounce vs throttle — *write this from memory*
- **Debounce:** run only after the user *stops* for N ms → **search-as-you-type**.
- **Throttle:** run at most once per N ms → **scroll / resize / infinite scroll**.

```js
function debounce(fn, delay = 300) {
  let timer;                                  // closure!
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

function throttle(fn, limit = 300) {
  let waiting = false;
  return (...args) => {
    if (waiting) return;
    fn(...args);
    waiting = true;
    setTimeout(() => (waiting = false), limit);
  };
}
```
**Say the business reason:** "Without debouncing, a 10-character search fires 10
API calls. Debounced, it fires one — that's 90% fewer requests hitting the backend."

---

## Q11 Hoisting · Temporal Dead Zone
Declarations are moved to the top of their scope at compile time.
`function` declarations hoist fully (callable before definition); `var` hoists as
`undefined`; `let`/`const` hoist but stay in the TDZ, so early access **throws** —
which is a feature, not a bug: it surfaces the mistake.

---

## Q12 Shallow vs deep copy
```js
const shallow = { ...original };            // nested objects still shared
const deep = structuredClone(original);     // modern, handles Dates/Maps
const deepJson = JSON.parse(JSON.stringify(original)); // loses Date, undefined, functions
```
🔴 In React this is *the* bug behind "my state changed but the UI didn't re-render" —
you mutated the existing object instead of creating a new reference.

---

## Q13 localStorage vs sessionStorage vs cookies
| | Size | Lifetime | Sent to server? |
|---|---|---|---|
| localStorage | ~5–10 MB | until cleared | no |
| sessionStorage | ~5 MB | until tab closes | no |
| cookies | ~4 KB | `Expires`/`Max-Age` | **yes, every request** |

"Auth tokens belong in an **httpOnly cookie** — JS can't read it, so an XSS script
can't steal it. localStorage is readable by any script on the page. For a fintech-
adjacent product handling student loan data, that distinction matters."

⚠️ **Next.js note:** `localStorage` doesn't exist on the server. Access it inside
`useEffect` or guard with `typeof window !== 'undefined'`.

---

## Q14 Quick-fire round (they'll rattle these off)
- **`slice` vs `splice`?** `slice` returns a copy, non-mutating. `splice` mutates.
- **`null == undefined`?** `true`. With `===`? `false`.
- **`typeof null`?** `'object'` — a famous JS bug kept for backwards compatibility.
- **Check an array?** `Array.isArray(x)`.
- **`NaN === NaN`?** `false`. Use `Number.isNaN(x)`.
- **Higher-order function?** Takes or returns a function — `map`, `debounce`.
- **Pure function?** Same input → same output, no side effects. React components
  should be pure with respect to props.
- **Sync vs async?** Sync blocks the stack; async hands off and continues.
- **`fetch` on a 404?** It **resolves** — you must check `res.ok` yourself. Axios
  throws automatically. This one catches people out constantly.

---

### ✅ Before you move on, you should be able to say out loud:
1. A closure, with the counter example, in under 30 seconds.
2. Why `1 4 3 2` is the output of the event-loop snippet.
3. Debounce, written from memory, no reference.
