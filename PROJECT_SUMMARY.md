# AAA Small App 当前项目总结

## 已完成

- 使用 uni-app + Vue 3 搭建前端，源码位于 `src/`。
- 配置 Flask 后端，源码位于 `services/api/`。
- 将当前阶段用不到的测试、数据库迁移、生产部署配置和技术文档移入 `shelved/`。
- 配置 VS Code 隐藏 `.venv`、`node_modules`、`dist`、`__pycache__` 等干扰目录。
- 已验证 H5 可以正常构建。
- 已验证 Flask 可以正常加载，健康接口返回 HTTP 200。

## 当前主要编辑位置

```text
src/                              前端页面、样式和交互
services/api/src/aaa_api/api/     Flask 后端接口
```

## 当前技术结构

```text
uni-app / Vue 3
       |
    HTTP API
       |
     Flask
       |
SQLite（本地开发）/ 腾讯云 MySQL（后续接入）
```

## 当前启动方式

前端 H5：

```bash
npm run dev:h5
```

Flask 后端：

```bash
cd services/api
uv run flask --app aaa_api:create_app run --debug
```

后端健康检查：

```text
http://127.0.0.1:5000/api/v1/health
```

## 搁置内容

`shelved/` 中保存了：

- 技术栈规划文档
- 后端自动化测试
- 数据库迁移配置
- 云数据库环境变量模板
- Gunicorn 生产部署入口

这些文件没有被删除，需要时可以恢复。

## 待决定事项

后端目前使用 Flask。后续可以根据项目需求决定：

- 继续使用 Flask：学习成本最低，适合当前技术基础。
- 改用 Express：前后端统一使用 JavaScript，但需要学习 Node.js 后端开发。
- 改用 FastAPI：适合后续 AI、RAG 和异步接口方向。
- 使用托管云后端：开发更快，但平台依赖更强。
