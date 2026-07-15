<div align="center">

# Replicate Web UI

**Rebuild the visual design, layout, and interactions of a reference website in your own frontend project.**

[![简体中文](https://img.shields.io/badge/简体中文-E5E7EB?style=for-the-badge)](./README.md)
[![English](https://img.shields.io/badge/English-111827?style=for-the-badge)](./README_EN.md)

A frontend visual migration Agent Skill that works across AI coding agents.

</div>

## What It Is

`replicate-web-ui` follows the open [Agent Skills specification](https://agentskills.io/specification). Give it a reference URL or screenshot and a target project path. A compatible AI coding agent analyzes the reference design system and rebuilds the experience using the target project's existing frontend stack.

It is not tied to one model or product. Use it with Agent Skills-compatible tools, or ask any AI agent with file, browser, terminal, and code-editing capabilities to read `SKILL.md` and follow the workflow directly.

It does not simply download website source code. It follows a verifiable implementation workflow:

1. Analyze layout, typography, color, spacing, radius, shadows, and motion
2. Identify responsive changes across desktop, tablet, and mobile
3. Adapt the reference design to your own brand and content
4. Implement it in an existing React, Vue, Next.js, or other frontend project
5. Run the app, capture screenshots, compare results, and iterate

## Use Cases

- Use a strong landing page as visual inspiration for your own product
- Rebuild a card, navigation bar, modal, or full page from a screenshot
- Transfer scroll motion, hover feedback, or responsive behavior into an existing app
- Modernize an older page toward a clearly defined visual style
- Rebuild a company-owned website at high fidelity after confirming authorization
- Extract a reference site's design language without copying its brand identity

## Universal Installation

The recommended project-level location is `.agents/skills/`. Run from your project root:

```powershell
git clone https://github.com/hxy180/replicate-web-ui.git .agents/skills/replicate-web-ui
```

Agent Skills-compatible tools can discover this directory automatically. Some clients also support product-specific skill directories; follow the documentation for your chosen tool.

### Tools Without Automatic Skill Discovery

Clone the repository anywhere:

```powershell
git clone https://github.com/hxy180/replicate-web-ui.git
```

Then ask the agent to read:

```text
replicate-web-ui/SKILL.md
```

Any agent that can read files, inspect a reference website, edit the target project, and run commands can follow the workflow.

## Usage

When your agent supports Skill invocation syntax, use:

```text
Use $replicate-web-ui.

Reference: https://example.com
Target project: D:\projects\my-app
Target page: home page
Fidelity: close
Requirements: preserve the scroll motion, use my branding, and support mobile.
```

You can also provide the `SKILL.md` path directly to any AI coding agent:

```text
Read and follow D:\skills\replicate-web-ui\SKILL.md to rebuild the Hero section
from https://example.com in my current React project.
```

## Examples

### Landing Page Migration

```text
Use $replicate-web-ui with https://example.com as the reference.
Build a product landing page in D:\projects\product-site with the same visual rhythm.
Preserve the layout and motion, but replace the logo, images, copy, and colors.
```

### Component From a Screenshot

```text
Use $replicate-web-ui to rebuild this pricing card from my screenshot
inside the current Vue project. Include its hover state and mobile layout.
```

### Interaction Transfer

```text
Use $replicate-web-ui to analyze the scroll reveals and card parallax
on the reference URL, then add those interactions to the current Next.js home page
without changing its existing content structure.
```

### Authorized High-Fidelity Migration

```text
Our company owns this page and I am authorized to reproduce it.
Use $replicate-web-ui in exact-authorized mode and verify it at
1440px, 768px, and 390px widths.
```

## Fidelity Modes

| Mode | Best for | Behavior |
| --- | --- | --- |
| `inspired` | Borrowing a design direction | Preserves design language while changing composition and identity |
| `close` | Achieving a similar visual experience | Matches layout, hierarchy, and motion while replacing branded material |
| `exact-authorized` | User-owned or explicitly authorized pages | Pursues high fidelity with multi-viewport visual verification |

The default is `close`.

## What the Skill Does

- Preserves the target project's framework, components, and design tokens
- Uses a real browser to inspect pages and interaction states
- Covers responsive desktop and mobile layouts
- Maintains semantic HTML, keyboard access, and reduced-motion support
- Runs available tests, lint, and build commands
- Uses screenshot comparison as a visual verification signal

## Safety and Copyright Boundaries

The Skill does not copy private source code, minified production bundles, tracking code, credentials, or hidden APIs. Without permission, it also replaces logos, trademarks, paid fonts, proprietary imagery, and copy.

Do not use it to build deceptive lookalike login, payment, wallet, banking, government, or account-recovery pages. See [`references/compliance-boundaries.md`](./references/compliance-boundaries.md) for the complete rules.

## Repository Structure

```text
replicate-web-ui/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── visual-analysis.md
│   └── compliance-boundaries.md
└── scripts/
    └── compare_screenshots.py
```

`SKILL.md`, `references/`, and `scripts/` are platform-neutral. `agents/openai.yaml` is an optional adapter for OpenAI/Codex clients that support that metadata format; other agents can ignore it.

## Dependencies

The Skill requires an AI agent that can read files, use a browser, edit code, and run terminal commands. The screenshot comparison helper requires Python 3 and Pillow:

```powershell
python -m pip install Pillow
```

## License

No open-source license has been selected yet. All rights are reserved by the repository owner.
