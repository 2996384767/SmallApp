---
name: miniapp-ui-review
description: Review completed WeChat Mini Program UI or screenshots for the Sulian MVP. Use after implementation or when screenshots are available; report usability, consistency, platform, and visual issues without redesigning the whole page.
---

# MiniProgram UI Review

## Purpose

Use this skill after a mini program page, flow, or screenshot exists. It reviews the implementation against business goals, WeChat Mini Program platform expectations, `docs/design-system.md`, and `UI_DESIGN_SKILLS.md`.

Review finds problems and recommends minimal fixes. It does not restart the design direction, change the component library, or rework the whole information architecture unless there is a blocking business or platform issue.

## Severity

Report issues in this order:

```text
P0 Blocking
P1 Major
P2 Medium
P3 Polish
```

P0 examples:

- Key action cannot be completed.
- Content is covered by navigation, capsule, keyboard, popup, or tab bar.
- Text is unreadable.
- Tap target is too small for a core action.
- Factory-facing page exposes private buyer information.

P1 examples:

- Primary action is unclear.
- Information hierarchy prevents fast demand/order scanning.
- TDesign, WeUI, and custom components are mixed inconsistently.
- Form flow is hard to complete.
- Status meaning is ambiguous.

P2 examples:

- Spacing or typography is inconsistent.
- Demand cards are too sparse or too dense.
- Too many colors or status tags compete.
- Empty/loading/error states are incomplete.

P3 examples:

- Minor icon alignment, copy, shadow, or spacing polish.

## Review Checklist

Check:

- The page answers who uses it, main task, key information, and key action.
- Business state is correct: published demand, pending application, approved application, generated order, progress stage.
- Factory pages show desensitized demand information only.
- Touch targets and form controls are comfortable on mobile.
- TDesign MiniProgram remains the primary component system.
- Tokens from `docs/design-system.md` are followed.
- Visual style is restrained and professional, without generic AI-gradient aesthetics.
- Loading, empty, error, and success feedback states exist where needed.

## Output

Lead with findings. Use file paths or screenshot references when available. For each issue, include severity, location, risk, and the smallest practical fix.

Do not run more than two review-fix-review loops unless the user explicitly asks for deeper polishing.
