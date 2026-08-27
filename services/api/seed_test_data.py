import os
import secrets
from pathlib import Path

import pymysql
from dotenv import load_dotenv


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
            cursor.execute("CREATE TABLE IF NOT EXISTS test (id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT, randomnums INT NOT NULL, PRIMARY KEY (id)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4")
            values = [(secrets.randbelow(1000) + 1,) for _ in range(10)]
            cursor.executemany("INSERT INTO test (randomnums) VALUES (%s)", values)
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


if __name__ == "__main__":
    main()
