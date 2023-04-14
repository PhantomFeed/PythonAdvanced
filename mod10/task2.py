import sqlite3

with sqlite3.connect('hw_2_database.db') as db:
    cursor = db.cursor()
    result = cursor.execute("SELECT * FROM table_checkout ORDER BY sold_count DESC").fetchone()[0]
    print(f'Чаще всего покупают телефоны цвета - {result}')

    red = cursor.execute("SELECT * FROM table_checkout WHERE phone_color = 'Red'").fetchone()
    blue = cursor.execute("SELECT * FROM table_checkout WHERE phone_color = 'Blue'").fetchone()

    if red[1] > blue[1]:
        print(f'Чаще покупают телефоны цвета - {red[0]}')
    elif red[1] < blue[1]:
        print(f'Чаще покупают телефоны цвета - {blue[0]}')
    else:
        print(f'Телефоны цветов {blue[0]} и {red[0]} покупают одинаково')

    result = cursor.execute("SELECT * FROM table_checkout ORDER BY sold_count").fetchone()[0]
    print(f'Самый непопулярный цвет телефона - {result}')

    db.close()
