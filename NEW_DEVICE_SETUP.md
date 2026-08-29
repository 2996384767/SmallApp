# AAA Small App 新设备配置与启动

本文用于在更换设备后快速恢复 AAA Small App 的开发环境。

## 1. 项目结构

```text
AAA_small_app/
|-- src/                         uni-app / Vue 3 前端源码
|-- services/api/
|   |-- src/aaa_api/             Flask 后端源码
|   |-- query_database.py        查询云数据库
|   |-- seed_test_data.py        创建测试数据
|   |-- pyproject.toml           Python 依赖配置
|   `-- uv.lock                  Python 依赖锁文件
|-- package.json                 前端依赖和命令
|-- README.md                    英文项目介绍
`-- README.zh-CN.md              中文项目介绍
```

运行关系：

```text
uni-app / Vue 3 前端
        |
     HTTP API
        |
      Flask
        |
  腾讯云 MySQL
```

## 2. 克隆项目

```bash
cd ~/Desktop
git clone https://github.com/2996384767/SmallApp.git AAA_small_app
cd AAA_small_app
```

确认仓库状态：

```bash
git status
git remote -v
```

## 3. 准备基础环境

新设备需要安装：

- Git
- Node.js LTS 与 npm
- Python 3.11 或更高版本
- uv
- VS Code
- 微信开发者工具（开发微信小程序时使用）
- Navicat（可选，用于查看云数据库）

确认命令可用：

```bash
git --version
node --version
npm --version
python3 --version
uv --version
```

## 4. 恢复前端环境

在项目根目录执行：

```bash
npm install
```

`node_modules/` 不上传 Git，由 `package.json` 和 `package-lock.json` 在新设备重建。

启动 H5：

```bash
npm run dev:h5
```

编译微信小程序：

```bash
npm run dev:mp-weixin
```

随后使用微信开发者工具打开：

```text
dist/dev/mp-weixin
```

## 5. 恢复 Flask 虚拟环境

```bash
cd services/api
uv sync
```

uv 会根据 `pyproject.toml` 和 `uv.lock` 自动创建：

```text
services/api/.venv
```

推荐直接使用 `uv run`，不必手动激活虚拟环境。

如需手动激活：

```bash
source .venv/bin/activate
```

退出虚拟环境：

```bash
deactivate
```

## 6. 重建后端环境变量

`services/api/.env` 包含数据库密码，因此不会上传 GitHub。新设备必须重新创建：

```bash
cd services/api
cp ../../shelved/backend/.env.example .env
```

编辑 `.env`：

```dotenv
DB_HOST=腾讯云数据库外网或内网地址
DB_PORT=数据库端口
DB_USER=数据库业务账号
DB_PASSWORD=数据库密码
DB_NAME=aaa_small_app
DATABASE_URL=mysql+pymysql://用户名:URL编码后的密码@数据库地址:端口/aaa_small_app?charset=utf8mb4
SECRET_KEY=替换为随机密钥
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

注意：

- 不要将 `.env` 提交到 GitHub。
- 密码含有 `@`、`#`、`:`、`/` 等字符时，`DATABASE_URL` 中需要进行 URL 编码。
- 正式上线前应使用只拥有 `aaa_small_app` 权限的业务账号。

## 7. 配置腾讯云 MySQL 网络

数据库位于腾讯云，新设备的公网 IP 可能与旧设备不同。

如果连接失败，请在腾讯云 MySQL 控制台检查：

1. 实例是否正常运行。
2. 外网连接地址是否开启。
3. 安全组是否允许数据库端口。
4. 数据库账号授权主机是否包含新设备公网 IP。
5. 数据库 `aaa_small_app` 是否存在。

正式部署 Flask 后，应优先使用同地域、同 VPC 的内网地址，并关闭不必要的数据库公网访问。

## 8. 配置 VS Code Python 解释器

在 VS Code 中按：

```text
Command + Shift + P
```

选择：

```text
Python: Select Interpreter
```

然后选择：

```text
services/api/.venv/bin/python
```

在终端验证：

```bash
cd services/api
source .venv/bin/activate
which python
```

正确结果应指向：

```text
AAA_small_app/services/api/.venv/bin/python
```

## 9. 启动完整开发环境

前端和后端是两个独立服务，需要打开两个终端。

终端一，启动 Flask：

```bash
cd ~/Desktop/AAA_small_app/services/api
uv run flask --app aaa_api:create_app run --debug
```

Flask 默认地址：

```text
http://127.0.0.1:5000
```

终端二，启动 uni-app H5：

```bash
cd ~/Desktop/AAA_small_app
npm run dev:h5
```

前端通常运行在：

```text
http://localhost:5173
```

## 10. 验证后端与数据库

浏览器打开：

```text
http://127.0.0.1:5000/
http://127.0.0.1:5000/api/v1/health
http://127.0.0.1:5000/api/v1/health/database
http://127.0.0.1:5000/test
```

数据库健康检查成功时返回：

```json
{
  "database": "connected",
  "status": "ok"
}
```

查询云数据库全部业务数据：

```bash
cd services/api
uv run python query_database.py
```

向 `test` 表追加 10 条随机数据：

```bash
uv run python seed_test_data.py
```

## 11. Git 日常同步

开始开发前：

```bash
git pull
```

完成开发后：

```bash
git status
git add .
git commit -m "描述本次修改"
git push
```

不应提交：

```text
services/api/.env
services/api/.venv/
node_modules/
dist/
__pycache__/
```

## 12. 常见问题

### `npm uniapp` 或 `npm run uniapp` 报错

使用项目中已经定义的命令：

```bash
npm run dev:h5
npm run dev:mp-weixin
```

### `pymysql` 或 `dotenv` 显示无法导入

重新选择 `services/api/.venv/bin/python`，或者执行：

```bash
cd services/api
uv sync
uv run python -c "import pymysql; import dotenv; print('OK')"
```

### Flask 无法连接数据库

依次检查：

```text
.env 配置
腾讯云外网地址和端口
新设备公网 IP 白名单
数据库账号权限
aaa_small_app 数据库是否存在
```

### `.venv` 在 VS Code 中看不到

`.venv` 是隐藏目录，通常不需要打开其内部文件。使用 `Command + Shift + P` 选择其中的 Python 解释器即可。

## 13. 恢复完成标准

满足以下条件即表示新设备配置成功：

- `npm run dev:h5` 可以启动前端。
- Flask 健康接口返回 HTTP 200。
- 数据库健康接口返回 `connected`。
- `/test` 能显示腾讯云 MySQL 中的数据。
- `git status` 可以正常查看仓库状态。
- `.env`、`.venv` 和 `node_modules` 未被 Git 跟踪。
