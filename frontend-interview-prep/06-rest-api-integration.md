# 06 · Connecting to REST APIs 🟠
**Time needed: 30 minutes**

The job description says: *"Working closely with our backend team to plug REST APIs
and data into the frontend smoothly."* Expect this in the coding round.

---

## First, the context: what an API call actually is

Your React app has no data of its own. The data lives on a server. An API is the
agreed way to ask for it.

```
   Browser                          Server
      |                                |
      |  GET /api/loans?bank=SBI       |
      | -----------------------------> |
      |                                |  looks in the database
      |  200 OK  [ {...}, {...} ]      |
      | <----------------------------- |
      |                                |
   render the list
```

**REST** is just a set of conventions for how those requests should look. Use nouns
for the address (`/loans`), and a verb to say what you want to do.

---

## Q1. The HTTP basics they may check

| Verb | Meaning |
|---|---|
| `GET` | Read data. Should never change anything. |
| `POST` | Create something new. |
| `PUT` | Replace an entire item. |
| `PATCH` | Update part of an item. |
| `DELETE` | Remove an item. |

### Status codes
| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 400 | Bad request. You sent something wrong. |
| **401** | **Not logged in.** "Who are you?" |
| **403** | **Logged in, but not allowed.** "I know who you are, and no." |
| 404 | Not found |
| 429 | Too many requests, you are rate limited |
| 500 | Server error. Not your fault. |

🔴 The 401 vs 403 difference is a common quick question. Learn the two sentences.

---

## Q2. `fetch` vs `axios`

| | `fetch` | `axios` |
|---|---|---|
| Setup | Built into the browser | A library, about 13 KB |
| Error on 404 or 500 | **No. You must check yourself.** | Yes, it throws automatically |
| JSON | You call `res.json()` | Automatic both ways |
| Timeout | Not built in | Built in option |
| Interceptors | No | Yes |

**What is an interceptor?** A function that runs on every request or every response.
It lets you write something once instead of in fifty places.

```js
// attach the token to every request, in one place
axios.interceptors.request.use(config => {
  config.headers.Authorization = `Bearer ${getToken()}`;
  return config;
});

// handle every expired session, in one place
axios.interceptors.response.use(
  res => res,
  err => {
    if (err.response?.status === 401) redirectToLogin();
    return Promise.reject(err);
  }
);
```

> "For a small project `fetch` is enough. On a bigger codebase I prefer axios for the
> interceptors, so the auth header and the 401 handling live in one place instead of
> being repeated in every call."

---

## Q3. The four states 🔴🔴

This is the most important idea in this file.

**Every screen that loads data has four possible states:**

1. **Loading** — the request is in flight. Show a spinner or a skeleton.
2. **Error** — something failed. Show a message and a retry button.
3. **Empty** — it worked, but there is nothing to show. Show "No loans match your
   filters."

4. **Success** — show the data.

**Most candidates only handle loading and success.** Saying all four out loud is a
genuine hiring signal, because empty and error are what users actually hit.

### The full pattern
```jsx
function LoanList() {
  const [loans, setLoans]     = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError]     = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    async function load() {
      try {
        setLoading(true);
        setError(null);

        const res = await fetch('/api/loans', { signal: controller.signal });

        // fetch does NOT throw on 404 or 500, so check it yourself
        if (!res.ok) throw new Error(`Request failed: ${res.status}`);

        setLoans(await res.json());
      } catch (err) {
        // ignore the error we caused ourselves by cancelling
        if (err.name !== 'AbortError') setError(err.message);
      } finally {
        setLoading(false);           // always runs, success or failure
      }
    }

    load();

    return () => controller.abort();  // cleanup: cancel if we unmount
  }, []);

  if (loading)       return <Spinner />;
  if (error)         return <ErrorState message={error} onRetry={load} />;
  if (!loans.length) return <p>No loans match your filters.</p>;

  return <ul>{loans.map(l => <LoanCard key={l.id} loan={l} />)}</ul>;
}
```

### Point out these three things without being asked
1. **`res.ok`** because `fetch` does not throw on a bad status.
2. **`AbortController` in the cleanup** for two reasons, explained next.
3. **`finally`** so loading always stops, even when the request fails.

---

## Q4. Race conditions, and why `AbortController` matters 🔴

### The problem, with a real example
The user types in a search box.

```
t=0ms    types "ax"    → request A starts
t=200ms  types "axis"  → request B starts
t=600ms  request B finishes → screen shows results for "axis"  ✅
t=900ms  request A finishes → screen shows results for "ax"    ❌ WRONG
```

The older, slower request finished last and overwrote the correct results. The
search box now shows results that do not match what is typed.

### The fixes
1. **Cancel the old request** with `AbortController`. This is the standard fix.
2. **Debounce** so fewer requests are made in the first place.
3. Use **React Query**, which handles this for you.

`AbortController` in the cleanup solves two problems at once: it prevents this race
condition, and it stops React warning that you updated state on a component that no
longer exists.

---

## Q5. CORS — you will be asked at least what it is

### What it is
CORS is a **browser** security rule. A page loaded from `site-a.com` is not allowed
to read a response from `site-b.com`, unless `site-b.com` explicitly permits it with
a response header:

```
Access-Control-Allow-Origin: https://site-a.com
```

### The two things to say
1. **It is enforced by the browser, not the server.** This is why the exact same
   request works fine in Postman but fails in the browser.

2. **It is fixed on the backend, not the frontend.** The server must send the
   header. A dev proxy is a local workaround, not a real fix.

For requests that are not simple, the browser first sends an `OPTIONS` request to
ask permission. That is called a **preflight**.

---

## Q6. React Query and SWR — worth mentioning

> "A lot of what people call global state is really just a cached copy of server
> data. React Query handles that properly: caching, background refetching,
> deduplicating identical requests, retries, and loading and error flags. It replaces
> most of the `useEffect` plus `useState` code above, including the race condition
> handling."

```js
const { data, isLoading, error } = useQuery({
  queryKey: ['loans'],
  queryFn: getLoans,
});
```

---

## Q7. Authentication on the frontend

- Store the token in an **httpOnly cookie** rather than `localStorage`. `httpOnly`
  means JavaScript cannot read it, so an injected script cannot steal it.

- Attach it with an interceptor so it is written once.
- Handle **401** in one place: clear the session and send the user to login.
- **Never put secrets in frontend code.** In Next.js, anything named
  `NEXT_PUBLIC_*` is visible in the browser. If you need to use a secret key, call it
  from an API route on the server instead.

---

## Q8. "How do you work with the backend team?" — the job description's real question

Answer as a teammate, not just a coder:

> "I ask for the contract early: the endpoint, the request shape, the response shape
> and the error shape. Agreeing on that before either side builds saves a lot of
> rework.
>
> If the API is not ready, I mock the response so I am not blocked, and swap the URL
> in later.
>
> I check pagination and the error format up front, because those are usually what
> break during integration.
>
> And if a response shape does not fit the UI well, I would rather raise it than
> quietly write conversion code in five different components."

---

## ✅ Check yourself before moving on
1. Name the four states, in order.
2. Explain the race condition example, and how `AbortController` fixes it.
3. Explain CORS in two sentences, including whose job it is to fix.
4. What does `fetch` do on a 404?
