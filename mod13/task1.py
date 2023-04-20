import sqlite3

sql_request = """
    SELECT COUNT(*)
        FROM(SELECT *
        FROM table_truck_with_vaccine)
        WHERE truck_number = ? AND temperature_in_celsius NOT BETWEEN 16 and 20
        """


def check_if_vaccine_has_spoiled(
        cursor: sqlite3.Cursor,
        truck_number: str
) -> bool:
    result = cursor.execute(sql_request, (truck_number,)).fetchone()[0]
    if result >= 3:
        print("Вакцина испорчена")
        return False
    else:
        print("Вакцина в порядке")
        return True


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as db:
        cursor = db.cursor()
        truck_number = input('Введите номер грузовика: ')
        vaccine = check_if_vaccine_has_spoiled(cursor, truck_number)

    db.close()