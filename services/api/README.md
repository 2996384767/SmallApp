# Flask 后端

当前开发数据库：本地 MariaDB。

首次配置：

```bash
cp .env.example .env
```

然后编辑 `.env` 中的 `DB_PASSWORD` 和 `DATABASE_URL`。

启动：

```bash
uv sync
uv run flask --app aaa_api:create_app run --debug
```

页面：<http://127.0.0.1:5000/test>

初始化 MVP 演示数据库：

```bash
python init_mvp_demo_data.py
```

该脚本会创建 `factory`、`demand`、`demand_application`、`orders`、`order_progress`、`admin` 六张表，并为每张表准备 100 条演示数据。
