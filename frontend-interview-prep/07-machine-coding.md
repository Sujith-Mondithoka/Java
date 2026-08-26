# 07 · Machine Coding Round 🔴
**Budget: 60 minutes — and TYPE these, don't read them.**
Reading code creates the illusion of competence. Open StackBlitz/CodeSandbox and
build problems 1 and 2 from scratch. That's the whole hour.

---

## How to run the round (the process is half the score)

1. **Clarify for 60 seconds.** "Should filtering be client-side or via API? Do you
   want it debounced? Should state persist on refresh?" *Candidates who clarify
   consistently outscore candidates who start typing immediately.*
2. **Say your plan out loud.** "State: `query`, `items`, `loading`. I'll debounce
   the input, derive the filtered list during render, then handle the empty state."
3. **Build the ugly working version first.** Working > pretty. You can style at the end.
4. **Narrate while typing.** Silence reads as stuck.
5. **Handle the edge cases out loud** — empty list, error, 0 results, long text.
   Even saying *"I'd add an error state here if I had more time"* scores.
6. **Refactor at the end** if time allows: extract a component, pull out a custom hook.

**Their favourite problems for this level:** search/filter list · todo CRUD ·
counter · accordion/tabs · star rating · form validation · fetch users and
display · pagination · modal · countdown timer.

---

## Problem 1 🔴 — Search + filter list with debounce
*The single most-asked machine-coding question in Indian frontend interviews.*

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
**Points to say aloud:** filtered list is **derived during render**, not stored in
state · debounce cuts API/compute churn · `key` is a stable id · empty state
handled · `.trim()` and case-insensitive matching are the edge cases they check.

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
**The retry button is the detail almost nobody adds. Add it.**

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
Highlights: `<form onSubmit>` so **Enter works** · functional updaters ·
map/filter never mutate · `crypto.randomUUID()` not array index · the remaining
count is derived, not stored.

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
**The senior touch:** errors only show **after blur**, not while the user is still
typing their first character; the submit button is disabled while in flight to
prevent double submission; single `handleChange` keyed by `name`.

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
"One `openId` instead of a boolean per item makes 'only one open' impossible to get
wrong. For multi-open I'd hold a `Set`. `aria-expanded` makes it accessible." —
*and an FAQ accordion with JSON-LD is an SEO win, which you can mention.*

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
`hover || value` is the whole trick — hover preview falls back to the committed value.

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
Edge cases to name: disabled buttons at the boundaries, empty list, resetting to
page 1 when filters change. *(You've built `xpagination` before — say so.)*

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
They are checking exactly two things: `setSeconds(s => s + 1)` (not `seconds + 1`)
and the `clearInterval` cleanup. Point both out.

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

### ✅ Tonight's deliverable
Build **Problem 1** and **Problem 2** from a blank file, no copy-paste. If you can
do those two while talking, you can handle anything they throw at this level.
