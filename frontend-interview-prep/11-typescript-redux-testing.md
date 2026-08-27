# 11 · TypeScript, State Management and Testing 🔴
**Time needed: 45 minutes. Read this straight after the React file.**

These are all on your resume, so they are fair game. TypeScript in particular:
you list it in your headline, so expect questions. Part C on choosing between
Redux, Zustand and React Query is the one most likely to come up in a design or
architecture conversation.

---

# Part A · TypeScript

## First, the context: what problem does TypeScript solve?

JavaScript only tells you about a mistake when the code runs.

```js
const user = { name: 'Sujith' };
console.log(user.nmae);     // undefined. No error. Silent bug.

function total(a, b) { return a + b; }
total('5', 3);              // "53". No error. Wrong answer.
```

Both bugs reach production and show up as a strange value on someone's screen.

TypeScript adds **types**, which are checked while you write the code. Both of the
above become errors in your editor, before the code ever runs.

```ts
const user: { name: string } = { name: 'Sujith' };
console.log(user.nmae);     // ❌ Property 'nmae' does not exist

function total(a: number, b: number) { return a + b; }
total('5', 3);              // ❌ Argument of type 'string' is not assignable
```

### The important detail: TypeScript disappears at build time
The browser cannot run TypeScript. It is compiled to plain JavaScript, and all the
types are removed. **There is no type checking at runtime.**

This matters: if an API returns something different from what you declared,
TypeScript will not catch it. It trusted you. That is why you still validate data
coming from outside.

### Say this
> "TypeScript catches type errors while I write the code rather than when a user
> hits them. On a banking platform that mattered a lot, because a wrong shape in a
> payment form is an expensive bug. It also makes refactoring much safer, since
> renaming a field shows every place that breaks. The thing to remember is that the
> types are erased at build time, so it does not validate API responses at runtime."

---

## Q1. `interface` vs `type` 🔴

Both describe the shape of an object. They overlap a lot.

```ts
interface User {
  id: number;
  name: string;
  email?: string;        // optional
  readonly createdAt: Date;
}

type User = {
  id: number;
  name: string;
};
```

### The differences that matter
**1. `interface` can be reopened. `type` cannot.**
```ts
interface User { id: number; }
interface User { name: string; }   // ✅ merged into one
```

**2. `type` can do things `interface` cannot:**
```ts
type Status = 'idle' | 'loading' | 'error';    // union
type ID = string | number;
type Point = [number, number];                  // tuple
```

### What to say
> "I use `interface` for object shapes, especially props and API models, because it
> reads well and can be extended. I use `type` when I need a union, a tuple, or
> something computed. In practice the team convention matters more than the
> difference."

---

## Q2. Typing React components 🔴 (most likely practical question)

```tsx
interface LoanCardProps {
  bank: string;
  rate: number;
  featured?: boolean;                    // optional
  onApply: (id: string) => void;         // a function prop
  children: React.ReactNode;             // anything renderable
}

function LoanCard({ bank, rate, featured = false, onApply, children }: LoanCardProps) {
  return <div>{bank} — {rate}%</div>;
}
```

### Typing hooks
```tsx
const [count, setCount] = useState(0);              // inferred as number
const [user, setUser] = useState<User | null>(null); // must be explicit
const [loans, setLoans] = useState<Loan[]>([]);      // otherwise it is never[]

const inputRef = useRef<HTMLInputElement>(null);
```
> "`useState(0)` infers `number` on its own. But `useState(null)` infers `null`, so
> if it will later hold a user I write `useState<User | null>(null)`. Same with an
> empty array, which would otherwise be `never[]`."

### Typing events
```tsx
const onChange = (e: React.ChangeEvent<HTMLInputElement>) => setQuery(e.target.value);
const onSubmit = (e: React.FormEvent<HTMLFormElement>) => { e.preventDefault(); };
const onClick  = (e: React.MouseEvent<HTMLButtonElement>) => { ... };
```

---

## Q3. The types worth knowing

**Union** — one of several options.
```ts
type Status = 'idle' | 'loading' | 'success' | 'error';
```
Very useful for the four UI states from file 06. The compiler then forces you to
handle each case.

**Generic** — a type that takes a type as a parameter.
```ts
function first<T>(items: T[]): T | undefined {
  return items[0];
}
first([1, 2, 3]);          // returns number | undefined
first(['a', 'b']);         // returns string | undefined
```
Read `<T>` as "whatever type goes in, the same type comes out". Without generics you
would write this function once per type, or fall back to `any` and lose the safety.

**Utility types** — built in helpers.
```ts
Partial<User>            // every field optional. Good for updates.
Required<User>           // every field required
Pick<User, 'id' | 'name'>  // only these fields
Omit<User, 'password'>     // everything except these
Record<string, number>     // an object with string keys and number values
```

**`unknown` vs `any`** — a good question to get right.
> "`any` switches type checking off completely. `unknown` also means 'I do not know
> the type', but it forces you to check before using it. So `unknown` is the safe
> version. I use `any` only as a temporary escape hatch, never as a habit."

**Enum** — a fixed set of named values.
```ts
enum Role { Admin = 'ADMIN', User = 'USER' }
```
Many teams prefer a union of string literals instead, because it produces no extra
JavaScript.

---

## Q4. Quick TypeScript questions

- **`?` vs `| undefined`?** `email?: string` means the key may be absent.
  `email: string | undefined` means the key must exist but may hold `undefined`.
- **What is type inference?** TypeScript works out the type without you writing it.
  `const n = 5` is already `number`. Do not annotate what is obvious.
- **What is `as`?** A type assertion. You are telling the compiler "trust me, this is
  a User". It does no checking, so it is a small risk each time.
- **Is TypeScript slower at runtime?** No. It is erased at build time. The output is
  plain JavaScript.
- **What is `strict` mode?** A tsconfig setting that turns on the important checks,
  most usefully `strictNullChecks`, which forces you to handle `null` and
  `undefined`. Worth having on.

---

# Part B · Redux and Redux Toolkit

## First, the context: what problem does Redux solve?

In React, state flows down through props. That works well until many unrelated
components across the app need the same data, and events from anywhere need to
change it.

Redux puts that shared state in one **store** outside the component tree. Any
component can read from it, and any component can dispatch an action to change it.

### The one-way cycle, which is the whole idea
```
  Component
     |  dispatch(action)          "ADD_TO_CART"
     v
  Reducer          a pure function: (currentState, action) -> newState
     |
     v
   Store           the single source of truth
     |
     v
  Component re-renders with the new value
```

The value of this shape is **predictability**. State can only change by dispatching
an action, and a reducer is a pure function, so given the same state and action you
always get the same result. That is why the Redux DevTools can show you every action
and let you step backwards through them.

### The three principles
1. **One store** for the application.
2. **State is read only.** You never mutate it directly, you dispatch an action.
3. **Reducers are pure functions.** No API calls, no random values, no mutation.

---

## Q5. Redux Toolkit — why it replaced classic Redux 🔴

Old Redux needed a lot of files: action type constants, action creators, a reducer
with a switch statement, and manual immutable updates with spread everywhere.

Redux Toolkit (RTK) is the official modern way and removes most of it.

```ts
import { createSlice } from '@reduxjs/toolkit';

const cartSlice = createSlice({
  name: 'cart',
  initialState: { items: [] as Item[], total: 0 },
  reducers: {
    addItem(state, action) {
      state.items.push(action.payload);     // looks like mutation, but it is safe
      state.total += action.payload.price;
    },
    clearCart(state) {
      state.items = [];
      state.total = 0;
    },
  },
});

export const { addItem, clearCart } = cartSlice.actions;
export default cartSlice.reducer;
```

### 🔴 "That looks like you are mutating state. Is that not forbidden?"
This is the exact follow up. The answer:
> "RTK uses **Immer** underneath. You write what looks like mutation, but Immer
> tracks the changes against a draft and produces a new immutable state object. So
> the rules are unchanged, the code is just far more readable than nested spreads."

### Using it in a component
```tsx
const items = useSelector((state: RootState) => state.cart.items);
const dispatch = useDispatch();
dispatch(addItem(loan));
```

---

## Q6. Selectors and memoization 🔴 (your dashboard story)

A **selector** is a function that reads a slice of state.

```ts
const selectItems = (state: RootState) => state.cart.items;
```

### The performance problem you fixed at Standard Bank
```ts
// ❌ creates a NEW array every time it runs
const selectExpensive = (state) => state.cart.items.filter(i => i.price > 1000);
```
`useSelector` compares the result with the previous one by reference. A new array is
always a new reference, so the component re-renders on **every** store update, even
one that has nothing to do with the cart.

```ts
// ✅ memoised with Reselect (built into RTK)
import { createSelector } from '@reduxjs/toolkit';

const selectExpensive = createSelector(
  [selectItems],
  (items) => items.filter(i => i.price > 1000)
);
```
Now the filter only runs when `items` actually changes, and the same reference comes
back otherwise. **This is exactly what you did to help get Lighthouse from 62 to 88.**

---

## Q7. Async in Redux

```ts
export const fetchLoans = createAsyncThunk('loans/fetch', async () => {
  const res = await fetch('/api/loans');
  return res.json();
});

const loansSlice = createSlice({
  name: 'loans',
  initialState: { data: [], status: 'idle' },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchLoans.pending,   (s) => { s.status = 'loading'; })
      .addCase(fetchLoans.fulfilled, (s, a) => { s.status = 'success'; s.data = a.payload; })
      .addCase(fetchLoans.rejected,  (s, a) => { s.status = 'error'; s.error = a.error.message; });
  },
});
```
Note the three cases: pending, fulfilled and rejected. That is the loading, success
and error triad from file 06, built into the tool.

### 🔴 "When would you NOT use Redux?"
An important question, and the honest answer scores well.
> "Most of the time. If state belongs to one component, `useState` is correct. If
> two siblings need it, I lift it up. If it is server data, React Query or SWR is a
> better fit than Redux, because caching and refetching come for free. I would reach
> for Redux when there is genuinely complex client state shared widely, with a lot of
> interactions changing it. On the Standard Bank dashboard that was justified. For a
> small marketing site it would be over-engineering."

---

# Part C · Choosing between Redux, Zustand and React Query 🔴🔴

## First, the context: there are two completely different kinds of state

This is the idea everything else in this section rests on. Get this right and the
rest of the answers fall out of it.

**Server state** is data that really lives on a server. Your app only holds a copy.
- It can become **stale** the moment you fetch it, because someone else can change it.
- Getting it is **asynchronous**, so it always has loading and error states.
- The same data is often needed by several screens.
- Examples: the list of banks, a student's application status, the current user record.

**Client state** is data that only exists in the browser. You own it completely.
- It is **synchronous**. You set it, it is set.
- It can never be stale, because there is no other source of truth.
- Examples: is the sidebar open, which tab is selected, the current step of a form,
  a dark mode toggle, items in a cart before checkout.

### Why this matters
**Most "we need a global state manager" problems are actually server state being
managed by hand.** Teams put API responses in Redux, then write loading flags, error
flags, refetch logic and cache invalidation themselves. That is a large amount of
code that a data fetching library already gives you.

Once you separate the two, the tool choice becomes obvious:

```
Server state  →  React Query  (or RTK Query, or SWR)
Client state  →  useState → Context → Zustand → Redux Toolkit
```

🔴 **This is your best answer to almost any state management question.** Say the
distinction first, then pick the tool. It shows you are reasoning, not reciting
library names.

---

## Q8. The decision path — what would you actually choose? 🔴

Work down this list. Stop at the first one that fits.

**1. Only one component needs it → `useState`.**
Most state is like this. Do not overthink it.

**2. Two or three nearby components need it → lift it to the shared parent.**

**3. It comes from an API → React Query.**
Caching, background refetching, deduplication, retries and loading and error states,
all handled. This covers far more cases than people expect.

**4. Client state, shared widely, changes rarely → Context.**
Theme, language, the current user object. Context is fine here because it rarely
updates, so the re-render cost does not matter.

**5. Client state, shared widely, changes often → Zustand.**
A cart, a complex filter panel, a wizard's state, notification toasts. Zustand gives
you selector based subscriptions, so only the components reading that specific value
re-render.

**6. Large app, large team, complex flows → Redux Toolkit.**
When you need strict conventions everyone follows, middleware, and serious debugging
tools. This is where your Standard Bank platform sat.

### Say this
> "I start with local state and only move up when there is a real reason. The first
> question I ask is whether it is server state or client state, because those need
> different tools. Server data goes in React Query so I am not hand-writing caching
> and loading flags. For client state I use Context when it barely changes, Zustand
> when it changes often, and Redux Toolkit when the app is big enough that the
> conventions and the DevTools are worth the setup."

---

## Q9. React Query — what problem does it solve? 🔴

### The code it replaces
This is the `useEffect` pattern from file 06:

```jsx
const [data, setData] = useState([]);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(null);

useEffect(() => {
  const controller = new AbortController();
  (async () => {
    try {
      setLoading(true);
      const res = await fetch('/api/loans', { signal: controller.signal });
      if (!res.ok) throw new Error(res.status);
      setData(await res.json());
    } catch (e) {
      if (e.name !== 'AbortError') setError(e.message);
    } finally {
      setLoading(false);
    }
  })();
  return () => controller.abort();
}, []);
```

Here is the same thing with React Query:

```jsx
const { data, isLoading, error } = useQuery({
  queryKey: ['loans'],
  queryFn: getLoans,
});
```

### What you get that the hand-written version does not have
- **Caching.** Navigate away and back, the data is shown instantly from cache while
  it refetches quietly in the background.
- **Deduplication.** Three components asking for `['loans']` at the same time cause
  **one** network request, not three.
- **Background refetching.** Refetches when the window regains focus, when the
  network reconnects, or on an interval you choose.
- **Race condition handling.** The problem from file 06 is handled for you.
- **Retries** with backoff on failure.
- **Pagination and infinite scroll** helpers.
- **Optimistic updates** with automatic rollback.

> "The point is not that it is shorter. It is that the hand-written version is only
> correct for the simple case. Once you need caching, deduplication and refetch on
> focus, you are rebuilding React Query badly."

### The concepts they will ask about

**`queryKey`** — the cache key. React Query stores results against it. Include every
value the query depends on, so changing a filter fetches fresh data:
```js
useQuery({ queryKey: ['loans', bankType, page], queryFn: () => getLoans(bankType, page) });
```

**`staleTime` vs `gcTime`** 🔴 — the most common React Query interview question.

| | What it means |
|---|---|
| `staleTime` | How long the data is treated as **fresh**. While fresh, React Query will not refetch it. Default is 0, meaning immediately stale. |
| `gcTime` | How long **unused** data stays in the cache before being thrown away. Default 5 minutes. *(This was called `cacheTime` before v5.)* |

> "`staleTime` controls refetching. `gcTime` controls memory. Data can be stale but
> still cached, which is what makes stale-while-revalidate work: you see the old data
> instantly, and it updates when the fresh response arrives."

**Mutations** — for writes.
```jsx
const queryClient = useQueryClient();

const { mutate, isPending } = useMutation({
  mutationFn: createApplication,
  onSuccess: () => {
    // the list is now out of date, so mark it stale and refetch
    queryClient.invalidateQueries({ queryKey: ['applications'] });
  },
});
```

**`invalidateQueries`** — "this cached data is now wrong, refetch it." This is how you
keep a list in sync after creating or deleting something.

**Optimistic update** — update the UI before the server confirms, and roll back if it
fails. Good for a like button or a checkbox, where waiting feels slow.

---

## Q10. Zustand — what is it and why do people like it? 🔴

### The store is just a hook
```js
import { create } from 'zustand';

const useCartStore = create((set) => ({
  items: [],
  addItem: (item) => set((state) => ({ items: [...state.items, item] })),
  clear: () => set({ items: [] }),
}));
```

Using it in a component:
```jsx
function CartCount() {
  const count = useCartStore((state) => state.items.length);
  return <span>{count}</span>;
}
```

### The three things that make it different
**1. No Provider.** The store lives outside React. You do not wrap your app in
anything. You can even read and write it from outside a component.

**2. Selector based subscriptions — this is the important one.** 🔴
`useCartStore(state => state.items.length)` subscribes **only** to that value. If some
other part of the store changes, this component does not re-render.

Compare that with Context, where **every** consumer re-renders whenever the context
value changes. Zustand solves the exact problem Context has.

**3. Very small.** Around 1 KB, against roughly 12 to 13 KB for Redux Toolkit.

### Middleware worth naming
```js
const useStore = create(persist(devtools((set) => ({ ... })), { name: 'cart' }));
```
`persist` saves to localStorage, `devtools` connects to the Redux DevTools extension,
`immer` lets you write mutating-looking updates.

### Say this
> "Zustand is a minimal client state store. The store is a hook, there is no provider,
> and you subscribe with a selector so only the components using that specific value
> re-render. That last part is what makes it better than Context for state that
> changes often. It is a good middle ground: more structured than passing props
> around, far less setup than Redux."

---

## Q11. Redux Toolkit — when is it still the right choice?

Redux is not obsolete. It is just no longer the default.

**Choose Redux Toolkit when:**
- The app is large and several developers work on it, and you want one enforced way
  of doing things.
- State transitions are complex and many parts of the app react to the same events.
- You want the **Redux DevTools**: every action logged, state inspected at each step,
  and time travel debugging. On a banking platform where you must explain how the app
  reached a state, this genuinely matters.
- You need middleware for cross-cutting concerns like logging, analytics or complex
  async orchestration.
- The codebase already uses it. Rewriting working state management is rarely worth it.

**RTK Query** is Redux's own answer to React Query, built into Redux Toolkit. If you
are already on Redux, use RTK Query rather than adding React Query as a second
library. They do the same job.

---

## Q12. The comparison table 🔴

| | **Redux Toolkit** | **Zustand** | **React Query** |
|---|---|---|---|
| Kind of state | Client | Client | **Server** |
| Size (approx) | 12–13 KB | ~1 KB | ~13 KB |
| Provider needed | Yes | **No** | Yes (`QueryClientProvider`) |
| Boilerplate | Moderate (slices) | Very little | Very little |
| Caching | No, you write it | No, you write it | **Yes, built in** |
| Loading / error states | You write them | You write them | **Given to you** |
| Avoids re-renders via | `useSelector` + memoised selectors | selector in the hook | per-query subscription |
| DevTools | Excellent | Via middleware | Excellent |
| Learning curve | Medium | Low | Medium |
| Best for | Large apps, strict conventions, complex flows | Shared client state that changes often | Anything from an API |

**The single most important row is the first one.** Redux and Zustand solve the same
problem. React Query solves a different one.

---

## Q13. The questions you should expect, with short answers 🔴

**"Redux or React Query — which would you pick?"**
A trick question. They are not alternatives.
> "They solve different problems, so it is not really either-or. React Query manages
> server state, Redux manages client state. A common setup is both: React Query for
> everything from the API, and a small Redux or Zustand store for genuine UI state."

**"Why not just `useEffect` and `useState` for fetching?"**
> "It works for a single simple screen. It stops being enough once you need caching
> between screens, deduplication when several components ask for the same data,
> refetching when the user comes back to the tab, retries, and correct handling of
> race conditions. At that point you are writing a worse version of React Query."

**"Why not put everything in Context?"**
> "Two reasons. Every consumer re-renders when the context value changes, so it is a
> poor fit for state that changes often. And Context is only a transport mechanism.
> It does not cache, refetch, or give you loading and error states, so for server data
> you still have to write all of that yourself."

**"Redux or Zustand for a new project?"**
> "For most new projects, Zustand. It is far less setup and the selector based
> subscriptions handle re-renders well. I would pick Redux Toolkit when the app is
> large and several people work on it and the enforced conventions and DevTools are
> worth the extra weight, or when the codebase already uses it."

**"What is `staleTime`?"** → How long data counts as fresh before React Query will
refetch it. Different from `gcTime`, which is how long unused data stays in memory.

**"How does React Query know when to refetch?"** → When the data is stale **and** one
of the triggers fires: the component mounts, the window regains focus, the network
reconnects, or you call `invalidateQueries`.

**"How do you update a list after creating an item?"** → A mutation, then
`invalidateQueries` on the list's key in `onSuccess`. Or write the new item straight
into the cache with `setQueryData` if you want to avoid the refetch.

**"How does Zustand avoid re-renders without a Provider?"** → The store is outside
React. Each component subscribes through a selector, and only re-renders when the
value that selector returns actually changes.

**"Is Redux dead?"**
> "No, but it is no longer the automatic choice. Redux Toolkit fixed most of the
> boilerplate complaints, and RTK Query covers data fetching. It is still the right
> answer for large applications, and a lot of production code runs on it. What changed
> is that reaching for it on day one of a small project is now over-engineering."

---

## 🔴 Your own answer — use your real experience

This is the strongest version of this answer available to you, because it is true:

> "On the Standard Bank platform we used Redux, and later Redux Toolkit. Looking back,
> a lot of what we kept in the store was server data, and that meant we hand-wrote
> loading flags, error flags and cache invalidation for each feature.
>
> If I were building it again, I would put the server data in React Query or RTK
> Query and keep the Redux store for genuine client state only. The store would be
> much smaller, and a whole category of bugs about stale data would just not exist.
>
> On QKart I used Context and custom hooks with memoisation instead, which cut
> re-renders by about 40%. That was the right size of solution for that app — adding
> Redux there would have been over-engineering."

This answer does three things at once: it shows real production experience, it shows
you can critique your own past decisions, and it shows you match the tool to the size
of the problem. That is a senior sounding answer at any level.

---

# Part D · Testing

## First, the context: what are you actually testing?

The goal is not "100% coverage". The goal is **confidence that a change did not
break something**.

| Type | What it checks | Tool |
|---|---|---|
| Unit | One function or component alone | Jest, JUnit |
| Integration | A few pieces working together | React Testing Library |
| End to end | The whole app in a real browser | Cypress, Playwright |

---

## Q14. React Testing Library — the core idea 🔴

> "React Testing Library's principle is to test the component the way a **user** sees
> it, not the way it is built internally. So I query by visible text, labels and
> roles, and I assert on what appears on screen. I avoid testing internal state,
> because if I refactor how the state is stored but the behaviour is the same, the
> test should still pass. A test that breaks on a refactor is a cost, not a safety
> net."

```tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('shows an error when the email is invalid', async () => {
  render(<LeadForm />);

  await userEvent.type(screen.getByLabelText(/email/i), 'not-an-email');
  await userEvent.click(screen.getByRole('button', { name: /submit/i }));

  expect(await screen.findByText(/enter a valid email/i)).toBeInTheDocument();
});
```

### The query priority, worth knowing
`getByRole` → `getByLabelText` → `getByText` → and `getByTestId` only as a last
resort. The order is deliberate: the top ones are how a real user, and a screen
reader, find things.

### `getBy` vs `queryBy` vs `findBy`
- `getBy` — expects it to be there now. Throws if missing.
- `queryBy` — returns `null` if missing. Use this to assert something is **not** there.
- `findBy` — waits for it to appear. Use for anything async.

---

## Q15. Mocking an API call

```tsx
global.fetch = jest.fn(() =>
  Promise.resolve({ ok: true, json: () => Promise.resolve([{ id: 1, bank: 'SBI' }]) })
);
```
> "I mock the network so tests are fast and do not depend on a real server being up.
> In a larger project I would use MSW, which intercepts at the network level, so the
> component code does not have to know it is being tested."

### What would you test first?
A good answer, and it shows judgement:
> "The parts where a bug is expensive. On the Business Card application that was the
> form validation and the step navigation, because a broken step could lose a user's
> data. I would not write tests for a component that only renders a heading."

---

## ✅ Check yourself before moving on
1. Explain in one sentence what TypeScript catches, and when the types disappear.
2. Type a React component's props, and `useState` for a value that starts as `null`.
3. Explain why RTK lets you write `state.items.push(...)` safely.
4. Explain the selector memoization problem, using your dashboard story.
5. **Explain the difference between server state and client state, then map each to a
   tool.** This is the highest value answer in this file.
6. Explain `staleTime` vs `gcTime`.
7. Explain how Zustand avoids re-renders without a Provider.
8. Give your own answer about what you would change on the Standard Bank store.
9. Explain the React Testing Library principle in one sentence.
