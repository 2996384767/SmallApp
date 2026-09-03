# Project Agent Instructions

## Current Product Path

Current implementation follows `MINIPROGRAM_MVP_PATH.md`.

Build the competition MVP first:

```text
WeChat native mini program
-> Flask API and Flask/Jinja2 admin
-> local MariaDB database smallapp
```

The old H5/uni-app path is prototype and learning context, not the active delivery path.

## UI Skill Workflow

For mini program UI work:

1. Read `MINIPROGRAM_MVP_PATH.md`.
2. Read `UI_DESIGN_SKILLS.md` when design-skill coordination matters.
3. Read `docs/design-system.md`.
4. Read `docs/ui-decisions.md`.
5. Use installed/project `ui-ux-pro-max-compat` as the Design Intelligence Layer when UX structure is needed.
6. Use installed `frontend-design` only as a Taste Layer when visual direction is needed.
7. Apply installed/project `china-miniapp-design` as the Platform Layer.
8. After implementation or screenshots, apply installed/project `miniapp-ui-review` as the Review Layer.

Do not let broad frontend taste guidance override WeChat platform rules, business correctness, or the frozen design system.

`frontend-design` must not introduce a new UI library, change frozen design tokens, add landing-page hero patterns, or push bold web aesthetics into factory-facing mini program screens.

## UI Conflict Priority

```text
Business correctness
> WeChat Mini Program platform rules
> Usability and accessibility
> Existing design system
> UX
> Aesthetic style
> Decoration
```

## Component Policy

Use TDesign MiniProgram as the single primary component system.

Use WeUI only as a WeChat native interaction reference. Do not introduce another UI framework without explicit user approval.

## Sensitive Data

Do not commit `services/api/.env`. Do not write real database passwords, tokens, private keys, or credentials into Markdown documentation or logs.
