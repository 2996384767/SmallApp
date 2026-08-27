import json
import os
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path

import pymysql
from dotenv import load_dotenv


def json_default(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, bytes):
        return f"<binary data: {len(value)} bytes>"
    return str(value)


def main():
    load_dotenv(Path(__file__).with_name(".env"))
    connection = pymysql.connect(
        host=os.environ["DB_HOST"], port=int(os.environ["DB_PORT"]),
        user=os.environ["DB_USER"], password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"], charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor, connect_timeout=8,
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            tables = [next(iter(row.values())) for row in cursor.fetchall()]
            print(f"数据库：{os.environ['DB_NAME']}")
            print(f"数据表数量：{len(tables)}")
            for table in tables:
                safe_table = table.replace("`", "``")
                cursor.execute(f"SELECT * FROM `{safe_table}`")
                rows = cursor.fetchall()
                print(f"\n=== {table} ===")
                print(json.dumps(rows, ensure_ascii=False, indent=2, default=json_default))
    finally:
        connection.close()


if __name__ == "__main__":
    main()
