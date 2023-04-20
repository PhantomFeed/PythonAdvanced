import sqlite3


def ivan_sovin_the_most_effective(cursor: sqlite3.Cursor, name: str) -> None:
    the_most_effective_employee = cursor.execute("SELECT salary FROM table_effective_manager WHERE name = 'Иван Совин'").fetchone()[0]
    employee = cursor.execute("SELECT salary FROM table_effective_manager WHERE name = ?", (name,)).fetchone()
    if not employee:
        print(f"Сотрудник {name} не найден в базе данных!")
        return
    salary = int(employee[0] * 1.1)
    if salary <= the_most_effective_employee:
        cursor.execute("UPDATE table_effective_manager SET salary = ? WHERE name = ?", (salary, name))
        print(f"Зарплата сотрудника {name} успешно повышена до {salary} рублей!")
    else:
        cursor.execute("DELETE FROM table_effective_manager WHERE name = ?", (name,))
        print(f"Сотрудник {name} уволен!")


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as db:
        cursor = db.cursor()
        name = input('Введите имя сотрудника\n>')
        ivan_sovin_the_most_effective(cursor, name)
    db.close()


