# 11 · TypeScript, Redux and Testing 🔴
**Time needed: 45 minutes. Read this straight after the React file.**

These three are on your resume, so they are fair game. TypeScript in particular:
you list it in your headline, so expect questions.

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

# Part C · Testing

## First, the context: what are you actually testing?

The goal is not "100% coverage". The goal is **confidence that a change did not
break something**.

| Type | What it checks | Tool |
|---|---|---|
| Unit | One function or component alone | Jest, JUnit |
| Integration | A few pieces working together | React Testing Library |
| End to end | The whole app in a real browser | Cypress, Playwright |

---

## Q8. React Testing Library — the core idea 🔴

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

## Q9. Mocking an API call

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
5. Explain the React Testing Library principle in one sentence.
