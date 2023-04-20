import sqlite3

sql_request_most_effective = """
    SELECT salary 
        FROM table_effective_manager 
        WHERE name = 'Иван Совин'
"""

sql_request_salary = """
    SELECT salary 
        FROM table_effective_manager 
        WHERE name = ?
"""

sql_request_update = """
    UPDATE table_effective_manager 
        SET salary = ? 
        WHERE name = ?
"""

sql_request_del = """
    DELETE 
        FROM table_effective_manager 
        WHERE name = ?
"""


def ivan_sovin_the_most_effective(cursor: sqlite3.Cursor, name: str) -> None:
    the_most_effective_employee = cursor.execute(sql_request_most_effective).fetchone()[0]
    employee = cursor.execute(sql_request_salary, (name,)).fetchone()[0]
    if not employee:
        print(f"Сотрудник {name} не найден в базе данных!")
        return
    salary = int(employee * 1.1)
    if salary <= the_most_effective_employee:
        cursor.execute(sql_request_update, (salary, name))
        print(f"Зарплата сотрудника {name} успешно повышена до {salary} рублей!")
    else:
        cursor.execute(sql_request_del, (name,))
        print(f"Сотрудник {name} уволен!")


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as db:
        cursor = db.cursor()
        name = input('Введите имя сотрудника\n>')
        ivan_sovin_the_most_effective(cursor, name)

    db.close()


