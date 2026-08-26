# 08 · Frontend System Design 🔴
**Time needed: 45 minutes**

This section was missing from the first version of the guide. It matters, because
at this level the system design round is where they check if you can **plan** before
you code, not just type React.

---

## First, the context: what "frontend system design" actually means

When a backend engineer hears "system design", they think about databases, servers
and load balancing. **You will not be asked that.**

A frontend system design question sounds like this:

- "How would you build the loan search page?"
- "Design an autocomplete search box."
- "How would you structure a multi step application form?"
- "We have a page with 5,000 rows. How do you make it fast?"

They are checking six things:

1. Do you **ask questions** before you start?
2. Can you break a screen into **components**?
3. Do you know **where the state should live**?
4. Do you think about the **API**, not just the UI?
5. Do you handle **loading, error and empty** cases?
6. Do you think about **performance** without being asked?

You do not need a perfect answer. You need a clear, ordered way of thinking.

---

## The framework: answer every design question in this order

Memorise these six steps. Use them for any question they ask.

```
1. CLARIFY     Ask 2-3 questions. Never start immediately.
2. COMPONENTS  Break the screen into a component tree.
3. STATE       Decide what state exists and who owns it.
4. DATA        What API calls, when, and in what shape.
5. EDGE CASES  Loading, error, empty, slow network, long text.
6. PERFORMANCE One or two improvements, with a reason.
```

**Step 1 is the one candidates skip, and it is the one that scores most.**
Starting to code before asking anything is the most common failure in this round.

Useful clarifying questions that work for almost any problem:

- "Is the filtering done on the client, or does the API do it?"
- "Roughly how many items are we showing? Ten, or ten thousand?"
- "Does this need to work for logged out users, and does it need to rank on Google?"
- "Is the data the same for everyone, or is it per user?"

That last question is powerful in a Next.js interview, because the answer decides
SSG, ISR or SSR.

---

## Design 1 🔴 — An autocomplete search box

*The most commonly asked frontend design question in India.*

### Step 1: Clarify
- "Does the API return results, or do I filter a list I already have?"
- "Should recent searches be remembered?"
- "Do we need keyboard navigation with arrow keys?"

### Step 2: Components
```
SearchBox
 ├── <input>            the text field
 ├── SuggestionList     shown only when there are results
 │    └── SuggestionItem
 └── StatusArea         spinner / "no results" / error
```

### Step 3: State
| State | Where it lives | Why |
|---|---|---|
| `query` | SearchBox | what the user typed |
| `debouncedQuery` | SearchBox (custom hook) | what we actually search with |
| `results` | SearchBox | what came back |
| `loading`, `error` | SearchBox | to show the right status |
| `activeIndex` | SearchBox | which suggestion is highlighted |

### Step 4: Data flow
```
user types  →  query updates on every keystroke
            →  debounce waits 400ms of silence
            →  ONE API call fires
            →  results render
```

### Step 5: Edge cases — say all of these out loud
- **Empty query.** Do not call the API at all. Close the dropdown.
- **No results.** Show "No banks found for axis". Do not show an empty box.
- **Error.** Show a short message and let them try again.
- **Race condition.** The user types "ax", then "axis". Two requests are running.
  If "ax" answers last, the screen shows the wrong list. Fix it by cancelling the
  old request with `AbortController`.

- **Clicking outside** should close the dropdown.
- **Keyboard.** Arrow keys move, Enter selects, Escape closes.

### Step 6: Performance
- **Debounce** turns 9 keystrokes into 1 request. That is a 90% reduction in load
  on the backend.

- **Cache** results per query in a simple object, so pressing backspace does not
  refetch something you already have.

- If the list is very long, **virtualise** it so only visible rows are in the DOM.

### The 60 second version to say out loud
> "I would hold the typed text in state, and pass it through a `useDebounce` hook so
> the API is only called after the user pauses for around 400 milliseconds. The
> request result goes into `results`, with separate `loading` and `error` state.
>
> I would show four states: loading, error, empty and results, because an empty
> dropdown with no message looks broken.
>
> The main bug to guard against is a race condition. If two requests are in flight,
> the slower older one can overwrite the newer results. I cancel the previous request
> with an `AbortController` in the effect cleanup. And I would cache results per
> query so backspacing does not refetch."

---

## Design 2 🔴 — A loan listing page with filters and pagination

*This is essentially their real product, so it is very likely to come up.*

### Step 1: Clarify
- "How many loans are there in total? Hundreds or thousands?"
- "Should filters appear in the URL, so a student can share the link?"
- "Does this page need to rank on Google?"

That last question changes the whole design, so ask it.

### Step 2: Components
```
LoansPage
 ├── FilterPanel
 │    ├── BankTypeFilter (public / private / NBFC)
 │    ├── AmountRangeFilter
 │    └── ClearAllButton
 ├── ResultsHeader     "24 loans found"  + sort dropdown
 ├── LoanList
 │    └── LoanCard × N
 └── Pagination
```

### Step 3: State, and the important decision
```
filters   = { type: 'public', maxRate: 10, page: 2 }
loans     = []
loading / error
```

**The key insight to mention: keep the filters in the URL.**

```
/loans?type=public&maxRate=10&page=2
```

Why this matters:

- The student can **share or bookmark** their filtered view.
- The **back button works** correctly.
- Refreshing the page keeps the filters.
- And for Next.js, the server can read those filters and render the page on the
  server, so it is crawlable.

If you keep filters only in `useState`, all four of those break. Saying this shows
product thinking, not just React knowledge.

### Step 4: Data — client side or server side filtering?
| | Filter on client | Filter on server |
|---|---|---|
| Good when | Under ~500 items | Thousands of items |
| Speed | Instant, no network | One request per change |
| Data sent | All items at once | Only the current page |

> "With a few hundred loans I would fetch once and filter in memory, which feels
> instant. With thousands, I would send the filters to the API and paginate on the
> server, because downloading everything would be slow and wasteful on mobile data."

### Step 5: Edge cases
- No results after filtering → "No loans match your filters" **plus a Clear filters
  button**. Do not leave a dead end.

- Changing a filter must **reset the page back to 1**. A very common bug.
- Disable Previous on page 1 and Next on the last page.
- Long bank names must not break the card layout.

### Step 6: Performance and rendering strategy
> "The loan list is the same for every visitor, so I would use **ISR** with a
> revalidate of about an hour. That gives static file speed from the CDN, and the
> rates are never more than an hour stale. Images go through `next/image`. If the
> list ever grows into thousands of rows on one page, I would virtualise it."

---

## Design 3 🔴 — A multi step application form

**This is your home ground.** You built a 14 screen onboarding flow (Business Card)
and a 7 screen recall workflow with navigation guards. If this question comes up,
answer it from real experience, not theory.

### Step 1: Clarify
- "How many steps, and can the user go back?"
- "If they close the browser, should the progress be saved?"
- "Is validation per step, or all at the end?"

### Step 2: Components
```
FormWizard              ← owns ALL the form data
 ├── ProgressBar        step 2 of 4
 ├── StepPersonal
 ├── StepEducation
 ├── StepLoanAmount
 ├── StepReview
 └── NavButtons         Back / Next / Submit
```

### Step 3: State — the important decision
**All form data lives in the parent `FormWizard`, not in each step.**

```jsx
const [formData, setFormData] = useState({ name: '', email: '', course: '' });
const [step, setStep] = useState(1);
const [errors, setErrors] = useState({});
```

**Why?** If each step kept its own state, going back to step 1 would unmount step 2
and destroy everything typed there. Keeping the data in the parent means the steps
become simple display components, and nothing is lost when moving between them.

*(This is exactly the bug you fixed on the Business Card application at Standard
Bank. Say so. A design answer backed by "I hit this in production and here is what
went wrong" is far stronger than a theoretical one.)*

### Step 4 and 5: Validation and edge cases
- Validate the current step before allowing Next.
- Show errors only **after** the user leaves a field, not while they are typing the
  first letter.

- Disable Submit while the request is in flight, so it cannot be double submitted.
- Save progress to `localStorage` so a refresh does not lose everything.
- On submit failure, keep all the data and show a retry. Never clear the form.

### Step 6: Performance
> "The steps that are not visible do not need to be rendered at all. If a step
> imported something heavy, like a document upload widget, I would lazy load it with
> `next/dynamic` so it is not in the initial bundle."

---

## Design 4 — "How would you make a reusable component?"

They may hand you a button or a card and ask how you would design its API.

### The principles, in simple words
**1. It should not know where it is used.**
A `LoanCard` should not contain `if (page === 'home')`. Pass differences in as props.

**2. Props describe *what*, not *how*.**
```jsx
<Button variant="primary" size="sm" loading={isSaving}>Apply</Button>
```
Not `<Button backgroundColor="#0055ff" paddingLeft="12px">`. If you pass raw styles,
every screen looks slightly different and you have no design system.

**3. Use `children` for the content.**
```jsx
<Card>
  <h3>SBI</h3>
  <p>9.15%</p>
</Card>
```
This is far more flexible than `<Card title="SBI" subtitle="9.15%" />`, because the
next screen will always need something you did not predict.

**4. Pass the rest of the props through.**
```jsx
function Button({ variant, children, ...rest }) {
  return <button className={styles[variant]} {...rest}>{children}</button>;
}
```
Now `onClick`, `disabled`, `type` and `aria-label` all work without you adding them
one by one.

**5. Handle its own states.** A button should support normal, hover, disabled and
loading. A card should survive a very long title.

### The warning sign to mention
> "If a component has grown to fifteen boolean props like `isHomePage`, `isCompact`,
> `hideFooter`, that usually means it is really two different components. I would
> split it rather than keep adding flags."

---

## Design 5 — How would you structure a large Next.js project?

```
app/                    routes only
  layout.js
  page.js
  loans/
    page.js
    [id]/page.js
  api/
components/
  ui/                   generic, reusable: Button, Card, Input, Modal
  loans/                feature specific: LoanCard, FilterPanel
  layout/               Header, Footer, Sidebar
hooks/                  useDebounce, useFetch, useLocalStorage
lib/                    api client, formatters, constants
styles/
public/                 images, fonts, icons
```

The one rule worth stating:
> "I separate **generic UI components** from **feature components**. Anything in
> `components/ui` knows nothing about loans and could be copied into another project.
> Anything in `components/loans` is allowed to know about our data. That boundary
> stops the shared components from slowly filling up with business logic."

---

## Design 6 — "This page is slow. How do you fix it?"

Never jump to a solution. Show a process. (Full detail is in file 04.)

```
1. MEASURE   Lighthouse + DevTools Network and Performance tabs.
             Throttle to Slow 4G. "I do not optimise what I have not measured."

2. CATEGORISE  Which is it?
   - Too many / too large downloads   → images, bundle
   - Slow server response (TTFB)      → caching, rendering strategy
   - Heavy JavaScript blocking        → long tasks, re-renders

3. FIX THE BIGGEST ONE FIRST   Usually images, then bundle size.

4. MEASURE AGAIN   Prove the change worked.
```

Then name concrete fixes: `next/image` for format and size, code splitting per
route, removing heavy libraries, virtualising long lists, debouncing inputs, and
moving pages to SSG or ISR so the HTML is ready before JavaScript loads.

---

## Design 7 — How do you handle authentication on the frontend?

### The simple flow
```
1. User submits email + password
2. Server checks them, returns a token
3. Token is stored          ← the important decision
4. Every later request sends the token
5. Server returns 401 when it expires → send user back to login
```

### The decision to explain
> "I would keep the token in an **httpOnly cookie** rather than `localStorage`.
> `httpOnly` means JavaScript cannot read it, so if someone manages to inject a
> script into the page, they still cannot steal the session. Anything in
> `localStorage` is readable by any script running on the page. For a product
> handling student financial data, that difference matters."

### The frontend pieces
- An **axios interceptor** to attach the token to every request, in one place.
- A second interceptor to catch **401** responses and redirect to login, in one place.
- **Protected routes.** In Next.js, middleware can redirect before the page even
  renders.

- An `AuthContext` so any component can read the current user.

---

## Design 8 — A toast / notification system

A nice small design question, and it shows you understand context.

### The problem
Any component anywhere might need to say "Saved successfully". You cannot pass a
callback down to all of them.

### The design
```
ToastProvider (context, sits near the root)
 ├── holds:  toasts = [{ id, message, type }]
 ├── gives:  showToast(message, type)
 └── renders: <ToastContainer> fixed in a corner
```

```jsx
// any component, at any depth
const { showToast } = useToast();
showToast('Application submitted', 'success');
```

Edge cases to name: auto dismiss after a few seconds, allow manual close, stack
multiple toasts instead of overwriting, and clear the timer on unmount so it does
not fire after the component is gone.

---

## The three sentences that work in any design answer

Keep these ready. They fit almost every question:

1. **"Before I start, can I ask two things about the requirements?"**
2. **"Every data driven screen has four states: loading, error, empty and success.
   Empty is the one people forget."**

3. **"Since this is a search driven business, I would check whether this page needs
   to be crawlable, because that decides whether it is client rendered or server
   rendered."**

---

## ✅ Check yourself before moving on
1. Say the six step framework from memory: clarify, components, state, data, edge
   cases, performance.

2. Give the autocomplete answer out loud in about 60 seconds.
3. Explain why filters should live in the URL, giving three reasons.
4. Explain client side vs server side filtering, and when you would use each.
