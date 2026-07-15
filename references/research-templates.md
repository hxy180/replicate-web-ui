# Research Templates

Use these templates for a full page or multi-component replication. Keep them concise and omit sections that do not affect implementation.

## REFERENCE.md

```markdown
# Reference

## Scope
- Input: URL / screenshot / video
- Captured at:
- Fidelity:
- Target route:

## Capture matrix
| Width | State | Artifact | Notes |
| ---: | --- | --- | --- |

## Design tokens
| Token | Observed value | Target mapping |
| --- | --- | --- |

## Breakpoints
| Range | Structural change |
| --- | --- |

## Assets
| Asset | Role | Reuse decision | Replacement |
| --- | --- | --- | --- |
```

## BEHAVIORS.md

```markdown
# Behaviors

| Component | Trigger | Initial state | Final state | Timing | Responsive notes | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
```

Include scroll position, sticky thresholds, modal dismissal, focus return, carousel controls, and reduced-motion behavior when relevant.

## Component specification

Create `components/<name>.md`:

```markdown
# Component name

## Purpose and evidence
- Screenshot or timestamp:
- Target component:

## Structure and layering
- Container:
- Children:
- Background / foreground / overlay:
- Pseudo-elements:

## Geometry and visual values
| Property | Desktop | Tablet | Mobile |
| --- | --- | --- | --- |

## States
| State | Trigger | Changed properties | Accessibility behavior |
| --- | --- | --- | --- |

## Content and assets
- Text:
- Images or icons:
- Licensing decision:

## Implementation notes
- Existing component or token mappings:
- Intentional differences:
- Unknown or inferred behavior:
```

Do not copy large production HTML or CSS into these documents. Record only evidence needed to implement and verify the result.
