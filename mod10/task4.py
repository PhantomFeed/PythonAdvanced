import sqlite3

with sqlite3.connect('hw_4_database.db') as db:
    cursor = db.cursor()
    result = cursor.execute("SELECT COUNT(*) FROM salaries WHERE salary < 5000").fetchone()[0]
    print(f"Количество людей, находящихся за чертой бедности: {result}")

    result = cursor.execute("SELECT AVG(salary) FROM salaries").fetchone()[0]
    print(f"Средняя зарплата на острове: {result}")

    array = cursor.execute("SELECT salary FROM salaries ORDER BY salary").fetchall()
    result = array[(len(array) + 1) // 2][0]
    print(f"Медианная зарплата на острове: {result}")

    cursor.execute("SELECT COUNT (*) FROM salaries")
    count = cursor.fetchone()[0]
    cursor.execute(f"SELECT SUM(salary) FROM (SELECT * FROM salaries ORDER BY salary DESC LIMIT 0.1 * {count})")
    T = cursor.fetchone()[0]
    cursor.execute(f"SELECT SUM(salary) - {T} FROM salaries")
    K = cursor.fetchone()[0]
    print(f"Социальное неравенство на острове: {round(T * 100 / K, 2)}")

    db.close()