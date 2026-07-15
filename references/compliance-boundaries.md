# Compliance Boundaries

## Allowed Adaptation

- Reimplement public visual patterns with original code
- Reuse general layout ideas, spacing systems, and interaction principles
- Create close visual adaptations with new branding, copy, and licensed assets
- Reproduce user-owned or explicitly authorized pages at high fidelity

## Do Not Copy

- Private or leaked source code
- Minified production bundles as implementation source
- Logos, trademarks, proprietary illustrations, photography, copy, or paid fonts without permission
- Tracking scripts, analytics identifiers, credentials, tokens, or private API behavior
- Content hidden behind authentication or access controls without authorization

## Deceptive or Sensitive Pages

Do not create a lookalike page intended to impersonate a real service, collect credentials, capture payment data, mislead users, or obscure who operates the page. This includes deceptive login, wallet, checkout, banking, government, healthcare, and account-recovery experiences.

For legitimate user-owned sensitive flows, preserve the user's own identity and security architecture. Do not import the reference service's branding or endpoints.

## Default Decision

When ownership or licensing is unclear:

1. Use `close` rather than `exact-authorized` fidelity.
2. Replace identity-bearing assets and copy.
3. Implement the behavior with original code.
4. Note the intentional differences in the final report.
