# 07 · Machine Coding Round 🔴
**Time needed: 60 minutes. And you must TYPE these, not read them.**

Reading code makes you feel prepared. It does not make you prepared. Open
CodeSandbox or StackBlitz and build problems 1 and 2 from an empty file. That is how
you should spend this hour.

---

## First, the context: what they are actually grading

They are not checking whether your code is beautiful. In 45 minutes nobody writes
beautiful code. They are checking six things:

1. Can you break the problem into state and components?
2. Do you know React well enough to not fight it?
3. Do you handle the cases that are not the happy path?
4. Do you talk while you work?
5. Do you notice your own mistakes?
6. Would it be pleasant to sit next to you for a day?

## How to run the round

**1. Clarify for 60 seconds. Do not start typing immediately.**
> "Should the filtering happen on the client, or should I call the API each time?"
> "Roughly how many items are we dealing with?"
> "Should the state survive a refresh?"

Candidates who ask questions score higher than candidates who start typing. Every
time.

**2. Say your plan out loud before you write it.**
> "I will keep the typed text in state, debounce it, then filter the list while
> rendering. Then I will handle the empty case."

**3. Build the ugly working version first.** Get it working, then improve it. Do not
style anything until the logic works.

**4. Keep talking while you type.** Silence makes the interviewer think you are
stuck. Narrate what you are doing, even if it feels awkward.

**5. Say the edge cases out loud**, even the ones you do not have time to build.
*"I would add an error state here if I had more time"* still earns you the point.

**6. Refactor at the end** if there is time. Pull something into a custom hook, or
split a component. It shows you know what good code looks like.

**Common problems at this level:** search and filter a list, todo CRUD, a counter,
an accordion or tabs, a star rating, form validation, fetching and displaying users,
pagination, a modal, a countdown timer.

---

## Problem 1 🔴 — Search and filter a list, with debounce
*The most commonly asked machine coding question in Indian frontend interviews.*

**What they are testing:** derived state, debouncing, keys, and whether you remember
the empty state.

```jsx
import { useState, useEffect, useMemo } from 'react';

function useDebounce(value, delay = 400) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const t = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(t);
  }, [value, delay]);
  return debounced;
}

export default function BankSearch({ banks }) {
  const [query, setQuery] = useState('');
  const [type, setType]   = useState('all');
  const debouncedQuery    = useDebounce(query);

  // derived state — NOT useState + useEffect
  const filtered = useMemo(() => {
    return banks.filter(b => {
      const matchesQuery = b.name.toLowerCase().includes(debouncedQuery.toLowerCase().trim());
      const matchesType  = type === 'all' || b.type === type;
      return matchesQuery && matchesType;
    });
  }, [banks, debouncedQuery, type]);

  return (
    <div>
      <input
        value={query}
        onChange={e => setQuery(e.target.value)}
        placeholder="Search banks…"
        aria-label="Search banks"
      />
      <select value={type} onChange={e => setType(e.target.value)}>
        <option value="all">All</option>
        <option value="public">Public</option>
        <option value="private">Private</option>
        <option value="nbfc">NBFC</option>
      </select>

      {filtered.length === 0
        ? <p>No banks match “{debouncedQuery}”.</p>
        : <ul>{filtered.map(b => <li key={b.id}>{b.name} — {b.rate}%</li>)}</ul>}
    </div>
  );
}
```
### Explain these four things while you type

**1. The filtered list is calculated during render, not stored in state.**
> "I could have put `filtered` in state and updated it in a `useEffect`, but then I
> have two sources of truth that can go out of sync, plus an extra render. It is
> derived data, so I calculate it."

**2. The debounce reduces work.**
> "Without this, typing nine characters runs the filter nine times. If it were an
> API call, that would be nine requests instead of one."

**3. The key is a stable id, never the array index.**

**4. The edge cases are handled.** `.trim()` removes accidental spaces, and
`.toLowerCase()` on both sides makes the search case insensitive. And when nothing
matches, the user sees a message instead of a blank area.

---

## Problem 2 🔴 — Fetch + loading / error / empty / retry
```jsx
import { useState, useEffect, useCallback } from 'react';

export default function Users() {
  const [users, setUsers]     = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError]     = useState(null);

  const load = useCallback(async (signal) => {
    try {
      setLoading(true);
      setError(null);
      const res = await fetch('https://jsonplaceholder.typicode.com/users', { signal });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      setUsers(await res.json());
    } catch (e) {
      if (e.name !== 'AbortError') setError(e.message);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    const c = new AbortController();
    load(c.signal);
    return () => c.abort();
  }, [load]);

  if (loading) return <p>Loading…</p>;
  if (error)   return (
    <div role="alert">
      <p>Couldn’t load users: {error}</p>
      <button onClick={() => load()}>Retry</button>
    </div>
  );
  if (!users.length) return <p>No users found.</p>;

  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}
```
### Why this scores well
- All four states are handled: loading, error, empty, and success.
- **The retry button.** Almost nobody adds this. An error state the user cannot
  escape from is a dead end.

- `res.ok` is checked, because `fetch` does not throw on a 404 or 500.
- The request is cancelled on unmount with `AbortController`.
- `finally` means loading always stops, even when the request fails.

---

## Problem 3 — Todo list (CRUD + no mutation)
```jsx
export default function Todos() {
  const [todos, setTodos] = useState([]);
  const [text, setText]   = useState('');

  const add = (e) => {
    e.preventDefault();
    const value = text.trim();
    if (!value) return;                                  // edge case: empty input
    setTodos(t => [...t, { id: crypto.randomUUID(), text: value, done: false }]);
    setText('');
  };

  const toggle = (id) =>
    setTodos(t => t.map(todo => todo.id === id ? { ...todo, done: !todo.done } : todo));

  const remove = (id) => setTodos(t => t.filter(todo => todo.id !== id));

  return (
    <>
      <form onSubmit={add}>
        <input value={text} onChange={e => setText(e.target.value)} />
        <button type="submit">Add</button>
      </form>
      <ul>
        {todos.map(todo => (
          <li key={todo.id}>
            <input type="checkbox" checked={todo.done} onChange={() => toggle(todo.id)} />
            <span style={{ textDecoration: todo.done ? 'line-through' : 'none' }}>{todo.text}</span>
            <button onClick={() => remove(todo.id)}>×</button>
          </li>
        ))}
      </ul>
      <p>{todos.filter(t => !t.done).length} remaining</p>
    </>
  );
}
```
### Details worth pointing out
- **`<form onSubmit>` instead of a button `onClick`.** This means the Enter key
  works, which is what users expect. Interviewers notice this.

- **Functional updaters** (`setTodos(t => ...)`) so you always work from the latest
  state.

- **`map` and `filter` never change the original array.** They return a new one,
  which is exactly what React needs to detect a change.

- **`crypto.randomUUID()` for the id**, not the array index.
- **The remaining count is calculated, not stored** in another piece of state.

---

## Problem 4 — Form with validation
```jsx
export default function LeadForm() {
  const [values, setValues]   = useState({ name: '', email: '', phone: '' });
  const [errors, setErrors]   = useState({});
  const [touched, setTouched] = useState({});
  const [status, setStatus]   = useState('idle');   // idle | submitting | success | error

  const validate = (v) => {
    const e = {};
    if (!v.name.trim()) e.name = 'Name is required';
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.email)) e.email = 'Enter a valid email';
    if (!/^[6-9]\d{9}$/.test(v.phone)) e.phone = 'Enter a valid 10-digit mobile number';
    return e;
  };

  const handleChange = (e) => {
    const next = { ...values, [e.target.name]: e.target.value };
    setValues(next);
    if (touched[e.target.name]) setErrors(validate(next));   // re-validate only after blur
  };

  const handleBlur = (e) => {
    setTouched(t => ({ ...t, [e.target.name]: true }));
    setErrors(validate(values));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const found = validate(values);
    setErrors(found);
    setTouched({ name: true, email: true, phone: true });
    if (Object.keys(found).length) return;
    setStatus('submitting');
    try {
      await fetch('/api/leads', { method: 'POST', body: JSON.stringify(values) });
      setStatus('success');
    } catch { setStatus('error'); }
  };

  return (
    <form onSubmit={handleSubmit} noValidate>
      {['name', 'email', 'phone'].map(field => (
        <div key={field}>
          <label htmlFor={field}>{field}</label>
          <input id={field} name={field} value={values[field]}
                 onChange={handleChange} onBlur={handleBlur}
                 aria-invalid={!!errors[field]} />
          {touched[field] && errors[field] && <small role="alert">{errors[field]}</small>}
        </div>
      ))}
      <button disabled={status === 'submitting'}>
        {status === 'submitting' ? 'Submitting…' : 'Submit'}
      </button>
      {status === 'success' && <p>Thanks — we’ll call you shortly.</p>}
    </form>
  );
}
```
### The three details that make this look experienced

**1. Errors only appear after the user leaves a field (`onBlur`).**
Showing "Enter a valid email" while someone is still typing the first letter of
their email is bad UX. That is what the `touched` state is for.

**2. The submit button is disabled while the request is in flight.**
Otherwise an impatient user clicks three times and creates three applications.

**3. One `handleChange` for all fields**, using `e.target.name`. Writing a separate
handler for every field does not scale.

---

## Problem 5 — Accordion (controlled, one open at a time)
```jsx
function Accordion({ items }) {
  const [openId, setOpenId] = useState(null);
  return (
    <div>
      {items.map(item => {
        const isOpen = openId === item.id;
        return (
          <div key={item.id}>
            <button aria-expanded={isOpen}
                    onClick={() => setOpenId(isOpen ? null : item.id)}>
              {item.title} {isOpen ? '−' : '+'}
            </button>
            {isOpen && <p>{item.body}</p>}
          </div>
        );
      })}
    </div>
  );
}
```
### Why one `openId` instead of a boolean per item
If each item had its own `isOpen` boolean, you would have to remember to close all
the others every time one opens. It is easy to get wrong. With a single `openId`,
"only one open at a time" is guaranteed by the shape of the state itself.

If they ask for multiple open at once, hold a `Set` of ids instead.

`aria-expanded` tells a screen reader whether the section is open. And if this is an
FAQ, you can mention that adding FAQ structured data would make it eligible for a
rich result in Google.

---

## Problem 6 — Star rating
```jsx
function Rating({ value = 0, onChange, max = 5 }) {
  const [hover, setHover] = useState(0);
  return (
    <div onMouseLeave={() => setHover(0)}>
      {Array.from({ length: max }, (_, i) => i + 1).map(star => (
        <button key={star} type="button"
                aria-label={`Rate ${star} of ${max}`}
                onMouseEnter={() => setHover(star)}
                onClick={() => onChange(star)}>
          {star <= (hover || value) ? '★' : '☆'}
        </button>
      ))}
    </div>
  );
}
```
### The trick is `hover || value`
While the mouse is over star 4, `hover` is 4, so stars 1 to 4 are filled as a
preview. When the mouse leaves, `hover` becomes 0, which is falsy, so it falls back
to the actual saved `value`. One line handles both the preview and the real state.

---

## Problem 7 — Pagination (client-side)
```jsx
function Paginated({ items, perPage = 10 }) {
  const [page, setPage] = useState(1);
  const totalPages = Math.ceil(items.length / perPage);
  const slice = items.slice((page - 1) * perPage, page * perPage);

  useEffect(() => { setPage(1); }, [items]);   // reset when the data set changes

  return (
    <>
      <ul>{slice.map(i => <li key={i.id}>{i.name}</li>)}</ul>
      <button disabled={page === 1} onClick={() => setPage(p => p - 1)}>Prev</button>
      <span>Page {page} of {totalPages || 1}</span>
      <button disabled={page >= totalPages} onClick={() => setPage(p => p + 1)}>Next</button>
    </>
  );
}
```
### Edge cases to name out loud
- Disable Previous on page 1 and Next on the last page.
- An empty list should not show "Page 1 of 0".
- **Reset to page 1 when the data changes.** If the user is on page 5 and applies a
  filter that leaves 3 results, they would see an empty page. This is a very common
  bug.

*(You have built `xpagination` before. Mention it.)*

---

## Problem 8 — Counter / timer (the `useRef` + cleanup check)
```jsx
function Timer() {
  const [seconds, setSeconds] = useState(0);
  const [running, setRunning] = useState(false);
  const idRef = useRef(null);

  useEffect(() => {
    if (!running) return;
    idRef.current = setInterval(() => setSeconds(s => s + 1), 1000);   // functional updater!
    return () => clearInterval(idRef.current);                          // cleanup!
  }, [running]);

  return (
    <>
      <h1>{seconds}s</h1>
      <button onClick={() => setRunning(r => !r)}>{running ? 'Pause' : 'Start'}</button>
      <button onClick={() => { setRunning(false); setSeconds(0); }}>Reset</button>
    </>
  );
}
```
### They are checking exactly two things here
**1. `setSeconds(s => s + 1)` and not `setSeconds(seconds + 1)`.**
The interval callback was created once. It captured `seconds` as 0 in a closure and
will never see a newer value. So `seconds + 1` would be `0 + 1` forever. The
function form always receives the latest value.

**2. The `clearInterval` cleanup.**
Without it, the timer keeps running after the component is gone and tries to update
state that no longer exists.

Point both out while you type. They are the entire reason this problem is asked.

---

## If they ask for plain JS/DOM instead
```js
document.querySelector('#list').addEventListener('click', (e) => {   // delegation
  const btn = e.target.closest('button[data-id]');
  if (!btn) return;
  removeItem(btn.dataset.id);
});
```

---

### ✅ Tonight's task
Build **Problem 1** and **Problem 2** from an empty file, with no copy and paste.

If you can build those two while explaining what you are doing, you can handle
anything they are likely to ask at this level.
