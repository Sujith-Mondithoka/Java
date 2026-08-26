# 03 · Next.js 🔴🔴 (Your best chance to stand out)
**Time needed: 75 minutes**

The job description names Next.js. Their business depends on Google search. Most
candidates at this level can use React but cannot explain **why Next.js exists**.
If you can, you move to the top of the list.

---

## First, the context: how a normal React app loads

When you build a plain React app (Create React App or Vite), the server sends the
browser an almost empty file:

```html
<html>
  <body>
    <div id="root"></div>              ← completely empty
    <script src="/bundle.js"></script> ← 300 KB of JavaScript
  </body>
</html>
```

Then, in the browser:

1. Download the HTML. It has no content.
2. Download the JavaScript bundle.
3. Parse and run the JavaScript.
4. React builds the page.
5. React asks the API for data.
6. Finally the user sees the loan offers.

This is called **Client Side Rendering (CSR)**. The client (browser) does the work.

### Two problems with this
**Problem 1: the user waits.** On a mid range Android phone on 4G, steps 2 to 6 can
take several seconds. The user stares at a blank white screen.

**Problem 2: Google sees an empty page.** When Google's crawler first visits, the
HTML has no content in it. Google can run JavaScript, but it does so later, in a
second pass. That makes indexing slower and less reliable. Other crawlers, like
LinkedIn and WhatsApp link previews, are much worse at it.

**For WeMakeScholars this second problem is serious.** Students find them by
searching Google for education loans. If the pages do not rank, there are no
students.

---

## Q1. Why Next.js instead of plain React? 🔴🔴

### What Next.js changes
Next.js runs React **on the server first**. The server builds the finished HTML and
sends that to the browser.

```html
<html>
  <body>
    <h1>Education Loans for Study Abroad</h1>   ← real content, immediately
    <ul><li>SBI — 9.15%</li><li>HDFC — 9.55%</li></ul>
    <script src="/bundle.js"></script>
  </body>
</html>
```

The user sees content straight away. Google sees content straight away.

### What else you get for free
- **File based routing.** Create a file, get a URL. No router setup.
- **Automatic code splitting.** Each page loads only its own JavaScript.
- **`next/image`.** Automatic image optimisation.
- **Built in SEO metadata.** Titles and descriptions per page.
- **API routes.** Small backend endpoints inside the same project.

### Say this
> "A plain React app sends an empty HTML file and then builds the page in the
> browser. That means the user waits with a blank screen, and a crawler's first look
> at the page has no content in it. Next.js renders on the server, so the browser
> gets real HTML immediately. That helps both first paint speed and SEO. It also
> gives me file based routing, code splitting and image optimisation without extra
> setup. For a site like WeMakeScholars, where students arrive from Google, that is
> not optional, it is how the pages get found."

### If they push back: "But Google runs JavaScript now"
> "It does, but rendering happens in a second pass that is queued, so indexing is
> slower and less reliable. Other crawlers such as Bing and social preview bots are
> worse at it. Server rendered HTML removes the risk. And it still helps real users
> on slow phones, which is the bigger benefit anyway."

---

## Q2. CSR, SSR, SSG, ISR 🔴🔴 (the most valuable answer in this guide)

These are four different **times** at which the HTML can be built.

### 1. CSR — Client Side Rendering
**Built in the browser, after JavaScript loads.**
The plain React behaviour described above.
Good for: pages behind a login, where SEO does not matter. A student's dashboard.

### 2. SSR — Server Side Rendering
**Built on the server, fresh for every single request.**
A student opens the page → the server runs the code → sends finished HTML.

Good for: pages that are different for each user, or must be perfectly up to date.
Cost: the server does work on every request, so it is the slowest of the server
options and puts the most load on your infrastructure.

```js
// App Router
const res = await fetch(url, { cache: 'no-store' });   // no cache = SSR
```

### 3. SSG — Static Site Generation
**Built once, at build time.** When you run `npm run build`, Next.js creates the
HTML files. They sit on a CDN and are served instantly.

Good for: content that is the same for everyone and rarely changes. An "About us"
page, a blog post, a landing page.
Cost: to change the content you must rebuild and redeploy the whole site.

```js
const res = await fetch(url);     // cached by default = SSG
```

### 4. ISR — Incremental Static Regeneration
**The best of both.** Built like SSG, but Next.js rebuilds the page quietly in the
background every N seconds.

```js
const res = await fetch(url, { next: { revalidate: 3600 } });   // every hour
```

How it works:

- A visitor gets the stored HTML instantly, like SSG.
- If the page is older than one hour, Next.js rebuilds it in the background.
- The next visitor gets the fresh version.
- Nobody waits for the rebuild.

Good for: content that is the same for everyone but changes now and then.

### Summary table

| | When HTML is made | Speed for user | Fresh data? | Use for |
|---|---|---|---|---|
| **CSR** | In the browser | Slowest first paint | Yes | Logged in dashboards |
| **SSR** | On every request | Good | Always fresh | Personalised pages |
| **SSG** | Once, at build | Fastest | Only at build time | Blog, about page |
| **ISR** | At build + refreshed on a timer | Fastest | Fresh within N seconds | Listings, prices |

### 🔴 The follow up question: "Which would you use for their bank listing page?"

This is where you win the interview. Think out loud:

> "The list of partner banks and their interest rates is the **same for every
> visitor**, so SSR would be wasteful. The server would rebuild an identical page for
> every student who lands on it.
>
> But the rates **do change** sometimes, and rebuilding the whole site for one rate
> change is not practical.
>
> So I would use **ISR with a revalidate of about an hour**. Visitors get a static
> file served from the CDN, which is the fastest possible, and the content is never
> more than an hour old.
>
> The student's own application status page is different. That is personal to them
> and must be current, so that would be SSR or client side behind a login."

**Practise saying that out loud tonight.** It is your single strongest answer.

---

## Q3. App Router vs Pages Router 🔴

Next.js has two routing systems. Version 13 introduced the new one.

| | Pages Router (older) | App Router (newer) |
|---|---|---|
| Folder | `/pages` | `/app` |
| A page | `pages/about.js` | `app/about/page.js` |
| Get data | `getServerSideProps`, `getStaticProps` | `async` component with `await fetch` |
| Default component type | Client | **Server Component** |
| Shared layout | `_app.js` | `layout.js`, and it can be nested |
| Loading state | You build it | `loading.js` file |
| Error state | `_error.js` | `error.js` per folder |

**Be honest about which one you have used.** Then show you understand the other.
> "I have built mostly with [X]. I know the App Router is the direction Next.js is
> going, and the main differences are Server Components by default and data fetching
> directly in the component instead of `getServerSideProps`."

---

## Q4. Server Components vs Client Components 🔴🔴

This is the newest concept, and the one people find confusing. Here is the simple
version.

### The idea
In the App Router, **components run on the server by default**. Their JavaScript is
never sent to the browser at all. Only the HTML they produced is sent.

If a component needs to be interactive (a button, an input, anything with `useState`
or `onClick`), you mark it with `'use client'` at the top of the file. That
component's code is then sent to the browser.

### Example
```jsx
// app/loans/page.js  — Server Component (no 'use client')
export default async function LoansPage() {
  // You can await directly. This runs on the server.
  const res = await fetch('https://api.example.com/loans', {
    next: { revalidate: 60 }
  });
  const loans = await res.json();

  return (
    <div>
      <h1>Education Loans</h1>
      <SearchBar />              {/* interactive, so it is a client component */}
      <LoanList loans={loans} /> {/* just displays data, stays on server */}
    </div>
  );
}
```

```jsx
// components/SearchBar.jsx
'use client';                    // ← this file goes to the browser

import { useState } from 'react';

export default function SearchBar() {
  const [query, setQuery] = useState('');
  return <input value={query} onChange={e => setQuery(e.target.value)} />;
}
```

### What each can do

| Server Component | Client Component |
|---|---|
| Sends **zero JavaScript** to the browser | Adds to the JavaScript bundle |
| Can `await` data directly | Cannot `await` at the top level |
| Can read secrets and hit a database safely | Runs in the browser, so no secrets |
| ❌ No `useState`, `useEffect`, `onClick` | ✅ All hooks and events work |

### 🔴 The rule to state
> "Keep components on the server by default, and push `'use client'` down to the
> leaves, meaning the small interactive pieces. If I put `'use client'` at the top of
> the page, every component inside it also goes to the browser and I have thrown away
> the benefit."

### Environment variables (a good detail to know)
In Next.js, environment variables are **server only** by default. That is safe.
Only variables starting with `NEXT_PUBLIC_` are sent to the browser.

```
DATABASE_PASSWORD=secret        ← safe, server only
NEXT_PUBLIC_API_URL=https://... ← visible to anyone in the browser
```
Never put a secret in a `NEXT_PUBLIC_` variable. Anyone can read it in DevTools.

---

## Q5. Routing

The folder structure **is** the routing.

```
app/
  layout.js                → wraps everything (nav, footer)
  page.js                  → /
  about/page.js            → /about
  loans/page.js            → /loans
  loans/[id]/page.js       → /loans/123      (dynamic)
  blog/[...slug]/page.js   → /blog/a/b/c     (catch all)
  loading.js               → shown while the page loads
  error.js                 → shown if the page throws
  not-found.js             → the 404 page
  api/leads/route.js       → an API endpoint at /api/leads
```

### Navigation
```jsx
import Link from 'next/link';
<Link href="/loans">View loans</Link>
```

**🔴 Why `<Link>` and not `<a>`?**

- `<a href="/loans">` makes the browser throw the whole page away and download
  everything again from scratch.

- `<Link>` fetches only the new page's data and swaps it in. Much faster.
- `<Link>` also **prefetches** the page when the link scrolls into view, so the
  navigation feels instant.

- Importantly, `<Link>` still renders a real `<a>` tag underneath. So Google can
  still follow it and middle click still works.

### Programmatic navigation
```jsx
'use client';
import { useRouter } from 'next/navigation';   // App Router

const router = useRouter();
router.push('/dashboard');
```
⚠️ App Router uses `next/navigation`. Pages Router uses `next/router`. Mixing them
up is a common mistake, so mention that you know the difference.

---

## Q6. `next/image` 🔴

```jsx
import Image from 'next/image';

<Image
  src="/bank-logo.png"
  alt="SBI bank logo"
  width={400}
  height={300}
  priority        // only for the main image at the top of the page
/>
```

### What it does automatically
1. **Converts the format.** Serves WebP or AVIF to browsers that support them.
   These are much smaller than JPEG or PNG.

2. **Resizes.** Generates several sizes and serves the right one for the device.
   A phone does not download a 2000 pixel wide image.

3. **Lazy loads.** Images below the fold only download when the user scrolls near them.
4. **Reserves space.** Because you gave width and height, the browser leaves an empty
   box of the right size. The page does not jump when the image arrives. This
   directly improves your CLS score (see file 04).

`priority` turns **off** lazy loading for your main hero image, so it loads
immediately instead of waiting.

### The same idea for fonts
`next/font` downloads Google Fonts at build time and serves them from your own
server. No extra connection to Google, and no flash of invisible text.

---

## Q7. SEO in Next.js 🔴 (their highlighted requirement)

```jsx
// A fixed title, in app/layout.js or any page.js
export const metadata = {
  title: 'Education Loans for Study Abroad | WeMakeScholars',
  description: 'Compare education loan offers from 15+ banks and NBFCs. Free.',
  openGraph: { title: '...', images: ['/og-image.png'] },
  alternates: { canonical: 'https://example.com/loans' },
};
```

```jsx
// A title built from data, for a dynamic page
export async function generateMetadata({ params }) {
  const bank = await getBank(params.id);
  return {
    title: `${bank.name} Education Loan Interest Rates 2026`,
    description: `Current ${bank.name} education loan rates, eligibility and documents.`,
  };
}
```

Also worth naming:

- `app/sitemap.js` and `app/robots.js` — Next.js generates these files for you.
- **JSON-LD structured data** — extra machine readable information in a
  `<script type="application/ld+json">` tag. It can give you rich results in Google,
  like an FAQ dropdown under your link. A loan FAQ page is a perfect fit for this.

---

## Q8. What is hydration?

### The idea
The server sends finished HTML, so the user sees the page immediately. But that HTML
is static. Buttons do not work yet.

Then the JavaScript arrives and React attaches all the event handlers to the
existing HTML. That process is called **hydration**. Like adding water to something
dried.

There is a short window where the page **looks** ready but is not yet interactive.

### Hydration errors
If the HTML the server made does not match what React builds in the browser, you get
a hydration mismatch warning.

Common causes:
```jsx
<p>{new Date().toLocaleTimeString()}</p>   // server time ≠ browser time
<p>{Math.random()}</p>                     // different every time
<p>{window.innerWidth}</p>                 // window does not exist on the server
```

Fix: move it into `useEffect`, which only runs in the browser, or load the component
with `next/dynamic` and `{ ssr: false }`.

---

## Q9. API Routes

You can put small backend endpoints inside your Next.js project.

```js
// app/api/leads/route.js
export async function POST(request) {
  const body = await request.json();

  // The API key stays on the server. The browser never sees it.
  await fetch('https://crm.internal/leads', {
    method: 'POST',
    headers: { Authorization: `Bearer ${process.env.CRM_SECRET}` },
    body: JSON.stringify(body),
  });

  return Response.json({ ok: true }, { status: 201 });
}
```

Useful when you need to hide an API key, reshape a response, or handle a form
submission without building a separate backend service.

---

## Q10. Quick questions

- **`next/dynamic`?** Load a component only when needed. With `{ ssr: false }` it
  skips the server entirely, which you need for libraries that use `window`, like
  charts and maps.

- **Middleware?** Code that runs before a request is completed. Used for auth
  redirects and A/B tests.

- **Streaming?** With `loading.js` or `Suspense`, Next.js sends the page shell first
  and streams in the slow parts as they become ready. The user sees something sooner.

- **How do you check what rendering a page uses?** Run `next build`. It prints a
  symbol next to each route showing static, SSG or dynamic.

- **Deployment?** Vercel is the simplest since they build Next.js. It also runs on
  any Node server with `next build && next start`.

---

## ✅ Check yourself before moving on
1. Say the CSR / SSR / SSG / ISR table out loud, then pick one for a bank listing
   page **and give the reason**.

2. Explain Server vs Client Components, and the "push `'use client'` to the leaves"
   rule.

3. Explain hydration in three sentences.

> **If your Next.js experience is only from tutorials, say so.** Then show the
> understanding above. Interviewers forgive thin experience. They do not forgive
> bluffing that falls apart under one follow up question.
