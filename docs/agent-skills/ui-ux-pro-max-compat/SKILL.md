---
name: ui-ux-pro-max-compat
description: Provide bounded UI/UX design intelligence for the Sulian Mini Program MVP when the full UI/UX Pro Max skill is unavailable or too broad. Use for UX, information architecture, form flow, accessibility, and design-token suggestions before visual implementation.
---

# UI/UX Pro Max Compat

## Purpose

This is a project-safe compatibility layer for the UI/UX design-intelligence role described in `UI_DESIGN_SKILLS.md`.

It does not replace the full third-party UI/UX Pro Max package. It gives this project enough reusable UX guidance without running external installers or introducing broad design rules that may conflict with WeChat Mini Program constraints.

## Authority

This skill is advisory. It can propose:

- User flows.
- Information architecture.
- Form structure.
- Accessibility improvements.
- State models.
- Design-token additions.
- Demand/order card hierarchy.

It cannot override:

- Business requirements in `MINIPROGRAM_MVP_PATH.md`.
- WeChat Mini Program platform rules.
- TDesign MiniProgram as the primary component system.
- Frozen tokens in `docs/design-system.md`.
- Existing decisions in `docs/ui-decisions.md`.

## Workflow

For a new page or flow, answer:

1. Who uses this?
2. What is the user's main task?
3. What information must be visible first?
4. What action must be easiest?
5. What states are needed: loading, empty, error, success, disabled?

Then propose the smallest useful UX structure before visual styling.

## Sulian MVP UX Defaults

Prioritize:

- Fast scanning of demand and order information.
- Clear status labels.
- Low-friction factory application flow.
- Visible manual review expectations.
- Desensitized demand details.
- Simple admin operations that support the live demo.

Avoid:

- Decorative flows that do not support the demo.
- Complex onboarding.
- Premature personalization.
- Multi-step forms when one clear page is enough.
- Hidden primary actions.

## Accessibility

Check contrast, tap target size, readable type, clear disabled/loading states, and non-color-only status communication.
