# 搁置内容说明

这里保存当前开发阶段暂时用不到、但上线或完善工程时还会用到的文件。

## 已搁置

- `../passtime file/TECH_STACK.md`：长期技术栈设想，已归档到旧说明文档文件夹。
- `backend/.env.example`：连接本地 MariaDB 和配置后端环境变量时使用。
- `backend/migrations/`：开始设计正式数据表后恢复到 `services/api/migrations/`。
- `backend/tests/`：需要自动化测试时恢复到 `services/api/tests/`。
- `backend/wsgi.py`：使用 Gunicorn 部署 Flask 时恢复到 `services/api/wsgi.py`。

这些文件不参与目前的 Vue/uni-app 页面开发和 Flask 本地启动。

## 当前常用位置

```text
AAA_small_app/
|-- src/                       前端页面和样式，主要编辑这里
|-- services/api/src/aaa_api/  Flask 接口，编写后端时编辑这里
|-- package.json               前端依赖和启动命令
|-- services/api/pyproject.toml 后端依赖
`-- shelved/                   暂时不用的内容
```

## 当前启动命令

前端：

```bash
npm run dev:h5
```

后端：

```bash
cd services/api
uv run flask --app aaa_api:create_app run --debug
```
