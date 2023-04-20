import sqlite3
import datetime


def create_table_birds(cursor: sqlite3.Cursor) -> None:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS birds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date_time TEXT NOT NULL
        )
    """)

sql_request = """
    INSERT 
        INTO birds (name, date_time) 
        VALUES (?, ?)
"""

sql_request_exist = """
    SELECT EXISTS(
        SELECT 1 
            FROM birds 
            WHERE name = ? LIMIT 1) 
"""

def log_bird(
        cursor: sqlite3.Cursor,
        bird_name: str,
        date_time: str,
) -> None:
    cursor.execute(sql_request, (bird_name, date_time))


def check_if_such_bird_already_seen(cursor: sqlite3.Cursor, bird_name: str) -> bool:
    cursor.execute(sql_request_exist, (bird_name,))
    return bool(cursor.fetchone()[0])


if __name__ == "__main__":
    print("Программа помощи ЮНатам v0.1")
    name = input("Пожалуйста введите имя птицы\n> ")
    count_str = input("Сколько птиц вы увидели?\n> ")
    count = int(count_str)
    current_time = datetime.datetime.utcnow().isoformat()

    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        create_table_birds(cursor)
        if check_if_such_bird_already_seen(cursor, name):
            print("Такую птицу мы уже наблюдали!")
        else:
            print("Такую птицу мы видим впервые!")
            log_bird(cursor, name, current_time)
