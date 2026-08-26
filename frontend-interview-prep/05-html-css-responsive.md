# 05 · HTML, CSS and Responsive Design 🟠
**Time needed: 30 minutes tonight, quick review tomorrow**

The first line of the job description is about "translating UI/UX wireframes into
clean, performant, responsive code". This topic shows up more in the coding round
than in questions, but a few questions are still likely.

---

## Q1. What is semantic HTML and why does it matter? 🔴

**Semantic** means the tag describes what the content **is**, not how it looks.

```html
<!-- Not semantic: everything is a div -->
<div class="header">
  <div class="nav">
    <div class="btn" onclick="submit()">Apply</div>
  </div>
</div>

<!-- Semantic -->
<header>
  <nav>
    <button onclick="submit()">Apply</button>
  </nav>
</header>
```

### Three reasons it matters
1. **Accessibility.** A screen reader user can jump straight to `<nav>` or `<main>`.
   A `<button>` can be reached with the Tab key and pressed with Enter. A
   `<div onClick>` cannot do either, unless you add a lot of extra code.

2. **SEO.** Crawlers use the structure to understand what the page is about.
3. **Readability.** The next developer can see the shape of the page instantly.

Tags worth knowing: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`,
`<aside>`, `<footer>`, `<figure>`, `<button>`, `<form>` and `<label>`.

---

## Q2. The box model 🔴

Every element is a box made of four layers, from inside out:

```
+---------------- margin ----------------+   space outside
|  +------------- border -------------+  |
|  |  +---------- padding ---------+  |  |   space inside
|  |  |        content             |  |  |
```

### The problem, and the one line fix
By default, `width: 300px` means the **content** is 300px. Add 20px of padding and a
2px border, and the box actually takes 344px on screen. This breaks layouts.

```css
* { box-sizing: border-box; }
```

Now `width: 300px` means the whole box is 300px, including padding and border. This
is what everyone expects, which is why this line is in almost every CSS reset.

---

## Q3. Flexbox vs Grid — when do you use which? 🔴

**Flexbox works in one direction.** A row, or a column.
**Grid works in two directions.** Rows and columns together.

### Use Flexbox for
Navbars, a row of buttons, centring something, spacing items apart, the inside of a
card.

```css
.navbar {
  display: flex;
  justify-content: space-between;  /* spread along the main axis */
  align-items: center;             /* centre on the cross axis */
  gap: 1rem;
}
```

### Use Grid for
Page layouts, card galleries, dashboards, anything with real rows and columns.

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.5rem;
}
```

### 🔴 That grid line is worth explaining, it sounds senior
Read it as: *"Fit as many columns as you can. Each must be at least 260px wide. Any
leftover space is shared equally between them."*

The result is a card grid that goes 4 across on a laptop, 2 on a tablet and 1 on a
phone, **with no media queries at all**. Demo that line and explain it.

### They work together
A common real layout is Grid for the page, Flexbox inside each card.

### Centring, the short version
```css
.parent { display: grid; place-items: center; }
```

---

## Q4. Responsive design and mobile first 🔴

### What mobile first means
Write the styles for the smallest screen first. Then use `min-width` media queries
to **add** complexity for bigger screens.

```css
/* base = mobile */
.card { padding: 1rem; }

@media (min-width: 768px)  { .card { padding: 2rem; } }   /* tablet and up */
@media (min-width: 1024px) { .card { padding: 3rem; } }   /* desktop and up */
```

### Why not the other way round?
If you write desktop styles first and use `max-width` to shrink them, the phone
downloads all the desktop rules and then overrides them. The weakest device does the
most work. Mobile first gives the simplest styles to the simplest device.

### The essentials
- **The viewport meta tag.** Without this line, nothing responsive works at all:
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```
- **Relative units** instead of fixed pixels: `rem`, `%`, `vw`.
- **Fluid sizing** with `clamp()`:
```css
font-size: clamp(1rem, 2.5vw, 2rem);   /* min, preferred, max */
```
- **`max-width: 100%` on images** so they never overflow their container.

---

## Q5. Position values

| Value | What it does |
|---|---|
| `static` | Default. Sits in normal flow. |
| `relative` | Moves relative to itself, but keeps its original space. |
| `absolute` | Removed from flow. Positioned against the nearest positioned parent. |
| `fixed` | Positioned against the viewport. Stays put when scrolling. |
| `sticky` | Normal until it reaches a threshold, then behaves like fixed. |

`sticky` is what you use for a table header that stays visible while scrolling. It
needs a `top` value to work.

---

## Q6. Specificity, in simple terms

When two rules target the same element, the more specific one wins.

```
inline style   = 1000
#id            = 100
.class         = 10
element (div)  = 1
```

`!important` beats everything. Treat it as a warning sign.
> "If I need `!important`, it usually means my selectors have got too specific
> somewhere. I would rather fix the selector than fight it."

---

## Q7. Quick questions

- **`display: none` vs `visibility: hidden` vs `opacity: 0`?**
  Removed from the layout / hidden but still takes up space / fully visible to the
  layout and **still clickable**.

- **Pseudo class vs pseudo element?** `:hover` is a state. `::before` creates a new
  sub element.

- **`rem` vs `em`?** `rem` is relative to the root font size, which is predictable.
  `em` is relative to the parent, so it multiplies when nested.

- **CSS variables?** Declare `--brand: #14356b` on `:root`, then use it anywhere as
  `background: var(--brand)`. They can be changed at runtime with JavaScript, which
  is how dark mode is usually built.

- **Why is my `z-index` not working?** Two common reasons. It only applies to
  positioned elements. And a parent with `transform` or `opacity` less than 1
  creates a new stacking context that traps its children.

- **What do you think of Tailwind?** Have an opinion but do not be extreme.
  > "Utility classes keep the styling next to the markup, and unused CSS is removed
  > at build time so the file stays small. The downside is that the JSX gets noisy.
  > I pull repeated patterns into components."

- **CSS Modules?** `styles.card` generates a unique class name, so styles cannot
  clash between files. Next.js supports them by default.

---

## ✅ Check yourself before moving on
1. Flexbox vs Grid, decided in one sentence.
2. Write the `auto-fit` and `minmax` grid line from memory and explain it.
3. Explain mobile first and why `min-width` is better than `max-width`.
