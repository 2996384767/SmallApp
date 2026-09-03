# 肃联跨境 Design System

## Status

```text
TOKEN_STATE = FROZEN
```

This file is the visual source of truth for the current WeChat Mini Program MVP. UI work should read this before creating or changing pages.

## Product Profile

```text
PRODUCT: B2B Apparel Order Marketplace
PROJECT: 肃联跨境
PLATFORM: WeChat Mini Program
PRIMARY_DESIGN_SYSTEM: TDesign MiniProgram
WEUI_ROLE: Interaction reference
VISUAL_DIRECTION: Professional Industrial Commerce
INFORMATION_DENSITY: Medium-High
VISUAL_EXPERIMENT: Low
MOTION: Low
DECORATION: Low
CONTENT_PRIORITY: High
```

## Users

```text
USER_A: 平台运营人员 / 管理员
USER_B: 服装工厂
HIDDEN_USER: 海外需求方，信息由平台审核脱敏后发布
```

## Design Principles

```text
业务 > 平台 > 可用性 > 设计体系 > UX > 审美 > 装饰
```

- One primary component system: TDesign MiniProgram.
- WeUI is only a platform interaction reference.
- Ant Design principles may inform B2B data hierarchy, not component choice.
- Do not expose buyer private information in factory-facing pages.
- Do not make the mini program look like a reduced desktop dashboard.

## Tokens

### Color

```text
Primary: #0052D9
Primary-Pressed: #003CAB
Background: #F5F7FA
Surface: #FFFFFF
Surface-Subtle: #F8FAFC
Text-Primary: #1F2937
Text-Secondary: #667085
Text-Muted: #98A2B3
Border: #E5E7EB
Success: #12B76A
Warning: #F79009
Danger: #D92D20
Info: #2E90FA
```

### Radius

```text
Radius-S: 8rpx
Radius-M: 16rpx
Radius-L: 24rpx
```

Use `Radius-M` for ordinary cards and inputs. Do not use extra-large rounded card styles unless recorded in `docs/ui-decisions.md`.

### Spacing

```text
Spacing-XS: 8rpx
Spacing-S: 16rpx
Spacing-M: 24rpx
Spacing-L: 32rpx
Spacing-XL: 48rpx
```

### Typography

```text
Title: 40rpx / 600
SectionTitle: 32rpx / 600
Body: 28rpx / 400
BodyStrong: 28rpx / 600
Caption: 24rpx / 400
Meta: 22rpx / 400
```

Use system fonts for WeChat native consistency.

### Status

```text
published: 可接单 / Info
pending: 待平台审核 / Warning
approved: 已通过 / Success
rejected: 已拒绝 / Danger
matched: 已匹配 / Success
closed: 已关闭 / Text-Muted
```

## Demand Card Hierarchy

Recommended order:

```text
Product category/name                 Status
Core demand description
Quantity      Craft      Country
Delivery days
Demand no / publish time
                                  View detail / Apply
```

Visual weight:

```text
Business object
> Status and core data
> Trade conditions
> Metadata
```

## Prohibited Defaults

Avoid:

- Purple/blue AI gradients.
- Glassmorphism.
- Large blur backgrounds.
- Oversized hero sections.
- Excessive card shadows.
- Multiple icon libraries.
- Emoji as formal icons.
- Over-rounded UI.
- Desktop dashboard layout on mobile.
- Decorative modules that do not support the task.
