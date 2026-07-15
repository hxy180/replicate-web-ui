---
name: replicate-web-ui
description: Analyze the visual design and interaction behavior of a reference website, then rebuild that experience inside the user's own frontend project using its existing framework and conventions. Use when the user asks to recreate, replicate, migrate, imitate, or take inspiration from a URL, screenshot, landing page, component, animation, responsive layout, or web interaction. Implement and verify the result rather than stopping at design analysis. Do not use to copy private source code, protected brand assets, deceptive authentication/payment pages, or websites the user is not authorized to reproduce exactly.
---

# Replicate Web UI

Rebuild a reference site's design system and behavior in the user's own codebase. Treat the reference as visual evidence, not as source code to copy.

## Required Inputs

Identify these from the request and workspace:

- Reference URL, screenshot, or video
- Target repository and route/component
- Existing frontend framework and styling system
- Desired fidelity: `inspired`, `close`, or `exact-authorized`
- Important viewports and interactions

Ask only when the reference or target cannot be discovered. Default to `close` fidelity, desktop plus mobile, and the project's current stack.

For `exact-authorized`, require a clear statement that the user owns the page or has permission. Otherwise use `close` and replace identity-bearing assets.

## Workflow

### 1. Inspect the target project

- Read the repository before designing.
- Identify framework, router, package manager, component library, tokens, fonts, and test commands.
- Preserve established architecture and reusable components.
- Check the worktree and protect unrelated changes.

### 2. Capture the reference

- Use an available browser automation skill or Playwright to inspect the live page.
- Capture full-page and viewport screenshots at desktop and mobile sizes.
- Exercise meaningful states: hover, focus, expanded menus, dialogs, carousels, and scroll-triggered motion.
- Record layout geometry, typography, color, spacing, radius, shadows, imagery, and motion.
- If access is blocked, use user-provided screenshots or videos and state the missing states.

Read [references/visual-analysis.md](references/visual-analysis.md) before analyzing a new reference.

### 3. Define the adaptation

- Separate design principles from brand identity.
- Map the reference structure to the user's content and product goals.
- Reuse target-project tokens where close enough; add a small token layer only when needed.
- Replace logos, trademarks, copyrighted illustrations, proprietary copy, and paid fonts unless supplied or licensed by the user.
- Prefer local placeholders or clearly licensed assets over hotlinking.

Read [references/compliance-boundaries.md](references/compliance-boundaries.md) when the page contains login, payment, financial, medical, government, brand-sensitive, or proprietary content.

### 4. Implement end to end

- Build the requested page or component in the target project.
- Match large geometry first, then typography and spacing, then decorative detail and motion.
- Implement responsive behavior intentionally; do not merely shrink the desktop layout.
- Preserve semantic HTML, keyboard access, visible focus, reduced-motion support, and readable contrast.
- Avoid adding dependencies when the existing stack can produce the effect.
- Do not copy minified bundles, hidden APIs, tracking code, or private source.

### 5. Verify visually

- Start the target app and load the implemented route in a real browser.
- Capture the same viewports and states used for the reference.
- Compare reference and implementation side by side.
- Fix overflow, wrapping, stacking, font metrics, spacing, breakpoint, and animation errors.
- Run relevant repository tests, lint, and build commands.

For same-size PNG comparisons, run:

```powershell
python scripts/compare_screenshots.py reference.png implementation.png --diff diff.png
```

Treat the numeric score as a signal, not as the goal. Intentional brand and content changes should remain different.

### 6. Report the result

Summarize:

- What was implemented
- Which reference traits were preserved
- Which assets or behaviors were intentionally changed
- Viewports and interactions verified
- Tests run and any remaining limitation

## Fidelity Levels

- `inspired`: Transfer the design language while changing composition and identity.
- `close`: Match layout, rhythm, hierarchy, and motion while replacing brand-specific material.
- `exact-authorized`: Pursue pixel-level similarity only for user-owned or explicitly authorized material.

## Completion Standard

Do not stop after screenshots, a style audit, or a plan when the user requested implementation. Finish only after the target code runs and the requested states have been visually checked, unless an external blocker makes that impossible.
