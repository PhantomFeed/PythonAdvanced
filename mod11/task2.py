import logging
import threading
import requests
import sqlite3
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URL = f'https://swapi.dev/api/people/'


def create_table(cursor: sqlite3.Cursor) -> None:
    cursor.execute('''CREATE TABLE
     IF NOT EXISTS characters 
     (id INTEGER PRIMARY KEY, name TEXT, gender TEXT, age INTEGER)''')


insert_characters = """
INSERT INTO characters (name, gender, age) VALUES (?, ?, ?)
"""


def get_characters():
    start = time.time()
    characters = []
    for i in range(1, 22):
        response = requests.get(URL + str(i))
        if response.status_code == 200:
            data = response.json()
            name, gender, age = data['name'], data['gender'], data['birth_year'] if data['birth_year'] != 'unknown' else None
            characters.append((name, gender, age))

    cursor.executemany(insert_characters, characters)

    logger.info('Done in {:.4}'.format(time.time() - start))


def get_characters_threads():
    start = time.time()
    characters = []
    threads = []
    for i in range(1, 22):
        thread = threading.Thread(target=get_character, args=(URL + str(i), characters))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    cursor.executemany(insert_characters, characters)

    logger.info('Done in {:.4}'.format(time.time() - start))


def get_character(url, characters):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name, gender, age = data['name'], data['gender'], data['birth_year'] if data['birth_year'] != 'unknown' else None
        characters.append((name, gender, age))


if __name__ == '__main__':
    with sqlite3.connect('star_wars.db') as db:
        cursor = db.cursor()
        create_table(cursor)
        get_characters_threads()
        db.commit()

    db.close()