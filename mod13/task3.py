import sqlite3
import datetime


def log_bird(
        cursor: sqlite3.Cursor,
        bird_name: str,
        date_time: str,
) -> None:
    cursor.execute("INSERT INTO birds (name, date_time) VALUES (?, ?)", (bird_name, date_time))


def check_if_such_bird_already_seen(cursor: sqlite3.Cursor, bird_name: str) -> bool:
    cursor.execute("SELECT EXISTS(SELECT 1 FROM birds WHERE name = ? LIMIT 1)", (bird_name,))
    return bool(cursor.fetchone()[0])


if __name__ == "__main__":
    print("Программа помощи ЮНатам v0.1")
    name = input("Пожалуйста введите имя птицы\n> ")
    count_str = input("Сколько птиц вы увидели?\n> ")
    count = int(count_str)
    right_now = datetime.datetime.utcnow().isoformat()

    with sqlite3.connect("birds.db") as connection:
        cursor = connection.cursor()
        if check_if_such_bird_already_seen(cursor, name):
            print("Такую птицу мы уже наблюдали!")
        else:
            print("Такую птицу мы видим впервые!")
            log_bird(cursor, name, right_now)
