import sqlite3
from datetime import datetime, timedelta


def update_work_schedule(cursor: sqlite3.Cursor) -> None:
    cursor.execute("SELECT id, preferable_sport FROM table_friendship_employees")
    employee_sports = {row[0]: row[1] for row in cursor.fetchall()}

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sports = {'Monday': 'football', 'Tuesday': 'hockey', 'Wednesday': 'chess', 'Thursday': 'SUP-surfing',
              'Friday': 'boxing', 'Saturday': 'Dota2', 'Sunday': 'chess-boxing'}

    cursor.execute("SELECT MIN(date) FROM table_friendship_schedule")
    start_date = datetime.strptime(cursor.fetchone()[0], '%Y-%m-%d')

    date_index = 0
    employee_index = 0

    while employee_index < 356:
        current_date = start_date + timedelta(days=date_index)
        current_day = days[current_date.weekday()]

        for i in range(10):
            employee_id = employee_index + i
            if employee_id in employee_sports and employee_sports[employee_id] == sports[current_day]:
                date_index += 1
                break
        else:
            for i in range(10):
                employee_id = employee_index + i
                cursor.execute("UPDATE table_friendship_schedule SET employee_id = ? WHERE date = ?",
                               (employee_id, current_date.strftime('%Y-%m-%d')))

            date_index += 1
            employee_index += 10


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as db:
        cursor = db.cursor()
        update_work_schedule(cursor)

    db.close()