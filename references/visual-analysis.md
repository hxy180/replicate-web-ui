# Visual Analysis Checklist

Use this checklist to turn a reference page into implementation evidence.

## Capture Matrix

Capture at minimum:

| Target | Width | State |
| --- | ---: | --- |
| Desktop | 1440 | top and full page |
| Tablet | 768 | top and key interaction |
| Mobile | 390 | top and full page |

Add product-specific breakpoints when the reference visibly changes elsewhere.

## Geometry

- Page max width and outer gutters
- Section heights and vertical rhythm
- Grid columns, gaps, alignment, and overlap
- Sticky or fixed regions
- Content order changes by breakpoint
- Overflow and clipping behavior

## Visual Tokens

- Background, surface, text, muted, border, and accent colors
- Font families, weights, sizes, line heights, and letter spacing
- Spacing scale and repeated dimensions
- Corner radii and border thickness
- Shadow direction, blur, spread, and opacity
- Icon family, stroke width, and optical size

## Interaction

- Hover, focus, active, selected, disabled, loading, and error states
- Menu, drawer, modal, tooltip, carousel, and accordion behavior
- Transition duration, delay, easing, direction, and stagger
- Scroll-linked, sticky, reveal, and parallax behavior
- Pointer versus keyboard behavior
- Reduced-motion fallback

## Content and Assets

- Separate structural imagery from brand-owned artwork
- Identify text that controls line wrapping and section height
- Record image aspect ratios and crop behavior
- Replace unavailable fonts with metric-compatible alternatives

## Implementation Order

1. Page shell and section geometry
2. Responsive grid and content flow
3. Typography and spacing
4. Color, borders, shadows, and imagery
5. Interaction states and animation
6. Accessibility and final visual comparison
