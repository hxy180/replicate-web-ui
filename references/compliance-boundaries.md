# Compliance Boundaries

## Allowed Adaptation

- Reimplement public visual patterns with original code
- Reuse general layout ideas, spacing systems, and interaction principles
- Create close visual adaptations with new branding, copy, and licensed assets
- Reproduce user-owned or explicitly authorized pages at high fidelity
- Inspect public DOM and computed styles to understand visible behavior

## Do Not Copy

- Private or leaked source code
- Minified production bundles as implementation source
- Logos, trademarks, proprietary illustrations, photography, copy, or paid fonts without permission
- Tracking scripts, analytics identifiers, credentials, tokens, or private API behavior
- Content hidden behind authentication or access controls without authorization
- Asset URLs as permanent hotlinks to the reference production server

## Deceptive or Sensitive Pages

Do not create a lookalike page intended to impersonate a real service, collect credentials, capture payment data, mislead users, or obscure who operates the page. This includes deceptive login, wallet, checkout, banking, government, healthcare, and account-recovery experiences.

For legitimate user-owned sensitive flows, preserve the user's own identity and security architecture. Do not import the reference service's branding or endpoints.

Do not submit forms, create accounts, purchase items, delete data, or trigger other irreversible external actions merely to inspect an interaction state.

## Assets and exact reproduction

- Treat public availability as access, not as a license.
- Inventory assets before downloading them and record whether each will be reused, replaced, or omitted.
- Reuse logos, copy, fonts, photography, video, and illustrations only when the user supplies them, confirms ownership, or provides a compatible license.
- Inline SVG structure may be studied, but identity-bearing artwork should be replaced unless authorized.
- Require explicit authorization for `exact-authorized`; a request for a "clone" alone is not sufficient.

## Default Decision

When ownership or licensing is unclear:

1. Use `close` rather than `exact-authorized` fidelity.
2. Replace identity-bearing assets and copy.
3. Implement the behavior with original code.
4. Note the intentional differences in the final report.
