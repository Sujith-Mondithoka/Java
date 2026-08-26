# 05 · HTML, CSS & Responsive Design 🟠
**Budget: 30 min tonight, skim tomorrow** · "Translating UI/UX wireframes into
clean, performant, responsive code" is the JD's opening line — this comes up in the
coding round more than in questioning.

---

## Q1 🔴 Semantic HTML — why bother?
`<header> <nav> <main> <section> <article> <aside> <footer> <figure> <button>`

"Semantic tags describe *meaning*, not appearance. Three payoffs: screen readers
can navigate by landmark, search engines understand page structure, and the markup
is readable to the next developer. A `<div onClick>` is invisible to a keyboard
user and to a crawler — a `<button>` is focusable, activates on Enter/Space, and is
announced as a button, all for free."

---

## Q2 🔴 The box model
`content → padding → border → margin`

```css
* { box-sizing: border-box; }   /* width now includes padding + border */
```
"With the default `content-box`, adding padding makes the element wider than the
width you set, which breaks grid layouts. `border-box` makes width mean what you
expect. It's the first line of nearly every reset."

---

## Q3 🔴 Flexbox vs Grid — *when do you use which?*
- **Flexbox = one dimension** (a row **or** a column). Navbars, button groups, centring, card internals, space distribution.
- **Grid = two dimensions** (rows **and** columns at once). Page layouts, card galleries, dashboards.
- "They compose — a Grid page layout with Flexbox inside each card is the normal setup."

```css
.nav   { display: flex; justify-content: space-between; align-items: center; gap: 1rem; }
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; }
.center{ display: grid; place-items: center; }   /* centring, done */
```
🔴 **`auto-fit` + `minmax` is a responsive grid with no media queries at all** —
demo that line and explain it. It reads as experience.

Flex axis vocabulary: `justify-content` = main axis, `align-items` = cross axis.
`flex: 1` = `flex-grow:1 flex-shrink:1 flex-basis:0`.

---

## Q4 🔴 Responsive design — mobile-first
```css
.card { padding: 1rem; }                              /* mobile base */
@media (min-width: 768px)  { .card { padding: 2rem; } }  /* tablet+ */
@media (min-width: 1024px) { .card { padding: 3rem; } }  /* desktop+ */
```
"I write mobile-first with `min-width` queries: the base styles are the simplest
case and each breakpoint adds complexity. `max-width` queries mean the phone —
usually the weakest device — downloads and overrides desktop styles."

Essentials: `<meta name="viewport" content="width=device-width, initial-scale=1">`
(without it, nothing responsive works), relative units (`rem`, `%`, `vw`, `ch`),
`clamp(1rem, 2.5vw, 2rem)` for fluid type, `max-width: 100%` on images,
and container queries when a component must adapt to *its container*, not the viewport.

---

## Q5 Position values
`static` (default) · `relative` (offset from itself, keeps its space, creates a
positioning context) · `absolute` (removed from flow, positioned against nearest
positioned ancestor) · `fixed` (against the viewport — sticky headers) ·
`sticky` (relative until it hits a threshold, then fixed — needs `top` set).

---

## Q6 Specificity & the cascade
inline (1000) > id (100) > class/attribute/pseudo-class (10) > element (1).
`!important` overrides everything — "a debugging smell; I'd rather fix the
selector. Consistent low specificity, or a utility framework like Tailwind, avoids
the arms race entirely."

---

## Q7 Quick-fire
- **`display: none` vs `visibility: hidden` vs `opacity: 0`?** Removed from layout / hidden but occupies space / visible to layout **and** still clickable.
- **Pseudo-class vs pseudo-element?** `:hover` (a state) vs `::before` (a generated sub-element).
- **`rem` vs `em`?** `rem` = root font size (predictable); `em` = parent's (compounds when nested).
- **Centre a div?** `display:grid; place-items:center` — or flex with `justify-content` + `align-items`.
- **CSS variables?** `--brand: #0055ff;` / `var(--brand)`. Runtime-changeable — the standard way to do theming and dark mode.
- **Z-index not working?** It only applies to positioned elements, and it's scoped to the parent's **stacking context** — a parent with `transform` or `opacity < 1` traps children.
- **Tailwind opinion?** "Utility classes keep styles co-located with markup, no naming debates, and unused CSS is purged so the bundle stays small. Trade-off is noisy JSX — I pull repeated patterns into components or `@apply`." *(Have an opinion; don't be dogmatic.)*
- **SCSS?** Nesting, variables, mixins, partials — compiles to CSS. Less needed now that CSS has nesting and custom properties.
- **CSS Modules?** `styles.card` — locally scoped class names, no global collisions. Next.js supports them out of the box.

---

### ✅ Self-check
1. Flexbox vs Grid, decided in one sentence.
2. Write the `auto-fit`/`minmax` responsive grid from memory.
3. Explain mobile-first and why `min-width` beats `max-width`.
