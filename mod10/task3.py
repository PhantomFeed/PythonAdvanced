import sqlite3

with sqlite3.connect('hw_3_database.db') as db:
    cursor = db.cursor()
    result = []
    for i in range(3):
        cursor.execute(f"SELECT COUNT(id) FROM table_{i+1}")
        result.append(cursor.fetchone()[0])
        print(f'Записей в table_{i+1} - {result[i]}')

    result = cursor.execute("SELECT COUNT(DISTINCT value) FROM table_1").fetchone()[0]
    print(f'Количество уникальных записей в таблице table_1: {result}')

    result = cursor.execute("SELECT COUNT(*) FROM table_1 WHERE value IN (SELECT value FROM table_2)").fetchone()[0]
    print(f'Количество записей из таблицы table_1 в таблице table_2: {result}')

    result = cursor.execute("SELECT COUNT(*) FROM table_1 WHERE value IN (SELECT value FROM table_2) AND value IN (SELECT value FROM table_3)").fetchone()[0]
    print("Количество записей из таблицы table_1 в таблицах table_2 и table_3:", result)