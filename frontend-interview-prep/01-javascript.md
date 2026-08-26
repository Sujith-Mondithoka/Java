# 01 · JavaScript Core 🔴
**Time needed: 60 minutes**

Every frontend interview starts here. React and Next.js are both written in
JavaScript. If your basics are weak, the interviewer will stop early and the rest
of the interview will not happen.

**How to read this file:** each question has four parts.
*What it means* (the idea in plain words) → *Simple example* (small code) →
*Why it matters* (the real problem it solves) → *Say this* (your answer in the room).

---

## First, the context: what is JavaScript doing on a web page?

A web page has three parts.

| Part | Language | Job |
|---|---|---|
| Structure | HTML | What is on the page. Headings, buttons, forms. |
| Look | CSS | Colours, spacing, layout. |
| Behaviour | **JavaScript** | What happens when the user does something. |

HTML and CSS cannot make decisions. They cannot fetch data. JavaScript can.
So when a student clicks "Check loan offers", JavaScript is the part that reads the
form, calls the server, waits for the answer, and updates the page.

JavaScript runs **inside the browser**. Every browser has a JavaScript engine
built in. This is why it is the only language that runs on a web page directly.

---

## Q1. What is the difference between `var`, `let` and `const`? 🔴

### What it means
These are three ways to create a variable. A variable is a name for a value.

```js
var  a = 1;   // old way, from 1995
let  b = 2;   // new way, when the value will change
const c = 3;  // new way, when the value will not change
```

### The difference that matters: scope
**Scope** means "which part of the code can see this variable".

`let` and `const` live only inside the nearest `{ }` block.
`var` ignores blocks. It leaks out to the whole function.

```js
function test() {
  if (true) {
    var x = 'I leak';
    let y = 'I stay inside';
  }
  console.log(x);  // "I leak"  ← still visible, this is confusing
  console.log(y);  // ReferenceError ← y is gone, this is correct
}
```

### The classic bug this causes
```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// prints 3, 3, 3   ← WRONG

for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// prints 0, 1, 2   ← correct
```
With `var` there is only **one** `i` for the whole loop. By the time the timers
run, the loop has finished and `i` is 3. With `let`, each turn of the loop gets its
own fresh `i`.

### Careful: `const` does not mean "cannot change"
`const` only means you cannot point the name at something new.
If the value is an object or array, the **inside** can still change.

```js
const user = { name: 'Sujith' };
user.name = 'Kumar';        // ✅ allowed. We changed what is inside.
user = { name: 'Kumar' };   // ❌ error. We tried to point `user` somewhere new.
```

### Say this
> "`var` is function scoped, so it leaks out of `if` blocks and loops. `let` and
> `const` are block scoped, so they stay inside the braces. I use `const` by
> default, `let` only when I need to reassign, and I do not use `var`. One thing to
> note is that `const` does not make an object immutable. It only stops you from
> reassigning the variable itself."

---

## Q2. What is a closure? 🔴

### What it means
A closure is a function that **remembers the variables around it**, even after the
outer function has finished running.

Think of it like a lunchbox. When you create the inner function, it packs a copy of
the surrounding variables. Wherever it goes later, it still has that lunchbox.

### Simple example
```js
function makeCounter() {
  let count = 0;              // this variable lives inside makeCounter

  return function () {
    count = count + 1;
    return count;
  };
}

const counter = makeCounter();
counter();  // 1
counter();  // 2
counter();  // 3
```

`makeCounter()` already finished on the first line. Normally `count` would be
deleted. But the returned function still needs it, so JavaScript keeps it alive.
That is a closure.

Notice something useful: nothing outside can touch `count`. You cannot write
`counter.count = 100`. The variable is private.

### Where you actually use closures
1. **Private data.** As above. The only way to change `count` is through the function.
2. **`useState` in React.** React stores your state in a closure and hands you back
   a value and a setter function.

3. **Debounce and throttle.** The timer id is kept in a closure between calls. (See Q10.)
4. **Event handlers that remember which item they belong to.**

### The trap they may ask about: stale closure
```js
useEffect(() => {
  const id = setInterval(() => {
    setCount(count + 1);   // ❌ `count` is stuck at its first value, 0
  }, 1000);
  return () => clearInterval(id);
}, []);                    // empty array = this runs once
```
The function inside `setInterval` packed its lunchbox on the first render only. It
will always see `count` as 0. So the counter goes 0 → 1, 1, 1, 1 forever.

Fix: use the function form of the setter. It always receives the newest value.
```js
setCount(c => c + 1);      // ✅
```

### Say this
> "A closure is a function that keeps access to the variables from where it was
> created, even after that outer function has returned. The counter example is the
> simplest one. In real code I use it for private state and for debounce, where the
> timer id has to survive between calls. It is also why the stale closure bug
> happens in `useEffect` with an empty dependency array."

---

## Q3. What is the event loop? 🔴

### The problem it solves
JavaScript can only do **one thing at a time**. It has a single call stack.

So what happens when you call an API that takes 2 seconds? If JavaScript simply
waited, the whole page would freeze. No clicking, no scrolling, nothing.

It does not wait. This is what the event loop is for.

### How it works, step by step
1. Your code runs on the **call stack**, one line at a time.
2. Slow things (network calls, timers) are **not** run by JavaScript. They are
   handed to the browser, which handles them in the background.

3. When the browser finishes, it puts your callback function in a **queue**.
4. The **event loop** watches the call stack. The moment the stack is empty, it
   takes the first item from the queue and runs it.

A simple picture:

```
  your code  →  [ CALL STACK ]  ← event loop pushes callbacks back in
                                          ↑
  slow work  →  [ browser handles it ] → [ QUEUE ]
```

### The one detail interviewers test
There are two queues, and one has priority.

- **Microtask queue** — Promises, `async/await`. **Higher priority.**
- **Macrotask queue** — `setTimeout`, `setInterval`, click events. Lower priority.

All microtasks run before the next macrotask.

```js
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
console.log('4');
```

Output: **1, 4, 3, 2**

Why:

- `1` and `4` are normal code, so they run first, in order.
- `3` is a Promise, so it goes to the microtask queue.
- `2` is a `setTimeout`, so it goes to the macrotask queue.
- Microtasks win, so `3` runs before `2`. Even though the timeout was 0 ms.

### Say this
> "JavaScript is single threaded, so it runs one thing at a time. Slow work like
> network calls is given to the browser instead of blocking the stack. When it
> finishes, the callback waits in a queue, and the event loop pushes it back onto
> the stack once the stack is empty. The detail people miss is that promises go to
> the microtask queue, which is drained fully before any `setTimeout` runs."

---

## Q4. Callbacks, Promises and async/await 🔴

### The context: three generations of the same idea
All three solve one problem. *How do I run some code later, after a slow thing
finishes?*

**1. Callback (oldest).** Pass a function in. It gets called when the work is done.
```js
getUser(1, function (user) {
  getOrders(user.id, function (orders) {
    getDetails(orders[0], function (details) {
      console.log(details);        // three levels deep already
    });
  });
});
```
This shape is called **callback hell**. It grows sideways and is hard to read.

**2. Promise.** An object that represents a value you will get later.
It has three states: `pending` → then either `fulfilled` or `rejected`.
```js
getUser(1)
  .then(user => getOrders(user.id))
  .then(orders => getDetails(orders[0]))
  .then(details => console.log(details))
  .catch(err => console.log('Something failed:', err));
```
Flat, not nested. One `.catch` handles errors from any step.

**3. async/await (newest).** The same Promise, written so it reads like normal code.
```js
async function show() {
  try {
    const user    = await getUser(1);
    const orders  = await getOrders(user.id);
    const details = await getDetails(orders[0]);
    console.log(details);
  } catch (err) {
    console.log('Something failed:', err);
  }
}
```
`await` means "pause here until this promise finishes". It does not freeze the
browser. It only pauses this one function.

### Real fetch example, with the mistake people make
```js
async function getLoans() {
  const res = await fetch('/api/loans');

  // ⚠️ fetch does NOT throw an error on 404 or 500.
  // It only throws if the network itself failed.
  // So you must check this yourself:
  if (!res.ok) {
    throw new Error('Request failed with status ' + res.status);
  }

  return res.json();
}
```
This catches many candidates. Remember it.

### Running calls in parallel 🔴
```js
// SLOW: 300ms + 300ms = 600ms
const banks  = await getBanks();
const offers = await getOffers();

// FAST: both start together, takes about 300ms
const [banks, offers] = await Promise.all([getBanks(), getOffers()]);
```
Use `Promise.all` when the calls do not depend on each other.

| Method | What it does |
|---|---|
| `Promise.all` | Waits for all. If any one fails, the whole thing fails. |
| `Promise.allSettled` | Waits for all. Tells you which passed and which failed. |
| `Promise.race` | Returns the first one to finish, success or failure. |
| `Promise.any` | Returns the first one to **succeed**. |

### Say this
> "Callbacks came first but nesting them becomes unreadable. Promises fixed the
> nesting with chaining. `async/await` is the same promise written in a way that
> reads top to bottom, with normal `try/catch` for errors. One thing I always
> remember is that `fetch` does not reject on a 404 or 500, so I check `res.ok`
> myself. And when two calls do not depend on each other I use `Promise.all` so
> they run in parallel instead of one after the other."

---

## Q5. What is `this`? How are arrow functions different? 🔴

### What it means
`this` is a word that points to an object. Which object it points to is decided by
**how the function is called**, not where it was written.

### The four rules
```js
const user = {
  name: 'Sujith',
  greet() { console.log(this.name); }
};

user.greet();          // "Sujith"   → called on user, so `this` = user

const g = user.greet;
g();                   // undefined  → called alone, so `this` is not user

g.call(user);          // "Sujith"   → we forced `this` to be user

new Person();          // `this` = the new object being created
```

### Arrow functions are different
A normal function decides `this` when it is called.
An arrow function does **not** have its own `this`. It borrows it from the code
around it, at the time it was written. This can never be changed.

```js
const user = {
  name: 'Sujith',
  regular: function () { console.log(this.name); },
  arrow:   () => { console.log(this.name); }
};

user.regular();  // "Sujith"    ← this = user
user.arrow();    // undefined   ← this came from outside the object
```

### Why this is useful
Before arrow functions, this was a common bug:
```js
const timer = {
  seconds: 0,
  start: function () {
    setInterval(function () {
      this.seconds++;      // ❌ `this` is not `timer` here
    }, 1000);
  }
};
```
The fix used to be `.bind(this)`. Now we just use an arrow function:
```js
setInterval(() => { this.seconds++; }, 1000);   // ✅ borrows `this` from start()
```

### Say this
> "`this` depends on how a function is called. If you call `obj.method()`, `this`
> is `obj`. If you pull the same function out and call it alone, `this` is lost.
> Arrow functions do not have their own `this`. They take it from the surrounding
> code, which is why they solved the old `bind(this)` problem in callbacks. In
> React with hooks I rarely deal with `this` at all now."

---

## Q6. ES6 features you use every day

These are just shortcuts. Learn what each one replaces.

**Destructuring** — pull values out of an object or array.
```js
// instead of:
const name = user.name;
const city = user.city;

// write:
const { name, city } = user;
const [first, second] = myArray;
```

**Default value** — used when the value is `undefined`.
```js
const { city = 'Hyderabad' } = user;
```

**Spread `...`** — copy an object or array into a new one.
```js
const newUser  = { ...user, verified: true };   // copy + change one field
const newList  = [...list, newItem];            // copy + add one item
```
⚠️ Spread makes a **shallow** copy. Objects inside are still shared.
For a full copy: `structuredClone(user)`.

**Rest `...`** — collect the remaining items.
```js
const [first, ...others] = [1, 2, 3, 4];   // first = 1, others = [2, 3, 4]
```

**Template literal** — build a string without `+`.
```js
const msg = `Hello ${name}, you have ${count} offers`;
```

**Optional chaining `?.`** — stop safely if something is missing.
```js
const city = user?.address?.city;    // undefined instead of a crash
```

**Nullish coalescing `??`** — a fallback, but only for `null` and `undefined`.
```js
const rate = apiRate ?? 8.5;
```

### 🔴 `??` vs `||` — know this difference
```js
const rate = 0;

rate || 8.5   // 8.5   ← wrong! 0 is falsy, so it was replaced
rate ?? 8.5   // 0     ← correct, 0 is a real value
```
`||` replaces **any** falsy value: `0`, `''`, `false`, `null`, `undefined`, `NaN`.
`??` replaces **only** `null` and `undefined`.

If an interest rate of 0% is valid, `||` will silently give you the wrong number.

---

## Q7. `==` vs `===`, and `null` vs `undefined`

**`===` compares value and type. No conversion.**
**`==` converts the types first, which gives strange results.**

```js
'5' === 5      // false   ← different types
'5' == 5       // true    ← '5' was converted to 5
0 == ''        // true
null == undefined  // true
null === undefined // false
```
Rule: always use `===`.

**`undefined`** — JavaScript's default. The variable exists but was never given a value.
**`null`** — you deliberately said "empty on purpose".

**Falsy values, memorise the list:**
`false`, `0`, `''` (empty string), `null`, `undefined`, `NaN`.
Everything else is truthy, including `[]` and `{}`.

---

## Q8. Array methods: map, filter, reduce, forEach 🔴

These come up constantly, because React lists are built with `map`.

```js
const loans = [
  { id: 1, bank: 'SBI',  amount: 500000 },
  { id: 2, bank: 'HDFC', amount: 800000 },
  { id: 3, bank: 'SBI',  amount: 300000 },
];
```

**`map`** — change every item. Returns a **new array of the same length**.
```js
const names = loans.map(loan => loan.bank);   // ['SBI', 'HDFC', 'SBI']
```
This is what you use to turn data into JSX in React.

**`filter`** — keep only some items. Returns a **shorter array**.
```js
const sbi = loans.filter(loan => loan.bank === 'SBI');   // 2 items
```
This is what you use for search and filter features.

**`find`** — get the **first matching item** itself, not an array.
```js
const one = loans.find(loan => loan.id === 2);   // { id: 2, ... }
```

**`reduce`** — turn the whole array into a single value.
```js
const total = loans.reduce((sum, loan) => sum + loan.amount, 0);
// 1600000
```
Read it as: start at 0, then add each loan's amount to the running total.

**`forEach`** — just loop. Returns nothing. Use it only for side effects.

### Why this matters in React
`map`, `filter` and `reduce` do **not** change the original array. They return a new
one. React needs a new array to notice that something changed. So these methods fit
React perfectly, and a loop with `push` does not.

---

## Q9. Event bubbling and event delegation

### Bubbling
When you click a button inside a div, the click event fires on the button first,
then travels **up** to the div, then to the body. This travelling up is bubbling.

```html
<div onClick="...">        ← 3rd
  <ul onClick="...">       ← 2nd
    <li onClick="...">     ← 1st (you clicked here)
```

### Delegation, and why it is useful
Imagine a list of 500 loan rows, each with a delete button.
You could add 500 click listeners. That is slow and uses memory.

Instead, add **one** listener on the parent, and check what was clicked:
```js
list.addEventListener('click', (e) => {
  const btn = e.target.closest('button');
  if (!btn) return;                  // they clicked somewhere else
  deleteRow(btn.dataset.id);
});
```
One listener instead of 500. It also works for rows added later, because the parent
was already listening.

### Two methods to know
- `e.stopPropagation()` — stop the event from bubbling further up.
- `e.preventDefault()` — stop the browser's default action, like a form reloading
  the page or a link navigating away.

---

## Q10. Debounce and throttle 🔴 (practise writing this)

### The problem
A user types "axis bank" in a search box. That is 9 characters. If you call the API
on every keystroke, you send **9 requests**. Eight of them are wasted, and the
results may arrive out of order.

### Debounce: wait until the user stops
"Only run after there has been no typing for 400ms."
Use for: **search boxes**, autocomplete, saving a draft.

```js
function debounce(fn, delay = 400) {
  let timer;                          // kept alive by a closure

  return function (...args) {
    clearTimeout(timer);              // cancel the previous plan
    timer = setTimeout(() => fn(...args), delay);   // make a new plan
  };
}
```
Every keystroke cancels the previous timer. Only the last one survives.
Result: 9 keystrokes, **1 request**.

### Throttle: run at most once every X ms
"No matter how many times this fires, run it only once per 300ms."
Use for: **scroll**, resize, mouse move, infinite scroll.

```js
function throttle(fn, limit = 300) {
  let waiting = false;

  return function (...args) {
    if (waiting) return;              // still in the cool-down period
    fn(...args);
    waiting = true;
    setTimeout(() => { waiting = false; }, limit);
  };
}
```

### The difference in one line
**Debounce waits for a pause. Throttle limits the rate.**

### Say this
> "Debounce runs the function only after the user stops for a set time, which is
> what you want for a search box. Throttle runs it at a fixed maximum rate, which is
> what you want for scroll events. Without debouncing, a nine letter search sends
> nine API calls instead of one."

---

## Q11. Hoisting

Before running your code, JavaScript scans it and makes room for all the
declarations. This is called hoisting.

```js
sayHi();                    // ✅ works
function sayHi() { ... }    // function declarations are fully hoisted

console.log(a);             // undefined  ← var is hoisted but empty
var a = 5;

console.log(b);             // ❌ ReferenceError
let b = 5;                  // let/const are hoisted but locked
```

That locked period for `let` and `const` is called the **Temporal Dead Zone (TDZ)**.
It is a good thing. It gives you a clear error instead of a silent `undefined`.

---

## Q12. Shallow copy vs deep copy 🔴

```js
const original = { name: 'Sujith', address: { city: 'Hyderabad' } };

const shallow = { ...original };
shallow.name = 'Kumar';               // ✅ original.name is safe
shallow.address.city = 'Chennai';     // ❌ original.address.city ALSO changed

const deep = structuredClone(original);
deep.address.city = 'Chennai';        // ✅ original is safe
```

Spread copies only the top level. Anything nested is still the same object in
memory. This is the reason behind a very common React bug: "I changed the state but
the screen did not update", or "I changed one item and another item changed too".

---

## Q13. localStorage vs sessionStorage vs cookies

| | Size | How long it lasts | Sent to the server? |
|---|---|---|---|
| `localStorage` | about 5 MB | Forever, until cleared | No |
| `sessionStorage` | about 5 MB | Until the tab is closed | No |
| Cookie | about 4 KB | Until it expires | **Yes, on every request** |

### Which one for a login token?
An **httpOnly cookie** is the safest. `httpOnly` means JavaScript cannot read it.
So if an attacker injects a script into your page, that script still cannot steal
the token. Anything in `localStorage` can be read by any script on the page.

For a product handling student loan data, this is worth saying out loud.

⚠️ **In Next.js:** `localStorage` does not exist on the server. Reading it in a
Server Component or during the first render will crash. Read it inside `useEffect`,
which only runs in the browser.

---

## Q14. Quick questions they fire at the end

- **`slice` vs `splice`?** `slice` returns a copy and leaves the original alone.
  `splice` changes the original array.

- **`typeof null`?** `'object'`. This is a famous bug in JavaScript from 1995. It was
  never fixed because too much code depends on it.

- **How to check for an array?** `Array.isArray(x)`. `typeof []` gives `'object'`.
- **`NaN === NaN`?** `false`. NaN is not equal to anything, including itself.
  Use `Number.isNaN(x)`.

- **Higher order function?** A function that takes a function, or returns one.
  `map`, `filter` and `debounce` are all higher order functions.

- **Pure function?** Same input always gives the same output, and it changes nothing
  outside itself. Easy to test and easy to reason about.

- **Synchronous vs asynchronous?** Synchronous blocks the next line until it
  finishes. Asynchronous starts the work and lets the next line run.

---

## ✅ Check yourself before moving on
You should be able to do these **without looking**:

1. Explain a closure using the counter example, in about 30 seconds.
2. Explain why `1 4 3 2` is the answer in the event loop question.
3. Write the `debounce` function from memory.
4. Explain why `0 || 8.5` gives the wrong answer and `0 ?? 8.5` gives the right one.
