---
name: china-miniapp-design
description: Apply WeChat Mini Program platform rules, TDesign MiniProgram component discipline, and B2B mobile information design for this project. Use when building or changing miniprogram UI, WXML/WXSS/app.json/project.config.json, or pages for the Sulian cross-border MVP.
---

# China MiniProgram Design

## Purpose

Use this skill when designing or implementing UI for the current WeChat Mini Program MVP. It converts broad UI advice into rules that fit a Chinese WeChat Mini Program, B2B order browsing, factory applications, and admin-driven demand matching.

The current product path is defined in `MINIPROGRAM_MVP_PATH.md`. The UI conflict policy is defined in `UI_DESIGN_SKILLS.md`. The design source of truth is `docs/design-system.md`; do not change global tokens unless the user asks or accessibility requires it.

## Authority

Priority order:

```text
Business correctness
> WeChat Mini Program platform rules
> Usability and accessibility
> Project design system
> UX suggestions
> Aesthetic direction
> Decoration and animation
```

This skill can override web-oriented visual advice when it conflicts with mobile task efficiency, touch ergonomics, WeChat platform conventions, or the project design system.

## Component System

Use one primary component system:

```text
TDesign MiniProgram
```

Use WeUI as an interaction and native behavior reference, not as a second component library. Do not mix TDesign Button, WeUI Button, and custom Button styles on different pages.

Component priority:

```text
Existing project component
> TDesign MiniProgram
> WeChat native component
> Custom component
```

Do not add Vant, NutUI, Ant Design Mobile, WeUI Components, or another UI framework unless the user explicitly approves a design-system change.

## Page Rules

Before designing a page, identify:

1. Who uses the page.
2. The main task.
3. The most important information.
4. The most important action.

For the Sulian MVP, prioritize readable demand/order information over decorative layout. Avoid landing-page patterns, oversized hero sections, desktop dashboard layouts squeezed into mobile, excessive shadows, glassmorphism, heavy gradients, and high-motion effects.

Expected pages:

- Login: enterprise account and password, token persistence, clear error states.
- Demand hall: published demand cards, category/country/craft/delivery filters, fast scanning.
- Demand detail: desensitized information, product image, quantity, craft, delivery days, apply action.
- Apply dialog: confirms demand number, product, quantity, and manual platform review.
- My applications: status-filtered application history.
- Order detail/progress: order summary and progress timeline.
- Profile: factory account and logout.

## Layout And Tokens

Use `rpx` for mini program sizing. Respect safe areas, navigation bar space, tab bar space, popup keyboard behavior, and touch targets.

Use tokens from `docs/design-system.md` for colors, radius, spacing, typography, and status styles. If a new UI need appears, add the smallest token necessary and record the decision in `docs/ui-decisions.md`.

## Visual Direction

Default direction:

```text
Professional Industrial Commerce
```

The interface should feel trustworthy, efficient, restrained, and commercial. Use clothing/product images, demand numbers, status tags, and industrial order metadata as the main visual signature.

## Privacy

Never display buyer private data in factory-facing pages:

- Customer name
- Email
- WhatsApp
- Full company identity unless already desensitized

Demand details should visibly communicate that customer information has been reviewed and desensitized.
