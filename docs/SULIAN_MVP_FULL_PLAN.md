可以直接按一个“**比赛可演示的真实 MVP**”来做，不做完整跨境电商平台，而是把计划书已经明确的核心链路真正跑通：

> **需求录入 → 审核脱敏 → 需求池发布 → 工厂查看/筛选 → 申请接单 → 平台审核 → 形成订单 → 进度同步。**

这与计划书规定的“需求录入、需求展示、工厂查看、接单确认、进度同步”一致，而且明确不做在线支付、不泄露客户隐私。

# 一、最终技术方案

建议直接采用：

```text
┌─────────────────────────────┐
│          微信小程序            │
│                             │
│ 登录  需求池  需求详情  我的订单 │
└──────────────┬──────────────┘
               │ HTTPS / JSON
               ↓
┌─────────────────────────────┐
│          Flask API           │
│                             │
│ 用户认证 / 需求 / 接单 / 订单   │
│ 后台管理 / 图片 / 状态管理      │
└──────────────┬──────────────┘
               │
               ↓
┌─────────────────────────────┐
│           MySQL             │
│                             │
│ factory                     │
│ demand                      │
│ demand_application          │
│ orders                      │
│ order_progress              │
│ admin                       │
└─────────────────────────────┘

               ↑
               │
┌─────────────────────────────┐
│        Web 管理后台           │
│                             │
│ 发布需求 / 审核接单 / 更新进度 │
└─────────────────────────────┘
```

你们现在不需要微服务、Redis、消息队列、Spring Cloud之类的东西。

**微信小程序 + Flask + MySQL + 简单 Web 后台**就足够。

---

# 二、小程序端具体做什么

我建议底部只设置三个 Tab：

```text
需求大厅      我的接单      我的
```

## 1. 登录页

第一版不用做复杂微信授权。

直接使用：

```text
企业账号
密码
```

登录成功后后端返回 Token。

例如：

```json
{
  "code": 200,
  "token": "xxxx",
  "factory": {
    "id": 3,
    "name": "肃宁春蕾制衣厂"
  }
}
```

小程序保存：

```javascript
wx.setStorageSync('token', res.data.token)
```

比赛测试时提前准备：

```text
factory001 / 123456
factory002 / 123456
factory003 / 123456
```

这样现场不容易翻车。

---

# 三、核心页面 1：需求大厅

这是整个小程序最重要的页面。

顶部：

```text
肃联跨境

海外采购需求

[全部] [T恤] [卫衣] [POLO]
```

增加筛选：

```text
国家 ▼
品类 ▼
工艺 ▼
交期 ▼
```

需求卡片：

```text
────────────────────────

DN260903001

🇹🇭 泰国

圆领纯棉印花T恤

1200 件 · 数码印花 · 25天

订单状态：可接单

          [查看详情]

────────────────────────
```

PPT里本来就规定了企业按照**品类、工艺、数量、交期**筛选需求，以及查看“可接需求”。

API：

```http
GET /api/demands
```

筛选：

```http
GET /api/demands?category=T恤
GET /api/demands?country=泰国
GET /api/demands?craft=数码印花
```

返回：

```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "demand_no": "DN260903001",
      "country": "泰国",
      "category": "圆领T恤",
      "quantity": 1200,
      "craft": "数码印花",
      "delivery_days": 25,
      "cover_image": "/uploads/001.jpg",
      "status": "published"
    }
  ]
}
```

---

# 四、核心页面 2：需求详情

点进去展示：

```text
← 海外采购需求

[服装图片]

需求编号
DN260903001

目的市场
泰国

产品品类
圆领印花T恤

采购数量
1200件

面料
180g纯棉

工艺
数码印花

颜色
黑 / 白 / 蓝

尺码
S / M / L / XL / XXL

交货周期
25天

特殊要求
领口无感标签

────────────────

✓ 客户信息已经脱敏

[申请接单]
```

这里建议至少保留这些字段：

| 字段       |  是否必须 |
| -------- | ----: |
| 需求编号     |    必须 |
| 国家       |    必须 |
| 产品品类     |    必须 |
| 产品图片     |    必须 |
| 数量       |    必须 |
| 工艺       |    必须 |
| 交期       |    必须 |
| 面料       |    推荐 |
| 颜色       |    推荐 |
| 尺码       |    推荐 |
| 特殊要求     |    推荐 |
| 客户姓名     |   不展示 |
| Email    |   不展示 |
| WhatsApp |   不展示 |
| 客户公司名    | 原则上脱敏 |

这尤其符合计划书“我方审核、翻译、脱敏后统一发布”和工厂不能直接获取客户隐私的设计。

---

# 五、核心页面 3：申请接单

工厂点击：

```text
申请接单
```

不要立刻变成“订单归你”。

弹窗：

```text
申请承接该需求？

需求编号：
DN260903001

产品：
圆领印花T恤

数量：
1200件

提交后将由肃联跨境工作人员
审核您的接单申请。

       取消    确认申请
```

请求：

```http
POST /api/demands/1/apply
```

Request：

```json
{
  "factory_id": 3
}
```

后台创建：

```text
demand_application
```

状态：

```text
pending
```

返回：

```json
{
  "code": 200,
  "message": "接单申请已提交"
}
```

这一点很重要，因为计划书明确是企业**自主申请接单 + 项目方人工辅助审核/牵线**，并不是完全自动抢单。

---

# 六、核心页面 4：我的接单

页面：

```text
我的接单

[全部] [待审核] [已通过] [已完成]


DN260903001

圆领印花T恤
1200件

申请时间
2026-09-03 15:23

状态
待平台审核

────────────────

DN260828005

基础卫衣
800件

状态
已通过

        [查看订单]
```

API：

```http
GET /api/my/applications
```

这样就解决 PPT 中：

> 系统记录接单历史，避免重复冲突。

后端也必须加唯一约束：

```text
factory_id + demand_id
```

避免一个厂家连续点十次。

---

# 七、核心页面 5：订单详情 / 进度

管理员批准以后：

```text
申请
↓
正式订单
```

工厂进入：

```text
订单详情

订单编号
OD260903001

产品
1200件圆领印花T恤

────────────────

订单进度

● 接单确认
  09-03 16:30

● 协议确认
  09-04 10:20

● 生产中
  当前节点

○ 集货质检

○ 报关

○ 国际运输

○ 海外仓

○ 已完成
```

建议只显示“状态”，第一版不用真的接物流 API。

管理员后台点一下：

```text
生产中 → 集货 → 报关 → 国际运输
```

小程序刷新之后自动变化。

计划书本身要求后续做到**订单状态可视、进度可查**。

---

# 八、后台一定要做

后台不用专门再开发 React/Vue。

为了比赛速度，我反而建议：

```text
Flask + Jinja2 + Bootstrap
```

做一个简单 Web 管理后台。

访问：

```text
https://你的域名/admin
```

首页：

```text
肃联跨境管理后台

今日需求       12
接单申请        5
执行订单        8
合作工厂       10
```

左侧：

```text
需求管理
接单管理
订单管理
工厂管理
```

---

# 九、后台——需求管理

页面：

```text
需求管理

[新增需求]

编号          国家   产品        数量    状态

DN001        泰国   印花T恤     1200   已发布
DN002        乌兹   卫衣         800   待审核
```

管理员可以：

```text
新增
修改
审核
发布
下架
```

新增需求：

```text
需求编号
国家
品类
产品名称
产品图片
数量
工艺
面料
颜色
尺码
交期
特殊要求
```

这正好对应真实业务：

```text
海外需求表
↓
工作人员翻译
↓
工作人员脱敏
↓
录入后台
↓
发布小程序
```

而不是让国外客户直接操作微信小程序。

---

# 十、后台——接单审核

例如：

```text
需求：

DN260903001
1200件圆领T恤

接单申请：

────────────────
肃宁春蕾制衣厂

主营：
T恤 / 卫衣

工艺：
印花 / 绣花

申请时间：
15:21

[拒绝]       [确认承接]
────────────────

肃宁华兴针织

主营：
针织衫 / T恤

[拒绝]       [确认承接]
```

点击：

```text
确认承接
```

后端：

```text
application.status = approved
```

然后：

```text
其他申请
=
rejected
```

再自动生成：

```text
order
```

---

# 十一、数据库直接这样设计

## `factory`

```sql
CREATE TABLE factory (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,

    factory_name VARCHAR(100) NOT NULL,

    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,

    contact_name VARCHAR(50),
    contact_phone VARCHAR(30),

    category VARCHAR(255),
    craft VARCHAR(255),

    status TINYINT DEFAULT 1,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## `demand`

```sql
CREATE TABLE demand (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,

    demand_no VARCHAR(30) UNIQUE NOT NULL,

    country VARCHAR(50),
    category VARCHAR(100),
    product_name VARCHAR(150),

    quantity INT,
    craft VARCHAR(150),

    fabric VARCHAR(150),
    colors VARCHAR(255),
    sizes VARCHAR(255),

    delivery_days INT,

    special_requirement TEXT,

    cover_image VARCHAR(500),

    status VARCHAR(30) DEFAULT 'draft',

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

状态：

```text
draft
published
matched
closed
```

---

## `demand_application`

这是最关键的一张表。

```sql
CREATE TABLE demand_application (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,

    demand_id BIGINT NOT NULL,
    factory_id BIGINT NOT NULL,

    status VARCHAR(30) DEFAULT 'pending',

    applied_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    UNIQUE KEY uk_factory_demand(factory_id, demand_id)
);
```

状态：

```text
pending
approved
rejected
```

---

# 十二、正式订单表

```sql
CREATE TABLE orders (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,

    order_no VARCHAR(30) UNIQUE NOT NULL,

    demand_id BIGINT NOT NULL,
    factory_id BIGINT NOT NULL,

    status VARCHAR(50),

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
```

---

# 十三、订单进度

```sql
CREATE TABLE order_progress (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,

    order_id BIGINT NOT NULL,

    stage VARCHAR(50),

    description VARCHAR(255),

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

例如：

```text
order_id = 1

接单确认
协议确认
生产中
集货质检
报关
国际运输
海外仓
完成
```

---

# 十四、管理员表

```sql
CREATE TABLE admin (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,

    username VARCHAR(50) UNIQUE,
    password_hash VARCHAR(255),

    name VARCHAR(50),

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

所以比赛第一版实际上就 **5 张业务表 + 1 张管理员表**。

---

# 十五、Flask API 建议直接固定

```text
认证
POST   /api/login

需求
GET    /api/demands
GET    /api/demands/<id>

接单
POST   /api/demands/<id>/apply
GET    /api/my/applications

订单
GET    /api/my/orders
GET    /api/orders/<id>
GET    /api/orders/<id>/progress


后台
POST   /api/admin/login

GET    /api/admin/demands
POST   /api/admin/demands
PUT    /api/admin/demands/<id>
DELETE /api/admin/demands/<id>

GET    /api/admin/applications
POST   /api/admin/applications/<id>/approve
POST   /api/admin/applications/<id>/reject

GET    /api/admin/orders
PUT    /api/admin/orders/<id>/status
```

整个 API 控制在 **15 个左右**，非常合适。

---

# 十六、小程序目录直接这样搭

```text
miniprogram/
│
├── pages/
│   │
│   ├── login/
│   │   ├── login.wxml
│   │   ├── login.wxss
│   │   ├── login.js
│   │   └── login.json
│   │
│   ├── demands/
│   │   ├── demands.wxml
│   │   ├── demands.wxss
│   │   ├── demands.js
│   │   └── demands.json
│   │
│   ├── demand-detail/
│   │
│   ├── applications/
│   │
│   ├── orders/
│   │
│   ├── order-detail/
│   │
│   └── profile/
│
├── utils/
│   ├── request.js
│   └── auth.js
│
├── images/
│
├── app.js
├── app.json
└── app.wxss
```

不要一开始搞复杂组件化。

先把页面跑起来。

---

# 十七、后端项目结构

建议：

```text
backend/
│
├── app.py
│
├── config.py
│
├── models/
│   ├── factory.py
│   ├── demand.py
│   ├── application.py
│   ├── order.py
│   └── admin.py
│
├── routes/
│   ├── auth.py
│   ├── demand.py
│   ├── application.py
│   ├── order.py
│   └── admin.py
│
├── templates/
│   └── admin/
│
├── static/
│
├── uploads/
│
└── requirements.txt
```

---

# 十八、图片怎么处理

你朋友说：

> “可以盗他这个衣服的图片。”

技术上当然能保存，但不建议真的这么做。

直接让合作厂：

```text
提供10～20张授权商品图片
```

然后管理员新增需求：

```text
上传图片
↓
Flask
↓
uploads/
↓
数据库保存图片 URL
↓
小程序显示
```

比赛阶段完全够。

后期再换：

```text
腾讯云 COS
```

---

# 十九、部署方案

正式比赛版建议：

```text
微信小程序
     ↓
HTTPS
     ↓
腾讯云服务器
     ↓
Nginx
     ↓
Gunicorn
     ↓
Flask
     ↓
MySQL
```

域名例如：

```text
api.sulianxxx.cn
```

然后：

```text
https://api.sulianxxx.cn/api/demands
```

微信公众平台后台添加：

```text
request合法域名
```

必须 HTTPS。

如果只是早期开发：

```text
开发者工具
↓
不校验合法域名
↓
本地 Flask
```

先调通即可。

---

# 二十、开发顺序非常重要

不要按照页面一个一个慢慢美化。

建议按照：

```text
第一阶段
数据库
↓
Flask API
↓
Postman测试


第二阶段
登录
↓
需求列表
↓
需求详情


第三阶段
申请接单
↓
我的接单


第四阶段
后台
↓
审核申请


第五阶段
订单
↓
订单进度


第六阶段
UI美化
↓
真实服装图片
↓
测试数据


第七阶段
服务器部署
↓
真机测试
```

---

# 二十一、按目前时间，我建议这样排

如果从现在 **9 月 3 日**开始，目标不是做到10月，而应该争取：

### 9月3～5日

完成：

```text
数据库
Flask项目
用户登录
需求CRUD
```

### 9月6～8日

完成：

```text
需求大厅
筛选
详情
图片展示
```

### 9月9～10日

完成：

```text
申请接单
我的接单
防止重复申请
```

### 9月11～12日

完成：

```text
后台
申请审核
生成订单
```

### 9月13～14日

完成：

```text
订单进度
后台修改进度
```

### 9月15～17日

完成：

```text
UI
服装图片
测试数据
异常处理
```

### 9月18日前

做到：

> **一台真实手机上可以完整演示整个业务流程。**

这样即使比赛要求突然提前，也有东西可交。

---

# 二十二、最终比赛演示应该是这样的

评委面前拿两个设备最好。

**电脑：运营管理后台**

新增一个泰国需求：

```text
圆领印花T恤
1200件
25天
```

点击：

```text
发布
```

然后拿手机：

```text
打开肃联跨境
↓
刷新
↓
看到刚发布的需求
↓
打开详情
↓
查看衣服图片
↓
点击申请接单
```

再回电脑：

```text
出现：
春蕾制衣厂申请接单
```

管理员：

```text
确认承接
```

手机重新进入：

```text
我的接单
↓
已通过
↓
进入订单详情
```

电脑修改：

```text
生产中
↓
集货质检
```

手机刷新：

```text
订单进度同步变化
```

这一套跑下来可能只需要 **2～3分钟**，但比放几十张“AI生成界面图”有说服力得多。

---

## 最后把项目边界定死

这次比赛版本的实际产品应该定义成：

> **“肃联跨境——肃宁针纺产业带海外需求撮合与订单进度管理小程序 MVP”**

核心不是“卖衣服”，也不是“中国版阿里国际站”，而是：

```text
海外需求
      ↓
平台审核脱敏
      ↓
需求池
      ↓
工厂申请
      ↓
人工审核
      ↓
订单形成
      ↓
进度可视
```

而**支付、报关系统、物流 API、海外买家端、AI 匹配、ERP、自动对接沧州平台全部留到后续版本**。计划书自己也采用了“前期轻量、后期升级”的策略，因此这个范围和现有商业计划是相容的。

按你的现有技术路线，直接使用 **微信原生小程序 + Flask + MySQL** 是最省时间的做法，没有必要临时换技术栈。

下一步最适合直接进入**数据库建表 + Flask API 骨架**，因为这两个确定以后，小程序页面基本就是照接口往上接。
