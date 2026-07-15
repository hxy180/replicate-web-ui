# Visual Analysis

Use this reference to turn a URL, screenshot, or video into implementation evidence. Observe first, infer second, and label unsupported assumptions.

## Capture matrix

Capture at minimum:

| Target | Width | Required evidence |
| --- | ---: | --- |
| Desktop | 1440 | top, full page, navigation, primary interaction |
| Tablet | 768 | top, content reflow, menus or sidebars |
| Mobile | 390 | top, full page, navigation, overflow |

Add widths immediately before and after any breakpoint where composition changes.

## Observation order

1. Capture the initial viewport.
2. Scroll slowly from top to bottom.
3. Record sticky, reveal, parallax, snap, and lazy-loaded behavior.
4. Return to relevant sections and exercise reversible interactions.
5. Change viewport widths and repeat only the states whose layout changes.

Scrolling before clicking helps distinguish scroll-driven effects from click-driven state.

## Geometry and layering

- Page max width, outer gutters, section heights, and vertical rhythm
- Grid columns, gaps, alignment, overlap, and content order
- Fixed, sticky, absolute, and normal-flow regions
- Overflow, clipping, masks, blend modes, and crop behavior
- Background, foreground, and overlay layers
- `::before` and `::after` decorations

## Computed-style extraction

Use computed styles on representative elements. Do not dump every DOM node.

```js
const element = document.querySelector('selector');
const style = getComputedStyle(element);
const properties = [
  'display', 'position', 'inset', 'zIndex',
  'width', 'height', 'maxWidth', 'minHeight',
  'padding', 'margin', 'gap',
  'gridTemplateColumns', 'flexDirection', 'alignItems', 'justifyContent',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'color', 'background', 'border', 'borderRadius', 'boxShadow',
  'opacity', 'overflow', 'objectFit', 'transform',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction',
  'animationName', 'animationDuration', 'animationTimingFunction'
];
Object.fromEntries(properties.map(name => [name, style[name]]));
```

Extract state differences after triggering `hover`, `focus`, `active`, `selected`, `disabled`, `open`, `loading`, or `error`. Record only properties that changed.

## Visual tokens

- Background, surface, text, muted, border, and accent colors
- Font families, weights, sizes, line heights, and letter spacing
- Repeated spacing, dimensions, radii, and border widths
- Shadow direction, blur, spread, and opacity
- Icon family, stroke width, optical size, and alignment
- Gradient stops, image aspect ratios, and crop positions

Cluster repeated values into tokens only when the repetition is real.

## Interaction and motion

For each behavior, record:

- Trigger and target
- Initial and final states
- Duration, delay, easing, direction, and stagger
- Whether it is interruptible or reversible
- Pointer, keyboard, and reduced-motion behavior
- Responsive differences

For video, inspect frames immediately before, during, and after each transition. Separate camera or recording movement from page animation.

## Screenshot-only evidence

Screenshots can prove visible geometry and styling, but usually cannot prove:

- Off-screen content or breakpoints
- Hover, focus, loading, or error states
- Transition timing and easing
- Sticky or scroll-triggered behavior

Infer conservatively and identify inferred behavior in the final report.

## Assets and content

- Identify structural imagery separately from identity-bearing artwork.
- Record text that affects wrapping and section height.
- Inventory image, video, SVG, icon, and font sources before deciding whether they can be reused.
- Prefer user-supplied or licensed assets and metric-compatible font substitutes.
- Do not permanently hotlink reference assets.

## Implementation order

1. Page shell and section geometry
2. Responsive grid and content flow
3. Typography and spacing
4. Color, borders, shadows, and imagery
5. Interaction states and motion
6. Accessibility and visual comparison
