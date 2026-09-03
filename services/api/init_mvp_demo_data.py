import os
from datetime import datetime, timedelta
from pathlib import Path

import pymysql
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash


BASE_TIME = datetime(2026, 9, 3, 9, 0, 0)
DEMO_COUNT = 100


COUNTRIES = ["泰国", "越南", "马来西亚", "印尼", "菲律宾", "乌兹别克斯坦", "哈萨克斯坦", "阿联酋"]
CATEGORIES = ["T恤", "卫衣", "POLO", "针织衫", "运动套装", "童装", "外套", "工装"]
CRAFTS = ["数码印花", "丝网印花", "刺绣", "热转印", "水洗", "扎染", "压胶", "贴标"]
FABRICS = ["180g纯棉", "220g精梳棉", "涤棉混纺", "速干面料", "针织罗纹", "抓绒布", "冰丝棉", "竹节棉"]
COLORS = ["黑 / 白 / 蓝", "白 / 灰 / 藏青", "红 / 白", "米色 / 咖色", "蓝 / 绿", "黑 / 灰", "粉 / 紫", "定制色"]
SIZES = ["S / M / L / XL / XXL", "M / L / XL", "儿童 100-150", "均码", "XS / S / M / L", "XL / XXL / XXXL"]
DEMAND_STATUSES = ["published", "published", "published", "matched", "draft", "closed"]
ORDER_STATUSES = ["接单确认", "协议确认", "生产中", "集货质检", "报关", "国际运输", "海外仓", "完成"]


def connect():
    load_dotenv(Path(__file__).with_name(".env"))
    return pymysql.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ["DB_PORT"]),
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False,
    )


def create_tables(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS factory (
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
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS demand (
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
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            KEY idx_demand_filters (status, country, category, craft)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS demand_application (
            id BIGINT PRIMARY KEY AUTO_INCREMENT,
            demand_id BIGINT NOT NULL,
            factory_id BIGINT NOT NULL,
            status VARCHAR(30) DEFAULT 'pending',
            applied_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE KEY uk_factory_demand (factory_id, demand_id),
            KEY idx_application_status (status),
            CONSTRAINT fk_application_demand
                FOREIGN KEY (demand_id) REFERENCES demand(id)
                ON DELETE CASCADE,
            CONSTRAINT fk_application_factory
                FOREIGN KEY (factory_id) REFERENCES factory(id)
                ON DELETE CASCADE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS orders (
            id BIGINT PRIMARY KEY AUTO_INCREMENT,
            order_no VARCHAR(30) UNIQUE NOT NULL,
            demand_id BIGINT NOT NULL,
            factory_id BIGINT NOT NULL,
            status VARCHAR(50),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                ON UPDATE CURRENT_TIMESTAMP,
            KEY idx_order_factory_status (factory_id, status),
            CONSTRAINT fk_order_demand
                FOREIGN KEY (demand_id) REFERENCES demand(id)
                ON DELETE CASCADE,
            CONSTRAINT fk_order_factory
                FOREIGN KEY (factory_id) REFERENCES factory(id)
                ON DELETE CASCADE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS order_progress (
            id BIGINT PRIMARY KEY AUTO_INCREMENT,
            order_id BIGINT NOT NULL,
            stage VARCHAR(50),
            description VARCHAR(255),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE KEY uk_order_stage (order_id, stage),
            CONSTRAINT fk_progress_order
                FOREIGN KEY (order_id) REFERENCES orders(id)
                ON DELETE CASCADE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS admin (
            id BIGINT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50) UNIQUE,
            password_hash VARCHAR(255),
            name VARCHAR(50),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
        """
    )


def one_based(items, number):
    return items[(number - 1) % len(items)]


def seed_factories(cursor):
    password_hash = generate_password_hash("123456")
    rows = []
    for i in range(1, DEMO_COUNT + 1):
        rows.append(
            (
                f"肃宁示范制衣厂{i:03d}",
                f"factory{i:03d}",
                password_hash,
                f"联系人{i:03d}",
                f"1380000{i:04d}",
                f"{one_based(CATEGORIES, i)} / {one_based(CATEGORIES, i + 2)}",
                f"{one_based(CRAFTS, i)} / {one_based(CRAFTS, i + 3)}",
                1 if i % 10 else 0,
                BASE_TIME + timedelta(minutes=i),
            )
        )
    cursor.executemany(
        """
        INSERT INTO factory (
            factory_name, username, password_hash, contact_name, contact_phone,
            category, craft, status, created_at
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            factory_name = VALUES(factory_name),
            password_hash = VALUES(password_hash),
            contact_name = VALUES(contact_name),
            contact_phone = VALUES(contact_phone),
            category = VALUES(category),
            craft = VALUES(craft),
            status = VALUES(status)
        """,
        rows,
    )


def seed_demands(cursor):
    rows = []
    for i in range(1, DEMO_COUNT + 1):
        category = one_based(CATEGORIES, i)
        craft = one_based(CRAFTS, i)
        country = one_based(COUNTRIES, i)
        rows.append(
            (
                f"DN260903{i:03d}",
                country,
                category,
                f"{country}{category}采购需求{i:03d}",
                300 + i * 25,
                craft,
                one_based(FABRICS, i),
                one_based(COLORS, i),
                one_based(SIZES, i),
                12 + (i % 35),
                f"演示需求{i:03d}：客户信息已审核脱敏，需注意包装和尺码准确性。",
                f"/uploads/demo/demand_{i:03d}.jpg",
                one_based(DEMAND_STATUSES, i),
                BASE_TIME + timedelta(hours=i),
            )
        )
    cursor.executemany(
        """
        INSERT INTO demand (
            demand_no, country, category, product_name, quantity, craft,
            fabric, colors, sizes, delivery_days, special_requirement,
            cover_image, status, created_at
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            country = VALUES(country),
            category = VALUES(category),
            product_name = VALUES(product_name),
            quantity = VALUES(quantity),
            craft = VALUES(craft),
            fabric = VALUES(fabric),
            colors = VALUES(colors),
            sizes = VALUES(sizes),
            delivery_days = VALUES(delivery_days),
            special_requirement = VALUES(special_requirement),
            cover_image = VALUES(cover_image),
            status = VALUES(status)
        """,
        rows,
    )


def seed_admins(cursor):
    password_hash = generate_password_hash("admin123456")
    rows = [
        (
            f"admin{i:03d}",
            password_hash,
            f"运营管理员{i:03d}",
            BASE_TIME + timedelta(minutes=i),
        )
        for i in range(1, DEMO_COUNT + 1)
    ]
    cursor.executemany(
        """
        INSERT INTO admin (username, password_hash, name, created_at)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            password_hash = VALUES(password_hash),
            name = VALUES(name)
        """,
        rows,
    )


def fetch_id_map(cursor, table, key_column, keys):
    placeholders = ", ".join(["%s"] * len(keys))
    cursor.execute(
        f"SELECT id, {key_column} FROM {table} WHERE {key_column} IN ({placeholders})",
        keys,
    )
    return {row[key_column]: row["id"] for row in cursor.fetchall()}


def seed_applications(cursor, demand_ids, factory_ids):
    rows = []
    for i in range(1, DEMO_COUNT + 1):
        rows.append(
            (
                demand_ids[f"DN260903{i:03d}"],
                factory_ids[f"factory{i:03d}"],
                "approved",
                BASE_TIME + timedelta(days=i % 14, minutes=i),
            )
        )
    cursor.executemany(
        """
        INSERT INTO demand_application (demand_id, factory_id, status, applied_at)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            status = VALUES(status),
            applied_at = VALUES(applied_at)
        """,
        rows,
    )


def seed_orders(cursor, demand_ids, factory_ids):
    rows = []
    for i in range(1, DEMO_COUNT + 1):
        rows.append(
            (
                f"OD260903{i:03d}",
                demand_ids[f"DN260903{i:03d}"],
                factory_ids[f"factory{i:03d}"],
                one_based(ORDER_STATUSES, i),
                BASE_TIME + timedelta(days=1 + i % 16, minutes=i),
            )
        )
    cursor.executemany(
        """
        INSERT INTO orders (order_no, demand_id, factory_id, status, created_at)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            demand_id = VALUES(demand_id),
            factory_id = VALUES(factory_id),
            status = VALUES(status)
        """,
        rows,
    )


def seed_progress(cursor, order_ids):
    rows = []
    for i in range(1, DEMO_COUNT + 1):
        stage = one_based(ORDER_STATUSES, i)
        rows.append(
            (
                order_ids[f"OD260903{i:03d}"],
                stage,
                f"演示订单{i:03d}当前进度：{stage}。",
                BASE_TIME + timedelta(days=2 + i % 16, minutes=i),
            )
        )
    cursor.executemany(
        """
        INSERT INTO order_progress (order_id, stage, description, created_at)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            description = VALUES(description),
            created_at = VALUES(created_at)
        """,
        rows,
    )


def print_counts(cursor):
    for table in ["factory", "demand", "demand_application", "orders", "order_progress", "admin"]:
        cursor.execute(f"SELECT COUNT(*) AS count FROM {table}")
        print(f"{table}: {cursor.fetchone()['count']}")


def main():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            create_tables(cursor)
            seed_factories(cursor)
            seed_demands(cursor)
            seed_admins(cursor)

            demand_keys = [f"DN260903{i:03d}" for i in range(1, DEMO_COUNT + 1)]
            factory_keys = [f"factory{i:03d}" for i in range(1, DEMO_COUNT + 1)]
            demand_ids = fetch_id_map(cursor, "demand", "demand_no", demand_keys)
            factory_ids = fetch_id_map(cursor, "factory", "username", factory_keys)

            seed_applications(cursor, demand_ids, factory_ids)
            seed_orders(cursor, demand_ids, factory_ids)

            order_keys = [f"OD260903{i:03d}" for i in range(1, DEMO_COUNT + 1)]
            order_ids = fetch_id_map(cursor, "orders", "order_no", order_keys)
            seed_progress(cursor, order_ids)

            connection.commit()
            print_counts(cursor)
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


if __name__ == "__main__":
    main()
