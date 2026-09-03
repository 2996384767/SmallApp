下面这版可以直接作为项目级规范保存。这里把 **现成 Skill** 和 **建议自建 Skill** 明确拆开，避免以后 Codex 把 TDesign、WeUI、Frontend Design 等规则混成一团。

# 前端 / 微信小程序 UI Skills 组合与冲突管理规范

**版本：v1.0**
**适用环境：Codex / Claude Code / Cursor / Windsurf 等 Coding Agent**
**主要适用项目：微信小程序、移动 Web、React/Vue 前端、B2B/交易型产品、管理端产品**

---

# 一、目标

本规范解决的不是“装哪些 UI Skill”这么简单，而是解决以下问题：

1. AI 写出的 UI 功能正常但审美一般；
2. 页面存在明显“AI 模板味”；
3. 不同 Skill 给出互相矛盾的设计建议；
4. Web 审美被错误应用到微信小程序；
5. TDesign、WeUI、Ant Design 等设计体系被混合使用；
6. 同一个项目不同页面风格逐渐失控；
7. AI 为了“优化 UI”擅自修改业务逻辑；
8. UI 完成以后缺少统一的视觉检查；
9. Codex 每次修改页面都会重新发明一套颜色、圆角和间距；
10. 小程序看起来像“缩小后的 PC SaaS 页面”。

最终目标是建立：

> **一个负责设计知识，一个负责审美方向，一个负责平台约束，一个负责最终审查。**

而不是让多个 Skill 平级竞争。

---

# 二、推荐 Skills 组合

推荐最终采用四层结构：

```text
┌─────────────────────────────────────┐
│ Layer 1：UI/UX Pro Max              │
│ 设计知识 / UX / Design System       │
└─────────────────┬───────────────────┘
                  ↓
┌─────────────────────────────────────┐
│ Layer 2：Frontend Design            │
│ 审美方向 / 去 AI 味 / 视觉个性       │
└─────────────────┬───────────────────┘
                  ↓
┌─────────────────────────────────────┐
│ Layer 3：China MiniProgram Design   │
│ 微信小程序 / TDesign / WeUI 平台约束 │
└─────────────────┬───────────────────┘
                  ↓
┌─────────────────────────────────────┐
│ Layer 4：MiniProgram UI Review      │
│ 截图审查 / 一致性 / 可用性 / 验收     │
└─────────────────────────────────────┘
```

四层不是平级关系。

它们分别回答四个问题：

| Skill                    | 核心问题                  |
| ------------------------ | --------------------- |
| UI/UX Pro Max            | 什么 UX、配色、字体、组件关系更合理？  |
| Frontend Design          | 怎样避免做成普通 AI 模板？       |
| China MiniProgram Design | 在微信小程序里哪些设计可以做、哪些不能做？ |
| UI Review                | 最终实现是否真的好看、统一、可用？     |

---

# 三、Skill 1：UI/UX Pro Max

## 定位

**设计知识层 / Design Intelligence**

建议作为整个设计流程的第一个 Skill。

当前 UI/UX Pro Max 已针对 Codex 等 Agent 提供安装结构，其 Skill 覆盖 UI、UX、可访问性、交互、响应式、Typography、Color、Charts 和多种技术栈，并包含可搜索的设计数据。([GitHub][1])

其现有工作流也明确支持先生成 Design System，再交给 frontend-design 确定视觉方向。([GitHub][2])

## 它应该负责

* 产品类型判断；
* UI 风格候选；
* 配色方案；
* Typography；
* UX 原则；
* 信息架构；
* Accessibility；
* 表单设计；
* 导航；
* 状态设计；
* 图表设计；
* 响应式原则；
* Design Token 建议；
* 常见 UI Anti-pattern。

## 它不应该负责

不要让它拥有以下最终决定权：

* 微信小程序原生交互规则；
* 是否使用 TDesign；
* 是否使用 WeUI；
* `rpx` 具体规范；
* 微信胶囊区域；
* 小程序安全区；
* 微信 TabBar；
* 具体组件库选择；
* 是否需要大胆视觉实验。

这些由后续 Skill 决定。

## 推荐角色

```text
ROLE:
Design Consultant

AUTHORITY:
Medium

CAN:
提出设计建议
生成 Design Tokens
提供 UX 原则

CANNOT:
违反平台规范
擅自改变组件库
擅自重构业务逻辑
```

---

# 四、Skill 2：Anthropic Frontend Design

## 定位

**审美导演 / Taste Layer**

Anthropic 官方 frontend-design Skill 的重点是：

> distinctive、intentional、避免 templated defaults。

它要求设计首先基于具体产品、用户和页面任务，再确定明确视觉方向，而不是直接套通用 AI 页面。([GitHub][3])

官方插件本身也明确强调避免 generic AI aesthetics。([GitHub][4])

## 它应该负责

### 1. 确定视觉方向

例如：

```text
Industrial Professional
Modern Commerce
Editorial
Premium Minimal
Data Dense
Warm Consumer
Technical Utility
```

每个项目选择一个主要方向。

### 2. 去除 AI 味

重点防止：

```text
紫蓝渐变
超大 Hero
三个完全一样的卡片
大面积 Glassmorphism
所有模块都有阴影
到处 24px+ 圆角
无意义装饰图形
页面极度居中
留白过量
```

### 3. 建立视觉记忆点

但只允许：

> 一个主要视觉 Signature。

例如：

```text
特色状态标签
工业订单编号视觉
轻量品牌色边框
商品图片裁切体系
特殊的信息标题结构
```

不要同时使用五六种“视觉创意”。

---

# 五、Frontend Design 的权限限制

这是整个组合中最需要限制的 Skill。

因为它天然倾向于：

```text
更大胆
更有设计感
更有个性
更具视觉冲击力
```

这些在 Landing Page 很有效。

但是对于：

```text
微信小程序
企业接单
订单平台
表单
数据页面
```

可能造成反效果。

因此规定：

```text
Frontend Design 可以提出视觉方向。

但不能覆盖：

平台规范
业务效率
触控体验
组件一致性
Accessibility
既有 Design System
```

例如：

```text
Frontend Design：
建议首页使用 64px 大型标题。

China MiniProgram Design：
交易型小程序首屏需要快速出现订单内容。

裁决：
采用小程序规则。
```

---

# 六、Skill 3：China MiniProgram Design

这是建议**自己建立的核心 Skill**。

它不是简单复制 TDesign。

而是：

```text
TDesign
+
WeUI
+
中国大陆移动端产品经验
+
微信小程序工程约束
+
B2B 信息设计
```

形成一个统一 Skill。

---

# 七、为什么需要自己建立这一层

TDesign 本身是一整套企业级设计体系，并提供专门的微信小程序组件库。([GitHub][5])

WeUI 则由微信官方设计团队为微信内网页和微信小程序设计，目标就是保持与微信原生视觉体验一致。([GitHub][6])

但：

```text
TDesign ≠ Agent Skill
WeUI ≠ Agent Skill
```

它们首先是设计体系 / UI Library。

因此正确方式不是：

```text
安装 TDesign Skill
安装 WeUI Skill
安装 Ant Design Skill
全部同时开启
```

而应该自己建立：

```text
china-miniapp-design/SKILL.md
```

由它统一吸收这些规范。

---

# 八、China MiniProgram Design 的职责

## 平台规则

负责：

```text
微信导航结构
Navbar
TabBar
Popup
Toast
Dialog
ActionSheet
Safe Area
胶囊区域
触控区域
移动端布局
rpx
滚动行为
键盘行为
表单
Picker
日期选择
上传
图片
加载
空状态
```

## 视觉规则

默认优先：

```text
清晰
克制
高信息效率
熟悉
移动端原生感
可信赖
商业化
```

而不是：

```text
炫技
艺术实验
大型视觉宣传页
复杂动画
```

---

# 九、TDesign 与 WeUI 如何组合

不要：

```text
页面 A：TDesign Button
页面 B：WeUI Button
页面 C：自己写 Button
```

否则极容易产生：

```text
圆角不同
高度不同
文字不同
Padding 不同
交互反馈不同
颜色不同
```

## 推荐策略

### 主设计体系

```text
TDesign MiniProgram
```

负责：

```text
Button
Input
Cell
Card
Tag
Tabs
Navbar
TabBar
Picker
Popup
Dialog
Toast
Loading
Skeleton
Empty
```

### WeUI

作为：

```text
微信原生行为参考
```

而不是第二套组件库。

主要参考：

```text
交互习惯
反馈方式
微信视觉语义
系统感
原生熟悉度
```

---

# 十、Ant Design 应该怎么处理

不要安装一个完整 Ant Design Skill 与 TDesign 竞争。

只吸收：

```text
数据密度
B2B 信息结构
表格思想
表单层级
状态设计
企业产品信息架构
```

形成规则。

例如：

```text
订单号
订单状态
品类
数量
交货时间
国家
工艺
报价
```

不同信息不能拥有相同视觉权重。

---

# 十一、Skill 4：MiniProgram UI Review

## 定位

**质量检查员**

注意：

Review Skill 不能重新设计页面。

它只负责：

```text
发现问题
指出问题
按严重程度排序
提出最小修改方案
```

UI/UX Pro Max 当前提供的完整设计 Stack 本身也采用“知识层 + Taste Layer + Visual Feedback + Design Review”的结构，并将 review 与生成阶段分开。([GitHub][7])

这正是推荐采用独立 Review 层的原因。

---

# 十二、Review Skill 禁止行为

禁止：

```text
重新换主题
重新换品牌色
重新选择设计风格
把页面完全重做
擅自换 UI Library
重新设计整个信息架构
```

除非发现：

```text
P0 / P1 级严重问题
```

否则采用：

> Minimal Visual Modification

即最小视觉修改。

---

# 十三、Skill 权限等级

建立七级优先级：

```text
P0 业务正确性
↓
P1 平台规范
↓
P2 Accessibility / 可用性
↓
P3 项目既有 Design System
↓
P4 UX
↓
P5 视觉方向
↓
P6 装饰与动画
```

高等级永远覆盖低等级。

---

# 十四、冲突裁决总原则

统一使用：

```text
Business
>
Platform
>
Usability
>
Existing Design System
>
UX
>
Aesthetic Style
>
Decoration
```

中文：

```text
业务正确性
>
平台规范
>
可用性
>
现有设计体系
>
UX
>
审美风格
>
视觉装饰
```

---

# 十五、典型冲突案例

## 冲突 1：大标题

Frontend Design：

```text
建议 64px 大标题增强视觉冲击。
```

MiniProgram：

```text
首屏空间有限。
```

业务：

```text
用户需要尽快看到订单。
```

结果：

```text
降低标题尺寸。
订单优先。
```

---

## 冲突 2：大圆角

UI/UX 风格推荐：

```text
24px 圆角。
```

TDesign：

```text
现有组件 Radius 更克制。
```

结果：

```text
遵守 Design Token。
```

禁止为了“更现代”单独改变。

---

## 冲突 3：组件库

Frontend Design：

```text
自己制作 Gradient Button。
```

项目：

```text
已经使用 TDesign Button。
```

结果：

```text
继续使用 TDesign。
通过 Token 调整。
禁止建立第二套 Button。
```

---

# 十六、最重要的冲突预防机制：Single Owner

每个设计领域必须只有一个 Owner。

| 领域                  | Owner                    |
| ------------------- | ------------------------ |
| Business            | 项目需求                     |
| Platform            | China MiniProgram Design |
| Components          | TDesign                  |
| UX                  | UI/UX Pro Max            |
| Aesthetic Direction | Frontend Design          |
| Tokens              | 项目 Design System         |
| Final Quality       | UI Review                |

例如：

```text
Button 圆角
```

不允许：

```text
UIUX Pro Max 决定一次
Frontend Design 又决定一次
MiniProgram Skill 又决定一次
Review 再决定一次
```

应该：

```text
Design Token 是唯一 Owner。
```

---

# 十七、建立 Design Token Freeze

这是避免 AI 每次修改都“重新设计”的核心机制。

第一次确定：

```text
Primary Color
Background
Surface
Text Primary
Text Secondary
Border
Success
Warning
Danger

Radius S
Radius M
Radius L

Spacing XS
Spacing S
Spacing M
Spacing L
Spacing XL

Title
Subtitle
Body
Caption
```

例如：

```text
Primary    #0052D9
Background #F5F6F7
Surface    #FFFFFF

Radius-S   8rpx
Radius-M   16rpx
Radius-L   24rpx

Spacing-S  16rpx
Spacing-M  24rpx
Spacing-L  32rpx
```

确定以后：

```text
TOKEN_STATE = FROZEN
```

以后 Skill 不允许随意改变。

---

# 十八、什么时候允许修改 Token

只允许：

### 情况 A

品牌整体重新设计。

### 情况 B

发现 Accessibility 问题。

### 情况 C

现有 Token 明显不一致。

### 情况 D

用户明确要求换视觉体系。

其他情况：

```text
禁止改变 Global Token。
```

---

# 十九、组件优先规则

写 UI 前必须检查：

```text
项目现有组件
↓
TDesign
↓
微信原生组件
↓
自定义组件
```

不能反过来。

也就是：

```text
Existing
>
TDesign
>
Native
>
Custom
```

Custom Component 永远最后考虑。

---

# 二十、禁止 Skill 擅自安装 UI 框架

例如当前项目使用：

```text
TDesign
```

Frontend Design 不允许因为某个效果方便而加入：

```text
Vant
NutUI
WeUI Components
另一个 CSS Framework
```

必须保持：

```text
ONE PRIMARY COMPONENT SYSTEM
```

---

# 二十一、执行顺序

推荐完整工作流：

```text
STEP 1
理解业务

↓

STEP 2
UI/UX Pro Max
生成 UX + Design System 建议

↓

STEP 3
Frontend Design
选择视觉方向

↓

STEP 4
China MiniProgram Design
平台裁剪

↓

STEP 5
Freeze Design Tokens

↓

STEP 6
实现页面

↓

STEP 7
运行 / 截图

↓

STEP 8
MiniProgram UI Review

↓

STEP 9
最小修改

↓

STEP 10
再次 Review
```

---

# 二十二、禁止执行顺序

不要：

```text
Frontend Design
↓
直接写代码
↓
UIUX Pro Max 又重新设计
↓
TDesign 又改
↓
Review 再换主题
```

这会产生设计震荡。

---

# 二十三、建议的项目目录

对于 Codex，可以设计成：

```text
project/
│
├── .agents/
│   └── skills/
│       │
│       ├── ui-ux-pro-max/
│       │   └── ...
│       │
│       ├── frontend-design/
│       │   └── SKILL.md
│       │
│       ├── china-miniapp-design/
│       │   └── SKILL.md
│       │
│       └── miniapp-ui-review/
│           └── SKILL.md
│
├── docs/
│   │
│   ├── design-system.md
│   ├── ui-guidelines.md
│   └── ui-decisions.md
│
├── miniprogram/
│
├── app.json
├── project.config.json
└── AGENTS.md
```

UI/UX Pro Max 当前 Codex 模板本身采用 `.agents/skills/ui-ux-pro-max` 形式。([GitHub][1])

---

# 二十四、建议增加 design-system.md

这是 Skill 冲突管理最重要的项目文件之一。

内容记录：

```text
PRODUCT_TYPE:
B2B Cross-border Apparel Marketplace

PLATFORM:
WeChat Mini Program

PRIMARY_DESIGN_SYSTEM:
TDesign MiniProgram

VISUAL_DIRECTION:
Professional Industrial Commerce

BRAND_COLOR:
...

TYPOGRAPHY:
...

RADIUS:
...

SPACING:
...

ICON_SYSTEM:
TDesign Icons

AI_AESTHETIC_POLICY:
Restrained

INFORMATION_DENSITY:
Medium-High
```

所有 Skill 先读取这里。

---

# 二十五、建议增加 ui-decisions.md

记录关键设计决策。

例如：

```text
2026-09-03

Decision:
使用 TDesign MiniProgram 作为唯一主要组件体系。

Reason:
项目为微信 B2B 交易产品。

Rejected:
WeUI + TDesign 混用。

---

Decision:
首页不使用大型 Hero。

Reason:
用户核心任务是浏览订单。

---

Decision:
商品 / 订单卡片采用 Medium Density。

Reason:
用户需要快速比较数量、工艺、国家和交付时间。
```

以后 AI 不应该重新讨论这些已经确定的问题。

---

# 二十六、Skill Trigger 设计

## UI/UX Pro Max

触发：

```text
新页面
Design System
UX
配色
排版
信息结构
表单
交互
```

---

## Frontend Design

触发：

```text
新 UI
视觉升级
页面太普通
去 AI 味
重新设计
视觉方向
```

不要在：

```text
普通 Bug 修复
API
数据库
后端
业务逻辑
```

任务中启动。

---

## China MiniProgram Design

检测到：

```text
app.json
project.config.json
*.wxml
*.wxss
*.wxs
```

或用户提到：

```text
微信小程序
MiniProgram
```

自动启用。

---

## UI Review

只在：

```text
页面已经完成
或者已有截图
```

以后启用。

---

# 二十七、Review 输出等级

建议 Review 不直接说：

```text
好看 / 不好看
```

而采用：

```text
P0 Blocking
P1 Major
P2 Medium
P3 Polish
```

---

## P0

例如：

```text
按钮点不到
内容被胶囊覆盖
文字不可读
关键操作不可完成
```

必须修。

---

## P1

例如：

```text
主操作不明显
信息层级严重混乱
组件明显不统一
表单难以完成
```

必须修。

---

## P2

例如：

```text
间距不统一
字体层级一般
卡片密度稍低
颜色使用过多
```

推荐修。

---

## P3

例如：

```text
阴影可以更轻
图标位置差 2–4rpx
个别文字可优化
```

按收益决定。

---

# 二十八、禁止 Review 无限循环

最多：

```text
Build
↓
Review
↓
Fix
↓
Review
```

通常两轮足够。

如果第三轮还是：

```text
改 2rpx
再改 2rpx
又换阴影
又换圆角
```

必须停止。

防止 Agent 出现：

> UI perfection loop

---

# 二十九、页面设计前必须回答四个问题

所有 Skill 开始设计之前统一回答：

```text
1. 这个页面是谁使用？

2. 用户来到这里最主要要完成什么？

3. 页面最重要的信息是什么？

4. 页面最重要的操作是什么？
```

如果回答不出来：

```text
禁止先讨论渐变、阴影、圆角。
```

---

# 三十、肃联跨境小程序推荐 Profile

针对当前服装产业带跨境需求 / 企业接单场景：

```text
PRODUCT:
B2B Apparel Order Marketplace

PLATFORM:
WeChat Mini Program

USER A:
海外需求方 / 运营人员

USER B:
服装工厂

DESIGN CHARACTER:
Professional
Efficient
Trustworthy
Industrial
Modern

DESIGN SYSTEM:
TDesign MiniProgram

WEUI:
Interaction Reference

INFORMATION DENSITY:
Medium → Medium High

VISUAL EXPERIMENT:
Low

MOTION:
Low

DECORATION:
Low

CONTENT PRIORITY:
High
```

---

# 三十一、订单卡片推荐信息层级

不要：

```text
订单编号
品类
数量
工艺
国家
时间
状态
```

全部相同大小。

应该：

```text
服装品类                    状态

核心需求描述

数量     工艺     国家

交货日期

订单编号 / 发布时间

                         查看详情
                         立即接单
```

视觉权重大致：

```text
业务对象
>
状态 / 核心数据
>
交易条件
>
Metadata
```

---

# 三十二、视觉禁止项

当前项目默认禁止：

```text
❌ 紫蓝 AI Gradient
❌ Glassmorphism
❌ 大面积 Blur
❌ 巨型 Hero
❌ 超大标题
❌ 大量漂浮卡片
❌ 每一个模块都有 Shadow
❌ 每一个模块都有 Border
❌ 五颜六色 Tag
❌ Emoji 当正式 Icon
❌ 混用多个 Icon Library
❌ 超大圆角
❌ Desktop Dashboard 缩小到手机
❌ 无意义动画
❌ 无意义插画
❌ 为填空白而增加模块
```

---

# 三十三、允许的视觉个性

不是完全禁止设计感。

推荐在以下位置体现：

```text
品牌 Primary Color
订单状态设计
产业带图片
服装商品图片
首页 Header
数据标签
Empty State
少量 Illustration
```

原则：

> 一个页面最多 1–2 个强视觉元素。

---

# 三十四、最终 Skill 权限图

```text
                     PROJECT REQUIREMENTS
                             │
                             ▼
                    ┌─────────────────┐
                    │ Business Rules  │
                    └────────┬────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ China MiniProgram   │
                  │ Platform Authority  │
                  └──────────┬──────────┘
                             │
             ┌───────────────┴──────────────┐
             │                              │
             ▼                              ▼
     ┌───────────────┐             ┌────────────────┐
     │ UI/UX Pro Max │             │ Frontend Design│
     │ Knowledge     │             │ Taste          │
     └───────┬───────┘             └────────┬───────┘
             │                              │
             └──────────────┬───────────────┘
                            ▼
                    DESIGN SYSTEM
                            │
                            ▼
                     IMPLEMENTATION
                            │
                            ▼
                      UI REVIEW
                            │
                            ▼
                     MINIMAL FIX
```

---

# 三十五、最重要的设计原则

整个系统最终只需要记住：

```text
业务 > 平台 > 可用性 > 设计体系 > 审美 > 装饰
```

以及：

```text
一个领域只有一个 Owner。
```

和：

```text
一个项目只使用一个主要组件体系。
```

以及：

```text
Review 负责找问题，而不是重新设计。
```

---

# 三十六、最终推荐组合

正式推荐：

```text
CORE

UI/UX Pro Max
+
Anthropic Frontend Design
+
China MiniProgram Design
+
MiniProgram UI Review
```

其中：

```text
UI/UX Pro Max
= Design Intelligence

Frontend Design
= Taste

China MiniProgram Design
= Platform

MiniProgram UI Review
= Quality Assurance
```

微信小程序：

```text
PRIMARY COMPONENT SYSTEM:
TDesign MiniProgram
```

微信原生体验：

```text
REFERENCE:
WeUI
```

B2B 信息结构：

```text
REFERENCE:
Ant Design Principles
```

不要让三套组件库同时进入项目。

---

# 三十七、最终决策

对于当前微信小程序项目，不建议继续安装大量“审美 Skill”。

推荐控制在：

```text
3 个生成 / 约束 Skill
+
1 个 Review Skill
```

即：

```text
UI/UX Pro Max
Frontend Design
China MiniProgram Design
MiniProgram UI Review
```

通过 `design-system.md` 作为唯一视觉事实来源，通过 `ui-decisions.md` 保存长期设计决定，通过优先级系统解决冲突。

这样既能够利用热门 Skill 的设计能力，又不会因为 Skill 数量增加导致 UI 风格失控。

这里有一个很关键的变化：**TDesign 和 WeUI 不再作为两个与 Frontend Design 平级的 Skill**，而是被收进 `China MiniProgram Design` 作为平台规则来源。这是我最建议采用的结构，也最能防止 Codex 后期反复“越优化越乱”。TDesign 官方定位本身就是跨技术栈的一致性企业设计体系，而 WeUI 更适合作为微信原生视觉与交互基准。([GitHub][8])

下一步最有价值的是直接把这份架构落成 **4 个真正可安装的 `SKILL.md` + 一个 `AGENTS.md` + `design-system.md` 模板**；这样就不是说明文档，而是可以直接放进你现在小程序仓库让 Codex 使用的完整 Skill 套件。

[1]: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/cli/assets/templates/platforms/codex.json?utm_source=chatgpt.com "ui-ux-pro-max-skill/cli/assets/templates/platforms/codex.json at main · nextlevelbuilder/ui-ux-pro-max-skill · GitHub"
[2]: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/stack/.claude/commands/design-plan.md?utm_source=chatgpt.com "ui-ux-pro-max-skill/stack/.claude/commands/design-plan.md at main · nextlevelbuilder/ui-ux-pro-max-skill · GitHub"
[3]: https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md?ref=unitedpooh.top&utm_source=chatgpt.com "claude-code/plugins/frontend-design/skills/frontend-design/SKILL.md at main · anthropics/claude-code · GitHub"
[4]: https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/README.md?utm_source=chatgpt.com "claude-code/plugins/frontend-design/README.md at main · anthropics/claude-code · GitHub"
[5]: https://github.com/Tencent/tdesign/blob/main/README.md?utm_source=chatgpt.com "tdesign/README.md at main · Tencent/tdesign · GitHub"
[6]: https://github.com/tencent/weui-wxss?utm_source=chatgpt.com "GitHub - Tencent/weui-wxss: A UI library by WeChat official design team, includes the most useful widgets/modules. · GitHub"
[7]: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/stack/CLAUDE.md?utm_source=chatgpt.com "ui-ux-pro-max-skill/stack/CLAUDE.md at main · nextlevelbuilder/ui-ux-pro-max-skill · GitHub"
[8]: https://github.com/tencent/tdesign?utm_source=chatgpt.com "GitHub - Tencent/tdesign: Enterprise Design System · GitHub"
