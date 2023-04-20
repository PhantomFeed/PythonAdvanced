import sqlite3


def check_if_vaccine_has_spoiled(
        cursor: sqlite3.Cursor,
        truck_number: str
) -> bool:
    cursor.execute("""
        SELECT *
        FROM table_truck_with_vaccine
        WHERE truck_number = ?
    """, (truck_number,))
    rows = cursor.fetchall()

    for i in range(len(rows) - 2):
        if rows[i][3] < -20 or rows[i][3] > -16:
            if rows[i + 1][3] - rows[i][3] >= 3 and rows[i + 2][3] - rows[i][3] >= 3:
                print("Вакцина испорчена")
                return True

    print("Вакцина в порядке")
    return False


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as db:
        cursor = db.cursor()
        truck_number = input('Введите номер грузовика: ')
        vaccine = check_if_vaccine_has_spoiled(cursor, truck_number)