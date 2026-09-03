# UI Decisions

## 2026-09-03

Decision:
Use TDesign MiniProgram as the single primary component system.

Reason:
The current product is a WeChat Mini Program for B2B demand browsing, factory applications, and order progress. A single component system prevents mixed button, card, popup, tag, and form styles.

Rejected:
Mixing TDesign, WeUI Components, Vant, NutUI, and custom UI systems.

---

Decision:
Use WeUI as an interaction reference only.

Reason:
WeUI matches WeChat native expectations, but using it as a second component library would cause visual inconsistency with TDesign.

---

Decision:
Set the visual direction to Professional Industrial Commerce.

Reason:
The app serves factory users and platform operators. It should feel trustworthy, efficient, restrained, and business-focused.

Rejected:
Large hero pages, marketing-style composition, glassmorphism, heavy gradients, and decorative animation.

---

Decision:
Freeze global design tokens in `docs/design-system.md`.

Reason:
Future UI changes should not re-invent colors, spacing, radius, and typography on each page.

---

Decision:
Prioritize demand and order information over visual spectacle.

Reason:
The main user task is scanning demands, applying for orders, and checking progress.
