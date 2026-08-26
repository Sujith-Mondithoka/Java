# 06 · REST API Integration 🟠
**Budget: 30 minutes** · The JD: *"Working closely with our backend team to plug
REST APIs and data into the frontend smoothly."* Expect this in the coding round —
fetch, loading, error, empty.

---

## Q1 REST basics they may check
| Verb | Use | Idempotent? |
|---|---|---|
| GET | read | yes |
| POST | create | no |
| PUT | replace whole resource | yes |
| PATCH | partial update | no (usually) |
| DELETE | remove | yes |

**Status codes:** 200 OK · 201 Created · 204 No Content · **400** bad request ·
**401** not authenticated · **403** authenticated but not allowed · **404** not
found · **429** rate limited · **500** server error.
🔴 401 vs 403 is a common gotcha — *"401 is 'who are you?', 403 is 'I know who you
are and you still can't.'"*

---

## Q2 🔴 fetch vs axios
| fetch | axios |
|---|---|
| built in, no dependency | ~13 KB library |
| **doesn't reject on 4xx/5xx** — check `res.ok` | rejects on error status automatically |
| manual `JSON.stringify` + `.json()` | auto JSON both ways |
| no built-in timeout (use `AbortSignal.timeout`) | `timeout` option |
| no interceptors | interceptors — attach auth token / handle 401 globally |

"For a small app, `fetch` is enough. On a bigger codebase I like axios interceptors:
one place to attach the auth header and one place to catch a 401 and redirect to
login, instead of repeating it in every call."

---

## Q3 🔴🔴 The four states — *say all four, most candidates say two*

**"Every data-driven UI has four states: loading, error, empty, and success. Empty
is the one people forget — 'no loans match your filters' should be a designed
state, not a blank screen."** That sentence is a hiring signal.

```jsx
function LoanList() {
  const [loans, setLoans]     = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError]     = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    (async () => {
      try {
        setLoading(true);
        setError(null);
        const res = await fetch('/api/loans', { signal: controller.signal });
        if (!res.ok) throw new Error(`Request failed: ${res.status}`);
        setLoans(await res.json());
      } catch (err) {
        if (err.name !== 'AbortError') setError(err.message);
      } finally {
        setLoading(false);
      }
    })();

    return () => controller.abort();       // 🔴 cleanup: cancel on unmount
  }, []);

  if (loading)          return <Spinner />;
  if (error)            return <ErrorState message={error} onRetry={refetch} />;
  if (!loans.length)    return <p>No loans match your filters.</p>;
  return <ul>{loans.map(l => <LoanCard key={l.id} loan={l} />)}</ul>;
}
```

**Point out three things in this snippet unprompted:**
1. `res.ok` — because `fetch` doesn't throw on 404/500.
2. `AbortController` in the cleanup — prevents the state update on an unmounted
   component and stops a **race condition** where a slow earlier request resolves
   after a fast later one and overwrites fresh data with stale.
3. `finally` — loading always ends, even on failure.

---

## Q4 🔴 Race conditions in search-as-you-type
"If the user types 'ax' then 'axis', two requests are in flight. If 'ax' resolves
last, the UI shows the wrong results. Three fixes: abort the previous request with
`AbortController` (my default), debounce so fewer requests are made at all, or tag
each request and ignore stale responses. React Query handles this for me."

---

## Q5 Auth on the frontend
- Token in an **httpOnly cookie** > `localStorage` (XSS-proof). Cookies need
  `credentials: 'include'` cross-origin.
- Attach `Authorization: Bearer <token>` via an axios interceptor.
- On **401** → clear session and redirect to login, in one interceptor.
- Refresh-token flow: on 401, try refresh once, retry the original request, else log out.
- **Never put secrets in frontend code.** In Next, anything `NEXT_PUBLIC_*` is
  visible in the browser bundle — proxy through a Route Handler instead.

---

## Q6 CORS — you will be asked at least the definition
"CORS is a **browser** security rule: a page on origin A can't read a response from
origin B unless B sends `Access-Control-Allow-Origin`. It's enforced by the browser,
not the server, which is why the same request works in Postman. **It's fixed on the
backend, not the frontend** — a dev proxy is a local workaround, not a fix. For
non-simple requests the browser first sends an OPTIONS preflight."

---

## Q7 React Query / SWR — worth mentioning
"Most 'global state' is really cached server state. React Query gives caching,
background refetching, deduped requests, retries, pagination, and
loading/error/stale flags in a few lines — replacing a lot of `useEffect` +
`useState` boilerplate and the race-condition handling above."

```js
const { data, isLoading, error } = useQuery({ queryKey: ['loans'], queryFn: getLoans });
```

---

## Q8 Working with the backend team — *the JD's actual ask*
Answer as a collaborator, not just a coder:
"I ask for the contract early — endpoint, request shape, response shape, error
shape — and agree on it before either side builds. If the API isn't ready, I mock
the response so I'm not blocked and swap the URL later. I check pagination and
error formats up front, because those are what break in integration. And when a
response shape doesn't fit the UI, I'd rather raise it than quietly write
transformation code in five components."

---

### ✅ Self-check
1. Recite the four UI states.
2. Explain why `AbortController` is in the cleanup — the two reasons.
3. Explain CORS in two sentences, including whose job it is to fix.
