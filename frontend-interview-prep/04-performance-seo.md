# 04 · Performance & SEO 🔴
**Budget: 60 minutes** · *"Making Things Fast"* was **highlighted in their own JD**.
Whoever wrote it cares. Treat this as a named requirement, not general knowledge.

---

## Why this is a business requirement here, not a technical one

Say this once, early: *"WeMakeScholars acquires students through organic search.
A slow page loses rankings and loses the student before the form even loads — most
of them are on mid-range Android phones on 4G. So performance work here is
directly lead generation, not polish."* This reframes you from coder to engineer.

---

## Q1 🔴🔴 Core Web Vitals — know all three, with numbers

| Metric | Measures | Good | Caused by | Fix |
|---|---|---|---|---|
| **LCP** — Largest Contentful Paint | when the main content appears | **< 2.5 s** | huge hero images, slow server, render-blocking CSS/JS | optimise & preload the hero image (`priority`), SSR/SSG, CDN, compress |
| **CLS** — Cumulative Layout Shift | visual stability / jumping | **< 0.1** | images without dimensions, injected banners, late-loading fonts | always set width/height or `aspect-ratio`, reserve ad/banner space, `font-display: swap` |
| **INP** — Interaction to Next Paint | responsiveness to clicks/taps *(replaced FID in 2024)* | **< 200 ms** | long JS tasks blocking the main thread | break up long tasks, debounce, memoize, ship less JS |

Supporting: **TTFB** (server response, < 800 ms), **FCP** (first pixel of content).

**If you remember one line:** "LCP is *is it there*, CLS is *does it stay still*,
INP is *does it respond*."

---

## Q2 🔴 "The page is slow. How do you diagnose it?" — give a *process*

Never jump straight to fixes. Interviewers score the method:

1. **Measure first.** Lighthouse for a lab score, Chrome DevTools Performance +
   Network panels, and real-user data from `web-vitals` / Search Console if
   available. "I don't optimise what I haven't measured."
2. **Find the category.** Network (too much / too big / too slow)? Rendering
   (blocking resources)? JavaScript (long tasks)? Backend (high TTFB)?
3. **Fix the biggest item first** — usually images or bundle size.
4. **Re-measure** to prove the change worked, throttled to Slow 4G / 4× CPU.

---

## Q3 🔴 Your optimisation toolbox (grouped — recite by group, not randomly)

**Images** *(usually the single biggest win)*
- Modern formats — WebP/AVIF; `next/image` does this automatically.
- Correct dimensions + `srcset` — don't ship a 2000 px image into a 400 px slot.
- `loading="lazy"` below the fold; `priority`/`preload` for the LCP image.
- Always set width & height → kills CLS.

**JavaScript / bundle**
- **Code splitting** — `React.lazy` + `Suspense`, or `next/dynamic`, per route.
- **Tree shaking** — import what you use: `import { debounce } from 'lodash-es'`, not the whole library.
- Audit dependencies — moment.js → date-fns; do you need that carousel library?
- Defer third-party scripts (`next/script` with `strategy="lazyOnload"`) — analytics and chat widgets are frequently the worst offenders.

**Rendering**
- SSR/SSG so content paints before JS (see file 03).
- `React.memo` / `useMemo` / `useCallback` on measured hot paths.
- **Virtualise long lists** — `react-window` renders only visible rows; a 5,000-row table becomes 20 DOM nodes.
- Debounce search inputs, throttle scroll handlers.

**Network / delivery**
- CDN + HTTP caching headers; gzip/Brotli compression.
- `preconnect` / `dns-prefetch` for critical third-party origins.
- Self-host fonts (`next/font`), subset them, `font-display: swap`.
- Avoid waterfalls — `Promise.all` parallel fetches instead of sequential awaits.

---

## Q4 🔴 Technical SEO checklist for a React/Next app

- **Server-render content that must rank.** CSR content is indexed slowly and unreliably.
- **Unique `<title>` and meta description per page** — `generateMetadata` in Next.
- **Semantic HTML:** one `<h1>`, ordered `<h2>/<h3>`, `<nav>`, `<main>`, `<article>`. Crawlers and screen readers both use structure.
- **`alt` text on every meaningful image** — accessibility *and* image search.
- **Canonical URLs** to prevent duplicate-content splits.
- **`sitemap.xml` + `robots.txt`** — Next has file conventions for both.
- **Structured data (JSON-LD)** — FAQ / Article / Organization schema for rich results. *A loan-comparison FAQ page is a textbook FAQ-schema use case — a great thing to volunteer.*
- **Open Graph / Twitter cards** for share previews.
- **Mobile-first & fast** — Google indexes the mobile version, and Core Web Vitals are a ranking signal.
- **Real `<a href>` links** for internal linking so crawlers can follow them. A `<div onClick={router.push}>` is invisible to a crawler — `<Link>` renders a proper anchor.

---

## Q5 Accessibility (a11y) — the quick version
Worth a minute, and it overlaps with SEO:
- Semantic elements over `<div onClick>` — a real `<button>` is keyboard-focusable and announced correctly for free.
- Labels tied to inputs (`htmlFor` / `id`).
- Visible focus states; everything reachable by keyboard.
- Colour contrast ≥ 4.5:1 for body text.
- `aria-label` only when there's no visible text (icon buttons); ARIA is a patch, not a substitute for semantics.
- Test: tab through the page; run the Lighthouse a11y audit.

---

## Q6 Caching, briefly
- **Browser cache** via `Cache-Control` — hashed asset filenames let you cache JS/CSS for a year and bust on deploy.
- **CDN cache** — static pages served from an edge near the user.
- **Data cache** — Next's `fetch` cache / ISR `revalidate`; React Query / SWR on the client.
- **Memoization** — cache within a single render tree.

---

## Q7 Likely rapid-fire
- **Reduce initial bundle?** Code split by route, lazy-load below-the-fold components, tree-shake, drop heavy deps, analyse with `@next/bundle-analyzer`.
- **Lazy loading?** Defer loading a resource until it's needed/near the viewport.
- **CDN?** Geographically distributed servers caching static assets close to the user — lower latency, less origin load.
- **Critical rendering path?** HTML → DOM, CSS → CSSOM → Render Tree → Layout → Paint. CSS is render-blocking; `<script>` in `<head>` without `defer` is parser-blocking.
- **`defer` vs `async`?** Both download in parallel. `async` executes the moment it lands (order not guaranteed); `defer` executes after HTML parsing, in order. Use `defer` for anything that touches the DOM.
- **Reflow vs repaint?** Reflow = geometry recalculated (expensive); repaint = pixels redrawn (cheaper). Animate `transform`/`opacity`, which skip both and run on the compositor — never animate `width`/`top`.
- **How would you measure improvement?** Lighthouse before/after + real-user CWV, on a throttled mobile profile.

---

### ✅ Self-check
1. Name LCP, CLS, INP with their thresholds and one fix each.
2. Give the four-step diagnosis process for "the page is slow".
3. Explain why CSR is a risk for SEO in one sentence.
