# 03 · Next.js 🔴🔴 (Your differentiator)
**Budget: 75 minutes** · The JD names Next.js explicitly and their business runs on
Google search traffic. **This is the file that wins you the offer.**

---

## Q1 🔴🔴 Why Next.js instead of plain React? *(near-certain first question)*

**The model answer — memorise the shape of this, not the words:**

> "Plain React with Vite or CRA ships a client-side rendered app: the browser
> downloads an almost-empty HTML file plus a JS bundle, then React builds the page.
> Two problems. First, the user stares at a blank screen until the JS parses —
> painful on a mid-range Android on 4G. Second, the HTML a crawler first sees is
> essentially empty.
>
> Next.js renders the page on the server, so the browser gets real HTML
> immediately — fast First Contentful Paint and fully crawlable content. On top of
> that it gives me file-based routing, API routes, automatic code splitting,
> `next/image` optimisation, and built-in metadata for SEO. For a site like
> WeMakeScholars where students arrive from Google searching for education loans,
> server rendering isn't a nice-to-have — it's how the pages get found."

**If they push: "But Google executes JavaScript now."**
→ "It does, but rendering is queued as a second pass, so indexing is slower and
less reliable — and other crawlers (social preview bots, Bing, LinkedIn) are much
worse at it. Server-rendered HTML removes the risk entirely. It also helps real
users on slow devices, which is the bigger win."

---

## Q2 🔴🔴 CSR vs SSR vs SSG vs ISR — *the highest-value table in this folder*

| | When HTML is built | Best for | Next.js (App Router) | Pages Router |
|---|---|---|---|---|
| **CSR** | in the browser, after JS loads | dashboards, logged-in areas, anything private | `'use client'` + `useEffect` fetch | same |
| **SSR** | on the server, **on every request** | personalised or always-fresh pages | `fetch(url, { cache: 'no-store' })` | `getServerSideProps` |
| **SSG** | at **build time**, once | blog, marketing pages, static content | default `fetch` (cached) | `getStaticProps` |
| **ISR** | at build, then **regenerated in the background every N seconds** | content that changes occasionally — *bank interest rates, loan listings* | `fetch(url, { next: { revalidate: 60 } })` | `getStaticProps` + `revalidate` |

**How to pick — say it as a decision rule:**
- Content same for everyone and rarely changes → **SSG** (fastest possible, served from CDN).
- Same for everyone but updates periodically → **ISR** (SSG speed + freshness, no rebuild).
- Different per request / needs cookies or auth → **SSR**.
- Behind a login and SEO-irrelevant → **CSR** is fine.

🔴 **The follow-up that separates candidates: "Which would you use for
WeMakeScholars' bank listing pages?"**
> "ISR. The list of partner banks and their rates is the same for every visitor, so
> per-request SSR wastes server work — but it does change, and a full rebuild for
> one rate change is impractical. `revalidate: 3600` gives me static-file speed and
> CDN caching, with content never more than an hour stale. A student's own
> application status page, on the other hand, is per-user, so that's SSR or CSR
> behind auth."

*If you say only that in the entire interview, you've made the shortlist.*

---

## Q3 🔴 App Router vs Pages Router

| | Pages Router (`/pages`) | App Router (`/app`, v13+) |
|---|---|---|
| Routing file | `pages/about.js` | `app/about/page.js` |
| Data fetching | `getServerSideProps` / `getStaticProps` | `async` Server Component with `await fetch` |
| Default component | client | **Server Component** |
| Layouts | `_app.js`, manual | nested `layout.js`, preserved across navigation |
| Loading UI | manual | `loading.js` (auto Suspense boundary) |
| Errors | `_error.js` | `error.js` per segment |
| Special files | — | `page`, `layout`, `loading`, `error`, `not-found`, `route` |

"App Router is where Next is going and what new projects should use, but plenty of
production apps are still on Pages Router — I'm comfortable reading and writing
both. **Be honest about which one you've actually built in** — say that, then show
you understand the other."

---

## Q4 🔴🔴 Server Components vs Client Components

```jsx
// app/loans/page.js — Server Component by default
export default async function LoansPage() {
  const res = await fetch('https://api.example.com/loans', { next: { revalidate: 60 } });
  const loans = await res.json();
  return <LoanList loans={loans} />;
}

// components/SearchBar.jsx
'use client';                       // opts into the browser bundle
import { useState } from 'react';
export default function SearchBar() {
  const [q, setQ] = useState('');
  return <input value={q} onChange={e => setQ(e.target.value)} />;
}
```

| Server Component | Client Component |
|---|---|
| Runs on the server only | Runs on server (for HTML) **and** browser |
| **Ships zero JS to the browser** | Adds to the bundle |
| Can `await` directly, hit a DB, read secrets | Can use hooks, events, browser APIs |
| ❌ no `useState`/`useEffect`/`onClick` | ✅ all of it |

**The rule to state:** "Keep components on the server by default and push
`'use client'` down to the **leaves** — the interactive bits. If I put `'use client'`
at the top of the page, everything under it goes to the browser and I've thrown
away the benefit. A common pattern is a Server Component page that fetches data
and renders a small client `<SearchBar>` inside it."

⚠️ Environment variables: server-only by default. Only `NEXT_PUBLIC_*` reaches the
browser — and anything with that prefix is **public**, never put a secret in one.
Great question to nail if asked.

---

## Q5 🔴 Routing essentials
```
app/
  layout.js              → root layout (html/body, shared nav)
  page.js                → /
  about/page.js          → /about
  loans/[id]/page.js     → /loans/123      (dynamic segment)
  blog/[...slug]/page.js → /blog/a/b/c     (catch-all)
  (marketing)/page.js    → route group — folder doesn't appear in the URL
  loading.js  error.js  not-found.js
  api/loans/route.js     → API endpoint (GET/POST exports)
```
```jsx
// Navigation — client-side, no full page reload, prefetched in the viewport
import Link from 'next/link';
<Link href="/loans">Loans</Link>

// Programmatic
'use client';
import { useRouter, useParams, useSearchParams } from 'next/navigation';
const router = useRouter();
router.push('/dashboard');
```
🔴 **`<Link>` vs `<a>`:** "`<a>` triggers a full page reload — the whole app
re-downloads and re-hydrates. `<Link>` does a client-side transition, only fetching
the new route's payload, and prefetches links as they enter the viewport. But
`<Link>` renders a real `<a>` underneath, so crawlers and middle-click still work."

⚠️ App Router imports from `next/navigation`; Pages Router uses `next/router`.
Mixing them up is a classic slip — mention you know the difference.

---

## Q6 🔴 `next/image` — *guaranteed if they care about performance*
```jsx
import Image from 'next/image';
<Image src="/bank.png" alt="Partner bank" width={400} height={300}
       priority /* only for above-the-fold / LCP image */ />
```
What it does for free: serves **WebP/AVIF** to browsers that support them,
generates responsive `srcset` sizes, **lazy-loads** below-the-fold images, and
**reserves the space** using width/height so the layout doesn't jump — that last
one is your CLS score. `priority` disables lazy-loading for the hero image so LCP
doesn't regress.

Same story for `next/font`: self-hosts the font at build time, so no round trip to
Google Fonts and no flash of invisible text.

---

## Q7 🔴 SEO in Next.js — *their highlighted requirement*
```jsx
// Static metadata — app/layout.js or any page.js
export const metadata = {
  title: 'Education Loans for Study Abroad | WeMakeScholars',
  description: 'Compare education loan offers from 15+ banks and NBFCs. Free.',
  openGraph: { title: '…', images: ['/og.png'] },
  alternates: { canonical: 'https://example.com/loans' },
};

// Dynamic, per-route
export async function generateMetadata({ params }) {
  const bank = await getBank(params.id);
  return { title: `${bank.name} Education Loan Interest Rates` };
}
```
Also mention, briefly: `sitemap.js` and `robots.js` file conventions, JSON-LD
structured data injected via a `<script type="application/ld+json">` for rich
results, and semantic headings — **one `<h1>` per page**.

---

## Q8 What is hydration? What's a hydration error?
"The server sends HTML so the user sees content immediately, then React attaches
event listeners to that existing markup in the browser — that's hydration. Until
it finishes, the page looks ready but isn't interactive.

A **hydration mismatch** happens when the server HTML and the first client render
differ — `new Date()`, `Math.random()`, `window`/`localStorage`, or
browser-extension-injected markup. Fix: render that bit inside `useEffect` after
mount, or use `next/dynamic` with `{ ssr: false }`."

---

## Q9 API routes / Route Handlers
```js
// app/api/leads/route.js
export async function POST(request) {
  const body = await request.json();
  // validate, call the real backend, keep API keys server-side
  return Response.json({ ok: true }, { status: 201 });
}
```
"Useful as a thin backend-for-frontend: hide an API key that must never reach the
browser, reshape a backend response, or handle a form POST — without standing up a
separate service."

---

## Q10 Quick-fire
- **`next/dynamic`?** Lazy-load a component; `{ ssr: false }` for browser-only libs (charts, maps).
- **Middleware?** Runs before a request completes — auth redirects, geo, A/B tests.
- **`revalidatePath` / `revalidateTag`?** On-demand ISR invalidation after a content update.
- **Streaming?** With `loading.js`/`Suspense`, HTML streams in chunks so the shell paints while slow data resolves.
- **`next build` output?** Prints per-route whether it's Static ○, SSG ●, or Dynamic ƒ — useful for verifying your rendering strategy.
- **Deploy?** Vercel is first-class; also `next build && next start` on any Node host, or `output: 'export'` for a fully static site.

---

### ✅ Self-check
1. Recite the CSR/SSR/SSG/ISR table and pick one for a bank-listing page **with a reason**.
2. Explain Server vs Client Components and the "push `'use client'` to the leaves" rule.
3. Explain hydration in three sentences.

> **If your Next.js experience is limited to a tutorial, say so honestly and then
> demonstrate the understanding above.** "I've built with it at a project level
> rather than in production, but here's how I reason about rendering strategies…"
> Recruiters forgive thin experience. Nobody forgives bluffing that unravels.
