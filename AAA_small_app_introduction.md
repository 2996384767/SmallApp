# AAA Small App

<p align="center">
  A learning-oriented full-stack starter for H5 and WeChat Mini Program development.
</p>

<p align="center">
  <strong>English</strong> | <a href="#中文介绍">简体中文</a>
</p>

## Overview

AAA Small App is an evolving full-stack demo built to explore a practical workflow across H5, WeChat Mini Programs, REST APIs, and cloud databases. It combines a uni-app frontend with a Flask backend and Tencent Cloud MySQL.

The project began on August 24, 2026. Its current focus is connecting the frontend and backend through a small, understandable end-to-end feature before expanding into a larger application.

## Highlights

- One uni-app codebase for H5 and WeChat Mini Program builds
- Vue 3 and TypeScript frontend
- Modular Flask backend with an application factory and API blueprint
- Tencent Cloud MySQL connectivity through SQLAlchemy and PyMySQL
- Local database inspection with Navicat
- Reproducible Python environment managed by uv
- Service and database health-check endpoints
- Test data creation and database query scripts
- A Flask test page that renders cloud database records

## Architecture

```text
H5 / WeChat Mini Program
          |
      uni-app + Vue 3
          |
        HTTP API
          |
         Flask
          |
 Tencent Cloud MySQL
```

## Tech Stack

| Layer | Technologies |
| --- | --- |
| Frontend | uni-app, Vue 3, TypeScript, Vite |
| Backend | Python, Flask, Flask-SQLAlchemy |
| Database | Tencent Cloud MySQL 8.0, PyMySQL |
| Tooling | uv, npm, VS Code, Navicat |

## Project Structure

```text
AAA_small_app/
|-- src/                         uni-app frontend source
|-- services/api/
|   |-- src/aaa_api/             Flask application
|   |-- query_database.py        Inspect application data
|   |-- seed_test_data.py        Create sample records
|   |-- pyproject.toml           Python dependencies
|   `-- uv.lock                  Locked Python environment
|-- shelved/                     Configuration reserved for later stages
|-- package.json                 Frontend scripts and dependencies
`-- yzs_notebook.md              Development journal
```

## Quick Start

### Prerequisites

- Node.js LTS
- Python 3.11 or later
- uv
- A MySQL-compatible database

### Frontend

```bash
npm install
npm run dev:h5
```

For WeChat Mini Program development:

```bash
npm run dev:mp-weixin
```

Open `dist/dev/mp-weixin` in WeChat DevTools.

### Backend

```bash
cd services/api
uv sync
uv run flask --app aaa_api:create_app run --debug
```

Useful local URLs:

- API information: `http://127.0.0.1:5000/`
- Service health: `http://127.0.0.1:5000/api/v1/health`
- Database health: `http://127.0.0.1:5000/api/v1/health/database`
- Test data page: `http://127.0.0.1:5000/test`

## Environment Variables

Create `services/api/.env` and provide your own database credentials:

```dotenv
DB_HOST=your-database-host
DB_PORT=3306
DB_USER=your-application-user
DB_PASSWORD=your-password
DB_NAME=aaa_small_app
DATABASE_URL=mysql+pymysql://user:password@host:3306/aaa_small_app?charset=utf8mb4
SECRET_KEY=replace-with-a-random-secret
CORS_ORIGINS=http://localhost:5173
```

Never commit `.env` or production credentials to Git.

## Current Status

Completed:

- uni-app and Flask development environments
- Tencent Cloud MySQL connection
- Cloud database CRUD verification
- Navicat connection and data inspection
- uv virtual environment workflow
- Flask database-backed test page

Next:

- Connect the uni-app frontend to Flask APIs
- Display MySQL records in the Vue interface
- Add form submission and validation
- Replace test data with real domain models
- Restore migrations and automated tests as the project grows

## Development Notes

This repository is currently a learning project and an early-stage prototype. The implementation favors a clear development path over premature infrastructure complexity. Progress is recorded in `yzs_notebook.md`.

---

# 中文介绍

<p align="center">
  面向 H5 与微信小程序开发的全栈学习项目。
</p>

<p align="center">
  <a href="#aaa-small-app">English</a> | <strong>简体中文</strong>
</p>

## 项目简介

AAA Small App 是一个持续开发中的全栈演示项目，用于学习 H5、微信小程序、REST API 和云数据库之间的实际开发流程。项目采用 uni-app 构建前端，以 Flask 提供后端服务，并连接腾讯云 MySQL。

项目开始于 2026 年 8 月 24 日。当前目标是先完成一个清晰、可理解的前后端数据闭环，再逐步扩展实际业务功能。

## 项目特点

- 一套 uni-app 源码构建 H5 和微信小程序
- 使用 Vue 3 与 TypeScript 开发前端
- Flask Application Factory 与 API Blueprint 模块化后端
- 通过 SQLAlchemy 和 PyMySQL 连接腾讯云 MySQL
- 使用 Navicat 在本地管理和检查数据
- 使用 uv 管理可复现的 Python 虚拟环境
- 提供服务与数据库健康检查接口
- 提供测试数据生成和全库查询脚本
- 提供读取云数据库记录的 Flask 测试页面

## 系统架构

```text
H5 / 微信小程序
       |
 uni-app + Vue 3
       |
    HTTP API
       |
      Flask
       |
 腾讯云 MySQL
```

## 技术栈

| 层级 | 技术 |
| --- | --- |
| 前端 | uni-app、Vue 3、TypeScript、Vite |
| 后端 | Python、Flask、Flask-SQLAlchemy |
| 数据库 | 腾讯云 MySQL 8.0、PyMySQL |
| 工具 | uv、npm、VS Code、Navicat |

## 项目结构

```text
AAA_small_app/
|-- src/                         uni-app 前端源码
|-- services/api/
|   |-- src/aaa_api/             Flask 应用
|   |-- query_database.py        查询应用数据库
|   |-- seed_test_data.py        创建测试数据
|   |-- pyproject.toml           Python 依赖配置
|   `-- uv.lock                  Python 依赖锁文件
|-- shelved/                     后续阶段再恢复的工程配置
|-- package.json                 前端命令与依赖
`-- yzs_notebook.md              开发记录
```

## 快速开始

### 环境要求

- Node.js LTS
- Python 3.11 或更高版本
- uv
- MySQL 兼容数据库

### 启动前端

```bash
npm install
npm run dev:h5
```

编译微信小程序：

```bash
npm run dev:mp-weixin
```

随后使用微信开发者工具打开 `dist/dev/mp-weixin`。

### 启动后端

```bash
cd services/api
uv sync
uv run flask --app aaa_api:create_app run --debug
```

本地地址：

- API 信息：`http://127.0.0.1:5000/`
- 服务健康检查：`http://127.0.0.1:5000/api/v1/health`
- 数据库健康检查：`http://127.0.0.1:5000/api/v1/health/database`
- 测试数据页面：`http://127.0.0.1:5000/test`

## 环境变量

创建 `services/api/.env`，填入自己的数据库信息：

```dotenv
DB_HOST=数据库地址
DB_PORT=3306
DB_USER=业务账号
DB_PASSWORD=数据库密码
DB_NAME=aaa_small_app
DATABASE_URL=mysql+pymysql://用户名:密码@地址:3306/aaa_small_app?charset=utf8mb4
SECRET_KEY=替换为随机密钥
CORS_ORIGINS=http://localhost:5173
```

不要将 `.env` 或生产环境密码提交到 Git 仓库。

## 当前进度

已经完成：

- uni-app 与 Flask 开发环境
- 腾讯云 MySQL 连接
- 云数据库增删改查验证
- Navicat 数据库连接与检查
- uv 虚拟环境使用流程
- Flask 数据库测试页面

下一步：

- 连接 uni-app 前端与 Flask API
- 在 Vue 页面中展示 MySQL 数据
- 增加表单提交和数据校验
- 使用实际业务模型替换测试数据
- 随项目增长恢复数据库迁移和自动化测试

## 开发说明

本仓库目前是学习项目和早期原型。现阶段优先保证开发过程清晰易懂，暂不提前加入复杂基础设施。开发进度记录在 `yzs_notebook.md` 中。
