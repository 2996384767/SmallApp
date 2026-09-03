# AAA Small App 目标技术栈

## 0. 当前执行路线覆盖说明

从当前比赛 MVP 阶段开始，项目实现路径以根目录 [MINIPROGRAM_MVP_PATH.md](../MINIPROGRAM_MVP_PATH.md) 为准。先实现“肃联跨境：肃宁针纺产业带海外需求撮合与订单进度管理小程序 MVP”，不继续按早期 H5/uni-app 学习路线作为主线推进。

当前执行方案：

```text
微信原生小程序
    |
    | HTTPS / JSON
    v
Flask API + Flask/Jinja2 管理后台
    |
    v
本地 MariaDB 开发库 smallapp
```

核心业务链路：

```text
需求录入 -> 审核脱敏 -> 需求池发布 -> 工厂查看/筛选
-> 申请接单 -> 平台审核 -> 形成订单 -> 进度同步
```

旧技术路径中的 uni-app、H5、长期 NestJS、PostgreSQL、Redis、S3、FastAPI AI 服务等内容暂时降级为后续参考，不进入当前比赛 MVP 的第一优先级。当前不做支付、物流 API、海外买家端、ERP、AI 匹配和复杂微服务。

## 1. 项目目标

建设一个同时支持以下客户端的商用项目：

- Web/H5
- 微信小程序
- 未来可扩展的 App
- 多端共用同一套后端 API
- 开发环境与生产环境相互隔离
- 后期可在不同云平台之间迁移

## 2. 目标架构

```text
uni-app（Web/H5 + 微信小程序）
                 |
                 | HTTPS / JSON API
                 v
     主业务 API（初期 Flask，长期可选 NestJS）
          /      |       |
     SQL /       | S3    | 缓存/队列（按需）
        v         v       v
 PostgreSQL   对象存储   Redis
```

上图是长期目标，不代表第一版必须一次性实现全部组件。

## 3. 前端

### 技术选择

- uni-app
- Vue 3
- TypeScript
- Vite
- Pinia（出现跨页复杂状态时再加入）

前端负责页面展示、用户交互、表单基础校验和调用 HTTPS API。
前端不得保存数据库密码、S3 Secret Key、微信 `AppSecret` 等服务端密钥。

## 4. 后端

### 长期备选技术

- Node.js LTS
- NestJS
- TypeScript
- REST API
- OpenAPI/Swagger API 文档

初期使用 Flask 承担身份认证、权限、业务逻辑、参数校验、数据库读写、文件上传授权、
日志和异常处理。需要扩展 Node.js 企业后端能力时再学习 NestJS。无论使用哪种框架，
前端都不直接连接数据库。

## 5. 关系型数据库

### 长期升级选择：PostgreSQL

PostgreSQL 适合新项目，具备完整的 SQL、事务、约束、复杂查询和 JSON/JSONB 能力，
也容易在主流云平台获得托管服务。

适合保存用户、角色、商品、内容、订单、支付记录、评论、文件元数据和审计记录。

### MariaDB 与 PostgreSQL 的关系

两者都是开源关系型数据库，都使用 SQL、表、索引、关联查询、事务和约束。

MariaDB 属于 MySQL 体系，与 MySQL 的语法和工具高度兼容。PostgreSQL 是独立体系，
更注重 SQL 标准、复杂查询、扩展性和丰富的数据类型。

| 对比项 | MariaDB | PostgreSQL |
| --- | --- | --- |
| 体系 | MySQL 兼容体系 | 独立的 PostgreSQL 体系 |
| 现有经验 | 项目所有者已经熟悉 | 需要学习部分差异 |
| 常见场景 | 传统 Web 系统、MySQL 技术栈 | 新应用、复杂数据模型 |
| JSON | 支持 | JSONB 查询和索引能力更强 |
| 高级 SQL | 足够完整 | 通常更全面 |
| 两者迁移 | 需调整建表语句和 SQL | 需调整建表语句和 SQL |

选择原则：

- 全新项目，预期使用复杂查询或 JSON 数据：选择 PostgreSQL。
- 希望尽快交付，优先发挥现有 MariaDB 经验：选择 MariaDB。

MariaDB 是本项目的正式备选方案。NestJS 应通过 ORM 或 Repository 层访问数据库，
保持前端 API 不受数据库更换影响。

### 当前本地 MariaDB 开发环境

当前开发阶段暂时使用本地 MariaDB 作为关系型数据库，便于离线开发、快速重建测试数据、降低云资源成本，并减少开发期开放云数据库端口带来的安全风险。

#### 本地实例建议

| 项目 | 配置 |
| --- | --- |
| 数据库 | MariaDB |
| 部署位置 | 本机开发环境 |
| 主机 | 127.0.0.1 |
| 端口 | 3306 |
| 数据库名 | smallapp |
| 字符集 | utf8mb4 |
| 排序规则 | utf8mb4_general_ci |
| 连接方式 | Flask 通过 SQLAlchemy + PyMySQL 连接 |

#### 后端环境变量

本地开发时在 `services/api/.env` 中配置 MariaDB 连接信息：

```dotenv
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_local_password
DB_NAME=smallapp
DATABASE_URL=mysql+pymysql://root:your_local_password@127.0.0.1:3306/smallapp?charset=utf8mb4
SECRET_KEY=replace-with-a-random-secret
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

`services/api/.env` 不提交到 Git。密码包含 `@`、`#`、`:`、`/` 等字符时，`DATABASE_URL` 中需要使用 URL 编码。

#### 本地建库参考

```sql
CREATE DATABASE IF NOT EXISTS smallapp
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

-- 当前临时使用本地 root 账号开发。
-- 后续正式开发建议改为专用业务账号，并只授予 smallapp 库权限。
```

前端不得直接连接 MariaDB，也不得保存数据库账号、密码或连接串。数据库连接信息只放在后端 `services/api/.env` 中，由 Flask 统一访问数据库并对前端暴露 HTTP API。

<!--
### 暂停使用：腾讯云 MySQL 开发环境

以下云数据库配置暂时保留为备注，当前开发阶段先替换为本地 MariaDB。后续需要云端联调或部署时再恢复。

#### 实例信息

| 项目 | 配置 |
| --- | --- |
| 地域 | 中国香港 |
| 可用区 | 香港二区 |
| 数据库版本 | MySQL 8.0 |
| 引擎 | InnoDB |
| 架构 | 单节点（云盘） |
| 实例规格 | 标准型 1核 / 2000MB |
| 磁盘 | SSD 云硬盘 20GB |
| 数据保护空间 | 1GB |
| 计费方式 | 按量计费 |
| MySQL 端口 | 3306 |
| 字符集 | UTF8 / UTF8_GENERAL_CI |
| 表名大小写敏感 | 关闭 |
| 参数模板 | 高稳定性模板（推荐） |

#### 网络配置

| 项目 | 配置 |
| --- | --- |
| VPC | aaa-hk-vpc |
| VPC 网段 | 10.0.0.0/16 |
| 子网 | aaa-hk-subnet |
| 子网网段 | 10.0.0.0/24 |
| 安全组 | aaa-hk-mysql-sg |
| 开发期入站规则 | all -> TCP:3306 -> 允许 |

#### 安全说明

开发期为了本地联调，安全组临时允许访问 TCP 3306。该规则仅用于临时开发，正式部署后应收紧为固定 IP 白名单，或改为后端服务通过同 VPC 内网访问数据库。

前端不得直接连接 MySQL，也不得保存数据库账号、密码或连接串。数据库连接信息只放在后端 `services/api/.env` 中，并通过 `DATABASE_URL` 或拆分的 `DB_HOST`、`DB_PORT`、`DB_USER`、`DB_PASSWORD`、`DB_NAME` 提供给 Flask 使用。

#### 费用参考

当前参考费用约为：

```text
0.03490289 USD / 小时
约 25.13 USD / 月（持续运行 30 天）
```

费用会随腾讯云实际计费规则、运行时长、磁盘、备份和网络策略变化。开发期如果长时间不用，可以考虑释放或停止相关资源以降低成本。
-->

## 6. S3 兼容对象存储

对象存储用于保存用户头像、商品图片、视频、PDF、表格、附件、导出文件和备份。

可选服务：

- Amazon S3
- 阿里云 OSS
- 腾讯云 COS
- MinIO
- Sealos Object Storage

大文件通常不直接存入关系型数据库。数据库保存文件元数据：

```text
files
-----
id
owner_id
object_key
public_url
mime_type
size_bytes
created_at
```

上传流程：

```text
1. uni-app 向 NestJS 申请上传。
2. NestJS 校验用户，生成短期有效的签名地址。
3. uni-app 将文件上传到对象存储。
4. NestJS 将 object key 和文件信息写入数据库。
5. API 返回公开地址或短期有效的下载地址。
```

存储桶默认为私有，只有确定对外公开的资源才开启公开读取。

## 7. Redis（按需加入）

第一版不必立即使用 Redis。出现验证码过期、API 限流、Session、热点数据缓存、
分布式锁或后台任务时再加入。

关系型数据库始终是正式数据源，Redis 只保存临时或可重建的数据。

## 8. 部署

- 使用 Sealos 或其他托管云平台部署 NestJS 容器。
- 使用托管 PostgreSQL，也可替换为 MariaDB。
- 使用 S3 兼容对象存储。
- 有明确需求时才启用 Redis。
- Web 端和 API 都使用 HTTPS 自定义域名。

```text
https://www.example.com       Web/H5
https://api.example.com       NestJS API
https://files.example.com     公开文件或 CDN
```

微信小程序上线前，必须将 API 和文件域名登记为合法服务器域名。

## 9. 环境隔离

```text
开发环境：
- 开发 API
- 开发数据库
- 开发对象存储桶

生产环境：
- 生产 API
- 生产数据库
- 生产对象存储桶
```

开发环境不得直接修改生产数据。密钥和环境差异通过环境变量管理：

```text
DATABASE_URL
S3_ENDPOINT
S3_BUCKET
S3_ACCESS_KEY
S3_SECRET_KEY
JWT_SECRET
WECHAT_APP_ID
WECHAT_APP_SECRET
```

只有可对外公开的前端变量才能使用 `VITE_` 前缀。

## 10. 未来目录结构

当后端开发正式开始后，可转换为 monorepo：

```text
AAA_small_app/
|-- apps/
|   `-- client/          uni-app 前端
|-- services/
|   |-- api/             Flask 主业务 API
|   `-- ai/              FastAPI AI 服务（按需）
|-- infra/
|   `-- docker/          Docker 与部署配置
|-- docs/
|   `-- openapi/         跨语言 API 契约
`-- README.md
```

在正式开始后端之前，不重构现有前端目录，项目继续从根目录运行。

## 11. 基于现有能力的最小学习方案

### 已掌握的技术

```text
HTML + CSS + JavaScript
Python + Flask
MariaDB
```

第一版不替换 Flask 和 MariaDB，先将已有技术完善成可上线架构：

```text
uni-app + Vue 3
        |
        | REST API / JSON
        v
   Flask 模块化单体
      |          |
      | SQL      | 出现文件上传时再加入
      v          v
   MariaDB    S3 对象存储
```

### 第一阶段：只学习项目必需内容

1. **Vue 3 基础**：组件、`ref`、`computed`、事件、表单、生命周期和 props。
2. **uni-app 基础**：`pages.json`、路由、页面生命周期、`uni.request`、`uni.uploadFile`、本地缓存和条件编译。
3. **REST API**：GET/POST/PATCH/DELETE、HTTP 状态码和统一 JSON 返回格式。
4. **Flask 工程化**：Application Factory、Blueprint、分环境配置、统一异常处理和日志。
5. **MariaDB 工程化**：SQLAlchemy ORM、Alembic/Flask-Migrate、索引、事务和备份。
6. **基础安全**：密码哈希、JWT/会话、权限检查、参数校验、CORS 和密钥环境变量。
7. **基础测试**：使用 pytest 覆盖登录、权限和核心 API。

当前 TypeScript 模板可以继续使用。初期只需学习基本类型、接口、可选属性和函数参数，
不需要先系统学完 TypeScript。

### 第二阶段：具备上线能力

1. 给前端和 Flask 配置开发、测试、生产环境。
2. 学习 Dockerfile 和 Docker Compose，能够在本地启动 Flask + MariaDB。
3. 将 Flask 部署到 Sealos、Render 或国内托管云平台。
4. 配置 HTTPS、域名、数据库备份、错误日志和基础监控。
5. 出现头像、附件等功能时，学习 S3 预签名上传。
6. 使用 GitHub Actions 自动执行测试和构建镜像。

### 第三阶段：出现真实需求后再升级

- 需要 JSONB、pgvector 或更复杂的数据能力时，再评估迁移 PostgreSQL。
- 出现验证码、热点缓存、限流或后台任务时，再加入 Redis。
- 确实依赖 Python AI 生态、独立扩缩容或长耗时推理时，再拆出 FastAPI AI 服务。
- 出现多个独立服务、多人协作和明确扩缩容需求时，再学习 Kubernetes。
- NestJS 作为后端岗位扩展技术学习，不为了更换技术而重写已经稳定的 Flask 业务。

### 最小学习结论

```text
现在必学：Vue 3 + uni-app + REST API + Flask 工程化 + SQLAlchemy + Docker
开发中再学：TypeScript 基础 + 身份认证 + pytest + S3 + CI/CD
暂不必学：NestJS + PostgreSQL + Redis + FastAPI + Kubernetes + 微服务
```

## 12. 长期企业化与 AI 方向设想

项目应先保持模块化单体，不为展示技术而过早拆分微服务。

```text
uni-app
   |
   v
主业务 API（初期 Flask，长期可选 NestJS）
   |-- MariaDB / PostgreSQL
   |-- S3 对象存储
   |-- Redis（按需）
   `-- FastAPI AI 服务（按需）
          |-- 文档解析与切分
          |-- Embedding 与检索
          |-- RAG 和引用来源
          `-- 评测、延迟、Token 和费用记录
```

AI 第一版优先考虑 PostgreSQL + pgvector，不同时引入独立向量数据库和 Neo4j。
只有存在明确图关系查询时才加入 Neo4j。

就业展示应优先完成：

- 可演示的完整业务流程。
- 登录、Token 刷新、RBAC 权限和安全校验。
- 数据库迁移、事务、索引和备份。
- S3 预签名上传和私有文件授权。
- 单元测试、集成测试和 CI/CD。
- 错误日志、健康检查、性能数据和可观测性。
- RAG 评测集、检索效果对比和答案引用。
- 清晰的 README、架构决策记录和线上演示。

Sealos 只是托管平台。只有实际配置并能解释 Deployment、Service、Ingress、Secret、
健康检查、资源限制、滚动更新和回滚时，才应将 Kubernetes 写成项目能力。

## 13. 实施顺序

1. 使用模拟数据完成 uni-app 主要页面。
2. 定义 API 契约和第一版数据库结构。
3. 创建模块化 Flask 后端和 MariaDB 开发数据库。
4. 加入身份认证和数据库迁移管理。
5. 在首个文件上传功能开发时接入对象存储。
6. 出现明确需求时再加入 Redis。
7. 创建独立的生产资源并部署。
8. 配置域名、HTTPS、监控、备份和上线检查。

## 14. 当前结论

```text
初期前端：   uni-app + Vue 3 + TypeScript 基础
初期后端：   Flask + Python
初期数据库： MariaDB
文件存储： S3 兼容对象存储
缓存：       Redis（按需）
AI 服务：    FastAPI + RAG（按需拆分）
长期后端备选：NestJS + TypeScript
长期数据库备选：PostgreSQL + pgvector
部署：       Docker + Sealos/国内托管云平台
工程：       pytest + GitHub Actions + 日志/监控
代码管理： GitHub
```
