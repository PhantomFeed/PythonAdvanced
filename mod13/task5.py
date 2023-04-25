import sqlite3
import random

# Список стран
countries = ["Англия", "Германия", "Испания", "Италия", "Франция", "Португалия", "Нидерланды", "Россия", "Украина",
             "Швеция", "Швейцария", "Турция", "Дания", "Бельгия", "Австрия", "Чехия", "Польша", "Уэльс", "Хорватия",
             "Словакия", "Северная Македония", "Шотландия", "Финляндия", "Венгрия"]

# Список уровней команд
levels = ["Сильная", "Средняя", "Слабая"]


def generate_test_data(cursor: sqlite3.Cursor, number_of_groups: int) -> None:
    commands = []
    for i in range(number_of_groups * 4):
        command_name = f"Команда {i + 1}"
        country = random.choice(countries)
        if i % 4 == 0:
            level = levels[0]
        elif i % 4 == 1 or i % 4 == 2:
            level = levels[1]
        else:
            level = levels[2]
        commands.append((i + 1, command_name, country, level))
    random.shuffle(commands)

    cursor.execute("DELETE FROM uefa_commands")
    cursor.executemany("INSERT INTO uefa_commands (command_number, command_name, command_country, command_level) VALUES (?, ?, ?, ?)", commands)

    groups = [[] for x in range(number_of_groups)]
    strong_commands = [command for command in commands if command[3] == "Сильная"]
    medium_commands = [command for command in commands if command[3] == "Средняя"]
    weak_commands = [command for command in commands if command[3] == "Слабая"]
    for i in range(number_of_groups):
        groups[i].append(random.choice(strong_commands))
        strong_commands.remove(groups[i][-1])
        groups[i].extend(random.sample(medium_commands, 2))
        medium_commands.remove(groups[i][-1])
        medium_commands.remove(groups[i][-2])
        groups[i].append(random.choice(weak_commands))
        weak_commands.remove(groups[i][-1])
        random.shuffle(groups[i])

    draw = [(team[0], i + 1) for i, group in enumerate(groups) for team in group]
    cursor.execute("DELETE FROM uefa_draw")
    cursor.executemany("INSERT INTO uefa_draw (command_number, group_number) VALUES (?, ?)", draw)

    print(f"Данные для {number_of_groups} групп успешно сгенерированы!")


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as db:
        cursor = db.cursor()
        count = int(input('Введите количество комманд от 4 до 16: '))
        generate_test_data(cursor, count)

    db.close()
