import sqlite3
from datetime import datetime, timedelta


sql_request_insert_in_schedule = """
    INSERT INTO table_friendship_schedule (employee_id, date)
        VALUES (?, ?); 
"""

def update_work_schedule(cursor: sqlite3.Cursor) -> None:
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sports = ['футбол', 'хоккей', 'шахматы', 'SUP сёрфинг', 'бокс', 'Dota2', 'шах-бокс']

    cursor.execute("DELETE FROM table_friendship_schedule")
    cursor.execute("SELECT * FROM table_friendship_employees")
    employees = cursor.fetchall()
    work_days = {}
    dates = {}
    current_date = datetime.strptime("2020-01-01", "%Y-%m-%d").date()

    for i in range(366):
        current_day = days[current_date.weekday()]
        for employee in employees:
            employee_id = employee[0]
            busy_day = days[sports.index(employee[2])]
            if current_day == busy_day:
                continue

            if employee_id not in work_days:
                work_days[employee_id] = 0
            work_days[employee_id] += 1
            cursor.execute(sql_request_insert_in_schedule, (employee_id, current_date))
            if current_date not in dates:
                dates[current_date] = 0
            dates[current_date] += 1
            if work_days[employee_id] == 11:
                employees.pop(employees.index(employee))
            if dates[current_date] == 10:
                current_date += timedelta(days=1)
                break


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as db:
        cursor = db.cursor()
        update_work_schedule(cursor)

    db.close()