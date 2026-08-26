# 04 · Performance and SEO 🔴
**Time needed: 60 minutes**

In their job description, the line **"Making Things Fast"** was highlighted in their
own document. That means the person who wrote it cares about it. Treat this as a
named requirement, not general knowledge.

---

## First, the context: why speed is a business problem here

WeMakeScholars gets students from Google search. So two things follow.

**1. Speed affects ranking.** Google uses page speed as a ranking signal. A slow
page appears lower in results, so fewer students find it.

**2. Speed affects conversion.** Most students are on mid range Android phones on
4G. If the page takes 5 seconds, many leave before it loads. The loan form never
gets filled.

So on this product, performance work is **lead generation**, not polish. Say that
once in the interview. It reframes you from someone who writes code to someone who
understands why the code matters.

---

## Q1. Core Web Vitals 🔴🔴

Google measures three things. Learn all three with their numbers.

### LCP — Largest Contentful Paint
**"When does the main content appear?"**
It measures the time until the biggest thing on screen is visible. Usually the hero
image or the main heading.

**Good: under 2.5 seconds.**

Common causes of a bad score:

- A huge unoptimised hero image
- Slow server response
- CSS or JavaScript blocking the page from rendering

Fixes: optimise and preload the hero image, use SSR or SSG so HTML arrives ready,
use a CDN, compress files.

### CLS — Cumulative Layout Shift
**"Does the page jump around while loading?"**

You have felt this. You go to tap a button, an image finishes loading above it,
everything shifts down, and you tap the wrong thing.

**Good: under 0.1.**

Common causes:

- Images without width and height, so no space is reserved
- Banners or ads inserted at the top after load
- A custom font loading late and changing the text size

Fixes: always set width and height on images (or use `next/image`), reserve space
for anything that loads late, use `font-display: swap`.

### INP — Interaction to Next Paint
**"When I tap something, how fast does the page respond?"**
This replaced FID in 2024.

**Good: under 200 milliseconds.**

Cause: JavaScript is busy doing something long, so the browser cannot respond to the
tap. Remember from file 01 that JavaScript is single threaded.

Fixes: break long tasks into smaller ones, debounce expensive handlers, reduce
unnecessary re-renders, ship less JavaScript.

### The one line summary
**LCP = is it there. CLS = does it stay still. INP = does it respond.**

Two more terms you may hear: **TTFB** (Time to First Byte, how fast your server
replies, good is under 800ms) and **FCP** (First Contentful Paint, the first pixel
of any content).

---

## Q2. "The page is slow. How do you find out why?" 🔴

Never answer with a list of fixes. They are testing your **process**.

### Step 1: Measure
- **Lighthouse** in Chrome DevTools for a score and a list of problems.
- **Network tab** to see what is being downloaded and how big it is.
- **Performance tab** to record and find long JavaScript tasks.
- Throttle to **Slow 4G** and 4x CPU slowdown, so you see what a real phone sees.

Say the line: *"I do not optimise what I have not measured."*

### Step 2: Decide which category the problem is in
| Category | Symptom in DevTools |
|---|---|
| Network | Very large files, or too many requests |
| Server | Long wait before the first byte arrives (TTFB) |
| Rendering | CSS or JS blocking, blank screen for a long time |
| JavaScript | Long tasks in the Performance tab, page feels frozen |

### Step 3: Fix the biggest item first
Usually images, then bundle size. Do not start with micro optimisations.

### Step 4: Measure again
Prove the change worked. Compare the before and after Lighthouse numbers.

---

## Q3. The optimisation toolbox

Learn these in **groups**. Reciting a random list sounds memorised. Grouping sounds
like understanding.

### Group 1: Images (usually the biggest win)
- **Modern formats.** WebP and AVIF are much smaller than JPEG. `next/image` does
  this automatically.

- **Right size.** Do not send a 2000 pixel image into a 400 pixel space.
- **Lazy load** anything below the fold, so it only downloads when scrolled to.
- **Set width and height** so the layout does not jump. This fixes CLS.

### Group 2: JavaScript
- **Code splitting.** Split by route with `next/dynamic` or `React.lazy`, so the
  user only downloads the page they are on.

- **Tree shaking.** Import only what you use. `import _ from 'lodash'` pulls in the
  whole library. `import debounce from 'lodash/debounce'` pulls in one function.

- **Check your dependencies.** Is that date library 70 KB when you only format one
  date? `date-fns` is smaller than `moment`.

- **Delay third party scripts.** Analytics and chat widgets are often the slowest
  things on a page. Load them last with `next/script` and `strategy="lazyOnload"`.

### Group 3: Rendering
- Use **SSG or ISR** so the HTML is ready before JavaScript loads.
- Reduce re-renders with `React.memo` and `useMemo`, but only where you measured a
  problem.

- **Virtualise long lists.** With `react-window`, a 5,000 row table only puts about
  20 rows in the DOM at a time. The rest are not rendered until you scroll.

- **Debounce** search inputs and **throttle** scroll handlers.

### Group 4: Network and delivery
- Use a **CDN** so files are served from a server near the user.
- Enable **gzip or Brotli** compression.
- **Self host fonts** with `next/font` so there is no extra connection.
- **Avoid waterfalls.** Two API calls that do not depend on each other should run
  with `Promise.all`, not one after the other.

---

## Q4. Technical SEO for a React or Next app 🔴

### The core issue
If content only appears after JavaScript runs, crawlers may not see it reliably. So
anything that must rank should be **server rendered**.

### The checklist
- **Unique title and meta description on every page.** Use `generateMetadata` in Next.
- **Semantic HTML.** One `<h1>` per page, then `<h2>` and `<h3>` in order. Use
  `<nav>`, `<main>`, `<article>`. Crawlers use this structure to understand the page.

- **`alt` text on every meaningful image.** Helps accessibility and image search.
- **Canonical URL** so Google knows which version of a page is the real one, when
  the same content is reachable from two URLs.

- **`sitemap.xml` and `robots.txt`.** Next.js can generate both from files.
- **Structured data (JSON-LD).** Machine readable information about the page. An FAQ
  page can get an expandable FAQ shown directly in Google results. A loan FAQ is a
  perfect example, and worth volunteering in the interview.

- **Open Graph tags** so shared links show a proper preview card.
- **Real `<a>` links for internal navigation.** A `<div onClick={router.push}>` is
  invisible to a crawler. `<Link>` renders a real anchor, so it is fine.

- **Mobile first and fast.** Google indexes the mobile version of your site.

---

## Q5. Accessibility, briefly

Worth a minute. It overlaps with SEO because both rely on good structure.

- Use real elements. A `<button>` is focusable, works with the Enter key, and is
  announced correctly by screen readers. A `<div onClick>` does none of that.

- Connect labels to inputs with `htmlFor` and `id`.
- Keep visible focus outlines. Do not remove them with `outline: none`.
- Text contrast of at least 4.5 to 1.
- Use `aria-label` only when there is no visible text, such as an icon only button.
  ARIA is a patch. Correct HTML is better.

- Quick test: press Tab through the page. Can you reach and use everything?

---

## Q6. Caching, in simple terms

| Type | Where | Example |
|---|---|---|
| Browser cache | User's device | JS and CSS files, cached for a year |
| CDN cache | Edge servers worldwide | Static pages served near the user |
| Data cache | Your app | Next.js `revalidate`, React Query |
| Memoization | Inside React | `useMemo`, `React.memo` |

Useful detail: build tools add a hash to filenames like `main.a3f9c2.js`. So you can
cache that file forever. When the code changes, the filename changes, and the
browser downloads the new one automatically.

---

## Q7. Quick questions

- **How do you reduce the initial bundle size?** Split code by route, lazy load
  below the fold components, remove heavy libraries, and check with
  `@next/bundle-analyzer`.

- **What is lazy loading?** Delaying the download of something until it is actually
  needed.

- **What is a CDN?** Servers spread around the world that hold copies of your files,
  so users download from a nearby one instead of a distant origin server.

- **`defer` vs `async` on a script tag?** Both download in the background. `async`
  runs as soon as it arrives, in no guaranteed order. `defer` runs after the HTML is
  parsed, in order. Use `defer` for anything that touches the page.

- **Reflow vs repaint?** Reflow means the browser recalculates positions and sizes,
  which is expensive. Repaint means it redraws colours, which is cheaper. This is
  why you animate `transform` and `opacity` and never `width` or `top`. Those two
  skip layout entirely and run on the GPU.

---

## ✅ Check yourself before moving on
1. Name LCP, CLS and INP with their target numbers and one fix each.
2. Give the four step process for "the page is slow".
3. Explain in one sentence why client side rendering is a risk for SEO.
