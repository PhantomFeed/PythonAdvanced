import sqlite3
import csv


def delete_wrong_fees(cursor: sqlite3.Cursor, wrong_fees_file: str) -> None:
    with open(wrong_fees_file, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            car_number, timestamp = row
            cursor.execute("DELETE FROM table_fees WHERE timestamp = ? AND truck_number = ?", (timestamp, car_number))

    print("Ошибочные штрафы успешно удалены!")


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as db:
        cursor = db.cursor()
        delete_wrong_fees(cursor, "wrong_fees.csv")

    db.close()
